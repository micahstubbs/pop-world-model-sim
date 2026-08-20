# Publicly Available Twitter/X Tweet Datasets for Download and Study

**Generated:** 2026-08-19
**Topic:** Well-structured, easy-to-access, publicly downloadable Twitter/tweet datasets with an academic track record
**Context:** Supporting a hackathon project at the [Postlabor.dev -- Building Economic World Models](https://luma.com/th01qwp1) Simulation Build Night, an event focused on large-scale AI agent simulations of economic and social systems. Dataset selection below is weighted toward corpora useful for seeding, calibrating, or evaluating agent-based social simulations.

## Executive Summary

The single most important fact about Twitter data in 2026 is that the era of freely collecting or "rehydrating" tweets is over. In early 2023, X shut down the free and Academic Research API tiers; replacement commercial tiers start at roughly $100/month with no historical access and climb to about $42,000/month for enterprise access. This broke the standard academic sharing workflow, in which papers shipped tweet-ID lists that anyone could rehydrate into full tweets with tools like twarc or the DocNow Hydrator. As a result, the practical value of a dataset today depends almost entirely on whether it ships **full tweet text and metadata**, not just IDs.

Fortunately, several excellent full-content corpora remain publicly downloadable and have deep academic pedigrees. For quick, structured work: **Sentiment140** (1.6M labeled tweets, one CSV) and **TweetEval** (seven classification tasks with fixed splits) are the easiest on-ramps. For scale and raw realism: the **Archive Team Twitter Stream Grab** on the Internet Archive offers roughly a decade (2011-early 2023) of 1% sampled global tweets as complete JSON, about 50 GB compressed per month. For post-2023 data and full user timelines -- arguably the best fit for persona-driven agent simulation -- the **Community Archive** provides 7M+ donated tweets as an open Supabase database and API. For network structure to drive simulation topology, Stanford SNAP's **Higgs Twitter** dataset (456K users; follower, retweet, reply, and mention layers around a single global event) is the standout.

For the world-model-simulation use case specifically, the recommended stack is: Higgs Twitter for realistic network topology and diffusion dynamics; Community Archive or Archive Team samples for realistic content and user timelines to build agent personas; and TweetEval-style labeled sets for evaluating whether simulated content is distributionally plausible.

## The 2023-2026 Access Landscape (Read This First)

- In early 2023 Twitter/X shut down the free API and the Academic Research track that had provided full-archive access to vetted researchers ([Columbia Journalism Review](https://www.cjr.org/tow_center/qa-what-happened-to-academic-research-on-twitter.php), ["RIP Twitter API: A Eulogy"](https://arxiv.org/pdf/2404.07340)).
- Twitter's developer terms historically prohibited redistributing full tweet objects, so most academic datasets were released as **tweet-ID lists** meant to be rehydrated via the API ([Twitter Data Sharing guide, Melanie Walsh](https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/13-Twitter-Data-Sharing.html)). With free API access gone, DocNow Hydrator and twarc broke; **ID-only datasets are now largely unusable without an expensive enterprise contract or third-party hydration services** of varying legitimacy ([xcrop guide](https://xcrop.io/blog/twitter-data-academic-research), [Sorsa](https://api.sorsa.io/solutions/academic-research)).
- A promised X "Research API" was announced in January 2024 but had shipped no implementation details as of the end of 2024.
- Practical consequence: **prefer datasets that ship full text.** Treat ID-only corpora as unusable unless you already hold hydrated copies.

## Tier 1 -- Full-Text, Download-and-Go Datasets

### 1. Sentiment140 -- the classic starter dataset

1.6 million tweets from 2009, distantly labeled for sentiment via emoticons, created by Stanford researchers (Go, Bhayani, Huang). One flat CSV with tweet text, timestamp, user, and polarity label. It is among the most-cited sentiment corpora in NLP and remains a default benchmark.

- **Get it:** [Hugging Face (stanfordnlp/sentiment140)](https://huggingface.co/datasets/stanfordnlp/sentiment140), [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140), [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/sentiment140)
- **Structure:** single CSV, 6 columns; loads in one line of pandas.
- **Academic pedigree:** thousands of citations; standard baseline ([overview](https://medium.com/lexiconia/the-sentiment140-dataset-a-benchmark-for-sentiment-classification-7f37313bf757)).
- **Caveat:** 2009-era tweets (140 chars, no threads/quote-tweets); labels are noisy by construction.

### 2. TweetEval -- seven benchmark tasks in one repo

Cardiff NLP's unified benchmark: emotion recognition, emoji prediction, irony detection, hate speech, offensive language, sentiment, and stance detection -- all as multi-class tweet classification with fixed train/validation/test splits in a consistent format.

- **Get it:** [GitHub (cardiffnlp/tweeteval)](https://github.com/cardiffnlp/tweeteval); also on Hugging Face as `tweet_eval`.
- **Structure:** plain-text one-tweet-per-line files plus label files per task; trivially parseable.
- **Academic pedigree:** the standard tweet-classification benchmark since 2020 (Findings of EMNLP); the basis for the widely used TimeLMs/twitter-roberta models.
- **Fit for the hackathon:** ready-made evaluators -- score simulated agent output for sentiment/emotion/stance realism.

### 3. Archive Team Twitter Stream Grab -- a decade of raw global tweets

The Internet Archive hosts the "Spritzer" 1% sample of the global Twitter firehose, collected by Archive Team from 2011 until the API shutdown in early 2023 (with some gap months). Each month is a tarball of hourly bzip2 files of **complete tweet JSON objects, all fields included** -- text, user objects, entities, geo, retweet structure.

- **Get it:** [Collection index](https://archive.org/details/twitterstream); example items: [2017-01](https://archive.org/details/archiveteam-twitter-stream-2017-01), [2021-08](https://archive.org/details/archiveteam-twitter-stream-2021-08), [2022-11](https://archive.org/details/archiveteam-twitter-stream-2022-11).
- **Size:** ~50 GB compressed per month; download only the months you need.
- **Academic pedigree:** used across hundreds of papers as the standard "random sample of Twitter" ([Baylor digital scholarship overview](https://blogs.baylor.edu/digitalscholarship/2018/11/02/archive-team-the-twitter-stream-grab-historic-twitter-content/)).
- **Fit for the hackathon:** the most realistic raw material for populating a simulated feed; hour-resolution timing supports temporal dynamics. Budget parsing time -- it is raw JSON, not a tidy table.

### 4. Community Archive -- open, post-2023, full user timelines

An open-source project where users donate their full Twitter archives to a public-domain database: 7M+ tweets as of September 2025, growing, with a public Supabase API and downloadable data. This is the rare source that is (a) full-text, (b) legally clean (donated by the authors), and (c) still alive after the API shutdown.

- **Get it:** [GitHub (TheExGenesis/community-archive)](https://github.com/TheExGenesis/community-archive), site at community-archive.org; [analysis quickstart notebook](https://github.com/DefenderOfBasic/twitter-archive-toolkit/blob/main/Community_Archive_Analysis_Quickstart.ipynb).
- **Structure:** relational DB (tweets, users, likes, followers) queryable via Supabase REST API; bulk export available.
- **Unique property:** **complete per-user timelines**, not topic slices -- ideal for building believable long-horizon agent personas (the exact pattern used in recent generative-agent papers that seed simulated users from real tweet histories).
- **Caveat:** self-selected population (skews tech/"ingroup" Twitter); not a representative sample.

### 5. PHEME rumour dataset -- conversation threads with veracity labels

Twitter rumour conversation threads around breaking-news events (Charlie Hebdo, Ferguson, the Germanwings crash, etc.), annotated for rumour vs. non-rumour and veracity. Ships full thread structure (source tweet + reply cascades).

- **Get it:** via figshare ("PHEME dataset for Rumour Detection and Veracity Classification"); indexed in [awesome-twitter-data](https://github.com/shaypal5/awesome-twitter-data).
- **Academic pedigree:** the standard rumour-detection benchmark (Zubiaga et al.); the related Twitter15/Twitter16 sets are used in current LLM-agent disinformation simulations.
- **Fit for the hackathon:** real reply-cascade structures to validate simulated conversation trees against.

## Tier 2 -- Network/Graph Datasets (Simulation Topology)

### 6. SNAP Higgs Twitter -- the best single dataset for diffusion simulation

Built by monitoring Twitter July 1-7, 2012, around the Higgs boson discovery announcement. Contains a 456,631-node, 14.9M-edge follower graph **plus** time-stamped retweet, reply, and mention interaction layers for the same users -- i.e., both the substrate network and the diffusion that ran over it.

- **Get it:** [SNAP page](https://snap.stanford.edu/data/higgs-twitter.html) -- plain edge-list files, anonymized.
- **Academic pedigree:** Domenico et al., *The Anatomy of a Scientific Rumor* (Scientific Reports, 2013); a staple in information-diffusion literature ([example](https://arxiv.org/pdf/1508.00540)).
- **Fit for the hackathon:** wire agents onto the real follower graph and compare simulated cascade shapes against the recorded retweet/mention cascades. This is essentially a ready-made ground-truth experiment for a social world model.

### 7. SNAP ego-Twitter -- social circles

973 ego-networks (~81K users, 1.77M edges) crawled from public Twitter, with node features and hand-labeled "circles." From McAuley & Leskovec, *Learning to Discover Social Circles in Ego Networks* (NIPS 2012).

- **Get it:** [SNAP page](https://snap.stanford.edu/data/ego-Twitter.html); mirrors on [Academic Torrents](https://academictorrents.com/details/276e1028b08decbf711f275a57901dbde88ca5ab) and [Kaggle social-graph bundles](https://www.kaggle.com/datasets/wolfram77/graphs-social).
- **Fit:** realistic local community structure for small/medium simulations; widely used in community-detection papers ([example](https://arxiv.org/pdf/2012.09561)).

### 8. Kwak et al. 2010 follower graph -- historically foundational, now hard to get

The WWW 2010 paper *What is Twitter, a Social Network or a News Media?* released a crawl of 41.7M users and 1.47B follow edges. It defined how the field understands Twitter's topology, but the original distribution was taken down at Twitter's request; treat it as unavailable unless you find a mirror, and check terms before using one.

## Tier 3 -- Topical ID-Only Corpora (Hydration Caveat Applies)

These remain important to know about -- they dominate the citation record -- but **ship tweet IDs only**, and hydration is effectively broken post-2023.

- **COVID-19 Twitter dataset (Chen, Lerman, Ferrara / USC-ISI):** ongoing multilingual collection started January 2020; billions of IDs. [GitHub (echen102/COVID-19-TweetIDs)](https://github.com/echen102/COVID-19-TweetIDs); paper in [JMIR Public Health](https://publichealth.jmir.org/2020/2/e19273/). One of the most-studied social datasets ever. CC-BY-NC-4.0-style academic terms.
- **Augmented multilingual COVID-19 dataset (Lopez et al.):** ~3.0B tweets collected through 2022, with IDs plus derived fields (sentiment, NER, geo where computable) that partially offset the hydration problem. [GitHub (lopezbec/COVID19_Tweets_Dataset)](https://github.com/lopezbec/COVID19_Tweets_Dataset).
- **Monkeypox/mpox 2022 datasets:** e.g., a 556K-tweet open collection ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9680479/)) -- again ID-centric.
- **DocNow Catalog:** a registry of hundreds of event-based tweet-ID datasets (protests, elections, disasters) at [catalog.docnow.io](https://catalog.docnow.io/) -- excellent as an index of what exists, subject to the same hydration caveat.

**Removed at Twitter's request (do not plan around them):** SNAP **Twitter7** (476M tweets, June-Dec 2009) was withdrawn from Stanford's site ([SNAP page](https://snap.stanford.edu/data/twitter7.html), [mailing-list confirmation](https://groups.google.com/g/snap-datasets/c/4_sMYlFRf9Q)). Mirrors circulate, but the takedown reflects the rights-holder's position.

## Datasets Purpose-Built for LLM Agent Simulation (2025)

Directly relevant to the Postlabor.dev build-night theme:

- **BluePrint** (2025): a social-media user dataset built specifically for LLM persona evaluation and training -- clustered real user timelines into privacy-preserving persona prototypes ([arXiv](https://arxiv.org/pdf/2510.02343)).
- Recent generative-agent-based-modeling (GABM) work seeds simulated users from real tweet histories -- e.g., simulating conversations with agents initialized from 2020 US-election user timelines and validating against the Twitter16 rumour set ([ResearchGate](https://www.researchgate.net/publication/397507280_Simulating_conversations_on_social_media_with_generative_agent-based_models), [survey chapter](https://dl.acm.org/doi/10.1007/978-3-031-78541-2_10)).
- Population-scale LLM-agent frameworks (AgentSociety, EconSimulacra, APS) use exactly the seed-from-real-corpora pattern the Tier 1 datasets enable ([EconSimulacra](https://arxiv.org/pdf/2606.26883), [APS](https://arxiv.org/pdf/2605.27419)).

## Analysis -- Which Dataset for Which Job

| Need | Best choice | Why |
|---|---|---|
| Load a clean table in 5 minutes | Sentiment140 | One CSV, 1.6M rows, labeled |
| Benchmark text realism | TweetEval | 7 tasks, fixed splits |
| Raw realistic feed content | Archive Team Stream Grab | Full JSON, 2011-2023 |
| Full user timelines for personas | Community Archive | Post-2023, full text, open API |
| Topology + ground-truth diffusion | SNAP Higgs Twitter | Follow graph + timed cascades |
| Conversation-thread structure | PHEME | Real reply trees with veracity labels |

Cross-cutting cautions: (1) anything ID-only is effectively frozen; (2) most corpora predate 2023 -- X-era behavior (paid verification, algorithmic feed changes) is not represented anywhere except the Community Archive; (3) respect per-dataset licenses -- several are NonCommercial; (4) all of these contain real people's speech -- aggregate, don't republish individual identifiable content.

## Recommendations -- Punch List for the Build Night

1. **Start with SNAP Higgs Twitter as the simulation substrate.** Download the follower graph + retweet/reply/mention layers (single page, small files). It gives both agent topology and ground-truth cascades to validate against. Cost: minutes. Defer only if the project is content-only with no network component.
2. **Pull one month of the Archive Team Stream Grab (e.g., 2022-11) for realistic content.** Sample a few hourly .bz2 files rather than the full 50 GB tarball. Use it to build empirical distributions of tweet length, posting cadence, and topic mix that agents should match. Defer if bandwidth-constrained; Sentiment140 is a lightweight fallback.
3. **Use the Community Archive API for persona seeding.** Query a handful of complete user timelines and initialize LLM agents from them (the GABM pattern). It's the only live, full-text, post-2023 source. Cost: an hour of API exploration.
4. **Adopt TweetEval classifiers as the realism scorecard.** Run cardiffnlp's pretrained twitter-roberta models over simulated output and compare label distributions to real data. Cost: low; models and data are on Hugging Face.
5. **Skip ID-only corpora (COVID-19-TweetIDs, DocNow catalog entries) for the hackathon.** Hydration is dead without enterprise API money. Revisit only if X ships the promised Research API.
6. **Do not build on Twitter7 or the Kwak 2010 graph.** Both were withdrawn at Twitter's request; mirrors carry legal ambiguity the project doesn't need.

## Sources

- [Archive Team: The Twitter Stream Grab (Internet Archive)](https://archive.org/details/twitterstream) -- decade-scale raw tweet JSON collection
- [Baylor Digital Scholarship on the Stream Grab](https://blogs.baylor.edu/digitalscholarship/2018/11/02/archive-team-the-twitter-stream-grab-historic-twitter-content/) -- format and size details
- [stanfordnlp/sentiment140 on Hugging Face](https://huggingface.co/datasets/stanfordnlp/sentiment140) * [Kaggle mirror](https://www.kaggle.com/datasets/kazanova/sentiment140) * [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/sentiment140)
- [cardiffnlp/tweeteval (GitHub)](https://github.com/cardiffnlp/tweeteval) -- TweetEval benchmark
- [TheExGenesis/community-archive (GitHub)](https://github.com/TheExGenesis/community-archive) * [analysis quickstart](https://github.com/DefenderOfBasic/twitter-archive-toolkit/blob/main/Community_Archive_Analysis_Quickstart.ipynb)
- [SNAP Higgs Twitter](https://snap.stanford.edu/data/higgs-twitter.html) * [SNAP ego-Twitter](https://snap.stanford.edu/data/ego-Twitter.html) * [SNAP Twitter7 (withdrawn)](https://snap.stanford.edu/data/twitter7.html)
- [echen102/COVID-19-TweetIDs (GitHub)](https://github.com/echen102/COVID-19-TweetIDs) * [JMIR paper](https://publichealth.jmir.org/2020/2/e19273/) * [lopezbec augmented dataset](https://github.com/lopezbec/COVID19_Tweets_Dataset)
- [Melanie Walsh, Twitter Data Sharing](https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/13-Twitter-Data-Sharing.html) -- tweet-ID/hydration norms
- [CJR: What happened to academic research on Twitter?](https://www.cjr.org/tow_center/qa-what-happened-to-academic-research-on-twitter.php) * [RIP Twitter API (arXiv)](https://arxiv.org/pdf/2404.07340) * [xcrop 2026 access guide](https://xcrop.io/blog/twitter-data-academic-research)
- [BluePrint persona dataset (arXiv)](https://arxiv.org/pdf/2510.02343) * [GABM conversation simulation](https://www.researchgate.net/publication/397507280_Simulating_conversations_on_social_media_with_generative_agent-based_models)
- [shaypal5/awesome-twitter-data (GitHub)](https://github.com/shaypal5/awesome-twitter-data) -- meta-index of Twitter datasets
- [DocNow Catalog](https://catalog.docnow.io/) -- registry of event-based tweet-ID datasets
- [Monkeypox 2022 dataset (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9680479/)
