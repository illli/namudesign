#!/usr/bin/env python3
"""Build the eight localized NAMU pages using only the Python standard library."""

from __future__ import annotations

import html
import json
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
SOURCE_ASSETS = ROOT / "src" / "assets"
OUTPUT = ROOT / "dist"


ROOT_INDEX = """<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NAMU DESIGN</title>
    <meta name="robots" content="noindex">
    <meta http-equiv="refresh" content="0; url=/zh/">
    <link rel="canonical" href="https://namu.design/zh/">
  </head>
  <body><p><a href="/zh/">进入 NAMU DESIGN</a> · <a href="/en/">English</a></p></body>
</html>
"""


NOT_FOUND = """<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>404 | NAMU DESIGN</title>
    <meta name="robots" content="noindex">
    <link rel="stylesheet" href="/assets/css/site.css">
  </head>
  <body><main class="error-page"><p>404</p><h1>页面不存在</h1><a href="/zh/">返回首页 / Back home</a></main></body>
</html>
"""


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def template(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def image_figure(image: dict, class_name: str, eager: bool = False) -> str:
    loading = "eager" if eager else "lazy"
    priority = ' fetchpriority="high"' if eager else ""
    return (
        f'        <figure class="{class_name}"><img src="{esc(image["src"])}" '
        f'alt="{esc(image["alt"])}" loading="{loading}"{priority}></figure>'
    )


def render_home(page: dict, locale: dict, routes: dict) -> str:
    gallery = "\n".join(
        image_figure(image, "home-gallery-item", eager=index == 0)
        for index, image in enumerate(page["images"])
    )
    projects = []
    for project in page["projects"]:
        url = routes[project["route"]][locale["locale"]]
        projects.append(
            "\n".join(
                [
                    f'        <a class="project-card" href="{esc(url)}">',
                    f'          <figure class="project-image"><img src="{esc(project["image"])}" alt="" loading="lazy"></figure>',
                    '          <div class="project-copy">',
                    f'            <p>{esc(project["name"])}</p>',
                    f'            <h3>{esc(project["title"])}</h3>',
                    f'            <span>{esc(locale["labels"]["view_project"])}</span>',
                    "          </div>",
                    "        </a>",
                ]
            )
        )
    tags = "\n".join(f"        <li>{esc(item)}</li>" for item in page["tags"])
    return template("home.html").format(
        eyebrow=esc(page["eyebrow"]),
        heading=esc(page["heading"]),
        intro=esc(page["intro"]),
        work_label=esc(locale["labels"]["work"]),
        gallery_html=gallery,
        tags_html=tags,
        projects_html="\n".join(projects),
    )


def render_info(page: dict) -> str:
    paragraphs = "\n".join(f"        <p>{esc(item)}</p>" for item in page["body"])
    client_items = "\n".join(
        f'            <li><img src="{esc(client["src"])}" alt="{esc(client["alt"])}" loading="lazy"></li>'
        for client in page["clients"]
    )
    clients = ""
    if client_items:
        clients = "\n".join(
            [
                '        <section class="clients">',
                f'          <h2>{esc(page["clients_heading"])}</h2>',
                '          <ul class="client-list">',
                client_items,
                "          </ul>",
                "        </section>",
            ]
        )
    team_rows = "\n".join(
        "\n".join(
            [
                '            <li class="team-row">',
                f'              <strong>{esc(member["name"])}</strong>',
                f'              <span>{esc(member["role_zh"])}</span>',
                f'              <span>{esc(member["role_en"])}</span>',
                "            </li>",
            ]
        )
        for member in page["team"]
    )
    service_rows = "\n".join(
        "\n".join(
            [
                '            <li class="service-row">',
                f'              <strong>{esc(service["name"])}</strong>',
                f'              <span>{esc(service["description"])}</span>',
                "            </li>",
            ]
        )
        for service in page["services"]
    )
    return template("info.html").format(
        eyebrow=esc(page["eyebrow"]),
        heading=esc(page["heading"]),
        body_html=paragraphs,
        studio_image_src=esc(page["studio_image"]["src"]),
        studio_image_alt=esc(page["studio_image"]["alt"]),
        team_heading=esc(page["team_heading"]),
        team_html=team_rows,
        client_statement=esc(page["client_statement"]),
        clients_html=clients,
        services_heading=esc(page["services_heading"]),
        services_html=service_rows,
    )


def render_case(page: dict, work_url: str, back_label: str) -> str:
    sections = []
    for section_index, section in enumerate(page["sections"]):
        media = "\n".join(
            image_figure(image, "case-gallery-item", eager=section_index == 0 and image_index == 0)
            for image_index, image in enumerate(section["images"])
        )
        description = f'<p>{esc(section["description"])}</p>' if section.get("description") else ""
        sections.append(
            "\n".join(
                [
                    '        <section class="case-section">',
                    '          <header class="case-section-header">',
                    f'            <p>{esc(section["label"])}</p>',
                    f'            <h2>{esc(section["title"])}</h2>',
                    f'            {description}',
                    "          </header>",
                    '          <div class="case-gallery">',
                    media,
                    "          </div>",
                    "        </section>",
                ]
            )
        )
    return template("case-study.html").format(
        eyebrow=esc(page["eyebrow"]),
        heading=esc(page["heading"]),
        summary=esc(page["summary"]),
        facts_html="".join(f"<span>{esc(item)}</span>" for item in page["facts"]),
        sections_html="\n".join(sections),
        work_url=esc(work_url),
        back_to_work_label=esc(back_label),
    )


def output_file(route: str) -> Path:
    return OUTPUT / route.strip("/") / "index.html"


def build() -> None:
    site = load_json(CONTENT / "site.json")
    layout = template("layout.html")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    if SOURCE_ASSETS.exists():
        shutil.copytree(SOURCE_ASSETS, OUTPUT / "assets")

    count = 0
    for locale_name in site["locales"]:
        locale = load_json(CONTENT / f"{locale_name}.json")
        other_locale = next(item for item in site["locales"] if item != locale_name)
        other_content = load_json(CONTENT / f"{other_locale}.json")

        for page_key, page in locale["pages"].items():
            route = site["routes"][page_key][locale_name]
            work_url = site["routes"]["home"][locale_name] + "#work"
            if page["template"] == "home":
                body = render_home(page, locale, site["routes"])
            elif page["template"] == "info":
                body = render_info(page)
            elif page["template"] == "case-study":
                body = render_case(page, work_url, locale["labels"]["back_to_work"])
            else:
                raise ValueError(f"Unknown template: {page['template']}")

            canonical = site["origin"] + route
            other_url = site["routes"][page_key][other_locale]
            document = layout.format(
                html_lang=esc(locale["html_lang"]),
                page_title=esc(page["title"]),
                page_description=esc(page["description"]),
                canonical_url=esc(canonical),
                zh_url=esc(site["origin"] + site["routes"][page_key]["zh"]),
                en_url=esc(site["origin"] + site["routes"][page_key]["en"]),
                default_url=esc(site["origin"] + site["routes"][page_key][site["default_locale"]]),
                og_type="website" if page_key in {"home", "info"} else "article",
                brand=esc(site["brand"]),
                page_key=esc(page_key),
                skip_label=esc(locale["labels"]["skip"]),
                theme_label=esc(locale["labels"]["theme"]),
                home_url=esc(site["routes"]["home"][locale_name]),
                info_url=esc(site["routes"]["info"][locale_name]),
                info_current=' aria-current="page"' if page_key == "info" else "",
                other_locale_url=esc(other_url),
                other_html_lang=esc(other_content["html_lang"]),
                other_language_name=esc(locale["other_language_name"]),
                year=datetime.now().year,
                body=body.rstrip(),
                footer_address_label=esc(locale["footer"]["address_label"]),
                footer_address_zh=esc(site["contact"]["address_zh"]),
                footer_address_en_line_1=esc(site["contact"]["address_en_line_1"]),
                footer_address_en_line_2=esc(site["contact"]["address_en_line_2"]),
                footer_phone_label=esc(locale["footer"]["phone_label"]),
                footer_consult_label=esc(locale["footer"]["consult_label"]),
                footer_phone=esc(site["contact"]["phone_display"]),
                footer_phone_href=esc(site["contact"]["phone_href"]),
                footer_email=esc(site["contact"]["email"]),
                brand_compact=esc(site["brand"].replace(" ", "")),
            )
            destination = output_file(route)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(document, encoding="utf-8")
            count += 1

    (OUTPUT / "index.html").write_text(ROOT_INDEX, encoding="utf-8")
    (OUTPUT / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    (OUTPUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://namu.design/sitemap.xml\n",
        encoding="utf-8",
    )
    sitemap_urls = [
        site["origin"] + localized[locale]
        for localized in site["routes"].values()
        for locale in site["locales"]
    ]
    sitemap = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            *(f"  <url><loc>{esc(url)}</loc></url>" for url in sitemap_urls),
            "</urlset>",
            "",
        ]
    )
    (OUTPUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    print(f"Built {count} localized pages in {OUTPUT}")


if __name__ == "__main__":
    build()
