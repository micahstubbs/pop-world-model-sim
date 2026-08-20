#!/usr/bin/env python3
"""Relationship strength + parasocial classification on the Sentiment140 mention graph.

Builds the full directed @-mention graph (all 1.6M tweets), models pair-level
relationship strength, classifies pairs, and scores mention targets on a
parasociality index. Honest about observability: reciprocity is only measurable
when the target also appears as an author in the sample.

Usage: .venv/bin/python scripts/relationship_analysis.py
Writes site/data/relationships.json and prints a summary.
"""
import json
from collections import defaultdict

import numpy as np
import pandas as pd

COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", encoding="latin-1", names=COLS)
df["dt"] = pd.to_datetime(df["date"], format="%a %b %d %H:%M:%S PDT %Y")
df["pos"] = (df["polarity"] == 4).astype(int)

authors_lower = {}
for u in df["user"].unique():
    authors_lower.setdefault(u.lower(), u)

m = df[df["text"].str.contains(r"@\w")].copy()
m["targets"] = m["text"].str.findall(r"@(\w+)")
e = m[["user", "targets", "pos", "dt"]].explode("targets").dropna(subset=["targets"])
e["tgt_l"] = e["targets"].str.lower()
e["src_l"] = e["user"].str.lower()
e = e[e["src_l"] != e["tgt_l"]]
e["day"] = e["dt"].dt.date

print(f"mention events: {len(e):,}  distinct senders: {e['src_l'].nunique():,}  distinct targets: {e['tgt_l'].nunique():,}")

# ---------- directed edge table ----------
ed = e.groupby(["src_l", "tgt_l"]).agg(w=("dt", "size"), days=("day", "nunique"), pos=("pos", "mean")).reset_index()
ed["tgt_in_sample"] = ed["tgt_l"].isin(authors_lower)
print(f"directed edges: {len(ed):,}  ({ed['tgt_in_sample'].mean()*100:.1f}% of edges point at in-sample authors)")

# ---------- pair-level model (both users in sample => reciprocity observable) ----------
obs = ed[ed["tgt_in_sample"]].copy()
key = obs.apply(lambda r: tuple(sorted([r["src_l"], r["tgt_l"]])), axis=1)
obs = obs.assign(pair=key)
pairs = {}
for _, r in obs.iterrows():
    p = pairs.setdefault(r["pair"], {"a": r["pair"][0], "b": r["pair"][1], "w_ab": 0, "w_ba": 0, "days_ab": 0, "days_ba": 0})
    if r["src_l"] == r["pair"][0]:
        p["w_ab"] = int(r["w"]); p["days_ab"] = int(r["days"])
    else:
        p["w_ba"] = int(r["w"]); p["days_ba"] = int(r["days"])
P = pd.DataFrame(pairs.values())
P["total"] = P["w_ab"] + P["w_ba"]
P["mn"] = P[["w_ab", "w_ba"]].min(axis=1)
P["mx"] = P[["w_ab", "w_ba"]].max(axis=1)
P["reciprocity"] = P["mn"] / P["mx"]
P["persistence"] = P[["days_ab", "days_ba"]].max(axis=1)
# strength: volume x persistence, with a reciprocity multiplier (mutual ties are
# relationally "stronger" than the same volume one-way)
P["strength"] = np.log1p(P["total"]) * np.log1p(P["persistence"]) * (1 + P["reciprocity"])


def classify(r):
    if r["mn"] >= 3:
        return "mutual_strong"
    if r["mn"] >= 1:
        return "mutual_weak"
    if r["mx"] >= 5:
        return "unidirectional_strong"   # persistent one-way attention, never returned
    if r["mx"] >= 2:
        return "unidirectional_repeat"
    return "one_off"


P["cls"] = P.apply(classify, axis=1)
cls_counts = P["cls"].value_counts().to_dict()
print("\npair classes (both users in sample):", cls_counts)

# ---------- target-level parasociality index ----------
tgt = ed.groupby("tgt_l").agg(audience=("src_l", "nunique"), mentions_in=("w", "sum"),
                              in_sample=("tgt_in_sample", "first")).reset_index()
# reciprocation: of the senders who mention T, how many does T mention back?
out_sets = defaultdict(set)
for _, r in ed.iterrows():
    out_sets[r["src_l"]].add(r["tgt_l"])
big = tgt[tgt["audience"] >= 20].copy()


def recip_rate(t):
    fans = set(e.loc[e["tgt_l"] == t, "src_l"])
    back = out_sets.get(t, set())
    return len(fans & back) / len(fans) if fans else 0.0


big["recip_rate"] = big["tgt_l"].apply(recip_rate)
# parasociality: big audience, low reciprocation. Only claim it when T is in
# sample (their silence is observed, not censored).
big["parasocial_score"] = np.log1p(big["audience"]) * (1 - big["recip_rate"])
big["label"] = np.where(~big["in_sample"], "broadcast_target_unobserved",
               np.where(big["recip_rate"] < 0.05, "parasocial",
               np.where(big["recip_rate"] < 0.25, "mostly_parasocial", "community_hub")))
print("\ntarget labels (audience >= 20):", big["label"].value_counts().to_dict())

top_para = big[big["label"] == "parasocial"].sort_values("audience", ascending=False).head(15)
top_hub = big[big["label"] == "community_hub"].sort_values("audience", ascending=False).head(10)
top_unobs = big[big["label"] == "broadcast_target_unobserved"].sort_values("audience", ascending=False).head(15)
print("\nTop parasocial (in-sample, observed silence):")
print(top_para[["tgt_l", "audience", "mentions_in", "recip_rate"]].to_string(index=False))
print("\nTop broadcast targets (reciprocity unobservable — likely celebrities):")
print(top_unobs[["tgt_l", "audience", "mentions_in"]].to_string(index=False))
print("\nTop community hubs (big audience, high reciprocation):")
print(top_hub[["tgt_l", "audience", "mentions_in", "recip_rate"]].to_string(index=False))

# ---------- fan-side view: strongest unrequited attachments ----------
uni = P[P["cls"] == "unidirectional_strong"].sort_values("mx", ascending=False)
print(f"\nstrongest unrequited (both in sample): {len(uni):,} pairs; top:")
for _, r in uni.head(8).iterrows():
    a, b = (r["a"], r["b"]) if r["w_ab"] > r["w_ba"] else (r["b"], r["a"])
    print(f"  {a} -> {b}: {int(r['mx'])} mentions over {int(r['persistence'])} days, zero back")

strongest = P[P["cls"] == "mutual_strong"].sort_values("strength", ascending=False).head(10)
print("\nstrongest mutual relationships:")
for _, r in strongest.iterrows():
    print(f"  {r['a']} <-> {r['b']}: {int(r['w_ab'])}+{int(r['w_ba'])} mentions, {int(r['persistence'])} days, strength {r['strength']:.1f}")

# ---------- share of attention that is parasocial ----------
ed2 = ed.merge(big[["tgt_l", "label"]], on="tgt_l", how="left")
att = ed2.groupby(ed2["label"].fillna("small_target"))["w"].sum()
print("\nmention volume by target class:")
print((att / att.sum() * 100).round(1).to_string())

json.dump({
    "pair_classes": cls_counts,
    "n_pairs_observed": int(len(P)),
    "target_labels": big["label"].value_counts().to_dict(),
    "attention_share_pct": (att / att.sum() * 100).round(1).to_dict(),
    "top_parasocial": top_para[["tgt_l", "audience", "mentions_in", "recip_rate"]].round(3).to_dict("records"),
    "top_broadcast_unobserved": top_unobs[["tgt_l", "audience", "mentions_in"]].to_dict("records"),
    "top_hubs": top_hub[["tgt_l", "audience", "mentions_in", "recip_rate"]].round(3).to_dict("records"),
    "strongest_mutual": strongest[["a", "b", "w_ab", "w_ba", "persistence", "strength"]].round(2).to_dict("records"),
    "strongest_unrequited": uni.head(10)[["a", "b", "w_ab", "w_ba", "persistence"]].to_dict("records"),
}, open("site/data/relationships.json", "w"))
print("\nwrote site/data/relationships.json")
