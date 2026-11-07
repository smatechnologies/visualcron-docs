#!/usr/bin/env python3
"""Render the rolling pre/post summary as a Continuous-branded .docx.

The program's per-unit reports are rendered by build_report.py. This script
renders the one document that spans every unit of visualcron-docs:

    <assessments>/VisualCron-docs-pre-post-summary.json   (state)
    <assessments>/VisualCron-docs-pre-post-summary.docx   (output)

where <assessments> is %VC_DOCS_ASSESSMENTS% if set, else
%OneDrive%/VisualCron-docs-assessments.

The JSON is the source of truth and is edited as the last step of phase 4 --
add the unit's entry, extend the scoreboard, then re-render. Scoreboard rows and
entries keep the keys "repo" and "slug" for schema parity with the OpCon program;
put the unit slug in both.

Branding (fonts, palette, table styling, logo) is imported from build_report.py
rather than duplicated, so the summary always matches the assessments.

Usage:
    python build_summary.py                 # default in/out under <assessments>
    python build_summary.py --state X.json --out Y.docx
"""
import argparse
import json
import os
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Inches, Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    sys.exit("python-docx is required: pip install python-docx")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_report import (  # noqa: E402  - reuse the brand, do not duplicate it
    BLACK_PEARL, SAPPHIRE, PEARL_60, ERROR_RED, SUCCESS_GREEN, WARNING_YELLOW,
    HEAD_FONT, BODY_FONT, heading, para, run, table, label_value,
)

FOLDER = "VisualCron-docs-assessments"
STATE_NAME = "VisualCron-docs-pre-post-summary.json"
OUT_NAME = "VisualCron-docs-pre-post-summary.docx"

STATE_COLOR = {"clear": SUCCESS_GREEN, "blocking": ERROR_RED}


def default_dir():
    explicit = os.environ.get("VC_DOCS_ASSESSMENTS")
    if explicit:
        return Path(explicit)
    root = os.environ.get("OneDriveCommercial") or os.environ.get("OneDrive")
    if not root:
        sys.exit("neither VC_DOCS_ASSESSMENTS nor %OneDrive% is set; "
                 "pass --state and --out explicitly")
    return Path(root) / FOLDER


def cover(doc, d, logo):
    if logo and logo.exists():
        doc.add_picture(str(logo), width=Inches(2.4))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.LEFT
    para(doc, d.get("doc_title", "VisualCron docs program"),
         size=11, color=PEARL_60, bold=True, space_after=2)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(14)
    run(p, d.get("doc_subtitle", "Pre/post summary"),
        size=26, bold=True, color=BLACK_PEARL, font=HEAD_FONT)

    label_value(doc, "Date", d["date"])
    label_value(doc, "Units complete", d["repos_complete"])
    m = d.get("means", {})
    if m and m.get("pre") is not None:
        label_value(doc, "Mean score",
                    "%s -> %s" % (m.get("pre"), m.get("post")), SAPPHIRE)
    blocking = [r for r in d["scoreboard"] if r.get("state") == "blocking"]
    label_value(doc, "Blocking", "%d of %d" % (len(blocking), len(d["scoreboard"])),
                ERROR_RED if blocking else SUCCESS_GREEN)
    if d.get("maintained_by"):
        label_value(doc, "Maintained by", d["maintained_by"])

    for block in d.get("intro", "").split("\n\n"):
        if block.strip():
            para(doc, block.strip(), size=10.5, space_after=6)


def how_to_read(doc, d):
    items = d.get("how_to_read") or []
    if not items:
        return
    heading(doc, "How to read this", 1)
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(4)
        run(p, it, size=10)


def scoreboard(doc, d):
    heading(doc, "Scoreboard", 1)
    if not d["scoreboard"]:
        para(doc, "No unit has completed the program yet. A row is added at the end of each "
                  "unit's phase 4.", size=10.5, italic=True, color=PEARL_60)
        return
    rows = []
    for r in d["scoreboard"]:
        rows.append([
            r["n"], r["repo"],
            "%s (%s)" % (r["pre"], r["pre_letter"]),
            "%s (%s)" % (r["post"], r["post_letter"]),
            r["ceiling"], r.get("corrections", ""), r.get("pages", ""),
            "{:,}".format(r["words_added"]) if isinstance(r.get("words_added"), int) else "",
        ])
    table(doc,
          ["#", "Unit", "Baseline", "Final", "Ceiling", "Corrections", "Pages",
           "Words added"],
          rows,
          widths=[0.3, 2.35, 0.75, 0.7, 0.65, 0.95, 0.6, 0.9])
    for note in d.get("scoreboard_notes") or []:
        para(doc, note, size=9.5, italic=True, color=PEARL_60, space_after=4)


def patterns(doc, d):
    items = d.get("patterns") or []
    if not items:
        return
    heading(doc, "Program-level patterns", 1)
    if d.get("patterns_intro"):
        para(doc, d["patterns_intro"], size=10, space_after=6)
    table(doc, ["Pattern", "Count", "Note"],
          [[p["pattern"], p["count"], p["note"]] for p in items],
          widths=[1.9, 1.0, 4.1])


def repos(doc, d):
    heading(doc, "Per-unit synthesis", 1)
    if not d["repos"]:
        para(doc, "No entries yet.", size=10.5, italic=True, color=PEARL_60)
        return
    for r in d["repos"]:
        title = "%d. %s" % (r["n"], r["slug"])
        move = "%s (%s) -> %s (%s)" % (r["pre"], r["pre_letter"],
                                       r["post"], r["post_letter"])
        heading(doc, "%s   %s" % (title, move), 2)
        if r.get("state") == "blocking":
            para(doc, "BLOCKING", size=9, bold=True, color=ERROR_RED, space_after=3)
        label_value(doc, "Code source", r.get("code", "—"), PEARL_60)
        label_value(doc, "Scope", r.get("scope", "—"), PEARL_60)
        if r.get("lead"):
            para(doc, r["lead"], size=10.5, bold=True, space_after=5)
        for b in r.get("body") or []:
            para(doc, b, size=10, space_after=5)
        if r.get("carried"):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            run(p, "Carried: ", size=10, bold=True, color=WARNING_YELLOW)
            run(p, r["carried"], size=10)
        if r.get("caveat"):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            run(p, "Caveat: ", size=10, bold=True, color=ERROR_RED)
            run(p, r["caveat"], size=10)
        if r.get("credit"):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            run(p, "Worth recording: ", size=10, bold=True, color=SUCCESS_GREEN)
            run(p, r["credit"], size=10, italic=True)


def caveats(doc, d):
    items = d.get("caveats") or []
    if not items:
        return
    heading(doc, "Caveats that survive the score", 1)
    if d.get("caveats_intro"):
        para(doc, d["caveats_intro"], size=10, space_after=6)
    table(doc, ["Unit", "Score", "What remains"],
          [[c["repo"], c["score"], c["remains"]] for c in items],
          widths=[2.2, 0.7, 4.1])
    if d.get("caveats_note"):
        para(doc, d["caveats_note"], size=9.5, italic=True, color=PEARL_60)


def method(doc, d):
    items = d.get("method") or []
    if not items:
        return
    heading(doc, "What the program has learned about its own method", 1)
    if d.get("method_intro"):
        para(doc, d["method_intro"], size=10, space_after=6)
    for i, it in enumerate(items, 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.25)
        run(p, "%d. " % i, size=10, bold=True, color=SAPPHIRE)
        run(p, it, size=10)


def build(d, out_path, logo):
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(10.5)
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Inches(0.8)
        section.left_margin = section.right_margin = Inches(0.9)

    cover(doc, d, logo)
    how_to_read(doc, d)
    scoreboard(doc, d)
    repos(doc, d)
    caveats(doc, d)
    method(doc, d)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
    return out_path


def validate(d):
    missing = [k for k in ("date", "repos_complete", "scoreboard", "repos") if k not in d]
    if missing:
        sys.exit("state file is missing required keys: " + ", ".join(missing))
    sb = {r["repo"] for r in d["scoreboard"]}
    rp = {r["slug"] for r in d["repos"]}
    if sb != rp:
        only_sb, only_rp = sorted(sb - rp), sorted(rp - sb)
        msg = ["scoreboard and per-unit entries disagree:"]
        if only_sb:
            msg.append("  in scoreboard only: " + ", ".join(only_sb))
        if only_rp:
            msg.append("  in entries only: " + ", ".join(only_rp))
        sys.exit("\n".join(msg))
    if len(d["repos"]) != d["repos_complete"]:
        sys.exit("repos_complete says %s but there are %d entries"
                 % (d["repos_complete"], len(d["repos"])))
    for r in d["scoreboard"]:
        if r["post"] > r["ceiling"]:
            sys.exit("%s: final %s exceeds ceiling %s. A post score above the "
                     "ceiling usually means a stale ceiling in the pre-assessment "
                     "after an owner's decision - find out which before rendering."
                     % (r["repo"], r["post"], r["ceiling"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--state", help="path to pre-post-summary.json")
    ap.add_argument("--out", help="output .docx path")
    ap.add_argument("--logo", help="override the bundled logo path")
    args = ap.parse_args()

    state = Path(args.state) if args.state else default_dir() / STATE_NAME
    out = Path(args.out) if args.out else default_dir() / OUT_NAME
    if not state.exists():
        sys.exit("state file not found: %s" % state)

    with open(state, encoding="utf-8") as fh:
        d = json.load(fh)
    validate(d)

    logo = (Path(args.logo) if args.logo
            else Path(__file__).resolve().parent.parent / "assets"
            / "continuous-horizontal-blue.png")
    print(build(d, out, logo))


if __name__ == "__main__":
    main()
