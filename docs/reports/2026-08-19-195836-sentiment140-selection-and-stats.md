# Dataset Selection and Descriptive Statistics: Sentiment140

**Generated:** 2026-08-19
**For:** Micah Stubbs, Yvonne Chen, Jake Schwartz — Postlabor.dev "Building Economic World Models" Simulation Build Night
**Selection criterion:** works single-node in-memory on one machine; maximizes the number of distinct users with at least 20 tweets each.

## Selection Result

**Sentiment140 wins on the stated criterion**, and it confirms Yvonne's earlier call (see `docs/decisions/use-sentiment140-dataset.md`).

Measured head-to-head on "distinct users with ≥20 tweets":

| Candidate | Users w/ ≥20 tweets | Notes |
|---|---|---|
| **Sentiment140** | **6,245** (measured) | 1.6M tweets, full text, 282 MB in RAM |
| Community Archive | ≤363 (363 accounts total, queried live) | Full-corpus access currently paused by the project |
| Archive Team Stream Grab | ~none | 1% sample — users rarely recur 20× |
| TweetEval / PHEME | n/a | No per-user timelines at this scale |

Sentiment140 beats the runner-up by ~17× on user diversity, loads in one line of pandas, and uses under 300 MB of a 62 GB machine — comfortably single-node, in-memory.

## Descriptive Statistics (computed locally, `scripts/sentiment140_stats.py`)

**Corpus:** 1,600,000 tweets · 659,775 distinct users · Apr 6 – Jun 25, 2009 (48 active days) · perfectly balanced labels (800K negative / 800K positive) · 282 MB in memory.

**Per-user distribution:** mean 2.43 tweets/user, median 1, max 549 (`lost_dog`). Thresholds: ≥2 tweets → 254,498 users; ≥5 → 67,088; ≥10 → 21,875; **≥20 → 6,245 users covering 226,202 tweets**; ≥50 → 927; ≥100 → 163.

**The ≥20-tweet cohort (our persona population):** 6,245 users · 226,202 tweets · mean 36.2 tweets/user (median 28) · per-user activity spans ~50 days on average — enough temporal depth for behavioral personas. Cohort sentiment skews positive (59% positive vs. 41% negative), unlike the balanced corpus overall — a selection effect worth remembering.

**Text:** mean 74 chars / 13.2 words per tweet (median 69 / 12), p95 = 136 chars.

**Interaction structure (bonus finding):** 46.2% of all tweets contain an @-mention (738,491 tweets). 432,926 mention edges point at users who are themselves authors in the dataset, and **31,867 edges run between cohort members (4,328 distinct senders)** — i.e., the cohort contains a genuine directed interaction graph, not just isolated timelines.

**Temporal:** ~33K tweets/day (max 111,676). Clear diurnal cycle: peak 23:00 PDT, trough 13:00 PDT — a realistic activity rhythm to calibrate agent posting schedules against.

## Suggested Directions

Aligned with the event's two papers — **Light Society** ("Modeling Earth-Scale Human-Like Societies with One Billion Agents," [arXiv:2506.12078](https://arxiv.org/abs/2506.12078): billion-agent simulation, agents grounded in World Values Survey demographics, mixture-of-models engine combining full LLMs with distilled surrogates, validated via trust games and opinion diffusion) and **MatrAIx** ("Simulating the World with 8.3 Billion Persona Agents," [arXiv:2608.04205](https://arxiv.org/abs/2608.04205): 8.3B persona records over 1,290 dimensions, ~600K human-grounded + 400K synthetic curated personas, 91.5% behavioral adherence) — and the two projects, **pop-world-model-sim** (this repo) and **mindmeld.now** (bilateral agent social network):

1. **Human-grounded persona mining (MatrAIx pattern → pop-world-model-sim).** Extract persona cards from each of the 6,245 cohort users (attribute dimensions: sentiment disposition, topics, verbosity, posting cadence, mention behavior). This mirrors MatrAIx's human-grounded persona base at hackathon scale — real timelines instead of survey records.
2. **Mixture-of-models scale ladder (Light Society pattern).** Power the 927 heavy users (≥50 tweets) with full LLM agents and the remaining ~5,300 with cheap distilled/statistical surrogates. That's Light Society's efficiency architecture, sized to a single node — and a concrete answer to "how do you simulate a population on one machine."
3. **Opinion/sentiment diffusion on the real mention graph (Light Society validation pattern).** Run diffusion experiments over the 31,867 cohort-to-cohort mention edges and validate simulated sentiment dynamics against the actual 48-day record (diurnal cycle, per-user sentiment trajectories).
4. **Bilateral agent conversations (mindmeld.now).** Seed dyads from real mention pairs in the cohort and simulate two-agent exchanges; compare simulated conversational dynamics to the real mention/reply patterns. Directly exercises mindmeld.now's bilateral-agent-social-network premise with grounded personas.
5. **Behavioral adherence eval (MatrAIx's headline metric).** Hold out each cohort user's last N tweets, generate synthetic ones from their persona, score with TweetEval classifiers plus a human/LLM judge, and report an adherence percentage — a crisp, demo-able number for the share-out round.

## Reproduce

```bash
# data/ (git-ignored): http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
.venv/bin/python scripts/sentiment140_stats.py
```
