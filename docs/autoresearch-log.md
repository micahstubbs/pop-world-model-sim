# Autoresearch log — §06 adherence challenge

Protocol: 6,245-user cohort, per-user temporal 80/20 split, sentiment adherence over 42,998 held-out tweets. Floor 63.1%, bar 91.5%.


## Run 2026-08-19 21:34

- split: 42,998 test tweets across 6,245 users; 1,557,002 trainable tweets
- **E0 per-user train-majority prior: 63.1%** (protocol floor)
- validation slice: 34,186 tweets; classifier fit pool: 1,522,816 tweets
- TF-IDF: 391,189 features
- **E1 global TF-IDF+logistic on test text: 81.5%**
- blend weight tuned on validation: w_prior=0.45 (val acc 85.1%)
- **E2 text+prior blend: 82.0%**
- per-user accuracy: mean 82.0%, median 83.3%, quantiles {0.1: 0.5, 0.25: 0.75, 0.5: 0.833, 0.75: 1.0, 0.9: 1.0}

**Best so far: 82.0%** (floor 63.1%, bar 91.5%). Next hypotheses: char 3-5gram vote; user-conditioned features; twitter-roberta zero-shot.


### E3 run 2026-08-19 21:36 — word+char+prior ensemble
- word model refit (47s)
- char 3-5gram model fit (147s)
- tuned on validation: char_share=0.1, prior_weight=0.45 (val acc 85.1%)
- **E3 word+char+prior ensemble: 81.9%** over 42,998 test tweets
- per-user: mean 82.0%, median 83.3%

**Best: 82.0%** (floor 63.1%, bar 91.5%). Plateau check: if E3 ~ E2, remaining headroom likely needs a pretrained twitter LM (roberta) — log and stop.

