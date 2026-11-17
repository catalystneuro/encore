I checked `claims/rich-2014.yaml` against the paper and supplement and made 11 changes; the file is ready for an attempt. Three problems remain open, listed below. Nothing was committed.

**Checker:** `claims/rich-2014.yaml: 27 claims, 27 quotes, 15 statistical values, 0 problems`. It said 17 statistical values before my edits; the two I removed account for the difference.

**Changes, by claim**
- **fig2-individual-poisson, figs6-few-field-cells-uniform:** removed the statistics entries. "0/61 cells with P < 0.05" and "0/5 pFDR<0.05" count cells or groups against a threshold, so they are method, not results. The 0 count stays as an expected value.
- **fig3b-overdispersion:** the statement says the fit is poor in each animal, as the Fig. S7A legend does, but the criterion accepted four of five animals. It now needs all five, and the expected number of cells with no field is computed per animal.
- **figs10-no-track-or-speed-influence:** the paper never defines a corner, and the 45-degree rule had been called a standard choice even though it changes panel B. It is now open, with two readings: 45 degrees or 90 degrees.
- **figs15-higher-threshold:** removed the requirement that the counts stay overdispersed. The S15 legend names no such test. The dispersion is now only reported.
- **figs16-anatomy:** the paper does not say what "not consistent within individual animals" means. It is now open, with two readings: fewer than three animals significant, or at least one animal with the opposite sign.
- **fig4b-single-field-proportion:** the criterion named two denominators (all cells, place cells) but judged on all cells only; it now judges on either and gives the formula for the second. I also corrected the note on the printed parameters: 5 to 10% falls at about 150 to 550 m and 1 to 2 m.
- **fig4c-active-subsets:** removed the condition that the fitted equal-rate proportion between environments over 20 m be below 0.05. The S18 legend says that of its high-rate condition only. The fitted equal-rate model gives about 0.25 for 20 m against 50 m, so the condition would have failed even on the paper's own model. The legend's statement is now checked on the twice-the-mean variant.
- **figs5-silent-cells-low-rate:** the criterion required every cell without fields to fall below the median cell with fields, which the paper never says. It now uses a one-sided Mann-Whitney group test, named as a reading. Its readings are renamed Z-a and Z-b, because E-a and E-b were already used in fig2.
- **fig3e-memoryless-recruitment:** the spacing readings are renamed V-a and V-b, because S-a and S-b were already used in fig2.
- **figs17-propensity-across-environments:** set the tolerance on the between-environment value to 0.015 (was 0.02). That is the half-width of 0.20 to 0.23, the rule the criterion itself states.

**Open**
- **Figure readings unchecked:** no PDF renderer was available, so I could not check the values read from figures: the S7A per-animal means, the S17 points and intervals, the roughly 5 m spacing in Fig. 3E, and the S15B threshold line. The S7A means are at least consistent with the text: they imply a pooled mean of 3.2 to 3.6, against 3.5 from r and p.
- **fig3c-extrapolation-500m:** the printed parameters give about 436 m, outside 500 ± 50 m. The paper says only "~500 m", so the result depends on the unrounded fit.
- **fig4b-single-field-proportion:** the "factor of 10 in L" standing for "a wide range" is not from the paper. The printed parameters give under a factor of 4, so as written the claim would likely fail on them. The Fig. 4B legend, which would settle the range of sizes and the denominator, is missing from the text supplied.

Every main finding has a claim, and none comes from outside the paper.
