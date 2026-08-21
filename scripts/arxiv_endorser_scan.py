#!/usr/bin/env python3
"""Cross-reference contact names against arXiv to find potential endorsers.

Input: TSV lines `name<TAB>email` on stdin (or a file). For each name, query
the arXiv API for papers by that author in the endorsement-eligible window
(submitted between 3 months and 5 years ago) and report hits, with category
counts. arXiv endorsement eligibility is per "endorsement domain"; this
script reports the raw category mix so a human can judge cs.* coverage.

Usage:
  python3 scripts/arxiv_endorser_scan.py candidates.tsv [--min 1] [--cs-only]

Rate limit: arXiv asks for ~1 request / 3 s. Script sleeps accordingly.
"""
import sys, time, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
now = datetime.now(timezone.utc)
LO, HI = now - timedelta(days=5 * 365), now - timedelta(days=90)

def query(name):
    # au: search needs surname first for best recall; try "Last, First" form
    parts = name.split()
    if len(parts) < 2:
        return []
    last, first = parts[-1], parts[0]
    q = f'au:"{last}, {first}" OR au:"{first} {last}"'
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "max_results": 50, "sortBy": "submittedDate", "sortOrder": "descending"})
    req = urllib.request.Request(url, headers={"User-Agent": "popsim-endorser-scan/0.1 (mailto:hi@micah.fyi)"})
    xml = urllib.request.urlopen(req, timeout=60).read()
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", NS):
        pub = datetime.fromisoformat(e.findtext("a:published", "", NS).replace("Z", "+00:00"))
        authors = [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)]
        # exact-ish author match: same first+last tokens (arXiv au: is fuzzy)
        if not any(re.search(rf"\b{re.escape(first)}\b.*\b{re.escape(last)}\b", a, re.I) for a in authors):
            continue
        cats = [c.get("term") for c in e.findall("a:category", NS)]
        out.append({
            "id": e.findtext("a:id", "", NS).split("/abs/")[-1],
            "title": " ".join(e.findtext("a:title", "", NS).split()),
            "published": pub.date().isoformat(),
            "eligible": LO <= pub <= HI,
            "cats": cats,
            "n_authors": len(authors),
        })
    return out

def main():
    path = sys.argv[1]
    cs_only = "--cs-only" in sys.argv
    rows = [l.rstrip("\n").split("\t") for l in open(path) if l.strip() and not l.startswith("#")]
    for row in rows:
        name, email = row[0].strip(), (row[1] if len(row) > 1 else "")
        if not name:
            continue
        try:
            papers = query(name)
        except Exception as ex:
            print(f"{name}\t{email}\tERROR {ex}", flush=True); time.sleep(6); continue
        elig = [p for p in papers if p["eligible"]]
        cs_elig = [p for p in elig if any(c.startswith("cs.") for c in p["cats"])]
        if cs_only and not cs_elig:
            time.sleep(6); continue
        print(f"{name}\t{email}\ttotal={len(papers)}\teligible={len(elig)}\tcs_eligible={len(cs_elig)}", flush=True)
        for p in elig[:6]:
            print(f"\t{p['id']}\t{p['published']}\t{','.join(p['cats'][:3])}\t{p['title'][:90]}", flush=True)
        time.sleep(6)

if __name__ == "__main__":
    main()
