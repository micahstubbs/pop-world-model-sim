---
name: ds
description: Deploy the popsim site - wrangler pages deploy site/ to the Cloudflare Pages project "popsim" (popsim.micahstubbs.ai), then mirror site/* to the micahstubbs/popsim gh-pages repo (code mirror only)
---

# DS (Deploy Site)

Ship `site/` to https://popsim.micahstubbs.ai.

## Facts (hosting cut over 2026-08-20)

- Source of truth: `site/` in THIS repo (micahstubbs/pop-world-model-sim).
- **Live hosting: Cloudflare Pages**, project `popsim`
  (popsim-92w.pages.dev), account `fa0c1c0e6b3f6cde0271c5301b128350`;
  Spaceship CNAME for popsim.micahstubbs.ai points at CF Pages.
- History: originally GitHub Pages on the separate `micahstubbs/popsim`
  repo (gh-pages), but GitHub's Let's Encrypt cert request wedged at "new"
  through two domain re-add cycles on launch night, so hosting moved to CF.
  The custom domain was REMOVED from GitHub Pages; **gh-pages is now just a
  code mirror** — keep it updated, but it serves nothing.

## Process

```bash
# 1. Commit + push the source change in this repo first.
# 2. Deploy to Cloudflare Pages:
export CLOUDFLARE_API_TOKEN=$(grep -oE '[A-Za-z0-9_-]{40}' ~/keys/cloudflare/CLOUDFLARE_API_TOKEN_EDIT_CLOUDFLARE_WORKERS.md | head -1)
export CLOUDFLARE_ACCOUNT_ID=fa0c1c0e6b3f6cde0271c5301b128350
npx wrangler pages deploy site --project-name popsim --branch main
# 3. Mirror to the gh-pages code mirror (COPY, never mirror-delete —
#    CNAME/.nojekyll/README live only in that clone):
git clone https://github.com/micahstubbs/popsim <scratch>/popsim-deploy
cp -r site/* <scratch>/popsim-deploy/ && cd <scratch>/popsim-deploy && git add -A && git commit -m "mirror site" && git push
# 4. Verify live:
curl -s -o /dev/null -w "%{http_code}" https://popsim.micahstubbs.ai/       # 200
curl -sI https://popsim.micahstubbs.ai/ | grep -i "server: cloudflare"      # CF serving
```

## Verification hooks

- `?flat` collapses the 92vh hero for headless screenshots (`/hss`).
- `?autorun` auto-runs the §03 diffusion animation.
- Serve locally first: `npx http-server -p <spare> site/`.

## Guardrails

- `site/data/*.json` are generated artifacts (`scripts/build_demo_artifacts.py`)
  — never hand-edit.
- Don't re-add the custom domain to GitHub Pages — it was deliberately
  removed after the wedged-cert launch night.
- Coordinate with any live session on this repo before editing
  `site/index.html` (see user-level `psc` skill).
