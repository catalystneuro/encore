# Verifier report, round 2: Wirth et al. 2017 (doi:10.1371/journal.pbio.2001045), CRCNS hc-12 / hc-21

The claims file has 28 claims, and the attempt record has 28 outcomes, one for each. They split as 5 reproduced, 3 partially reproduced, 6 not reproduced and 14 blocked (11 for insufficient metadata, 3 for underspecified methods).

## 1. Outcomes

| Claim | Outcome in the record | Agree? | Note |
|---|---|---|---|
| gaze-anticipates-action | reproduced (assumed) | Yes | The assumption is stated and reasonable. Cell 28 gives the sign from eye velocity during turns, not from eye position, in 40/40 sessions of K and 20/20 of S. See caveat (a) below; it does not change the outcome. |
| gaze-anticipates-landmarks | reproduced (assumed) | Yes, changed from my round-1 partial | The sign now comes from the slow-phase velocity during turns at the centre, which does not use eye position, so the test is no longer circular. Cell 31: K −0.56 SD, p = 6.2e-58, 39/41 sessions; S −0.56, p = 6.4e-30, 20/21. See claims-file point (b) below. |
| learning-trials | reproduced | Yes | Cell 18. |
| learning-to-90 | reproduced | Yes | Cell 20: 0.898, or 0.803 over all sessions. Only one session reaches 0.9 at the criterion trial itself. |
| probe-transfer | not reproduced | Yes | Cell 23: 28.3% and 58.3% against 44 and 73. No variant puts both means inside tolerance. |
| probe-faster-criterion | blocked (methods underspecified) | Yes | |
| cells-recorded | partially reproduced | Yes | |
| responsive-cells | blocked (metadata insufficient) | Yes | |
| state-space-most-responsive | not reproduced | Yes | Cell 38: 37 to 57 cells against 75.6 to 92.4, and 41 to 58 using the upper tail only. |
| multi-space-coding | blocked (metadata insufficient) | Yes | |
| direction-center-vs-periphery | partially reproduced (assumed) | Yes | The assumption is stated: the three-space responsive cells stand in for reading (b). It is the weakest step. For a signed-rank test the result on 59 cells puts no bound on the result over the paper's set. Under reading (a) neither level is met (cell 41). |
| direction-tuning-not-maintained | not reproduced | Yes, under the same stand-in, but it should be marked `assumed: true` | Reading (b) uses the same three-space stand-in as the previous claim, which is only a lower bound of the responsive set. The record does not mark this as an assumption. With shifted chunks under (b), 51 cells give 14 low (cell 44). Up to 10 more cells could join and keep n within 56 ± 5.6, and only 4 of them would need to be low to reach 18. Over the paper's set, the criterion is therefore not excluded under that reading. Reading (a) fails on n (40 and 28, against 56 ± 5.6). |
| state-space-ic-higher | partially reproduced | Yes | Cell 53: p < 0.01 under all 12 rows; the largest is 0.0022. |
| sparsity-state-vs-direction | reproduced (assumed) | Yes | Cell 48. Reproduced with the full-trial window, which is the claims file's reading (a). Not significant from start to reward. |
| sparsity-state-vs-position | not reproduced | Yes | Cell 50: the overall test is significant (p ≤ 0.00043) and the per-cell counts are 3 to 11, against 15 ± 1.5. |
| sparsity-gaze-vs-state | blocked | Yes | |
| state-space-selectivity | not reproduced (assumed: permuted chunks) | Yes, as an assumption | The assumption is stated and reasonable. The Results say "randomly shuffling periods of spiking activity in time", and the Methods say the 5 s chunks were "randomly shifted". The claims file left both readings open, and under shifted chunks the claim cannot be decided (cell 56). Without the assumption the outcome would be blocked. |
| landmark-identity-distance | not reproduced | Yes | Cell 61: at most 31 cells (33 with type III), against 64 ± 6.4. |
| landmark-identity-center | blocked | Yes | Cell 63: the bounds straddle 11 to 13. |
| path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked (metadata insufficient) | Yes | |
| fields-per-cell, dimensionality-control | blocked (methods underspecified) | Yes | |
| spatial-selectivity-fraction | blocked | Yes | Cell 66: (a) gives 0.129 to 0.247 and fails; (b) and (c) cannot be decided. |

Caveat (a), gaze-anticipates-action: cell 28 prints the eye velocity in the 500 ms before the turn code. For K it already shows a slow-phase-like difference: right 0.250 against left −0.189, in 38/40 sessions, p = 2.3e-9. So in K the view may already be rotating in that window, perhaps from a preceding turn the same way, and the eye-position effect there may partly continue that rotation. S shows no such difference (9/20 sessions, p = 0.40) and has the larger position effect (−1.00 SD). The outcome stands, but the record should mention this.

Claims-file point (b), reported and not corrected: the claim says the monkeys looked proactively at where landmarks would appear. The criterion for gaze-anticipates-landmarks takes the mean eye position over the whole return, so it cannot separate anticipation from the shift of eye position that comes with any rotating view. The attempt says so (cell 32 and the record's notes). The criterion does not test the "proactive" part of the claim.

## 2. Text against the printed outputs

Almost every sentence checked matches the outputs, including all the numbers in the record's notes and findings. These are the exceptions:

- **Cell 9:** "at the trial start (code 21) the abscissa is at the arm end, at the arrival at the choice point (code 22) it is 0, and one second later or earlier it is not."
  - Cell 8 prints `start +0s 0.01` (near 0, which cell 7 defines as the centre) and `center +1s 0.00`.
  - Both halves are contradicted.
- **Cell 7:** "Column 5 … runs from 0 at the centre to 1 at the arm end."
  - The same outputs fit an abscissa that runs from the start of each branch: 0.01 at the trial start, 0.72 one second before the centre, 1.00 at the reward.
  - The record's landmark-identity-distance deviation repeats "(0 centre, 1 arm end)".
  - On the entry paths the quarters may be numbered in the opposite order. The main-effect and interaction counts do not depend on the order, so no conclusion changes.
- **Record, direction-tuning-not-maintained:** "The low count misses 18 to 22 under every reading." This holds for the stand-in set only, not for the paper's reading (b); see section 1.
- **README:** the row "State-space selectivity in the centre | Not reproduced" drops the qualifier carried by the notebook summary (cell 67) and cell 57: "permuted chunks; open under shifted chunks".

Cell 0, the Summary (cell 67) and the record's findings are otherwise supported.

The record's `verifications` entry states my round-1 reasons accurately, mostly in my own wording, with my problems 1 to 10 assigned to the right claims and summarised under `reviewed`.

## 3. Round-1 points

**Resolved:**
- Problem 2: the shift surrogates were rebuilt. Cell 34 gives a synthetic false-positive rate of 3.3% at p < 0.01 over 60 trains, against 100% before.
- Problem 3: tails are now stored; at most 3 cells are significant on the low side.
- Problem 4: three move typings were run.
- Problem 5: state-space-ic-higher is now graded, under all readings.
- Problem 6: a start-to-reward window with returns was added.
- Problem 7: start-arm sequences and variants were added.
- Problem 8: type III sums of squares were added.
- Problem 9: signed-rank tests across sessions were added.
- Problem 10: all 187 files have 12 columns and a radius of 0.81 to 3.0.
- Problem 1: resolved as far as the data allow, through the velocity check. It remains a stated assumption.
- All section C requests were answered.

**Remaining issues that bear on a conclusion:**
1. direction-tuning-not-maintained rests on the three-space stand-in for reading (b). It should be marked `assumed: true`, and the notes should say that under shifted chunks the paper's set could still meet the criterion.
2. state-space-selectivity is not reproduced only under the permuted-chunk assumption, and the README row should say so.
3. gaze-anticipates-action in monkey K: the slow-phase velocity before the turn code suggests the window overlaps an ongoing rotation. This is a caveat on interpretation; the outcome stands under the criterion.
4. Claims file: the gaze-anticipates-landmarks criterion does not separate anticipation from rotation-linked eye position. The attempt states this, and it is reported here, not corrected.

Not bearing on a conclusion: the abscissa description in cells 7 and 9 and in the record's deviation.
