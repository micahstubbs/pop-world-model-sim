# Site favicon + clickable mindmeld.now and dyad handle links

## Summary

Added a favicon set derived from the site's design system, made the
plain-text mindmeld.now mentions clickable, and linked the real 2009 Twitter
handles in the dyads section to their x.com profiles; deployed to
popsim.micahstubbs.ai. Work executed by the dramatic-academic-paper-reader
session on user routing, coordinated with the resident popsim session.

## Completed Work (commit 0307413 here; 19adb45 on micahstubbs/popsim gh-pages)

- `scripts/generate-icons.mjs`: parametric SVG — 3×3 population dot grid on
  the ink background, amber personas with one teal (positive) and one orange
  (negative) sentiment accent. Outputs favicon.svg, favicon.ico (48/32/16),
  icons/apple-touch-icon.png (full-bleed, 12% inset for iOS masking).
  Requires inkscape + ImageMagick convert.
- `site/index.html`: icon `<link rel>` tags; mindmeld.now → https://mindmeld.now
  in the §04 lede and the conversation-panel note; dyad handles in the kicker
  and chat-bubble "who" lines → `https://x.com/<handle>` (target=_blank,
  rel=noopener, encodeURIComponent + esc). Handle links inherit surrounding
  color with a dotted underline (peer's guidance: keep the mono,
  sentiment-neutral look). Selector buttons keep plain text — an `<a>` inside
  `<button>` is invalid HTML; the same handles are linked in the panel each
  button opens.
- Verified locally (http-server + headless full-page screenshot with ?flat):
  links render correctly, sentiment styling intact, icon files 200.
- Deployed per the copy-don't-mirror recipe (CNAME/.nojekyll preserved); now
  codified as project skill `.claude/skills/ds` (deploy-site).
- Beads: pop-world-model-sim-hqu (favicon), -1uk (links).

## Pending

- TLS cert for popsim.micahstubbs.ai was wedged at "new"; resident session
  re-cycled the domain and watches for https_enforced. The paper-reader
  session holds the "site is live" team email until HTTPS 200 + HTTP→HTTPS
  301 verify.
