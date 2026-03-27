import { translate } from "@docusaurus/Translate";
import { iconNoResults } from "./icons";
import styles from "./SearchBar.module.css";
import { POPULAR_SEARCHES, getRecentSearches } from "./searchConstants";

// ── Quick-search links (recent + popular) shown when input is empty ───────────
function renderQuickSearches() {
    const recent  = typeof localStorage !== "undefined" ? getRecentSearches() : [];
    const popular = POPULAR_SEARCHES.filter((p) => !recent.includes(p)).slice(0, 6 - Math.min(recent.length, 4));

    const recentHtml = recent.length > 0
        ? `<div class="search-quick-group">
             <div class="search-quick-label">Recent</div>
             <div class="search-quick-items">
               ${recent.map((s) => `<a href="/search?q=${encodeURIComponent(s)}" class="search-quick-term search-quick-term--recent">🕐 ${s}</a>`).join("")}
             </div>
           </div>`
        : "";

    const popularHtml = popular.length > 0
        ? `<div class="search-quick-group">
             <div class="search-quick-label">Popular searches</div>
             <div class="search-quick-items">
               ${popular.map((s) => `<a href="/search?q=${encodeURIComponent(s)}" class="search-quick-term search-quick-term--popular">🔍 ${s}</a>`).join("")}
             </div>
           </div>`
        : "";

    return `<div class="search-quick-container">${recentHtml}${popularHtml}</div>`;
}

// ── No-results state shown when a query returns nothing ───────────────────────
function renderNoResults(query) {
    const suggestions = POPULAR_SEARCHES.slice(0, 4)
        .map((s) => `<a href="/search?q=${encodeURIComponent(s)}" class="search-quick-term search-quick-term--popular">🔍 ${s}</a>`)
        .join("");

    return `<span class="${styles.noResults}">
        <span class="${styles.noResultsIcon}">${iconNoResults}</span>
        <span>${translate({ id: "theme.SearchBar.noResultsText", message: "No results" })}</span>
        <div class="search-no-results-help">
          <p class="search-no-results-hint">Try a different term or browse popular topics:</p>
          <div class="search-quick-items">${suggestions}</div>
          <p class="search-no-results-links">
            <a href="https://www.visualcron.com/forum.aspx" target="_blank" rel="noopener noreferrer">Community Forum</a>
            &nbsp;·&nbsp;
            <a href="https://www.visualcron.com/support.aspx" target="_blank" rel="noopener noreferrer">Support</a>
          </p>
        </div>
      </span>`;
}

export function EmptyTemplate() {
    if (process.env.NODE_ENV === "production") {
        // Determine whether the search bar currently has text
        const inputEl = typeof document !== "undefined"
            ? document.querySelector(".navbar__search-input")
            : null;
        const hasQuery = inputEl && inputEl.value.trim().length > 0;

        return hasQuery ? renderNoResults(inputEl.value) : renderQuickSearches();
    }
    return `<span class="${styles.noResults}">⚠️ The search index is only available when you run docusaurus build!</span>`;
}
