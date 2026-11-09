I've revised the attempt for every point in the round-1 report, re-run the entry and recorded the round. The full notebook ran clean from a fresh environment in about 41 minutes (`tools/entry.py check`: 0 errors). Main results were identical across three full runs. New totals: 35 reproduced, 1 partially reproduced, 7 not reproduced, 7 blocked (was 27 / 11 / 5 / 7). Nothing is committed.

**The excess of place cells (B1) is fixed.** The paper's helper package, TwoPUtils, is public (GiocomoLab/TwoPUtils), although the record had said it was not. Its test differs from the first round's in two ways: it rolls position rather than activity, and it subtracts the rate map's minimum and adds 0.001 before taking spatial information. With that test, 48.7% of cells are place cells, against the paper's 48.5%. The first-round test is shown as a variant (59.9%), with two others (the files' own deconvolved series, 49.6%; OASIS time constant 1.0 s, 46.3%). The code also confirms that the shuffle uses one offset per trial for all cells, as the first round did.

**Outcome changes and why:**
- **Now reproduced:**
  - **Because the place-cell counts now match:** place-cell-fraction, remap-category-fractions (under reading a), rr-cell-fractions, ed2jl, ed2m and ed5a; ed4hij now passes, but only just (p = 0.046).
  - **ed6c:** slope −0.203, p = 6.9e-5.
  - **fig6e:** 8 of 11 mice under reading (b).
  - **ed7:** matches the verifier's call; the depth part is still untested.
- **Now not reproduced:**
  - **ed2f:** after the switch 6.71% of cells, against a lower limit of 6.75%, about 3 cells short.
  - **fig5i:** p = 0.087.
  - **fig4j:** matches the verifier's call.
- **Disagreement recorded:** I kept ed4l as partially reproduced, where the verifier said not reproduced. The decrease is significant near reward (p = 0.020) and in the stated direction but not significant far from reward (p = 0.069), which is what the protocol calls holding only in part.
- Outcomes that changed because of the new test are marked as resting on an assumption.

**Other fixes and outputs the verifier asked for:**
- **Model fits (B2):** each mixed-model fit now prints whether it converged, its warnings, the random-intercept variance, and an ordinary regression with errors clustered by mouse for comparison.
- **Place fields (B3):** now tested on the raw, unbinned activity, following the Methods and the paper's code, with the binned version kept as a variant. Per-day counts of one- and two-field cells are printed. The two-field counts are still 2.5 and 4.2 times the paper's.
- **Cross-day matching (B4):** two variants are added, one threshold per mouse, and the matching rule of TwoPUtils. Outcomes are the same except fig5f, which is significant only under the TwoPUtils rule (p = 0.032, from a fit that did not converge). I kept the Methods' wording as the main reading, as the protocol puts the Methods ahead of code.
- **Data check:** a new cell lists everything a day-14 file holds. There is no depth or matching data.
- **Smaller points:**
  - B9: the cross-correlation step already matches the paper's code (`dayData.py:1432-1434`), so I left it.
  - B8: documented, since it touches only variants.
  - B11: fig3b/c stay "too large", because the protocol uses that label when the estimate exceeds the notebook's time limit.
  - I added retries to the archive connection after one run failed on a dropped connection.

**Questions for a reader**, in the new `questions/001361.yaml`:
- ed8df: should the speed tests use the 61 sessions the legend counts?
- fig2i: the statistic can never be negative, so "positive at every distance" is a weak test.
- The header lists depth estimates the files don't have.
- place-cell-fraction: the criterion says "SI as the Methods' formula". Does that include the code's 0.001 offset? This decides whether the place-cell fraction matches.

**Not done:**
- The decoder, GLM, k-means and teleport claims are still blocked; there wasn't time to try them.
- The variant with position rolled and no offset wasn't run on the full data, so the record doesn't separate how much of the change comes from the offset and how much from rolling position.

The record is `attempts/001361-sosa-2025-01.yaml`. It has a `verifications` entry for round 1 covering all 50 claims, with the verifier agreeing on 40.
