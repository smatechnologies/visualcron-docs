#!/usr/bin/env python3
"""Resolve the visualcron-docs assessment units and inventory their pages.

The docs repo is one corpus of about 720 pages, so the program's unit of work is a
*unit* (a Task category, the Event Triggers, the Connections...) rather than a
repository. references/units.json is the fixed partition. This script is the
only way a page list should be produced: phase 1 records it, phase 4 re-runs
it, and the two must match or the delta is meaningless.

USAGE
    python units.py --docs <repo>/docs check          # partition sanity: exit 1 on any fault
    python units.py --docs <repo>/docs list           # every unit with page and line counts
    python units.py --docs <repo>/docs pages <slug>   # one unit's inventory (path, lines, front matter, first body line)
    python units.py --docs <repo>/docs pages <slug> --json   # same, as JSON for findings.json "pages"

Patterns are fnmatch globs relative to docs/, where "*" also crosses "/".
First match wins, in units.json order.
"""
import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

UNITS = Path(__file__).resolve().parent.parent / "references" / "units.json"


def load_units():
    with open(UNITS, encoding="utf-8") as fh:
        return json.load(fh)


def all_pages(docs):
    # Recursive, always. A single-level listing silently misses subdirectories.
    return sorted(p.relative_to(docs).as_posix()
                  for p in docs.rglob("*") if p.suffix in (".md", ".mdx") and p.is_file())


def assign(docs, cfg):
    pages = all_pages(docs)
    owner, hits = {}, {}
    for u in cfg["units"]:
        for pat in u["include"]:
            hits[(u["slug"], pat)] = 0
    for page in pages:
        for u in cfg["units"]:
            pat = next((p for p in u["include"] if fnmatch.fnmatchcase(page, p)), None)
            if pat:
                owner[page] = u["slug"]
                hits[(u["slug"], pat)] += 1
                break
    return pages, owner, hits


def front_matter(text):
    # Two pages in this corpus start "1---"; report that rather than hide it.
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, lines
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, lines
    fm = {}
    for ln in lines[1:end]:
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", ln)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, lines[end + 1:]


def inventory(docs, page):
    raw = (docs / page).read_bytes()
    text = raw.decode("utf-8", errors="replace")
    fm, body = front_matter(text)
    first = next((l.strip() for l in body if l.strip()), "")
    return {
        "path": "docs/" + page,
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        # Working-tree line endings only: the index stores LF, and core.autocrlf
        # may convert on checkout on Windows, so this says nothing about the repo.
        "crlf_worktree": b"\r\n" in raw,
        "front_matter": fm,
        "opens_with_h2": first.startswith("## "),
        "first_body_line": first[:80],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--docs", required=True, help="path to the visualcron-docs docs/ folder")
    ap.add_argument("cmd", choices=["check", "list", "pages"])
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    docs = Path(a.docs)
    if not docs.is_dir():
        sys.exit(f"not a directory: {docs}")
    cfg = load_units()
    pages, owner, hits = assign(docs, cfg)
    slugs = [u["slug"] for u in cfg["units"]]

    if a.cmd == "check":
        bad = 0
        unmatched = [p for p in pages if p not in owner]
        for p in unmatched:
            print(f"UNMATCHED  {p}")
        bad += len(unmatched)
        if len(set(slugs)) != len(slugs):
            print("DUPLICATE SLUGS in units.json")
            bad += 1
        for (slug, pat), n in hits.items():
            if n == 0:
                print(f"DEAD PATTERN  {slug}: {pat}   (matches nothing, or is shadowed by an earlier unit)")
        empty = [s for s in slugs if not any(v == s for v in owner.values())]
        for s in empty:
            print(f"EMPTY UNIT  {s}")
            bad += 1
        print(f"{len(pages)} pages, {len(owner)} assigned, {len(slugs)} units, units.json v{cfg['version']}")
        sys.exit(1 if bad else 0)

    if a.cmd == "list":
        print(f"{'unit':28} {'pages':>5} {'lines':>7}  title")
        for u in cfg["units"]:
            mine = [p for p in pages if owner.get(p) == u["slug"]]
            lines = sum(inventory(docs, p)["lines"] for p in mine)
            flag = "" if u.get("scored", True) else "  [not scored]"
            print(f"{u['slug']:28} {len(mine):5} {lines:7}  {u['title']}{flag}")
        return

    if a.cmd == "pages":
        if a.slug not in slugs:
            sys.exit(f"unknown unit {a.slug!r}; run 'list' for the slugs")
        rows = [inventory(docs, p) for p in pages if owner.get(p) == a.slug]
        if a.json:
            print(json.dumps(rows, indent=2))
            return
        for r in rows:
            fm = r["front_matter"]
            fm_s = "NO FRONT MATTER" if fm is None else ",".join(sorted(fm))
            h2 = "" if r["opens_with_h2"] else f"  [opens: {r['first_body_line']!r}]"
            print(f"{r['lines']:5}  {r['path']}  ({fm_s}){h2}")
        print(f"{len(rows)} pages, {sum(r['lines'] for r in rows)} lines")


if __name__ == "__main__":
    main()
