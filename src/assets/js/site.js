(function () {
  "use strict";

  var root = document.documentElement;
  var themeState = window.NAMU_THEME || {};
  var storageKey = themeState.storageKey || "namu-theme";
  var media = themeState.media || window.matchMedia("(prefers-color-scheme: dark)");
  var themeToggle = document.querySelector(".theme-toggle");

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

  document.querySelectorAll(".home-gallery").forEach(function (gallery) {
    var resumeTimer = null;

    function pauseMotion() {
      window.clearTimeout(resumeTimer);
      gallery.classList.add("is-interacting");
    }

    function resumeMotion() {
      window.clearTimeout(resumeTimer);
      resumeTimer = window.setTimeout(function () {
        gallery.classList.remove("is-interacting");
      }, 240);
    }

    gallery.addEventListener("pointerdown", pauseMotion, { passive: true });
    gallery.addEventListener("pointerup", resumeMotion, { passive: true });
    gallery.addEventListener("pointercancel", resumeMotion, { passive: true });
  });

})();
