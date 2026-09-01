#!/usr/bin/env python3
"""Validate generated pages, local dependencies, links and sensitive-file hygiene."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FORBIDDEN_HOST_MARKERS = ("figma.com", "figmausercontent.com", "cdn.jsdelivr.net", "unpkg.com")


class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_lang = ""
        self.title = ""
        self._in_title = False
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.resources: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.html_lang = values.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.meta.append(values)
        elif tag == "a":
            self.links.append(values)
        elif tag == "img":
            self.images.append(values)
            self.resources.append((tag, values.get("src", "")))
        elif tag == "script" and values.get("src"):
            self.resources.append((tag, values["src"]))
        elif tag == "link" and "stylesheet" in values.get("rel", "").split():
            self.resources.append((tag, values.get("href", "")))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def load_site() -> dict:
    return json.loads((ROOT / "content" / "site.json").read_text(encoding="utf-8"))


def local_target(url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = parsed.path
    if path.startswith("/"):
        target = DIST / path.lstrip("/")
    else:
        return None
    if path.endswith("/"):
        target /= "index.html"
    return target


def check(allow_missing_assets: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    site = load_site()
    expected = {
        (locale, page_key): DIST / route.strip("/") / "index.html"
        for page_key, localized in site["routes"].items()
        for locale, route in localized.items()
    }
    actual = set(DIST.glob("**/index.html")) - {DIST / "index.html"}
    expected_files = set(expected.values())
    for path in sorted(expected_files - actual):
        errors.append(f"missing generated page: {path.relative_to(ROOT)}")
    for path in sorted(actual - expected_files):
        errors.append(f"unexpected generated page: {path.relative_to(ROOT)}")

    for required in ("index.html", "404.html", "robots.txt", "sitemap.xml"):
        if not (DIST / required).exists():
            errors.append(f"missing generated file: dist/{required}")

    sitemap_source = (DIST / "sitemap.xml").read_text(encoding="utf-8") if (DIST / "sitemap.xml").exists() else ""
    for localized in site["routes"].values():
        for route in localized.values():
            url = site["origin"] + route
            if f"<loc>{url}</loc>" not in sitemap_source:
                errors.append(f"sitemap missing URL: {url}")

    descriptions: set[str] = set()
    for (locale, page_key), path in expected.items():
        if not path.exists():
            continue
        parser = Document()
        source = path.read_text(encoding="utf-8")
        parser.feed(source)
        label = str(path.relative_to(ROOT))
        expected_lang = "zh-CN" if locale == "zh" else "en"
        if parser.html_lang != expected_lang:
            errors.append(f"{label}: expected lang={expected_lang!r}")
        if not parser.title.strip():
            errors.append(f"{label}: missing title")

        description = next((item.get("content", "") for item in parser.meta if item.get("name") == "description"), "")
        if not description:
            errors.append(f"{label}: missing meta description")
        elif description in descriptions:
            errors.append(f"{label}: duplicate meta description")
        descriptions.add(description)

        head_links = []
        head_parser = HTMLParser()
        del head_parser
        # Parse head link elements separately with a tiny collector.
        class LinkCollector(HTMLParser):
            def __init__(self) -> None:
                super().__init__()
                self.items: list[dict[str, str]] = []
            def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
                if tag == "link":
                    self.items.append({key: value or "" for key, value in attrs})
        collector = LinkCollector()
        collector.feed(source)
        head_links = collector.items
        route = site["routes"][page_key][locale]
        canonical = site["origin"] + route
        canonical_values = [item.get("href") for item in head_links if item.get("rel") == "canonical"]
        if canonical_values != [canonical]:
            errors.append(f"{label}: incorrect canonical URL")
        alternates = {item.get("hreflang"): item.get("href") for item in head_links if item.get("rel") == "alternate"}
        expected_alternates = {
            "zh-CN": site["origin"] + site["routes"][page_key]["zh"],
            "en": site["origin"] + site["routes"][page_key]["en"],
            "x-default": site["origin"] + site["routes"][page_key][site["default_locale"]],
        }
        if alternates != expected_alternates:
            errors.append(f"{label}: incorrect hreflang mapping")

        for image in parser.images:
            if "alt" not in image:
                errors.append(f"{label}: image missing alt attribute: {image.get('src', '')}")
            src = image.get("src", "").split("?", 1)[0]
            is_content_image = (
                src.startswith("/assets/images/fotile/")
                or src.startswith("/assets/images/farfetch-china/")
                or src.startswith("/assets/images/info/team/")
                or src == "/assets/images/info/studio.png"
            )
            if is_content_image and "media-image" not in image.get("class", "").split():
                errors.append(f"{label}: content image missing loading placeholder: {src}")
        for tag, url in parser.resources:
            if any(marker in url.lower() for marker in FORBIDDEN_HOST_MARKERS):
                errors.append(f"{label}: forbidden remote dependency: {url}")
            target = local_target(url)
            if target and not target.exists():
                message = f"{label}: missing local {tag} resource: {url}"
                (warnings if allow_missing_assets else errors).append(message)
        for link in parser.links:
            url = link.get("href", "")
            if not url or url.startswith(("#", "mailto:", "tel:")):
                continue
            target = local_target(url)
            if target and not target.exists():
                errors.append(f"{label}: broken internal link: {url}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "dist" in path.parts:
            continue
        if path.suffix.lower() in {".pem", ".key"}:
            errors.append(f"sensitive file must not be in the project: {path.relative_to(ROOT)}")
        if path.stat().st_size <= 1_000_000:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            private_key_marker = "-----BEGIN " + "PRIVATE KEY-----"
            rsa_key_marker = "-----BEGIN RSA " + "PRIVATE KEY-----"
            if private_key_marker in text or rsa_key_marker in text:
                errors.append(f"private key content found: {path.relative_to(ROOT)}")

    node = shutil.which("node")
    scripts = sorted((ROOT / "src" / "assets" / "js").glob("*.js"))
    if node:
        for script in scripts:
            result = subprocess.run([node, "--check", str(script)], capture_output=True, text=True)
            if result.returncode:
                errors.append(f"JavaScript syntax error in {script.relative_to(ROOT)}: {result.stderr.strip()}")
    elif scripts:
        warnings.append("node is unavailable; JavaScript syntax check skipped")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-missing-assets", action="store_true", help="report missing local assets as warnings")
    args = parser.parse_args()
    errors, warnings = check(args.allow_missing_assets)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Check passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
