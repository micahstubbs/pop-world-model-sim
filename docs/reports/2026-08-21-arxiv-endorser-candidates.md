# arXiv Endorser Candidates for the popsim Paper

**Generated:** 2026-08-21
**Target category:** cs.MA (Multiagent Systems), cross-list cs.SI / cs.AI
**Why this matters:** since 2026-01-21 arXiv no longer auto-endorses on an institutional email. Neither popsim author has one anyway, so the paper needs a personal endorsement from an author with arXiv papers in the CS endorsement domain submitted between ~May 2021 and ~May 2026. Endorsement requests succeed on warm connections with a readable draft attached; they fail cold.

## Method

Three sources were mined and every plausible name was cross-referenced against the arXiv API (`scripts/arxiv_endorser_scan.py`, exact first+last author match, papers in the 3-month-to-5-year eligibility window, category mix reported):

1. **Google Takeout contacts** (`scripts/edu_contacts.py`): 390 `.edu`/`.ac.*` emails across 170 domains, plus 23 at AI-lab/top-university domains. Mostly OU/OSU/ORU/JBU alumni rosters; 46 research-plausible names were scanned.
2. **Gmail / Calendar / Drive / session transcripts / julius-world CRM**: searched for "autoresearch", "Steven", Stanford/OpenAI, `.edu` correspondents, reading groups. `.edu` mail is all newsletters (Knight Center, Stanford Math Circle, OU MarComm); sent mail is family/school/vendors. **"Steven from the autoresearch group" was not found in any of these** — the only autoresearch traces are the Karpathy fork at `~/wk/autoresearch`, the defunct `knoxus-ai/AutoResearch` repo (Unreasonable Labs), and the May 30 "Autoresearch Systems Hackathon with Modal, OpenAI, Raindrop & Antler" listing in a Bond AI SF digest. The group chat is presumably on Luma/WhatsApp/Discord. *Action for Micah: supply Steven's surname and I will run the arXiv check in one call.*
3. **X followers of @micahstubbs** (Apify `kaitoeasyapi/premium-x-follower-scraper-following-data`, 4,464 followers, $0.63): `scripts/x_followers_academic.py` scored bios for academic signals → 1,384 flagged, 229 with score ≥4 were scanned against arXiv → **87 have CS-eligible papers** (`docs/data/x-academic-arxiv-scan.out` plus `x-academic-arxiv-scan-retry.out` for the 63 names arXiv rate-limited on the first pass).

Raw data: `docs/data/x-followers-micahstubbs-2026-08-21.json`, `docs/data/x-followers-academic-2026-08-21.tsv`, `docs/data/x-academic-arxiv-scan.out`, probe at `docs/scrape-probe-2026-08-21-apify-x-followers.json`.

**Ground truth caveat.** The arXiv API scan is a proxy. The authoritative check is the "Which authors of this paper are endorsers?" link on any candidate's abstract page (`arxiv.org/auth/show-endorsers/<id>`), which requires an arXiv login — Micah should click it for the top two or three before emailing.

## Tier 1 — topical fit with popsim (social simulation / agents) and eligible

These people would *understand and appreciate* a reproduction of billion-agent social simulators, and they follow Micah on X.

| Candidate | Affiliation | Eligible CS papers (sample) | Why them |
|---|---|---|---|
| **Deepak Nathani** (@deepaknathani11) | ML researcher (agents) | 2604.00842 (**cs.AI/LG/cs.MA** "Proactive Agent Research Environment: Simulating Active Users to Evaluate…"), 2603.17863 (cs.LG/AI); 10 eligible | The only follower with a recent **cs.MA** paper, and it is about simulating users to evaluate agents — the closest thing to popsim in the whole set. |
| **Dhiraj Murthy** (@dhirajmurthy) | Professor, Journalism/Media & Sociology, UT Austin; author of *Twitter: Social Communication in the Twitter Age* | 2505.20584 (cs.SI/CY/HC, mpox discourse dashboard), 2408.06900 (cs.CY/AI, social-bot detection) | Computational social scientist working on exactly the social-media dynamics popsim simulates; cs.SI author. Strongest topical match. |
| **David Sumpter** (@Soccermatics) | Professor of Applied Mathematics, Uppsala; *Collective Animal Behavior*, *Outnumbered* | 2603.12741 (cs.CY/HC), 2504.00767 (cs.LG/CL/HC); 11 eligible incl. cs.SI | Collective behaviour and social-contagion modelling is his field; writes for a popular audience so will read a reproduction paper charitably. |
| **Daniel Angus** (@antmandan) | Professor of Digital Communication, QUT Digital Media Research Centre | 2511.15732 (cs.CY/AI, conspiratorial ideation), 2509.18874 (cs.HC/AI/CR) | Computational social science / platform studies; 3 eligible CS papers. |
| **Zijie Jay Wang** (@Jay4w) | Safety researcher, OpenAI; ML PhD Georgia Tech | 2605.24578 (cs.CV "World Models as Group Actions"), 2604.19921 (cs.CL); 40 eligible | Human-AI interaction + world models; built WizMap/Diffusion Explainer — a vis person who will get the popsim visualizations. Possibly the "Steven at OpenAI" confusion is not him, but he is the OpenAI follower with the most eligible papers. |
| **Kai Arulkumaran** (@kaixhin) | Sakana AI; ex-Imperial, DeepMind, FAIR | 2605.23908 (cs.AI/CL/CV, "Replicating Picbreeder" — a *reproduction* paper), 2507.13602 | Open-endedness / agents; literally just published a replication study, so he values the genre. |
| **Leonardo F. Nascimento** (@leofn3) | UFBA, computational social scientist (misinformation, hate speech) | 2604.16337 (cs.IR/AI/CY, multi-LLM-agent Q&A) | Multi-agent LLM systems applied to social questions. 1 eligible paper — confirm on the endorsers link. |
| **Frank Schlosser** (@franksh_) | Spotify; ex-Brockmann lab (complex systems, RKI) | 2304.12087 (physics.soc-ph/q-bio), 2112.12521 (physics.soc-ph/cs.CY, mobility biases in epidemic models) | Complex-systems modelling of populations; cs.CY cross-list. Closer to physics.soc-ph domain — good if the paper cross-lists there. |

## Tier 2 — strong eligible endorsers who know Micah's work (vis / HCI / ML community)

Warm relationships from the data-vis world; all have many eligible cs.* papers. They may not be cs.MA specialists, but arXiv endorsement is by domain, and all are active cs.HC/cs.AI/cs.LG authors.

| Candidate | Affiliation | Eligible CS papers | Notes |
|---|---|---|---|
| **Jeffrey Heer** (@jeffrey_heer) | Professor, UW CSE; Vega/D3 lineage | 25 (cs.HC/AI/CL/DB) | Micah's D3/Vega community; the most natural "knows you personally" endorser. |
| **Jessica Hullman** (@JessicaHullman) | Professor, Northwestern CS; vis + statistical reasoning | 37 (cs.HC/LG/stat) | Vis community; writes about uncertainty and simulation-based reasoning — will read the evaluation sections critically but fairly. |
| **Miles Brundage** (@Miles_Brundage) | Independent AI policy researcher; ex-OpenAI | 13 (cs.CY) | Societal-impact framing of agent simulations; cs.CY domain. |
| **Bum Chul Kwon** (@BCKwon) | IBM Research, vis/ML | 17 (cs.LG/AI/HC) | Vis community. |
| **Meredith Martin** (@mmvty) | Princeton, computational humanities | 3 (cs.AI/CY/HC) | Cultural-technology framing of generative AI. |
| **Bharath Ramsundar** (@rbhar90) | DeepChem | 21 (cs.LG) | Open-science ML; values reproductions. |
| **Ian McKenzie** (@McKenzieIA) | FAR AI | 3 (cs.CL/AI/LG) | |
| **Dominik Moritz** (@domoritz) | Prof CMU HCII; Apple | 39 (cs.HC/AI/LG/DB) | Vega-Lite co-creator; ML-adjacent (interpretability) so reads agent papers. |
| **Hanspeter Pfister** (@hpfister) | Harvard professor, vis/graphics/CV | 46 | Very active; large lab. |
| **Elena Glassman** (@roboticwrestler) | Asst Prof CS, Harvard | 30 (cs.HC/AI/CY) | Human-AI interaction; cs.AI author. |
| **Fred Hohman** (@fredhohman) | Apple HCI+ML research scientist | 19 (cs.HC/AI/CL/LG) | Georgia Tech Polo Club alum; interpretability + vis. |
| **Bongshin Lee** (@bongshin) | Professor, Yonsei; ex-MSR | 19 (cs.HC/GR/CV) | Vis community. |
| **Carolina Nobre** (@carolinanobre84) | U Toronto, vis | 16 (cs.HC/AI/CY) | |
| **Yisong Yue** (@yisongyue) | Caltech AI professor | 42 (cs.AI/LG/CL/GT) | Big ML lab; cs.GT/MA-adjacent. Less personal. |
| **Ari Morcos** (@arimorcos) | CEO DatologyAI; ex-FAIR/DeepMind | 24 (cs.LG/AI/CL) | |
| **Anna Huang** (@huangcza) | MIT faculty; DeepMind Magenta | 18 | |
| **Douglas Eck** (@douglas_eck) | Google DeepMind lead | 6 (incl. Gemini 2.5 report) | Senior; likely too busy for cold asks. |
| **Tom Le Paine** (@TomLePaine) | Google DeepMind | 7 (Gemini 2.5, Imagen 3) | |
| **Jeremy Howard** (@jeremyphoward) | fast.ai / Answer.AI | 1 (2412.13663 ModernBERT, cs.CL/AI) | Eligible on one paper; huge reach; values reproductions. |
| **Paige Bailey** (contacts: paige.bailey@alumni.rice.edu) | Google DeepMind (Gemma/Gemini/PaLM 2) | 5 (cs.CL/AI/LG, incl. A2Perf agents benchmark 2503.03056) | From Micah's contacts, not X. Knows agent benchmarks. |
| **Anmol Agrawal** (contacts: anmolagrawal@utexas.edu) | UT Austin | 2 (cs.CL/HC, cs.IR/AI legal RAG 2602.23371) | Legal-AI overlap with CaseMirror; junior — may not yet have endorser status; check the link. |
| **Flood Sung** (@RotekSong) | Moonshot AI (Kimi) | 13 (cs.AI/CL/SE, agentic) | Agents; industry. |
| **Kevin Robinson** (@krob), **Diego Garcia-Olano** (@dgolano), **Christopher Nguyen** (@pentagoniac), **Simon Colton**, **Justin Matejka**, **Paul Parsons**, **Panagiotis Ritsos**, **Romain Vuillemot**, **Bernease Herman**, **Georgina Cosma**, **David van Dijk**, **Chris Choy**, **Sumeet Singh**, **Federico Pernici**, **Erfan Miahi** | various | 4–22 each | Eligible; weaker topical or relationship fit. Full list with paper ids in `docs/data/x-academic-arxiv-scan.out`. |

## Probable homonyms (ignore unless bio confirms)

James Bailey (43), John Thompson (20), Alexander Chen (14), Weihao Yu (35), Jonathan N. Katz (cs.CR hits are a different Katz), Steve Smith, Dan Zhang / Wei Wong / Caleb Chen from contacts. Common names pull other people's papers; the bios for these followers don't match the paper affiliations.

## Contacts-only results (no X overlap)

Of 46 scanned contact names, real eligible hits: Paige Bailey, Anmol Agrawal, Dan Robinson (Paradigm; cs.GT auction papers 2410.19106, 2403.03367), David Greenberg (cs.LG simulation-based inference; verify it is the UCL contact and not the Hereon researcher), Matthew Wettergreen (Rice; 2301.04030 cs.SI conversational turn-taking on networks — topically close, but one paper), Nathan Brooks (CMU photonics; the cs.MA 2022 hit is likely a different Nathan Brooks).

## Recommendation — who to ask, in order

1. **Deepak Nathani** — the one cs.MA author, working on simulated users for agent evaluation; the paper is squarely in his lane.
2. **Dhiraj Murthy** — cs.SI, social-media dynamics, UT Austin. Send the draft with a note on the Twitter-corpus / relationship-strength parts of popsim.
3. **Jeffrey Heer**, **Dominik Moritz**, or **Jessica Hullman** — the warmest personal connections with unambiguous endorser status in CS; either will endorse on a quick read if the vis figures are good.
4. **David Sumpter** — collective-behaviour modelling; likely enthusiastic about a reproduction paper.
5. Backups: Zijie Jay Wang (OpenAI), Kai Arulkumaran (just wrote a replication paper), Daniel Angus.
6. **Steven (autoresearch group)** — still the user's own top pick; unresolved only because the surname is unknown. Provide it and the check takes one API call.

Ask one or two at a time, attach the PDF and the six-character endorsement code, and do not re-ping. Before emailing, open one of their abstract pages while logged in and confirm the "endorsers" link lists them for the cs domain.

## Costs and artifacts

- Apify: probe $0.02 + full run $0.63.
- arXiv API: 229 + 46 queries at 3 s spacing, no cost.
- Scripts (also installed at `~/.claude/scripts/find-arxiv-endorsers/`, skill `/fae`): `scripts/edu_contacts.py`, `scripts/x_followers_academic.py`, `scripts/arxiv_endorser_scan.py`.
