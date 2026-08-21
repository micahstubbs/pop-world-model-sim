# Related-work search for popsim (docs/paper/popsim.tex)

Search date: 2026-08-21. Sources: arXiv abs/HTML pages, Semantic Scholar API
(heavily rate-limited; used for record lookups only), ACL Anthology, First
Monday, PLoS ONE, web search. Every paper below had its abstract (and, where
noted, full text) read during this search. PNAS pages (Aral 2009, Kramer 2014)
blocked fetching; their title/author/venue records were confirmed via the
Semantic Scholar API and their content is summarized from the open PDF copies
and secondary sources (flagged inline).

Existing bibkeys in the paper: lightsociety, matraix, park2023, sentiment140,
tweeteval, kwak2010, horton1956, degroot1974.

---

## 1. Ranked recommended citations

Ranking = (how much the paper's claims depend on it) x (how likely a reviewer
is to ask "why didn't you cite X?").

### Tier A — should cite; a reviewer will expect these

**1. Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop**
Igor Itkin. 2026 (arXiv, submitted 19 Jul 2026). https://arxiv.org/abs/2608.11215
Replaces each LLM agent with a 2–12-parameter surrogate fitted by behavioral
cloning from a few hundred to a few thousand cheap LLM queries, then runs the
society at any N on a laptop; validated on eight named simulations
(EconAgent, AgentTorch, OASIS, AgentSociety, Generative Agents' Smallville,
etc.) with pre-registered predictions, total API spend "a few dollars."
Fit: Related Work (population-scale simulation) and §Ladder. This is the
closest prior work to the "billion-agent methodology on one machine" framing
and to the surrogate tier; popsim differs by grounding in a real corpus and
a real interaction graph rather than cloning LLM policies. Must cite.

**2. OASIS: Open Agent Social Interaction Simulations with One Million Agents**
Ziyi Yang, Zaibin Zhang, Zirui Zheng, ... Jing Shao. 2024/2025 (arXiv v5,
Mar 2025; ICML 2025). https://arxiv.org/abs/2411.11581
Open-source X/Reddit-style simulator scaling to 10^6 LLM agents with dynamic
networks, action spaces, and recommender; reproduces information spread,
polarization, herd effects. Fit: Related Work, population-scale simulation
sentence — the standard open million-agent baseline between Park 2023 and
Light Society.

**3. AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society**
Jinghua Piao, Yuwei Yan, ... Yong Li. 2025 (arXiv, v2 Apr 2026). https://arxiv.org/abs/2502.08691
Tens of thousands of LLM agents in a data-grounded urban environment with
social/economic/mobility behaviors; open-source framework (AgentSociety 2,
arXiv:2607.11895, 2026). Fit: Related Work, one clause alongside OASIS.

**4. SocioVerse: A World Model for Social Simulation Powered by LLM Agents and A Pool of 10 Million Real-World Users**
Xinnong Zhang, Jiayu Lin, ... Zhongyu Wei. 2025 (arXiv, v2 Jul 2025). https://arxiv.org/abs/2504.10157
Frames social simulation as a "world model" with explicit alignment of
environment, users (a pool of 10M real users), interactions, and behaviors;
experiments in politics, news, economics. Fit: Related Work — the
"human-grounded user pool" idea that popsim mirrors with 6,245 Sentiment140
users; also relevant because the paper's own title uses "world model."

**5. LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals** (originally "Generative Agent Simulations of 1,000 People")
Joon Sung Park, Carolyn Q. Zou, ... Michael S. Bernstein. 2024 (arXiv, v3 Jun 2026). https://arxiv.org/abs/2411.10109
Agents built from 2-hour interviews / surveys of 1,052 Americans predict
held-out survey responses at 83–86% of participants' own two-week
test-retest consistency vs. 74% for demographics-only agents. Fit:
§Benchmark — the canonical "does the agent behave like the real person"
evaluation; its test-retest normalization is the right contrast for
popsim's per-user temporal split and its "volatile tail" of users.

**6. BluePrint: A Social Media User Dataset for LLM Persona Evaluation and Training**
Aurélien Bück-Kaeffer, Je Qin Chooi, Dan Zhao, Maximilian Puelma Touzel, Kellin Pelrine, Jean-François Godbout, Reihaneh Rabbany, Zachary Yang. 2025 (arXiv). https://arxiv.org/abs/2510.02343
SIMPACT framework + BluePrint dataset from public Bluesky political
discussion: anonymized users clustered into personas, 12 interaction types
with preceding context, next-action prediction as the core task, metrics at
cluster and population level. Fit: §Benchmark related work — the nearest
existing "persona agent benchmark on a public social-media corpus";
companion SocialSim persona challenge (COLM 2025; winning entry White &
Shimorina, arXiv:2511.17241, hybrid history-lookup + LightGBM, macro-F1 0.64
common actions). popsim differs: per-user (not cluster) personas, a single
observable dimension, 2009 Twitter.

**7. How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation (BehaviorChain)**
Rui Li, Heming Xia, Xinfeng Yuan, Qingxiu Dong, Lei Sha, Wenjie Li, Zhifang Sui. 2025 (Findings of ACL 2025). https://arxiv.org/abs/2502.14642
15,846 behaviors over 1,001 personas; models iteratively predict the next
contextually appropriate behavior given persona + history; SOTA models
degrade as chains lengthen. Fit: §Benchmark — prior persona-behavior
benchmark; note it uses constructed personas, not real users' held-out
behavior.

**8. In the mood: the dynamics of collective sentiments on Twitter**
Nathaniel Charlton, Colin Singleton, Danica Vukadinović Greetham. 2016 (Royal Society Open Science 3:160162). https://arxiv.org/abs/1604.03427
Studies sentiment vs. the evolving @-mention network: highly central users
use more positive / less negative sentiment; sentiment of structurally
stable communities is stable over months, with sudden changes traceable to
external events; calibrates a simple ABM of emotive response. Fit:
§Diffusion — direct empirical precedent for "sentiment on the @-mention
graph is stable/dispositional rather than contagious at the community
level"; also §Parasocial (central users' sentiment profile).

**9. Measuring Emotional Contagion in Social Media**
Emilio Ferrara, Zeyao Yang. 2015 (PLoS ONE 10(11):e0142390). https://arxiv.org/abs/1506.06021
Observational Twitter study (one week, Sept 2014): linear relation between
valence of exposure and of subsequent posts, but tiny effects (negative
posts follow 4.34% over-exposure to negative content; positive 4.50%), with
a highly-susceptible minority and a scarcely-susceptible majority. Fit:
§Diffusion — the positive-but-weak contagion result that popsim's
persistence-beats-DeGroot finding is consistent with; must be cited to
avoid overclaiming "no diffusion."

**10. Experimental evidence of massive-scale emotional contagion through social networks**
Adam D. I. Kramer, Jamie Guillory, Jeffrey T. Hancock. 2014 (PNAS 111(24):8788–8790). https://doi.org/10.1073/pnas.1320040111
Facebook feed-manipulation experiment (N=689,003): reducing positive
(negative) content in feeds reduced positive (negative) posting; effects
real but very small (Cohen's d on the order of 0.001–0.02; summarized from
the open PDF, PNAS page blocked fetch). Fit: §Diffusion — causal evidence
that contagion exists but is small relative to within-person baselines.

**11. Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks**
Sinan Aral, Lev Muchnik, Arun Sundararajan. 2009 (PNAS 106(51):21544–21549). https://doi.org/10.1073/pnas.0908800106
Dynamic matched-sample estimation on 27.4M users shows homophily explains
more than half of apparent behavioral contagion; naive methods overstate
influence by 300–700% (numbers from the paper's abstract as reported in
the open PMC copy; PNAS page blocked fetch). Fit: §Diffusion interpretation
and Limitations — popsim's DeGroot-vs-persistence contrast is an instance
of "dispositional similarity masquerading as influence."

**12. Homophily and Contagion Are Generically Confounded in Observational Social Network Studies**
Cosma Rohilla Shalizi, Andrew C. Thomas. 2011 (Sociological Methods & Research 40(2):211–239). https://arxiv.org/abs/1004.4704
Proves that homophily, contagion and covariate effects are non-identifiable
from observational network data without strong assumptions. Fit:
Limitations — caveat that popsim's negative result shows diffusion does not
*help prediction*, not that influence is causally absent.

**13. Social networks that matter: Twitter under the microscope**
Bernardo A. Huberman, Daniel M. Romero, Fang Wu. 2009 (First Monday 14(1)). https://firstmonday.org/ojs/index.php/fm/article/view/2317
The declared follower graph hides a much sparser network of actual
@-interactions; users direct attention to a handful of reciprocating
"friends" regardless of follower count. Fit: §Parasocial — the original
observation that reciprocal @-mentions, not follows, define the relationship
backbone; popsim's 77%-one-off-contacts figure extends it.

**14. Measuring User Influence in Twitter: The Million Follower Fallacy**
Meeyoung Cha, Hamed Haddadi, Fabricio Benevenuto, Krishna P. Gummadi. 2010 (ICWSM). https://ojs.aaai.org/index.php/ICWSM/article/view/14033
Compares indegree, retweet and mention influence over 54M users; high
indegree does not imply retweet/mention influence; mention influence
concentrates on celebrities. Fit: §Parasocial — mention-based attention to
celebrities as a distinct channel, supporting the broadcast tier.

**15. User-Level Sentiment Analysis Incorporating Social Networks**
Chenhao Tan, Lillian Lee, Jie Tang, Long Jiang, Ming Zhou, Ping Li. 2011 (KDD). https://arxiv.org/abs/1109.6018
Shows follower and @-mention ties carry user-level sentiment homophily on
Twitter and that graph-regularized transductive models beat text-only SVMs.
Fit: §Diffusion — the constructive counterpart: neighbors *do* carry
information about a user's sentiment when used as a static prior, even
though dynamic mixing destroys information in popsim; worth one sentence.

**16. Social Influence and Opinions** (Friedkin–Johnsen model)
Noah E. Friedkin, Eugene C. Johnsen. 1990 (J. Mathematical Sociology 15(3–4):193–205). https://doi.org/10.1080/0022250X.1990.9990069
DeGroot averaging with a per-agent "stubbornness" anchor to the initial
opinion. Fit: §Diffusion + Limitations — the obvious "richer contagion
model" that interpolates persistence and DeGroot; name it explicitly as
future work (popsim's α=0.7 is a special case with no anchor).

### Tier B — strengthens specific claims

**17. Diurnal and Seasonal Mood Vary with Work, Sleep, and Daylength Across Diverse Cultures**
Scott A. Golder, Michael W. Macy. 2011 (Science 333(6051):1878–1881). https://doi.org/10.1126/science.1202775
Twitter mood of 2.4M users across 84 countries shows robust diurnal and
weekly cycles. Fit: §Dataset, diurnal figure — the canonical citation for
using Twitter diurnal rhythm to calibrate posting schedules.
(Alternative/addition: Dodds et al. 2011, "Temporal patterns of happiness
and information in a global social network: Hedonometrics and Twitter,"
PLoS ONE 6(12):e26752, https://arxiv.org/abs/1101.5120.)

**18. Will Scaling Improve Social Simulation with LLMs?**
Caleb Ziems, William Held, Su Doga Karaca, David Grusky, Tatsunori Hashimoto, Diyi Yang. 2026 (arXiv). https://arxiv.org/abs/2607.02464
85+35 models up to 70B: scale helps opinion/behavior modeling for
well-represented English populations, scales slowly for longitudinal
forecasting and underrepresented groups, fails to fix calibration to human
biases. Fit: §Ladder motivation — justifies spending frontier compute only
where signal is dense, and flags that longitudinal forecasting (popsim's
task) is exactly where scale helps least.

**19. LLM-Based Social Simulations Require a Boundary**
Zengqing Wu, Run Peng, Takayuki Ito, Makoto Onizuka, Chuan Xiao. 2025/2026 (ICML 2026 position paper). https://arxiv.org/abs/2506.19806
Systematic review: LLM agents act as an "average persona"; fewer than half
of validation studies assess behavioral variance and most find less
variance than humans; recommends reporting variance and restricting claims.
Fit: §Benchmark — motivates reporting the per-user adherence distribution
(bimodal) rather than only the 63.1% aggregate.

**20. Towards Operational Validation of LLM-Agent Social Simulations: A Replicated Study of a Reddit-like Technology Forum**
(authors per arXiv listing) 2025 (arXiv; EPJ Data Science 2026). https://arxiv.org/abs/2508.21740
30 independent 30-day Y Social simulations vs. 30 matched Voat windows:
activity rhythms, heavy tails and core–periphery reproduced; comment
volume, thread length and toxicity over-produced. Fit: Related Work —
example of validation against real platform ground truth, the practice
popsim follows at the individual level.

**21. APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents**
Quan Zheng, Yan Gao, Shaobin He, Haoxiang Guan, Yuanhe Tian, Jie Feng, Ming Wang, Shuxin Zheng, Zhen Liu. 2026 (arXiv). https://arxiv.org/abs/2605.27419
From the Light Society group: LLM as oracle on adaptive prototypes, local
response surfaces for nearby agents, shadow-audit correction; 381.1x fewer
LLM calls at 10M agents with final-round JSD 0.094 vs. full-LLM reference.
Fit: §Ladder — the follow-on to Light Society's mixture of models; directly
comparable "x-fold reduction" number (popsim's 702.7x is nominal, theirs is
measured).

**22. Integrating LLM and Diffusion-Based Agents for Social Simulation**
Xinyi Li, Zhiqiang Guo, Qinglang Guo, Hao Jin, Weizhi Ma, Min Zhang. 2025 (arXiv). https://arxiv.org/abs/2510.16366
Dual-tier design: LLM agents for a core user subset, diffusion-model agents
for the rest, unified simulation loop; better prediction on three real
datasets. Fit: §Ladder — independent instance of the core/background split.
(Related: TopoSim, Xu et al. 2026, arXiv:2604.18011, 50–90% token reduction
by grouping agents with similar structural roles into shared backbone
units.)

### Tier C — optional, one clause each

- **Y Social: an LLM-powered Social Media Digital Twin.** Rossetti et al. 2024. https://arxiv.org/abs/2408.00818 — open LLM social-media twin; Related Work list.
- **Characterizing LLM-driven Social Network: The Chirper.ai Case.** Zhu, He, Haq, Tyson, Hui. 2025/2026. https://arxiv.org/abs/2504.10286 — 65k LLM agents / 7.7M posts vs. Mastodon humans; posting and network-structure differences. Related Work or Limitations ("LLM populations differ structurally from humans").
- **Scaling Synthetic Data Creation with 1,000,000,000 Personas (PersonaHub).** Ge et al. 2024. https://arxiv.org/abs/2406.20094 — synthetic persona corpus MatrAIx builds on; contrast with popsim's behavior-derived personas.
- **Twin-2K-500.** Toubia et al. 2025 (Marketing Science 2025). https://arxiv.org/abs/2505.17479 — 2,058 respondents x 500 questions with a test-retest wave; survey-grounded twins with a human-consistency ceiling.
- **TwinVoice** (Du et al. 2025, https://arxiv.org/abs/2510.25536) and **PersonaArena** (Shi et al., Findings of ACL 2026, https://arxiv.org/abs/2605.17044) — persona-simulation benchmarks on real user-generated content (PersonaArena's persona bank from 19k users / 681k blog posts); both evaluate with LLM judges, not held-out real behavior.
- **Can LLMs Simulate Social Media Engagement?** Qiu, Lyu, Xiong, Luo 2025. https://arxiv.org/abs/2502.12073 — zero-shot LLMs underperform BERT at predicting real X users' actions; supports the "simple baselines are strong" framing of the 63.1% floor.
- **GRAPHIA.** Ji et al. 2025/2026. https://arxiv.org/abs/2510.24251 — real social graphs as supervision for simulation agents; relevant to "use the real mention graph."
- **A Graph-Based Framework for Temporal and Causal Analysis of Sentiments** (NTCGN), ACM Trans. Web 2025, https://doi.org/10.1145/3759440 — one of very few works using Sentiment140 for temporal/graph analysis (with GDELT) rather than classification; cite only if you want to claim "Sentiment140 has rarely been used beyond classification."

---

## 2. Closest prior work / has anyone done this?

**Frank assessment: no one has done the specific combination, but three pieces are individually close.**

1. **"Billion-agent methodology on one machine."** Itkin's *Poor Man's Agentic Modeling* (arXiv:2608.11215, Jul 2026) makes almost the same framing claim — large LLM-agent societies on a laptop for a few dollars — and it cites and re-implements OASIS, AgentSociety and Smallville. It is *not* grounded in real human data (it clones LLM policies into tiny surrogates) and does not validate against a real interaction graph. popsim's differentiator is real personas + real graph + held-out ground truth. The Related Work must acknowledge it directly or a reviewer will flag it; the title phrase "on a Single Machine" is now shared territory.

2. **Mixture-of-models / tiered compute.** Besides Light Society, APS (arXiv:2605.27419, same group) reports a *measured* 381.1x reduction at 10M agents; Li et al. (arXiv:2510.16366) and TopoSim (arXiv:2604.18011) use core-LLM/background splits. popsim's 702.7x is a nominal-unit estimate (the paper already says so in Limitations) and should be framed as an instantiation, not a new result.

3. **Persona-agent benchmark on a public social-media corpus.** BluePrint/SIMPACT (Bluesky, next-action prediction, cluster-level personas, COLM 2025 SocialSim challenge) is the nearest thing. Differences: BluePrint aggregates users into 25 persona clusters for privacy; popsim keeps individual users (public 2009 data) and a per-user temporal split on a single dimension (sentiment). Park et al. 2024 / Twin-2K-500 do the individual-level held-out test but on survey items, not observed behavior. **No one has published a persona-adherence benchmark on Sentiment140**, and no paper found uses Sentiment140's @-mention graph or per-user timelines for persona/diffusion work (NTCGN uses it for event-sentiment causality only). That novelty claim is safe.

4. **"Disposition beats diffusion."** Not new as a *phenomenon*: Charlton et al. 2016 found community sentiment on the @-mention network stable over months; Ferrara & Yang 2015 found contagion effects of ~4%; Aral et al. 2009 and Shalizi & Thomas 2011 show apparent contagion is mostly homophily. What is new is the specific predictive test (DeGroot over the real mention graph vs. per-user persistence, r=0.54 vs 0.73) on a public corpus. Rephrase the claim as a replication/quantification consistent with that literature, not a surprise.

5. **Parasocial structure.** Huberman et al. 2009 (reciprocal @-network is the "network that matters") and Cha et al. 2010 (mention influence concentrates on celebrities) are direct precedents; Kwak 2010 is already cited. The paper's contribution there is the pair-level classification and the 1,957 vs 1,901 count, plus the broadcast-tier implication — fine, but cite the precedents.

---

## 3. Suggested Related Work rewrite (LaTeX)

Proposed bibkeys: oasis, agentsociety, socioverse, park2024, poorman, aps,
hybriddiffusion, ysocial, chirper, blueprint, behaviorchain, twin2k,
personaarena, boundary, scaling, charlton2016, ferrara2015, kramer2014,
aral2009, shalizi2011, tan2011, huberman2009, cha2010, friedkin1990,
golder2011.

```latex
\section{Related Work}

\textbf{Population-scale simulation.} Generative agent-based modeling
descends from Park et al.'s generative agents \ecite{park2023}, which
demonstrated believable social behavior from memory-augmented LLM agents in
a small sandbox town. Open simulators have since pushed scale: OASIS
\ecite{oasis} models X- and Reddit-style platforms with up to $10^6$
agents, AgentSociety \ecite{agentsociety} simulates tens of thousands of
agents in a data-grounded urban environment, Y~Social \ecite{ysocial}
provides an open social-media digital twin, and SocioVerse
\ecite{socioverse} frames simulation as a world model aligned to a pool of
ten million real users. Light Society \ecite{lightsociety} formalizes
society simulation as structured transitions of agent and environment
states governed by LLM-powered operations, scaling to $10^9$ agents
grounded in World Values Survey profiles via a mixture-of-models engine
that routes requests among full LLMs, distilled surrogates, and
precomputed lookup tables; its successor APS \ecite{aps} reports a
measured $381\times$ reduction in LLM calls at $10^7$ agents. MatrAIx
\ecite{matraix} builds an 8.3B-record persona database (599{,}847
human-grounded profiles among the curated subset) and evaluates
behavioral adherence across four environments. Closest in spirit to our
framing, Itkin \ecite{poorman} shows that LLM-agent societies can be run
on a laptop by cloning each agent's policy into a few-parameter surrogate;
we pursue the complementary question of which elements survive when the
population, the interaction graph, and the validation target are all
real.

\textbf{Tiered compute.} Heterogeneous agent cost is now a recurring
design: core LLM agents with diffusion-model agents for the remaining
population \ecite{hybriddiffusion}, topology-aware grouping of agents
into shared backbone units \ecite{toposim}, and Light Society's surrogate
distillation \ecite{lightsociety}. Ziems et al.\ \ecite{scaling} find
that model scale helps opinion and behavior modeling for well-represented
populations but scales slowly for longitudinal forecasting, which
motivates spending frontier compute only on users with dense signal.

\textbf{Evaluating persona agents.} Park et al.\ \ecite{park2024} ground
agents in two-hour interviews with 1{,}052 people and score held-out
survey responses against each participant's own test--retest consistency;
Twin-2K-500 \ecite{twin2k} supplies a survey-based dataset with a repeat
wave for the same purpose. On social media, BluePrint \ecite{blueprint}
clusters anonymized Bluesky users into personas and poses next-action
prediction; BehaviorChain \ecite{behaviorchain}, TwinVoice, and
PersonaArena \ecite{personaarena} test persona simulation with
constructed or judge-scored scenarios. Wu et al.\ \ecite{boundary} review
this literature and find that fewer than half of validation studies
report behavioral variance, which is why we report the per-user
adherence distribution alongside the aggregate. Our benchmark differs
from all of these in scoring individual (not clustered) users on
real held-out behavior from a fully public corpus.

\textbf{Sentiment dynamics and contagion on Twitter.} Whether sentiment
spreads over ties has a long empirical record. Kramer et al.\
\ecite{kramer2014} established causal emotional contagion on Facebook
with very small effect sizes; Ferrara and Yang \ecite{ferrara2015}
measured about a 4\% over-exposure effect on Twitter with a
scarcely-susceptible majority; Charlton et al.\ \ecite{charlton2016}
found that sentiment levels of stable @-mention communities persist over
months, with shifts traceable to external events. Aral et al.\
\ecite{aral2009} and Shalizi and Thomas \ecite{shalizi2011} show that
observational contagion estimates are confounded with homophily, while
Tan et al.\ \ecite{tan2011} show that @-mention neighbors are nonetheless
a useful static prior for user-level sentiment. Our diffusion experiment
(\S\ref{sec:diffusion}) quantifies this trade-off predictively on a public
corpus: DeGroot averaging \ecite{degroot1974} over the real mention graph
versus each user's own history, with the Friedkin--Johnsen anchored
variant \ecite{friedkin1990} as the natural intermediate left to future
work.

\textbf{Relationship structure.} Kwak et al.\ \ecite{kwak2010}
established the large-scale structural view of Twitter; Huberman et al.\
\ecite{huberman2009} showed that the sparse network of reciprocal
@-interactions, not the follower graph, is the network that matters; Cha
et al.\ \ecite{cha2010} showed that mention-based attention concentrates
on celebrities independently of follower count. Horton and Wohl
\ecite{horton1956} introduced the parasocial-interaction construct we
operationalize on mention pairs.

\textbf{Data.} Sentiment140 \ecite{sentiment140} provides 1.6M tweets
from April--June 2009, distantly labeled for sentiment by emoticons. It
remains one of the few large fully-public full-text tweet corpora: since
the 2023 restriction of the X API, tweet-ID ``hydration'' workflows that
most academic Twitter datasets rely on are effectively defunct, making
full-text corpora the practical substrate for new work. To our knowledge
it has been used almost exclusively for classifier benchmarking; we use
its per-user timelines and @-mention graph instead. TweetEval
\ecite{tweeteval} standardizes tweet classification benchmarks and
supplies pretrained classifiers usable as realism scorecards; Golder and
Macy \ecite{golder2011} document the diurnal mood cycle we recover in
Figure~\ref{fig:diurnal}.
```

### \paperurl lines (add to preamble)

```latex
\paperurl{oasis}{https://arxiv.org/abs/2411.11581}
\paperurl{agentsociety}{https://arxiv.org/abs/2502.08691}
\paperurl{ysocial}{https://arxiv.org/abs/2408.00818}
\paperurl{socioverse}{https://arxiv.org/abs/2504.10157}
\paperurl{aps}{https://arxiv.org/abs/2605.27419}
\paperurl{poorman}{https://arxiv.org/abs/2608.11215}
\paperurl{hybriddiffusion}{https://arxiv.org/abs/2510.16366}
\paperurl{toposim}{https://arxiv.org/abs/2604.18011}
\paperurl{scaling}{https://arxiv.org/abs/2607.02464}
\paperurl{park2024}{https://arxiv.org/abs/2411.10109}
\paperurl{twin2k}{https://arxiv.org/abs/2505.17479}
\paperurl{blueprint}{https://arxiv.org/abs/2510.02343}
\paperurl{behaviorchain}{https://arxiv.org/abs/2502.14642}
\paperurl{personaarena}{https://arxiv.org/abs/2605.17044}
\paperurl{boundary}{https://arxiv.org/abs/2506.19806}
\paperurl{kramer2014}{https://doi.org/10.1073/pnas.1320040111}
\paperurl{ferrara2015}{https://arxiv.org/abs/1506.06021}
\paperurl{charlton2016}{https://arxiv.org/abs/1604.03427}
\paperurl{aral2009}{https://doi.org/10.1073/pnas.0908800106}
\paperurl{shalizi2011}{https://arxiv.org/abs/1004.4704}
\paperurl{tan2011}{https://arxiv.org/abs/1109.6018}
\paperurl{friedkin1990}{https://escholarship.org/uc/item/2r82w1vs}
\paperurl{huberman2009}{https://firstmonday.org/ojs/index.php/fm/article/view/2317}
\paperurl{cha2010}{https://ojs.aaai.org/index.php/ICWSM/article/view/14033}
\paperurl{golder2011}{https://doi.org/10.1126/science.1202775}
```

(Friedkin–Johnsen: the eScholarship URL is an author-hosted full text; the
DOI fallback is https://doi.org/10.1080/0022250X.1990.9990069. Kramer and
Aral have no legitimate full-text host besides PNAS; the DOI pages are
open access.)

### \bibitem lines (insert into thebibliography; change `{9}` to `{99}`)

```latex
\bibitem{oasis}
Z.~Yang, Z.~Zhang, Z.~Zheng, Y.~Jiang, Z.~Gan, Z.~Wang, Z.~Ling, J.~Chen,
M.~Ma, B.~Dong, P.~Gupta, S.~Hu, Z.~Yin, G.~Li, X.~Jia, L.~Wang, B.~Ghanem,
H.~Lu, C.~Lu, W.~Ouyang, Y.~Qiao, P.~Torr, J.~Shao.
\newblock \reftitle{oasis}{OASIS: Open Agent Social Interaction Simulations
with One Million Agents}.
\newblock In \emph{Proc.\ ICML}, 2025. arXiv:2411.11581.

\bibitem{agentsociety}
J.~Piao, Y.~Yan, J.~Zhang, N.~Li, J.~Yan, X.~Lan, Z.~Lu, Z.~Zheng, J.~Y. Wang,
D.~Zhou, C.~Gao, F.~Xu, F.~Zhang, K.~Rong, J.~Su, Y.~Li.
\newblock \reftitle{agentsociety}{AgentSociety: Large-Scale Simulation of
LLM-Driven Generative Agents Advances Understanding of Human Behaviors and
Society}.
\newblock \emph{arXiv:2502.08691}, 2025.

\bibitem{ysocial}
G.~Rossetti, M.~Stella, R.~Cazabet, K.~Abramski, E.~Cau, S.~Citraro,
A.~Failla, R.~Improta, V.~Morini, V.~Pansanella.
\newblock \reftitle{ysocial}{Y Social: an LLM-powered Social Media Digital
Twin}.
\newblock \emph{arXiv:2408.00818}, 2024.

\bibitem{socioverse}
X.~Zhang, J.~Lin, X.~Mou, S.~Yang, X.~Liu, L.~Sun, H.~Lyu, Y.~Yang, W.~Qi,
Y.~Chen, G.~Li, L.~Yan, Y.~Hu, S.~Chen, Y.~Wang, X.~Huang, J.~Luo, S.~Tang,
L.~Wu, B.~Zhou, Z.~Wei.
\newblock \reftitle{socioverse}{SocioVerse: A World Model for Social
Simulation Powered by LLM Agents and A Pool of 10 Million Real-World Users}.
\newblock \emph{arXiv:2504.10157}, 2025.

\bibitem{aps}
Q.~Zheng, Y.~Gao, S.~He, H.~Guan, Y.~Tian, J.~Feng, M.~Wang, S.~Zheng,
Z.~Liu.
\newblock \reftitle{aps}{APS: Bias-Controlled Adaptive Prototype Simulation
for Population-Scale LLM Agents}.
\newblock \emph{arXiv:2605.27419}, 2026.

\bibitem{poorman}
I.~Itkin.
\newblock \reftitle{poorman}{Poor Man's Agentic Modeling: Simulating Large
LLM-Agent Societies on a Laptop}.
\newblock \emph{arXiv:2608.11215}, 2026.

\bibitem{hybriddiffusion}
X.~Li, Z.~Guo, Q.~Guo, H.~Jin, W.~Ma, M.~Zhang.
\newblock \reftitle{hybriddiffusion}{Integrating LLM and Diffusion-Based
Agents for Social Simulation}.
\newblock \emph{arXiv:2510.16366}, 2025.

\bibitem{toposim}
Y.~Xu, S.~Zhang, Y.~Zhou, S.~Zeng, L.~V.~S. Lakshmanan, C.~Ma.
\newblock \reftitle{toposim}{Topology-Aware LLM-Driven Social Simulation: A
Unified Framework for Efficient and Realistic Agent Dynamics}.
\newblock \emph{arXiv:2604.18011}, 2026.

\bibitem{scaling}
C.~Ziems, W.~Held, S.~D. Karaca, D.~Grusky, T.~Hashimoto, D.~Yang.
\newblock \reftitle{scaling}{Will Scaling Improve Social Simulation with
LLMs?}
\newblock \emph{arXiv:2607.02464}, 2026.

\bibitem{park2024}
J.~S. Park, C.~Q. Zou, J.~Kamphorst, N.~Egan, A.~Shaw, B.~M. Hill, C.~Cai,
M.~R. Morris, P.~Liang, R.~Willer, M.~S. Bernstein.
\newblock \reftitle{park2024}{LLM Agents Grounded in Self-Reports Enable
General-Purpose Simulation of Individuals}.
\newblock \emph{arXiv:2411.10109}, 2024.

\bibitem{twin2k}
O.~Toubia, G.~Z. Gui, T.~Peng, D.~J. Merlau, A.~Li, H.~Chen.
\newblock \reftitle{twin2k}{Twin-2K-500: A Dataset for Building Digital Twins
of over 2,000 People Based on Their Answers to over 500 Questions}.
\newblock \emph{Marketing Science}, 2025. arXiv:2505.17479.

\bibitem{blueprint}
A.~B\"uck-Kaeffer, J.~Q. Chooi, D.~Zhao, M.~Puelma Touzel, K.~Pelrine,
J.-F. Godbout, R.~Rabbany, Z.~Yang.
\newblock \reftitle{blueprint}{BluePrint: A Social Media User Dataset for
LLM Persona Evaluation and Training}.
\newblock \emph{arXiv:2510.02343}, 2025.

\bibitem{behaviorchain}
R.~Li, H.~Xia, X.~Yuan, Q.~Dong, L.~Sha, W.~Li, Z.~Sui.
\newblock \reftitle{behaviorchain}{How Far are LLMs from Being Our Digital
Twins? A Benchmark for Persona-Based Behavior Chain Simulation}.
\newblock In \emph{Findings of ACL}, 2025. arXiv:2502.14642.

\bibitem{personaarena}
W.~Shi, J.~Lian, M.~Wu, H.~Qin, M.~Zhou, X.~Xie, N.~Chao, H.~Liao.
\newblock \reftitle{personaarena}{PersonaArena: Dynamic Simulation for
Evaluating and Enhancing Persona-Level Role-Playing in Large Language
Models}.
\newblock In \emph{Findings of ACL}, 2026. arXiv:2605.17044.

\bibitem{boundary}
Z.~Wu, R.~Peng, T.~Ito, M.~Onizuka, C.~Xiao.
\newblock \reftitle{boundary}{LLM-Based Social Simulations Require a
Boundary}.
\newblock In \emph{Proc.\ ICML (Position Papers)}, 2026. arXiv:2506.19806.

\bibitem{kramer2014}
A.~D.~I. Kramer, J.~E. Guillory, J.~T. Hancock.
\newblock \reftitle{kramer2014}{Experimental Evidence of Massive-Scale
Emotional Contagion through Social Networks}.
\newblock \emph{PNAS}, 111(24):8788--8790, 2014.

\bibitem{ferrara2015}
E.~Ferrara, Z.~Yang.
\newblock \reftitle{ferrara2015}{Measuring Emotional Contagion in Social
Media}.
\newblock \emph{PLoS ONE}, 10(11):e0142390, 2015.

\bibitem{charlton2016}
N.~Charlton, C.~Singleton, D.~V. Greetham.
\newblock \reftitle{charlton2016}{In the Mood: The Dynamics of Collective
Sentiments on Twitter}.
\newblock \emph{Royal Society Open Science}, 3(6):160162, 2016.

\bibitem{aral2009}
S.~Aral, L.~Muchnik, A.~Sundararajan.
\newblock \reftitle{aral2009}{Distinguishing Influence-Based Contagion from
Homophily-Driven Diffusion in Dynamic Networks}.
\newblock \emph{PNAS}, 106(51):21544--21549, 2009.

\bibitem{shalizi2011}
C.~R. Shalizi, A.~C. Thomas.
\newblock \reftitle{shalizi2011}{Homophily and Contagion Are Generically
Confounded in Observational Social Network Studies}.
\newblock \emph{Sociological Methods \& Research}, 40(2):211--239, 2011.

\bibitem{tan2011}
C.~Tan, L.~Lee, J.~Tang, L.~Jiang, M.~Zhou, P.~Li.
\newblock \reftitle{tan2011}{User-Level Sentiment Analysis Incorporating
Social Networks}.
\newblock In \emph{Proc.\ KDD}, 2011.

\bibitem{friedkin1990}
N.~E. Friedkin, E.~C. Johnsen.
\newblock \reftitle{friedkin1990}{Social Influence and Opinions}.
\newblock \emph{Journal of Mathematical Sociology}, 15(3--4):193--205, 1990.

\bibitem{huberman2009}
B.~A. Huberman, D.~M. Romero, F.~Wu.
\newblock \reftitle{huberman2009}{Social Networks that Matter: Twitter under
the Microscope}.
\newblock \emph{First Monday}, 14(1), 2009.

\bibitem{cha2010}
M.~Cha, H.~Haddadi, F.~Benevenuto, K.~P. Gummadi.
\newblock \reftitle{cha2010}{Measuring User Influence in Twitter: The
Million Follower Fallacy}.
\newblock In \emph{Proc.\ ICWSM}, 2010.

\bibitem{golder2011}
S.~A. Golder, M.~W. Macy.
\newblock \reftitle{golder2011}{Diurnal and Seasonal Mood Vary with Work,
Sleep, and Daylength across Diverse Cultures}.
\newblock \emph{Science}, 333(6051):1878--1881, 2011.
```

Note: all author lists above were read from the arXiv abs/HTML page or
publisher page listed (AgentSociety and Twin-2K-500 re-verified on arXiv).

After editing, run `scripts/test_paper_links.py --update` per CLAUDE.md.

---

## 4. Sentences elsewhere that should be rephrased

**Abstract, "Disposition beats diffusion."** Keep the slogan, but it now
stands in a literature. Suggested: "Disposition beats diffusion, consistent
with the small contagion effects and strong homophily reported in
observational and experimental studies." (Optional; abstracts can stay
terse.)

**Intro, contribution 1: "including a negative result we believe is
informative for simulator design."** Replace with: "including a negative
result that replicates, at the individual level and on a public corpus,
the weak-contagion / strong-disposition pattern found in prior Twitter and
Facebook studies \ecite{ferrara2015,kramer2014,charlton2016}."

**Intro, "Two recent systems define the frontier..."** Add a clause so the
intro does not imply only two systems exist: "Two recent systems define the
frontier of population-scale social simulation, in a line that runs from
generative agents \ecite{park2023} through million-agent open simulators
such as OASIS \ecite{oasis}." (Note `\ecite` takes one key; if citing two,
use two `\ecite` calls — the macro wraps a single `\cite`.)

**§Diffusion, "Neighbor-mixing strictly destroys predictive information at
this horizon."** Keep, but add a sentence after "who a person is outweighs
who they talk to": "This is the predictive face of a well-known
identification problem: in observational network data, apparent contagion
is largely homophily \ecite{aral2009}, and the two are generically
confounded \ecite{shalizi2011}. Our test does not show that influence is
absent, only that averaging over neighbors adds no information beyond a
user's own history at a 24-day horizon, in line with the ${\sim}4\%$
exposure effects Ferrara and Yang \ecite{ferrara2015} measure and the
month-scale stability Charlton et al.\ \ecite{charlton2016} observe on the
mention graph."

**§Diffusion, "which is why persona grounding (\S\ref{sec:personas})
matters."** Add: "Static neighbor information may still help as a prior
\ecite{tan2011}; what fails is dynamic mixing."

**§Ladder, "Light Society's central efficiency device is heterogeneous
agent cost."** Rephrase to: "Heterogeneous agent cost is Light Society's
central efficiency device \ecite{lightsociety} and has since appeared as
core/background splits \ecite{hybriddiffusion}, structural grouping
\ecite{toposim}, prototype routing \ecite{aps}, and whole-agent surrogates
\ecite{poorman}."

**§Ladder, "$702.7\times$ reduction with zero fidelity loss"** — "zero
fidelity loss" is asserted, not measured (Limitations admits nominal
costs). Suggested: "a $702.7\times$ reduction under the nominal cost model,
with the full-LLM tier reserved for the users who carry most of the
observable signal. APS \ecite{aps} reports a measured $381\times$ reduction
at $10^7$ agents with a full-LLM reference; we do not measure fidelity loss
here."

**§Parasocial, "Genuine relationships are rare: 77\% of pairs are one-off
contacts."** Add: "echoing Huberman et al.'s finding that the network of
reciprocal @-interaction is far sparser than the declared graph
\ecite{huberman2009}."

**§Parasocial, celebrity sentence.** After "who tweet but do not talk
back," add "the mention-concentration on celebrities that Cha et al.\
\ecite{cha2010} documented."

**§Benchmark, "currently lacks a public, fixed-protocol instantiation that
anyone can run."** This is too strong given BluePrint/SIMPACT and
Park 2024. Replace with: "currently lacks a public, fixed-protocol
instantiation on real held-out behavior of individual users: Park et al.\
\ecite{park2024} and Twin-2K-500 \ecite{twin2k} score held-out survey
items, and BluePrint \ecite{blueprint} scores next actions for anonymized
persona clusters rather than individuals. We contribute one on an existing
fully-public corpus."

**§Benchmark, per-user distribution sentence.** Add: "Reporting the
distribution, not only the mean, follows Wu et al.'s \ecite{boundary}
recommendation that simulation evaluations report behavioral variance."

**§Limitations, "richer contagion models could yet beat persistence."**
Specify: "richer contagion models, most naturally Friedkin--Johnsen
\ecite{friedkin1990}, which anchors each agent to its initial state and
interpolates between persistence and DeGroot, could yet beat persistence;
and because homophily and influence are not separable in observational
data \ecite{shalizi2011}, our result concerns prediction, not causation."

**§Limitations / Conclusion, "The methodology of billion-agent social
simulators is not confined to billion-agent budgets."** Add a clause:
"a point made independently by Itkin \ecite{poorman} for LLM-cloned
surrogates; our contribution is to do it with real people, a real graph,
and real held-out behavior."

**§Dataset, diurnal sentence.** Append "\ecite{golder2011}" after "usable
for calibrating agent posting schedules" (Golder and Macy's diurnal mood
cycle).
