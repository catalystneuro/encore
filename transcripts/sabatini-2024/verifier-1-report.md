**Verifier report, round 1: Sabatini & Kaufman 2024 on DANDI:000070 (two notebooks, 34 claims in the claims file)**

Overall: 13 reproduced, 10 partially reproduced, 10 not reproduced, 1 blocked.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| data-composition | partially_reproduced | 72 conditions (36 straight, 36 curved). Trials are 1595/2121 under reading (a) and 1381/1884 under (b), all within tolerance (nb1 cell 7). The unit criterion cannot be applied: the files hold 96 unsorted threshold-crossing channels per array, none marked single- or multi-unit (cell 5; the archive's file metadata agrees). |
| jpca-fit-r2 | partially_reproduced | Straight 4/4 and curved 4/4 in range under both readings. All conditions: 2/4 (best) or 1/4 (skew) (cell 20). The signed-rank test gives p<0.001 only in M1-J; it is reported, not decisive. |
| jpca-variance-explained | reproduced | 9.1, 10.6, 10.8 and 6.8%, all in 6.3–13.2%; s.d. below 13 (cell 22). |
| single-lds-variance | not_reproduced | 77.3–82.6% under (a) and 79.6–86.5% under (b); all above 72.6% (cell 28). |
| fig2c-condition-lds-variance | reproduced | k = 5, 5, 7, 7 (or 5, 5, 7, 5); variance explained 83.2–94.1% (cell 31). |
| fig3a-eigenvalue-clusters | not_reproduced | Median pair frequencies are off: M1-J [0.85, 2.38] and M1-N [0.63, 1.74, 3.19] Hz. Only 3 of 10 pairs are within 10% (cell 35). |
| fig3c-eigenvalue-distance-auc | not_reproduced | AUC 0.58–0.72 with the half-split null and 0.59–0.80 with the Poisson null. Only PMd-N is within 0.459–0.638 (cell 38). |
| suppfig2-eigenvalues-from-kinematics | not_reproduced | Pooled R² 0.247 or 0.298, against 0.10 ± 0.05 (cell 42). |
| fig3g-basis-frequencies | partially_reproduced | Every dataset has 3–4 rotation pairs plus one offset. Only 5 of 14 frequencies are within 10%; the lowest is 0.61–0.73 Hz everywhere (cell 9). The criterion has no partial clause; I read the count and offset holding while the frequencies fail as partial. |
| tbf-variance-explained | reproduced | 92.3–97.1%, s.d. ≤1.3 (cell 11). |
| tbf-shuffle-control | reproduced | Shuffled 35.1–45.6%; rank-sum p ≈ 4e-25, real higher (cell 14). |
| fig3h-recoverability | reproduced | Real 95.1–96.6%, rank-sum p<0.001 (cell 15). Chance is 84.8–87.8%, above the paper's stated 63–80% in all four; it is inside only because the upper bound is widened to 88. |
| fig3i-duration-warping | not_reproduced | Unwarped M1-N rho = 0.013 (paper −0.26) and PMd-N 0.246 is out of range. Warped (truncate) is in range in only 2/4 (PMd-J −0.06, PMd-N −0.27), so the partial condition also fails (cell 18). |
| suppfig3-model-comparison | not_reproduced | Under the claims file's main reading, held-out TBF (73.5–88.8%) is below the in-sample LDS (83.2–94.1%) in 4/4. The in-sample variant reproduces (cell 44). See problem 3. |
| fig4b-plane-alignment | partially_reproduced | 13 of 14 rotations have AUC 0.83–0.94 with signed-rank p<0.001. PMd-N 3.65 Hz has AUC 0.545 (cell 48). |
| fig4c-subspace-excursion-angles | partially_reproduced | Counts are in range for 3 of 4 datasets. PMd-N gives 23–25 (saturating at the 25-dimension cap); 10 of 14 counts in range (cell 57). |
| rotation-orientation-dimensionality | not_reproduced | PCs to 80% are 3–24 (3/14 in range) and participation ratio 2–20 (2/14), under both PCA readings. The SNR dimensions (13/14) are the only part that holds (cell 60). |
| fig4d-jpca-variance-correlation | not_reproduced | 5/6 planes at p<0.05 (83%, tolerance 59.4–72.6). Plane rho values are −0.09 to 0.92 and neither reading falls in 0.351–0.506 (cell 24). |
| fig4f-plane-alignment-explains-jpca | partially_reproduced | 5 of 6 planes have rho ≥0.738 with p<0.001; M1-N plane 1 is 0.685 (cell 26). |
| fig5a-frequencies-segregated | partially_reproduced | 35/36 comparisons pass with the paired test and 33/36 with rank-sum; 80% or more is the partial rule (cell 53). |
| fig5c-rotations-predict-rotations | reproduced | Rotation pairs explain 40.9–90.5%; 36/36 above the null at p<0.001 (nb2 cell 6). |
| suppfig6a-location-alignment | partially_reproduced | AUC 0.890, 0.698, 0.889, 0.764: 2 of 4 in range. Observed alignment is below noise with p<0.001 in all four (cell 50). The criterion has no partial clause; I read it as following fig4b, as its criterion says. |
| suppfig6b-location-dimensionality | not_reproduced | SEA angles >15°: 1–2 (needs 3.6–5.5). PCs 3–15 and participation ratio 2–7, 0/4 in range. SNR 3/4 (cells 61, 60). |
| suppfig6c-location-distinct-from-rotations | reproduced | Location-to-location alignment (0.89–0.97) is above location-to-rotation in every comparison, p≈0 (cell 54). |
| fig6b-location-predicts-rotations | reproduced | 65.4–83.0%; signed-rank p ≤ 7e-12 against the null (nb2 cell 9). |
| fig6c-location-tracks-direction | reproduced | Circular correlation 0.66, 0.72, 0.63, 0.36 after a per-dataset PC sign flip; p ≤ 9e-4 (cell 11). |
| fig6e-kinematics-predict-location | partially_reproduced | Linear in range 3/4 (PMd-N 0.24). Kernel in range 2/4 (Ornstein-Uhlenbeck) or 0/4 (Gaussian). All beat all 1000 permutations (cell 14). |
| fig7c-ldr-encoding | reproduced | Linear 68.9–85.4% and kernel 84.7–92.9%, p<0.001 against the null, under both kinematic readings (cell 17). |
| suppfig7a-not-memorization | reproduced | Kernel beats nearest-neighbour in all datasets, p ≤ 1.5e-4 (cell 19). |
| fig7c-standard-encoding-worse | reproduced | LDR models beat the standard models in 24/24 comparisons, p<0.001 (cell 22). |
| fig7f-ldr-decoding | reproduced | Mean over trials 88.9–93.3% (cell 25). |
| fig7f-decoder-beats-standard | blocked (too_large) | Only the single-trial kernel decoders are plausibly too large; the archive holds the spikes and hand position needed. The linear decoders and the decoders trained on trial averages were feasible and not run. GPFA is missing from the environment, which is not a data block. |
| suppfig8-no-output-potent-dependence | not_reproduced | p ranges from 1e-5 to 5e-10 in all datasets, below 0.036. The mean drop is only 0.3–0.9 points (cell 29). No EMG is in the files; I checked the NWB processing modules. |
| trial-curvature-decoding | partially_reproduced | 7 of 8 correlations in range with the svd kinematic reading; PMd-J y curvature is 0.092. 6 of 8 with the skew-normal reading (cell 27). |

### B. Problems

1. **[affects a conclusion] fig3i, `durations` and `warped_average` (nb1 cell 17).**
   - The criterion defines reach duration per trial and correlates each condition's mean duration. The notebook takes one duration from the condition-mean hand speed and warps every trial with it.
   - The warp scales `0 < st < wf` with `st` offset by +100 ms. That warps −100 to wf−100 ms, not −100 ms to the end of the reach as the notebook's own text says, so the last 100 ms of each reach falls in the unwarped segment.
   - The per-trial reading was not run.
2. **[affects a conclusion] Alignment event, `ldr.load_session`.** All data are aligned on online `move_begins_time`. The offline onset in the file differs by a median of 25 ms (J) and 52 ms (N), and the paper does not say which onset it used. The analysis was not rerun under the second reading, although the jPCA window (−160 to +40 ms) and the fig3i durations depend on it.
3. **[affects a conclusion] Claims-file misreading, suppfig3.** The Supplementary Figure 3 legend says the LDR model "explains greater neural variance when cross-validated" than the condition-specific LDS. The main reading compares held-out TBF with in-sample LDS. The notebook's own held-out LDS scores (cell 31, split 0.5, chosen k) are 0.675, 0.768, 0.835 and 0.788, all below held-out TBF (0.735, 0.810, 0.888, 0.817). A like-for-like comparison would therefore favour TBF in 4/4, though the windows differ.
4. **[affects a conclusion] fig4d and fig4f (cells 24, 26).** The Methods soft-normalise and mean-subtract before extracting the temporal basis functions. The notebook reuses the basis from unnormalised data and only rescales and centres the loadings.
5. **[affects a conclusion] Kernel length scales, fig6e and fig7c (nb2 cells 3, 13).**
   - The four reach parameters' scale depends on how the kinematic basis is normalised. Here they span ±30, from unit-norm SVD vectors summed cumulatively.
   - The paper's length scales (10³ and 400) were tuned to `kinFuncEval`'s unknown scale, so they do not transfer.
   - The scale was never checked. The fig6e kernel failures (Gaussian 0/4) may come from this.
6. **[affects a conclusion] fig7f-decoder-beats-standard (nb2 cell 30).** The linear decoders and the kernel decoders trained on trial averages (about 4,000 samples) fit in memory and were not run. They would have tested most of the comparison set.
7. **[affects a conclusion] Data difference, all claims (nb1 cell 5).** The paper used 79–118 sorted single and multi-units per array; the files hold 96 unsorted threshold crossings. The notebook states this, but it bears on the dimensionality claims (PCs, participation ratio, single LDS) that fail.
8. **[does not affect a conclusion] fig3c (cell 36).** The markdown says the Poisson null has 50 repeats; the code runs 30. The half-split null runs 150 repeats instead of 500. AUCs are stable across seeds (cell 40).
9. **[does not affect a conclusion] jpca-fit-r2, `per_cond` (cell 20).** It projects data that lacks jPCA's second soft-normalisation and PC centring onto the jPC plane, so the per-condition R² is approximate. It only feeds the non-decisive signed-rank test. The straight/curved pairing (condition 3j+1 with 3j+2 as the same target) is assumed and never printed.
10. **[does not affect a conclusion] suppfig8 (nb2 cell 29).** `Kp.mean(1)` removes the mean across the four kinematic variables at each sample, while neurons have their mean removed over time. This looks like a transposed MATLAB `mean`, and I could not verify it against `removePotent.m`. The drops are small and consistent, so p would likely stay below 0.036.
11. **[does not affect a conclusion] suppfig2 (cell 42).** Both members of each conjugate pair enter as targets, so every real part is counted twice in the pooled mean.
12. **[does not affect a conclusion] fig6e (cell 13).** The target offset columns come from a TBF fitted on all 72 conditions, including the held-out ones. Only the predictors are kept out of training.

I tested the helpers on synthetic data and they behave correctly: `eig_transform` recovers 0.5, 1.5 and 2.5 Hz and a 0.3 s half-life exactly; `lds_eigs_batch` returns 0.49, 1.51 and 2.50 Hz. `alignment_index`, `auc_folded`, `pca_dims`, `circ_corr`, `sea` and `split_halves` give the expected values. So the frequency, AUC and dimensionality misses are not helper bugs.

### C. What I could not check

- **Code the notebooks cite.** `warpTrial.m`, `removePotent.m`, `getRotations.m` and the jPCA codepack's R² definition were not available to me. These outputs would have settled problems 1, 2, 4, 5 and 10:
  - fig3i run with per-trial durations, and with the warp ending at st = wf + 100;
  - the whole pipeline rerun on `offline_move_onset_time`;
  - fig4d and fig4f with the basis re-extracted from soft-normalised, mean-subtracted data;
  - a fig6e and fig7c kernel sweep over the reach-parameter scale or length scale;
  - a print of the first rows of `Kp` and `Dsub` for suppfig8.
- **suppfig3.** A table of held-out LDS against held-out TBF on the same −160 to +850 ms window and split would show whether problem 3 changes the outcome.
- **fig7f-decoder-beats-standard.** The linear decoders and the decoders trained on trial averages, run against LDR with signed-rank tests.
- **Straight/curved pairing.** A print of target positions for conditions 3j+1 and 3j+2.
- **Plots.** The figures in nb1 cell 9 and nb2 cells 2 and 11 were judged only from the printed statistics.
