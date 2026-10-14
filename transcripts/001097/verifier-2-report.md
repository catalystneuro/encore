# Verification report, round 2: Liu, Nair et al. 2024 (doi:10.1038/s41586-024-07916-w), dandiset 001097 v0.260624.0330

**Bottom line:** I agree with all 25 outcomes. Every round-1 point bearing on a conclusion has been worked on. Cell order is settled. What remains is mostly about the Figure 2e GLM: one sentence in the fig2e notes is contradicted by the notebook's own numbers. Two numbers in the text are stale or wrong.

I re-downloaded the paper from Europe PMC to `paper/PMC11499253.xml` and `paper/paper.txt`. Cell numbers below are those of the re-executed notebook, which has 79 cells.

## 1. Outcomes

I agree with all 25 stated outcomes: 7 reproduced, 2 partially reproduced, 3 not reproduced, 13 blocked.

- **fig2e (not reproduced) and fig2f (reproduced):** I agree, at low confidence for both, for the reason in section 3.
- **ed6e and ed7 (partially reproduced):** each criterion is met as written (cells 59 and 63).
- **Blocked claims:** the reasons hold. I checked them against cell 71 and the Methods; the paper's "small time interval Δt" is indeed left open.

## 2. Text against the printed outputs

Almost every sentence in the "Result:" cells, the Summary (cell 78), the README and the attempt record matches the outputs. These do not:

- **Cell 61 and the ed6e notes, "0.62 on the receptive day against 0.23 and 0.19":** cell 59 prints 0.614, which is 0.61. The 0.62 is left over from round 1 (0.616, before the raster fix).
- **Cell 61, "close to the paper's 0.69 against 0.09":** the unreceptive values are 0.231 and 0.191, about twice the paper's 0.09. "Close" fits only the receptive-day value.
- **fig2e notes, "The paper's point that behaviour explains little of the activity holds under every design":** with random folds, cell 47 gives 0.322 for both behaviours together. The claims file defines "little" as below 0.25, so under this design the point fails by the criterion's own standard. Cell 52 does not make this claim.
- **fig5c notes, "matching a day ... works for 5 of the 7 mice":** the matching rule in cell 14 finds 4 mice (543, m541, m542, m551). m438 day 1 is added in cell 19 on frame count alone, and its male annotation counts differ (60 against 76).
- **fig1e response, "No 7-day session matches the receptive session of m928, m930 or m940":** the evidence printed in cell 19 does not settle this for m930.
  - Day 3 has 4,520 frames against 4,511 and an interaction of 322.7 s against 322.3 s. That is the same kind of near-identity used to mark m438 day 1 (808.4 against 808.5 s) as a duplicate.
  - Day 4's trace match is 0.73. That is above every non-duplicate day shown (0.33 to 0.50) and close to m438 day 1 (0.78).
- **fig3a notes:** the per-session fit timing and the linear-dynamical-system stand-in result (rotations in 14 of 15 sessions) are not in any printed output. Cell 0 says they were not run in the notebook. They are unverifiable here, not contradicted.
- **README, "It takes about seven minutes":** no printed output shows a run time.

**My round-1 reasons in the attempt record:** they are in my own words and faithful. Some evidence was compressed away:

- fig1e: the bout and interval counts (1,540 and 1,471 against 1,685 and 1,611) are dropped.
- fig2c: "18 to 75% of cells pass the shuffle test" is dropped.
- fig2e loses the most:
  - the synthetic null with unrelated behaviour regressors (−0.09);
  - the random-fold null score (+0.04);
  - the observation behind the penalty-selection point, that "both" scored below "male".

None of these changes a reason's meaning.

## 3. Round-1 points

**Resolved:**

- **1, cell order of the weights:** 171 of 176 and 71 of 72 cells best match the same index; the projections correlate at 0.94 to 0.96 (cell 11).
- **3, choice-probability comparison set:** the pairwise variant tunes more cells, not fewer (cell 44).
- **4, fig2i:** the window ending at the last annotation is added, and the four mice of the figure are not identified, so no subset could be chosen.
- **5:** trial counts per bin and a fixed-trial curve are added.
- **6, 7, 8, 11:** recorded in the deviations or notes.
- **9:** resolved except for m930 (see below).
- **10:** the raster is fixed, with an assert in cell 6.
- **12:** the exploratory pencil-cup tail and ramp checks are added (cells 73 and 76), and the reason for not using partial least squares is given.
- **Section C requests:** the per-mouse file contents, trace types, the tail list and duplicate evidence are all now printed.

**Still bearing on a conclusion:**

1. **fig2e and fig2f, from Problem 2.** The intercept-only baseline is now reported (−0.086), but the penalty is still chosen on the last fifth of each training set. "Both" still gains less than "male" alone (0.029 against 0.073, cell 49). A ridge model with a well-chosen penalty should not get worse when regressors are added, so the ordering failure, which is part of the "partially" rule, may be an artefact of the selection. Random folds still leak through autocorrelation. Neither outcome rests on a sound design, and the "every design" sentence should go.
2. **ed7: the cells are not specific to the integration factor.** In m541, cells weighted on the other factor (factor 1, above 1 SD) also lengthen on the receptive day: 30.8 against 17.5 s, KS p 7e-6 (cell 64). That is as strong as the integration factor's own cells. In 543, factor 2 on its own would have met the ed6e mounting criterion (0.655 against 0.538 and 0.505, cell 59). So the "integration dimension" label, chosen by ACHW, carries much of both partial outcomes. The text never says this.
3. **Possible duplicate in the fig1 trial set (m930).** If m930 day 3 or day 4 duplicates the receptive session, the set drops to 68 trials. fig1g is the most sensitive: the interval value of 0.218 is 0.011 inside its tolerance, and its "reproduced" rests on that single reading.
