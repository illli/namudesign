(function () {
  "use strict";

  var storageKey = "namu-theme";
  var root = document.documentElement;
  var media = window.matchMedia("(prefers-color-scheme: dark)");
  var preference = null;

  try {
    preference = window.localStorage.getItem(storageKey);
  } catch (_error) {
    preference = null;
  }

  if (preference !== "light" && preference !== "dark") {
    preference = null;
  }

  var theme = preference || (media.matches ? "dark" : "light");
  root.dataset.theme = theme;
  root.dataset.themePreference = preference || "system";
  root.style.colorScheme = theme;

  window.NAMU_THEME = {
    media: media,
    storageKey: storageKey
  };
})();

