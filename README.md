# VisualCron Documentation

Docusaurus-powered documentation site for VisualCron. Also produces a CHM (Compiled HTML Help) file for the desktop application's built-in help system.

## Prerequisites

- Node.js 18+
- Yarn (`npm install -g yarn`)
- [HTML Help Workshop](https://web.archive.org/web/20200918004813/https://www.microsoft.com/en-us/download/details.aspx?id=21138) (Windows only, required for CHM compilation)

## Getting Started

```bash
cd visualcron-docs
yarn install
yarn start
```

This launches a local Docusaurus dev server with hot reload at `http://localhost:3000`.

## Available Scripts

| Command | Description |
|---|---|
| `yarn start` | Local Docusaurus dev server |
| `yarn build` | Production Docusaurus build |
| `yarn build:chm` | Generate CHM source files to `chm-output/` |

## CHM Build

The CHM is built locally in two steps:

```
yarn build:chm                    # 1. Generate .htm files, .hhp project, .hhc TOC, .hhk index
hhc.exe chm-output/VisualCron.hhp    # 2. Compile into VisualCron.chm (returns exit code 1 on success)
```

`hhc.exe` is installed with HTML Help Workshop, typically at `C:\Program Files (x86)\HTML Help Workshop\hhc.exe`.

## Key Files

| File | Purpose |
|---|---|
| `chm-config.json` | Maps doc IDs to `.htm` filenames, labels, and VC source references |
| `scripts/build-chm.js` | Reads `chm-config.json` + Markdown sources, emits `chm-output/` |

## Adding a New Help Topic

1. Create the Markdown file under `docs/` and add it to `sidebars.js`.
2. Add a mapping entry in `chm-config.json` with `chmFile`, `mdFile`, `label`, and (if applicable) `helpKeywordSources`.
3. Run `yarn build:chm` and compile with `hhc.exe` to verify the topic appears in the CHM.
