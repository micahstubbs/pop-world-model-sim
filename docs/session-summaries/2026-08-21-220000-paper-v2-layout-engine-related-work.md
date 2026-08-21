# Paper v2: figure-near-text layout engine, related-work expansion, CaseMirror v2

## Summary

Built a float-placement layout engine that keeps every figure on the page of
the body text that cites it, expanded Related Work with 25 new references from
a literature search, fixed the diurnal chart labels, and published popsim v2
on CaseMirror Research.

## Completed Work

- `30da7d6` — Diurnal figure (Fig 3): a.m./p.m. tick labels (12 a.m. … 11 p.m.),
  peak/trough annotations in a.m./p.m., trough label lifted above the bars
  with a leader (pop-world-model-sim-wfm).
- `933d42e` — `scripts/paper_layout.py`: hill-climbs figure source position ×
  placement spec, rebuilding with pdflatex and reading fig/ref pages from the
  `.aux`; cost = page distance (trailing 3/page, leading 2/page) + 0.25/page
  + 4 × rasterized internal column gaps. Preferences written up in
  `docs/paper/LAYOUT.md`; `scripts/test_paper_links.py` now also fails on
  off-page figures. `\clearpage` before references removed. Related Work
  rewritten (paragraphs on population-scale simulation, tiered compute,
  persona evaluation, contagion on Twitter, relationship structure, data)
  plus ~12 sentence-level rephrasings (702.7× now framed under the nominal
  cost model; benchmark novelty claim narrowed; diffusion result framed as a
  replication of weak-contagion findings). Search report:
  `docs/paper/related-work-search.md` (pop-world-model-sim-faj, -p7y, -mca).
- CaseMirror `95cd0adcf` — migration 258 (v2 row + versions history), assets
  `popsim-2026-v2.pdf` + refreshed thumbnail, deployed to the VM and verified
  at https://casemirror.ai/research/popsim-2026 (pop-world-model-sim-ii6).

## Key results

Final layout (8 pages): Fig 1 p2 (ref p3), Figs 2–3 p3, Figs 4–5 p4 with
Section 6, Figs 6–7 p5, Fig 8 p6 inline between the protocol and baseline
paragraphs, References start mid-p7.

Literature search verdict: nobody has done the full combination (real
Sentiment140 personas + real mention graph + held-out adherence benchmark),
but Itkin's *Poor Man's Agentic Modeling* (arXiv:2608.11215) shares the
single-machine framing and APS (arXiv:2605.27419) reports a measured 381×
tiered-compute reduction — both now cited and differentiated.

## Lessons

- The optimizer's paragraph indexing originally counted whitespace-only
  fragments as paragraphs, so offsets did not round-trip after a rewrite;
  fixed with `is_real()`.
- A figure block the optimizer has moved *above* a section heading will be
  deleted by a naive "replace everything between `\section{A}` and
  `\section{B}`" edit — it happened to `fig:dist`; recovered from git.
- `[H]` floats can "win" on page proximity while leaving a half-empty column;
  the `.aux` cannot see whitespace, so the engine rasterizes pages at 20 dpi
  and penalizes internal blank runs.
- CaseMirror `yarn migrate` is in a bad state (83 "pending", fails at 183);
  apply research migrations with psql and insert the `migration_history` row
  by hand. `/research/papers/*.pdf` returns 200 with the SPA HTML before the
  asset is deployed — check `content_type`, not the status code.

## Pending

- The two screenshots (`fig:ui-data`, `fig:ui-adherence`) and Fig 1 land on
  the page *before* their reference, the allowed fallback; the strict
  same-page target is met for the other five.
- `docs/data/x-followers-micahstubbs-2026-08-21.json` is untracked from a
  prior session (left alone).
