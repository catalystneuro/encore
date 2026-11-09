# Verification report, round 1: Liu, Nair et al. 2024 (doi:10.1038/s41586-024-07916-w), dandiset 001097 v0.260624.0330

**Bottom line:** 7 claims reproduced (fig1b, fig1c, fig1d, fig1e, fig1g, fig2f, ed10c), 2 partially (ed6e, ed7), 3 not reproduced (fig2c, fig2e, fig2i), 13 blocked. Two problems weaken conclusions. First, the notebook never checks that the deposited rSLDS weights line up cell by cell with the session files (ed6e, ed7). Second, the GLM cross-validation gives negative R² even on data with no behaviour signal, so the fig2e result says little about the paper's claim.

The paper's full text came from Europe PMC (PMC11499253) and is saved as `paper/PMC11499253.xml` and `paper/paper.txt`. I checked the helper functions on synthetic inputs and they are correct: autocorrelation, MATLAB-style smoothing, choice probability (against sklearn's ROC AUC), the ridge shortcut that leaves out the target cell, and the lagged regressors. The ACHW of a simulated AR(1) series came out at 7.2 s against an expected 6.9 s.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| fig1b-accepting-escalates | reproduced | Cell 17: accepting Spearman 0.74 (p 3e-6) and 0.59 (p 6e-4); resistance peaks at bin 2 and falls to 0.07. Both parts hold in both trial sets. Only 12 of 23 mice have a positive correlation on their own (cell 19). |
| fig1c-responsive-dominates | reproduced | Cell 21: all four readings (0.841, 0.844, 0.829, 0.835) are inside 0.755 to 0.923. |
| fig1d-male-drives-mating | reproduced | Cell 24: the mean of per-trial ratios over all annotated trials is 11.75, inside 10.17 to 12.43. This is the paper's own measure ("mean ± s.e.m."). The other five readings (7.1 to 9.3) are outside, and 11.75 is pulled up by one trial at 79.3. |
| fig1e-interbout-interval | reproduced | Cell 27: with 0.1-s merging, 14.00, 14.86 and 14.61 s, all inside 12.33 to 15.07. Counts: 1,540 bouts and 1,471 intervals in 69 trials, against the paper's 1,685 and 1,611 in 74. |
| fig1g-social-in-bouts-and-intervals | reproduced | Cell 30: all annotated trials, mean of per-bout fractions: 0.649 in bouts and 0.230 in intervals, both inside tolerance. The pooled and receptive-only readings fail, so this rests on one reading. |
| fig2c-few-tuned-cells | not_reproduced | Cell 32: tuned share is 6.4 to 35.3% across behaviours, median 20.8%, so even the "partially" rule fails. Problem 3 likely inflates these numbers. |
| fig2e-glm-behaviour-explains-little | not_reproduced, low confidence | Cell 35, contiguous folds: −0.078, −0.011, −0.048. Random folds: 0.234, 0.207, 0.323. The ordering and the below-0.25 rule fail under both. The negative values come from the cross-validation design (Problem 2), so this is a weak test. |
| fig2f-glm-coupling | reproduced | Cell 35: 0.450 over cells and 0.434 over mouse means, inside 0.414 to 0.506. It depends on fig2e, whose pipeline is questionable. |
| fig2i-persistent-cells | not_reproduced | Cell 39: the best reading gives 0.200 of cells above 25 s and a mean of 15.5 s; targets are 0.27 to 0.33 and 18 to 22 s. Per mouse the share ranges from 0 to 0.48 (cell 40). |
| ed3b-pencil-cup | blocked (metadata_insufficient) | No label marks the pencil cup (cell 51). The data may still be there: see Problem 12. |
| fig3a-rslds-fit | blocked (other) | Needs rSLDS fits; the `ssm` package does not build in the environment. |
| fig3c-integration-dimension | blocked (other) | Same as fig3a. By the notebook's own timing, the 15 fits would take about 2 h, so the build failure is the real block. |
| ed3s-integrator-model | blocked (other) | Needs the integration dimension in 15 mice. |
| ed4b-single-cell-ramps | blocked (other) | Could be partly tested in the 2 mice with deposited weights: correlate the weighted cells with an ideal ramp on the receptive day. |
| fig3k-perturbation-relaxation | blocked (data_missing) | Confirmed in the asset list: no perturbation sessions, and no LED labels (the `laser_on` epochs belong to the male-inhibition experiment and last about 300 s). |
| fig4b-persistence-during-intervals | blocked (other) | Needs the integration dimension. With weights, only m541's receptive day is usable, and it has 7 intromissions. |
| fig4d-persistence-male-inhibition | blocked (other) | None of the 8 male-inhibition mice has deposited weights. |
| fig4h-peak-before-ejaculation | blocked (other) | Ejaculation is annotated in 12 sessions, but none of them has weights. |
| fig5c-attractor-receptive-days | blocked (other) | Needs a dynamics matrix for each day; only one set of loadings per mouse is deposited. |
| ed6e-projection-unreceptive-days | partially_reproduced | Cell 42: in m541, mounting values are 0.616 on the receptive day against 0.232 and 0.191; in mouse 543, 0.608 against 0.643 and 0.626. The criterion holds in one mouse. This depends on the unchecked cell order (Problem 1). |
| ed7-achw-across-cycle | partially_reproduced | Cell 45: weighted cells are longer on the receptive day in both mice (28.4 vs 17.2 s, p 2e-5; 26.7 vs 9.1 s, p 2e-4). Other cells do not change in m541 (p 0.23) but do in 543 (p 0.005). Same dependency on Problem 1. |
| ed9j-ovx-hormone-priming | blocked (other) | Needs rSLDS fits; no weights for the ovariectomy series. |
| fig5k-receptivity-correlation | blocked (other) | The 42 trials are present but have no fits or weights. |
| ed10c-population-mean-uncorrelated | reproduced | Cell 48: the slope is not significant under any of the three readings (r² 0.015, 0.003, 0.027; p 0.30 to 0.73). The notebook has 42 trials where the paper has 50. |

## B. Problems

1. **[affects a conclusion]** Cells 9, 42, 45 (`match`): cell order of the weights is never checked. ed6e and ed7 assume column i of the per-mouse weights is column i of the natural-cycle session. `match` only reports the median best-match correlation over any cell (0.86 for m541 day 3, 0.80 for 543 day 1); it never checks that cell i's best match is cell i. A correlation of about 0.8 for what should be the same recording also means the per-mouse traces were processed differently. The weights are applied to the stored z-scored traces without checking that the scaling matches.
2. **[affects a conclusion]** Cell 35 and `cv_ridge`: the GLM cross-validation punishes slow drift. With contiguous folds, fold means differ when activity drifts, which pushes R² below zero. I tested this on synthetic drifting traces with no behaviour signal: an intercept-only model scored −0.07 and unrelated behaviour regressors scored −0.09. In the real data, 1,018 of 1,335 cells are below 0 for female behaviours. No intercept-only baseline is reported. "Both" scoring below "male" suggests choosing the penalty on the last fifth of the training set is unreliable. Random folds leak information through autocorrelation: the same null data scored +0.04.
3. **[affects a conclusion]** Cell 32: the choice-probability comparison set differs from the paper. The Methods compute choice probability between pairs of behaviours. The notebook compares each behaviour against all other interaction bins, so cells that ramp score high for behaviours that happen late (lordose, wiggle, intromission). The shuffle null ignores autocorrelation, so the 2-SD test barely filters (18 to 75% of cells pass it); the paper does the same.
4. **[affects a conclusion]** Cells 39 and 40, fig2i: possible mismatch in which mice are pooled. The Fig. 2i legend gives n = 4 mice for the bottom panel, but the notebook pools all 15. The "whole recording" reading also includes up to 7 min of unannotated imaging after the interaction.
5. **[does not affect a conclusion]** Cell 17, fig1b: trial count per bin falls from 69 to 11, so late bins contain only long trials. Combined with only 12 of 23 mice having positive per-mouse correlations, the escalation may partly reflect which trials remain.
6. **[does not affect a conclusion]** Cells 24 and 30: fig1d and fig1g each pass on one reading only. fig1d passes on 1 of 6 readings and depends on outlier trials; fig1g passes on 1 of 4.
7. **[does not affect a conclusion]** Cell 42: the integration factor in m541 is chosen with lags up to 300 s, where the authors' code caps at 50 s; with the cap the two factors tie. The outcome holds either way: with factor 1, m541 gives 0.619 against 0.483 and 0.488, and the ed7 variant in cell 46 also holds.
8. **[does not affect a conclusion]** Cell 45: the weighted cells are selected from a model fitted on the receptive day, which favours cells that are slow on that day. The paper has the same circularity.
9. **[does not affect a conclusion]** Cell 15: duplicate detection is incomplete. It only covers the 3-day series, so the receptive sessions of m928, m930 and m940 are never compared with their 7-day sessions. It also marks m438 WT day 1 as a duplicate on frame count alone, although its male annotation count (60) differs from the receptive session's (76).
10. **[does not affect a conclusion]** `raster`: each annotation is extended by one frame (0.1 s) past its stop time.
11. **[does not affect a conclusion]** Cell 13: m928 WT_7d day 2 fails the clock check but stays in fig1 and ed10c without comment.
12. **[does not affect a conclusion]** Cells 0 and 51: some blocked reasons are too broad.
    - ed3b: The Methods say imaging continued 3 to 5 min under the pencil cup. Cell 6 finds 7 receptive sessions with 1 to 7 min of unannotated imaging after the last annotation. Four of them (m541, m542, m543, m551) have 469 cells; the paper reports 470 neurons from 5 mice. An exploratory test of this tail is possible.
    - ed4b: can be partly tested with the two deposited weight sets.
    - Paper's own fallback: the Methods give a partial-least-squares regression onto a ramp (Extended Data Fig. 3d,e) as an independent way to find the integration dimension. The notebook never considers it. Using it for the ramp and persistence claims would be partly circular.

## C. What I could not check, and the output that would settle it

- **Cell order of the weights (Problem 1):** for each per-mouse file, the share of cells whose best match is the same index, and the same-index correlation.
- **Contents of the per-mouse files:** the dandiset description says they hold "low-dimensional latent factors from dynamical models", but the notebook only reads the weight table. A list of every object under `analysis` and `processing` would show whether latent time series or dynamics matrices are there. Dynamics matrices would make parts of fig3c and fig5c testable in 2 mice.
- **GLM (Problem 2):** the intercept-only cross-validated R² under the same folds, and R² computed within each fold.
- **Choice probability (Problem 3):** tuned percentages for pairwise behaviour comparisons, as the Methods describe.
- **Trace types:** I inferred from the counts that the 15 receptive files are raw fluorescence and the cycle and oestrogen files are z-scored. A per-file table of trace type would confirm it.
- **Pencil cup:** a per-session list of how long imaging runs past the last annotation, and the ACHW within that tail.
- **Duplicates:** frame and cell counts for the receptive sessions of m928, m930 and m940 next to their 7-day sessions.
- **fig1b:** the trial count per bin for the receptive and non-receptive subsets separately.

I did not run the notebook or stream any NWB file. Asset metadata came from the DANDI REST API only.
