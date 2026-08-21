# LESSONS.md

Append-only log of debugging lessons and non-obvious patterns from this project.

## 2026-08-21T15:45 - Verifying PDF hyperlinks: raw byte grep finds nothing

**Problem**: Auditing whether a LaTeX-built PDF actually contained the `\href` links, `grep -a '/URI' popsim.pdf` returned zero matches even though the links worked.

**Root Cause**: pdflatex (with modern defaults) writes annotations into compressed object streams, so `/URI (...)` never appears as plain bytes in the file.

**Lesson**: Never judge a PDF's link/annotation content from raw bytes. Decompress first.

**Solution**:
```bash
qpdf --qdf --object-streams=disable popsim.pdf - | grep -ao '/URI *([^)]*)' | sort | uniq -c
```
This is now wrapped in `scripts/test_paper_links.py`, which also maps each annotation to its page via the page's `/Annots` array and snapshots `(page, url, rect)`.

**Prevention**: For any "does the PDF contain X metadata" question, use `qpdf --qdf` / `pdfinfo` / `pdftotext`, not grep on the binary.

## 2026-08-21T15:50 - Bash tool cwd stuck after `cd` in a compound command

**Problem**: A command chain starting with `cd docs/paper && ...` left later Bash calls running inside `docs/paper`; a `mkdir -p docs/session-summaries` then created `docs/paper/docs/session-summaries/` and `git add .gitignore` failed with "pathspec did not match".

**Root Cause**: The Bash tool's working directory persists between calls; a `cd` in one call silently changes the base for every following call.

**Lesson**: Treat every Bash call as possibly starting in the last `cd`'d directory.

**Prevention**: Use absolute paths (or `cd /abs/project && ...` as the first token) in every command that touches files; avoid relative `cd` entirely. When a stray directory results, `mv` it into `archive/` — `rmdir` is blocked by the dcg no-delete guard.

## 2026-08-21T15:55 - Snapshot-test a LaTeX refactor on link annotations + text, not on the PDF bytes

**Problem**: Needed to prove a macro refactor (`\ecite{url}{key}` → registry-based `\ecite{key}`) changed nothing in the rendered paper.

**Root Cause**: PDF bytes differ on every build (timestamps, IDs), so byte comparison is useless; but the meaningful invariants — every link's URL, page, and rectangle, plus extracted text — are deterministic across builds.

**Lesson**: Snapshot the *semantic* render (link annotations via qpdf, `pdftotext -layout`) and mutation-check the test (change one URL, confirm failure) before trusting a PASS.

**Prevention**: `python3 scripts/test_paper_links.py` after any paper edit; `--update` only after an intentional content change and a PDF rebuild. Note that a change to the title block shifts every rect on the page, so a rect-only mismatch with an identical URL multiset is expected after header edits.

## Meta-Lessons

- Verify claims about build artifacts with format-aware tools, and verify the verifier with a deliberate mutation before relying on it.
