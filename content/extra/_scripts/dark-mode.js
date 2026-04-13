/*
  Unified light/dark mode handling for the whole site.
  Source of truth:
  - html[data-dark] = "true" | "false"
  - localStorage["dark-mode"] = "true" | "false"
*/

(function () {
  const STORAGE_KEY = "dark-mode";
  const root = document.documentElement;

  function getSystemDarkPreference() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function getStoredDarkMode() {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    if (stored === "true") return true;
    if (stored === "false") return false;
    return null;
  }

  function getPreferredDarkMode() {
    const stored = getStoredDarkMode();
    return stored === null ? getSystemDarkPreference() : stored;
  }

  function applyDarkMode(isDark) {
    const value = String(Boolean(isDark));
    root.dataset.dark = value;

    document.querySelectorAll(".dark-toggle").forEach((toggle) => {
      if ("checked" in toggle) {
        toggle.checked = isDark;
      }
    });

    const themeToggleButton = document.getElementById("theme-toggle");
    if (themeToggleButton) {
      themeToggleButton.setAttribute(
        "aria-label",
        isDark ? "Switch to light mode" : "Switch to dark mode"
      );
      themeToggleButton.setAttribute("aria-pressed", isDark ? "true" : "false");
    }
  }

  function saveDarkMode(isDark) {
    window.localStorage.setItem(STORAGE_KEY, String(Boolean(isDark)));
  }

  function setDarkMode(isDark, persist = true) {
    applyDarkMode(isDark);
    if (persist) {
      saveDarkMode(isDark);
    }
  }

  function toggleDarkMode() {
    setDarkMode(root.dataset.dark !== "true");
  }

  // Apply as early as possible.
  applyDarkMode(getPreferredDarkMode());

  function init() {
    document.querySelectorAll(".dark-toggle").forEach((toggle) => {
      toggle.addEventListener("change", (event) => {
        setDarkMode(Boolean(event.target.checked));
      });
    });

    const themeToggleButton = document.getElementById("theme-toggle");
    if (themeToggleButton) {
      themeToggleButton.addEventListener("click", () => {
        toggleDarkMode();
      });
    }

    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    const handleSystemChange = (event) => {
      if (getStoredDarkMode() === null) {
        applyDarkMode(event.matches);
      }
    };

    if (typeof mediaQuery.addEventListener === "function") {
      mediaQuery.addEventListener("change", handleSystemChange);
    } else if (typeof mediaQuery.addListener === "function") {
      mediaQuery.addListener(handleSystemChange);
    }

    applyDarkMode(getPreferredDarkMode());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Backward-compatible inline handler used by current template markup
  window.onDarkToggleChange = function (event) {
    setDarkMode(Boolean(event.target.checked));
  };

  // Optional helper for debugging from the console
  window.siteTheme = {
    setLight() {
      setDarkMode(false);
    },
    setDark() {
      setDarkMode(true);
    },
    reset() {
      window.localStorage.removeItem(STORAGE_KEY);
      applyDarkMode(getSystemDarkPreference());
    },
    current() {
      return root.dataset.dark === "true" ? "dark" : "light";
    },
  };
})();
