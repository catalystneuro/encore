I've handled both answered questions. Neither changed an outcome. The entry checks pass with 0 errors, the notebook runs from a clean environment in 257 s, and the handover is built in `executed/park-2019/handover/`. I haven't committed or pushed anything, and haven't verified my own work.

**Question 1, fig5-error-inhomogeneous: the reader amended the claim.** The criterion now names three readings of what the error distribution covers:
- (i) the mean absolute error in each 10 degree bin of head direction;
- (ii) the head directions of windows decoded within 15, 30 or 45 degrees;
- (iii) the signed error angles. This is the only reading I ran before the answer.

I re-ran the claim under all three readings, with the three pooling readings and both windows (660 ms and 133 ms).

- **Outcome: partially reproduced, the same as before.** Every test holds (all four distributions non-uniform, both Kuiper's tests at p < 0.05) in 75 of the 80 combinations. None of them has all four r values within tolerance, and the best has two.
- **Closest match.** This is ensemble 0930R029 with 660 ms windows, one of four ensembles tied for most cells, under reading (ii) at 15 degrees:

  | r value | Measured | Expected |
  |---|---|---|
  | Room-frame error | 0.604 | 0.589 (within) |
  | Arena-frame error | 0.484 | 0.653 (outside) |
  | Room-frame head direction | 0.072 | 0.147 (outside) |
  | Arena-frame head direction | 0.360 | 0.378 (within) |

  These replace the earlier measured values from reading (iii): 0.560, 0.144, 0.072 and 0.360.
- **What the new readings change.** They bring the arena-frame error r closer to 0.653, up to 0.548 for the median over ensembles at 133 ms, but never within tolerance. With all seven ensembles pooled, no r is within tolerance under any reading.
- **Two choices of mine, recorded as deviations.** The paper doesn't fix two details of reading (i):
  - The Rayleigh n is the number of decoded windows, because the paper's z implies about 680. With n = 36 bins as a variant, the arena-frame error is uniform for every ensemble.
  - Kuiper's test compares the error weights with head-direction occupancy over the same bins, using a new helper `hd20.kuiper_binned`.

  Neither choice changes the outcome, since readings (ii) and (iii) give the same result.
- **Files updated.** In the notebook I rewrote the method text, the analysis cell and the conclusion for this claim. The attempt record has new notes, new measured values and the two deviations. The README and summary table stay as they were, since the outcome is the same.

**Question 2, figs3-no-head-direction-bias: the reader left the claim unchanged.** The threshold stays at p ≥ 0.05, so I didn't re-run it. The outcome is still reproduced, resting on my assumption about the Rayleigh n. The claim's notes now record the answer. They also say that with my assumed n the smallest p is 0.35, so the result would meet the paper's p > 0.17 as well.

fig5c-error-minima-at-cues uses the same decoding but wasn't amended; its numbers came out identical in the new run.
