# Paper layout preferences (durable)

These are standing aesthetic rules for `docs/paper/popsim.tex` and for any
future paper in this repo. They are enforced by `scripts/paper_layout.py`
(`--check` fails CI-style when violated; no flag rewrites the `.tex` to satisfy
them) and are stated here so they survive any one session.

## The rule

**A figure lives on the same page as at least part of the body text that
discusses it.** Not "the page after", not "somewhere in the section". A
reader should never have to flip pages between a claim and the chart that
backs it.

Corollaries:

1. The body text that "discusses" a figure is the paragraph containing the
   first `\ref{fig:…}` to it. Every figure therefore must have an in-text
   reference in the section it belongs to (screenshots included: a reference
   only from the Conclusion anchors the figure to the wrong page).
2. When the ideal is unreachable (e.g. a double-column `figure*` after a very
   long section), the figure goes on the page **before** its reference, never
   after. The cost function encodes this: trailing costs 3/page, leading 2/page.
3. Page count is a tiebreak only (0.25/page). Never add a page to fix a figure,
   but never accept a longer paper for no proximity gain either.
4. No `\clearpage` / `\newpage` before `\begin{thebibliography}`. References
   start immediately after the last body paragraph (or acknowledgments), in
   the same column flow.
5. Otherwise the look stays stock arXiv: `article` class, two-column, 10pt,
   `[t]`/`[b]` floats preferred, `[H]` and `!` only when the engine needs them
   for rule 1, no float-only pages.

## How the engine works

`scripts/paper_layout.py` treats the `.tex` as paragraphs plus movable figure
blocks. For each figure it searches:

- **source position**: −3…+2 paragraphs relative to the referencing paragraph
  (−8…0 for `figure*`, which LaTeX can only place on a page *after* the one
  where it meets the float);
- **placement spec**: `t b htb !t !b !htb H` (double-column: `t !t b !b`).

Each candidate is built with `pdflatex` (two passes, ~0.4 s) into a temp dir.
A `\label{refpage:fig:x}` is planted right after the first `\ref{fig:x}`, so
the `.aux` reports both the figure's page and the reference's page. Coordinate
descent over figures, up to three sweeps, minimizes

```
cost = Σ_fig (3·max(0, fig_page − ref_page) + 2·max(0, ref_page − fig_page))
       + 0.25 · total_pages
       + 4 · internal_column_gaps        (in page-heights)
```

`internal_column_gaps` is measured by rasterizing every page but the last at
20 dpi and summing blank runs taller than 5 % of the page that sit *between*
content in a column. This is what stops `[H]` from "winning" by forcing a
column break and leaving a half-empty column behind it — the `.aux` cannot
see whitespace, the raster can.

Only figure blocks move and only their `[…]` option changes; every other byte
of the source is preserved. The result is summarized in
`docs/paper/layout-report.md`. `scripts/test_paper_links.py` also fails if
any figure is more than one page before, or any distance after, its reference.

## Workflow

```
.venv/bin/python scripts/paper_figures.py   # regenerate figure PDFs if data changed
python3 scripts/paper_layout.py             # optimize placement, rewrites popsim.tex
python3 scripts/paper_layout.py --check     # verify (exit 1 on any off-page figure)
cd docs/paper && pdflatex popsim && pdflatex popsim && pdflatex popsim
pdftoppm -r 80 -png popsim.pdf page        # look at every page, not just page 1
python3 scripts/test_paper_links.py --update   # refresh link/text snapshots
```

Re-run the optimizer after **any** edit that changes text length (new
paragraph, new reference, caption edit): float placement is global, and a
paragraph added in §3 can push a §6 figure onto the wrong page.

## Other figure conventions

- Time-of-day axes use `12 a.m. … 11 p.m.` labels, not 0–23. Annotations
  ("peak 11 p.m.", "trough 1 p.m.") float in clear space with a thin leader,
  never over bars.
- Single-column figures are 3.4 in wide; double-column 0.92`\textwidth`.
- Every reference title and in-text citation is a hidden hyperlink (see
  `CLAUDE.md`, "Easter-egg reference and citation hyperlinks").
