#!/usr/bin/env python3
"""Regression test for docs/paper/popsim.tex rendering.

Builds the paper in a scratch directory and checks that the rendered PDF
matches the committed snapshot in docs/paper/snapshots/:

  * links.json  -- every URI link annotation (page, URL, rounded rect).
    Guards the easter-egg citation feature: each reference title and each
    in-text citation must be a clickable, correctly-targeted link at the
    same place on the page.
  * text.txt    -- pdftotext output, so wording and pagination are preserved.

Usage:
  scripts/test_paper_links.py            # run test
  scripts/test_paper_links.py --update   # regenerate snapshots from a fresh build
"""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs" / "paper"
SNAP = PAPER / "snapshots"


def build(workdir: Path) -> Path:
    shutil.copy(PAPER / "popsim.tex", workdir / "popsim.tex")
    if (PAPER / "figures").exists():
        shutil.copytree(PAPER / "figures", workdir / "figures")
    for _ in range(3):  # resolve refs / page breaks
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "popsim.tex"],
                           cwd=workdir, capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("pdflatex failed:\n" + r.stdout[-3000:])
    return workdir / "popsim.pdf"


def links(pdf: Path):
    qdf = subprocess.run(["qpdf", "--qdf", "--object-streams=disable", str(pdf), "-"],
                         capture_output=True).stdout.decode("latin-1")
    # Map annotation object ids -> page numbers via each page's /Annots array.
    objs = dict(re.findall(r"\n(\d+) 0 obj\n(.*?)\nendobj", qdf, re.S))
    pages = [oid for oid, body in objs.items() if "/Type /Page\n" in body or "/Type /Page " in body]
    pages.sort(key=lambda o: qdf.index(f"\n{o} 0 obj\n"))
    page_of = {}
    for pno, oid in enumerate(pages, 1):
        m = re.search(r"/Annots\s*\[(.*?)\]", objs[oid], re.S)
        if m:
            for aid in re.findall(r"(\d+) 0 R", m.group(1)):
                page_of[aid] = pno
    out = []
    for oid, body in objs.items():
        if "/Subtype /Link" not in body:
            continue
        uri = re.search(r"/URI \(([^)]*)\)", body)
        rect = re.search(r"/Rect \[\s*([^\]]+?)\s*\]", body)
        if not uri:
            continue
        rect_vals = [round(float(x)) for x in rect.group(1).split()] if rect else None
        out.append({"page": page_of.get(oid), "url": uri.group(1), "rect": rect_vals})
    out.sort(key=lambda d: (d["page"] or 0, -(d["rect"][1] if d["rect"] else 0), d["rect"][0] if d["rect"] else 0))
    return out


def text(pdf: Path) -> str:
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout


def main():
    update = "--update" in sys.argv
    with tempfile.TemporaryDirectory() as td:
        pdf = build(Path(td))
        got_links, got_text = links(pdf), text(pdf)
    assert got_links, "no link annotations found in built PDF"
    layout_ok = check_layout()
    if update:
        SNAP.mkdir(exist_ok=True)
        (SNAP / "links.json").write_text(json.dumps(got_links, indent=1) + "\n")
        (SNAP / "text.txt").write_text(got_text)
        print(f"snapshots updated: {len(got_links)} links, {len(got_text)} chars of text")
        return
    exp_links = json.loads((SNAP / "links.json").read_text())
    exp_text = (SNAP / "text.txt").read_text()
    ok = True
    if got_links != exp_links:
        ok = False
        print("LINK MISMATCH")
        es, gs = {json.dumps(x) for x in exp_links}, {json.dumps(x) for x in got_links}
        for x in sorted(es - gs): print("  missing:", x)
        for x in sorted(gs - es): print("  extra:  ", x)
    if got_text != exp_text:
        ok = False
        print("TEXT MISMATCH")
        import difflib
        sys.stdout.writelines(difflib.unified_diff(exp_text.splitlines(1), got_text.splitlines(1), "expected", "got", n=1))
    ok = ok and layout_ok
    print("PASS" if ok else "FAIL", f"({len(got_links)} links)")
    sys.exit(0 if ok else 1)


def check_layout() -> bool:
    """Figure-near-text rule from docs/paper/LAYOUT.md: every figure sits on the
    page of its first reference, or at worst the page before; never after."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import paper_layout as pl
    preamble, parts, figs = pl.parse((PAPER / "popsim.tex").read_text())
    with tempfile.TemporaryDirectory() as td:
        _cost, info = pl.evaluate(preamble, parts, figs, Path(td))
    ok = True
    for r in info["figures"]:
        d = r["fig_page"] - r["ref_page"]
        if d > 0 or d < -1:
            ok = False
            print(f"LAYOUT: {r['label']} on p{r['fig_page']} but first referenced on p{r['ref_page']}")
    return ok


if __name__ == "__main__":
    main()
