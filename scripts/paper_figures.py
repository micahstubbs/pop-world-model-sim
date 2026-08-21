#!/usr/bin/env python3
"""Generate figures for the popsim arXiv paper from the real data/artifacts.

Usage: .venv/bin/python scripts/paper_figures.py
Writes PNG (300 dpi, for verify) + PDF (vector, for LaTeX) into docs/paper/figures/.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path("docs/paper/figures")
OUT.mkdir(parents=True, exist_ok=True)

# print-safe palette (colorblind-safe on white)
NEG = "#c8502e"      # ember
POS = "#0f7f6d"      # teal
AMB = "#b0791f"      # amber
BLU = "#4a63b8"      # blue
GRY = "#6f6f6f"

plt.rcParams.update({
    "font.family": "serif", "font.size": 8.5, "axes.titlesize": 9, "axes.labelsize": 8.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#dddddd", "grid.linewidth": .5, "grid.linestyle": ":",
    "figure.dpi": 300, "savefig.bbox": "tight",
})

FIGW = 3.4  # single-column width (in)


def save(fig, name):
    fig.savefig(OUT / f"{name}.png")
    fig.savefig(OUT / f"{name}.pdf")
    plt.close(fig)
    print("wrote", name)


stats = json.load(open("site/data/stats.json"))
adh = json.load(open("site/data/adherence.json"))
diff = json.load(open("site/data/diffusion.json"))
ladder = json.load(open("site/data/ladder.json"))
rel = json.load(open("site/data/relationships.json"))

COLS = ["polarity", "tweet_id", "date", "query", "user", "text"]
df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", encoding="latin-1", names=COLS)
uc = df.groupby("user").size()

# ---- fig 1: per-user tweet count distribution (log-log ccdf-style histogram) ----
fig, ax = plt.subplots(figsize=(FIGW, 2.4))
counts = uc.value_counts().sort_index()
ax.loglog(counts.index, counts.values, ".", color=BLU, ms=3.5, alpha=.8)
ax.axvline(20, color=NEG, lw=1, ls="--")
ax.text(21, counts.values.max() * .25, "cohort threshold\n($\\geq$20 tweets)", fontsize=7.5, color=NEG)
ax.set_xlabel("tweets by user $k$")
ax.set_ylabel("number of users")
ax.set_title("Per-user tweet counts (1.6M tweets, 659,775 users)")
save(fig, "fig1_user_distribution")

# ---- fig 2: diurnal cycle ----
def ampm(h):
    """0 -> '12 a.m.', 13 -> '1 p.m.', 23 -> '11 p.m.'"""
    h = int(h) % 24
    return f"{(h % 12) or 12} {'a.m.' if h < 12 else 'p.m.'}"


fig, ax = plt.subplots(figsize=(FIGW, 2.2))
hours = np.arange(24)
vol = np.array(stats["by_hour"]) / 1000
ax.bar(hours, vol, color=POS, width=.8, edgecolor="white", linewidth=.4)
pk, tr = int(np.argmax(vol)), int(np.argmin(vol))
ax.annotate(f"peak {ampm(pk)}", (pk, vol[pk]), textcoords="offset points", xytext=(-3, 2),
            fontsize=7.5, ha="right", va="bottom")
ax.set_ylim(0, vol.max() * 1.12)
# Trough label floats in the clear space above the neighbouring bars (not over
# them) and points down to the trough bar with a thin leader.
ax.annotate(f"trough {ampm(tr)}", (tr, vol[tr]), textcoords="offset points", xytext=(0, 26),
            fontsize=7.5, ha="center", va="bottom",
            arrowprops=dict(arrowstyle="-", color=GRY, lw=.6, shrinkB=1))
ax.set_xlabel("hour of day (PDT)")
ax.set_ylabel("tweets (thousands)")
ticks = [0, 4, 8, 12, 16, 23]  # last tick is the 11 p.m. peak, not 8 p.m.
ax.set_xticks(ticks)
ax.set_xticklabels([ampm(h) for h in ticks], fontsize=7)
ax.set_xlim(-.7, 23.7)
ax.set_title("Diurnal activity cycle")
save(fig, "fig2_diurnal")

# ---- fig 3: diffusion validation ----
v = diff["validation"]
fig, ax = plt.subplots(figsize=(FIGW, 1.9))
labels = ["persistence\n(own past)", "DeGroot diffusion\n(neighbors)"]
vals = [v["r_baseline"], v["r_sim"]]
bars = ax.barh(labels, vals, color=[GRY, AMB], height=.55)
for b, val in zip(bars, vals):
    ax.text(val + .012, b.get_y() + b.get_height() / 2, f"r = {val:.2f}", va="center", fontsize=8)
ax.set_xlim(0, .85)
ax.set_xlabel(f"Pearson r vs. second-half sentiment (n = {v['n_users']:,} users)")
ax.set_title("Disposition beats diffusion")
ax.invert_yaxis()
save(fig, "fig3_diffusion")

# ---- fig 4: scale ladder cost ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FIGW * 2.05, 2.2))
tiers = ladder["tiers"]
names = [t["name"].replace(" ", "\n", 1) for t in tiers]
users = [t["users"] for t in tiers]
cols = [AMB, BLU, GRY]
b = ax1.bar(names, users, color=cols, width=.6)
ax1.set_yscale("log")
for bb, u in zip(b, users):
    ax1.text(bb.get_x() + bb.get_width() / 2, u * 1.25, f"{u:,}", ha="center", fontsize=7.5)
ax1.set_ylabel("users (log)")
ax1.set_title("Tier populations")
ax1.tick_params(axis="x", labelsize=7)

costs = [ladder["all_llm_cost"], ladder["ladder_cost"]]
b2 = ax2.bar(["all-LLM\npopulation", "mixture-of-models\nladder"], costs, color=[GRY, AMB], width=.5)
ax2.set_yscale("log")
for bb, cval in zip(b2, costs):
    ax2.text(bb.get_x() + bb.get_width() / 2, cval * 1.3, f"{cval:,.0f}", ha="center", fontsize=7.5)
ax2.set_ylabel("relative cost per tick (log)")
ax2.set_title(f"{ladder['savings_x']}$\\times$ cheaper")
ax2.tick_params(axis="x", labelsize=7)
fig.tight_layout()
save(fig, "fig4_ladder")

# ---- fig 5: adherence histogram ----
fig, ax = plt.subplots(figsize=(FIGW, 2.2))
bins = np.array(adh["acc_hist"])
edges = np.linspace(0, 1, len(bins) + 1)
centers = (edges[:-1] + edges[1:]) / 2
colors = [NEG if c < .5 else POS for c in centers]
ax.bar(centers, bins, width=.045, color=colors, edgecolor="white", linewidth=.3)
ax.axvline(.5, color=GRY, lw=1, ls="--")
ax.text(.455, max(bins) * .55, "chance", rotation=90, va="top", ha="right", fontsize=7, color=GRY)
ax.axvline(adh["adherence"], color=AMB, lw=1.2)
ax.text(adh["adherence"] + .01, max(bins) * .95, f"overall {adh['adherence']*100:.1f}%", fontsize=7.5, color=AMB, va="top")
ax.set_xlabel("per-user accuracy on held-out tweets")
ax.set_ylabel("users")
ax.set_title(f"Baseline adherence across {adh['n_users']:,} personas")
save(fig, "fig5_adherence")

# ---- fig 6: relationship classes + attention shares ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FIGW * 2.05, 2.3))
pc = rel["pair_classes"]
order = ["one_off", "unidirectional_repeat", "mutual_weak", "unidirectional_strong", "mutual_strong"]
lab = ["one-off", "unidirectional\nrepeat", "mutual\nweak", "unidirectional\nstrong", "mutual\nstrong"]
vals = [pc[k] for k in order]
cols6 = [GRY, NEG, POS, NEG, POS]
b = ax1.bar(lab, vals, color=cols6, width=.62)
ax1.set_yscale("log")
for bb, u in zip(b, vals):
    ax1.text(bb.get_x() + bb.get_width() / 2, u * 1.3, f"{u:,}", ha="center", fontsize=6.8)
ax1.set_ylabel("pairs (log)")
ax1.set_title("Pair classes (293,212 observable pairs)")
ax1.tick_params(axis="x", labelsize=6.5)

att = rel["attention_share_pct"]
aorder = ["small_target", "broadcast_target_unobserved", "parasocial", "mostly_parasocial", "community_hub"]
alab = ["small\ntargets", "broadcast\n(unobs.)", "parasocial", "mostly\npara.", "community\nhubs"]
avals = [att[k] for k in aorder]
acols = [GRY, AMB, NEG, NEG, POS]
b2 = ax2.bar(alab, avals, color=acols, width=.62)
for bb, u in zip(b2, avals):
    ax2.text(bb.get_x() + bb.get_width() / 2, u + 1.5, f"{u}%", ha="center", fontsize=6.8)
ax2.set_ylabel("share of mention volume (%)")
ax2.set_title("Where attention flows")
ax2.tick_params(axis="x", labelsize=6.5)
fig.tight_layout()
save(fig, "fig6_parasocial")

print("done")
