#!/usr/bin/env python3
"""Filter an X/Twitter follower dump (Apify kaitoeasyapi format) for accounts
with academic / research-lab affiliations, and emit a candidate TSV for
scripts/arxiv_endorser_scan.py.

Usage:
  python3 scripts/x_followers_academic.py followers.json > candidates.tsv

Scoring: each signal adds points; accounts with score >= MIN are emitted,
sorted by score desc. Signals are matched in bio + location + url +
expanded urls. Tune REGEXES as needed.
"""
import json, re, sys, html

MIN = 2
SIGNALS = [
    (4, r"\b(professor|prof\.|assistant prof|associate prof|faculty|lecturer|postdoc|post-doc|postdoctoral)\b"),
    (3, r"\b(phd|ph\.d|dphil|doctoral|grad student|graduate student|phd student|phd candidate)\b"),
    (3, r"\b(research scientist|researcher|research fellow|scientist|principal investigator)\b"),
    (3, r"\.edu\b|\.ac\.(uk|jp|il|in|kr|nz|za)\b|\.edu\.(au|cn|sg|hk|tw)\b"),
    (3, r"\b(deepmind|openai|anthropic|fair|meta ai|google research|google brain|microsoft research|msr|allen institute|ai2|nvidia research|mila|vector institute|santa fe institute|sfi)\b"),
    (2, r"\b(university|univ\.|universit|institute of technology|college|polytechnic|école|eth zurich|epfl|mit|caltech|stanford|berkeley|cmu|carnegie mellon|oxford|cambridge|harvard|princeton|yale|columbia|cornell|ucl|imperial|tsinghua|peking|kaist|nus|ntu|toronto|mcgill|ubc|georgia tech|gatech|uw|umich|uiuc|nyu|ucla|ucsd|ucsb|uc davis|utexas|ut austin|wisc|purdue|jhu|johns hopkins|duke|northwestern|brown|upenn|usc|rice|tufts|dartmouth|umass|rutgers|vanderbilt|emory|boston university|northeastern)\b"),
    (2, r"\b(lab|laboratory|research group|research lab|computational|ml research|ai research)\b"),
    (2, r"\b(arxiv|neurips|icml|iclr|acl|emnlp|cvpr|aaai|aamas|kdd|www|chi|ieee|acm)\b"),
    (1, r"\b(science|scientific|academic|academia|research)\b"),
]
SIG = [(w, re.compile(p, re.I)) for w, p in SIGNALS]

def text_of(u):
    parts = [u.get("name") or "", u.get("description") or "", u.get("location") or "", u.get("url") or ""]
    ent = u.get("entities") or {}
    for k in ("url", "description"):
        for x in (ent.get(k) or {}).get("urls", []) or []:
            parts.append(x.get("expanded_url") or x.get("display_url") or "")
    return html.unescape(" ".join(parts))

def main():
    data = json.load(open(sys.argv[1]))
    rows = []
    seen = set()
    for u in data:
        sn = u.get("screen_name")
        if not sn or sn in seen:
            continue
        seen.add(sn)
        t = text_of(u)
        score, hits = 0, []
        for w, rx in SIG:
            m = rx.search(t)
            if m:
                score += w; hits.append(m.group(0).lower())
        if score >= MIN:
            rows.append((score, u.get("name") or "", sn, u.get("followers_count", 0), (u.get("description") or "").replace("\n", " ")[:140], ";".join(hits)))
    rows.sort(key=lambda r: (-r[0], -r[3]))
    print(f"# {len(rows)} of {len(seen)} followers flagged academic (score>={MIN})", file=sys.stderr)
    print("name\thandle\tscore\tfollowers\tbio\thits")
    for s, n, sn, fc, bio, hits in rows:
        print(f"{n}\t@{sn}\t{s}\t{fc}\t{bio}\t{hits}")

if __name__ == "__main__":
    main()
