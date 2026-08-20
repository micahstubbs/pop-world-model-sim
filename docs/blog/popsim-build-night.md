# Simulating 6,245 real people on one machine

Last night I went to [a simulation build night](https://luma.com/th01qwp1) built around two papers that simulate absurdly large artificial societies: [Light Society](https://arxiv.org/abs/2506.12078) (a billion LLM agents) and [MatrAIx](https://arxiv.org/abs/2608.04205) (8.3 billion persona records). Both are impressive. Neither is something you can run at home.

So with [Yvonne Chen](https://x.com/ycyvonne_) and Jake Schwartz, I built [popsim](https://popsim.micahstubbs.ai) — an attempt to reproduce the load-bearing elements of both papers on a single machine, over one public dataset, in an evening. Everything runs in under 300 MB of RAM.

#### Finding a dataset that still exists

The first surprise was how thoroughly the tweet-dataset landscape has collapsed. Since X shut down free API access in 2023, sharing tweet-ID lists for "rehydration" is effectively dead — the IDs are out there, but turning them back into text requires an enterprise contract.

What you want now is full-text corpora, and the best one for persona work turns out to be seventeen years old: [Sentiment140](https://huggingface.co/datasets/stanfordnlp/sentiment140), 1.6 million labeled tweets from 2009. Measured on distinct users with at least 20 tweets each — enough history to ground a persona — it beats the runner-up by an order of magnitude: 6,245 qualifying users against the Community Archive's 363 accounts.

#### Five experiments, one honest negative result

The [interactive explainer](https://popsim.micahstubbs.ai) has the full story. The short version:

**Persona mining.** Every user with ≥20 tweets became a persona card — sentiment disposition, verbosity, mention rate, peak posting hour, vocabulary. MatrAIx's human-grounded personas at hackathon scale.

**A scale ladder.** Light Society's trick, one node: full LLM agents for the 927 heaviest users, cheap surrogates for 5,318, statistical samplers for the rest. 702.7× cheaper per tick than all-LLM.

**Diffusion vs. ground truth.** The cohort has a real social graph — 31,515 @-mention edges. I ran DeGroot opinion diffusion over it and asked whether that predicts second-half sentiment better than assuming people stay themselves. It doesn't: r = 0.54 against r = 0.73 for plain persistence. **Disposition beats diffusion**, at least on a 48-day horizon.

**Parasocial structure.** Strong mutual bonds (0.6% of pairs) and strong one-way attachments (0.7%) are almost exactly balanced, and 12.1% of mention volume flows to accounts that never reply. That broadcast tier costs almost nothing to simulate — it's one-directional by definition.

**A benchmark.** Per-user temporal 80/20 split, sentiment adherence on 42,998 held-out tweets. The zero-parameter baseline gets 63.1%; MatrAIx's 91.5% frames the gap. [Section 06](https://popsim.micahstubbs.ai/#6) has a copy-paste prompt that points any agentic LLM at the repo to run its own research loop. I ran it myself: TF-IDF plus per-user priors reaches 82.0%, then plateaus. The remaining ten points probably need a real language model.

#### The part I didn't expect

Both surprises push the same way. Diffusion failed *informatively* — who you are predicts your behavior better than who you talk to — and the parasocial analysis says most of the attention economy is one-directional anyway. If you're simulating a population on a budget, spend it on the personas.

Code is in [pop-world-model-sim](https://github.com/micahstubbs/pop-world-model-sim), the site source in [popsim](https://github.com/micahstubbs/popsim), and there's an arXiv draft in the works. Beat 82.0% and open a PR — I want to see it.
