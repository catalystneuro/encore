I've done steps 1 to 6 of the Author section for CRCNS ia-1 and run the handover. The entry passes `check` and runs clean in 248 s; nothing is committed. Files written: `entries/crcns-ia-1-eyherabide-2008/` (notebook, `ia1.py`, `entry.yaml`, `README.md`, lock files) and `attempts/crcns-ia-1-eyherabide-2008-01.yaml`. The verifier's package is in `executed/crcns-ia-1-eyherabide-2008/handover/`.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| data-sessions-and-trials | partially reproduced (assumed) |
| table1-sessions-per-protocol | not reproduced |
| firing-rate-uniform | reproduced |
| threshold-population | blocked: data_missing |
| table1-bursting-sessions | not reproduced |
| table1-isolated-spikes | partially reproduced (assumed) |
| table1-burst-length | not reproduced |
| fig5-burst-probability-vs-stimulus | reproduced (assumed) |
| fig3-correlation-shape | reproduced (assumed) |
| method-correlation-error | reproduced (assumed) |
| model-matches-classification | blocked: data_missing |
| fig6-bursts-less-correlated | reproduced (assumed) |
| fig7ab-information-per-burst-increases | partially reproduced (assumed) |
| fig7cd-occurrence-decreases | partially reproduced (assumed) |
| fig7ef-jitter-independent-of-n | reproduced (assumed) |
| fig7gh-information-rate | not reproduced (assumed) |
| direct-method-comparison | partially reproduced (assumed) |
| fig8-nbta-differ | partially reproduced (assumed) |
| fig8-latency-decreases | reproduced (assumed) |
| fig8e-sigma-minimum | not reproduced (assumed) |
| sigma-n-below-sta-sigma | reproduced (assumed) |
| fig9-nbta-not-concatenated-1bta | reproduced (assumed) |
| fig9c-population-nbta | reproduced (assumed) |
| fig10-burst-n-vs-height | not reproduced (assumed) |
| firing-rate-no-effect-on-limit | reproduced (assumed) |
| model-reproduces-coding-trends | blocked: data_missing |

Totals: 11 reproduced, 6 partially reproduced, 6 not reproduced, 3 blocked.

**(2) The dataset**
- **Selection:** The paper's stated selection rule cannot be recovered. Data1 has 150 sessions. The 116 that use the paper's seven protocols come from exactly the paper's 37 cells and 23 recording dates. But the stated rule (trial-to-trial rate SD below 35 Hz) keeps 115 of them, where the paper kept 86. Every session count therefore runs high (60 reference sessions against 43), while the bursting fractions per protocol follow the paper's pattern.
- **Missing data:** Data1 records no thresholds, best frequencies or animals, so the model claims and the threshold claim are blocked.
- **Metadata problems:**
  - 34 sessions use stimuli the paper never mentions, and the descriptor does not describe two of those stimulus types.
  - The descriptor gives 98 to 533 trials per session; the files hold 69 to 503.
  - In three sessions the header intensity differs from `cell.dat` by more than 1 dB (up to 6.6 dB).
  - Six sessions had 450 ms pauses where the paper states 700 ms.
  - Two experiments are missing from `singlecells.txt`.
- **Clock check:** It passes. The spike-triggered stimulus average (STA) peaks a median 5.6 ms before the spike in all 116 sessions, and almost vanishes when the stimulus is shifted by 100 ms.
- **Version:** CRCNS does not version data sets. I pinned the zip by the MD5 in `checksums.md5`; the helper checks the S3 ETag against it before reading.

**Assumptions** (the questions for the paper's authors are in the `methods_unavailable` finding):
- **Burst identification:** I took the first peak as the largest value below 5 ms. The first local maximum lands on noise and leaves only 15 of 115 sessions bursting. With N as the number of trials, no session bursts at all.
- **Correlation-function error:** I left τ = 0 out of the span of the correlation function. The result is then 2.7% against the paper's 3.4%.
- **Figure 9:** I subtracted the mean stimulus before summing the 1-spike burst averages in Eq. 15.
- **Figure 3:** I chose the peak-prominence threshold used to count peaks.
- **Jitter:** I chose how reading (b) groups burst onsets into events.
- **Animals:** I assumed one animal per recording date.

No questions to a reader.

**(3) Where the protocol was unclear or did not fit**
1. "Pin the most recent published version" does not fit an unversioned archive. I recorded `unversioned` and checked the MD5 against the ETag.
2. The protocol does not say whether the author may add a reading the claims file does not list. I added a third reading of σ and N (from paragraph 6) and the exclusion of τ = 0, shown beside the listed readings and marked as assumptions.
3. Many criteria define only "reproduced". I gave "partially" when the effect held and some expected values matched, and "not" otherwise.
4. There is no rule for expected session counts when the dataset keeps more sessions than the paper did. I judged by the criterion and reported the proportions in the notes.
5. It is unclear whether picking one of the claims file's own listed readings counts as an assumption. I marked `assumed` wherever the outcome depends on the burst reading.
6. The data-check examples assume a task with trials and labels. For stimulus-driven data I used the STA against a 100 ms-shifted stimulus as the contrast.

**(4) Runtime and failures**
The work ran from 18:18 to about 19:00 UTC. The notebook takes 248 s from a clean environment. Two development runs failed on bugs that are now fixed (an array size and a plot-range count). Nothing failed in the final run. Some untracked files (dotfiles, `scripts/`) at the repository root were already there and are not mine; I left them alone.
