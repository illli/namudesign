(function () {
  "use strict";

  var root = document.documentElement;
  var themeState = window.NAMU_THEME || {};
  var storageKey = themeState.storageKey || "namu-theme";
  var media = themeState.media || window.matchMedia("(prefers-color-scheme: dark)");
  var themeToggle = document.querySelector(".theme-toggle");
  var menuToggle = document.querySelector(".menu-toggle");
  var siteNav = document.querySelector(".site-nav");

  function readPreference() {
    var value = null;

    try {
      value = window.localStorage.getItem(storageKey);
    } catch (_error) {
      value = null;
    }

    return value === "light" || value === "dark" ? value : null;
  }

  function applyTheme(theme, preference) {
    root.dataset.theme = theme;
    root.dataset.themePreference = preference || "system";
    root.style.colorScheme = theme;

    if (themeToggle) {
      themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
      themeToggle.querySelector("span").textContent = theme === "dark" ? "LIGHT" : "DARK";
    }
  }

  function applyStoredOrSystemTheme() {
    var preference = readPreference();
    applyTheme(preference || (media.matches ? "dark" : "light"), preference);
  }

  if (themeToggle) {
    applyStoredOrSystemTheme();

    themeToggle.addEventListener("click", function () {
      var nextTheme = root.dataset.theme === "dark" ? "light" : "dark";

      try {
        window.localStorage.setItem(storageKey, nextTheme);
      } catch (_error) {
        // The selected theme still applies for the current page when storage is unavailable.
      }

      applyTheme(nextTheme, nextTheme);
    });
  }

  function handleSystemThemeChange() {
    if (!readPreference()) {
      applyTheme(media.matches ? "dark" : "light", null);
    }
  }

  if (typeof media.addEventListener === "function") {
    media.addEventListener("change", handleSystemThemeChange);
  } else if (typeof media.addListener === "function") {
    media.addListener(handleSystemThemeChange);
  }

  window.addEventListener("storage", function (event) {
    if (event.key === storageKey || event.key === null) {
      applyStoredOrSystemTheme();
    }
  });

  function setMenuOpen(open) {
    if (!menuToggle || !siteNav) return;

    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.classList.toggle("is-open", open);
    siteNav.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
  }

  if (menuToggle && siteNav) {
    menuToggle.addEventListener("click", function () {
      setMenuOpen(menuToggle.getAttribute("aria-expanded") !== "true");
    });

    siteNav.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        setMenuOpen(false);
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menuToggle.getAttribute("aria-expanded") === "true") {
        setMenuOpen(false);
        menuToggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth >= 768) {
        setMenuOpen(false);
      }
    });
  }
})();
