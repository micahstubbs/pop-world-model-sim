# Replace bot/incoherent surrogate samples on popsim site

## Summary
Replaced three of the four "What the cheapest surrogate sounds like" examples (§05) on popsim.micahstubbs.ai: `SallytheShizzle` had a gibberish surrogate; `webwoke` and `tweetpet` were template-spam bots with useless real tweets.

## Completed Work
- d608f00 — `scripts/build_demo_artifacts.py`: `BOT_USERS` exclusion (webwoke, tweetpet, what_bugs_u, wowlew); `CURATED` per-user (real tweet, Markov seeds) picks; explicit display order lost_dog → tsarnick → TraceyHewins → SallytheShizzle. Regenerated `site/data/adherence.json` samples from the generator (not hand-edited). Issue pop-world-model-sim-nig.
- Deployed via `ds`: wrangler → CF Pages (578c001f.popsim-92w.pages.dev), mirrored to micahstubbs/popsim gh-pages. Verified live with headless full-page screenshot.

## Key Changes
- Surrogates still come from the same per-user word-bigram chain; only the RNG seed is curated (seeds 16/2, 7/12, 10/1) and candidates were checked not to be verbatim tweets.

## Pending
- `lost_dog` (first sample) is also a bot ("I am lost. Please help me find a good home.") — left as-is, not requested.

## Next Session Context
- Surrogate samples no longer need a full rebuild to tweak: edit `CURATED` / `order` in build_demo_artifacts.py.
