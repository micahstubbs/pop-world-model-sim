#!/usr/bin/env python3
"""Build demo artifacts for the popsim explainer site.

Implements five directions on Sentiment140:
  1. persona mining (MatrAIx pattern)        -> personas.json
  2. full-LLM + surrogate scale ladder       -> ladder.json
  3. sentiment diffusion on mention graph    -> diffusion.json
  4. bilateral dyads from real mention pairs -> dyads.json
  5. held-out behavioral-adherence eval      -> adherence.json
  plus headline stats                        -> stats.json

Usage: .venv/bin/python scripts/build_demo_artifacts.py
Writes site/data/*.json
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path("site/data")
OUT.mkdir(parents=True, exist_ok=True)

COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", encoding="latin-1", names=COLS)
df["dt"] = pd.to_datetime(df["date"], format="%a %b %d %H:%M:%S PDT %Y")
df["pos"] = (df["polarity"] == 4).astype(int)
df = df.sort_values("dt").reset_index(drop=True)

uc = df.groupby("user").size()
cohort_users = uc[uc >= 20].index
c = df[df["user"].isin(cohort_users)].copy()

STOP = set("""the a an and or but if of to in on at for with is are was were be been am i you he she it we
they my your his her its our their me him them this that these those so just too very not no do does did done
have has had having get got will would can could should shall may might must about as by from up down out off
over under again then once here there when where why how all any both each few more most other some such only
own same than s t don now im ive u ur 2 4 amp quot lt gt""".split())


def top_words(texts, n=5):
    cnt = Counter()
    for t in texts:
        for w in re.findall(r"[a-z']{3,}", t.lower()):
            if w not in STOP and not w.startswith("http"):
                cnt[w] += 1
    return [w for w, _ in cnt.most_common(n)]


# ---------- 1. personas ----------
print("personas...")
g = c.groupby("user")
stats_u = pd.DataFrame({
    "n": g.size(),
    "pos": g["pos"].mean().round(3),
    "w": g["text"].apply(lambda s: s.str.split().str.len().mean()).round(1),
    "m": g["text"].apply(lambda s: s.str.contains(r"@\w").mean()).round(3),
    "ph": g["dt"].apply(lambda s: s.dt.hour.mode().iloc[0]),
    "span": (g["dt"].max() - g["dt"].min()).dt.days,
})
top300 = stats_u.sort_values("n", ascending=False).head(300)
personas = []
for u, row in top300.iterrows():
    texts = c.loc[c["user"] == u, "text"]
    ex = min(texts.tolist(), key=lambda t: abs(len(t) - 80))
    personas.append({"u": u, "n": int(row["n"]), "pos": float(row["pos"]), "w": float(row["w"]),
                     "m": float(row["m"]), "ph": int(row["ph"]), "span": int(row["span"]),
                     "top": top_words(texts), "ex": ex[:140]})
pos_hist = np.histogram(stats_u["pos"], bins=20, range=(0, 1))
json.dump({"cards": personas,
           "cohort": {"users": int(len(stats_u)), "tweets": int(stats_u['n'].sum()),
                      "pos_hist": pos_hist[0].tolist()}},
          open(OUT / "personas.json", "w"))

# ---------- 2. scale ladder ----------
print("ladder...")
t1 = uc[uc >= 50]
t2 = uc[(uc >= 20) & (uc < 50)]
t3 = uc[uc < 20]
COST = {"llm": 1000, "surrogate": 1, "stat": 0.01}  # relative cost per agent-tick
ladder = {
    "tiers": [
        {"name": "Full LLM agents", "rule": ">= 50 tweets", "users": int(len(t1)), "tweets": int(t1.sum()),
         "engine": "frontier LLM per tick", "cost_per_tick": COST["llm"]},
        {"name": "Distilled surrogates", "rule": "20-49 tweets", "users": int(len(t2)), "tweets": int(t2.sum()),
         "engine": "persona-conditioned small model", "cost_per_tick": COST["surrogate"]},
        {"name": "Statistical background", "rule": "< 20 tweets", "users": int(len(t3)), "tweets": int(t3.sum()),
         "engine": "rate + sentiment sampler", "cost_per_tick": COST["stat"]},
    ],
    "all_llm_cost": float(len(uc) * COST["llm"]),
    "ladder_cost": float(len(t1) * COST["llm"] + len(t2) * COST["surrogate"] + len(t3) * COST["stat"]),
}
ladder["savings_x"] = round(ladder["all_llm_cost"] / ladder["ladder_cost"], 1)
json.dump(ladder, open(OUT / "ladder.json", "w"))

# ---------- 3. diffusion on the real mention graph ----------
print("diffusion...")
lower_to_user = {u.lower(): u for u in cohort_users}
men = c[c["text"].str.contains(r"@\w")].copy()
men["targets"] = men["text"].str.findall(r"@(\w+)")
edges_all = men[["user", "targets", "pos", "dt"]].explode("targets")
edges_all["tl"] = edges_all["targets"].str.lower()
ce = edges_all[edges_all["tl"].isin(lower_to_user)].copy()
ce["target"] = ce["tl"].map(lower_to_user)
ce = ce[ce["user"] != ce["target"]]
ew = ce.groupby(["user", "target"]).size().reset_index(name="w")

mid = c["dt"].median()
first = c[c["dt"] <= mid].groupby("user")["pos"].agg(["mean", "size"])
second = c[c["dt"] > mid].groupby("user")["pos"].agg(["mean", "size"])
valid = first[first["size"] >= 5].join(second[second["size"] >= 5], lsuffix="_a", rsuffix="_b").dropna()

# DeGroot diffusion: s(t+1) = alpha*s(t) + (1-alpha)*neighbor mean, seeded with first-half sentiment
nbrs = defaultdict(list)
for _, r in ew.iterrows():
    if r["user"] in valid.index and r["target"] in valid.index:
        nbrs[r["user"]].append((r["target"], r["w"]))
s = valid["mean_a"].to_dict()
ALPHA = 0.7
for _ in range(10):
    s_new = {}
    for u in s:
        nb = nbrs.get(u, [])
        if nb:
            nb_mean = sum(s[t] * w for t, w in nb) / sum(w for _, w in nb)
            s_new[u] = ALPHA * s[u] + (1 - ALPHA) * nb_mean
        else:
            s_new[u] = s[u]
    s = s_new
sim = pd.Series(s)
r_sim = float(np.corrcoef(sim, valid.loc[sim.index, "mean_b"])[0, 1])
r_base = float(np.corrcoef(valid["mean_a"], valid["mean_b"])[0, 1])
connected = [u for u in sim.index if nbrs.get(u)]
r_sim_conn = float(np.corrcoef(sim[connected], valid.loc[connected, "mean_b"])[0, 1])
r_base_conn = float(np.corrcoef(valid.loc[connected, "mean_a"], valid.loc[connected, "mean_b"])[0, 1])

# viewer subgraph: top-degree nodes of largest component-ish neighborhood
deg = Counter()
for _, r in ew.iterrows():
    deg[r["user"]] += r["w"]; deg[r["target"]] += r["w"]
keep = set([u for u, _ in deg.most_common(320)])
sub_e = ew[ew["user"].isin(keep) & ew["target"].isin(keep)]
sub_nodes = sorted(set(sub_e["user"]) | set(sub_e["target"]))
upos = c.groupby("user")["pos"].mean()
nodes_out = [{"id": u, "s": round(float(upos.get(u, .5)), 3), "d": int(deg[u])} for u in sub_nodes]
edges_out = [{"s": r["user"], "t": r["target"], "w": int(r["w"])} for _, r in sub_e.iterrows()]

daily = c.set_index("dt")["pos"].resample("D").agg(["mean", "size"])
daily = daily[daily["size"] > 100]
json.dump({
    "validation": {"r_sim": round(r_sim, 3), "r_baseline": round(r_base, 3),
                   "r_sim_connected": round(r_sim_conn, 3), "r_baseline_connected": round(r_base_conn, 3),
                   "n_users": int(len(sim)), "n_connected": len(connected), "alpha": ALPHA, "steps": 10},
    "graph": {"nodes": nodes_out, "edges": edges_out,
              "total_edges": int(len(ew)), "total_weight": int(ew['w'].sum())},
    "daily": [{"d": d.strftime("%m-%d"), "pos": round(float(r["mean"]), 3), "n": int(r["size"])}
              for d, r in daily.iterrows()],
}, open(OUT / "diffusion.json", "w"))

# ---------- 4. bilateral dyads ----------
print("dyads...")
pair_w = {}
for _, r in ew.iterrows():
    key = tuple(sorted([r["user"], r["target"]]))
    d = pair_w.setdefault(key, {})
    d[(r["user"], r["target"])] = r["w"]
recip = [(k, v) for k, v in pair_w.items() if len(v) == 2]
recip.sort(key=lambda kv: min(kv[1].values()), reverse=True)
dyads = []
for (a, b), w in recip[:12]:
    ex = []
    for u, t in [(a, b), (b, a)]:
        rows = ce[(ce["user"] == u) & (ce["target"] == t)].head(2)
        for _, rr in rows.iterrows():
            full = c[(c["user"] == u) & (c["dt"] == rr["dt"])]["text"]
            if len(full):
                ex.append({"from": u, "to": t, "text": full.iloc[0][:140], "pos": int(rr["pos"])})
    dyads.append({"a": a, "b": b,
                  "w_ab": int(w[(a, b)]), "w_ba": int(w[(b, a)]),
                  "pos_a": round(float(upos[a]), 2), "pos_b": round(float(upos[b]), 2),
                  "ex": ex[:4]})
json.dump({"dyads": dyads, "reciprocal_pairs": len(recip)}, open(OUT / "dyads.json", "w"))

# ---------- 5. behavioral adherence (held-out eval) ----------
print("adherence...")
per_user_acc = []
n_test_total, n_hit_total = 0, 0
for u, grp in c.groupby("user"):
    grp = grp.sort_values("dt")
    k = max(4, int(len(grp) * 0.2))
    train, test = grp.iloc[:-k], grp.iloc[-k:]
    pred = int(train["pos"].mean() >= 0.5)
    hits = int((test["pos"] == pred).sum())
    per_user_acc.append(hits / len(test))
    n_hit_total += hits
    n_test_total += len(test)
adherence = n_hit_total / n_test_total
acc_hist = np.histogram(per_user_acc, bins=20, range=(0, 1))

# surrogate text samples: word-bigram Markov per heavy user (clearly labeled synthetic)
# Bot/spam accounts among the heaviest posters — skip them; a template-spam
# "real tweet" is a useless example of persona voice.
BOT_USERS = {"webwoke", "tweetpet", "what_bugs_u", "wowlew"}
# Curated picks for the displayed samples (pop-world-model-sim-nig): a
# substantive real tweet and a Markov seed whose walk reads coherently.
# Seeds index a fresh default_rng per user; real text must be verbatim.
CURATED = {
    "tsarnick": ("@tequilakitty haha you're a bit paranoid aren't you??  i like it. i don't want to get blocked!", [16, 2]),
    "TraceyHewins": ("@keza34 Watching the Wizard of Oz for the millionth time with me. Cooking for me! lol I know. I'm lucky", [7, 12]),
    "SallytheShizzle": (None, [10, 1]),
}
rng = np.random.default_rng(42)
samples = []
heavy = [u for u in stats_u.sort_values("n", ascending=False).index if u not in BOT_USERS]
# site shows the first 4; lead with the curated human voices, then fill by volume
order = ["lost_dog", "tsarnick", "TraceyHewins", "SallytheShizzle"]
order += [u for u in heavy if u not in order][:2]
for u in order:
    texts = c.loc[c["user"] == u, "text"].tolist()
    chains = defaultdict(list)
    starts = []
    for t in texts:
        ws = t.split()
        if len(ws) > 2:
            starts.append(ws[0])
            for i in range(len(ws) - 1):
                chains[ws[i]].append(ws[i + 1])
    real_pick, seeds = CURATED.get(u, (None, [None, None]))
    gen = []
    for seed in seeds:
        r = rng if seed is None else np.random.default_rng(seed)
        w = r.choice(starts); out = [w]
        for _ in range(16):
            nxt = chains.get(w)
            if not nxt:
                break
            w = str(r.choice(nxt)); out.append(w)
        gen.append(" ".join(out)[:140])
    real = next((t for t in texts if real_pick and t.strip() == real_pick.strip()), texts[0])
    samples.append({"u": u, "real": real[:140], "synthetic": gen})

json.dump({"adherence": round(adherence, 4),
           "n_users": len(per_user_acc), "n_test_tweets": n_test_total,
           "baseline": 0.5, "acc_hist": acc_hist[0].tolist(),
           "samples": samples},
          open(OUT / "adherence.json", "w"))

# ---------- headline stats ----------
json.dump({
    "tweets": int(len(df)), "users": int(df["user"].nunique()),
    "cohort_users": int(len(cohort_users)), "cohort_tweets": int(len(c)),
    "days": 48, "mention_edges_cohort": int(ew["w"].sum()),
    "mem_mb": int(df.memory_usage(deep=True).sum() / 1e6),
    "by_hour": df["dt"].dt.hour.value_counts().sort_index().tolist(),
    "adherence": round(adherence, 3),
    "diffusion_r": round(r_sim, 3),
    "ladder_savings_x": ladder["savings_x"],
}, open(OUT / "stats.json", "w"))

for f in sorted(OUT.glob("*.json")):
    print(f"{f.name}: {f.stat().st_size/1024:.0f} KB")
print("done")
