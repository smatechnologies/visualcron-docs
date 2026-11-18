# VisualCron Documentation Repository Map

The VisualCron documentation is maintained as an open-source Docusaurus site
at **`smatechnologies/visualcron-docs`**, with content under `docs/`. The
published site is `help.visualcron.com`; the legacy compiled help set is at
`visualcron.com/doc/HTML/`.

Verify the actual tree with `Glob` before relying on this map — the structure
evolves. Use this file to know *where a surface should be documented* and to
detect misplacement.

---

## Observed structure

```
docs/
├── index.md                          # Product overview, doc build date
├── changelog.md                      # Release history, VCPCM issue IDs
├── debugging-and-logging.md
├── using-visualcron/
│   ├── using-visualcron.md
│   ├── how-does-visualcron-work.md   # Trigger > Condition > Task > Notification
│   ├── visualcron-client.md
│   ├── visualcron-api.md             # .NET API
│   ├── visualcron-web-api.md         # REST / SOAP
│   └── powershell.md
└── client-user-interface/
    ├── job-folders.md
    └── server/
        ├── jobs-jobs.md
        ├── settings-folders.md
        └── job-tasks/
            ├── file-tasks/           # e.g. write-file.md
            ├── internal-tasks/       # e.g. control.md
            └── <category>-tasks/     # one folder per Task category
```

The key structural rule: **`job-tasks/<category>-tasks/<task-name>.md` is one
page per Task type.** This makes Task coverage directly countable — compare
the file count in each category folder against the Task types the product
exposes in that category.

---

## Frontmatter conventions

Pages use Docusaurus frontmatter. The house convention is `sidebar_label` plus a quoted
`hide_title: 'true'`, and the body opens with a `## H2` heading (the H2 is the visible page title):

```yaml
---
sidebar_label: 'Debug and Logging'
hide_title: 'true'
---

## Debug and Logging
```

Check for:

- Missing or empty `sidebar_label` on a page that needs a short nav label
- `hide_title: 'true'` on a page whose body does not open with a `## H2` — produces an untitled page
- Files on disk that appear in no sidebar entry (**orphaned page**, Section 4)
- Sidebar entries pointing at files that do not exist (**broken nav**, Section 4)

---

## Where each product surface should be documented

Use this mapping to decide whether a gap is "missing" or merely "misplaced."
A page that exists but sits in the wrong category is a **Structural** finding
(Section 4), not a **Missing** finding (Section 1).

| Product surface | Expected doc location |
|---|---|
| A Task type | `client-user-interface/server/job-tasks/<category>-tasks/<task>.md` |
| A Trigger type | Trigger reference section under `client-user-interface/server/` |
| A Condition type | Condition reference section under `client-user-interface/server/` |
| A Connection type | Connection reference section |
| Variables and functions | `client-user-interface/server/global-variables.md`, `global-date-time-variables.md`, `job-variables.md` |
| Server settings tab | `client-user-interface/server/settings-*.md` |
| .NET API | `using-visualcron/visualcron-api.md` |
| Web API routes | `using-visualcron/visualcron-web-api.md` |
| PowerShell usage | `using-visualcron/powershell.md` |
| Logging and troubleshooting | `debugging-and-logging.md` |
| Release changes | `changelog.md` |

---

## Reading the changelog as an input signal

`docs/changelog.md` is the single best low-cost signal for doc drift, and it
is the primary usable source when only **Tier E** evidence is available.

Observed conventions:

- `:star:` marks a new feature or enhancement
- `:white_check_mark:` marks a fix
- Entries carry a JIRA-style issue ID, e.g. `(VCPCM-2207)`
- Entries are prefixed with the affected component, e.g. `Client/Server:`

**Method for a changelog-driven audit:**

1. Extract entries for versions newer than the last substantive doc update.
2. Keep only entries describing **user-visible** change — a new field, a
   renamed option, a changed default, a new Task, altered behavior. Discard
   internal fixes with no doc surface.
3. For each kept entry, grep the doc tree for the feature, Task, or field it
   names.
4. No hit → candidate **Missing** (M-series). Hit that contradicts the entry →
   candidate **Outdated** (O-series).
5. Mark every one of these **Evidence Tier E** and state that Tier A–D
   confirmation is required before anyone acts on it.

Do not report a changelog entry as a doc defect without step 3. Many entries
describe changes that need no documentation.

---

## Version notes in body text

VisualCron pages commonly gate content by version in prose — for example, a
page noting that Job folders arrived in a specific release. When auditing:

- A version-gated capability documented **without** its version note is a
  finding (readers on older builds follow steps that do not apply)
- A version note referencing a release **older than the oldest supported
  version** is stale and can be flagged Low impact
- Never add or infer a version number you cannot source from the changelog or
  a Tier A–D source

---

## Structural checks specific to this repo

Run these regardless of depth setting:

```bash
# Pages on disk vs. pages reachable from the sidebar
# (compare Glob output against sidebars.js / sidebars.ts entries)

# Relative links that resolve to nothing
grep -rnoE "\]\(\.{0,2}/[^)]+\)" --include="*.md" docs/

# Images referenced but absent
grep -rnoE "!\[[^]]*\]\(([^)]+)\)" --include="*.md" docs/

# Pages missing frontmatter entirely
for f in $(find docs -name "*.md"); do head -1 "$f" | grep -q '^---$' || echo "NO FRONTMATTER: $f"; done

# Task category folders and their page counts (coverage baseline)
find docs -type d -name "*-tasks" -exec sh -c 'echo "$(ls -1 "$1" | wc -l)  $1"' _ {} \;
```

The last command is the fastest single coverage signal in the whole repo:
compare each count against the number of Task types the product exposes in
that category.
