#!/usr/bin/env python3
"""Scan Google Takeout vCards for .edu (and .ac.*) email addresses.

Prints TSV: name<TAB>email<TAB>domain, deduped by email, excluding bulk
roster domains (e.g. utulsa.edu, listed in EXCLUDE) that are not personal
contacts.
"""
import glob, re, sys, collections

ROOT = "/home/m/wk/contacts/data/google-takeout/Takeout/Contacts"
EXCLUDE = {"utulsa.edu"}
pat_edu = re.compile(r"[\w.+-]+@([\w-]+\.)*(edu|ac\.[a-z]{2}|edu\.[a-z]{2})$", re.I)

seen = {}
for path in glob.glob(f"{ROOT}/**/*.vcf", recursive=True):
    name, emails = None, []
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if line.startswith("BEGIN:VCARD"):
            name, emails = None, []
        elif line.startswith("FN:"):
            name = line[3:]
        elif line.upper().startswith("EMAIL"):
            emails.append(line.split(":", 1)[-1].strip())
        elif line.startswith("END:VCARD"):
            for e in emails:
                e = e.lower()
                if pat_edu.match(e) and e.split("@")[1] not in EXCLUDE:
                    seen.setdefault(e, name or "")
by_domain = collections.Counter(e.split("@")[1] for e in seen)
for e, n in sorted(seen.items(), key=lambda kv: (kv[0].split("@")[1], kv[1])):
    print(f"{n}\t{e}\t{e.split('@')[1]}")
print(f"\n# {len(seen)} edu emails across {len(by_domain)} domains", file=sys.stderr)
print("# top domains:", by_domain.most_common(15), file=sys.stderr)
