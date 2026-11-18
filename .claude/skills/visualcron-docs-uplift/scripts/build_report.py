#!/usr/bin/env python3
"""Render a VisualCron docs unit assessment as a Continuous-branded .docx.

Adapted from the integration-docs-uplift renderer, with the brand unchanged so
both programs' reports look alike. Every report in this program goes through
this script so the pre/post pair for a unit -- and every unit in the corpus --
is laid out identically.

USAGE
    python build_report.py findings.json
    python build_report.py findings.json --out "C:/path/report.docx"
    python build_report.py --schema

With no --out, both phases are written to one folder, because the program has one repo:
    %VC_DOCS_ASSESSMENTS%, default %OneDrive%/VisualCron-docs-assessments/
named visualcron-docs-<unit>-<phase>assessment-<date>.docx, so a unit's pre and
post reports sort next to each other.

FINDINGS JSON SCHEMA
{
  "repo":            "visualcron-docs",               # required, always this value
  "unit":            "tasks-file",                    # required, a slug from references/units.json
  "unit_title":      "File Tasks",                    # optional, shown as the cover title
  "units_version":   "1.0",                           # required, units.json "version"
  "docs_ref":        "279071a on origin/main",        # required
  "phase":           "pre" | "post",                  # required
  "date":            "2026-10-07",                    # required, YYYY-MM-DD
  "rubric_version":  "1.0",                           # required
  "assessed_by":     "Claude Opus 5.5",               # optional

  "code_source": {                                    # required
    "status": "verified" | "candidate" | "none",
    "repo":   "VisualCron source snapshot (local export, no git)",
    "ref":    "13.4.2-era; see snapshot note",
    "note":   "How the snapshot was dated, and version alignment with the docs"
  },

  "summary": "3-5 sentences of plain prose.",         # required

  "repo_score": <score>, "repo_letter": "<letter>",   # required
  "achievable_ceiling": <score>,                      # required
  "blocking": true,                                   # required BOOLEAN (any open High).
                                                      # Prose here is rejected: it was silently
                                                      # dropped and rendered BLOCKED in the
                                                      # OpCon program. Narrative goes in summary.

  "pages": [                                          # required, >=1; from scripts/units.py
    {"path": "docs/<path>.md",
     "lines": <n>, "score": <score>, "letter": "<letter>", "ceiling": <score>}
  ],

  "axes": [                                           # optional but recommended
    {"axis": "Accuracy", "status": "assessed" | "not assessed",
     "high": 1, "medium": 3, "low": 0, "note": "no code source"}
  ],

  "findings": [                                       # required (may be empty)
    {"id": "I-001",
     "axis": "Install",                               # Accuracy|Coverage|Install|
                                                      # Structure|Terminology|
                                                      # FrontMatter|Links|Version
     "severity": "High" | "Medium" | "Low",
     "page": "docs/installation.md",
     "location": "## Prerequisites (L44-52)",
     "issue": "What is wrong.",
     "evidence": "Code file + lines, or a short page quote.",
     "tier": "A" | "B" | "C" | "D" | "E",              # optional, vc-doc-analyzer evidence tier
     "recommendation": "What it should say.",
     "resolvable": "in-process" | "needs-sme",
     "status": "open" | "closed" | "carried"          # post reports only
    }
  ],

  "unverifiable": ["Claim and what would be needed to confirm it."],

  "delta": {                                          # post reports only
    "pre_score": <score>, "pre_letter": "<letter>", "pre_date": "<YYYY-MM-DD>",
    "closed": 12, "carried": 3, "new": 1,
    "note": "Optional prose on comparability."
  },

  "prior_uplift": {                                   # optional, pre and post
    "window": "<YYYY-MM-DD> to <YYYY-MM-DD>",
    "original": "<hash>, <YYYY-MM-DD>",                # state before the earlier uplift
    "handover": "<hash>, <YYYY-MM-DD>",                # state this program started from
    "scale": {"uplift_commits": 4, "files_changed": 30, "pages_before": 29,
              "pages_after": 30, "words_net": 13044},
    "commits": [{"date": "2026-04-20", "title": "Phase 1 documentation uplift"}],
    "prior_assessment": {"date": "2026-06-08", "method": "Own weighted rubric",
                         "score_before": "<letter> (<score>/100)", "score_after": "<letter> (<score>/100, estimated)",
                         "outcome": "Prose."},        # or null
    "attribution": [{"bucket": "Written during the 2026 uplift", "count": 3,
                     "examples": "Prose."}],
    "note": "Prose on what this means for reading the scores."
  }
}

Unknown top-level keys are ignored, so the schema can grow without breaking
older findings files.
"""

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
except ImportError:
    sys.exit("python-docx is required:  pip install python-docx")

# Continuous brand tokens -- from the continuous-brand skill's palette.
BLACK_PEARL = RGBColor(0x01, 0x11, 0x1F)
SAPPHIRE = RGBColor(0x0F, 0x4B, 0xBD)
PEARL_60 = RGBColor(0x67, 0x70, 0x79)
ERROR_RED = RGBColor(0xC6, 0x28, 0x28)
WARNING_YELLOW = RGBColor(0xF9, 0xA8, 0x25)
SUCCESS_GREEN = RGBColor(0x2E, 0x7D, 0x32)
DISABLED_GRAY = RGBColor(0x9E, 0x9E, 0x9E)

ICEBERG_HEX = "E3F1FD"
SAPPHIRE_HEX = "0F4BBD"

HEAD_FONT = "Kaleko"        # brand headline face
BODY_FONT = "BDO Grotesk"   # brand body face

SEVERITY_COLOR = {"High": ERROR_RED, "Medium": WARNING_YELLOW, "Low": DISABLED_GRAY}
AXIS_ORDER = ["Exposure", "Accuracy", "Coverage", "Install", "Structure",
              "Terminology", "FrontMatter", "Links", "Version"]

REQUIRED = ["repo", "unit", "units_version", "docs_ref", "phase", "date",
            "rubric_version", "code_source", "summary", "repo_score", "repo_letter",
            "achievable_ceiling", "blocking", "pages", "findings"]


# --------------------------------------------------------------------------
# low-level docx helpers
# --------------------------------------------------------------------------

def shade(cell, hex_fill):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hex_fill)
    cell._tc.get_or_add_tcPr().append(el)


def run(paragraph, text, *, size=10.5, bold=False, color=BLACK_PEARL,
        font=BODY_FONT, italic=False):
    r = paragraph.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name = font
    return r


def para(doc, text="", **kw):
    p = doc.add_paragraph()
    space_after = kw.pop("space_after", 6)
    align = kw.pop("align", None)
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    if text:
        run(p, text, **kw)
    return p


def heading(doc, text, level=1):
    sizes = {1: 19, 2: 14, 3: 11.5}
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16 if level == 1 else 12)
    p.paragraph_format.space_after = Pt(5)
    run(p, text, size=sizes.get(level, 11.5), bold=True,
        color=SAPPHIRE if level <= 2 else BLACK_PEARL, font=HEAD_FONT)
    return p


def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = ""
        run(cell.paragraphs[0], str(h), size=9.5, bold=True,
            color=RGBColor(0xFF, 0xFF, 0xFF), font=BODY_FONT)
        shade(cell, SAPPHIRE_HEX)
    for r_i, row in enumerate(rows):
        cells = t.add_row().cells
        for c_i, val in enumerate(row):
            cells[c_i].text = ""
            color = BLACK_PEARL
            bold = False
            if isinstance(val, str) and val in SEVERITY_COLOR:
                color, bold = SEVERITY_COLOR[val], True
            run(cells[c_i].paragraphs[0], "" if val is None else str(val),
                size=9.5, bold=bold, color=color, font=BODY_FONT)
            if r_i % 2 == 1:
                shade(cells[c_i], ICEBERG_HEX)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def label_value(doc, label, value, value_color=BLACK_PEARL):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    run(p, f"{label}  ", size=10, bold=True, color=PEARL_60)
    run(p, str(value), size=10, color=value_color)
    return p


# --------------------------------------------------------------------------
# report sections
# --------------------------------------------------------------------------

CODE_SOURCE_LABEL = {
    "verified": ("Verified", SUCCESS_GREEN),
    "candidate": ("Candidate — unconfirmed", WARNING_YELLOW),
    "none": ("None — docs-only assessment", ERROR_RED),
}


def cover(doc, d, logo):
    if logo and logo.exists():
        doc.add_picture(str(logo), width=Inches(2.4))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.LEFT
    phase_word = "Pre-assessment" if d["phase"] == "pre" else "Post-assessment"
    para(doc, "VisualCron documentation " + phase_word.lower(),
         size=11, color=PEARL_60, bold=True, space_after=2)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(14)
    run(p, d.get("unit_title") or d["unit"], size=26, bold=True, color=BLACK_PEARL,
        font=HEAD_FONT)
    label_value(doc, "Unit", "%s  (units.json v%s)" % (d["unit"], d["units_version"]))
    label_value(doc, "Docs", "%s @ %s" % (d["repo"], d["docs_ref"]))

    cs = d["code_source"]
    cs_text, cs_color = CODE_SOURCE_LABEL.get(
        cs.get("status", "none"), ("Unknown", DISABLED_GRAY))
    if cs.get("repo") and cs.get("status") != "none":
        cs_text += f" — {cs['repo']}"
        if cs.get("ref"):
            cs_text += f" @ {cs['ref']}"

    label_value(doc, "Date", d["date"])
    label_value(doc, "Phase", phase_word)
    label_value(doc, "Code source", cs_text, cs_color)
    if cs.get("note"):
        label_value(doc, "Source note", cs["note"], PEARL_60)
    label_value(doc, "Pages assessed", len(d["pages"]))
    label_value(doc, "Rubric version", d["rubric_version"])
    if d.get("assessed_by"):
        label_value(doc, "Assessed by", d["assessed_by"])


def scoreboard(doc, d):
    heading(doc, "Score", 1)
    blocking = bool(d["blocking"])
    highs = sum(1 for f in d["findings"] if f.get("severity") == "High")
    table(doc,
          ["Unit score", "Letter", "Achievable ceiling", "High findings", "Status"],
          [[d["repo_score"], d["repo_letter"], d["achievable_ceiling"], highs,
            "BLOCKED" if blocking else "Clear"]],
          widths=[1.5, 0.8, 1.5, 1.2, 1.2])

    gap = d["achievable_ceiling"] - d["repo_score"]
    if d["phase"] == "pre":
        note = (f"{gap} points are reachable by this process. "
                if gap > 0 else "The repo is already at its achievable ceiling. ")
        note += ("Findings above the ceiling need subject-matter input and cannot be "
                 "closed by documentation work alone.")
        para(doc, note, size=9.5, italic=True, color=PEARL_60)
    if blocking:
        para(doc,
             "At least one High finding is present. A High finding blocks the pull request "
             "regardless of the numeric score.",
             size=9.5, bold=True, color=ERROR_RED)
    if d["code_source"].get("status") == "none":
        para(doc,
             "No code source was confirmed. The Accuracy axis was not assessed — it is not "
             "scored clean. An unknown number of accuracy findings therefore sit outside the "
             "ceiling shown above.",
             size=9.5, italic=True, color=ERROR_RED)


def delta_section(doc, d):
    dl = d.get("delta")
    if not dl:
        return
    heading(doc, "Movement since pre-assessment", 1)
    move = d["repo_score"] - dl["pre_score"]
    table(doc,
          ["", "Score", "Letter", "Date"],
          [["Pre-assessment", dl["pre_score"], dl.get("pre_letter", ""),
            dl.get("pre_date", "")],
           ["Post-assessment", d["repo_score"], d["repo_letter"], d["date"]],
           ["Change", f"{move:+d}", "", ""]],
          widths=[1.6, 1.0, 0.9, 1.2])
    table(doc, ["Findings closed", "Carried forward", "Newly found"],
          [[dl.get("closed", 0), dl.get("carried", 0), dl.get("new", 0)]],
          widths=[1.5, 1.5, 1.5])
    if dl.get("note"):
        para(doc, dl["note"], size=9.5, italic=True, color=PEARL_60)


def prior_uplift_section(doc, d):
    pu = d.get("prior_uplift")
    if not pu:
        return
    heading(doc, "Earlier 2026 uplift", 1)
    if pu.get("note"):
        para(doc, pu["note"], size=10.5)
    sc = pu.get("scale", {})
    table(doc, ["Window", "Uplift commits", "Files changed", "Pages", "Words, net"],
          [[pu.get("window", ""), sc.get("uplift_commits", ""), sc.get("files_changed", ""),
            "%s → %s" % (sc.get("pages_before", ""), sc.get("pages_after", "")),
            "{:+,}".format(sc["words_net"]) if isinstance(sc.get("words_net"), int) else ""]],
          widths=[1.7, 1.0, 1.0, 1.0, 1.0])
    para(doc, "Measured on the current version's docs/ tree from %s (before the earlier uplift) "
              "to %s (where this program started)." % (pu.get("original", "?"), pu.get("handover", "?")),
         size=9.5, italic=True, color=PEARL_60)
    if pu.get("commits"):
        table(doc, ["Date", "Earlier uplift change"],
              [[c.get("date", ""), c.get("title", "")] for c in pu["commits"]],
              widths=[1.0, 5.4])
    pa = pu.get("prior_assessment")
    if pa:
        heading(doc, "Earlier assessment", 2)
        table(doc, ["Date", "Method", "Score before", "Score after"],
              [[pa.get("date", ""), pa.get("method", ""), pa.get("score_before") or "—",
                pa.get("score_after") or "—"]],
              widths=[1.0, 2.6, 1.4, 1.4])
        if pa.get("outcome"):
            para(doc, pa["outcome"], size=10)
    if pu.get("attribution"):
        heading(doc, "Where this program's findings came from", 2)
        table(doc, ["Origin", "Findings", "Examples"],
              [[a.get("bucket", ""), a.get("count", ""), a.get("examples", "")]
               for a in pu["attribution"]],
              widths=[2.0, 0.7, 3.7])


def summary_section(doc, d):
    heading(doc, "Summary", 1)
    para(doc, d["summary"], size=10.5)


def pages_section(doc, d):
    heading(doc, "Pages", 1)
    rows = [[p.get("path", ""), p.get("lines", ""), p.get("score", ""),
             p.get("letter", ""), p.get("ceiling", "")] for p in d["pages"]]
    table(doc, ["Page", "Lines", "Score", "Letter", "Ceiling"], rows,
          widths=[3.0, 0.7, 0.7, 0.7, 0.8])


def axes_section(doc, d):
    axes = d.get("axes")
    if not axes:
        return
    heading(doc, "Findings by axis", 1)
    order = {a: i for i, a in enumerate(AXIS_ORDER)}
    rows = []
    for a in sorted(axes, key=lambda x: order.get(x.get("axis", ""), 99)):
        rows.append([a.get("axis", ""), a.get("status", "assessed"),
                     a.get("high", 0), a.get("medium", 0), a.get("low", 0),
                     a.get("note", "")])
    table(doc, ["Axis", "Status", "High", "Med", "Low", "Note"], rows,
          widths=[1.1, 1.0, 0.5, 0.5, 0.5, 2.3])


RESOLVABLE_LABEL = {"in-process": "Fixable in this process",
                    "needs-sme": "Needs subject-matter input"}


def findings_section(doc, d):
    heading(doc, "Findings", 1)
    if not d["findings"]:
        para(doc, "No findings.", size=10.5, italic=True, color=PEARL_60)
        return

    rank = {"High": 0, "Medium": 1, "Low": 2}
    order = {a: i for i, a in enumerate(AXIS_ORDER)}
    ordered = sorted(d["findings"],
                     key=lambda f: (rank.get(f.get("severity"), 3),
                                    order.get(f.get("axis"), 99),
                                    f.get("id", "")))
    for f in ordered:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(1)
        run(p, f"{f.get('id', '?')}  ", size=11, bold=True, color=SAPPHIRE,
            font=HEAD_FONT)
        run(p, f.get("severity", ""), size=10, bold=True,
            color=SEVERITY_COLOR.get(f.get("severity"), DISABLED_GRAY))
        run(p, f"   {f.get('axis', '')}", size=10, color=PEARL_60)
        if f.get("tier"):
            run(p, f"   Tier {f['tier']}", size=9.5, color=PEARL_60)
        if f.get("status"):
            run(p, f"   [{f['status']}]", size=9.5, italic=True, color=PEARL_60)

        loc = f.get("page", "")
        if f.get("location"):
            loc = f"{loc} — {f['location']}" if loc else f["location"]
        if loc:
            para(doc, loc, size=9.5, color=PEARL_60, space_after=3)

        for label, key in (("Issue", "issue"), ("Evidence", "evidence"),
                           ("Recommendation", "recommendation")):
            if f.get(key):
                b = doc.add_paragraph()
                b.paragraph_format.space_after = Pt(2)
                b.paragraph_format.left_indent = Inches(0.16)
                run(b, f"{label}: ", size=10, bold=True, color=BLACK_PEARL)
                run(b, f[key], size=10)

        if f.get("resolvable"):
            b = doc.add_paragraph()
            b.paragraph_format.space_after = Pt(2)
            b.paragraph_format.left_indent = Inches(0.16)
            run(b, RESOLVABLE_LABEL.get(f["resolvable"], f["resolvable"]),
                size=9.5, italic=True,
                color=PEARL_60 if f["resolvable"] == "in-process" else WARNING_YELLOW)


def unverifiable_section(doc, d):
    items = d.get("unverifiable") or []
    heading(doc, "Unverifiable", 1)
    if not items:
        para(doc, "Nothing was left unverified.", size=10.5, italic=True,
             color=PEARL_60)
        return
    para(doc,
         "Flagged during assessment but not confirmed. These are excluded from the score "
         "rather than guessed at.",
         size=9.5, italic=True, color=PEARL_60)
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        run(p, item, size=10)


# --------------------------------------------------------------------------

def validate(d):
    missing = [k for k in REQUIRED if k not in d]
    if missing:
        sys.exit(f"findings JSON is missing required keys: {', '.join(missing)}")
    if d["phase"] not in ("pre", "post"):
        sys.exit('"phase" must be "pre" or "post"')
    if d["repo"] != "visualcron-docs":
        sys.exit('"repo" must be "visualcron-docs"; this renderer is for the VisualCron program')
    if not isinstance(d["blocking"], bool):
        sys.exit('"blocking" must be true or false. Put narrative in "summary": prose in this '
                 'field is never rendered and a non-empty string reads as BLOCKED.')
    open_high = any(f.get("severity") == "High" and f.get("status", "open") != "closed"
                    for f in d["findings"])
    if d["blocking"] != open_high:
        sys.exit(f'"blocking" is {d["blocking"]} but open High findings present = {open_high}')
    if d["phase"] == "post":
        closed = [f.get("id", "?") for f in d["findings"] if f.get("status") == "closed"]
        if closed:
            print("warning: post report lists closed findings (%s). List what still stands; "
                  "narrate closures in summary and count them in delta." % ", ".join(closed),
                  file=sys.stderr)
    if d["repo_score"] > d["achievable_ceiling"]:
        sys.exit("score exceeds ceiling - usually a stale ceiling after an owner decision")
    if not d["pages"]:
        sys.exit('"pages" must list at least one page')
    if d["phase"] == "post" and "delta" not in d:
        print("warning: post report has no \"delta\" block — the movement section "
              "will be omitted", file=sys.stderr)
    bad = [f.get("id", "?") for f in d["findings"]
           if f.get("severity") not in SEVERITY_COLOR]
    if bad:
        sys.exit(f"findings with invalid severity: {', '.join(bad)}")


def assessments_dir():
    """The assessments folder: VC_DOCS_ASSESSMENTS if set, else
    %OneDrive%/VisualCron-docs-assessments (OneDriveCommercial, then OneDrive).
    Returns None when none of these is set."""
    explicit = os.environ.get("VC_DOCS_ASSESSMENTS")
    if explicit:
        return Path(explicit)
    root = os.environ.get("OneDriveCommercial") or os.environ.get("OneDrive")
    return Path(root) / "VisualCron-docs-assessments" if root else None


def default_out(d):
    out_dir = assessments_dir()
    if out_dir is None:
        sys.exit("neither VC_DOCS_ASSESSMENTS nor %OneDrive% is set; pass --out explicitly")
    if not out_dir.is_dir():
        sys.exit(f"expected folder does not exist: {out_dir}")
    stamp = d.get("date") or date.today().isoformat()
    return out_dir / f"{d['repo']}-{d['unit']}-{d['phase']}assessment-{stamp}.docx"


def build(d, out_path, logo):
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(10.5)
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Inches(0.8)
        section.left_margin = section.right_margin = Inches(0.9)

    cover(doc, d, logo)
    scoreboard(doc, d)
    if d["phase"] == "post":
        delta_section(doc, d)
    prior_uplift_section(doc, d)
    summary_section(doc, d)
    pages_section(doc, d)
    axes_section(doc, d)
    findings_section(doc, d)
    unverifiable_section(doc, d)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
    return out_path


def main():
    ap = argparse.ArgumentParser(
        description="Render a Continuous-branded VisualCron docs unit assessment.",
        epilog="Run with --schema to print the findings JSON schema.")
    ap.add_argument("findings", nargs="?", help="path to findings JSON")
    ap.add_argument("--out", help="output .docx path (default: "
                                  "%%VC_DOCS_ASSESSMENTS%%, default "
                                  "%%OneDrive%%/VisualCron-docs-assessments/)")
    ap.add_argument("--logo", help="override the bundled logo path")
    ap.add_argument("--schema", action="store_true",
                    help="print the findings JSON schema and exit")
    args = ap.parse_args()

    if args.schema:
        print(__doc__)
        return
    if not args.findings:
        ap.error("a findings JSON path is required (or use --schema)")

    with open(args.findings, encoding="utf-8") as fh:
        d = json.load(fh)
    validate(d)

    logo = (Path(args.logo) if args.logo
            else Path(__file__).resolve().parent.parent / "assets"
            / "continuous-horizontal-blue.png")
    out = Path(args.out) if args.out else default_out(d)
    print(build(d, out, logo))


if __name__ == "__main__":
    main()
