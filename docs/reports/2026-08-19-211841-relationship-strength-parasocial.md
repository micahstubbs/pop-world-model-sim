# Relationship Strength and Parasocial Structure in the Sentiment140 Mention Graph

**Generated:** 2026-08-19
**Script:** `scripts/relationship_analysis.py` · **Artifact:** `site/data/relationships.json`

## Method

Built the full directed @-mention graph over all 1.6M tweets (not just the ≥20-tweet cohort). For every ordered pair we count mentions and distinct active days; for every unordered pair where **both users are authors in the sample** (so silence is observed, not censored) we model:

- **Reciprocity** r = min(w_ab, w_ba) / max(w_ab, w_ba) ∈ [0,1]
- **Strength** = log(1+total mentions) × log(1+persistence in days) × (1+r) — volume alone doesn't make a relationship; repeated contact over time does, and mutuality multiplies it.

Pairs classify as: `mutual_strong` (≥3 each way), `mutual_weak` (≥1 each way), `unidirectional_strong` (≥5 one way, zero back), `unidirectional_repeat` (2–4 one way, zero back), `one_off`.

Targets with an audience of ≥20 distinct mentioners get a **parasociality index** = log(1+audience) × (1−reciprocation rate), where reciprocation rate = share of their mentioners they ever mention back. Targets who never author a tweet in the sample are labeled `broadcast_target_unobserved` — their silence is unmeasurable in a 1% sample, so we do not claim parasociality, only broadcast-scale attention.

## Findings

**Pair-level (293,212 observable pairs):**

| class | pairs | share |
|---|---|---|
| one_off | 226,103 | 77.1% |
| mutual_weak | 31,634 | 10.8% |
| unidirectional_repeat | 31,617 | 10.8% |
| unidirectional_strong | 1,957 | 0.7% |
| mutual_strong | 1,901 | 0.6% |

Genuine relationships are rare and symmetric classes are eerily balanced: ~1,900 strong mutual bonds vs ~1,950 strong one-way attachments. For every real friendship in the observable graph there is roughly one sustained unrequited attachment.

**Target-level (654 in-sample targets with audience ≥20, plus 524 out-of-sample):**

- **408 `parasocial`** — in-sample accounts that reciprocate <5% of their mentioners. Top: `wossy` (Jonathan Ross, 368 fans, 0.5% reciprocation), `ashleytisdale` (362 fans, 0.0%), `officialtila`, `alexalltimelow`, `therealjordin`, `tomfelton` (315 fans, 0.3%), `songzyuuup` — 2009-era celebrities who tweet but do not talk back.
- **163 `mostly_parasocial`** (5–25% reciprocation) and **163 `community_hub`** — big-audience accounts that DO talk back (`pembsdave` 73 fans at 32%, `paul_steele` 53%). Same audience scale, opposite social contract.
- **524 `broadcast_target_unobserved`** — the true celebrity tier, absent as authors: `jonasbrothers` (1,901 distinct fans, 2,384 mentions in 48 days), `taylorswift13` (929), `mitchelmusso`, NKOTB members (`jonathanrknight` 717, `jordanknight` 710), `aplusk`, `stephenfry`.

**Attention economy:** 87.0% of mention volume goes to small targets (audience <20) — ordinary conversation. But **12.1% of all mention volume flows to broadcast/parasocial accounts** (5.7% out-of-sample broadcast + 5.6% in-sample parasocial + 0.8% mostly-parasocial), while genuinely reciprocating hubs receive just 1.0%. Measured by attention, parasocial attachment outweighs community leadership by an order of magnitude.

**Extremes:**
- Strongest unrequited: `keren4562 → tommcfly` — 73 mentions in 10 days, zero back. Also multiple sustained one-way attachments to `mileycyrus` (55 and 52 mentions from single fans) — and notably `violetscruk → glasgowlassy` (46 mentions over 12 days), an unrequited *peer* attachment, not a celebrity one.
- Strongest mutual: `mlexiehayden ↔ msjuicy313` (42+41 mentions over 21 days, strength 27.1) — the §04 dyads of the demo site reappear at the top of the model's ranking, a consistency check between the two analyses.

## Implications for the world model

1. **A realistic simulated population needs a broadcast tier.** ~12% of attention flows to accounts that structurally never respond. Agent populations built only of peers mis-model the attention economy.
2. **Parasocial edges are cheap to simulate** — they are one-directional by definition, so the celebrity side needs no LLM at all (a content feed suffices). This slots directly into the §02 scale ladder as a fourth, near-zero-cost tier.
3. **The `unidirectional_strong` peer pairs (like violetscruk → glasgowlassy) are the interesting hard case** — one-way attention between ordinary people, invisible in celebrity-centric models.

## Caveats

A 1% sample censors reciprocity: a target's reply can be missing from the sample rather than nonexistent. We mitigate by (a) claiming parasociality only for in-sample authors, (b) requiring audience ≥20 so a ~0% observed reciprocation rate is statistically meaningful, and (c) labeling out-of-sample targets as unobserved rather than parasocial. Mention ≠ relationship; we never see follows, DMs, or reads.
