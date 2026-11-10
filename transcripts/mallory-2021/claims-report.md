I wrote `claims/mallory-2021.yaml` and did not commit it. The quote checker passes every quote. It still flags two p-values, which I confirmed by reading: P = 2.0e-7 and P = 8.0e-4 in the Supplementary Fig. 7 legend. The checker does not recognise the trailing ".0" in how they are printed.

**Text read**
- **Paper:** the version of record (Europe PMC full text, PMC7844029), with Methods and figure legends.
- **Supplement:** the three PMC supplementary files. These are the Supplementary Information (legends of Supplementary Figs. 1 to 12), the peer review file (only an editorial note) and the reporting summary.
- **PDFs:** not opened. No claim needed a number that appears only inside a figure.
- **Code:** `khardcastle/spline-lnp-model` at commit 34b470f is the spline LN model with forward search. `GiocomoLab/ln-model-of-mec-neurons` at commit 643386b is the older 2017 model; I read it and did not follow it. Neither repository holds the pitch, roll or eye analyses, tuning-curve shapes, stability or PCA clustering, so those methods come from the Methods and legends. Where the code differs from the Methods (3-s fold sections, position bins of box × 10/100, 12 head-direction points), I followed the Methods and recorded the code's settings as variants.

**Claims:** 42 in all, every one with a quote. 23 have statistics (53 values), 33 have expected values with tolerances, and all 42 have a criterion. All are `data: dataset`.

**Details the paper leaves open, with the readings named for each:**
1. **How the cross-validation folds are built** ("10-s sections"): consecutive sections assigned to folds in turn, or assigned at random. The code's 3-s sections are a variant.
2. **Restricting behaviour to its inner 95% or 98%:** keep only time bins where every variable is in range, or clip each variable separately.
3. **Contribution to model performance:** (full − reduced) / full, which gives the paper's ranking with body position strongest; or 1 minus that, which is the literal wording. Performance is the mean over the 10 folds, or a single held-out section as in the code.
4. **"Explored" range for classifying tuning-curve shape:** the share of the preset range covered between the behavioural percentiles, or the share of bins with any occupancy.
5. **A cell's preferred direction:** slope sign for linear cells and the side of the curve's maximum for the rest, or the side with the larger slope.
6. **Asymmetric versus symmetric velocity cells:** the two slopes have opposite signs, or the rule from the Methods' shuffle comparison.
7. **Tuning curves compared across the tracks with and without landmarks:** model-derived curves refitted on each track, or raw curves.
8. **One P printed for several pairs:** read as the largest P of those pairs.

**Choices I made, where the paper's wording forced one:**
- Eye units for the preset bounds are fixed as % of eye width. A fraction of eye width would put the bounds beyond the eye.
- "P = 3.3–23" and "P = 1.9–20" are read as 3.3e-23 and 1.9e-20.
- The 52 body-speed cells in the azimuthal head velocity stability comparison are read as the Cohort 1 body-speed cells, the count Supplementary Fig. 3b gives.
- The spline tension is set to 0.5, the code's value; the Methods allow 0.5 to 0.7, and 0.7 is run as a variant.

**Missing from the paper for some claims:**
- **Fig. 8e** (eye tuning preserved in cells that encode both body and eye position) has examples only and no test. Its criterion uses a signed-rank test chosen here and is marked as resting on that assumption.
- **Smaller unstated settings:** the number of label scrambles for the clustering tests (1000 used, a standard choice), the pairwise alpha for the eye-stability comparisons (0.0167 used, as in the Fig. 5 legends), and the resampling for model-versus-raw tuning-curve correlations.
- **The no-landmark sessions** (Fig. 8, 6 sessions in 6 mice): the paper does not say whether they are among the 11 main head-fixed recordings.
- **Cohort 2** includes recordings from three earlier papers and has no head-tilt sensor (IMU). The raw data are said to be on figshare. Whether DANDI:000053 holds Cohort 2 and the no-landmark sessions is for the author to check.
