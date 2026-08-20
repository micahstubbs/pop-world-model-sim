#!/usr/bin/env python3
"""E3: add a char n-gram classifier and ensemble word+char+prior.
Same fixed protocol as adherence_lab.py; weights tuned on train-carved validation."""
import json
import time

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.calibration import CalibratedClassifierCV

t0 = time.time()


def log(msg):
    print(f"[{time.time()-t0:7.1f}s]", msg, flush=True)
    with open("docs/autoresearch-log.md", "a") as f:
        f.write(msg + "\n")


COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", encoding="latin-1", names=COLS)
df["dt"] = pd.to_datetime(df["date"], format="%a %b %d %H:%M:%S PDT %Y")
df["y"] = (df["polarity"] == 4).astype(int)
df = df.sort_values("dt").reset_index(drop=True)
uc = df.groupby("user").size()
cohort = set(uc[uc >= 20].index)
df["rank"] = df.groupby("user").cumcount()
df = df.merge(uc.rename("n_user"), left_on="user", right_index=True)
df["k_test"] = np.maximum(4, (df["n_user"] * 0.2).astype(int))
df["is_cohort"] = df["user"].isin(cohort)
df["is_test"] = df["is_cohort"] & (df["rank"] >= df["n_user"] - df["k_test"])
test = df[df["is_test"]]
train_all = df[~df["is_test"]]
train_cohort = train_all[train_all["is_cohort"]]
prior = train_cohort.groupby("user")["y"].mean()

tc = train_cohort.copy()
tc["trank"] = tc.groupby("user").cumcount()
tc = tc.merge(tc.groupby("user").size().rename("n_tr"), left_on="user", right_index=True)
tc["is_val"] = tc["trank"] >= tc["n_tr"] - np.maximum(2, (tc["n_tr"] * 0.2).astype(int))
val = tc[tc["is_val"]]
fit_pool = pd.concat([train_all[~train_all["is_cohort"]], tc[~tc["is_val"]]])
prior_fit = fit_pool[fit_pool["is_cohort"]].groupby("user")["y"].mean()

log(f"\n### E3 run {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')} — word+char+prior ensemble")


def fit_clf(ngram, analyzer, min_df, max_feat):
    vec = TfidfVectorizer(ngram_range=ngram, analyzer=analyzer, min_df=min_df,
                          max_features=max_feat, sublinear_tf=True)
    X = vec.fit_transform(fit_pool["text"])
    clf = CalibratedClassifierCV(
        SGDClassifier(loss="log_loss", alpha=1e-6, max_iter=8, tol=None, random_state=0),
        method="sigmoid", cv=3)
    clf.fit(X, fit_pool["y"])
    return (clf.predict_proba(vec.transform(val["text"]))[:, 1],
            clf.predict_proba(vec.transform(test["text"]))[:, 1])


pv_w, pt_w = fit_clf((1, 2), "word", 5, 800_000)
log(f"- word model refit ({time.time()-t0:.0f}s)")
pv_c, pt_c = fit_clf((3, 5), "char_wb", 10, 600_000)
log(f"- char 3-5gram model fit ({time.time()-t0:.0f}s)")

pv_prior = prior_fit.reindex(val["user"]).fillna(0.5).values
pt_prior = prior.reindex(test["user"]).values


def logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


best = (0, 0, 0, 0)
for a in np.arange(0, 1.01, 0.1):          # char weight among text models
    for w in np.arange(0, 0.81, 0.05):     # prior weight
        z = (1 - w) * ((1 - a) * logit(pv_w) + a * logit(pv_c)) + w * logit(pv_prior)
        acc = (((1 / (1 + np.exp(-z))) >= 0.5).astype(int) == val["y"].values).mean()
        if acc > best[0]:
            best = (acc, a, w, z)
acc_v, a, w, _ = best
log(f"- tuned on validation: char_share={a:.1f}, prior_weight={w:.2f} (val acc {acc_v*100:.1f}%)")
z_t = (1 - w) * ((1 - a) * logit(pt_w) + a * logit(pt_c)) + w * logit(pt_prior)
pred = ((1 / (1 + np.exp(-z_t))) >= 0.5).astype(int)
e3 = (pred == test["y"].values).mean()
log(f"- **E3 word+char+prior ensemble: {e3*100:.1f}%** over {len(test):,} test tweets")

tt = test.copy(); tt["hit"] = (pred == tt["y"].values)
per_user = tt.groupby("user")["hit"].mean()
log(f"- per-user: mean {per_user.mean()*100:.1f}%, median {per_user.median()*100:.1f}%")
r = json.load(open("site/data/challenge_results.json"))
r["e3"] = round(float(e3), 4)
r["best"] = round(float(max(r["best"], e3)), 4)
r["per_user_hist"] = np.histogram(per_user, bins=20, range=(0, 1))[0].tolist()
json.dump(r, open("site/data/challenge_results.json", "w"))
log(f"\n**Best: {r['best']*100:.1f}%** (floor 63.1%, bar 91.5%). Plateau check: if E3 ~ E2, "
    "remaining headroom likely needs a pretrained twitter LM (roberta) — log and stop.\n")
print("DONE", flush=True)
