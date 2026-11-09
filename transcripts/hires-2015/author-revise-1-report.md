I've revised the attempt for verifier round 1. The entry re-ran cleanly with `python tools/entry.py all entries/000013-hires-2015` (0 errors, 12.1 min) and every conclusion now matches the new numbers. Nothing is committed.

**Outcomes changed (5).** The record now has 22 reproduced, 1 partially reproduced, 8 not reproduced and 14 blocked, against 22, 5, 4 and 14 before.

| Claim | Before | Now | Why |
|---|---|---|---|
| behavior-whisking-bouts | partially | not reproduced | The verifier was right: these criteria need every value within tolerance and have no partial rule. Bout duration fails under every reading. |
| behavior-touches-reaction | partially | not reproduced | Same reason: the touch count fails under every reading. |
| example-cell-touch-window | partially | not reproduced | Same reason: the time fraction fails under every reading. |
| whisking-rate-l4-no-change | partially | blocked (methods_underspecified) | With the corrected whisking periods, L4 C2 shows no change with touch epochs left out (p = 0.595) but does change with them in (p = 1.3e-7). The criterion's two readings now disagree. |
| fig4c-phase-decoding | blocked | not reproduced | Using phase cycles from the whole trial, C2 comes out at 66 to 103 deg (or never reaches 76% correct) against 24 deg, and is worse than outside C2 under every reading. The criterion ends with "else methods_underspecified"; I read that as its rule for readings that disagree, which they no longer do. The verifier may question this in round 2. |

**What I fixed or added**
- **Whisking periods (problem 1):** they now leave out licking cycles and the 70 ms after each touch, as the claims file defines them. The files hold only lick onsets, so a whisk cycle counts as "during licking" when it contains one; this is my own choice and is labelled as such. The old mask is shown as a variant.
- **Phase tuning (problem 3):** it now uses every phase-analysis cycle in the trial, not only those inside the sample epoch. The sample-epoch version is kept for example-cell-phase-modulation (its criterion says "exploration periods") and as a variant elsewhere. Effects:
  - The L4 vs L5 tests now also hold for cells with at least 20 phase spikes (p = 0.0043 and 0.032).
  - fig3d-touch-phase-l4c2 now passes in 1 of 16 readings instead of 4.
- **Touch detector (problem 2):** the fraction detected is now read at the time point of best percent correct, and tied thresholds are broken at the middle one. The tie rule is not in the claims file, so I recorded it as a deviation and show the old lowest-threshold rule as a variant. Repetitions went from 20 to 50.
  - The verifier's synthetic test (a neuron with no touch information) now scores 0.15 detected, not 1.
  - Across readings, the population needed for 95% is 12 to 30 neurons, and only one reading (14) falls within 15 ± 1.5.
- **Zero-median check (problem 4):** the two zero medians in the L4 outside C2 row of Table 1 now count among its 17 values. Neither median is ever 0, so the count is unchanged.
- **Outputs the verifier asked for:**
  - each L4 C2 file's touch-peak latency by clock offset;
  - per-cell touch windows for the L4 outside and L5 cells;
  - the two rows where cell 11 matches, and the number of units tested;
  - percent correct with one neuron;
  - phase depths for cells with at least 20 spikes.
- **Clock finding:** corrected to say that a residual 4 ms difference between the two batches of files is not explained.
- **Record:**
  - `verifications` round 1 now lists all 45 claims, each with the verifier's reason and my response.
  - The notebook summary, README and runtime (13 min) are updated.

**Disagreements I kept**
- **Kept blocked by dependency:** fig3c-touch-spikes-outside, fig3d-touch-phase-outside and fig4a-touch-detection-outside. The protocol blocks a claim that depends on a blocked claim. Their notes say how each fares under its own criterion: fig4a-outside now holds under every reading, and the other two fail under every reading.
- **Kept blocked because readings disagree:**
  - **table1-l4-outside:** its count straddles the threshold.
  - **fig5-modulation-correlations:** it holds in 16 of 64 readings.
  - **example-cell-ff-around-touch:** no cell matches with pooled touches, but cell 11 matches in 2 of 394 grouped units.

**Not done**
- I did not change the claims file and filed no new questions. The verifier's three concerns about it are recorded in the verifications responses for a reader to take up:
  - the cutoff rule for cells with no real rise;
  - the risk of a chance match when about 400 units are tried;
  - noise latencies from the latency rule.
- I did not rebuild the handover package. For round 2 the full executed notebook is handed over, which is in `executed/000013-hires-2015/`.
