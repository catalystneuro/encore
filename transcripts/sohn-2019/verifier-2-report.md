**Verifier report, round 2: Sohn et al. 2019 on DANDI:000130 (0.241017.1448)**

The claims file lists 23 claims and the attempt record gives 23 outcomes: 10 reproduced, 3 partially reproduced, 7 not reproduced and 3 blocked (data_missing). The cell numbers below are this notebook's, which differ from round 1.

### 1. Outcomes

I agree with all 23 stated outcomes.

- **Changed fits, same outcomes.**
  - gpfa-variance-inverted-u stays not reproduced: with 1000 EM iterations, p = 0.0547, 6 of 8 below zero (cell 68).
  - gpfa-mean-sigmoid stays reproduced: 7 of 8, p = 0.0156, and 4 of 4 slopes (cell 71).
- **No outcome is marked `assumed: true`.** The choices that outcomes depend on are listed as deviations and run both ways:
  - the intercept (beh-slopes, beh-long-more-bias);
  - the kernel width (pca-dimensionality);
  - the number of GPFA iterations, and nominal against actual Set times.

  Only beh-long-more-bias changes with one of these: it would be partial without the intercept. The notes say so, and the criterion fixes the regression. I consider these choices stated and reasonable.
- **alt-speed-unmodulated is "reproduced" only because the test cannot fail with 4 datasets.** The record says this.

### 2. Sentences the printed outputs do not support

- **alt-speed-unmodulated, cell 60 and the record's notes.** "The speed rise in the measured steps is accounted for by noise, so these data do not show the modulation the claim denies."
  - With the noise removed, the slope is negative in 8 of 8 in the main analysis (−0.84 to −10.99 per s) and in 8 of 8 with fixed trials (cell 59). That is a falling speed, which is also modulation, and the sentence leaves it out.
  - The noise estimate also looks too large late in the support. The noise-only step at the end (5.07 to 6.85) is above the mean measured step in all 8 dataset-priors (2.79 to 6.06). By a straight-line fit it is also above the measured step at the end, for example Eye Right Long, about 4.4 measured against 6.12. If the estimate were unbiased, the measured step could not be smaller than the noise step on average.
  - With fixed trials the noise-only slope is still positive in 8 of 8 (2.4 to 8.0 per s), so the rise is not only an effect of attrition.

  The correction therefore does not support "accounted for by noise".
- **README.** "It takes about 26 minutes". Cell 74 prints 21.4 min.
- **Summary, cell 75.** "other readings of the smoothing kernel width do not change that" (a 2-dimensional estimation space). Under FWHM 40 ms, Hand Left needs 3 components (cell 35). This is minor, since 7 of 8 values are still 2.
- **Attempt record, findings.** "For aborted trials `tp` holds negative values (such as -1600 or -2400 ms)". No printed output shows these values. Cell 4 shows only that 1026 trials have tp > 0.
- **speed-vs-projection, cell 51 and the notes.** "the noise-only speed is not correlated with Xu when pooled" is true. Within datasets, though, it is −0.77, −0.82 and −0.87 in three dataset-priors (cell 50). This does not affect the outcome, which uses the pooled value.

Every other number in the conclusions, the Summary, the README table and the notes matches the outputs. I checked each one.

**My round-1 reasons in the record.** They are stated faithfully, mostly in my own words. Problems 4, 8 and 9, which I marked as not affecting a conclusion, are attached to the reasons for encoding-r2, alt-threshold-monotonic and glm-prior-ts without that qualifier.

**Claims file.** It still misreads the paper in these places:
- The header and the beh-bayes-model criterion still say the supplement was not available. The response "Corrected the header" refers to the notebook (cell 0), not the claims file.
- New this round: the criterion for alt-speed-unmodulated uses smoothed rates. The STAR Methods say speed was computed "in the full neural space to avoid any potential distortion by smoothing and PCA".
- From round 1: the per-condition rule for beh-slopes is stricter than the median-slope test in Table S1.
- From round 1: short-in-long-control leaves out the paper's interaction test (F1,7 = 161.43).

### 3. Round-1 points

**Resolved:**
- 2: GPFA now runs 1000 iterations, with the log-likelihood rising 0.17 to 0.53 over the last 10.
- 3: all readings of the kernel width were run for both epochs.
- 4: the weak specificity of encoding-r2 is stated.
- 5: basic bootstrap intervals were added, and both interval types are said to be unreliable.
- 6: the interaction was run (F(1, 3) = 0.56), and the record says the criterion cannot fail.
- 8: a padded variant was run. At 75% variance it would give partial, but the criterion fixes 60%.
- 9: actual-Set variants were run for the GLM and GPFA.
- 10, 11, and the wording about the GPFA session.

Point 1 is handled in the notebook and by questions to a reader. The claims file itself is unchanged.

**Remaining points that bear on a conclusion:**
1. **alt-speed-unmodulated.** As above, the noise correction shows falling speed in 8 of 8, and the noise estimate may be inflated late in the support. The output that would settle it is the measured step and the noise-only step for each bin, plus a check of the noise estimator on rates with constant noise. The claims file's use of smoothed rates is a further departure from the paper. The outcome cannot change, because the test cannot fail, but the conclusion's interpretation should change.
2. **gpfa-variance-inverted-u.** p ranges from 0.055 to 0.125 across the three fits. The outcome holds under all three, but the result is fragile.
3. **initial-speed-biased.** With the noise removed it is 7 of 8 but p = 0.078. This is reported, and the outcome rests on the raw speeds that the criterion specifies.
4. **Claims-file questions to a reader.** The outcomes of beh-slopes, beh-long-more-bias and short-in-long-control depend on these: the Table S1 reading, the intercept, and the interaction test.
