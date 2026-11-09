**Round 2 verification: Sohn et al. 2019 on DANDI:000130 (0.241017.1448)**

Counts come from the claims file and the attempt record. There are 23 claims: 20 tested and 3 blocked. The record gives 9 reproduced, 4 partially reproduced, 7 not reproduced and 3 blocked (data_missing). That matches my round-1 totals. Cell indices below refer to the current 89-cell notebook, so they differ from my round-1 numbering.

I could not get the paper text. PMC's BioC service returned 429 and Europe PMC returned 500. Two error responses were left under `paper/`: `PMC6805134_bioc.json`, which holds the 429 page, and `PMC6805134.xml`, which holds the 500 message. Neither contains paper text. Deleting them was blocked because it needed approval and this session has no way to give it. Without the paper I could not check the figures that come from it (see item 8 in section 2).

**1. Agreement with the stated outcomes**

I agree with all 23 outcomes as the claims-file criteria define them.
- **Reproduced but uninformative:** short-in-long-control and alt-speed-unmodulated are "reproduced" only because a test over 4 datasets cannot fail. The record now says this plainly.
- **Sensitive to choices fixed beforehand:**
  - pca-dimensionality fails on unnormalised rates but passes in 8 of 8 with z-scored rates.
  - alt-threshold-monotonic depends on how many components are kept: −210 ms at 60% of the variance, −80 ms at 75%, −40 ms in the full space, and −70 ms with at least 3 components.

  Keeping each outcome on the pre-fixed criterion is correct, and both dependences are stated.

**2. Statements the printed numbers do not support**

1. **Cell 79 and the record's alt-threshold-monotonic notes:** "In the eye datasets, with 1 component (16 curves), the minima are crossings." Cell 77 shows the distance at Go is more than 10 times the minimum in only 5 of the 16. Cell 76 shows 4 of the 16 have their minimum at Go (ratio 1.000). The output shows crossings for at most 5 curves, not all 16.
2. **Cell 88 (Summary):** z-scoring "removes the encoding axis's advantage over random axes." In cell 44, with z-scored rates, u's R² is above the median random axis in all 8 dataset-priors (for example Hand Right Short 0.973 against 0.761). Between 7.6% and 39.5% of random axes score above u. What is lost is beating 95% of random axes (0 of 8); an advantage over the median remains.
3. **Cell 71 and the record's alt-speed-unmodulated notes:** "This session shows no speed modulation beyond what noise produces." In cell 70 the observed slope is below the null mean in 8 of 8 with the attrition measure and in 8 of 8 with fixed trials. The data never exceed the null, but they sit below it every time. Either the null overstates the noise or speed falls during the support, so the data match the null only in the one-sided sense.
4. **Record, beh-bayes-model:** "wm and wp (0.09 to 0.11)." Cell 25 gives wp from 0.090 to 0.106, but wm from 0.013 to 0.117.
5. **Cell 84:** "0.065 to 0.085% in this run." Cell 83 prints 0.067 to 0.084%. The difference is small.
6. **Record, gpfa-variance-inverted-u:** "the counts and p values did not change over four runs." No cell shows repeated runs.
7. **README:** "It takes about seven minutes." Cell 86 prints a total run time of 609 s, about 10 minutes.
8. **Paper-derived figures I could not check:**
   - Cell 88 gives "536 (H) and 636 (G) units", while the record's finding says "617 and 741 units". These may be selected and recorded counts, but neither text says which.
   - The record's finding calls "N = 48 … N = 107" GPFA "sessions"; in the paper's sentence N is the number of neurons.
9. **Minor:** cell 49 and the record say "Differences are 0.045 to 0.573." That range covers only the datasets where the Bayesian model wins and leaves out Hand Right Short at +0.186, although the cell names that exception just before.

Everything else in the conclusion cells (14, 17, 20, 23, 27, 31, 36, 40, 45, 49, 52, 55, 59, 62, 67, 71, 74, 79, 84, 87), the Summary, the README table and the record notes matches the printed outputs.

**Round-1 reasons in the record:** they are in my words and faithful. A few merge in points from my problems section: weighted_fit under encoding-bayes-beats-linear, and the Long ts time points under glm-prior-ts. These attributions are correct.

**3. Round-1 points: what is resolved and what remains**

Resolved:
- **P1 (attrition noise in cell 69):** a null and a fixed-trial variant were added and the bootstrap intervals dropped. A new issue came out of this; see remaining item 1.
- **P5 (speed correlations):** residual correlations were added. The ts confound is now stated.
- **P6 (weighted RMSE):** the counts are the same.
- **P9 and the glm chance levels:** added, and far above chance. It uses only 5 shuffles, and the shifted labels still agree with the true ones on about half the trials, which makes that null conservative.
- **dfr peak stability:** 192 of 200 bootstrap samples peak at 480 to 640 ms.
- **alt-transient-parallel variants:** p for the longest ts stays at or below 0.039 in every variant except soft normalisation (0.055).
- **P8:** documented in the findings.

Partly resolved:
- **P2:** the normalisation variants settle the PCA dependence and encoding specificity. Pooling across sessions cannot be tested with one session.
- **P4:** the variants are reported. The outcome stays sensitive to the number of components.
- **P7:** 12 latents beat 8 in all 4 datasets, so the best value is again the top of the grid. The training log-likelihood is still rising after 100 EM iterations. The inverted-U and sigmoid results do not change with 12 latents.

Remaining points that bear on a conclusion:
1. **alt-speed-unmodulated:** the observed slopes are below the Poisson null in 16 of 16 comparisons. The null is miscalibrated, or speed falls during the support. Comparing the null's mean speed with the observed mean speed would tell which. Until then the "no modulation" wording is not supported. The outcome itself rests on an uninformative test and does not change.
2. **alt-threshold-monotonic:** the outcome depends on dimensionality (−230 ms with at least 2 components, −70 ms with at least 3), and the wording about crossings is overstated (item 1 in section 2).
3. **encoding-r2 and encoding-bayes-beats-linear:** the match to te is reproduced. Specificity to u is not shown, and the short-in-long control shows the same Bayesian advantage. The Summary's wording on this needs correcting (item 2 in section 2).
4. **speed-predicts-tp, trial-by-trial variant (cell 65):** each trial's speed is measured from Set to that trial's own Go on smoothed single-trial rates. Shorter trials therefore have a larger share of bins near Go and fewer bins to average noise over. This could produce a negative speed–tp correlation within ts by itself. It is unchecked; a Poisson null with matched durations would settle it. The outcome is judged on condition means, so it does not change.
5. **Not available:** Tables S1–S3 and Fig. S5. The fitted wm and wp and the paper's own random-axis values still cannot be compared.
