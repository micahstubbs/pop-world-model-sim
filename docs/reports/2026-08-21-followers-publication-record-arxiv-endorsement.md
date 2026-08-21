# The @micahstubbs Follower Graph and Its Publication Record: A Survey for arXiv Endorsement

**Prepared by:** CaseMirror Research
**Date:** 2026-08-21
**Subject:** Who among Micah Stubbs's X followers, email contacts, and address book publishes on arXiv, which of them are eligible to endorse a first-time cs.MA submission in August 2026, and who is the best person to ask for the popsim paper.

## Executive Summary

arXiv stopped auto-endorsing on institutional email on 2026-01-21. A first-time submitter without a co-authored arXiv paper now needs a personal endorsement from an author with papers in the same endorsement domain submitted between three months and five years ago. Neither author of *popsim: Reproducing Elements of Billion-Agent Social Simulators* (Micah Stubbs, CaseMirror Research; Yvonne Chen) qualifies for the automatic path, so this report answers one question: who in Micah's own network can endorse, and who among them would actually understand and appreciate the paper?

Three sources were surveyed and every plausible name was cross-referenced against the arXiv API. The X follower graph dominated. Of **4,464 followers of @micahstubbs**, 1,383 (31%) carry academic or research-lab signals in their bio, and of the 229 highest-scoring, **96 have arXiv papers in the eligibility window and 89 have them in computer science**, together accounting for 858 eligible CS papers. The follower base is, in short, an unusually research-dense audience: a data-visualization and machine-learning community anchored in San Francisco, London, New York and Seattle, with Google, MIT, Meta, Apple, Microsoft, Harvard, Stanford and OpenAI the most-cited affiliations.

The contacts export (390 `.edu` addresses) and Gmail contributed little: the `.edu` mail is newsletters and the address book is alumni rosters. Three real hits surfaced there — Paige Bailey (Google DeepMind), Anmol Agrawal (UT Austin) and Dan Robinson (Paradigm). The person Micah named first, "Steven from the autoresearch group, recently moved from Stanford to OpenAI," does not appear in any searchable source; the group evidently lives on Luma or WhatsApp. His surname is the one missing input.

**Recommendation.** Ask, in order: **Deepak Nathani** (the only follower with a 2026 cs.MA paper, on simulating users to evaluate agents), **Dhiraj Murthy** (UT Austin, cs.SI social-media discourse), then one of **Jeffrey Heer, Dominik Moritz, or Jessica Hullman** (warm vis-community ties, 25–39 eligible papers each), with **David Sumpter**, **Zijie Jay Wang** (OpenAI) and **Kai Arulkumaran** as backups. Ask one or two at a time with the draft PDF attached; verify endorser status on the abstract-page link (login required) before writing.

## The Follower Graph

**Size and shape.** 4,464 accounts follow @micahstubbs (pulled 2026-08-21 via the Apify `kaitoeasyapi` follower scraper, $0.63, after a 200-account smoke test). 3,691 have a bio, 3,309 a location, 2,521 a URL. The median follower has 466 followers of their own; 313 have more than 10,000. Account ages skew old — 1,772 were created 2007–2010 and only 243 since 2020 — consistent with a following built during the D3/data-vis era rather than bought or recent.

**Geography** (substring match on the location field): San Francisco 255, London 113, New York 109, Seattle 67, Los Angeles 57, India 52, Bay Area 45, Paris 45, Germany 44, Berlin 43, Austin 38, Washington 34, Toronto 31, Boston 31, Chicago 26.

**Academic density.** `scripts/x_followers_academic.py` scores each bio, location and URL for affiliation signals (professor/postdoc/PhD, research scientist, `.edu`/`.ac.*`, named labs, named universities, venue names). 1,383 accounts score ≥2; the distribution is long-tailed: 924 at score 2, 195 at 3, 83 at 4, 64 at 5, 38 at 6, 29 at 7, 23 at 8, 16 at 9, and 11 at 10–14. The top of the distribution is unambiguous: Sanja Fidler (NVIDIA VP / U Toronto), Elena Glassman (Harvard), Bongshin Lee (Yonsei), Jeffrey Heer (UW), Hanspeter Pfister (Harvard), Vasia Kalavri (BU), Yisong Yue (Caltech), Douglas Eck (DeepMind), Anna Huang (MIT), Dominik Moritz (CMU).

**Affiliations named in flagged bios:** Google 26, MIT 16, Meta 12, Apple 11, Microsoft 11, Harvard 10, Stanford 10, OpenAI 7, UW 6, NVIDIA 5, Caltech 4, Amazon 4, Northeastern 4, DeepMind 4, Toronto 4, Yale 3, Columbia 3.

## Publication Record

The 229 followers scoring ≥4 were queried against the arXiv API (`scripts/arxiv_endorser_scan.py`; `au:"Last, First"` with an exact first+last author match on each result; window 2021-08 to 2026-05). arXiv rate-limited the first pass at 3-second spacing (63 HTTP 429s), so those names were re-run at 6-second spacing with zero errors.

| Metric | Value |
|---|---|
| Followers scanned | 229 |
| With ≥1 eligible arXiv paper (any category) | 96 (42%) |
| With ≥1 eligible paper in cs.* | 89 (39%) |
| Eligible papers, all categories (sum over authors, capped at 50/author) | 989 |
| Eligible papers in cs.* | 858 |
| Median eligible papers among CS authors | 7 |

**Category mix of the sampled eligible papers:** cs.AI 120, cs.LG 97, cs.HC 93, cs.CL 81, cs.CV 55, cs.CY 32, cs.SD 15, stat.ML 12, cs.RO 11, cs.CR 10, cs.IR 7, cs.SI 6, cs.SE 5, physics.soc-ph 5. The concentration in cs.HC reflects the visualization community; cs.AI/cs.LG/cs.CL reflect the ML-lab followers. cs.MA appears exactly once (Deepak Nathani), which is why he leads the recommendation.

**Most prolific eligible authors among followers** (eligible CS papers in window): Hanspeter Pfister 46, Yisong Yue 42, Zijie Jay Wang 40, Dominik Moritz 39, Jessica Hullman 37, Elena Glassman 30, Jeffrey Heer 25, Ari Morcos 24, Georgina Cosma 22, Bharath Ramsundar 21, Sumeet Singh 21, Bongshin Lee 19, Fred Hohman 19, Anna Huang 18, Bum Chul Kwon 17, Carolina Nobre 16. (James Bailey 43, Weihao Yu 35, John Thompson 20 and Alexander Chen 14 are excluded as probable homonyms: common names whose arXiv output does not match the follower's bio.)

**Homonym control.** The arXiv author search is fuzzy; the scanner requires both first and last name tokens to appear in an author string, but cannot distinguish two people with the same name. Twenty-two names in the appendix are flagged `(homonym?)` where the paper subject matter does not match the bio (e.g. a pathologist credited with MoE-inference papers). Treat flagged rows as unverified.

## Contacts and Email

**Google Takeout contacts.** `scripts/edu_contacts.py` found 390 `.edu`/`.ac.*` addresses across 170 domains and 23 at AI-lab or top-university domains. The bulk are University of Oklahoma (52), Oklahoma State (48), ORU (18), JBU (12) and Arkansas (9) alumni — personal history, not research contacts. Forty-six research-plausible names were scanned; real eligible hits were **Paige Bailey** (Google DeepMind; Gemini, Gemma, PaLM 2, A2Perf agents benchmark — 5 cs papers), **Anmol Agrawal** (UT Austin; legal RAG and physics-solution agents — 2 cs papers), **Dan Robinson** (Paradigm; auction-managed AMMs, cs.GT — 4 papers), **David Greenberg** (cs.LG simulation-based inference, 8 papers; affiliation match to the UCL contact unconfirmed) and **Matthew Wettergreen** (Rice; one cs.SI paper on conversational turn-taking on networks). Nathan Brooks (CMU) publishes in photonics; the 2022 cs.MA hit under his name is a different person.

**Gmail, Calendar, Drive, transcripts, CRM.** Searches for "autoresearch", "Steven", Stanford/OpenAI, `.edu` correspondents, reading groups and the knoxus-ai/Unreasonable Labs colleagues returned no endorsement-relevant people. `.edu` mail is the Knight Center, Stanford Math Circle, OU MarComm and the Exploratorium; sent mail over 18 months is family, school, TRM Labs, Y Combinator and vendors. The only "autoresearch" artifacts are the Karpathy fork in `~/wk/autoresearch`, the defunct `knoxus-ai/AutoResearch` repository, and a Bond AI SF listing for the 30 May "Autoresearch Systems Hackathon with Modal, OpenAI, Raindrop & Antler". **Steven** is therefore unresolved; with a surname the arXiv check is a single query.

## Endorser Shortlist

### Tier 1 — topical fit with popsim

| Candidate | Affiliation | Evidence | Why them |
|---|---|---|---|
| **Deepak Nathani** @deepaknathani11 | PhD student, UCSB NLP; ex-Meta AI, AWS, Google AI | 2604.00842 cs.AI/LG/**cs.MA** "Proactive Agent Research Environment: Simulating Active Users to Evaluate…"; 10 eligible | The one cs.MA author in the set, working on simulated users for agent evaluation. |
| **Dhiraj Murthy** @dhirajmurthy | Professor, UT Austin (Journalism/Media, Sociology) | 2505.20584 cs.SI/CY/HC; 2408.06900 cs.CY/AI social-bot detection; 8 eligible | Computational social scientist on social-media dynamics; author of *Twitter*. |
| **David Sumpter** @Soccermatics | Professor of Applied Mathematics, Uppsala | 2603.12741 cs.CY/HC; 2504.00767 cs.LG; 11 eligible incl. cs.SI | Collective behaviour and contagion modelling. |
| **Daniel Angus** @antmandan | Professor of Digital Communication, QUT | 2511.15732 cs.CY/AI; 2509.18874 cs.HC/AI; 3 eligible | Computational social science, platform studies. |
| **Zijie Jay Wang** @Jay4w | Safety researcher, OpenAI; PhD Georgia Tech | 2605.24578 cs.CV "World Models as Group Actions"; 40 eligible | Human-AI interaction and vis (WizMap, Diffusion Explainer). |
| **Kai Arulkumaran** @kaixhin | Sakana AI | 2605.23908 cs.AI "Replicating Picbreeder"; 9 eligible | Just published a replication study; open-endedness and agents. |
| **Leonardo F. Nascimento** @leofn3 | UFBA, computational social science | 2604.16337 cs.IR/AI/CY multi-LLM-agent Q&A; 1 eligible | Multi-agent LLMs on social questions; confirm endorser status. |
| **Frank Schlosser** @franksh_ | Spotify; ex-Brockmann lab | 2112.12521 physics.soc-ph/cs.CY mobility-bias epidemic modelling | Population complex systems; better for a physics.soc-ph cross-list. |
| **Miles Brundage** @Miles_Brundage | AI policy, ex-OpenAI | 2601.11699, 2507.15916 cs.CY; 13 eligible | Societal framing of agent systems. |

### Tier 2 — warm vis/HCI/ML ties with unambiguous eligibility

Jeffrey Heer (UW, 25), Dominik Moritz (CMU/Apple, 39), Jessica Hullman (Northwestern, 37), Hanspeter Pfister (Harvard, 46), Elena Glassman (Harvard, 30), Fred Hohman (Apple, 19), Bongshin Lee (Yonsei, 19), Bum Chul Kwon (IBM, 17), Carolina Nobre (Toronto, 16), Yisong Yue (Caltech, 42), Ari Morcos (Datology, 24), Anna Huang (MIT, 18), Douglas Eck (DeepMind, 6), Tom Le Paine (DeepMind, 7), Jeremy Howard (Answer.AI, 1), Flood Sung (Moonshot, 13), Bharath Ramsundar (DeepChem, 21), Paige Bailey (DeepMind, 5, from contacts), Anmol Agrawal (UT Austin, 2, from contacts).

### Recommendation

1. **Deepak Nathani** — lead with the agent-evaluation angle.
2. **Dhiraj Murthy** — lead with the Twitter-corpus and relationship-strength results.
3. **Heer / Moritz / Hullman** — warmest personal ties; lead with the figures.
4. **David Sumpter** — collective-behaviour framing.
5. Backups: Zijie Jay Wang, Kai Arulkumaran, Daniel Angus.
6. **Steven (autoresearch group)** once a surname is supplied.

Protocol: generate the six-character code by starting the cs.MA submission; email one or two people with the PDF and the code; do not mass-mail or re-ping (arXiv's stated etiquette); confirm on `arxiv.org/auth/show-endorsers/<paper-id>` (login required) that the person is listed as an endorser for the cs domain.

## Method and Reproducibility

- Follower pull: Apify actor `kaitoeasyapi/premium-x-follower-scraper-following-data`. Input quirk: `maxFollowers` and `maxFollowings` must both be ≥200 even with `getFollowing:false`. Smoke test saved to `docs/scrape-probe-2026-08-21-apify-x-followers.json`; full run 62 s, $0.63; raw JSON (22 MB) kept locally at `docs/data/x-followers-micahstubbs-2026-08-21.json` and deliberately not committed (third-party data).
- Scoring: `scripts/x_followers_academic.py` → `docs/data/x-followers-academic-2026-08-21.tsv`.
- arXiv scan: `scripts/arxiv_endorser_scan.py` → `docs/data/x-academic-arxiv-scan.out` and `-retry.out`. 275 names total (229 followers + 46 contacts); 6-second spacing is required above ~150 queries.
- Contacts: `scripts/edu_contacts.py` over the Google Takeout vCards.
- The whole workflow is packaged as the `/fae` (`find-arxiv-endorsers`) skill with scripts in `~/.claude/scripts/find-arxiv-endorsers/`.
- Companion report on the submission process itself: `docs/reports/2026-08-21-104626-arxiv-submission-first-time-industry-author.md`.

## Appendix: All Followers With Eligible cs.* Papers

Sorted by eligible CS paper count. "Eligible" = submitted 2021-08 to 2026-05; capped at 50 per author by the API query. Rows marked `(homonym?)` have papers whose subject does not match the follower's bio.

1. **Hanspeter Pfister** (@hpfister) — 46 CS / 46 total eligible; cs.CV, cs.HC, cs.AI. Harvard Professor in Computer Science focusing on research i. e.g. arXiv:2605.23672.
2. **James Bailey** (homonym?) (@jbailey) — 43 CS / 44 total eligible; cs.AI, cs.LG, cs.CV. Professor @ProvidenceCol, Health Economist, two-bit hedge wi. e.g. arXiv:2605.15618.
3. **Yisong Yue** (@yisongyue) — 42 CS / 43 total eligible; cs.AI, cs.CL, cs.LG. AI Professor @Caltech (@YueLabCaltech). e.g. arXiv:2605.03101.
4. **Zijie Jay Wang** (@Jay4w) — 40 CS / 43 total eligible; cs.CV, cs.CL, cs.CR. Safety researcher @OpenAI 🤖 / ML PhD @GeorgiaTe 🐝 / Research. e.g. arXiv:2605.24578.
5. **Dominik Moritz** (@domoritz) — 39 CS / 40 total eligible; cs.AI, cs.HC, cs.CL. Prof @cmuhcii @cmudig, researcher @apple. Interactive vis to. e.g. arXiv:2605.05329.
6. **Jessica Hullman** (@JessicaHullman) — 37 CS / 39 total eligible; cs.AI, cs.HC, cs.LG. Ginni Rometty Prof @NorthwesternCS / Fellow @IPRatNU  AI / u. e.g. arXiv:2604.08421.
7. **Weihao Yu** (homonym?) (@yuwh) — 35 CS / 35 total eligible; cs.CV, cs.CL, cs.RO. Assistant Professor at Shenzhen Graduate School, Peking Univ. e.g. arXiv:2604.23775.
8. **Elena Glassman** (@roboticwrestler) — 30 CS / 30 total eligible; cs.HC, cs.AI, cs.CY. Human. Asst Professor of CS at Harvard University @HSEAS. @R. e.g. arXiv:2604.04307.
9. **Jeffrey Heer** (@jeffrey_heer) — 25 CS / 25 total eligible; cs.HC, cs.AI, cs.CL. UW Computer Science Professor. Data, visualization & interac. e.g. arXiv:2603.07446.
10. **Ari Morcos** (@arimorcos) — 24 CS / 24 total eligible; cs.LG, cs.CL, cs.AI. CEO and Co-founder @datologyai working to make it easy for a. e.g. arXiv:2605.11405.
11. **Georgina Cosma** (@gcosma1) — 22 CS / 23 total eligible; cs.LG, cs.AI, cs.IR. Professor of AI @lborouniversity  Neural Information Process. e.g. arXiv:2601.19017.
12. **Sumeet S Singh** (@unterix) — 21 CS / 22 total eligible; cs.RO, cs.AI, cs.LG. AI / ML Research. Tech Founder. IISc alum. Tweets are person. e.g. arXiv:2603.10282.
13. **Bharath Ramsundar** (@rbhar90) — 21 CS / 24 total eligible; cs.LG, cs.AI, cs.CL. Founder and CEO @deepforestsci. Creator of @deep chem. Autho. e.g. arXiv:2602.18060.
14. **John Thompson** (homonym?) (@jr_thomp) — 20 CS / 29 total eligible; cs.LG, cs.HC, cs.AI. Sr. Research Scientist @autodesk / data visualization, autho. e.g. arXiv:2604.07316.
15. **Bongshin Lee** (@bongshin) — 19 CS / 19 total eligible; cs.HC, cs.GR, cs.CV. Professor at Yonsei University. @ieeeVGTC Chair. Formerly  S. e.g. arXiv:2606.06498.
16. **Fred Hohman** (@fredhohman) — 19 CS / 19 total eligible; cs.LG, cs.HC, cs.AI. HCI+ML research scientist @Apple, PhD @polodataclub, fellow. e.g. arXiv:2605.05329.
17. **Anna Huang** (@huangcza) — 18 CS / 18 total eligible; cs.SD, cs.LG, cs.AI. Faculty @MIT, Research Sc. Magenta @GoogleDeepMind, Canada C. e.g. arXiv:2605.22717.
18. **Bum Chul Kwon** (@BCKwon) — 17 CS / 17 total eligible; cs.LG, cs.HC, cs.AI. Researcher @IBMResearch. Data Visualization, Visual Analytic. e.g. arXiv:2511.02769.
19. **Carolina Nobre** (@carolinanobre84) — 16 CS / 16 total eligible; cs.HC, cs.AI, cs.CY. Assistant Professor @ University of Toronto. Understanding h. e.g. arXiv:2601.15445.
20. **Alexander Chen** (homonym?) (@alexanderchen) — 14 CS / 42 total eligible; cs.AI, cs.DC, cs.NE. Creative Director at Google Creative Lab. Opinions are my ow. e.g. arXiv:2605.07255.
21. **David van Dijk** (@david_van_dijk) — 13 CS / 13 total eligible; cs.LG, cs.AI, cs.CE. Yale Professor / Founder & CEO @CellTypeInc (YC W26) / AI +. e.g. arXiv:2603.17353.
22. **Simon Colton** (@SimonGColton) — 13 CS / 13 total eligible; cs.SD, cs.AI, cs.LG. Generative artist & AI professor at QMUL and Monash unis. #G. e.g. arXiv:2605.13431.
23. **Flood Sung** (@RotekSong) — 13 CS / 13 total eligible; cs.CL, cs.AI, cs.LG. XVI Robotics Founder & CEO / ex-RL lead at Moonshot / ex-res. e.g. arXiv:2602.02276.
24. **Miles Brundage** (@Miles_Brundage) — 13 CS / 13 total eligible; cs.CY, cs.AI, cs.LG. AI policy researcher, @lfschiavo wife guy, fan of animals an. e.g. arXiv:2601.11699.
25. **Paul Parsons** (@drpaulparsons) — 12 CS / 12 total eligible; cs.HC. associate professor @lifeatpurdue  /  program lead for UX De. e.g. arXiv:2602.02397.
26. **Kevin Robinson** (@krob) — 12 CS / 12 total eligible; cs.CL, cs.AI, cs.CV. 💻❤️ #CSforALL i work at Google Research. e.g. arXiv:2603.20217.
27. **Zhijian Li** (homonym?) (@ZhijianLi3) — 12 CS / 15 total eligible; cs.AI, cs.RO, cs.LG. Postdoc @broadinstitute with @lucapinello working on single-. e.g. arXiv:2605.06483.
28. **Diego Garcia-Olano** (@dgolano) — 10 CS / 10 total eligible; cs.CL, cs.AI, cs.CY. Research Scientist - interpretability/alignment @MetaAI MSL/. e.g. arXiv:2602.24176.
29. **Christopher Nguyen** (@pentagoniac) — 10 CS / 11 total eligible; cs.AI, cs.CL, cs.LG. CEO @Aitomatic—Builder, Leader, Professor, Advisor—Panasonic. e.g. arXiv:2510.07423.
30. **Deepak Nathani** (@deepaknathani11) — 10 CS / 10 total eligible; cs.AI, cs.LG, cs.CL. PhD Student @UCSBNLP / Prev: @AIatMeta / @AWS AI / @GoogleAI. e.g. arXiv:2604.00842.
31. **Kai Arulkumaran** (@kaixhin) — 9 CS / 9 total eligible; cs.HC, cs.LG, cs.NE. Researcher, programmer, DJ, transhumanist. Now at @SakanaAIL. e.g. arXiv:2605.23908.
32. **Justin Matejka** (@JustinMatejka) — 9 CS / 9 total eligible; cs.HC, cs.AI, cs.CL. Sr. Principal Research Scientist (Visualization and HCI) at. e.g. arXiv:2604.13621.
33. **Federico Pernici** (@FedPernici) — 9 CS / 9 total eligible; cs.CV, cs.LG. Computer Vision, Machine Learning, Deep Learning, AI. Associ. e.g. arXiv:2511.08322.
34. **dhiraj murthy** (@dhirajmurthy) — 8 CS / 8 total eligible; cs.SI, cs.CY, cs.HC. Author of Twitter:Social Communication in the Twitter Age ht. e.g. arXiv:2505.20584.
35. **Hua Guo** (homonym?) (@Tacitia) — 8 CS / 28 total eligible; cs.SE, cs.CV. . e.g. arXiv:2512.03753.
36. **Jonathan N. Katz** (homonym?) (@Jonathan_N_Katz) — 7 CS / 10 total eligible; cs.CR, cs.DS, cs.LG. Professor @Caltech, social sciences and statistics. Mastadon. e.g. arXiv:2605.14718.
37. **David Sumpter** (@Soccermatics) — 7 CS / 11 total eligible; cs.HC, cs.LG, cs.CL. Professor of Applied Maths and Author. Co-founder and data s. e.g. arXiv:2603.12741.
38. **Chris Choy** (@realChrisChoy) — 7 CS / 7 total eligible; cs.CV, cs.LG, cs.RO. Sr. Research Scientist @NvidiaAI. Ph.D. from @StanfordSVL.. e.g. arXiv:2604.20395.
39. **Tom Le Paine** (@TomLePaine) — 7 CS / 7 total eligible; cs.CL, cs.AI, cs.CV. Research Scientist at DeepMind. e.g. arXiv:2507.06261.
40. **Erfan Miahi** (@erfan_mhi) — 7 CS / 7 total eligible; cs.CL, cs.LG, cs.DC. Collab with people from @googledeepmind & @rlai lab (Rich Su. e.g. arXiv:2605.10893.
41. **Panagiotis D. Ritsos** (@ritsos_p) — 7 CS / 7 total eligible; cs.HC, cs.LG. aka Panos - #HCI, #XR, #InfoVis, #Data #Visualization, #Imme. e.g. arXiv:2508.08737.
42. **Martin Tomko** (homonym?) (@dinomirMT) — 7 CS / 7 total eligible; cs.LG, cs.CV, cs.CL. Understanding and supporting people in their spatial interac. e.g. arXiv:2603.04683.
43. **Douglas Eck** (@douglas_eck) — 6 CS / 6 total eligible; cs.CL, cs.AI, cs.LG. Google DeepMind lead and recovering faculty member. Sometime. e.g. arXiv:2508.04651.
44. **Scott Carter** (homonym?) (@HereticalSraffa) — 6 CS / 9 total eligible; cs.HC, cs.CL, cs.CY. Professor of Economics at The University of Tulsa. e.g. arXiv:2604.24536.
45. **Karthik Duddu** (homonym?) (@karthikduddu) — 6 CS / 6 total eligible; cs.CL, cs.AI, cs.IR. Google Research, CMU, IIT-G. e.g. arXiv:2509.20354.
46. **Bernease Herman** (@bernease) — 4 CS / 4 total eligible; cs.CY, cs.LG, cs.AI. Data sci at WhyLabs, UW eScience Institute, UW iSchool PhD s. e.g. arXiv:2508.06760.
47. **Romain Vuillemot** (@romsson) — 4 CS / 4 total eligible; cs.HC, cs.CV, cs.RO. Enseignant-chercheur / Assistant Professor @CentraleLyon @LI. e.g. arXiv:2409.07695.
48. **Alejandro Benito-Santos** (@alexbensan) — 4 CS / 4 total eligible; cs.CL, cs.HC, cs.IR. Assistant Professor @nlpuned. Visual analytics and language. e.g. arXiv:2601.20464.
49. **Jason Park** (homonym?) (@JasonPathology) — 4 CS / 4 total eligible; cs.AI, cs.CV, cs.CL. Pathologist and Clinical Genomics Lab Director. Tweets my ow. e.g. arXiv:2604.23150.
50. **Peter Butcher** (@pwsbutcher) — 4 CS / 4 total eligible; cs.HC. Lecturer in Human Computer Interaction at @BangorUni @Bangor. e.g. arXiv:2508.08737.
51. **Daniel Angus** (@antmandan) — 3 CS / 3 total eligible; cs.AI, cs.CY, cs.HC. Professor of Digital Communication @qutdmrc @QUTSchoolOfComm. e.g. arXiv:2511.15732.
52. **Adam Chekroud** (@drchekkers) — 3 CS / 3 total eligible; cs.AI, cs.ET, cs.CY. eliminating barriers to mental health. cofounder @spring hea. e.g. arXiv:2605.13318.
53. **Jaime Snyder** (@jay_ess) — 3 CS / 3 total eligible; cs.HC, cs.AI, cs.CY. Associate Professor, Information School, University of Washi. e.g. arXiv:2605.21777.
54. **Bill Chen** (homonym?) (@realchillben) — 3 CS / 3 total eligible; cs.CL, cs.AI, cs.LG. @openai ; Prev @ycombinator @Meta @Columbia views are my own. e.g. arXiv:2601.03267.
55. **Meredith Martin** (@mmvty) — 3 CS / 3 total eligible; cs.AI, cs.CY, cs.CL. Director CDH @PrincetonDH; English Prof. @prosodyarchive. ht. e.g. arXiv:2604.16403.
56. **Dan Paul Smith** (homonym?) (@danpaulsmith) — 3 CS / 5 total eligible; cs.CY, cs.SE, cs.CV. Lead Data Scientist @benevolent ai. Specialising in tooling,. e.g. arXiv:2601.14588.
57. **Hyemi Song** (@BohyemianSong) — 3 CS / 3 total eligible; cs.HC, cs.CL, cs.AI. Current: UMD CS PhD, Natural Language+Immersive DataVis, For. e.g. arXiv:2510.12156.
58. **Ian McKenzie** (@McKenzieIA) — 3 CS / 3 total eligible; cs.CL, cs.AI, cs.LG. . e.g. arXiv:2506.24068.
59. **Mariya I. Vasileva** (@mariyaivasileva) — 2 CS / 2 total eligible; cs.CV, cs.LG, cs.AI. Research Scientist. Multimodal world models, evaluation • pr. e.g. arXiv:2212.12645.
60. **Kolawole J. Adebayo** (@collawolley) — 2 CS / 2 total eligible; cs.CV, cs.AI. Assistant Prof @ Maynooth // Ex Fellow @EUErasmusPlus // Ex. e.g. arXiv:2410.22490.
61. **Frank Schlosser** (@franksh_) — 2 CS / 3 total eligible; cs.CY, cs.SI. Data Scientist @ Spotify. Former PhD candidate in Physics at. e.g. arXiv:2304.12087.
62. **Aditeya Pandey** (@aaditeya) — 2 CS / 2 total eligible; cs.HC, cs.CY, cs.GR. Engineering + Research for Genomics Data Analysis @Regeneron. e.g. arXiv:2210.06417.
63. **Ashish Jaiswal** (@ashiz2013) — 2 CS / 2 total eligible; cs.AI, cs.CL, cs.HC. Research Scientist @meta / Ph.D. (Vision+ML+HCI) @utarlingto. e.g. arXiv:2411.06798.
64. **Michael O'Riordan** (@M_O_Riordan) — 2 CS / 4 total eligible; cs.LG, cs.AI. Research Scientist at Spotify 🎵 PhD in Astrophysics 🚀. e.g. arXiv:2503.18756.
65. **Luke Sanford** (@LC_Sanford) — 2 CS / 2 total eligible; cs.LG, cs.CL. Assistant Prof @YaleEnvironment.  Environmental Politics, re. e.g. arXiv:2502.12323.
66. **Tomasz Malisiewicz** (@quantombone) — 1 CS / 1 total eligible; cs.CV. Research Scientist Manager @ Meta Reality Labs. ex-Amazon, e. e.g. arXiv:2304.02009.
67. **Nelson Silva** (@njssnjss) — 1 CS / 1 total eligible; cs.HC, cs.CY, cs.SE. Senior Lecturer & Researcher at IT:U (https://t.co/tTSeCSTLQ. e.g. arXiv:2303.14699.
68. **Abhishek Koladiya** (@abhivkoladiya) — 1 CS / 1 total eligible; cs.LG, cs.DC. Postdoc  @StanfordMed / @ISAC CYTO Marylou Ingram Scholar /. e.g. arXiv:2201.00701.
69. **Shameer Khader** (@kshameer) — 1 CS / 1 total eligible; cs.LG. Global Head @Sanofi: Computational & AI Strategy, AI/ML, Dat. e.g. arXiv:2311.17969.
70. **Rex Douglass** (@RexDouglass) — 1 CS / 3 total eligible; cs.CL. Applied Scientist in Industry. Previously https://t.co/6rhmL. e.g. arXiv:2401.10558.
71. **Leonardo F. Nascimento** (@leofn3) — 1 CS / 1 total eligible; cs.IR, cs.AI, cs.CY. Chem Tech, Psychologist, PhD in Soc Sci / Computacional Soci. e.g. arXiv:2604.16337.
72. **Joses Ho** (@jacuzzijo) — 1 CS / 1 total eligible; cs.LG. Senior Research Fellow working on @GISAID data. Previously @. e.g. arXiv:2505.22688.
73. **Derya Unutmaz** (@Derya_) — 1 CS / 1 total eligible; cs.CL, cs.AI. please Follow my main account @DeryaTR    Professor @jackson. e.g. arXiv:2511.16072.
74. **Christoph Kinkeldey** (@geovisual) — 1 CS / 1 total eligible; cs.HC, cs.AI, cs.CY. visualization researcher, lecturer, developer. datavis, geov. e.g. arXiv:2109.11849.
75. **Nezar Abdennur** (@nv1ctus) — 1 CS / 2 total eligible; cs.HC. computational biologist / biological computer / asst prof @U. e.g. arXiv:2605.04306.
76. **Steve Smith** (homonym?) (@spsmith1) — 1 CS / 2 total eligible; cs.CR. PhD Computer Scientist, Unfussy Bon Vivant, Iconoclast, Cont. e.g. arXiv:2404.18785.
77. **Jonathan C Stroud** (@jonathancstroud) — 1 CS / 1 total eligible; cs.CV, cs.AI, cs.LG. Software Engineer at Waymo. Former PhD in Computer Vision at. e.g. arXiv:2306.01075.
78. **Nicholas Spyrison** (@nspyrison) — 1 CS / 2 total eligible; cs.AI, cs.LG. Multivariate data visualizations and dimensionality reductio. e.g. arXiv:2301.00077.
79. **Cameron Yick** (@cam_data) — 1 CS / 1 total eligible; cs.HC. Data Science and Viz Links for #JacksonBigData course @Yale.. e.g. arXiv:2110.11986.
80. **Jeremy Howard** (@jeremyphoward) — 1 CS / 1 total eligible; cs.CL, cs.AI. 🇦🇺 Co-founder: @AnswerDotAI/@FastDotAI ; Prev: Professor@UQ;. e.g. arXiv:2412.13663.
81. **Abhishek Nagaraj** (@abhishekn) — 1 CS / 1 total eligible; cs.HC. Associate Prof @berkeleyhaas, NBER RA. Dad to 2 girls. he/hi. e.g. arXiv:2305.16872.
82. **Carmen Ng** (homonym?) (@Carmen_NgKaMan) — 1 CS / 1 total eligible; cs.AI, cs.HC, cs.RO. Responsible AI in 🤖 & cross-cultural AI ethics @tu muenchen. e.g. arXiv:2603.16537.
83. **Alex Engler** (homonym?) (@AlexCEngler) — 1 CS / 1 total eligible; cs.CY, cs.AI, cs.LG. Penn Center for Media, Tech & Democracy / "If you can keep i. e.g. arXiv:2403.07918.
84. **Branden Murray** (homonym?) (@bmurr26) — 1 CS / 1 total eligible; cs.LG. data scientist at @h2oai. kaggle competition grandmaster. ma. e.g. arXiv:2605.18383.
85. **Alex Sherstinsky** (homonym?) (@AlexSherstinsky) — 1 CS / 1 total eligible; cs.CL, cs.AI, cs.LG. Scientist, Engineer, Manager, Musician, Athlete, Thespian, F. e.g. arXiv:2405.00732.
86. **Hassan Hijazi** (homonym?) (@HassanLHijazi) — 1 CS / 4 total eligible; cs.CV. Scientist at Los Alamos National Laboratory, works on Optimi. e.g. arXiv:2506.22797.
87. **Damon Civin** (homonym?) (@DCivin) — 1 CS / 1 total eligible; cs.AI, cs.CL, cs.CV. Data scientist, AI @ meta. Coffee enthusiast, lousy surfer,. e.g. arXiv:2407.21783.
88. **Federico Castanedo** (homonym?) (@overfit) — 1 CS / 1 total eligible; cs.AI, cs.LG. Ditector InceptionAI - Adjunct Prof IE University. ex DataRo. e.g. arXiv:2605.14455.
89. **Michael Tu** (homonym?) (@tuzhucheng) — 1 CS / 1 total eligible; cs.CE, cs.DC, cs.ET. Research Scientist/Engineer @LumaLabsAI. Prev. Research Engi. e.g. arXiv:2309.00597.
