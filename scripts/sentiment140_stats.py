#!/usr/bin/env python3
"""Descriptive statistics for the Sentiment140 dataset.

Usage: .venv/bin/python scripts/sentiment140_stats.py
Reads data/training.1600000.processed.noemoticon.csv, prints a stats summary.
"""
import re
import pandas as pd

COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
PATH = "data/training.1600000.processed.noemoticon.csv"

df = pd.read_csv(PATH, encoding="latin-1", names=COLS)
df["dt"] = pd.to_datetime(df["date"], format="%a %b %d %H:%M:%S PDT %Y")

print("== Corpus ==")
print(f"tweets: {len(df):,}")
print(f"distinct users: {df['user'].nunique():,}")
print(f"date range: {df['dt'].min()} .. {df['dt'].max()}")
print(f"polarity counts: {df['polarity'].value_counts().to_dict()}  (0=negative, 4=positive)")
print(f"in-memory size: {df.memory_usage(deep=True).sum()/1e6:.0f} MB")

print("\n== Per-user tweet counts ==")
uc = df.groupby("user").size().sort_values(ascending=False)
print(uc.describe().round(2).to_string())
for k in [2, 5, 10, 20, 50, 100]:
    print(f"users >= {k} tweets: {(uc >= k).sum():,} (covering {uc[uc >= k].sum():,} tweets)")
print("top 5 users:", uc.head(5).to_dict())

print("\n== Cohort: users with >= 20 tweets ==")
cohort_users = uc[uc >= 20].index
c = df[df["user"].isin(cohort_users)]
print(f"users: {len(cohort_users):,}   tweets: {len(c):,}")
print(f"tweets/user: mean {len(c)/len(cohort_users):.1f}, median {uc[uc>=20].median():.0f}, max {uc.max()}")
pol = c.groupby("polarity").size()
print(f"cohort polarity: {pol.to_dict()}")
span = c.groupby("user")["dt"].agg(["min", "max"])
days = (span["max"] - span["min"]).dt.days
print(f"per-user activity span (days): mean {days.mean():.0f}, median {days.median():.0f}")

print("\n== Text ==")
tl = df["text"].str.len()
print(f"chars/tweet: mean {tl.mean():.0f}, median {tl.median():.0f}, p95 {tl.quantile(.95):.0f}, max {tl.max()}")
wc = df["text"].str.split().str.len()
print(f"words/tweet: mean {wc.mean():.1f}, median {wc.median():.0f}")

print("\n== Interaction structure (@-mentions) ==")
has_mention = df["text"].str.contains(r"@\w", regex=True)
print(f"tweets containing @-mention: {has_mention.sum():,} ({has_mention.mean()*100:.1f}%)")
mentions = df.loc[has_mention, ["user", "text"]].copy()
mentions["target"] = mentions["text"].str.findall(r"@(\w+)")
edges = mentions.explode("target")
edges["target_lower"] = edges["target"].str.lower()
users_lower = set(u.lower() for u in df["user"].unique())
internal = edges[edges["target_lower"].isin(users_lower)]
print(f"mention edges total: {len(edges):,}; targets that are also dataset authors: {len(internal):,}")
cohort_lower = set(u.lower() for u in cohort_users)
cc = internal[internal["user"].str.lower().isin(cohort_lower) & internal["target_lower"].isin(cohort_lower)]
print(f"cohort-to-cohort mention edges: {len(cc):,} among {cc['user'].nunique():,} senders")

print("\n== Temporal ==")
per_day = df.set_index("dt").resample("D").size()
per_day = per_day[per_day > 0]
print(f"active days: {len(per_day)}; tweets/day mean {per_day.mean():.0f}, max {per_day.max():,}")
by_hour = df["dt"].dt.hour.value_counts().sort_index()
print(f"peak hour (PDT): {by_hour.idxmax()}:00 ({by_hour.max():,} tweets); trough: {by_hour.idxmin()}:00 ({by_hour.min():,})")
