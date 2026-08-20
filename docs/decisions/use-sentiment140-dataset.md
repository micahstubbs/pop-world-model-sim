# Decision: Use the Sentiment140 Dataset

**Status:** Accepted
**Date:** 2026-08-19
**Decided by:** Yvonne Chen (relayed by Micah Stubbs to the team)
**Participants:** Micah Stubbs, Yvonne Chen, Jake Schwartz
**Source:** Email thread "Report: Publicly Available Twitter/X Tweet Datasets for Download and Study" (Aug 19, 2026, ~7:35–7:47 PM PT)

## Decision

The team will use the **Sentiment140** dataset as the tweet corpus for the pop-world-model-sim project (Postlabor.dev "Building Economic World Models" Simulation Build Night).

Canonical source: https://huggingface.co/datasets/stanfordnlp/sentiment140

## Context

- A research report surveying publicly available Twitter/tweet datasets was circulated to the team (see `docs/reports/2026-08-19-193128-public-twitter-datasets.md`). Its Tier 1 recommendation for a quick, structured on-ramp was Sentiment140.
- Micah forwarded the report to Yvonne and Jake; GitHub IDs were exchanged and collaborators added to this repo.
- Yvonne made the call to go with Sentiment140; Micah recorded it on the thread at 7:47 PM PT: "A decision from yvonne: We will use this sentiment140 dataset."

## Why Sentiment140

From the report's evaluation:

- **Full text included** — no tweet-ID hydration required (hydration has been effectively dead since the 2023 X API shutdown).
- **Trivial to load** — one flat CSV, 1.6M tweets, 6 columns (polarity, id, date, query, user, text); one line of pandas or `datasets.load_dataset("stanfordnlp/sentiment140")`.
- **Labeled** — positive/negative sentiment labels usable directly for agent affect or as evaluation signal.
- **Deep academic pedigree** — created by Stanford researchers (Go, Bhayani, Huang, 2009); thousands of citations; a standard sentiment benchmark, so results are comparable to prior work.
- **Right size for a build night** — big enough to derive realistic content/posting distributions, small enough to work with on a laptop.

## Known Caveats (accepted)

- Tweets are from 2009: 140-character era, no threads, quote tweets, or modern platform dynamics.
- Sentiment labels are distant-supervised via emoticons and therefore noisy.
- No network structure — if the simulation later needs follower-graph topology or ground-truth cascades, the report recommends pairing with SNAP Higgs Twitter.

## Consequences / Next Steps

- Build data loading and agent-seeding pipelines against the Hugging Face `stanfordnlp/sentiment140` distribution.
- Treat the report's other Tier 1 datasets (TweetEval, Community Archive, Archive Team Stream Grab, SNAP Higgs Twitter) as optional later additions, not current scope.
