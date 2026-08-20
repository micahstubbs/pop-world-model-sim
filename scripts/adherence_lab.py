#!/usr/bin/env python3
"""§06 adherence challenge: autonomous research loop.

Protocol (fixed): cohort = 6,245 users with >=20 tweets; per-user temporal split,
train = first 80%, test = last 20% (min 4); metric = accuracy on held-out
sentiment labels over all test tweets. Never trains on any user's test tweets.

Experiments:
  E0  per-user train-majority prior (reproduces the 63.1% floor)
  E1  global text classifier (TF-IDF word 1-2grams + SGD-logistic) trained on
      every tweet in the corpus EXCEPT cohort test tweets
  E2  blend of E1 probability with the per-user prior, weight tuned on a
      validation slice carved from TRAIN only
  E3  E2 + char n-gram classifier vote (if time permits)

Appends results to docs/autoresearch-log.md.
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.calibration import CalibratedClassifierCV

t0 = time.time()
LOG = Path("docs/autoresearch-log.md")
LOG.parent.mkdir(exist_ok=True, parents=True)


def log(msg):
    stamp = f"[{time.time()-t0:7.1f}s]"
    print(stamp, msg, flush=True)
    with open(LOG, "a") as f:
        f.write(msg + "\n")


if not LOG.exists() or LOG.stat().st_size == 0:
    with open(LOG, "w") as f:
        f.write("# Autoresearch log — §06 adherence challenge\n\n"
                "Protocol: 6,245-user cohort, per-user temporal 80/20 split, "
                "sentiment adherence over 42,998 held-out tweets. Floor 63.1%, bar 91.5%.\n\n")

COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", encoding="latin-1", names=COLS)
df["dt"] = pd.to_datetime(df["date"], format="%a %b %d %H:%M:%S PDT %Y")
df["y"] = (df["polarity"] == 4).astype(int)
df = df.sort_values("dt").reset_index(drop=True)

uc = df.groupby("user").size()
cohort = set(uc[uc >= 20].index)

# per-user temporal split
df["rank"] = df.groupby("user").cumcount()
df = df.merge(uc.rename("n_user"), left_on="user", right_index=True)
df["k_test"] = np.maximum(4, (df["n_user"] * 0.2).astype(int))
df["is_cohort"] = df["user"].isin(cohort)
df["is_test"] = df["is_cohort"] & (df["rank"] >= df["n_user"] - df["k_test"])

test = df[df["is_test"]]
train_all = df[~df["is_test"]]                      # everything except cohort test tweets
train_cohort = train_all[train_all["is_cohort"]]
log(f"\n## Run {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
log(f"- split: {len(test):,} test tweets across {test['user'].nunique():,} users; "
    f"{len(train_all):,} trainable tweets")
assert test["user"].nunique() == 6245

# E0: per-user prior
prior = train_cohort.groupby("user")["y"].mean()
e0_pred = (prior.reindex(test["user"]).values >= 0.5).astype(int)
e0 = (e0_pred == test["y"].values).mean()
log(f"- **E0 per-user train-majority prior: {e0*100:.1f}%** (protocol floor)")

# validation slice from TRAIN only (last 20% of each cohort user's train segment)
tc = train_cohort.copy()
tc["trank"] = tc.groupby("user").cumcount()
tc = tc.merge(tc.groupby("user").size().rename("n_tr"), left_on="user", right_index=True)
tc["is_val"] = tc["trank"] >= tc["n_tr"] - np.maximum(2, (tc["n_tr"] * 0.2).astype(int))
val = tc[tc["is_val"]]
fit_pool = pd.concat([train_all[~train_all["is_cohort"]], tc[~tc["is_val"]]])
log(f"- validation slice: {len(val):,} tweets; classifier fit pool: {len(fit_pool):,} tweets")

# E1: global text classifier
vec = TfidfVectorizer(ngram_range=(1, 2), min_df=5, max_features=800_000,
                      sublinear_tf=True, strip_accents="unicode")
Xf = vec.fit_transform(fit_pool["text"])
log(f"- TF-IDF: {Xf.shape[1]:,} features")
base = SGDClassifier(loss="log_loss", alpha=1e-6, max_iter=8, tol=None, random_state=0)
clf = CalibratedClassifierCV(base, method="sigmoid", cv=3)
clf.fit(Xf, fit_pool["y"])
p_test = clf.predict_proba(vec.transform(test["text"]))[:, 1]
e1 = ((p_test >= 0.5).astype(int) == test["y"].values).mean()
log(f"- **E1 global TF-IDF+logistic on test text: {e1*100:.1f}%**")

# E2: blend with per-user prior, weight tuned on validation
p_val = clf.predict_proba(vec.transform(val["text"]))[:, 1]
prior_fit = fit_pool[fit_pool["is_cohort"]].groupby("user")["y"].mean()
pv_prior = prior_fit.reindex(val["user"]).fillna(0.5).values
pt_prior = prior.reindex(test["user"]).values  # full-train prior is legal for test


def logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


best_w, best_acc = 0, 0
for w in np.arange(0, 1.01, 0.05):
    blend = 1 / (1 + np.exp(-((1 - w) * logit(p_val) + w * logit(pv_prior))))
    acc = ((blend >= 0.5).astype(int) == val["y"].values).mean()
    if acc > best_acc:
        best_acc, best_w = acc, w
log(f"- blend weight tuned on validation: w_prior={best_w:.2f} (val acc {best_acc*100:.1f}%)")
blend_t = 1 / (1 + np.exp(-((1 - best_w) * logit(p_test) + best_w * logit(pt_prior))))
e2_pred = (blend_t >= 0.5).astype(int)
e2 = (e2_pred == test["y"].values).mean()
log(f"- **E2 text+prior blend: {e2*100:.1f}%**")

# per-user distribution for the best experiment
best_pred = e2_pred if e2 >= e1 else (p_test >= 0.5).astype(int)
tt = test.copy(); tt["hit"] = (best_pred == tt["y"].values)
per_user = tt.groupby("user")["hit"].mean()
q = per_user.quantile([.1, .25, .5, .75, .9]).round(3).to_dict()
log(f"- per-user accuracy: mean {per_user.mean()*100:.1f}%, "
    f"median {per_user.median()*100:.1f}%, quantiles {q}")
hist = np.histogram(per_user, bins=20, range=(0, 1))[0].tolist()

best = max(e0, e1, e2)
log(f"\n**Best so far: {best*100:.1f}%** (floor 63.1%, bar 91.5%). "
    f"Next hypotheses: char 3-5gram vote; user-conditioned features; twitter-roberta zero-shot.\n")

json.dump({"e0": round(e0, 4), "e1": round(e1, 4), "e2": round(e2, 4),
           "best": round(best, 4), "w_prior": best_w,
           "per_user_hist": hist, "n_test": int(len(test))},
          open("site/data/challenge_results.json", "w"))
print("DONE", flush=True)
