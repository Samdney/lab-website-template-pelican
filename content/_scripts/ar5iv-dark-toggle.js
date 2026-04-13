/*
  Paper pages use the same unified theme system as the rest of the site.
  This file remains as a compatibility bridge for pages that still include it.
*/

(function () {
  const root = document.documentElement;

  function applyFromStoredValue() {
    const stored = window.localStorage.getItem("dark-mode");
    if (stored === "true" || stored === "false") {
      root.dataset.dark = stored;
    }
  }

  applyFromStoredValue();

  function init() {
    const button = document.getElementById("theme-toggle");
    if (!button) return;

    button.addEventListener("click", function () {
      if (window.siteTheme && typeof window.siteTheme.current === "function") {
        const isDark = window.siteTheme.current() === "dark";
        if (isDark) {
          window.siteTheme.setLight();
        } else {
          window.siteTheme.setDark();
        }
      } else {
        const nextDark = root.dataset.dark !== "true";
        root.dataset.dark = String(nextDark);
        window.localStorage.setItem("dark-mode", String(nextDark));
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
