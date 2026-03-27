// ── Popular search terms shown when the search bar is empty ───────────────────
export const POPULAR_SEARCHES = [
  'ftp task',
  'email notification',
  'trigger',
  'variable',
  'condition',
  'connection',
  'job folder',
  'flow control',
  'user permissions',
  'scheduler',
  'sftp',
  'ssh task',
];

// ── Abbreviation / synonym expansion ─────────────────────────────────────────
// Keys are what users type; values are what gets sent to Lunr
export const SYNONYMS = {
  'vc':       'visualcron',
  'ftp':      'ftp task',
  'sftp':     'sftp task',
  'ssh':      'ssh task',
  'smtp':     'email',
  'sql':      'sql task',
  'ps':       'powershell',
  'http':     'http task',
  'rest':     'http task',
  'api':      'http task',
  'regex':    'regular expression',
  'env':      'variable',
  'var':      'variable',
  'cron':     'scheduler',
  'sched':    'scheduler',
  'notify':   'notification',
  'notif':    'notification',
  'perm':     'user permissions',
  'perms':    'user permissions',
  'auth':     'user permissions',
};

// Expand any known abbreviations in a query before sending to Lunr
export function expandSynonyms(query) {
  if (!query) return query;
  const lower = query.toLowerCase().trim();
  // Exact match first
  if (SYNONYMS[lower]) return SYNONYMS[lower];
  // Word-boundary substitution for multi-word queries
  let expanded = query;
  for (const [abbr, full] of Object.entries(SYNONYMS)) {
    const regex = new RegExp(`(?<![\\w])${abbr}(?![\\w])`, 'gi');
    expanded = expanded.replace(regex, full);
  }
  return expanded;
}

// ── Recent-search localStorage helpers ───────────────────────────────────────
const STORAGE_KEY = 'visualcron-docs-recent-searches';
const MAX_RECENT  = 5;

export function getRecentSearches() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
  } catch {
    return [];
  }
}

export function addRecentSearch(term) {
  if (!term?.trim()) return;
  try {
    const recent = getRecentSearches().filter((s) => s !== term);
    recent.unshift(term);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(recent.slice(0, MAX_RECENT)));
  } catch {
    // localStorage may be unavailable (private mode, etc.)
  }
}
