**Round 2 verifier report: Mohebi et al. 2019 on CRCNS vta-2 (attempt mohebi-2019-01)**

The claims file has 37 claims, and the attempt record gives 37 outcomes, one per claim: 8 reproduced, 7 partially_reproduced, 2 not_reproduced and 20 blocked (data_missing). The record marks two outcomes as `assumed: true`: retro-tagged-cells-resemble-others and fig4ac-dopamine-cue-responses. Cell indices below are those of the re-executed notebook, which differ from round 1.

**1. Outcomes**

I agree with all 37 outcomes.

- **Blocked (20 claims).** Agreed. The data set holds only the 29 tagged dopamine cells; nothing else the paper used is deposited.
- **Outcomes that stand with a variant run or noted.**
  - **fig2efgh-tonic-firing-indifferent-to-reward-rate (partially_reproduced).** Agreed. Cell 38: reading (a) finds 18 of 27 cells significant, and 9 of 27 when the high/low labels are shifted circularly. Reading (b) finds 2 of 27, or 0 of 27 with the median block put low. Across cells, firing is 0.50 Hz higher in high blocks (signed-rank p = 0.0006). The record now rests this outcome on the readings together, with no assumption.
  - **fig5a-early-trial-firing-not-reward-rate (not_reproduced).** Agreed, following the criterion's Pearson count (8 and 6 of 29 cells). Under the new circular-shift variant, the window before Center-In still exceeds chance: 2 of 29 cells, binomial p = 0.034. So the outcome would hold under that variant too.
  - **fig5ab-weak-negative-rpe and ed8-other-reward-expectation-estimates (partially_reproduced).** Agreed, for the reasons now written into the record.
- **retro-tagged-cells-resemble-others (assumed).** The assumption is stated and reasonable. Cell 47: with 5 or 6 blocks a side, reading (b) could reach p = 0.009 and 0.004, so it has power for these cells, and it finds no change (p = 0.076 and 0.75). Reading (a) against circular shifts also finds no change (p = 0.27 and 0.85). Setting aside the plain rank-sum of 1 min bins is justified, because it treats serially dependent bins as independent.
- **fig4ac-dopamine-cue-responses (assumed 0.5 s window).** The assumption is stated and reasonable. The outcome does depend on it. With the 1 s window, 13 of 27 cells (48%) respond to Light-On, which is not more than half, so that reading would give not_reproduced. The record's deviation says Light-On falls under half with the 1 s window, which is accurate.

**2. Text checked against the printed outputs**

Almost every sentence of the "Result:" cells, the Summary (cell 73), the README and the record notes matches the printed numbers. These do not:

- **"13 units" with out-of-order spike times** (cell 8, Summary cell 73, record finding "Spike times are not in ascending order … 13 of the 29 units").
  - The `unsorted_segments` column in cell 7 lists 11 units, not 13.
  - The record's example, "2399.4926 after 2399.4930 s in IM657160613t11a", is not printed anywhere in the notebook, so I could not check it.
- **"individual cells do change under every test with the power to detect it"** (cell 39; also in the fig2efgh record notes).
  - Cell 38 shows only that 6 cells cannot reach p < 0.05 under reading (b). Reading (b) can reach p ≤ 0.05 for the other 21 cells and finds 2 of 27 (binomial p = 0.394), or 0 of 27 with the median block put low.
  - The sentence holds for the tests on 1 min bins, not for reading (b).
- **"with 2 or 3 blocks a side 6 of the 27 cells cannot reach p < 0.05"** (cell 39 and the record notes).
  - With the median block dropped, the 6 cells that cannot reach it are the six with 2 blocks a side (minimum p 0.121).
  - The seven cells with 3 a side can just reach it (minimum p 0.0495).
- **"no valley correlation can be significant"** (cell 69 and the fig5ab notes).
  - Cell 67: the valley varies across trials in 8 of 29 cells (1 to 3 s window) and 2 of 29 (0 to 2 s), so for those cells a correlation is defined. The output shows that none is significant, not that none can be.
  - "Under 0.5 Hz on all 3695 unrewarded trials" rests on a printed "100.0%", which is rounded to one decimal.
- **"where the latency fit is weak"** (cell 72 and the ed8 notes).
  - Cell 71 does not support this for every session at the edge of the alpha grid. Two of the four Q-learning sessions at alpha = 1.00 fit well: IM-1002_170127 (r −0.346) and IM-1078_180827 (r −0.402).
  - The phrase comes from my round-1 item 9, which was wrong on this point.
- **README.** The fig4ac row reads "Partially reproduced" without the "(assumed window)" marker that the Summary table and the record carry.

The record's verification entry states my round-1 reasons faithfully. Mostly it quotes my table and attaches my numbered items to the claims they concern; that is accurate, but much of it is a near-verbatim quote, not a paraphrase. Its summary is correct: I agreed with 33 outcomes, differed on 4 (fig2efgh, retro, fig4e, fig5ab), and reported no misreading of the paper by the claims file. Two of my own round-1 statements were inaccurate, and the notebook now prints the correct values:

- I wrote that "7 IM-1037 cells and 6 others" had a guaranteed "no change" under reading (b). Only 6 cells cannot reach p < 0.05.
- I wrote "1.00 in up to 6 sessions" for the alpha grid. That is 2 sessions for the actor-critic and 4 for Q-learning.

I found no place where the claims file misreads the paper. The Methods do print "Gaussian kernel with variance 20ms".

**3. Round-1 points**

All are resolved:

- 1, valley always 0 Hz: the notebook now prints which of the authors' scripts compute a valley or pause (none do), and the conclusion says the valley part cannot be tested.
- 2, pause reading that drops trials: a third pause reading was added, the dropped trials per cell are printed, and the outcome is partial.
- 3, kernel: the SD 4.5 ms kernel was run for the click and cue responses and the Light-On alignment, with the same outcomes.
- 4, tonic-test power: the smallest reachable p per cell and a circular-shift null are printed.
- 5, serial correlation in fig5a-early: the circular-shift null was run.
- 6, 1 ms pulse substitution: the counts without it are shown.
- 7, SALT's p resolution: stated.
- 8, 8 against 9 IM-1037 cells: explained.
- 9, alpha at the grid's edge: edge counts printed, though the "weak fit" wording needs fixing (above).
- 10, firing rate over all segments: stated.
- 11, burst and cue-response checks: no change was needed.
- 12, blocked claims: confirmed.
- Section C, Light-On window overlapping Center-In: settled. Using only trials with latency over 0.5 s gives 11 of 27 cells.

Remaining items that bear on a conclusion's wording; none changes an outcome:

- fig2efgh: the "every test with the power" sentence and the "2 or 3 blocks" phrasing.
- fig5ab and ed8: the "can be significant" wording about the valley, and the "latency fit is weak" wording.
- fig4ac: the README should mark the outcome as resting on the 0.5 s window.

Not bearing on a conclusion: the count of units with out-of-order spike times is 11, not 13, in cell 8, the Summary and the finding.
