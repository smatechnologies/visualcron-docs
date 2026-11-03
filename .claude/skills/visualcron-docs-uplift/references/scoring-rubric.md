# Scoring rubric — VisualCron docs

**Rubric version: VC 1.1.** Record this in every report. If the rubric changes, a pre/post pair built
across the change is not comparable, and the report has to say so; re-baseline the pre-assessment
under the new version instead.

- VC 1.1 (2026-10-20): Client vocabulary rule. Words the Client uses as control or action names
  (click, check, icon, combo box and others) are no longer banned terminology in any use.
- VC 1.0 (2026-10-07): first version.

This rubric is derived from the integration-docs rubric (1.2). The **severity weights, letter bands,
ceiling calculation and the corpus rule are unchanged**, so a 78 here and a 78 in the OpCon program
mean roughly the same amount of trouble. What changed is everything that depends on the corpus: the
house standard, the front matter convention, the help-context contract with the product, and the
VisualCron-specific escalations. Those are marked **VC** below.

## Scope of a finding

A finding is about **the corpus**, not the page. This corpus is about 720 pages, and a fact is routinely
established once — on `global-variables.md`, `task-main-settings`, a Connection page — and used on
dozens of Task pages. Before recording anything as missing, search **all of `docs/`**, not just the
unit:

```bash
grep -rniE "<the thing>|<the thing, loosened for hyphen/space drift>" docs/ --include=*.md --include=*.mdx
```

| What the search shows | Rating |
|---|---|
| Documented nowhere in `docs/` | Coverage finding, severity by what the reader cannot do without it |
| Documented on another page, and the page under review needs it to be usable | **Cross-reference** — Medium at most; the fix is a link |
| Documented on another page, and the page under review is complete without it | Not a finding |
| Documented on two pages that disagree | Accuracy finding against whichever contradicts the code |

Shared settings are the common case. Every Task has the Main settings, Flow, On error, Conditions,
Timeout and Notifications tabs, documented once under the `task-framework` unit. A Task page that
does not repeat them is **not** a coverage gap. A Task page whose own settings tab is undocumented is.

## Severity weights

Start each page at 100 and deduct:

| Severity | Deduction | What earns it |
|---|---|---|
| High | 25 | A reader following the page gets a wrong result: wrong default, wrong field, wrong Variable syntax, missing required step, documented capability that no longer exists, a live Task/Trigger/Connection with no page at all. |
| Medium | 8 | A reader is slowed or has to guess: undocumented setting, vague qualifier doing real work, stale UI label, missing prerequisite, page-type structure violated, banned terminology, F1 opens nothing. |
| Low | 2 | Cosmetic or metadata: heading case, object-noun casing, missing alt text, admonition misuse, a stale-but-harmless version note. |

| Letter | Range |
|---|---|
| A | 90–100 |
| B | 80–89 |
| C | 70–79 |
| D | 60–69 |
| F | below 60 |

Floor a page at 0. **Unit score** is the unweighted mean of its page scores, rounded. **Any open High
finding blocks**, regardless of the arithmetic — say so explicitly.

### VC escalations (from the vc-doc-analyzer impact rubric)

VisualCron runs unattended with broad privileges, and an unresolved Variable does not fail a Job —
it resolves to empty or literal text and the Job proceeds. So:

1. **Wrong Variable syntax, a renamed Variable key, or a wrong scope prefix is always High.** The Job
   succeeds with wrong data, which is worse than a failure.
2. **Anything touching Credentials, Connections, permissions, or the Web API token is High by
   default.** Demote only with the reason written into the finding.
3. **A wrong default or missing warning on a destructive Task** (File delete/move/overwrite, service
   control, registry, AD modification, SQL) is High.
4. **Confidence is separate from severity.** Record evidence tier (A–E, below) on the finding. Do not
   lower severity to express doubt; if the finding cannot be established at all, it goes to
   Unverifiable and gets no severity.

## The axes

Score every page against all nine. No credit for passing, only deductions — which keeps pre and post
arithmetic identical.

### 1. Accuracy vs. code (`A`)

Every factual claim — field labels, defaults, valid values, Variable names and syntax, menu paths,
Trigger-emitted Variables, exit codes, API routes and switches — matches the code snapshot recorded in
the report. The private code map (see "Private companions" in `SKILL.md`) says where each fact
lives and the traps in reading it.

Two VC-specific rules:

- **Labels are verified against what the Client renders, not against the designer file.** The
  Client replaces designer text at runtime with text looked up from its language resources, and the
  two can differ (a short designer label can render as a longer runtime label). Resolve each
  runtime lookup key through the English language resource; some keys are short tokens whose English
  text is a full sentence.
- **A field the code declares but the Client never shows is not a documentation gap.** See
  reachability under Coverage.

**If there is no usable code source for the unit** (the Task ships in an add-on that is absent from
the snapshot, for instance), this axis is `not assessed` for that unit. Never score it clean.

### 2. Coverage (`C`)

The documented surface against the reachable surface, across the whole of `docs/`. Start from
the private help-link join script (`helplink_join.py --unit <slug>`, see "Private companions" in
`SKILL.md`): every Task type, Event Trigger and Connection type the code
assigns to this unit, and every page in the unit that nothing in code points at.

| Join result | What it usually is |
|---|---|
| `OK` | Page exists. Now check its fields against the object's settings definition and its Client editor. |
| `NO PAGE (HelpLink empty)` | Product has no help page assigned. If the object is reachable and live, **High** Coverage plus an engineering item for the empty HelpLink. |
| `UNMAPPED in chm-config` | The page may exist under another name; F1 opens nothing. See axis 7. |
| `[Obsolete]` | Retired. Not a coverage gap. A page that still presents it as current is an Accuracy finding. |
| Page no code points at | Overview or shared-settings page (fine), a removed object, or a renamed HelpLink. Check which. |

**Check reachability before calling a capability undocumented.** An enum member is not a capability.
Members are retired by doc comment, skipped in pickers, gated by edition, or shipped only in add-ons
that are not in the snapshot. Trace from the Client's entry point inward — the code that picks the
Task editor for a Task type, the code that picks the Trigger editor for a Trigger type, the
Connection add menu.
When reachability cannot be settled from source, the honest outcome is **Unverifiable**.

**Trigger-emitted Variables are the most under-documented VC surface.** An Event Trigger page that
omits the Variables it emits entirely is High (downstream Tasks silently receive nothing); a partial
list is Medium.

### 3. Prerequisites and setup (`I`)

A reader should be able to configure the object from the page alone. **VC**: for Task, Trigger and
Connection pages, check that the page states, or links to where it states:

- the Connection or Credential the object requires, and which Connection type
- third-party software that must be installed on the Server (Office for Office Tasks, an SSIS
  version, PowerShell remoting and its port for remote scope)
- which **edition** the capability needs, where the code gates it — say *which* edition, never *how*
  the check works (licensing internals are an Exposure finding)
- permissions the user needs in VisualCron, and on the target system

For the `install`, `clustering` and `licensing` units this axis is the original install axis:
versions, accounts, ports, file locations, a verification step, uninstall or rollback. A missing
verification step is Medium. A missing required prerequisite is High.

### 4. Structure and page type (`S`)

Against `visualcron-documentation-types.md` (conceptual, procedural, reference) and the procedural
rules in `visualcron-documentation-standards.md`: lead-in sentence, numbered steps, one action per
step, a result statement, about 10 steps per section, tables explain consequences.

**VC**: the page opens with a `## H2` immediately after front matter, because `hide_title: 'true'`
suppresses the auto-title. A page opening with an admonition or prose has no visible title. That is
Medium. (Fifteen deprecated Twitter pages open with a `:::warning` — the warning is deliberate; the
missing H2 is still a finding, and the fix is to put the H2 first, not to remove the warning.)

**Do not score against the 13-section "Writer-Friendly Documentation Standard"**
(`visualcron-primary-analysis.md`). It is a feature-page completeness template for a different
assessor. Applied to 400 Task reference pages it would deduct for missing FAQs and Glossaries on every
page, measuring the template rather than the documentation.

**Never restyle a layout an owner chose.** Presentation belongs to the owner. When something is merely
not how you would build it, ask or leave it.

### 5. Terminology and voice (`T`)

Against `visualcron-documentation-standards.md` and `visualcron-glossary.md`. **Run the grep before
recording the result**, and score **per term per page**, not per occurrence.

Banned: hit, drop-down (any spelling), hamburger, dialog box. Job/Task confusion. Glossary "do not
use" terms (Agent and Engine for the Server, Console or Portal for the Client, Frequency or Schedule as
an object, and so on).

#### Client vocabulary — owner rule, 2026-10-20

**A word the Client uses as the name of a control or an action is not banned, in any use**, generic
or naming the element. It is never a terminology finding. This replaces the scoped rule of
2026-10-07, under which these words were allowed only when they named the product element. A word
counts when the Client shows it as a NAME (label, control or element type, event, activity, option,
value, Task type); a word found only in PROSE (tooltip, message, help text) does not.

Client vocabulary on 2026-10-20 (all NAME-level; table below has the evidence): click, execute,
check / uncheck, turn on / turn off, navigate to, launch, icon, checkbox, toggle, radio button, text
box, **combo box**, modal, screen. Still banned: hit, drop-down, hamburger (no product use) and dialog
box (PROSE only). The standards' decision-tree verbs (Select, Clear, Run, Go to) stay the recommended
wording for drafted text, but the Client's word is never deducted.

| Sentence | Verdict |
|---|---|
| "Click the _Save_ button." | Allowed: Client vocabulary (no finding) |
| "Select a value in the combo box." | Allowed: Client vocabulary |
| "The Trigger fires on *Checkbox clicked*." | Allowed: names a Desktop Trigger event |
| "Hit _Save_." | **Finding:** banned verb |
| "Pick a value from the drop-down." | **Finding:** banned UI term |
| "The Agent runs your Jobs." | **Finding:** "Agent" used as a name for the VisualCron Server (glossary) |

#### The product-language exemption — owner rule, 2026-10-07

Any word, including a still-banned one and a glossary "do not use" term, is used exactly as the Client
shows it when the page refers to that product element: a Task type, activity, event, option, label or
value keeps its name, casing and spelling, in italics. Load balancing *Server Agents* and MFT
*Endpoints* are used normally.

For a still-banned word or a glossary term, the test for each hit: **does the sentence name, quote or describe a specific product feature,
label, option, value, activity, event or Task type that uses this word?** If yes, it is exempt. Quote
labels exactly as the Client renders them, in italics.

**Prove the label is what the Client renders before exempting it.** Enum-backed lists usually display
the member's description attribute, not its name. A page that quotes the run-together code name of a
member, where the Client shows the spaced, readable description, is an accuracy finding, not product
language. For every exempted term, find the code that sets the displayed text (a language-resource
lookup, an enum description, a designer label).

**The evidence comes from code, not memory.** The private product-terms script
(`product_terms.py --code "$VC_CODE_EXPORT"`, see "Private companions" in `SKILL.md`) builds a corpus
of every user-visible English string in the product (the English language resources, runtime labels,
description and display-name attributes, designer labels, XAML, in-product object descriptions and
enum names). It reports, per term, the product's NAME uses and PROSE uses. `--term <word>` lists every
hit with its source. Re-run it when the snapshot changes rather than
editing the table below by hand.

Product uses found on 2026-10-07, re-checked 2026-10-20 (NAME-level unless noted):

| Term | Where the Client uses it as a name |
|---|---|
| click | Robot/web macro activities *Click*, *Double Click*, *Click Element*, *Action - Click*, *Step - Click*; Desktop Trigger events *Button clicked*, *Checkbox clicked*, *Textbox clicked*, *Window clicked*, *Label clicked* |
| execute | Task types *Execute*, *Remote Execute*, *Assembly Execute*, *Execute Script*, *Execute SSIS package*; labels *Execution time*, *Last executed*, *Executed by*, *Execution Id*; load-balancing *Agent Execute Type* |
| check / uncheck | Labels such as *Check every*, *Check port*, *Check VM*, *Don't check*; Desktop Trigger *Checkbox checked* / *unchecked* |
| turn on / turn off | System *Control monitor* options *Turn on* / *Turn off*; Task types *Turn off VM* (VMware) and *Turn Off* (Virtual Server); VM states *Turned off (guest saved)* |
| navigate to | Robot activity *Navigate to URL*; web macro step *Navigate to* |
| launch | Task *EC2 - Launch instance*; VMware Start VM option *Launch GUI*; SharePoint *Quick launch*; web macro *Launch New Instance*; *VisualCron Server Launcher* |
| icon | Popup Task *Icon type*; shortcut *Icon location*, *Path to Shortcut icon*; file explorer *Icons* view |
| checkbox / check box | Popup Task input type *Check Box*; Desktop Trigger element *Checkbox* and its events |
| toggle | PDF Sign option *Toggle no view* |
| radio button | Popup Task input type *Radio Button*; Desktop Trigger element *Radio button* and its events |
| text box | Desktop Trigger element *Textbox* and its events |
| combo box | Popup Task input type *Combo Box*; Desktop Trigger element *Combobox* and its events (*Combobox opened*, *Combobox clicked*) |
| modal | Popup Task option *Modal window* |
| screen | Task *Image Capture Screen*; VMware guest *Capture screen*; Robot *Set Full Screen Mode*, screenshot *Screen*; key *PRINT SCREEN* |
| dialog box | PROSE only: the web macro activity that responds to a browser *JavaScript dialog box*. **Still banned**; exempt only when referring to that browser dialog. |
| hit, drop-down, hamburger | **No product use.** Still banned. |

The glossary's "do not use" terms are already scoped ("as a synonym for..."), so the same test
applies. Each of these is also product language:

| Term | Product language | Still a finding when used as... |
|---|---|---|
| agent | Load balancing *Server Agents* (*Agents* menu, *Agent select*); SNMP *Agent IP Address*; IIS / HTTP *User Agent* | a name for the VisualCron Server |
| endpoint | MFT Server *FTP/SFTP/HTTP Endpoints*; *Token endpoint/URL*; *Custom endpoint* | a synonym for Connection |
| step | Web macro *Steps* and *Step - ...* names; SQL Task *Job steps* | a synonym for Task |
| action | Robot/web macro *Action - ...* names; Robot error handling *Error Action*; *Action type* | a synonym for Task or Task type |
| activity | Robot *Activities settings*, *Activities repository*, *Activity Error Action* | a synonym for Task type |
| process | Process Task category; *Process id*, *End process*; Process Trigger and Condition | a synonym for Job |
| event | Event Triggers; *Event Log*; Desktop Trigger *Key event*; *Job events* | a synonym for Notification |
| schedule | the Client ribbon's *Schedule* group; PeopleSoft *Process Schedule* and *Schedule PSQuery* Tasks | a noun for a Trigger or a container of Jobs |
| dependency | *Trigger dependency* | a synonym for Condition |
| property, token, profile, threshold, engine, console, alert, command type | e.g. *Property Name*, *Access token*, *SAS token*, *Load profile*, *Multipart upload threshold*, *JSON filter engine*, a *console session* (Session change Event Trigger), *Set Display Alerts*, the FTP *Command type* field | the synonym the glossary names |
| frequency, batch user, service account, portal | **No product use** | always |

#### Other exclusions

**The sweep tells you where to look, not what to conclude.** Before recording, also exclude:

| Hit | Why it is not a violation |
|---|---|
| `right-click` | The one sanctioned exception. Form: `Right-click the X and select Y`, never "right-click on". Use `(^|[^-])\bclick\b`. |
| A banned word inside a **literal UI label** | Covered by the exemption. If the label itself reads badly, report it as an engineering item, not a docs finding. |
| `Client` | **Not banned here.** "VisualCron Client" is the product's name for its desktop application. |
| A historical changelog entry | A release record. Never edited for style. |
| Image file names and URLs | Not prose. |

This exemption was added to rubric VC 1.0 before any unit was assessed, so no report is affected and
the version is unchanged. Any later change to it is a rubric change and needs a version bump.

**VC object nouns are capitalized**: Job, Task, Trigger, Condition, Connection, Credential,
Notification, Variable, Server, Client. Casing drift is Low, once per page.

Banned terms are pervasive in this corpus (`click` on about 420 pages before any uplift). Expect
terminology to be the largest single source of deductions in early units. That is a real finding about
the corpus, not a calibration error. Report it on its own row in the axes table so it does not hide
accuracy problems behind a low number.

### 6. Front matter and registration (`F`)

**VC convention** — and it is the only one that applies here:

| Requirement | Severity if missing or wrong |
|---|---|
| Front matter fenced by `---` on line 1 | Medium. Two pages start `1---`, which renders the YAML as body text. |
| `sidebar_label` present, single-quoted, in the corpus naming pattern (`Task File - Copy`, `Event Trigger - File`, `Connection - SFTP`) | Low; Medium if absent |
| `hide_title: 'true'` | Low. Without it, Docusaurus renders a second title. |
| Page registered in `sidebars.js` | Medium. The CHM table of contents is built from the sidebar, so an unregistered page is missing from in-product help too. |
| Page mapped in `chm-config.json` | Low, unless a code HelpLink targets it, in which case axis 7. |

**`title`, `description` and `tags` are not required and their absence is not a finding.** No page in
the corpus has them; the house convention is `sidebar_label` plus `hide_title`, as this repository's
`CLAUDE.md` states.

### 7. Links, images and help context (`L`)

- Internal links and anchors resolve. `onBrokenLinks: 'throw'` fails the build — High in a procedure,
  Medium elsewhere.
- Images exist at their referenced paths.
- **Alt text**: the standard requires it, and 1,235 of 1,238 image references have none. Score it
  **Low, once per page**, not per image. It is in-process — the images can be read — but it is slow
  work; say so in the ceiling discussion rather than leaving it out.
- **VC help context.** The product's F1 and help buttons open the CHM page named by the code's
  HelpLink, resolved through `chm-config.json` to a page:
  - a reachable object whose HelpLink has no `chm-config.json` mapping — **Medium**; in-process when
    the target page exists (add the mapping), engineering item when the HelpLink itself is wrong
  - a mapping whose `mdFile` no longer exists — **Medium**
  - **never rename or move a docs file, and never change a `chmFile` value, to fix anything.** The
    `chmFile` names are a contract with compiled product code. Renaming one breaks F1 in every
    installed Client.

### 8. Version and release currency (`V`)

- Behavior or fields added in a release carry a version note where the changelog dates them.
- **Changelog drift**: a user-visible changelog entry since the last substantive edit of the page,
  with no corresponding change on the page — Medium, Tier E unless code confirms the change.
- A page presenting a capability the changelog says was removed, with no note — High.
- Very old "since 5.x / 6.x" notes are **not** findings until the owner states the oldest supported
  version. Record the count in the report as a question.
- **Do not document what has not shipped.** A capability in the code snapshot with no changelog entry
  may be unreleased. That is an owner question, not a coverage gap.

### 9. Exposure (`X`)

**The repo is public and publishes to help.visualcron.com.** The code is not.

| Finding | Severity |
|---|---|
| Credential material, signing material, license or activation internals, support-code mechanics | High |
| An internal host name, machine name, user name, or internal service endpoint — **including inside a screenshot** | High |
| Internal class, form, control or namespace names in prose (the source's class, form and user-control naming prefixes, internal project names) or a source snippet | High |
| Support-only command-line actions documented as customer-facing | High |
| Edition-gating described by mechanism rather than by edition | Medium |
| Stale internal test artifacts (old Job names, dates, IDs) in examples or screenshots | Low |

Calibrate before reporting. A class name that the product itself prints into a log the customer
receives passes the see/set/receive test. `192.168.1.1` in an example is a textbook address. Over
2,000 screenshots exist: sweep the unit's images with Windows OCR (`Windows.Media.Ocr` through
PowerShell) for host and user names rather than reading them by eye.

Repository-level exposure (outside a page) is not a page finding; it goes in the engineering-items
file.

## Evidence tiers

Carried from vc-doc-analyzer. Record on every Accuracy, Coverage and Version finding.

| Tier | Source here |
|---|---|
| A | The code snapshot |
| B | Compiled assemblies from an installed build |
| C | A live non-production Server: Web API, `VCCommand.exe` help output, the Client itself |
| D | Exported Job/settings XML |
| E | The changelog alone |

A finding backed only by Tier E is **High-or-whatever-it-is, Tier E, needs confirmation** — it is not
demoted, and it does not go to phase 3 until something above E confirms it.

## Achievable ceiling

Classify each finding:

- **In-process** — fixable from the code snapshot and the standards.
- **Needs SME** — needs knowledge no available source holds: unreleased-or-not, Client behavior no
  source explains, a screenshot that must be retaken from a running Client, the supported-version
  window, a publishing decision.

**Ceiling = 100 − (sum of deductions for needs-SME findings)**, per page, averaged like the score.

## Finding IDs

`<axis-letter>-<NNN>`, numbered per unit report: `A` accuracy, `C` coverage, `I` prerequisites, `S`
structure, `T` terminology, `F` front matter, `L` links/help context, `V` version, `X` exposure.
Phase 4 reuses the phase 1 ID.
