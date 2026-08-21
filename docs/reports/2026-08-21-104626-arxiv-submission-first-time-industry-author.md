# Submitting to arXiv in August 2026 as a First-Time Author from Industry

**Generated:** 2026-08-21
**Topic:** The end-to-end process for getting a paper accepted and announced on arXiv in August 2026, with emphasis on the obstacles that apply to a first-time submitter who works in industry (no academic email, no prior arXiv papers, no advisor). Tailored at the end to the popsim paper in this repository.

## Executive Summary

arXiv in 2026 is materially harder to enter than it was two years ago, and almost all of the new friction lands on exactly the profile described here: a first-time submitter without an academic affiliation. Three changes matter most. First, as of **January 21, 2026, an institutional email no longer auto-endorses anyone** in any arXiv section; automatic endorsement now requires *both* an academic/research email *and* claimed co-authorship of an existing arXiv paper in the same "endorsement domain." Everyone else, industry authors included, must obtain a **personal endorsement** from an established arXiv author. Second, since **October 31, 2025, the CS section rejects review/survey and position papers unless they have already passed peer review** at a journal or conference (workshops do not count) and carry the journal reference and DOI in metadata. Third, moderation itself is slower and stricter in categories that attract misrouted or LLM-generated submissions; an independent analysis of ~64k papers shows median delay is still about one working day for most categories, but the 90th percentile in catch-all categories like cs.CY, cs.OH, math.GM, and physics.gen-ph runs to 2–3 weeks.

None of this is a barrier to a well-prepared industry author. The winning sequence is: (1) create an ORCID and an arXiv account under your real name and current industry affiliation; (2) identify the precise category and confirm your paper is a *research* contribution, not a survey or position piece; (3) secure a personal endorser before you finish polishing the manuscript, asking one or two people you actually know or whose work you cite, never mass-emailing; (4) submit LaTeX source, not a compiled PDF, with a disclosure of any significant generative-AI use; (5) choose a license deliberately, because it is irrevocable; (6) submit before 14:00 Eastern on a weekday and leave a buffer of one to two weeks before any external deadline, because a first-time submission is more likely to be held for human review.

The report below documents each step with the governing rule, the source, and the practical failure modes observed by other first-time authors.

## Research Findings

### What arXiv is and is not

arXiv is a moderated distribution service, not a peer-reviewed journal. Moderators are "volunteer subject matter experts with terminal degrees in their field" who check that a submission is topical for its category, meets minimal scholarly standards, and is of "interest, relevance, and value to the disciplines we serve." They do not referee correctness. Acceptance means the paper is announced with an arXiv identifier; it is not an endorsement of the results. Several Hacker News commenters pointed out that first-time authors frequently confuse the two and that journals accept direct submissions without an arXiv preprint. ([arXiv moderation](https://info.arxiv.org/help/moderation/index.html); [HN thread](https://news.ycombinator.com/item?id=46243256))

Content arXiv explicitly declines: course projects and assignments, proposals, news, political content, plagiarized or falsified material, papers with images "likely to cause egregious offense," and content whose submitter lacks the legal right to grant the chosen license. Authors clearing a backlog are asked to submit no more than three papers per day. ([arXiv moderation](https://info.arxiv.org/help/moderation/index.html))

### Step 1: Identity, account, and affiliation

- Each person may hold **one** arXiv account. Register under your real name; arXiv treats misrepresentation of identity or affiliation as "possible grounds for immediate and permanent suspension." ([Identity and affiliation policy](https://info.arxiv.org/help/policies/identity_and_affiliation.html))
- "Claimed affiliation should be current in the conventional sense: e.g., physical presence, funding, e-mail address." A company affiliation is perfectly acceptable; what is not acceptable is listing a university you are not currently part of. Use the company name as it would appear on letterhead. (Same source.)
- arXiv recommends linking an **ORCID iD** to the account. The solo-researcher guide reviewed here goes further and recommends creating the ORCID *before anything else*, since it disambiguates you across Google Scholar, Semantic Scholar, and any later journal submission. ([Identity policy](https://info.arxiv.org/help/policies/identity_and_affiliation.html); [Solo researcher guide](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv))
- Use an email you will keep. Endorsement, hold notices, and appeal correspondence all go to the account address, and the account email is also how arXiv detects (or no longer detects) institutional status.

### Step 2: Endorsement — the gate that changed in 2026

**The rule.** From arXiv's January 21, 2026 announcement: "arXiv will no longer accept institutional email addresses ... as the sole qualifier of endorsement for new authors." Endorsement now follows two paths:

1. *Automatic*: requires **both** an academic/research institutional email **and** claimed ownership of a previous paper already accepted into the same endorsement domain.
2. *Personal*: "seeking personal endorsement directly from an established arXiv author in the same endorsement domain."

arXiv is explicit that "arXiv staff cannot waive endorsement requirements or provide a personal endorsement for authors." The rationale given is "an unsustainable increase in the number of non-scientific submissions" from auto-endorsed accounts. Math piloted the change on December 10, 2025; it went site-wide six weeks later. ([Jan 21, 2026 blog](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/); [Dec 10, 2025 blog](https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/))

**What this means for an industry author.** Path 1 is closed to you unless you hold a current academic email. You need a personal endorsement. The mechanics, from arXiv's help page:

- When you start a submission in a category where you are not endorsed, arXiv shows an endorsement request that generates a **six-character alphanumeric code**. You send that code to a prospective endorser; they enter it on arXiv's endorsement form and approve or deny.
- An eligible endorser must have authored enough arXiv papers in the endorsement domain, counting only papers submitted **between three months and five years ago**. arXiv says "any active scientist who has been working in their field for a few years should be able to endorse."
- You can check whether a specific person qualifies: open any of their arXiv abstract pages and click **"Which authors of this paper are endorsers?"** near the bottom.
- arXiv's guidance on whom to ask: "it is best for you to find an endorser who you know personally and is knowledgeable in the subject area of your work." And the etiquette rule: "it is inappropriate to email large numbers of potential endorsers at once, or to repeatedly email the same endorser with a request for endorsement."
- Endorsement is not review. The endorser "should either know the person or review the intended paper to verify it's appropriate for the subject area" but need not verify correctness. ([Endorsement help](https://info.arxiv.org/help/endorsement.html); [CASRAI summary](https://casrai.org/dictionary/term/arxiv-endorsement-system))

**What actually works, per first-hand accounts.** The HN thread on independent-researcher endorsement and the solo-researcher guide converge on the same tactics:

- Ask authors of papers you cite heavily. One commenter got endorsed this way after checking the "endorsers" link on the abstract pages of cited papers.
- Ask someone from a workshop, meetup, or reading group where you presented or interacted ("I asked someone who organised a workshop I had spoken at").
- Ask a co-author's former advisor, or a former colleague who moved to academia, or a university collaborator on a company project.
- Send the draft PDF with the request so the endorser can satisfy the "topically appropriate" standard in five minutes. A cold request with no manuscript attached is routinely ignored.
- Public "please endorse me" posts on forums (Hugging Face, ResearchGate) exist but show few success stories; the thread consensus is that genuine connection is "the most reliable path." ([HN thread](https://news.ycombinator.com/item?id=46243256); [HF forum example](https://discuss.huggingface.co/t/seeking-arxiv-cs-ai-endorsement-independent-researcher-preprint-on-emergent-identities-in-llms/168007); [Solo researcher guide](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv))

**Co-author leverage.** Endorsement is per-submitter, not per-paper. If any co-author is already endorsed in the target category, that co-author can be the submitting author and no endorsement is needed. Alternatively, if a co-author has an academic email and prior arXiv papers in the domain, they should claim ownership of those papers first ("claim ownership of all of them and keep your arXiv account as up-to-date as possible") and they will likely pass Path 1. ([Jan 21, 2026 blog](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/))

**Endorsement domains.** Endorsement is granted per "endorsement domain," a cluster of related categories, not per individual category. Being endorsed once in a CS domain typically covers related CS categories; submitting later to a different domain (e.g., q-bio or physics.soc-ph) triggers a fresh endorsement check. (Same source.)

### Step 3: Pick the right category and confirm the content type

**Category.** Misclassification is the most common cause of delay for newcomers. The fi-le.net analysis (63,847 papers, 2015–April 2026) found the overall median delay is one working day, but catch-all categories behave very differently: cs.CY (Computers and Society) has mean delay 6.0 working days with a 90th percentile of 21 days; cs.OH 6.9 days mean, p90 19 days; math.GM and physics.gen-ph similar. The author's diagnosis: these categories fill with papers whose authors "don't know all the subjects," and moderators must read and reclassify each one. Picking a specific, correct primary category is the single cheapest way to reduce hold risk. ([fi-le.net delay analysis](https://fi-le.net/arxiv/))

Older accounts (the n-Category Café and Azimuth discussions of a 2022 case) describe papers reclassified to general categories "without communication from arXiv," and note that "reclassifications, especially to general categories, may damage a paper's credibility." Moderators may reclassify without author consent. You may request a different category via appeal, but the decision is theirs. ([n-Category Café](https://golem.ph.utexas.edu/category/2022/02/submission_to_arxiv.html); [Azimuth](https://johncarlosbaez.wordpress.com/2022/02/04/submission-to-arxiv/))

**Content type (CS only).** Since October 31, 2025: "review articles and position papers must now be accepted at a journal or a conference and complete successful peer review" before submission to any CS category, and "must include documentation of successful peer review." Specifically:

- Include the peer-reviewed journal reference and DOI in the submission metadata; without it "your review article or position paper will likely be rejected."
- Workshop review "generally does not meet the same standard of rigor ... and is not enough."
- arXiv frames this as enforcement of an existing rule, not a new policy: review and position papers "are not (and have never been) listed as part of the accepted content types" and were historically accepted only at moderator discretion.
- If rejected on this ground, do not resubmit; file an appeal once peer review is complete.
- The trigger was volume: arXiv now receives "hundreds of review articles every month," most of which are "little more than annotated bibliographies." ([Oct 31, 2025 blog](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/); [Stanford SDR summary](https://sdr.library.stanford.edu/news/arxiv-policy-change-impacts-computer-science-authors); [404 Media](https://www.404media.co/arxiv-changes-rules-after-getting-spammed-with-ai-generated-research-papers/))

The practical implication for a first-time author: a paper that *reproduces*, *benchmarks*, *measures*, or *builds* something is a research article and is unaffected. A paper whose contribution is "we surveyed the literature" or "we argue that the field should" is now effectively blocked in CS until refereed. Framing matters: a moderator skimming the abstract should see a concrete artifact or result in the first two sentences.

### Step 4: Prepare the files

- **Submit LaTeX source.** arXiv's order of preference is "(La)TeX, AMS(La)TeX, PDFLaTeX," then PDF, then HTML. Critically, "We do not accept dvi, PS, or PDF created from TeX/LaTeX source." If you wrote it in LaTeX, you must upload the `.tex`, `.bbl`, figures, and any custom `.sty`/`.cls` files. arXiv compiles it on their TeX Live installation and you must check the resulting PDF before finalizing. ([Submit help](https://info.arxiv.org/help/submit/index.html); [Why TeX](https://info.arxiv.org/help/faq/whytex.html))
- Include the `.bbl`, not just the `.bib`; arXiv does not run BibTeX.
- Filenames may use only `a-z A-Z 0-9 _ + - . , =` and are case-sensitive (`Figure1.PDF` and `figure1.pdf` are different files). Figures for PDFLaTeX: JPEG, GIF, PNG, or PDF. ([Submit help](https://info.arxiv.org/help/submit/index.html))
- Expect arXiv's compiler to differ from yours: strip `\usepackage` lines you do not use, avoid shell-escape (`minted`, `svg`), and make sure `hyperref` options are compatible. arXiv adds its own watermark and may rebuild with `hyperref` in its own configuration; test locally with a fresh TeX Live if possible.
- **Generative-AI disclosure.** arXiv's moderation policy requires disclosure of "significant use of sophisticated tools, such as instruments and software," explicitly including "text-to-text generative AI," and states that authors bear "full responsibility for all its contents, irrespective of how the contents were generated." A one-sentence statement in the acknowledgments or a footnote suffices; listing an LLM as an author does not. ([arXiv moderation](https://info.arxiv.org/help/moderation/index.html))
- Keep the manuscript self-contained and conventionally structured: abstract, introduction, related work, method, results, discussion, references. Moderators decline papers lacking "appropriate and carefully prepared sections, figures, tables, references." The solo-researcher guide singles out *related work* as the section that signals field literacy for authors without institutional credentials. ([arXiv moderation](https://info.arxiv.org/help/moderation/index.html); [Solo researcher guide](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv))

### Step 5: Metadata and license

- Metadata: title, author list (names exactly as in the PDF), abstract (plain text with limited TeX math, no line breaks or markup), primary category, optional cross-lists, optional comments (page count, code URL, "accepted at X"), optional journal reference and DOI, optional report number and ACM/MSC classes. A code/data URL in the comments field is a positive signal for moderators reviewing a reproduction or systems paper.
- **Licenses offered**: CC BY 4.0, CC BY-SA 4.0, CC BY-NC-SA 4.0, CC BY-NC-ND 4.0, CC0, and the arXiv perpetual non-exclusive license 1.0 (the minimal grant that lets arXiv distribute but reserves all other rights). arXiv "encourages authors to choose a liberal license for re-use." ([License help](https://info.arxiv.org/help/license/index.html))
- **Irrevocable.** "The license chosen is irrevocable and cannot be changed," per version. You can pick a different license for v2, but v1 stays as licensed. Before choosing CC BY, confirm that any journal or conference you might later target accepts CC BY preprints (most do; some publishers require the accepted manuscript to be CC BY-NC-ND or impose embargoes). If unsure, the arXiv perpetual non-exclusive license keeps your options widest; CC BY maximizes reuse and is what most ML venues expect. (Same source.)
- An industry author should also confirm internally that they have "legal authority to grant the selected license" — i.e., that the employer's IP policy permits the release. Moderators ask authors to confirm this and it is a stated ground for removal. ([arXiv moderation](https://info.arxiv.org/help/moderation/index.html))

### Step 6: Timing and the announcement cycle

All times are US Eastern. Submissions received by **14:00 ET** on a weekday are "generally made available at 20:00 (Eastern)" that day, per the schedule:

| Received | Announced |
|---|---|
| Mon 14:00 – Tue 14:00 | Tue 20:00 |
| Tue 14:00 – Wed 14:00 | Wed 20:00 |
| Wed 14:00 – Thu 14:00 | Thu 20:00 |
| Thu 14:00 – Fri 14:00 | Sun 20:00 |
| Fri 14:00 – Mon 14:00 | Mon 20:00 |

No announcements Friday or Saturday. Edits made before the 14:00 cutoff do not delay announcement or create a new version. arXiv's stated caveat: "Quality assurance checks can take between one to four days to resolve, sometimes longer." Identifiers "cannot be back-dated," so a paper held across a month boundary gets the later month's ID. 2026 deferral dates still ahead as of this report: September 7, November 26, December 25, 29, and 31. ([Availability](https://info.arxiv.org/help/availability.html))

For August 2026 specifically: there are no arXiv holidays in August; the next deferral is Labor Day, September 7. A submission Monday–Thursday before 14:00 ET that clears moderation will be visible that evening; a Friday submission waits until Sunday night.

### Step 7: What happens after you click Submit

Submission statuses, from arXiv's status page:

- **Incomplete** — editable; deleted after 14 days of inactivity (any edit resets the clock).
- **Processing** — brief automated analysis; no editing.
- **Submitted** — queued for the next announcement; you may **Unsubmit** to fix something before it goes public, with no new version created.
- **On hold** — flagged by automated or human checks. "Editors contact authors via email if action is needed." Held submissions "don't expire." The one instruction arXiv emphasizes: "do not make a duplicate submission while your work is on hold," which causes further delay. ([Status help](https://info.arxiv.org/help/submit_status.html))

Realistic expectations for a first-time author: the first submission from a new account is more likely than average to be held for a human look. arXiv says holds are usually "relatively short"; the empirical data says the median is one working day even in CS, with a long tail. Plan a buffer of 1–2 weeks ahead of any date you have promised the paper to someone, and longer if your category is a general one. ([fi-le.net](https://fi-le.net/arxiv/))

### Step 8: If it is held, reclassified, or declined

- Correspondence comes by email from arXiv moderation; reply through the same thread or the user support portal. Do not contact moderators directly — appeals "exclusively through arXiv's user support portal."
- An appeal must include the submission/arXiv identifier, prior correspondence, "a detailed description of the research content of your article, and how the content of your paper directly applies to your requested category," and, for declined papers, the PDF.
- Timeline: most decisions within two weeks; ask for a status update after four. Appellate decisions are "final," and arXiv states that "detailed feedback about moderation decisions or appeals will not be provided." Procedural (not content) concerns can be escalated to a Section Chair, but "it is highly unlikely that a section chair will override a moderator on a decision related to the content of an article."
- In some cases arXiv will require acceptance at a conventional journal before reconsidering. ([Appeals](https://info.arxiv.org/help/moderation/appeals.html))

Authors' accounts of the process (n-Category Café, ResearchGate, astro.multivax) describe it as opaque and occasionally slow; holds of months are documented in edge cases. The countermeasure is prevention: correct category, conventional structure, clear research contribution, real affiliation, and TeX source.

### Step 9: After announcement

- To fix errors, **replace** (new version) rather than submit anew. Each version is separately licensed and timestamped; v1 stays visible forever. Withdrawal is possible but leaves the earlier versions accessible; arXiv does not delete papers. ([Submit help](https://info.arxiv.org/help/submit/index.html))
- When the paper is later published, add the journal reference and DOI to the metadata; this is free and does not create a version.
- Link the paper to your ORCID; claim it on Google Scholar and Semantic Scholar. ([Solo researcher guide](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv))

### Fallbacks if endorsement fails

If no endorser materializes, the options raised in the sources are: Zenodo (instant DOI, no gatekeeping, lower prestige; HN commenters were skeptical of its signal value), SSRN, TechRxiv (IEEE), OpenReview, or direct submission to a conference or journal — several commenters noted that in many fields "uploading your PDF directly to a journal's submission system is standard practice" and arXiv is not a prerequisite. The solo-researcher guide's sequence is Zenodo first for timestamped priority, then continue pursuing arXiv endorsement in parallel. ([HN thread](https://news.ycombinator.com/item?id=46243256); [Solo researcher guide](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv))

### Institutional context in 2026

arXiv spun out of Cornell University on July 1, 2026 to become an independent nonprofit, appointed its first CEO in March 2026, and passed three million articles. None of these changes altered submission rules, but they explain the tone of the recent policy posts: the organization is scaling moderation under volume pressure and is shifting gatekeeping from automated heuristics (email domains) to community vouching (personal endorsement) and external refereeing (for surveys). ([arXiv blog 2026 index](https://blog.arxiv.org/2026/))

## Analysis

Two forces define the 2026 experience for an industry author, and they pull in opposite directions.

The first is that **credentials-by-proxy are gone.** A `.edu` address used to be a skeleton key; now it is merely one half of one path. This flattens the field somewhat — the industry author and the new grad student are in the same boat unless the student has co-authored before — but it moves the decisive step out of the website and into a human relationship. The endorsement request is effectively a micro-referral, and it behaves like one: it succeeds when there is a warm connection and a readable draft, and it fails when it arrives cold and empty-handed. Budget for this as a social task with lead time, not as a form to fill in.

The second is that **moderators are triaging harder on content type and category fit**, because LLM-generated surveys and misrouted submissions consumed the volunteer bandwidth. The rules themselves did not change (surveys were never an accepted type), but enforcement did. The observable consequence is a fat tail of hold times concentrated in general categories and in anything that reads like commentary rather than research. A paper with a concrete artifact, a measured result, and a specific category is largely insulated from this.

Everything else — TeX source, license irrevocability, the 14:00 ET cutoff, the no-duplicates rule while on hold, the appeals-only-via-portal rule — is unchanged from prior years and is well documented; the failure modes there are mechanical and avoidable.

### Application to the popsim paper in this repository

The paper at `docs/paper/popsim.tex` is titled "popsim: Reproducing Elements of Billion-Agent Social Simulators," with authors Micah Stubbs (CaseMirror Research, `micah@casemirror.ai`) and Yvonne Chen (no listed affiliation). Observations against the findings above:

1. **Content type is favorable.** A reproduction of a published system with measurements is a research article, not a survey or position paper, so the October 2025 CS restriction does not apply. The abstract should lead with what was built and what was measured, so a moderator does not mistake it for a commentary on the billion-agent-simulator literature.
2. **Category choice will determine hold risk.** Candidate primaries are cs.MA (Multiagent Systems), cs.SI (Social and Information Networks), cs.AI, or physics.soc-ph, with cross-lists as appropriate. Avoid cs.CY as primary: it is the slowest CS category in the delay data and is the default landing spot for reclassified "society" papers. cs.MA is specific and well-moderated. Physics cross-lists may require endorsement in a separate domain.
3. **Endorsement is the critical path.** Neither author has an academic email, so Path 1 is closed. Start the personal-endorsement outreach now: the most natural targets are authors of the simulators the paper reproduces (they are the people most likely to care that their system was reproduced, and to be eligible endorsers in the CS domain). Check eligibility via "Which authors of this paper are endorsers?" on each candidate's abstract page, write to one or two with the draft PDF attached, and wait for a reply before contacting others. If either author has a former colleague or collaborator who is an active arXiv CS author, that is an even better first ask.
4. **Affiliation fields.** "CaseMirror Research" is a legitimate current affiliation and should be kept; the second author's empty affiliation line is fine (arXiv does not require one) but "Independent Researcher" is the conventional fill if one is desired. Both authors should create ORCIDs and use the exact name form that appears in the PDF.
5. **TeX hygiene.** The paper uses the custom `\paperurl` / `\ecite` / `\reftitle` macros and `hyperref` with `hidelinks`; these compile under standard TeX Live but should be tested in a clean environment before upload. Submit the source, `.bbl`, and figures; the existing link-regression test (`scripts/test_paper_links.py`) can be rerun against arXiv's compiled PDF to confirm the Easter-egg hyperlinks survived. The grep for generative-AI terms in the `.tex` returns hits (14), so a one-sentence tool-use disclosure in the acknowledgments is appropriate if LLMs contributed to text or code.
6. **License.** CC BY 4.0 is the norm for ML/MAS work and maximizes reuse; confirm CaseMirror has no objection and that any venue you may later target accepts CC BY preprints. Remember it cannot be changed for v1.
7. **Timing.** Submit Monday–Thursday before 14:00 ET; no August holidays. Treat the first announcement date as "sometime in the next one to ten working days," not "tonight."

## Recommendations

A prioritized punch list, phrased so each item stands alone:

1. **Create ORCID iDs for both authors and register one arXiv account each** under the real names used in the PDF, with current affiliations (CaseMirror Research; blank or "Independent Researcher"). Link ORCID to the arXiv account.
2. **Decide the primary category (recommend cs.MA) and cross-lists** before drafting the endorsement request, since endorsement is scoped to the domain of that category.
3. **Begin personal-endorsement outreach immediately.** Shortlist three to five eligible endorsers (authors of the reproduced systems and any personal contacts active on arXiv CS), verify eligibility via the abstract-page "endorsers" link, and email one or two with the draft PDF and the six-character code. Do not mass-email; do not re-ping the same person.
4. **Make the abstract and introduction unmistakably a research contribution**: system built, experiments run, numbers reported, code link in the comments field. This is the cheapest insurance against a content-type hold.
5. **Add a generative-AI tool-use disclosure** (one sentence, acknowledgments) if applicable, and confirm with CaseMirror that the company authorizes release under the chosen license.
6. **Choose CC BY 4.0 unless a target venue forbids it**; record the decision, since it is irrevocable per version.
7. **Do a clean-room LaTeX build** (fresh TeX Live, no shell-escape, `.bbl` included, arXiv-legal filenames) and check the PDF; then upload source, not PDF.
8. **Submit Monday–Thursday before 14:00 ET**, leaving at least two weeks of slack before any external deadline. If held, wait for moderator email; never submit a duplicate.
9. **If declined or reclassified**, appeal through the support portal with the identifier, the PDF, and a category-fit argument; expect roughly two weeks; accept that the appellate decision is final.
10. **In parallel, post to Zenodo for a timestamped DOI** if priority matters and endorsement is taking longer than a couple of weeks; it does not preclude a later arXiv submission.

## Sources

- [arXiv: Endorsement](https://info.arxiv.org/help/endorsement.html) — endorsement mechanics, eligibility window, etiquette rules.
- [arXiv blog, Jan 21 2026: Updated endorsement policy](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/) — end of email-only auto-endorsement; two-path model; staff cannot waive.
- [arXiv blog, Dec 10 2025: Updated endorsement policy for Mathematics](https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/) — pilot of the same change; detailed author scenarios.
- [arXiv blog, Oct 31 2025: Review articles and position papers in CS](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/) — peer-review prerequisite, DOI metadata, workshop exclusion, appeal path.
- [arXiv: Content moderation](https://info.arxiv.org/help/moderation/index.html) — what moderators check, grounds for decline, AI-tool disclosure, three-per-day guidance.
- [arXiv: Appealing a moderation decision](https://info.arxiv.org/help/moderation/appeals.html) — portal-only appeals, required contents, two/four-week timelines, finality.
- [arXiv: Submission status](https://info.arxiv.org/help/submit_status.html) — status definitions, 14-day expiry, no-duplicates rule.
- [arXiv: Submit overview](https://info.arxiv.org/help/submit/index.html) — format preferences, TeX-source requirement, filename rules, unsubmit and replace.
- [arXiv: Why submit TeX source](https://info.arxiv.org/help/faq/whytex.html) — rationale for refusing TeX-derived PDFs.
- [arXiv: Availability and announcement schedule](https://info.arxiv.org/help/availability.html) — 14:00 ET cutoff table, 2026 holiday deferrals, 1–4 day QA caveat.
- [arXiv: License and copyright](https://info.arxiv.org/help/license/index.html) — license menu, irrevocability, journal-policy caution.
- [arXiv: Identity, affiliation, and registration](https://info.arxiv.org/help/policies/identity_and_affiliation.html) — one account, current affiliation, ORCID recommendation, misrepresentation penalty.
- [arXiv blog: 2026 index](https://blog.arxiv.org/2026/) — nonprofit spin-out, CEO appointment, 3M articles, Juneteenth schedule note.
- [fi-le.net: Counting arXiv delays (July 2026)](https://fi-le.net/arxiv/) — empirical delay distribution across 63,847 papers; per-category table; cs.CY/cs.OH tail.
- [Hacker News: ArXiv endorsement as independent researcher](https://news.ycombinator.com/item?id=46243256) — first-hand tactics (cite-and-ask, workshop contacts), alternatives, arXiv-is-not-peer-review.
- [Learned Geek: A solo researcher's guide to publishing on arXiv](https://learnedgeek.com/Blog/Post/solo-researcher-guide-arxiv) — ORCID-first sequence, Zenodo fallback, related-work emphasis.
- [Stanford Digital Repository: arXiv policy change impacts CS authors](https://sdr.library.stanford.edu/news/arxiv-policy-change-impacts-computer-science-authors) — library summary of the CS survey rule.
- [404 Media: arXiv changes rules after AI-generated paper spam](https://www.404media.co/arxiv-changes-rules-after-getting-spammed-with-ai-generated-research-papers/) — press context for the CS change.
- [CASRAI: arXiv endorsement](https://casrai.org/dictionary/term/arxiv-endorsement-system) — secondary summary of endorser eligibility.
- [n-Category Café: Submission to arXiv (2022)](https://golem.ph.utexas.edu/category/2022/02/submission_to_arxiv.html) and [Azimuth mirror](https://johncarlosbaez.wordpress.com/2022/02/04/submission-to-arxiv/) — documented reclassification-without-notice cases and credibility concerns.
- [Hugging Face forum: endorsement request example](https://discuss.huggingface.co/t/seeking-arxiv-cs-ai-endorsement-independent-researcher-preprint-on-emergent-identities-in-llms/168007) — illustrates the public cold-request pattern.
