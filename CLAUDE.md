# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Docusaurus 3.9.2 site for the VisualCron documentation at https://help.visualcron.com. The same Markdown sources are also compiled into a CHM (Compiled HTML Help) file shipped with the VisualCron desktop app for F1-help.

Stack: Docusaurus classic preset, React 18, Node.js 18+, Yarn. No ESLint/Prettier/Biome configured.

## Project layout

```
help.visualcron.com/         <- usual CWD; NOT a git repo, just a container
├── chm_extracted/           <- historical CHM dump, reference only; do not edit
└── visualcron-docs/         <- THIS repo (smatechnologies/visualcron-docs, branch: main)
    ├── docs/                <- Markdown sources (the only thing you usually edit)
    ├── sidebars.js          <- navigation tree
    ├── chm-config.json      <- doc-id -> .htm filename + label mapping for CHM
    ├── scripts/build-chm.js <- generates chm-output/ from docs/ + chm-config.json
    ├── chm-output/          <- generated; never edit
    └── build/               <- Docusaurus output; never edit
```

## Commands

| Command | What it does |
|---|---|
| `yarn start` | Dev server with hot reload at http://localhost:3000 |
| `yarn build` | Production Docusaurus build. `onBrokenLinks: 'throw'` -> internal link rot fails the build. Run this before pushing. |
| `yarn build:chm` | Generates `chm-output/` (.htm, .hhp, .hhc, .hhk) |
| `hhc.exe chm-output/VisualCron.hhp` | Compiles the final `.chm`. Requires HTML Help Workshop (Windows-only). **Exit code 1 means success** (not failure). |

## Adding a new help topic

Both files must be updated, or the topic is unreachable in one of the two outputs:

1. Create `docs/<slug>.md` and add it to `sidebars.js`.
2. Add a mapping entry in `chm-config.json` (`chmFile`, `mdFile`, `label`, optional `helpKeywordSources`).
3. `yarn build` to verify (catches broken links).
4. `yarn build:chm` + `hhc.exe chm-output/VisualCron.hhp` if you need to verify CHM output locally.

## Editing existing topics — do not rename `chmFile` entries

The `chmFile` values in `chm-config.json` are anchor targets that the VisualCron desktop app links to from F1-help (via `helpKeywordSources`). Renaming a `chmFile` silently breaks F1-help in shipped builds. Change `label` and `mdFile` freely; treat `chmFile` as a stable identifier.

## Workflow

- Feature branch -> PR -> merge to `main`.
- Push to `main` triggers `.github/workflows/deploy.yml`, which builds a Docker image and pushes it to the configured registry. There is no separate test/lint step in CI, so `yarn build` locally is the only pre-push gate.

## Conventions

- Use PowerShell for scripts and shell snippets in this codebase (Windows-first environment).
- Avoid em-dashes in any generated content.
