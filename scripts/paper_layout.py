#!/usr/bin/env python3
"""Figure-near-text layout engine for docs/paper/popsim.tex.

arXiv-style two-column LaTeX (article class, [t]/[b] floats, no float
pages) with one aesthetic preference layered on top, stated in
docs/paper/LAYOUT.md: **every figure lands on the same page as (part of)
the body text that references it.**  LaTeX's float algorithm optimizes
for filling pages, not for proximity, so this script searches over the
two knobs an author would otherwise turn by hand:

  1. where in the source each figure environment sits, measured in
     paragraphs relative to the paragraph holding the first \\ref to it;
  2. the placement specifier ([t], [b], [htb], [H], with/without !).

For each candidate it rebuilds the paper (pdflatex, ~0.4 s) and reads the
.aux file to learn the page of each figure and the page of its first
reference (the script plants a \\label right after that \\ref).  It then
hill-climbs (coordinate descent, one figure at a time) on a cost that
penalizes distance between those pages, with a small tiebreak on total
page count so it never trades a page of whitespace for nothing.

Usage
  scripts/paper_layout.py            # optimize, rewrite popsim.tex in place
  scripts/paper_layout.py --check    # build once and report (exit 1 if any
                                     #   figure is off-page from its reference)
  scripts/paper_layout.py --dry-run  # optimize but only print the plan

The rewrite is conservative: only figure blocks move and only their
placement option changes; every other byte of the .tex is preserved.
"""
import argparse, itertools, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs" / "paper"
TEX = PAPER / "popsim.tex"
REPORT = PAPER / "layout-report.md"

# ---- search space --------------------------------------------------------
OFFSETS = [-3, -2, -1, 0, 1, 2]           # paragraphs before(-)/after(+) the anchor
# figure* (double-column) floats can only appear on a page AFTER the one where
# LaTeX meets them, so their source must sit well before the reference.
DBL_OFFSETS = [-8, -7, -6, -5, -4, -3, -2, -1, 0]
PLACEMENTS = ["t", "b", "htb", "!t", "!b", "!htb", "H"]
DBL_PLACEMENTS = ["t", "!t", "b", "!b"]   # figure* cannot take h/H

# ---- cost ----------------------------------------------------------------
COST_SAME_PAGE = 0.0
COST_BEFORE = 2.0      # per page the figure precedes its reference
COST_AFTER = 3.0       # per page the figure trails its reference (worse: reader has to flip forward)
COST_PER_PAGE = 0.25   # tiebreak: shorter document wins
COST_GAP = 4.0         # per page-height of internal blank space inside a column
GAP_MIN = 0.05         # blank runs shorter than this fraction of the page are ignored

FIG_RE = re.compile(r"\\begin\{(figure\*?)\}(\[[^\]]*\])?(.*?)\\end\{\1\}", re.S)
LABEL_RE = re.compile(r"\\label\{(fig:[^}]+)\}")
NEWLABEL_RE = re.compile(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}")


class Figure:
    def __init__(self, env, opt, body):
        self.env, self.body = env, body
        self.label = LABEL_RE.search(body).group(1)
        self.placement = (opt or "[t]").strip("[]")
        self.offset = 0  # filled in by parse()
        self.anchor = None

    @property
    def double(self):
        return self.env == "figure*"

    def render(self):
        head = f"\\begin{{{self.env}}}[{self.placement}]"
        return head + self.body + f"\\end{{{self.env}}}"


def split_paragraphs(text):
    """Split body text on blank lines, keeping separators so we can rejoin losslessly."""
    return re.split(r"(\n[ \t]*\n)", text)


def parse(tex):
    m = re.search(r"\\begin\{document\}", tex)
    preamble, rest = tex[: m.end()], tex[m.end():]
    figs = []
    def grab(mo):
        f = Figure(mo.group(1), mo.group(2), mo.group(3))
        figs.append(f)
        return f"\n\n@@FIG:{f.label}@@\n\n"  # sentinel paragraph marking the original slot
    stripped = FIG_RE.sub(grab, rest)
    parts = split_paragraphs(stripped)
    is_marker = lambda p: p.strip().startswith("@@FIG:")
    # anchor = index (in `parts`) of the paragraph with the first \ref to the label
    for f in figs:
        ref = re.compile(r"\\ref\{" + re.escape(f.label) + r"\}")
        f.anchor = next((i for i, p in enumerate(parts) if ref.search(p)), None)
        if f.anchor is None:
            sys.exit(f"no \\ref to {f.label}")
        slot = next(i for i, p in enumerate(parts) if p.strip() == f"@@FIG:{f.label}@@")
        # offset in *real* paragraphs (markers excluded) between original slot and anchor
        f.offset = _para_index(parts, slot) - _para_index(parts, f.anchor)
    # drop the sentinel paragraphs (and the separator that followed each)
    cleaned, skip = [], False
    for p in parts:
        if skip:
            skip = False
            continue
        if is_marker(p):
            skip = True  # also drop the separator after the marker
            continue
        cleaned.append(p)
    # anchors must be recomputed on the cleaned list
    for f in figs:
        ref = re.compile(r"\\ref\{" + re.escape(f.label) + r"\}")
        f.anchor = next(i for i, p in enumerate(cleaned) if ref.search(p))
    return preamble, cleaned, figs


def is_real(p):
    """A paragraph with content: not a separator, not whitespace, not a figure marker."""
    return bool(p.strip()) and not p.strip().startswith("@@FIG:")


def _para_index(parts, i):
    """Count of real paragraphs before index i."""
    return sum(1 for p in parts[:i] if is_real(p))


def assemble(preamble, parts, figs, instrument=False):
    """Re-insert figures before paragraph (anchor + offset); optionally plant ref-page labels."""
    real = [i for i, p in enumerate(parts) if is_real(p)]
    inserts = {}
    for f in figs:
        k = _para_index(parts, f.anchor) + f.offset
        k = max(0, min(k, len(real) - 1))
        inserts.setdefault(real[k], []).append(f)
    out = [preamble]
    for i, p in enumerate(parts):
        for f in inserts.get(i, []):
            out.append("\n" + f.render() + "\n\n")
        if instrument:
            for f in figs:
                if i == f.anchor:
                    p = re.sub(r"(\\ref\{" + re.escape(f.label) + r"\})",
                               r"\1\\label{refpage:" + f.label + "}", p, count=1)
        out.append(p)
    return "".join(out)


INSTRUMENT_PREAMBLE = "\\usepackage{float}\n"  # for [H]


def build(tex_src, workdir, passes=2):
    (workdir / "popsim.tex").write_text(tex_src)
    if not (workdir / "figures").exists():
        shutil.copytree(PAPER / "figures", workdir / "figures")
    for _ in range(passes):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "popsim.tex"],
                           cwd=workdir, capture_output=True, text=True)
        if r.returncode != 0:
            return None
    aux = (workdir / "popsim.aux").read_text()
    pages = {name: int(page) for name, _num, page in NEWLABEL_RE.findall(aux)}
    npages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(
        ["pdfinfo", str(workdir / "popsim.pdf")], capture_output=True, text=True).stdout).group(1))
    return pages, npages, gap_fraction(workdir / "popsim.pdf", npages)


def gap_fraction(pdf, npages):
    """Total internal blank space (in page heights) across both columns of every
    page but the last.  Catches the stretched-glue holes that [H] floats and
    forced column breaks leave behind, which the .aux cannot see."""
    import numpy as np
    from PIL import Image
    subprocess.run(["pdftoppm", "-r", "20", "-gray", "-png", str(pdf), str(pdf.with_suffix(""))],
                   capture_output=True)
    total = 0.0
    for pno in range(1, npages):  # skip last page: a short final column is fine
        f = next(pdf.parent.glob(f"popsim-{pno}.png"), None) or next(pdf.parent.glob(f"popsim-0{pno}.png"))
        a = np.asarray(Image.open(f).convert("L")) < 200
        h, w = a.shape
        for col in (a[:, : w // 2], a[:, w // 2 :]):
            rows = np.flatnonzero(col.any(axis=1))
            if len(rows) < 2:
                continue
            blank = np.flatnonzero(~col[rows[0] : rows[-1]].any(axis=1))
            if not len(blank):
                continue
            runs = np.split(blank, np.flatnonzero(np.diff(blank) > 1) + 1)
            for r in runs:
                if len(r) / h >= GAP_MIN:
                    total += len(r) / h
    return total


def evaluate(preamble, parts, figs, workdir):
    src = assemble(preamble, parts, figs, instrument=True)
    if "\\usepackage{float}" not in src:
        src = src.replace("\\begin{document}", INSTRUMENT_PREAMBLE + "\\begin{document}", 1)
    res = build(src, workdir)
    if res is None:
        return float("inf"), None
    pages, npages, gaps = res
    rows, cost = [], COST_PER_PAGE * npages + COST_GAP * gaps
    for f in figs:
        fp, rp = pages.get(f.label), pages.get("refpage:" + f.label)
        if fp is None or rp is None:
            return float("inf"), None
        d = fp - rp
        cost += (COST_AFTER * d if d > 0 else COST_BEFORE * -d)
        rows.append({"label": f.label, "env": f.env, "placement": f.placement,
                     "offset": f.offset, "fig_page": fp, "ref_page": rp})
    return cost, {"pages": npages, "gaps": round(gaps, 3), "figures": rows}


def describe(info):
    lines = [f"pages: {info['pages']}   internal column gaps: {info['gaps']} page-heights"]
    for r in info["figures"]:
        flag = "" if r["fig_page"] == r["ref_page"] else "   <-- off-page"
        lines.append(f"  {r['label']:<18} {r['env']:<8} [{r['placement']}] off={r['offset']:+d}"
                     f"  fig p{r['fig_page']}  ref p{r['ref_page']}{flag}")
    return "\n".join(lines)


def optimize(preamble, parts, figs, workdir, log=print):
    best_cost, best_info = evaluate(preamble, parts, figs, workdir)
    log(f"start cost={best_cost:.2f}\n{describe(best_info)}")
    improved, sweep = True, 0
    while improved and sweep < 3:
        improved, sweep = False, sweep + 1
        for f in figs:
            cur = (f.offset, f.placement)
            opts = DBL_PLACEMENTS if f.double else PLACEMENTS
            offs = DBL_OFFSETS if f.double else OFFSETS
            for off, pl in itertools.product(offs, opts):
                if (off, pl) == cur:
                    continue
                f.offset, f.placement = off, pl
                c, info = evaluate(preamble, parts, figs, workdir)
                if c < best_cost - 1e-9:
                    best_cost, best_info, cur, improved = c, info, (off, pl), True
                    log(f"  {f.label}: off={off:+d} [{pl}] -> cost {c:.2f}")
            f.offset, f.placement = cur
    log(f"final cost={best_cost:.2f}\n{describe(best_info)}")
    return best_info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    tex = TEX.read_text()
    preamble, parts, figs = parse(tex)
    with tempfile.TemporaryDirectory() as td:
        wd = Path(td)
        if a.check:
            cost, info = evaluate(preamble, parts, figs, wd)
            print(describe(info))
            off = [r for r in info["figures"] if r["fig_page"] != r["ref_page"]]
            sys.exit(1 if off else 0)
        info = optimize(preamble, parts, figs, wd)
    if a.dry_run:
        return
    out = assemble(preamble, parts, figs)
    if "\\usepackage{float}" not in out and any(f.placement == "H" for f in figs):
        out = out.replace("\\usepackage{graphicx}", "\\usepackage{graphicx}\n\\usepackage{float}", 1)
    TEX.write_text(out)
    REPORT.write_text("# Layout report\n\nGenerated by `scripts/paper_layout.py`.\n\n```\n"
                      + describe(info) + "\n```\n")
    print("wrote", TEX, "and", REPORT)


if __name__ == "__main__":
    main()
