import React, { useCallback, useEffect, useRef, useState } from "react";
import clsx from "clsx";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useIsBrowser from "@docusaurus/useIsBrowser";
import { useHistory, useLocation } from "@docusaurus/router";
import { translate } from "@docusaurus/Translate";
import { fetchIndexes } from "./fetchIndexes";
import { SearchSourceFactory } from "@easyops-cn/docusaurus-search-local/dist/client/client/utils/SearchSourceFactory";
import { SuggestionTemplate } from "./SuggestionTemplate";
import { EmptyTemplate } from "./EmptyTemplate";
import {
    searchResultLimits,
    Mark,
    searchBarShortcut,
    searchBarShortcutHint,
    searchBarPosition,
    indexDocs,
} from "@easyops-cn/docusaurus-search-local/dist/client/client/utils/proxiedGenerated";
import LoadingRing from "@easyops-cn/docusaurus-search-local/dist/client/client/theme/LoadingRing/LoadingRing";
import styles from "./SearchBar.module.css";
import { expandSynonyms, addRecentSearch } from "./searchConstants";

async function fetchAutoCompleteJS() {
    const autoCompleteModule = await import("@easyops-cn/autocomplete.js");
    const autoComplete = autoCompleteModule.default;
    if (autoComplete.noConflict) {
        autoComplete.noConflict();
    } else if (autoCompleteModule.noConflict) {
        autoCompleteModule.noConflict();
    }
    return autoComplete;
}

const SEARCH_PARAM_HIGHLIGHT = "_highlight";

export default function SearchBar({ handleSearchBarToggle }) {
    const isBrowser = useIsBrowser();
    const {
        siteConfig: { baseUrl },
    } = useDocusaurusContext();

    const history = useHistory();
    const location = useLocation();
    const searchBarRef = useRef(null);
    const indexStateMap = useRef(new Map());
    const focusAfterIndexLoaded = useRef(false);
    const [loading, setLoading] = useState(false);
    const [inputChanged, setInputChanged] = useState(false);
    const [inputValue, setInputValue] = useState("");
    const search = useRef(null);
    const [focused, setFocused] = useState(false);

    const loadIndex = useCallback(async () => {
        if (indexStateMap.current.get("default")) return;
        indexStateMap.current.set("default", "loading");
        search.current?.autocomplete.destroy();
        setLoading(true);

        const [{ wrappedIndexes, zhDictionary }, autoComplete] = await Promise.all([
            fetchIndexes(baseUrl, ""),
            fetchAutoCompleteJS(),
        ]);

        // Wrap SearchSourceFactory with synonym expansion
        const baseSource = SearchSourceFactory(wrappedIndexes, zhDictionary, searchResultLimits);
        const sourceWithSynonyms = (query, callback) => {
            baseSource(expandSynonyms(query), callback);
        };

        const searchFooterLinkElement = ({ query }) => {
            const a = document.createElement("a");
            const params = new URLSearchParams();
            params.set("q", query);
            const url = `${baseUrl}search?${params.toString()}`;
            a.href = url;
            a.textContent = translate({ id: "theme.SearchBar.seeAll", message: "See all results" });
            a.addEventListener("click", (e) => {
                if (!e.ctrlKey && !e.metaKey) {
                    e.preventDefault();
                    search.current?.autocomplete.close();
                    history.push(url);
                }
            });
            return a;
        };

        search.current = autoComplete(
            searchBarRef.current,
            {
                hint: false,
                autoselect: true,
                openOnFocus: true,
                cssClasses: {
                    root: clsx(styles.searchBar, {
                        [styles.searchBarLeft]: searchBarPosition === "left",
                    }),
                    noPrefix: true,
                    dropdownMenu: styles.dropdownMenu,
                    input: styles.input,
                    hint: styles.hint,
                    suggestions: styles.suggestions,
                    suggestion: styles.suggestion,
                    cursor: styles.cursor,
                    dataset: styles.dataset,
                    empty: styles.empty,
                },
            },
            [
                {
                    source: sourceWithSynonyms,
                    templates: {
                        suggestion: SuggestionTemplate,
                        empty: EmptyTemplate,
                        footer: ({ query, isEmpty }) => {
                            if (isEmpty) return;
                            const a = searchFooterLinkElement({ query, isEmpty });
                            const div = document.createElement("div");
                            div.className = styles.hitFooter;
                            div.appendChild(a);
                            return div;
                        },
                    },
                },
            ]
        )
            .on("autocomplete:selected", function (event, { document: { u, h }, tokens }) {
                searchBarRef.current?.blur();

                // Save to recent searches and fire GA event
                const query = searchBarRef.current?.value || inputValue;
                addRecentSearch(query);
                window.gtag?.("event", "search_result_click", {
                    search_term: query,
                    result_url: u,
                });

                let url = u;
                if (Mark && tokens.length > 0) {
                    const params = new URLSearchParams();
                    for (const token of tokens) params.append(SEARCH_PARAM_HIGHLIGHT, token);
                    url += `?${params.toString()}`;
                }
                if (h) url += h;
                history.push(url);
            })
            .on("autocomplete:closed", () => {
                searchBarRef.current?.blur();
            });

        indexStateMap.current.set("default", "done");
        setLoading(false);

        if (focusAfterIndexLoaded.current) {
            const input = searchBarRef.current;
            if (input.value) search.current?.autocomplete.open();
            input.focus();
        }
    }, [baseUrl, history]);

    // On-page keyword highlighting — excluding code blocks
    useEffect(() => {
        if (!Mark) return;
        const keywords = isBrowser
            ? new URLSearchParams(location.search).getAll(SEARCH_PARAM_HIGHLIGHT)
            : [];
        setTimeout(() => {
            const root = document.querySelector("article");
            if (!root) return;
            const mark = new Mark(root);
            mark.unmark();
            if (keywords.length !== 0) {
                mark.mark(keywords, {
                    exclude: ["pre *", "code *"],
                    separateWordSearch: false,
                    acrossElements: false,
                });
            }
            setInputValue(keywords.join(" "));
            search.current?.autocomplete.setVal(keywords.join(" "));
        });
    }, [isBrowser, location.search, location.pathname]);

    const onInputFocus = useCallback(() => {
        focusAfterIndexLoaded.current = true;
        loadIndex();
        setFocused(true);
        handleSearchBarToggle?.(true);
    }, [handleSearchBarToggle, loadIndex]);

    const onInputBlur = useCallback(() => {
        setFocused(false);
        handleSearchBarToggle?.(false);
    }, [handleSearchBarToggle]);

    const onInputMouseEnter = useCallback(() => {
        loadIndex();
    }, [loadIndex]);

    const onInputChange = useCallback((event) => {
        setInputValue(event.target.value);
        if (event.target.value) setInputChanged(true);
    }, []);

    const isMac = isBrowser
        ? /mac/i.test(navigator.userAgentData?.platform ?? navigator.platform)
        : false;

    useEffect(() => {
        if (!searchBarShortcut) return;
        const handleShortcut = (event) => {
            if (
                (isMac ? event.metaKey : event.ctrlKey) &&
                (event.key === "k" || event.key === "K")
            ) {
                event.preventDefault();
                searchBarRef.current?.focus();
                onInputFocus();
            }
        };
        document.addEventListener("keydown", handleShortcut);
        return () => document.removeEventListener("keydown", handleShortcut);
    }, [isMac, onInputFocus]);

    const onClearSearch = useCallback(() => {
        const params = new URLSearchParams(location.search);
        params.delete(SEARCH_PARAM_HIGHLIGHT);
        const paramsStr = params.toString();
        const searchUrl =
            location.pathname +
            (paramsStr !== "" ? `?${paramsStr}` : "") +
            location.hash;
        if (searchUrl !== location.pathname + location.search + location.hash) {
            history.push(searchUrl);
        }
        setInputValue("");
        search.current?.autocomplete.setVal("");
    }, [location.pathname, location.search, location.hash, history]);

    return (
        <div
            className={clsx("navbar__search", styles.searchBarContainer, {
                [styles.searchIndexLoading]: loading && inputChanged,
                [styles.focused]: focused,
            })}
        >
            <input
                placeholder={translate({
                    id: "theme.SearchBar.label",
                    message: "Search",
                    description: "The ARIA label and placeholder for search button",
                })}
                aria-label="Search"
                className="navbar__search-input"
                onMouseEnter={onInputMouseEnter}
                onFocus={onInputFocus}
                onBlur={onInputBlur}
                onChange={onInputChange}
                ref={searchBarRef}
                value={inputValue}
            />
            <LoadingRing className={styles.searchBarLoadingRing} />
            {searchBarShortcut &&
                searchBarShortcutHint &&
                (inputValue !== "" ? (
                    <button className={styles.searchClearButton} onClick={onClearSearch}>
                        ✕
                    </button>
                ) : (
                    isBrowser && (
                        <div className={styles.searchHintContainer}>
                            <kbd className={styles.searchHint}>{isMac ? "⌘" : "ctrl"}</kbd>
                            <kbd className={styles.searchHint}>K</kbd>
                        </div>
                    )
                ))}
        </div>
    );
}
