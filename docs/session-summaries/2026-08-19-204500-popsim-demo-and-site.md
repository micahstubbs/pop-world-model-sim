# Session Summary: Five-Direction Demo + popsim Explainer Site

## Summary

Implemented all five suggested directions (persona mining, mixture-of-models scale ladder, diffusion validation, bilateral dyads, behavioral adherence) as a computed-artifact pipeline over Sentiment140, then built and deployed an interactive D3 explainer site to https://popsim.micahstubbs.ai for the Postlabor.dev build-night demo.

## Completed Work

- `scripts/build_demo_artifacts.py` — computes all five directions locally → `site/data/*.json` (commit `0f650ef`)
- `site/index.html` — single-page interactive explainer (Fraunces/Archivo/Fragment Mono, validated dark palette, canvas dot-field hero on the real diurnal clock, persona scatter + cards, √-scaled ladder, animated DeGroot diffusion on the real mention graph, dyad browser, adherence gauge)
- Deployed: public repo `micahstubbs/popsim`, `gh-pages` branch, GitHub Pages custom domain `popsim.micahstubbs.ai`, Spaceship CNAME → `micahstubbs.github.io` (same pattern as qutip.micahstubbs.ai)
- Visual verification: headless Chrome screenshots of every section, local + live domain
- Rebased over teammate commit `540d107` (character personas added by team)

## Key Numbers (all computed from the real corpus)

- Ladder: 702.7× cheaper than all-LLM population (927 LLM-tier / 5,318 surrogate / 653,530 statistical)
- Diffusion validation: DeGroot r=0.54 vs persistence baseline r=0.73 → finding: disposition beats diffusion
- Dyads: 3,324 reciprocal mention pairs; 31,515 cohort-internal mention edges
- Adherence: 63.1% on 42,998 held-out tweets (chance 50%), persona-only predictor

## Pending/Blocked

- HTTPS cert provisioning was in flight at write time (background watcher enforcing `https_enforced` once issued)
- Episodic-memory DB repair agent running in background (corrupted SQLite archived before recovery)

## Next Session Context

- Site source of truth: `site/` in this repo; deploy = copy to `micahstubbs/popsim` gh-pages
- `?flat` query param collapses the hero for headless screenshot verification
- Beads epic `pop-world-model-sim-t7h` tracks the demo work
