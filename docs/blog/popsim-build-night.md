# Simulating 6,245 real people on one machine

Last night I went to [a simulation build night](https://luma.com/th01qwp1) organized around two papers that simulate absurdly large artificial societies: [Light Society](https://arxiv.org/abs/2506.12078), which runs over a billion LLM agents grounded in World Values Survey demographics, and [MatrAIx](https://arxiv.org/abs/2608.04205), which maintains 8.3 billion persona records. Both are impressive. Neither is something you can run at home.

So with Yvonne Chen and Jake Schwartz, I built [popsim](https://popsim.micahstubbs.ai) — an attempt to reproduce the load-bearing elements of both papers on a single machine, over one public dataset, in an evening. Everything below runs in under 300 MB of RAM.

## Finding a dataset that still exists

The first surprise was how much the tweet-dataset landscape has collapsed. Since X shut down free API access in 2023, the standard academic practice of sharing tweet-ID lists for "rehydration" is effectively dead — the IDs are still out there, billions of them, but turning them back into text requires an enterprise contract.

What you want now is full-text corpora, and the best one for persona work turns out to be seventeen years old: [Sentiment140](https://huggingface.co/datasets/stanfordnlp/sentiment140), 1.6 million labeled tweets from 2009. We measured the alternatives on one criterion — how many distinct users have at least 20 tweets each, enough history to ground a persona — and Sentiment140 won by an order of magnitude: 6,245 qualifying users against the Community Archive's 363 total accounts.

## Five experiments, one honest negative result

The [interactive explainer](https://popsim.micahstubbs.ai) walks through everything, but the short version:

**Persona mining.** Every user with ≥20 tweets became a persona card: sentiment disposition, verbosity, mention rate, peak posting hour, vocabulary. This is MatrAIx's human-grounded persona idea at hackathon scale.

**A mixture-of-models scale ladder.** Light Society affords a billion agents by mixing full LLMs with distilled surrogates. Same trick, one node: full LLM agents for the 927 heaviest users, cheap surrogates for 5,318 more, statistical samplers for the remaining 653,530. That's 702.7× cheaper per simulation tick than an all-LLM population.

**Diffusion, tested against ground truth.** The cohort contains a real social graph — 31,515 @-mention edges between personas. We seeded each user with their first-half sentiment, ran DeGroot opinion diffusion over the real graph, and asked whether that predicts their second-half sentiment better than just assuming people stay themselves. It doesn't. Diffusion managed r = 0.54; plain persistence hit r = 0.73. **Disposition beats diffusion**, at least on a 48-day horizon — which is itself an argument for persona-grounded simulators over contagion-heavy ones.

**Parasocial structure.** Of 293,212 observable user pairs, strong mutual bonds (0.6%) and strong one-way attachments (0.7%) are almost exactly balanced — for every real friendship in the graph there's one sustained unrequited one. And 12.1% of all mention volume flows to accounts that structurally never reply. If you're building a population simulator, that broadcast tier costs almost nothing to model, because it's one-directional by definition.

**A benchmark you can try to beat.** We defined a fixed behavioral-adherence protocol: per-user temporal 80/20 split, sentiment adherence scored on 42,998 held-out tweets. A zero-parameter baseline (predict each user's own majority sentiment) gets 63.1%. MatrAIx reports 91.5% adherence under their protocol, which frames the gap. [Section 06 of the site](https://popsim.micahstubbs.ai/#6) has a copy-paste prompt that points any agentic LLM at the repo to run its own research loop against the protocol.

I ran that loop myself as a sanity check: a TF-IDF logistic classifier trained on the 1.5M non-test tweets reaches 81.5%, blending it with per-user priors gets 82.0%, and a char-ngram ensemble plateaus there. So 82.0% is the number to beat, and the remaining ten points probably need a real language model.

## The part I didn't expect

The most useful output wasn't any single number — it was how far persona grounding carried everything else. The diffusion experiment failed *in an informative direction*: who you are predicts your behavior better than who you talk to. The parasocial analysis said most of the attention economy is one-directional anyway. Both findings push the same way: if you're simulating a population on a budget, spend it on the personas.

Code and analysis are in [pop-world-model-sim](https://github.com/micahstubbs/pop-world-model-sim), the deployed site lives in [popsim](https://github.com/micahstubbs/popsim), and there's an arXiv draft in the works. If you beat 82.0% on the benchmark, open a PR — we want to see it.
