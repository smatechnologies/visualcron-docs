---
name: visualcron-docs-uplift
description: >
  Run the VisualCron documentation assessment and uplift program on the
  smatechnologies/visualcron-docs repository (help.visualcron.com), unit by
  unit, against a local, private export of the VisualCron source code (VC_CODE_EXPORT). Use this skill whenever the
  user wants to score, grade, assess, audit, uplift, or improve VisualCron
  documentation, or says anything like "pre-assess the File Tasks docs",
  "score the VisualCron connections pages", "compare the VC docs to the code",
  "uplift the Event Trigger docs", "run the post-assessment for tasks-net", or
  "where does the VisualCron uplift stand". Produces branded .docx assessments
  in the assessments folder (VC_DOCS_ASSESSMENTS) on a fixed rubric so pre and post scores are comparable, and gates
  every write behind explicit approval. Not for the OpCon *-docs repositories:
  those use integration-docs-uplift.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Skill
---

# VisualCron docs uplift

You run a repeatable program that takes VisualCron's documentation from its current state to the best
state this process can reach, and measures both ends with the same rubric. It is the VisualCron
counterpart of `integration-docs-uplift` (the OpCon connector and agent program), and it keeps that
program's method, gates, rubric arithmetic and report format, so the two programs' numbers read on the
same scale.

## What is different from the OpCon program

Read this first. Almost every adaptation in this skill follows from one of these rows.

| | OpCon program | This program |
|---|---|---|
| Docs | ~59 small `*-docs` repos, 5–12 pages each | **One repo, about 720 pages** — `smatechnologies/visualcron-docs` |
| Unit of work | A repository | **A unit** — a Task category, the Event Triggers, the Connections — fixed in [references/units.json](references/units.json) (58 units) |
| Code | Hard to find, often unreachable | One local, private export, at the path in the environment variable **`VC_CODE_EXPORT`**. **No git**, so no ref to cite — see the private code map (Private companions, below) |
| Code language | Java, C#, Perl | **VB.NET first**, then C# |
| Docs-to-code join | By hand | **Mechanical**: the product names its help page for every Task, Event Trigger and Connection (the private `helplink_join.py`) |
| Front matter | `title`, `description`, `tags`, `sidebar_label` | **`sidebar_label` + `hide_title: 'true'`**, body opens with `## H2`. No page has title/description/tags, and none should be scored for it. |
| Standards | `technical-writer`, vendored in each repo | **VisualCron standards**, in this repo at `.claude/skills/visualcron-technical-writer/` (see Standards precedence) |
| Extra contract | — | `chm-config.json` maps pages to the CHM help compiled into the product. **F1 in the Client depends on it.** |
| Repo activity | Mostly quiet | **Busy**: daily commits, release branches, several active writers |

## The two rules that shape everything else

**One unit at a time, start to finish** — unless the owner chooses Fast-track mode (below). Accuracy
comes from holding one unit's code surface and pages in context at once. Do not batch units or
pre-fetch the next one. If asked for several, finish the first and ask before continuing. Small units (1–3 pages: `tasks-informatica`, `tasks-sap`,
`tasks-string`...) may be **paired with an adjacent unit only when the user asks**, and each unit
still gets its own report.

**Assess the corpus, not the page.** In this repo a fact is established once and used on dozens of
pages — every Task shares the Main settings, Flow, On error, Conditions, Timeout and Notifications tabs,
documented in the `task-framework` unit. **Grep all of `docs/` before recording anything as missing**,
not just the unit. A shared setting a Task page does not repeat is not a coverage gap.

## Phases and their gates

| # | Phase | Writes? | Gate |
|---|---|---|---|
| 1 | Pre-assessment (**provisional**) | Report only, to the assessments folder | None — run on request |
| 2 | Docs↔code comparison, uplift proposal, **baseline finalized** | No | None — the proposal is the deliverable |
| 3 | Apply uplift, **commit locally** | Yes, to a local branch only | **Explicit approval of the proposal**. No push and no PR without the owner's go-ahead (see below) |
| 4 | Post-assessment | Report only, to the assessments folder | None |

**Publishing is the owner's decision.** This program commits locally. Never `git push`, never open a
PR and never run `gh pr ...` against `visualcron-docs` without the owner's explicit go-ahead for that
specific push or PR. Approval of a proposal is approval to commit locally, nothing more. When a phase
ends with local commits, report the branch and commit hashes and state plainly whether anything has
been pushed. The public commit-message rules and leak greps (Phase 3) apply to every commit either
way.

**The phase 1 baseline is provisional; phase 2 finalizes it.** Say so when you deliver it. In the OpCon
program, phase 2's source re-read routinely changed the phase 1 numbers — findings withdrawn, findings
added, mechanisms corrected. Reissue the pre-assessment with a revision note when phase 2
changes it. Never compare a post-assessment against a baseline you know to be wrong.

Announce which phase you are entering and **stop at the end of it**. Do not roll from phase 2 into phase
3 because the proposal looked good to you. Approval on one unit does not carry to the next.

### Write everything in US English

Every artifact — reports, the summary, the engineering-items file, commit messages and PR bodies — in
standard American spelling. The OpCon skill's explicit word list applies (program, artifact, behavior,
normalize, finalize, judgment, organization, labeled, canceled, catalog, gray, while, among...). Do not
apply a blanket `-ise` → `-ize` rule: it wrecks *precise, promise, enterprise, otherwise, advise,
exercise, compromise*. Re-scan with `\w*is(e|ed|es|ing)`, `\w+our`, `\w+lled` and judge by eye.

### Output locations

**One folder for everything**, separate from the integrations program's folders. There is one
repository, so pre- and post-assessments do not need folders of their own (owner decision, 2026-10-07).
The folder is the environment variable **`VC_DOCS_ASSESSMENTS`**, default
`%OneDrive%\VisualCron-docs-assessments`:

```
%VC_DOCS_ASSESSMENTS%\
    visualcron-docs-<unit>-preassessment-<YYYY-MM-DD>.docx    phase 1 (reissued with a revision note if phase 2 changes it)
    visualcron-docs-<unit>-preassessment-findings.json        the findings data behind the latest report (keep current)
    visualcron-docs-<unit>-proposal-<YYYY-MM-DD>.md           phase 2 proposal, approved or rejected page by page
    visualcron-docs-<unit>-postassessment-<YYYY-MM-DD>.docx   phase 4
    VisualCron-docs-engineering-items.md                      items documentation cannot fix
    VisualCron-docs-pre-post-summary.json                     rolling summary state (hand-edited)
    VisualCron-docs-pre-post-summary.docx                     rolling summary, rendered by build_summary.py
```

Verify the folder exists; create it only if missing. Never write into the `Integrations-docs-*` folders.
Read `VC_DOCS_ASSESSMENTS` first; when it is not set, read `%OneDrive%` from the environment
(`$env:OneDriveCommercial`, else `$env:OneDrive`). Never hardcode a tenant name or a user path. The
scripts resolve the folder the same way. The unit slug comes before the phase in every filename, so a
unit's pre and post reports sort next to each other. The assessments are internal: they cite private
source and never go into this repository.

## Before every phase: three checks

Run all three, every time. Each one guards against a failure that cost the OpCon program a full
re-assessment.

```bash
# 1. The working tree IS the assessment target. Empty output = assess in place; anything else = stop.
git -C <docs-repo> fetch -q origin && git -C <docs-repo> diff --stat origin/main -- docs/ sidebars.js chm-config.json

# 2. The unit partition still covers every page exactly once (exit 1 on any fault).
python scripts/units.py --docs <docs-repo>/docs check

# 3. Which release the code snapshot is — see the private code map, "Identifying the snapshot".
```

A clone can hold several local branches, and some may be hundreds of commits behind `main`. A branch that has *lost* content
manufactures "documented nowhere" findings. When a unit throws up a cluster of absences, suspect the
tree before believing the pattern.

If check 3 shows the snapshot is **older** than the newest changelog release on `main`, findings about
the newer features are version artifacts: name the gap in the report header and do not score them.

## Fast-track mode

The owner may choose this batch method instead of one unit at a time. It is how the program was
finished. Everything else in this skill (rubric, report format, gates, public-commit rules) still
applies.

1. **Batches in parallel.** Units are grouped into batches, and the units in a batch run in parallel.
2. **One pass assesses and drafts.** For each unit, a single pass produces the pre-assessment and the
   drafted replacement text together, instead of separate phase 1 and phase 2 passes.
3. **One attack round per batch**: two independent accuracy reviewers and one standards reviewer, all
   read-only and none of them the drafter. **Every claim they make is re-verified against source**
   before it is accepted.
4. **Drafter revision.** The drafter revises from the verified claims only.
5. **One approval stop per batch, at the proposal.** The owner approves or rejects page by page. No
   other stop is taken inside the batch.
6. **Local commit per unit**, on that unit's own branch, after the standards pass, the build and the
   leak greps.
7. **One post reviewer, then a fix round with its own review.** An independent reviewer checks every
   changed sentence against source before phase 4 is scored; fixes from that review get one further
   review of their own.

**Standing owner decisions** apply to every unit without asking again:

- Describe a product defect in **neutral wording**: what the product does today, without calling it
  a bug or speculating about a fix. The defect itself goes to the engineering-items file.
- **Images are never moved or replaced**; the only image change is adding alt text.
- **Passages about a provider change** (a third-party service that was replaced, renamed or retired)
  are **held** for the owner, not rewritten.
- **Front matter, file names, `chmFile` values and `sidebars.js` are frozen.**
- **Connection facts on a Task page are stated briefly, with a link** to the Connection page that
  documents them, rather than repeated in full.

## Phase 1 — Pre-assessment

1. **Name the unit.** Map the user's words to a slug with `python scripts/units.py --docs ... list`.
   If they named something that spans units ("the triggers"), say which units that is and ask which
   to start with.
2. **Inventory the pages** with `python scripts/units.py --docs ... pages <slug> --json`. This exact
   set is what phase 4 re-scores. Record `units_version` and the docs ref.
3. **Read every page in the unit before scoring any page**, and build a map of which page establishes
   which fact. For Task units, also read the `task-framework` pages the unit relies on.
4. **Join the unit to the code** with the private `helplink_join.py` (see Private companions):
   `python "$VC_SKILL_PRIVATE/helplink_join.py" --code "$VC_CODE_EXPORT" --docs-repo <docs-repo> --unit <slug>`.
   This lists every object the product assigns to the unit, its F1 page, and the unit's pages that no
   object points at. Then follow the private code map to each object's settings definition, its Client
   editor and its Server-side process. A unit whose objects ship in an add-on absent from the snapshot
   is **docs-only for accuracy** — say so on the cover.
5. **Run the gap analysis** with the `vc-doc-analyzer` method (Step 0–4 and its impact rubric — see
   Bundled resources). It is page-oriented, so **re-check every gap it raises against the whole
   corpus** before adopting it. Do **not** use `doc-scorer` or any other OpCon assessor: their axes
   assume the OpCon corpus.
6. **Score** with [references/scoring-rubric.md](references/scoring-rubric.md).
7. **Write the report**: build `findings.json`, render with `scripts/build_report.py`. Never
   hand-assemble a .docx. Check the rendered document against its own data before delivering it.
   **Copy the findings JSON into the assessments folder** as
   `visualcron-docs-<unit>-preassessment-findings.json` every time you render. The session scratchpad
   is not durable: working files have vanished between phases before, and the data then had to be
   rebuilt and checked against the rendered report.

## Phase 2 — Compare and propose

Read the code surface for every object in the unit — its settings definition (properties, defaults,
enums, documentation comments), its Client editor (what the Client actually shows and its runtime
labels), and its Server-side process (what the Server does, what it writes to output, what errors it
raises). Compare against
every documented claim.

**Re-read the source before drafting replacement text.** Phase 1 establishes *that* something is wrong;
phase 2 must establish *what it should say*. Checking that a property exists is not checking that
anything consumes it — a dead setting documented as live describes behavior that does not exist.

Produce a **proposal**, not edits, grouped by page so the user can approve page by page. For each item:
the page and location, what is wrong or missing, what it should say, the code evidence and tier, the
axis and severity it clears, and the score movement.

- **Never invent product behavior.** If the code does not show it, the item is "needs SME". A confident
  wrong default on an unattended Job is exactly the harm this program exists to prevent.
- **State the achievable ceiling** and list what sits above it and why: screenshots that need a running
  Client, behavior no source explains, release status, publishing decisions.
- **Never propose documenting something with no changelog entry** without asking whether it has
  shipped. The standards forbid documenting unreleased features, and the snapshot may be ahead of the
  release line.
- Where the code itself is wrong — a wrong label, an empty HelpLink, an unused setting — that is an
  **engineering item**, not documentation. Do not document a defect as
  behavior, and never edit code. Where the **current** behavior is a safety risk (a misleading label, an
  ignored filter), a neutral warning describing what the product does today may be the right customer
  guidance. That is the owner's call: ask, do not decide.

**Before delivering the proposal, attack it.** Launch three independent, read-only reviewers in
parallel, none of whom wrote the proposal:
1. an **accuracy falsifier** that re-derives every drafted claim from source without your evidence
2. an **exposure and standards auditor** for the text that would be published
3. a **customer-clarity critic** that reads each resulting page as an administrator would

Then **verify every claim they make against the source yourself** before accepting it. Reviewers are
also instruments. On the first unit this pass found wrong or overstated drafted sentences, High
defects that phase 1 and phase 2 had missed, a code name wrongly exempted as product language (the
Client shows a spaced, readable description), and a sample procedure breaking the rule it was written
to fix. The proposal had looked finished.

## Phase 3 — Uplift, committed locally

Only after the user approves specific items. **Nothing in this phase is pushed** without the owner's
go-ahead (see "Publishing is the owner's decision" above). Fetching `origin` to branch from current `main` is fine: it reads, it does not publish.

1. **Branch from `origin/main`**: `docs/uplift-<unit>-<YYYY-MM-DD>`. Never commit to `main`, never
   branch off a parked feature branch. Fetch first — `main` moves daily here.
2. **Apply only the approved items.** If applying one reveals another problem, note it; do not expand
   scope silently.
3. **Line endings: the repo stores LF; a Windows clone may check out CRLF.** Every tracked page is
   `i/lf` in the index, there is no `.gitattributes`, and on a Windows clone with `core.autocrlf=true`
   checkout produces CRLF in the
   working tree. So a page *looks* CRLF on disk and is LF in the repository. Do not "preserve" or
   "fix" either. After editing, `git diff --stat` must show only the lines you meant to change; if a
   file shows as wholly rewritten, check `git ls-files --eol <file>` and `git config core.autocrlf`
   before committing, and do not commit until the diff is the size of the change.
   (A first version of this rule asserted the corpus was CRLF and shipped a check for it; run against
   the untouched tree, the check flagged every file with no trailing newline, and the index showed the
   premise was a working-tree artifact. Prove a check on clean input before trusting it.)
4. **Never rename or move a page, and never change a `chmFile` value.** The CHM file names are a
   contract with compiled product code; F1 in every installed Client depends on them. A new page needs
   a `sidebars.js` entry **and** a `chm-config.json` mapping, or it is missing from in-product help.
5. **Never edit a historical changelog entry** to satisfy a style rule. It is a release record.
6. **Run the VisualCron standards pass** — read `.claude/skills/visualcron-technical-writer/SKILL.md`
   and its `resources/` (see Bundled resources) and apply its **Edit** mode and pre-flight checklist to
   every changed page. **Client vocabulary is
   not banned** (owner rule, 2026-10-20): click, execute, check, launch, checkbox, combo box and the
   other words the Client uses as control or action names are never rewritten as a terminology fix.
   Only hit, drop-down, hamburger and dialog box are banned. Never rewrite a word that names a product
   feature, label, activity, event or Task type (*Click* activity, *Modal window*, *Remote Execute*,
   *Turn off VM*); changing it makes the page disagree with the Client. See Standards precedence.
7. **Build**: `yarn install && yarn build` (`onBrokenLinks: 'throw'` catches broken links). Confirm new
   anchors exist in the built HTML. If `chm-config.json` or `sidebars.js` changed, also run
   `yarn build:chm` and confirm the page is in the generated `.hhc`. CI does **not** build PRs — the
   only automated check runs on push to `main` — so the local build is the only check this work gets.
8. **Verify each item closed**, mechanically where possible. The OpCon lessons below apply in full.
9. **Read the full diff, run the leak checks, then commit locally.** One branch per unit. Report the
   branch name and commit hash, and say plainly that nothing was pushed. Because the branch is
   unpushed and `main` moves daily, note in the report how far behind `origin/main` it is
   (`git rev-list --count <branch>..origin/main`). Publishing is a separate, explicit step that the
   owner authorizes. CODEOWNERS is the docs team, and one PR per unit keeps review and rebase
   tractable.

### The repo is public, so commit messages are written to be published

`visualcron-docs` publishes to help.visualcron.com; the code does not. A local commit message becomes
public the day the branch is pushed, and fixing it then means a history rewrite. Write every commit as
though it were already published:

- **No source path, file name, class name, or line citation** from the code. Those belong in the
  internal assessment report. A customer-facing file (`VCCommand.exe`,
  `"C:\Program Files (x86)\VisualCron"`) is fine; a source file name with a line number is not.
- **No grade, letter, baseline or ceiling.** The rubric is internal.
- Describe defects as **what a reader was getting wrong**, not as what the code does internally.

**Run this on every commit message, and on the added lines of the diff, before committing.** In the
OpCon program these rules were often forgotten before anyone checked.

```bash
t="$(cat commit-msg.txt; git diff --cached | grep '^+')"   # message file plus the added lines
echo "$t" | grep -inE 'baseline \*?\*?[0-9]+|achievable ceiling|\([A-F]\)|scored [0-9]|rubric'
echo "$t" | grep -inE '\.(vb|cs|resx|vbproj|csproj|xml):[0-9]+'      # source file with a line number
echo "$t" | grep -inE 'C:[\\/]Users|`[0-9a-f]{7,}`'
[ -n "$VC_CODE_EXPORT" ] && echo "$t" | grep -inF "$VC_CODE_EXPORT"   # the local export path itself
echo "$t" | grep -inwF "$USERNAME"                                      # your own user name
```

The patterns for private source names (source folders, class and control naming, internal project
names) are kept in the private code map; run them from there before every commit.

An unpushed commit message can still be amended cheaply; once pushed it cannot, and rewriting a
published branch is the owner's call. Run the grep **before** committing.

## Phase 4 — Post-assessment

Re-score the **same page inventory** (re-run `units.py pages <slug>`; any page added by the uplift is
scored and named) with the **same rubric version** and the **same snapshot**. Report the delta: per-axis
and overall movement, findings closed, findings remaining and why, the gap left to the ceiling. If the
rubric, the unit partition or the snapshot had to change, say so and say what it does to comparability.

- **`blocking` is a boolean.** Narrative goes in `summary`. The renderer now refuses prose in that
  field, because in the OpCon program it was silently dropped and rendered every report BLOCKED.
- **A post report's Findings section lists what still stands**, each with its `status`. Narrate
  closures in `summary`; let `delta` carry the counts.
- **Check a superlative against the scoreboard before writing it.** *First*, *most*, *furthest* are
  arithmetic, and the table is in the same document.
- **Close phase 4 by updating the rolling summary** (below).

## Standards precedence

| Question | Authority |
|---|---|
| Terminology, banned verbs and UI terms, voice, procedure rules, admonitions, front matter | `visualcron-documentation-standards.md` and `visualcron-glossary.md`, including their **Client vocabulary** rule (owner rule, 2026-10-20) and **Product-language exemption** (2026-10-07), which the rubric applies the same way |
| Page type and structure | `visualcron-documentation-types.md`; field descriptions in `visualcron-parameter-descriptions.md`; API pages in `visualcron-api-reference.md` |
| Typographic conventions (italics for UI, bold-italics for tabs, `->` menus, `"values"`, `<placeholders>`) | `docs/documentation-format.md`, the product's own published page — the standards defer to it |
| Repository conventions (front matter, registration, change notes) | This repository's `CLAUDE.md`, the VisualCron project file |

The standards files live in this repository at `.claude/skills/visualcron-technical-writer/resources/`.
If you keep a second copy anywhere else, **any change to one copy is made to both in the same
session**, then verified with a byte comparison (ignoring CR). When the standards and
`documentation-format.md` disagree, note it in the report rather than silently picking. When
`CLAUDE.md` and the standards files disagree, the standards files win and the disagreement is an owner
item.

## Non-negotiables

- **Read-only in phases 1, 2 and 4.** Never edit a docs file and never edit code during assessment.
- **Search the corpus before calling anything missing.**
- **Verify the tree is the target before running a single check.**
- **Never fabricate product behavior, defaults, labels, Variable syntax or version numbers.** Flag the
  gap and name the source that would settle it.
- **Record what you could not verify.** Every report has an Unverifiable section, and for a closed-
  source product it is expected to be substantial.
- **Presentation belongs to the owner.** Accuracy, terminology and completeness are this program's
  authority. Layout someone chose is not a defect.
- **"Ships but undocumented" is a question, not a finding.** What goes on a public site is a publishing
  decision. A capability missing from every navigation surface of an otherwise careful section is
  evidence of intent. Ask before writing a page for it.
- **Deprecated and removed content is the owner's.** The Twitter pages are labeled deprecated in a
  corpus whose changelog says the integration was removed, while the code snapshot may still contain
  it.
  Do not delete, and do not "fix" them toward either reading. Ask.
- **Git Bash rewrites `branch:path` arguments.** `git show <branch>:.claude/...`
  is converted into a Windows path and fails with "ambiguous argument". The failure looks like a
  difference between files. Set `MSYS_NO_PATHCONV=1` for any `git show <ref>:<path>`.

## Carried from the OpCon program — the method lessons that apply here unchanged

Each of these cost the OpCon program a withdrawn finding, a corrective PR or a re-issued report. The
OpCon program's skill, `integration-docs-uplift` (not in this repository), has the full stories; these
are the rules.

- **Suspect the instrument before the corpus.** In the OpCon program the verifier was repeatedly
  wrong more often than the documentation. On day one of this program an early survey counted a
  commented-out member as a live Event Trigger type, and the obsolete-member detector found nothing
  (the source marks retirement in a doc comment). Sanity-check every count.
- **Skip commented-out code; do not key on the literal you expect; products roll their own helpers.**
  Grep for every path a value can take before trusting a list.
- **Audit descriptions, not just values.** A table whose keys all match can still describe them wrong.
- **A finding scoped "across the corpus" needs a corpus-wide closure check**, with any carve-out
  (historical changelog entries) stated rather than skipped.
- **Read the diff, not only the verification output.**
- **A stale comment in the source can be the cause of a docs defect.** Check whether the
  documentation comment, the in-product object description or the tooltip says the same wrong thing; if so, the fix is a docs change
  **and** an engineering item.
- **A closure check confirms text, not correctness.** When a fix asserts a *new* rule ("these fields
  are required"), the verifier must test the rule against source, not that the sentence exists.
- **Sweep every repetition of a claim**, phrased any way, before calling it closed — **including
  `sidebar_label`**, which is what the sidebar, the CHM index and search results show.
- **Give sibling pages the same safety net.** A caution added to one Task page is a defect on its
  sibling that does the same thing (Copy and Move, Execute and Remote Execute).
- **A successful build says nothing about whether the markup is right.** Check table invariants
  (`|---|` in the first two lines of every pipe-row run) and admonition placement inside numbered
  steps (4-space indent, per the standards).
- **Prove a new check catches the bug it was written for**: put the defect back and watch it fail.
- **Verify what a new page asserts, not only what a correction changes.** Strings in a settings class
  are candidates, not options, until the Client is shown to expose them.
- **A caution reused verbatim has not been read in its new position.**
- **The banned-term list is a prompt to check the product, not a verdict.** Owner rule (2026-10-20):
  a word the Client uses as a control or action name is not banned in any use. Before recording a
  terminology finding, check the word with the private `product_terms.py --code "$VC_CODE_EXPORT"
  --term <word>`: any NAME hit means it is Client vocabulary. A 0 for a word the script has not seen
  before still deserves a quick grep of the Client's English language resource.
- **Review the applied text again before scoring phase 4**, with an independent read-only reviewer who
  checks every changed sentence against source. On the first unit the proposal had passed two
  reviews, and this third pass still overturned several claims. Verify each reviewer claim yourself; fix the
  ones that hold, and score new defects in untouched text as new post findings (`delta.new`).
- **Check a correction against earlier program decisions, not only the source.** A correct description
  of a suspected defect is still unpublishable if the owner has not approved publishing that item.
- **Anchors cannot contain trailing whitespace**; keep an `assert count == 1` on every scripted
  replacement so a non-match is loud.
- **Survey recursively.** `units.py` does; a hand-built page list must too.

## Tracking progress

The assessments folder is the state. A unit with a pre-report and no post-report is mid-program. When
the user asks where things stand, list the assessments folder and report from the filenames, matched
on `visualcron-docs-<unit>-(pre|post)assessment-<date>.docx`, against `units.py list`. Do not answer
from memory.

### The engineering-items file

`%VC_DOCS_ASSESSMENTS%\VisualCron-docs-engineering-items.md` records everything the
review surfaces that **documentation cannot fix**: product defects, empty or wrong HelpLinks, bad UI
labels, repo configuration, exposure that is not on a page, and questions only an owner can answer.

**Append to it in the same session you find the item, then grep the file to confirm it is there before
saying it is.** Sort by severity, not by unit. A finding belongs in a unit report only if editing that
unit's documentation could close it.

### The rolling pre/post summary — the last action of phase 4

```
%VC_DOCS_ASSESSMENTS%/VisualCron-docs-pre-post-summary.json   <- state, hand-edited
%VC_DOCS_ASSESSMENTS%/VisualCron-docs-pre-post-summary.docx   <- rendered: python scripts/build_summary.py
```

Same shape and rules as the OpCon summary: four rendered sections (How to read, Scoreboard, Per-unit
synthesis, method list); one scoreboard row per unit with `#`, unit, baseline (the **phase-2-finalized**
score), final, ceiling, corrections, pages, words added; `repo` and `slug` both hold the unit slug.
Measure `pages` and `words_added` from the unit's local branch diff
(`git diff origin/main...docs/uplift-<unit>-<date> -- docs/`, skipping the `+++`/`---` headers), not
from memory. Identify the branch by its name, never by adjacency. A unit has a PR only if the owner
authorized one; do not assume one exists. The renderer refuses a final score above its ceiling — that is almost always a stale ceiling
after an owner decision; find out which before touching either number. Add a `method` rule only when a
revision or a withdrawn finding paid for it.

## Private companions (not in this repository)

Three files map the private source code and therefore stay private. They are kept in the folder named
by the environment variable `VC_SKILL_PRIVATE`, and are never committed to this repository:

| File | What it is for | How it is used |
|---|---|---|
| `code-map.md` | Where each documented surface lives in the source, how to date the snapshot, source-reading traps, reachability, exclusions, what never to publish, and the internal project-name patterns for the leak greps | Read it before any phase that touches code |
| `helplink_join.py` | The code-to-page join: every Task type, Event Trigger and Connection type the product assigns to a unit, its F1 help page, and the unit pages no object points at | `python "$VC_SKILL_PRIVATE/helplink_join.py" --code "$VC_CODE_EXPORT" --docs-repo <docs-repo> --unit <slug>` in phase 1 |
| `product_terms.py` | Every user-visible English string in the product, classified as NAME or PROSE use, so a terminology finding can be checked against Client vocabulary | `python "$VC_SKILL_PRIVATE/product_terms.py" --code "$VC_CODE_EXPORT" --term <word>` before recording any terminology finding |

When the private companions are missing, say so on the report cover. Without the join and the code
map, the Accuracy and Coverage axes rest on whatever other source tier is available, and the report
must name that tier.

## Bundled resources

| File | Read it when |
|---|---|
| [references/scoring-rubric.md](references/scoring-rubric.md) | Any scoring. Axes, weights, VC escalations, exclusions, evidence tiers, ceiling. |
| [references/units.json](references/units.json) | The fixed unit partition. Change it only with a version bump and a note. |
| `scripts/units.py` | Every page list, and the partition check. |
| `scripts/build_report.py` | Rendering a unit report. `--schema` documents the JSON. Writes to `VC_DOCS_ASSESSMENTS` (default `%OneDrive%\VisualCron-docs-assessments`) unless `--out` is given. |
| `scripts/build_summary.py` | Rendering the rolling summary, from and to the same folder. |
| `assets/continuous-horizontal-blue.png` | The logo on every rendered report. |
| `.claude/skills/vc-doc-analyzer/` | The gap-analysis method and impact rubric (Step 0–4, evidence tiers). Read `SKILL.md` and its `references/`. |
| `.claude/skills/visualcron-technical-writer/` | The VisualCron standards (`SKILL.md` and `resources/`), and the writer used in phase 3. |

## Environment

| Variable | Meaning |
|---|---|
| `VC_CODE_EXPORT` | The local, private export of the VisualCron source. Read-only. Never cite its path in anything published. |
| `VC_DOCS_ASSESSMENTS` | The assessments output folder. Default: `%OneDrive%\VisualCron-docs-assessments`. |
| `VC_SKILL_PRIVATE` | The folder that holds the private companions (`code-map.md`, `helplink_join.py`, `product_terms.py`). Not in this repository. |

This skill lives in the docs repository at `.claude/skills/visualcron-docs-uplift/`. It may also be
installed at user level so it loads outside the repository.
