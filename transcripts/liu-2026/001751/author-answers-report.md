No question was ever asked about this attempt, so there was nothing to re-run and I changed no claim.

**Questions:** `questions/001751.yaml` doesn't exist. It isn't on this branch, on `origin/attempt/001751`, or anywhere in the git history. My first author run listed "Questions to a reader: none". The open questions from that run are for the paper's authors and are recorded as `methods_unavailable` findings in the attempt record:
- what rule decides a connection, and which pairs and cells make up the paper's 1,292 and 377;
- which time window and voltage steps give the Na+ current peak.

The answer run (`transcripts/001751/answer-report.md`) found nothing to answer and changed nothing in `claims/001751/` or `questions/`. Between my author run and now, no file in `claims/`, `entries/` or `attempts/` has changed.

**Effect on claims:** none. No claim had its statement, expected values or criterion amended, so every outcome stays as the first author run recorded it, with no earlier outcome to compare against. The main ones on this dataset:
- **Reproduced:** code-table-link, fig5-in-to-ven-absent, fig5fg-example-slice.
- **Not reproduced:** fig5d-connectivity-totals (26 connections against 31; 295 cells against 377), fig5-pc-to-pc, fig5-ven-outputs-absent.
- **Partially reproduced:** fig5-pc-to-ven, fig5-pc-in, fig5i-ven-sparse-local-connectivity.
- **Blocked:** fig5-pair-distances (data missing) and fig5-pc-rate-comparable-primate (methods underspecified).

The outcomes for claims tested on data outside this dataset are also unchanged. With nothing re-run, I didn't edit the notebook, the conclusions, the attempt record or any claim's notes.

**Entry checks:**
- `entry.py lock` rewrote `requirements.lock.txt`, and git shows no change to it.
- `entry.py all` reports 0 errors, and the notebook ran in 165 s.
- `entry.py handover` built the package in `executed/001751-liu-2026/handover/`.
- Nothing is committed or pushed.

The untracked dotfiles in the repository root, and a `scripts` entry that is a character device, are left over from the environment; I left them alone.
