I rewrote `claims/000061/10.1038-nn.4637.yaml` from the full text, and every quote passes the checker. The checker still exits non-zero on four p-values: the text prints them as "9.70 × 10−9", "8.85x10-05", "7.75x10-05" and "6.45x10-05", forms it doesn't recognise. I checked each against the text by hand and left the checker unchanged.

**Text read.** The version of record (supplied PDF, extracted text): main text, figure legends, Online Methods and reporting summary, plus the Supplementary Information PDF (Supplementary Figs. 1–11, Tables 1–2). Nothing the claims need is missing. The one gap is Supplementary Table 1, which is an image with no numbers in the text, but the counts the claims use are also stated in the Results.

**Code read.** The code the paper links, `buzsakilab/papers`, folder `GGirardeau-BLAHpcInteractions-Package`, commit cdcec89f8d1f. For `SyncHist` I also read FMAToolbox at commit 6bbb3662f7ed.

**Claims.** There are 31 claims: all 31 have quotes, 23 have statistics, all 31 have criteria and 12 have expected values. Six ids are kept because the finding is the same: `hpc-bla-reactivation-post-sleep`, `reactivation-peaks-at-ripples`, `bla-ripple-up-subgroup`, `reactivation-involves-ripple-up-cells`, `aversive-direction-stronger` and `rats-learn-puff-location`. The other 25 are new, covering behaviour, unit counts, sleep firing rates, reactivation decay, the absence of REM reactivation, piriform cortex and central nuclei, within-structure reactivation, downmodulation, pair contributions and gain, the safe trajectory, all cell types, ripple rate, and Fig. 7. The opening comment says what changed and why: the two flagged claims and the other old criteria used agent-chosen measures in place of the paper's own (EV/REV, the Poisson ripple-modulation test and reactivation strength R).

**Details the paper and code leave open, with the readings named:**
- **O1, lap window:** the code picks the track's left limit by hand. Readings: (a) laps the dataset holds; (b) a 150-cm window starting at the smallest run-epoch position; (c) laps between rewards at opposite ends.
- **O2, `poissonTest`:** not in the repository. Readings: tails P(X ≥ n) / P(X ≤ n), or strict tails.
- **O3, bin timestamps:** bin start or centre. I used the standard choice (centre); it can't change an outcome.
- **O4, Fig. 2c cells:** (a) the monosynaptically identified cells, if the dataset marks them; (b) all putative cells of each type.
- **O5, Fig. 1b Bonferroni family size:** (a) all post hoc tests in the panel; (b) uncorrected.
- **O6, Fig. 5a post hoc test:** the Methods say Bonferroni; the legend and the code say Tukey–Kramer. Bonferroni is the main reading (Methods first) and Tukey–Kramer the variant.
- **O7, BLA rate on safe vs air-puff laps:** (a) spike count over lap time; (b) the mean of the position rate curve.
- **Claim-level details:**
  - Habituation: which laps are counted (the Methods, the legend and the code differ). The paper gives no test, so I named readings for "gradually diminished".
  - Supplementary Fig. 9: no test is given; two readings of "did not depend".
  - Fig. 3d comparison: 14 vs 17 piriform sessions; both are shown.
  - Supplementary Fig. 6b: the code's non-significant group is restricted to negative correlations, so it is a variant.

**Paper inconsistencies, recorded in the claims:**
- Fig. 3c prints "z = 0.38" with P = 0.00013 (recorded as printed).
- The text and legend give opposite z signs for the Fig. 5b test (legend z = −3.913 recorded).
- The ripple-rate script calls a right-tailed test, but the printed P is two-sided; the criterion follows the paper.

**Missing for any claim.** Nothing the claims need is missing from the paper.
