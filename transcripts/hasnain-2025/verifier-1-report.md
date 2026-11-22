**Verifier report, round 1: Hasnain, Han & Economo 2025 on DANDI:000363 (0.231012.2129)**

The claims file has 19 claims. 11 rest on the paper's own recordings and 8 on the MAP data. Cells 21 and 31 still contain the author's result text. I read them but reached the outcomes below on my own from the printed outputs.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| own-recordings-cohort, fig1i-selectivity-proportions, fig2c-subspace-variance, fig2e-potent-only-units, fig2f-letn-preference-like-un, fig2gh-letn-span-subspaces, ed2f-false-negatives, fig3c-network-beats-linear, fig3d-letn-un-movement-encoding, ed3-letn-fast-switch, ed3a-cd-early-un-not-letn (11) | blocked (data_missing) | I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174 files in every version). Searching the archive for "Hasnain", "Economo", "extratelencephalic" and "movement-null" finds no dataset with the paper's own recordings. All 11 need phototagged L-ETNs or the paper's videos, so no part can be tested on MAP. |
| map-session-selection | not_reproduced | Cell 12: 17 bilateral sessions from 9 mice (tolerance 20 ± 2). ALM and medulla: 5 sessions from 4 mice, against 11 (Methods) or 16 (Results). Unit counts: ALM 300 (paper 604), medulla 340 (paper 724), right ALM 858 (paper 961 ± 96.1). Only left ALM (1001) is within tolerance. |
| fig4b-medulla-selectivity | partially_reproduced | Cell 16, Bonferroni, E1 reading: sample 34.1%, delay 52.9%, response 86.5%, against 7 / 21 / 49. The order holds (response highest, sample lowest), which the criterion counts as partial, but every value is 2 to 5 times the paper's, under every seed and alpha. |
| fig4c-alm-null-potent-similar | partially_reproduced | Cell 18: the absence holds under every main reading (p 0.13 to 0.26, n = 5). Means are out of tolerance (V1 54.5 / 77.3; V2 null 24.0, below the 28.6 floor). Only the example.m z-score, which M3 calls a "variant", matches (30.7 / 29.1, p = 0.119). Whether a variant counts as a reading is ambiguous in the claims file; if it does, this becomes reproduced. |
| fig4c-medulla-null-smaller | reproduced, under the criterion but fragile | Cell 18: B2 with V2 gives null 28.5 and potent 51.2 (both within tolerance), p = 0.0097, stable over 5 seeds. That is 1 of 15 reading combinations. The main reading gives p = 0.445, and V2 is the reading the claims file says departs from the Methods formula. See B4. |
| fig4d-alm-predicts-medulla-null | not_reproduced | Cells 27 and 28: R2 at λ = 0.01 is strongly negative under every reading and seed (ALM to medulla −153 to −326%; ALM to ALM, A1 reading, −2035 to −7423%). With a larger λ (variant), ALM to ALM (5.7%) falls below ALM to medulla (21.3%), the reverse of the paper. B2 explains why this failure says little about the paper's numbers. |
| fig4d-decoding-asymmetry | not_reproduced | Cell 27: asymmetry p = 0.46 to 0.89. Medulla to ALM R2 ranges from −378 to −184%, against 21 ± 6.7%. |
| fig4e-medulla-null-lower-dimension | not_reproduced | Cell 23: N1 p = 0.646 (medulla lower in 2 of 5 sessions). N2 p = 0.092 (lower in 4 of 5). No reading reaches p < 0.05. With n = 5 against the paper's 16 the test is weak. |
| fig4f-medulla-null-not-spanning-alm | not_reproduced (by inspection) | Cell 33 plot: medulla points cover nearly the whole extent of the ALM points. Only 2 of 31 grid cells that hold ALM units have no medulla unit, and 5 of 34 medulla cells lie outside the ALM cells. The neighbour statistic cannot be trusted (B3). |

### B. Problems

1. **[affects a conclusion]** Session and unit selection (`select_sessions`, cells 6 and 12). Every Figure 4 claim runs on 5 sessions with 300 ALM and 340 medulla units, against the paper's 16 sessions with 604 and 724. The notebook says no reading of 'good' other than `classification` can place units in the CCF, because `anno_name` is filled only for those units. It never checked whether the electrodes table carries CCF coordinates or labels per electrode, which would let the `unit_quality == 'good'` reading be tested. The paper's "unit classification based on common spike sorting metrics" fits that reading at least as well. Sweeping the threshold shows the counts are sensitive: at 20 units per region, 31 bilateral and 14 ALM and medulla sessions qualify. The small n also weakens the absence claim (fig4c ALM) and the not-reproduced verdict for fig4e.

2. **[affects a conclusion]** Decoding (`ridge_r2`, cells 27 to 31). The extreme negative R2 values (down to −55,507% in one session) were not traced to their cause, and two choices that could change the outcome were not run.
   - The projections come from baseline-z-scored rates with heavy tails: |z| reaches 95 to 213 (cell 14, `z_absmax`). With λ = 0.01 the ridge is close to plain least squares (condition number about 1e6, cell 30), so outlier test trials blow up. The example.m z-score, which brings |z| down to about 30 to 60 and is the only variant that matched the ALM variance explained, was never used for decoding.
   - The R2 denominator is open. The per-bin across-trial variance used here strips out all time-locked variance. The alternative, variance over the whole averaged span, is not run, and the claims file does not list it (M8). I report this as a gap in the claims file, not a correction.
   - My synthetic test shows `ridge_r2` itself is correct: it recovers R2 = 0.90 against an expected 0.91.

3. **[affects a conclusion]** UMAP (`umap_run` and `nn_stats`, cell 33).
   - The medulla of sub-460436_ses-20200109 has d_null = 1 (cell 14). A rank-1 reconstruction, z-scored per unit and compared by cosine distance, maps all 65 units onto two points (plus and minus one time course). That fits the stacked medulla points at x ≈ 12 to 16: the medulla 95th percentile on x is 15.96, against 1.61 for ALM.
   - The label-shuffle null mixes units across sessions. So "19.3% of ALM units with no medulla neighbour (shuffled 0.1%)" and "60.6% of medulla units with an ALM neighbour (shuffled 99.8%)" measure clumping by session and by low rank, not by region.

4. **[affects a conclusion]** Figure 4c readings (cell 18). No single reading reproduces both Figure 4c claims. B2, which gives the medulla result, also makes ALM null fall below potent (p = 0.024, against the paper's absence of a difference). The example.m z-score, which matches ALM, gives a medulla null mean of 31.5, outside 26.4 ± 3.9. The medulla "reproduced" therefore rests on one of 15 combinations, chosen per claim.

5. **[does not affect a conclusion]** Selectivity is 2 to 5 times the paper's (cell 16), and the notebook offers no diagnosis. The per-session sample-epoch values range from 1.7% to 48.4%. The code checks out on synthetic data: `selectivity_p` is calibrated (0.75% of null units at p < 0.01, 6.8% at p < 0.05), and the kernel in `rates` is causal. Non-stationary trial order, which would bias the permutation test, was not looked at. The claim stays partial either way.

6. **[does not affect a conclusion]** Cell 31's text does not match the printed outputs:
   - ALM to ALM range: text says −7333 to −2712, output shows −7422.6 to −2713.5.
   - λ = 100 asymmetry: text says 13.5 points, p = 0.040; output shows 13.20, p = 0.0369.
   - λ = 100 values: text says 5.8% and 7.8%; output shows 5.72% and 8.13%.

7. **[does not affect a conclusion]** The subspaces used for decoding and UMAP are fitted on all trials, test trials included (`fit_region`, cells 14 and 25). This is unsupervised and within one region, so the leakage is small.

8. **[does not affect a conclusion]** The stated deviations look reasonable:
   - `shuffle_dimension` uses 100 shuffles on every 4th bin. On synthetic data it recovers the true rank, including with units scaled up 10 to 40 times.
   - Otsu's threshold sits in the trough of a clearly bimodal histogram (cell 10).
   - `movement_mask` handles B1 and B2 and the bout merging correctly on synthetic input.
   - Leaving out early-lick and photostimulation trials is a reasonable assumption.

9. **[does not affect a conclusion]** `fit_region` includes bins with no tracking (mask −1) in the total covariance C used for variance explained.

### C. What I could not check, and the output that would settle it

- **Unit selection under the `unit_quality` reading:** the electrodes table's column names, and whether each electrode has a CCF label or coordinates. If it does, per-session counts of `unit_quality == 'good'` units by CCF region.
- **Trial filtering:** the unique values of `outcome`, `photostim_duration` and `early_lick` that `trial_mask` relies on. In particular, whether "N/A" is the only label for trials without stimulation.
- **The UMAP artifact:** the Figure 4f embedding coloured by session, the per-session d_null next to it, and the neighbour null with labels shuffled within session.
- **Decoding:** results under the example.m z-score; R2 with the variance over the whole span as denominator; R2 per bin over time; and the across-trial target variance at each bin.
- **Selectivity:** the fraction of selective units against a test that respects trial order (for example, shuffling in blocks), and the share of right trials by position in the session.
- **Movement mask:** the fraction of moving bins per epoch. The reported 30 to 80% overall cannot be checked against the paper's moving and stationary bins.
- **Baseline window:** the MAP sample-cue time relative to the go cue, to confirm that −2.1 to −1.85 s falls in the inter-trial interval. The speed traces in cell 10 suggest the sample starts near −1.85 s, but this was not checked from the trial table.
