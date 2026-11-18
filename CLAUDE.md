# VisualCron Documentation — Claude Code Project

This repository contains the VisualCron product documentation site built with Docusaurus.

## Claude skills in this repository

Three skills are bundled under `.claude/skills/`. They work together: the analyzer finds gaps, the uplift program scores and fixes them unit by unit, and the technical writer enforces the standards on every page that changes.

| Skill | Location | What it is for | When to use it |
|---|---|---|---|
| `visualcron-technical-writer` | `.claude/skills/visualcron-technical-writer/` | The VisualCron documentation standards: terminology, voice, structure, formatting, page types | Writing, reviewing, or editing any page in `docs/` (see below) |
| `vc-doc-analyzer` | `.claude/skills/vc-doc-analyzer/` | Read-only gap analysis of the docs against the product surface (source, assemblies, Web API, exported XML, or changelog), with evidence tiers and an impact rubric | Auditing docs against the product: "what's missing", "is this still accurate", "compare the docs to the product" |
| `visualcron-docs-uplift` | `.claude/skills/visualcron-docs-uplift/` | The assessment and uplift program: fixed units, a fixed scoring rubric, branded pre/post .docx reports, gated phases, local commits | Scoring, assessing or uplifting a unit of the docs ("pre-assess the File Tasks docs", "run the post-assessment for tasks-net", "where does the uplift stand") |

### Environment for the analyzer and the uplift program

| Variable | Meaning |
|---|---|
| `VC_CODE_EXPORT` | The local, private export of the VisualCron source. It is never part of this repository, and its paths, file names and class names are never published. |
| `VC_DOCS_ASSESSMENTS` | Where the uplift program writes its internal reports. Default: `%OneDrive%\VisualCron-docs-assessments`. |
| `VC_SKILL_PRIVATE` | The folder that holds the uplift program's private companions. Not in this repository. |

The uplift program also uses three private companions (a code map and two scripts that read the source). They are kept in the folder named by `VC_SKILL_PRIVATE`, and are not in this repository.

### Publishing

Publishing is the owner's decision. Never push a branch or open a pull request without the owner's explicit go-ahead. Commit messages and added lines are written to be public: no source paths, file names, class names, line citations, scores or local paths. The uplift skill lists the leak greps to run before every commit.

## VisualCron Technical Writer Skill

A technical writer skill and its resource files are bundled in this repository at `.claude/skills/visualcron-technical-writer/`. The skill enforces VisualCron documentation standards for terminology, voice, structure, and formatting.

### Skill Location

```
.claude/skills/visualcron-technical-writer/
├── SKILL.md                                  # Skill definition, guardrails, and operating modes
└── resources/
    ├── visualcron-documentation-standards.md   # Action verbs, UI terms, formatting rules, pattern library, pre-flight checklist
    ├── visualcron-documentation-types.md       # Conceptual / Procedural / Reference templates
    ├── visualcron-glossary.md                  # Controlled vocabulary — preferred terms and "do not use" terms
    ├── visualcron-learner-roles.md             # Audience profiles and tone guidance per role
    ├── visualcron-golden-examples.md           # Reference examples for each documentation type
    ├── visualcron-api-reference.md             # .NET API, PowerShell, Web API (REST/SOAP), and VCCommand templates
    ├── visualcron-parameter-descriptions.md    # Patterns for field, tooltip, and parameter description text
    └── visualcron-primary-analysis.md          # 13-section feature page template used to score page completeness
```

### Using the Skill

Invoke the skill when writing, reviewing, or editing documentation pages. The skill operates in four modes:

| Mode | Trigger words | Behavior |
|---|---|---|
| **Write** | "Write," "Create," "Draft" | Produce complete documentation matching the page type template |
| **Review** | "Review," "Check," "Audit" | Report violations with line references and suggested fixes |
| **Edit** | "Fix," "Update," "Revise" | Apply targeted changes while preserving compliant content |
| **Consult** | "Should I," "How do I" | Provide guidance from the standards without producing output |

### Automatic invocation on document changes

Apply the visualcron-technical-writer skill automatically whenever you work on `.md` files in `docs/`:

| Situation | Mode | Required action |
|---|---|---|
| You edit an existing `.md` file in `docs/` | Edit | Run the skill before reporting the task complete — fix all violations found |
| You create a new `.md` file in `docs/` | Write | Produce a compliant page from the start using the correct page type template |
| User asks you to review or audit docs | Review | Report all violations with file path, line number, and suggested fix |
| User asks "should I" or "how do I" about standards | Consult | Answer from the standards without producing output |

Do not report a documentation task as complete until the skill has run and all violations are resolved.

### Guardrails

The skill's guardrails override all other guidance:

- **Never invent information.** Every claim, setting, workflow, UI label, field name, and example must come from the VisualCron product, its documentation, or the in-product API reference
- **Never fabricate data, examples, or settings**
- **Flag gaps explicitly** — state which section is affected, what is missing, and what source would resolve it
- **Verify UI labels and element types from the Client** before writing a procedural step
- **Verify feature behavior before writing** — never write from memory or inference

### Key Standards

- **Terminology**: Job (container) vs Task (unit of work), Trigger, Condition, Dependency, Notification, Connection, Credential, Variable, VisualCron Server, VisualCron Client, Grid. Never use: hit, drop-down, hamburger, dialog box, or "task"/"process" as a synonym for a Job. Words the Client uses as control or action names (click, execute, check, launch, checkbox, combo box, and others) are Client vocabulary and are allowed in any use; product names and labels are kept exactly as the Client shows them
- **Voice**: Second person ("you") for instructions. No first person ("we," "our"). Present tense for descriptions, imperative for steps.
- **Formatting**: _Italics_ for UI elements, **_bold italics_** for tab names, `->` for menu paths, `"double quotes"` for values, paths, and file names
- **Structure**: Numbered steps for procedures, one action per step. Lead-in sentence required: "To [goal], complete the following steps:"
- **Front matter**: Every page requires `sidebar_label` and `hide_title: 'true'`, and opens with a `## H2` heading
- **Change notes**: Documentation for a new feature or improvement also requires a `docs/changelog.md` entry
- **Registration**: A new page must be added to both `sidebars.js` and `chm-config.json`, or it is unreachable in the website and the CHM

---

## Repository Structure

```
docs/                    # Primary documentation pages
src/                     # Docusaurus theme customizations
static/                  # Images and static assets
scripts/                 # Build and CHM generation scripts
sidebars.js              # Website navigation structure
chm-config.json          # CHM topic structure
docusaurus.config.js     # Site configuration
```

## Running Locally

```bash
yarn install
yarn start
```
