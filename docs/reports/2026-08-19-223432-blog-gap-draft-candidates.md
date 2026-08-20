# Blog gap-filler: draft candidates for 2026-02-26 → 2026-08-19

**Blog:** micahstubbs.ai ("Micah Stubbs' Weblog")
**The gap:** previous post `Cleaning up taskmaster's terminal output` (2026-02-25) → latest post `Simulating 6,245 real people on one machine` (2026-08-20). ~25 weeks with nothing published.
**Goal:** find existing drafts/reports that can be backdated into the gap, with each date grounded in evidence.

## Executive summary

The blog database holds only **three** drafts, and only **one** of them (entanglement-swap, 2026-07-24) actually falls inside the gap. The real supply is elsewhere: `docs/reports/` and `docs/investigations/` across ~40 projects contain a large number of genuine debugging-narrative and measured-finding writeups from exactly this window, most of them already written in a publishable voice.

**10 recommended candidates** below. Publishing all ten leaves **no gap longer than ~4.7 weeks** (the widest remaining stretch is 2026-03-02 → 2026-04-04).

Sources scanned: the blog DB via `blog list --drafts`; `~/wk/*/docs/blog/`, `docs/blog-posts/`, `~/wk/sites/homepage/docs/`; all `*draft*`/`*post*`/`*blog*`-named markdown under `~/wk/*/docs`; 185 files in `~/wk/*/docs/reports` + `docs/investigations` with mtime in the window; and `~/wk/*/docs/*.md` top level. `~/posts/` does not exist. Worktrees, node_modules, .venv, and archive dirs excluded.

---

## Ranked candidates

### 1. Entanglement Swap: a reading group on Shakespeare, quantum physics, and cognitive offloading
- **Source:** blog DB slug `entanglement-swap-a-reading-group-on-shakespeare-quantum-physics` (mirror at `/home/m/wk/entanglement-swap/docs/blog-post-entanglement-swap.md`)
- **Proposed date:** **2026-07-24**
- **Evidence:** blog draft created 2026-07-24 18:11 UTC; git commit "Draft Entanglement Swap blog post" 2026-07-24 11:15 -0700. Body opens "Yesterday afternoon…" and calls the event a Thursday — 2026-07-23 was a Thursday, 2026-07-24 a Friday. Date is pinned exactly.
- **Readiness:** **publish-as-is** (only fix: the `/static/entanglement-swap/*.pdf` asset paths must exist, and "posted this month" re the Fields & Levin preprint is now stale)
- **Pitch:** Ten people in Golden Gate Park used an afternoon of argument as the joint measurement that left a 2016 Shakespeare-and-Lacan thesis entangled with a 2026 biophysics preprint — and both texts independently landed on metaphor as the mechanism by which understanding crosses a boundary.
- **Words:** ~1,010

### 2. Where the Reading Pipeline Spends Its Time: a measured optimization report
- **Source:** `/home/m/wk/dramatic-academic-paper-reader/docs/reports/optimization-opportunities-report.md`
- **Proposed date:** **2026-07-10**
- **Evidence:** git-added 2026-07-10; mtime 2026-07-10 08:14
- **Readiness:** **publish-as-is** — already written as an essay with a three-part thesis and the best title in the whole corpus
- **Pitch:** Measuring where a text-to-audio pipeline actually spends its time shows the JSON store is the scaling cliff (every cookie-bearing request parses the whole thing, transcripts are 96% of its bytes), the Rust port makes serving 8-16x faster without touching the real bottleneck, and everything the user actually waits on is vendor TTS.
- **Words:** 1,772

### 3. The FUSE mount that made every disk tool lie
- **Source:** `/home/m/wk/casemirror/docs/investigations/2026-04-28-013052-fuse-mnt-shadow-investigation.md`
- **Proposed date:** **2026-04-28**
- **Evidence:** git-added 2026-04-28; timestamp encoded in filename (01:30:52); mtime 2026-04-28 03:16
- **Readiness:** **light edit** (add a lede, trim machine-specific paths)
- **Pitch:** A FUSE-mounted NTFS volume on `/mnt` shadowed the real ext4 mounts, so `df`, `stat -f`, `lsblk` and `findmnt` all agreed the disk had 29 GB free — until `tune2fs -l` on the block device reported 4.10 TB with 420 GB free, by which point the wrong number had already convinced a subagent that a bulk import was infeasible.
- **Words:** 1,323

### 4. Kitty breaks sudo, and `sudoc` fixes it
- **Source:** `/home/m/wk/casemirror/docs/reports/sudo-vs-sudoc.md`
- **Proposed date:** **2026-03-02**
- **Evidence:** git-added 2026-03-02; mtime 2026-03-02 23:39
- **Readiness:** **light edit** (short — publish as a ~400-word TIL note)
- **Pitch:** Kitty sets `TERMINFO` and `TERM=xterm-kitty` in a way that collides with sudo's environment security policy, so `sudo` fails in confusing ways on an otherwise healthy box; a three-line `env -i` wrapper makes it work again.
- **Words:** 496
- **Why this slot:** the earliest in-gap dated artifact found — it closes the gap within a week of the 2026-02-25 post.

### 5. Forensics on a dead 3TB drive: the kernel driver did it
- **Source:** `/home/m/wk/home-scripts/docs/investigations/toshiba-3tb-ntfs-corruption-investigation.md`
- **Proposed date:** **2026-08-15**
- **Evidence:** git-added 2026-08-15; mtime 2026-08-15 13:29
- **Readiness:** **light edit** (3,634 words — trim the recovery-plan appendix, or split into two posts)
- **Pitch:** The Linux `ntfs3` kernel driver wrote self-overlapping cluster runlists during a VM-backup `dd` job and destroyed the NTFS primary boot sector; read-only forensics across both `$MFT` extents proved 55,553 records were intact, named the culprit file, and pinned its two-minute write window — all without writing a single byte back to the patient.
- **Words:** 3,634
- **Why this slot:** the strongest single story in the set, and it lands five days before the 2026-08-20 post, closing the tail of the gap.

### 6. undici works in your shell and fails in cron
- **Source:** `/home/m/wk/casemirror/docs/reports/slip-monitor-outage-investigation.md`
- **Proposed date:** **2026-04-04**
- **Evidence:** git-added 2026-04-04; mtime 2026-04-04 15:22; content describes an outage running 2026-03-31 → 2026-04-03
- **Readiness:** **light edit**
- **Pitch:** A court-opinion monitor went dark for five days because Node's native `fetch` (undici) failed under cron while the exact same URLs worked from curl and from an interactive Node session — the curl-fallback cascade recovered 53 missed opinions.
- **Words:** 782

### 7. The protocol, not the cable, is the bottleneck: adb vs MTP
- **Source:** `/home/m/wk/home-scripts/docs/adb-vs-rcopy-import-tradeoffs.md`
- **Proposed date:** **2026-06-09**
- **Evidence:** git-added 2026-06-09 12:51 -0700; content cites measurements from "the 2026-06-09 import (331 files, 275.8 GB)"
- **Readiness:** **light edit**
- **Pitch:** Pulling 275.8 GB off a Samsung S22 takes 3-5 hours over gvfs MTP and about an hour over adb, on the identical USB 3 cable — MTP dies by a thousand FUSE round-trips while adb just streams, and the destination NVMe was never close to being the limit.
- **Words:** 1,382

### 8. Cross-compiling for macOS from Linux: why it doesn't work
- **Source:** `/home/m/wk/beads_rust/docs/cross-compiling-macos.md`
- **Proposed date:** **2026-07-06**
- **Evidence:** git-added 2026-07-06 16:26 -0700; the date is also in the document's own title
- **Readiness:** **light edit** (short, self-contained negative result)
- **Pitch:** zig + cargo-zigbuild handles most Rust cross-compiles to `aarch64-apple-darwin`, but the dependency chain `self_update → reqwest → rustls → aws-lc-rs → aws-lc-sys` reaches a C build that needs `CoreServices/CoreServices.h`, and there is no fixing that without Apple SDK headers or dropping the crypto backend.
- **Words:** 413

### 9. Nightcore is a resample, not a time-stretch — and it lands on Alan Walker's tempo
- **Source:** `/home/m/wk/nightcorify/docs/reports/nightcore-and-alan-walker-tempo-analysis.md`
- **Proposed date:** **2026-06-08**
- **Evidence:** git-added 2026-06-08; mtime 2026-06-08 20:53
- **Readiness:** **light edit**
- **Pitch:** Nightcore is a pure resample — 125% speed, +3.86 semitones, no time-stretching — and because Alan Walker's catalogue is bimodal at ~86-100 BPM and ~128-131 BPM, the nightcore lift of a 100 BPM source arrives almost exactly at his club tempo by pure coincidence of two unrelated goals.
- **Words:** 1,032
- **Why this slot:** a deliberate change of pace between two systems-debugging posts.

### 10. Why Ubuntu's default file manager is slow
- **Source:** `/home/m/wk/memex/docs/reports/2026-05-09-121929-nautilus-slow-fix-or-replace-with-thunar.md`
- **Proposed date:** **2026-05-09**
- **Evidence:** git-added 2026-05-09; timestamp in filename (12:19:29); mtime 2026-05-09 12:22
- **Readiness:** **light-to-moderate edit** (3,331 words — trim the local-machine sections; broad-appeal content is maybe 1,500 of them)
- **Pitch:** Nautilus slowness is not one bug but a stack of them, some of which GNOME's own developers describe as needing "fundamental (complex) changes" — here are the five `gsettings` that recover most of it, and the case for just switching to Thunar.
- **Words:** 3,331
- **Why this slot:** the only strong candidate anywhere in May; it is load-bearing for the spread.

---

## Coverage / spread analysis

Proposed publication dates, in order:

| Date | Post | Days since previous |
|---|---|---|
| 2026-02-25 | *(existing)* Cleaning up taskmaster's terminal output | — |
| 2026-03-02 | #4 Kitty breaks sudo | 5 |
| 2026-04-04 | #6 undici under cron | 33 |
| 2026-04-28 | #3 FUSE mount lies | 24 |
| 2026-05-09 | #10 Nautilus slow | 11 |
| 2026-06-08 | #9 Nightcore tempo | 30 |
| 2026-06-09 | #7 adb vs MTP | 1 |
| 2026-07-06 | #8 Cross-compiling macOS | 27 |
| 2026-07-10 | #2 Reading pipeline | 4 |
| 2026-07-24 | #1 Entanglement Swap | 14 |
| 2026-08-15 | #5 Toshiba forensics | 22 |
| 2026-08-20 | *(existing)* Simulating 6,245 real people | 5 |

**Longest remaining gap: 33 days (~4.7 weeks), 2026-03-02 → 2026-04-04.** Mid-March is genuinely thin in the source material; the best filler is alternate A3 below (2026-03-13).

A smaller **five-post** set — #4 (Mar 2), #3 (Apr 28), #7 (Jun 9), #1 (Jul 24), #5 (Aug 15) — leaves a maximum gap of ~8 weeks. Ten posts is what gets it under five weeks.

---

## Alternates (good, but lower priority)

| # | Title / source | Date + evidence | Readiness | Words |
|---|---|---|---|---|
| A1 | SANDWORM_MODE npm supply-chain worm: scanning my own workstation — `/home/m/wk/security/docs/sandworm-mode-detection-report.md` | 2026-03-03 (git commit 09:33; repo created same day) | light edit | 989 |
| A2 | Brave's `super_mac` goes stale after 15 days uptime — `/home/m/wk/home-scripts/docs/reports/2026-03-03-brave-profile-error-root-cause.md` | 2026-03-03 (git-added; mtime is a bulk touch, ignore it) | light edit | 1,788 |
| A3 | Playing a 30-minute WAV through a phone call — `/home/m/wk/phone-agent/docs/audio-playback-extended-30min-analysis.md` | 2026-03-13 (git-added) | needs framing | 1,991 |
| A4 | Two adjacent calls, 121s vs 1s: an ngrok-to-relay WebSocket regression — `/home/m/wk/phone-agent/docs/investigations/silence-immediate-hangup-root-cause.md` | 2026-04-18 (git-added) | light edit | 1,438 |
| A5 | Speaker diarization with the OpenAI Realtime API — `/home/m/wk/memex/docs/diarization-with-openai-realtime-api.md` | 2026-04-18 (git-added) | light edit (researchy) | 2,692 |
| A6 | Large-file upload bugs: reading a 10 GB body into RAM — `/home/m/wk/home-scripts/docs/upload-large-file-bugs-2026-04-24.md` | 2026-04-26 git-added; content dated 2026-04-24 | light edit | 1,596 |
| A7 | Where a published algorithm write-up diverges from its own source — `/home/m/wk/liteparse_rust/docs/investigations/2026-04-28T031247-0700-grid-projection-fidelity-differences.md` | 2026-04-28 (git-added; timestamp in filename) | light edit | 2,783 |
| A8 | Firejail's private `/tmp` hides Brave's singleton socket — `/home/m/wk/home-scripts/docs/investigations/brave-evince-secure-link-handoff.md` | 2026-06-08 (git-added; mtime is a bulk touch) | light edit | 792 |
| A9 | What the logs can't tell you about an 8-day machine crash — `/home/m/wk/scripts/docs/investigations/machine-crash-safeguards.md` | 2026-06-28 (git-added) | needs framing | 1,364 |
| A10 | Node vs Rust with honest methodology disclosure — `/home/m/wk/dramatic-academic-paper-reader/docs/reports/rust-port-vs-node-benchmark.md` | 2026-07-09 (git-added) | light edit | 1,851 |
| A11 | What SCOTUS booklet printing actually costs — `/home/m/wk/dragonfly/docs/reports/2026-07-13-195446-scotus-paid-filing-booklet-cost-analysis.md` | 2026-07-13 (git-added; timestamp in filename) | light edit + genericize personal case details | 2,182 |
| A12 | The Church of Claude: order of evening service — `/home/m/wk/hail-claude/docs/liturgy/church-of-claude-liturgy-draft.md` | 2026-07-19 (git-added) | needs a framing essay wrapped around it | 1,083 |
| A13 | A circuit split is not a prerequisite to cert — `/home/m/wk/dragonfly/docs/reports/granted-cert-petition-circuit-split-classification.md` | 2026-07-25 (git-added) | light edit; own the n=7 sample | 1,103 |
| A14 | The Cloudflare 521 that only hit plain-HTTP visitors — `/home/m/wk/casemirror/docs/investigations/cloudflare-521-http-listener-incident.md` | 2026-07-26 (git-added) | **must scrub a real user's name + email from the header** | 1,252 |

---

## The two out-of-gap blog DB drafts

Both predate the gap. They can either publish at their true dates (immediately before the gap, which does not help the gap itself) or be refreshed and moved into it — but the honest date is the earlier one.

| Slug | True date + evidence | Readiness | Words |
|---|---|---|---|
| `gpu-tui-rebuilding-nvidia-smi-with-auto-refresh-and-thousands-se` | **2026-02-14** — blog draft created 2026-02-15 07:59 UTC = 2026-02-14 23:59 PST; git commit "Add blog post: gpu-tui…" 2026-02-14 23:59 -0800 | publish-as-is | 943 |
| `pre-1964-california-court-opinions-are-all-published-and-your-le` | **2026-02-02** — body carries an explicit `**Date:** 2026-02-02`; blog draft created 2026-02-03; source md git-added 2026-02-02 16:18 | publish-as-is | 676 |

Both are genuinely good (the pre-1964 one is a real historical finding: California had no selective publication before 1964, which is why 80% of 405,718 Court of Appeal opinions show "unknown" status). Recommend publishing both at their true February dates regardless — they are finished work sitting unshipped.

---

## Gaps and caveats

- **mtime is unreliable in `home-scripts`.** A bulk touch on 2026-07-15 04:54 reset mtimes on many files; git `%ai` is authoritative there. Candidates A2 and A8 are affected.
- **Mid-March is genuinely thin.** Only A3 (2026-03-13) sits between 2026-03-03 and 2026-04-04.
- **Privacy screens applied.** Excluded from all recommendations: the `dragonfly` personal-litigation material (except the two generic legal-research pieces, A11/A13), `memex` personal-life research, `background-checker` PII-adjacent work, and vendor contract analyses. A14 carries a specific redaction requirement.
- **Not candidates:** session summaries, LESSONS files, raw audit dumps, status/progress trackers, third-party generated text (the ribbonfarm reading script, the Joy.jl changelog), and the `clipboard-visualizer` drafts (all three copies still contain a live `github.com/yourusername/...` placeholder).
- **Do not re-publish:** `thread-locks-dont-cross-process-boundaries` — already live.
- Blog DB was not modified. This report is read-only research.
