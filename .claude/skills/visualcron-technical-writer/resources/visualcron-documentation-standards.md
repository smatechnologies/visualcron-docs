# Documentation Standards

Writing and formatting rules for all VisualCron documentation. These standards are the single source of truth for style, formatting, and procedural writing decisions. They align with the conventions in the VisualCron docs `documentation-format.md`.

**Primary references (in order of authority):**

1. This document
2. VisualCron docs `documentation-format.md` — the product's own formatting conventions
3. [Merriam-Webster](https://www.merriam-webster.com/) — spelling
4. [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/) — technical writing, UI, and procedures

When this document conflicts with an external reference, this document takes precedence.

---

## Core Principles

- Write for **users and administrators**, not internal teams.
- Be **clear, concise, and consistent**.
- Prioritize **accuracy and completeness** over cleverness.
- Do not document features that are **not released**.
- Assume automation runs **unattended in production** — be explicit about outcomes and side effects.
- Always describe what success looks like (messages, state changes, output).

## Front Matter

Front matter is the first element of every page. Complete it before writing content.

Every Markdown documentation file includes YAML front matter between `---` fences at the top of the file. VisualCron docs use Docusaurus front matter with a hidden auto-title, so the page body opens with a `## H2` heading instead of an H1.

### Fields

| Field | Required | Description |
|---|---|---|
| `sidebar_label` | Yes | The short label shown in the sidebar navigation and used for the CHM topic label. Usually matches or abbreviates the page's H2 heading. Enclose in single quotes. |
| `hide_title` | Yes | Set to `'true'` so Docusaurus does not render a duplicate auto-title above the H2 heading. |
| `slug` | When needed | A custom URL path for the page (for example, the site root uses `slug: '/'`). |

### Template

```yaml
---
sidebar_label: 'Add a Task to a Job'
hide_title: 'true'
---

## Add a Task to a Job
```

### Guidelines

- Every page opens with a `## H2` heading immediately after the front matter, because `hide_title` suppresses the auto-title
- Use `###` and `####` for subheadings within the page
- Keep `sidebar_label` concise — it appears in a narrow navigation column
- When adding a new page, also register it in `sidebars.js` and add a `chm-config.json` mapping entry (see the repo README), or the topic is unreachable in one of the two outputs

---

## Language and Grammar

- Use **second person**: "you," not "we"
  > **Exception:** Pages where VisualCron (the company) describes its own
  > processes or policy may use first person ("we"). This is rare — most
  > documentation is instructional and uses second person.
- Use **active voice**, especially in procedures
- Use **imperative verbs** in instructions: "Select," "Enter," "Go to"
- Follow **US English** spelling and punctuation
- One idea per sentence; prefer short sentences over compound ones
- Avoid em-dashes in generated content (per the repo conventions)

---

## Action Verbs

Use the following decision tree for every user interaction. There are no exceptions.

```
Is the user navigating a menu?              → "Go to"
Is the user pressing a physical key?        → "Press"
Is the user running a Job, Task, or query?  → "Run"
Is the user clearing an option?             → "Clear"
Is the user typing into a field?            → "Enter"
Is the user opening a context menu?         → "Right-click"
Everything else (buttons, options, tabs,
  links, fields, list selections)           → "Select"
```

### Quick Reference

| Action | Verb | Example |
|---|---|---|
| Menu navigation | Go to | Go to _Server_ -> _Settings_ -> _Main settings_. |
| Button | Select | Select the _Save_ button. |
| Option (checkbox) | Select / Clear | Select the _Run once_ option. |
| List selection | Select + pick | Select the _Task type_ field and pick _Execute_ from the list. |
| Tab | Select | Select the **_Tasks_** tab. |
| Link | Select | Select the _Manage Connections_ link. |
| Field entry | Enter | In the _Name_ field, enter the Job name. |
| Keyboard key | Press | Press the _Enter_ key. |
| Context menu | Right-click | Right-click the Job in the Grid and select _Run_. |
| Job, Task, or query | Run | Run the Job. |
| Clearing | Clear | Clear the _Run once_ option. |

### Banned Verbs

Never use the following verbs in documentation:

- **click** — use "Select"
- **hit** — use "Press" for keys, "Select" for UI elements
- **execute** — use "Run"
- **check / uncheck** — use "Select" / "Clear"
- **turn on / turn off** — use "Select" / "Clear"
- **navigate to** — use "Go to"
- **launch** — use "Open" for applications or "Start" for the service

### Negative Examples

```
✅ Select the _Save_ button.
❌ Click the Save button.
❌ Click _Save_.

✅ Go to _Server_ -> _Settings_ -> _Main settings_.
❌ Navigate to Server > Settings > Main settings.
❌ Click on the Server menu.

✅ Select the _Run once_ option.
❌ Check the Run once checkbox.
❌ Turn on the Run once toggle.

✅ Select the _Task type_ field and pick _Execute_ from the list.
❌ Click the Task type dropdown and choose Execute.

✅ Right-click the Job in the Grid and select _Run_.
❌ Right-click on the Job and click Run.
```

### Additional Notes

The word "right-click" is the ONE exception to the ban on "click." It is permitted because:

- There is no clear alternative verb for opening a context menu
- VisualCron legitimately relies on right-click context menus in the Grid
- The pattern "Right-click [element] and select [option]" is concise and unambiguous

Rules for using "right-click":
- Always hyphenate: "right-click," not "right click"
- Never follow with "on": "Right-click the **Job**," not "Right-click on the Job"
- Always pair with "and select" for the menu option that follows
- Only use for actual context menus

---

## UI Element References

VisualCron documentation uses **italics** for UI element names, following `documentation-format.md`. This differs from products that bold every UI element.

| Element | How to Refer to It | Example |
|---|---|---|
| Button | _Label_ + "button" | Select the _Save_ button. |
| Checkbox | _Label_ + "option"; select/clear | Select the _Run once_ option. |
| Radio button | _Label_ + "option" | Select the _Interval_ option. |
| Drop-down / list | Use "list," never "drop-down" | Select _Execute_ from the list. |
| Field | Exact _label_ + "field" | In the _Name_ field, enter the value. |
| Tab | **_Bold italics_**, tab name only | Select the **_Tasks_** tab. |
| Menu navigation | "Go to" + `->` path in italics | Go to _Server_ -> _Settings_. |
| Dialog / window | "dialog" or "window" + its name | The _Add Job_ dialog is displayed. |
| Value, path, or file name | Double quotes | Save the file to `"C:\Program Files (x86)\VisualCron"`. |
| Placeholder | Angle brackets in code font | Enter `<server name>` in the field. |

### Formatting Conventions (from `documentation-format.md`)

| Convention | Meaning |
|---|---|
| _Italics_ | Menu item, button, or parameter name (UI elements) |
| **Bold** | A defined word or expression, a note label, or a paragraph name |
| **_Bold italics_** | Tab name |
| `"value"` | A specific expression, parameter value, path, or file name |
| `<name>` | Placeholder for a specific name |
| `->` | Menu navigation (for example, _Server_ -> _Settings_ -> _Main settings_) |

### Banned UI Terminology

Never use these terms in documentation:

- **drop-down** (any variation) — use "list" or "field"
- **icon** — treat as a button if it performs an action
- **checkbox** — use "option"
- **toggle** — use "option"
- **radio button** — use "option"
- **hamburger** — use the label or "menu button"
- **text box** — use "field"
- **dialog box** — use "dialog" or "window"
- **modal** — use "dialog" or "window"
- **screen** (as a UI element name) — use "page," "dialog," "window," or "area"; "screen" is acceptable only for the physical display

---

## Menu Paths

For menu navigation, use the `->` convention with each label in italics. Do not bold or italicize the `->` separator.

```
✅ Go to _Server_ -> _Settings_ -> _Main settings_.
❌ Go to **Server > Settings > Main settings**.
❌ Navigate to Server > Settings > Main settings.
```

Use `->` paths for sequential navigation within the menu. For more complex flows that leave the menu, use separate numbered steps.

---

## Formatting

### Headings and Titles

- Use **sentence case** for headings you write
- The page opens with a `## H2` heading (auto-title is hidden); use `###`/`####` for subsections
- Do not create new styles or override platform defaults

### Emphasis

- Use _italics_ for UI element names (buttons, fields, options, menu items, parameters)
- Use **_bold italics_** for tab names
- Use **bold** for a defined term or a note label
- Match UI element names to the product **exactly**, including capitalization. Never apply sentence case or title case to a UI label.

```
✅ Select the **_Tasks_** tab.
✅ Select the _Add Job_ button.
❌ Select the **_tasks_** tab.
❌ Select the _add job_ button.
```

### Values, Paths, and Code

- Use double quotes for specific values, parameter values, paths, and file names: Save to `"C:\ProgramData\VisualCron"`.
- Use fenced code blocks for multi-line commands, scripts, API calls, and variable examples.
- Use inline code font for VisualCron variables in running text, for example `{DATE(Now)}`.

### Lists

- **Numbered lists** → sequential or ordered steps (procedures)
- **Bulleted lists** → unordered or descriptive content
- Do **not** end bulleted list items with periods
- **Do** end numbered procedural steps with periods
- Introduce every list with a heading, a complete sentence, or a fragment ending with a colon

### Dates

- Use an unambiguous format. The VisualCron changelog uses **YYYY-MM-DD**; match that format in release/change content. Elsewhere, spell the month if there is any ambiguity.

---

## Procedural Instructions

Procedures explain **how to do something** and must be predictable and scannable.

### Required Rules

1. Open with: "To [accomplish goal], complete the following steps:"
2. Use **numbered lists** for all steps
3. **One action per step** — do not combine actions
4. End the procedure with a **result statement** describing what the user sees or what changed
5. Break procedures longer than **~10 steps** into linked sections
6. Reuse wording and structure — **repetition improves usability**

### Step Structure

```markdown
To add a Task to a Job, complete the following steps:

1. In the Grid, right-click the Job and select _Edit_. The _Edit Job_ dialog is displayed.
2. Select the **_Tasks_** tab.
3. Select the _Add_ button. The _Add Task_ dialog is displayed.
4. Select the _Task type_ field and pick a Task type from the list.
5. In the _Name_ field, enter a name for the Task.
6. Select the _Save_ button. The Task is added to the Job.
```

### Sub-Steps

Use letters for nested actions within a step:

```markdown
1. Configure the Trigger:
   a. Select the **_Triggers_** tab.
   b. Select the _Add_ button.
   c. Select the _Time_ option and configure the interval.
```

### Optional Steps

Mark optional steps explicitly:

```markdown
4. (Optional) Select the _Run once_ option.
```

### Tables in Procedures

Use tables when users must choose between options within a step.

- Introduce the table in the step text
- Indent the table — and any note preceding it — with **4 spaces** to keep it attached to the step in Docusaurus
- Always explain the **consequences** of each option

```markdown
2. Select the Trigger type you need:

    :::note
    A Job can have multiple Triggers. By default they combine as an OR
    relationship — any one of them can start the Job.
    :::

    | Option | Use when |
    |---|---|
    | **Time Trigger** | You want the Job to run on a time schedule |
    | **Event Trigger** | You want the Job to run in response to a system event |

3. Select the _Save_ button. The Trigger is added to the Job.
```

### Linking to Other Procedures

When a procedure references steps documented elsewhere, link rather than duplicate:

```markdown
1. [Create a Connection](../server/global-connections.md) for the FTP server.
```

---

## Pattern Library

Match each new task to the closest pattern.

### Pattern 1: Simple Run

```markdown
To run a Job manually, complete the following steps:

1. In the Grid, select the Job.
2. Select the _Run_ button on the toolbar. The Job starts and its status updates in the Grid.
```

### Pattern 2: Configuration / Settings

```markdown
To configure email settings, complete the following steps:

1. Go to _Server_ -> _Settings_ -> _Main settings_.
2. Select the **_Email_** tab.
3. In the _SMTP server_ field, enter the server address.
4. In the _Port_ field, enter the port number.
5. (Optional) Select the _Use SSL_ option.
6. Select the _Save_ button. The settings are saved.
```

### Pattern 3: Create Then Configure

```markdown
To add a Job, complete the following steps:

1. On the toolbar, select the _Add Job_ button. The _Add Job_ dialog is displayed.
2. In the _Name_ field, enter a name for the Job.
3. Add at least one Trigger and one Task.
4. Select the _Save_ button. The Job is added to the Job List.
```

### Pattern 4: Multi-Option Step

```markdown
3. Select an output format:
   - For plain text: add `/text/` to the request URL.
   - For JSON: add `/json/` to the request URL.
   - For XML: add `/xml/` to the request URL.
```

### Pattern 5: Long Procedure (Broken Into Sections)

When a procedure exceeds ~10 steps, break it into named sections and link between them:

```markdown
## Step 1 — Install the Server

1. Run the VisualCron installer on the server.
2. Complete the installation wizard.

## Step 2 — Start the service

1. Open the Windows Services console.
2. Right-click the _VisualCron_ service and select _Start_.
```

---

## Risk Callouts

Use Docusaurus admonitions, which VisualCron docs already use. Match the level to the risk.

| Level | Syntax | Use For |
|---|---|---|
| Note | `:::note` | Helpful, non-critical information — tips, clarifications, reminders |
| Info | `:::info` | Additional context worth highlighting |
| Tip | `:::tip` | A recommended approach or shortcut |
| Warning | `:::warning` | Risk of data loss, failed automation, or configuration damage |

```markdown
:::note
The VisualCron Server service runs as LOCALSYSTEM. Use a Credential to
run a Task under a specific user account.
:::

:::warning
Deactivating a Job stops all of its Triggers. Scheduled runs will not
occur until the Job is activated again.
:::
```

### Placement

- **Applies to a specific step decision** → indent it within that step, before the table, at 4 spaces
- **Applies to the entire procedure** → place it before the opening "To [goal]…" sentence
- **Applies to a post-procedure result** → place it after the final result statement

---

## Images

Include images **only when they add clarity** — when a step involves a UI element the reader must visually identify.

- Use **PNG** format and store under `static/img/`
- Provide **alt text** for every image
- Maintain **aspect ratio** when resizing
- Reference images with a relative path, for example `![Add Job dialog](../../static/img/add-job.png)`

---

## Content Reuse

- If a procedure is identical across pages, write it once and link to it
- If a procedure is similar but role-specific, write separate versions and note the differences
- Never copy-paste content between pages — duplicated content creates maintenance debt
- Use "Related topics" links to connect shared concepts

---

## Release / Change Notes

VisualCron records releases in `docs/changelog.md`. Match the existing structure.

### Structure

Each release is a `###` heading with the version and date, followed by grouped entries:

```markdown
### 13.3.1 [2026-07-20]

#### Features

:star: Client/Server: Full Output Retention Across Task Runs (VCPCM-2802)

#### Bug Fixes

:white_check_mark: Client: Credential Password Lost After Service Restart (VCPCM-3648)
```

### Entry Guidelines

- Version heading format: `### <version> [YYYY-MM-DD]`
- Group entries under `#### Features` and `#### Bug Fixes`
- Prefix feature entries with `:star:` and bug-fix entries with `:white_check_mark:`
- Start each entry with the affected area, for example `Client/Server:`, `Client:`, or `Server:`
- State the change concisely in title case, in customer-facing terms (consult the glossary)
- Include the internal ticket reference in parentheses at the end (for example, `(VCPCM-3481)`) — this matches the existing changelog convention
- One entry per user-visible change

> **Note:** VisualCron's changelog intentionally includes ticket references and area prefixes. Follow the existing file's convention rather than importing a different release-notes style.

---

## Pre-Flight Checklist

Before finalizing any documentation, verify:

### Content

- [ ] Feature is released
- [ ] Uses correct VisualCron terminology (consult glossary)
- [ ] Appropriate for the target audience role (consult learner-roles)
- [ ] Risks are called out with the appropriate admonition

### Formatting

- [ ] Front matter present with `sidebar_label` and `hide_title: 'true'`
- [ ] Page opens with a `## H2` heading
- [ ] UI element names are in _italics_ and match the product exactly
- [ ] Tab names use **_bold italics_**
- [ ] Menu paths use the `->` convention with italic labels
- [ ] Values, paths, and file names use `"double quotes"`
- [ ] No bulleted list items end with periods
- [ ] All numbered procedural steps end with periods
- [ ] Headings use sentence case

### Procedures

- [ ] Opens with "To [goal], complete the following steps:"
- [ ] One action per step
- [ ] Steps are numbered sequentially
- [ ] Numbered lists have two or more steps — single-action procedures use prose
- [ ] Ends with a result statement
- [ ] No procedure exceeds ~10 steps without a section break
- [ ] Tables in procedures explain the consequences of each option

### Banned Terms

- [ ] No instance of "click" (except "right-click")
- [ ] No instance of "execute" (use "run")
- [ ] No instance of "hit"
- [ ] No instance of "check/uncheck" or "turn on/turn off"
- [ ] No instance of "navigate to" (use "go to")
- [ ] No instance of "drop-down" (use "list" or "field")
- [ ] No instance of "icon" (treat as button)
- [ ] No instance of "checkbox," "toggle," or "radio button" (use "option")
- [ ] No instance of "launch" (use "open" or "start")
- [ ] No misuse of "Job" for "Task" or "Task" for "Job"

---

**When in doubt:** Follow the VisualCron `documentation-format.md` conventions first, then the Microsoft Writing Style Guide, and optimize for clarity over brevity.
