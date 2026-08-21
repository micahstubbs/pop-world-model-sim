# Paper citation URL registry refactor and author affiliations

## Summary
Added a rendering regression test for the paper, refactored the easter-egg citation macros so each source URL is declared once, and updated the author block. Beads: pop-world-model-sim-hq4.

## Completed Work
- `scripts/test_paper_links.py` (87ae191): builds `popsim.tex` in a scratch dir and compares all PDF URI link annotations (page, URL, rect) plus `pdftotext` output against `docs/paper/snapshots/`. Mutation-checked: a wrong URL fails the test.
- Refactor: `\paperurl{key}{url}` registry in the preamble; `\ecite{key}` and `\reftitle{key}{Title}` look the URL up. Test passed with byte-identical link set and text before the author edit.
- Author block: "San Francisco, CA" removed (location is implied by the Luma link in acknowledgments); Micah → "CaseMirror Research"; Yvonne → blank affiliation line (`\mbox{}`) reserved for later.
- PDF rebuilt, snapshots updated, CLAUDE.md paper convention updated. Visually verified title block and references page via pdftoppm.

## Next Session Context
Run `python3 scripts/test_paper_links.py` after any paper edit; `--update` after intentional changes plus a PDF rebuild.

## Addendum (session close)
- 59b0d1f: both author affiliation lines dropped (CaseMirror Research removed too); affiliation implied by email. PDF rebuilt, snapshots updated, header verified.
- Latest PDF emailed to hi@micah.fyi via Resend (id c37bd56a-b97f-4083-9c7e-0e6c0cc015c2).
- /close: LESSONS.md created (3 lessons); new skills `apc`/`audit-pr-commits` and `plt`/`pdf-link-snapshot-test`; `sfr` skill and global CLAUDE.md updated.
