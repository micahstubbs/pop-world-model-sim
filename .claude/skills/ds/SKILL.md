---
name: ds
description: Deploy the popsim site - copy site/* from this repo into a clone of the separate micahstubbs/popsim gh-pages repo (never mirror; CNAME/.nojekyll/README live only there), push, and verify https://popsim.micahstubbs.ai
---

# DS (Deploy Site)

Ship `site/` to https://popsim.micahstubbs.ai (GitHub Pages, custom domain).

## Facts

- Source of truth: `site/` in THIS repo (micahstubbs/pop-world-model-sim).
- Hosting: the SEPARATE public repo `micahstubbs/popsim`, branch `gh-pages`
  (default/only branch), GitHub Pages with custom domain
  `popsim.micahstubbs.ai` (Spaceship CNAME → micahstubbs.github.io, same
  pattern as qutip.micahstubbs.ai).
- The Pages clone contains files that do NOT exist in `site/`: `CNAME`,
  `.nojekyll`, `README.md`. **Copy, never mirror/delete** — clobbering CNAME
  breaks the custom domain and re-triggers TLS provisioning.

## Process

```bash
# 1. Commit + push the source change in this repo first.
# 2. Fresh clone of the Pages repo (scratch dir):
git clone https://github.com/micahstubbs/popsim <scratch>/popsim-deploy
# 3. COPY the site in (no --delete, no rsync mirror):
cp -r site/* <scratch>/popsim-deploy/
# 4. Commit + push; GitHub itself sometimes commits CNAME changes (cert
#    re-provisioning), so on rejection:
git pull --rebase && git push
# 5. Verify live (allow ~1 min propagation):
curl -s -o /dev/null -w "%{http_code}" https://popsim.micahstubbs.ai/   # 200
```

## Verification hooks

- `?flat` collapses the 92vh hero for headless screenshots (`/hss`).
- `?autorun` auto-runs the §03 diffusion animation.
- Serve locally first: `npx http-server -p <spare> site/`.

## Guardrails

- `site/data/*.json` are generated artifacts (`scripts/build_demo_artifacts.py`)
  — never hand-edit.
- Don't touch the GitHub Pages settings or CNAME during TLS provisioning;
  poll `gh api repos/micahstubbs/popsim/pages` for cert state instead.
- Coordinate with any live session on this repo before editing
  `site/index.html` (see user-level `psc` skill).
