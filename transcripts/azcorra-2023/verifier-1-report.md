# Verifier report, round 1: Azcorra, Gaertner et al. 2023 on DANDI 001038 (0.241111.1719)

The claims file has 29 claims. I judge 18 reproduced, 7 partially reproduced, 1 not reproduced and 3 blocked. One caveat applies to most of them. The striatal locomotion selection does not reproduce: the notebook has more recordings than the paper in all five groups. So the 18 claims that depend on that selection were tested on a larger set of recordings than the paper's.

I saved the full text (PMC10545540, CC BY 4.0) under `paper/`. I tested the helper functions on synthetic inputs and they behaved correctly: `crosscorr` lag sign and formula, `fastsmooth` centring, the `responses` windows, `triggered` alignment, the `pca_uncentered` sign convention, `select_acc_dec` and `bad_405`.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| recording-counts-locomotion | not_reproduced | 0 of 5 within tolerance (cell 16): 50/28/82/89/85 against the paper's 42/22/47/74/75. Anxa1 is 74% over. Mice are 14/7/9/14/15 against 12/6/10 (Methods 9)/14/14. |
| recording-counts-stimuli | reproduced | 8 of 8 counts match exactly (cell 18), as do the mouse counts, the Aldh1a1 30 and the unconsumed-reward fractions 1/29, 0/17, 6/57 from the Methods. |
| fig2f-xcorr-direction | reproduced | Integral over lags 0 to 1 s (cell 20): Vglut2 −0.033 and Calb1 −0.036 (both negative), Anxa1 +0.014 (positive). All p×3 < 1e-4. The 405 nm control integrals are about 0.005. |
| fig2i-trough-lag | partially_reproduced | Methods measure (cell 22): Vglut2 0.416 s, within tolerance. Calb1 0.140 s is outside 0.17 ± 0.017. p×3 = 2e-8. The code variant (0.436, 0.160) would pass. |
| fig2jk-pca-variance | reproduced | PC1 58.32% and PC2 22.09% (cell 24). Both are within tolerance, but only just (bounds 57.78 and 22.11). The total is 80.4% against 84.3%. |
| fig2l-pc-angles | reproduced | Mean angles 140.1/208.8/233.3 against 141/208/239 (cell 26). The three tests give p×3 ≤ 1.3e-5. |
| fig2g-event-counts | reproduced | Accelerations 131.4 ± 75.1 and decelerations 129.2 ± 95.0 against 135 ± 77 and 138 ± 101 (cell 28). Both within tolerance. |
| ed7f-prob-transient-after-event | reproduced | 61.8%, 63.9% and 55.8% against 62.4, 62.3 and 57.5 (cell 30). All within tolerance. |
| ed6f-dec-peak-timing | partially_reproduced | Vglut2 0.476 s and Calb1 0.320 s are both outside tolerance (0.35, 0.23). Vglut2 is later, p = 0.001 (cell 32). |
| fig5ab-transient-scaling | partially_reproduced | Ratios 239/266/222% (cell 34). The Vglut2 ratio is outside 214 ± 21.4. All three exceed 100% with p×3 ≤ 0.002. |
| fig4g-reward-response | partially_reproduced | Methods windows give 8.77/13.73/6.69 (cell 36). All three are positive with p < 0.05, and all three are just outside tolerance. The code windows give 7.90/12.40/5.88, which matches the paper to 0.02. |
| fig4g-anxa1-no-reward | reproduced | Mean −0.42, signed-rank p×4 = 0.12, which meets the p ≥ 0.05 criterion (cell 38). |
| fig4g-airpuff-response | partially_reproduced | Vglut2 16.8, Calb1 5.41 and Anxa1 −3.66 are within tolerance. DAT is 2.69 against 5.3, with n = 69 matching. All four directions are significant (cell 40). |
| fig4h-reward-vs-airpuff | reproduced | Vglut2 air puff > reward, p×4 = 9e-6. Calb1 reward > air puff, p×4 = 0.003 (cell 42). |
| fig4i-reward-size | partially_reproduced | Calb1 4.43 (p×4 = 0.005) and DAT 2.33 are both significant but outside tolerance. Vglut2 (p = 0.22) and Anxa1 (p = 1) are not significant, as the paper says. The code windows give 3.93/1.83/0.95/0.04, which matches the paper (cell 44). |
| ed8f-rest-reward-same | reproduced | Vglut2 and Calb1 both p×4 = 1 (cell 46). The n differs from the paper: Calb1 8 against 10, Vglut2 from 3 mice against 6. |
| fig6c-kmeans | reproduced | Median accuracy 92.6% over 100 seeds (cell 48). The n is 19/14/35, against the paper's 16/11/16. |
| fig7f-soma-axon-correlation | reproduced | Means 0.650/0.672/0.530/0.377 (cell 50). Anxa1 is just inside tolerance (bound 0.522). All p×3 ≤ 0.002 against DAT. |
| ed9c-snc-stimulus-responses | reproduced | Vglut2 and Calb1 reward and air puff responses are positive with p×4 ≤ 0.008. The Anxa1 reward test gives p = 1. The n matches the legend within 1 (cell 52). |
| ed9k-snc-variance-explained | reproduced | Total 75.05%, PC1 48.09% and PC2 26.96%, all within 10% of the legend values (cell 54). See problem 5 for the denominator. |
| ed1h-aldh1a1-depth | partially_reproduced | Spearman ρ = −0.57, p = 1e-8. The mean integral at depths under 2.5 mm is +0.024, as expected. At depths over 3 mm it is +0.0001, where the criterion needs a negative value, and that bin has only n = 5 (cell 56). |
| ed1i-aldh1a1-reward-locomotion | reproduced | ρ = −0.51, p = 0.011, n = 24 (cell 58). |
| fig3a-overlap-locomotion | reproduced | Calb1 mean −0.027 and Anxa1 +0.009, rank-sum p = 1e-4 (cell 60). Counts do not match: Calb1 has 17 recordings against the legend's 5, Anxa1 20 against 16. |
| fig4l-overlap-stimuli | reproduced | Calb1 reward 14.35 against Anxa1 0.94, p = 5e-4. Anxa1 air puff −2.06. The counts 9/13/17 and mice match the legend exactly (cell 62). |
| snrna-nuclei-qc | reproduced | 12,065 nuclei, mean UMI 3,436, mean genes 1,684 (cell 64). |
| snrna-anxa1-within-aldh1a1 | reproduced | Odds ratio 8.2, p = 2e-107. Aldh1a1 is detected in 0.77 of Anxa1 nuclei; Anxa1 in 0.11 of Aldh1a1 nuclei (cell 66). |
| snrna-clusters | blocked (other) | Not in the dandiset. The API lists 1238 files, all NWB photometry, and no snRNA-seq. Data are in GEO GSE222558. The exact 15-cluster Seurat SCTransform result cannot be reproduced in Python. A partial test is possible: whether an Anxa1-enriched cluster exists inside the Aldh1a1 nuclei, using scanpy on the GEO matrices. |
| scrna-meta-integration | blocked (other) | Not in the dandiset. Needs four external datasets and Seurat/LIGER integration. No part was attempted. |
| histology-anxa1-cre | blocked (data_missing) | No images in the dandiset (all 1238 assets are NWB). They are on Zenodo 7909331, which the dandiset metadata does not link, and need manual cell counting. |

## B. Problems

1. **[affects a conclusion]** Locomotion selection (`recordings_table` `loco`, cell 16). Every group has more recordings than the paper. The four Methods criteria do not account for the difference: the 405 nm threshold step removes 0 to 10 recordings per group. The excess is unevenly spread:
   - Anxa1 is +74%.
   - Calb1 in the overlap region is 17 against 5 (cell 60), although Calb1 overall is only +6.
   - The k-means Anxa1 set is 35 against 16 (cell 48).

   The stimulus counts match exactly, so the data, the SNR filter and the region conversion are not the cause. Some criterion is missing. All 18 locomotion-dependent outcomes rest on a different set of recordings, and the passes of fig2jk and fig7f are within about 1% of their tolerance bounds.

2. **[affects a conclusion]** Response windows (cells 36 and 44). The code windows reproduce the paper's means to 0.01 to 0.05 in seven of seven values. The Methods windows run 10 to 14% higher. This is strong evidence that the paper's numbers come from the code windows. Under the claims file's rule (Methods is the main result), fig4g-reward-response and fig4i-reward-size come out partial.

3. **[affects a conclusion]** Deceleration peak timing (cell 32, `peak_methods`). Both means are 0.09 to 0.13 s later than the paper. The code variant does not close the gap, and the cause is unexplained. The trough lag (cell 22) matches, so the trigger alignment does not look wrong.

4. **[affects a conclusion]** DAT air puff response (cell 40) is 2.69 against 5.3 with a matching n of 69, while the other three groups match. The cause is unexplained.

5. **[does not affect a conclusion, unchecked]** ed9k denominator (cell 54). `var.sum()` sums over the 160 economy components of the striatal PCA. It is not the SNc data's total variance, trace(XsᵀXs). On synthetic data a 160-component basis captured only 79% of other data's variance, so the percentages could be inflated. If the code does the same, the port is faithful. The outcome would only flip if the basis missed more than about 7% of the SNc variance.

6. **[does not affect a conclusion, unchecked]** `RewardNoRest = reward & ~rew_rest` (`_read`). If a rest interval ends before its reward interval, this creates a false onset. A synthetic test showed exactly that. Event durations were never checked. The ed8f counts also differ from the paper (Calb1 8 against 10, Anxa1 36 against 42, DAT 33 against 42).

7. **[does not affect a conclusion]** `rew_long` and `rew_short` are not shifted by the 1 bin that `reward` is (`_read`). The size-split responses are aligned 0.01 s differently from the overall response.

8. **[does not affect a conclusion]** fig4i requires at least 3 small and 3 large rewards. That gives Anxa1 37 and DAT 50, against the paper's 42 and 55.

9. **[does not affect a conclusion]** fig2l uses the arithmetic mean of angles on 0 to 360°, as the code does. The circular means differ a lot (Anxa1 301° against 233°), so the comparison of means depends on where the circle is cut.

10. **[does not affect a conclusion]** fig5ab (cell 34):
    - The ratio uses every recording with a value in either quintile, while the test uses only paired recordings.
    - The size analysis uses the recomputed onsets. These keep events after unconsumed rewards (146 files have extra onsets, cell 9).

11. **[does not affect a conclusion]** `kmeans_accuracy` (cell 48) maps clusters to subtypes by median label. That median can be non-integer, and two subtypes can map to the same cluster. This follows the code. The median accuracy over seeds is stable, but single seeds range from 41 to 93%.

12. **[does not affect a conclusion]** ed1h: the partial outcome rests on a bin over 3 mm deep with only 5 recordings.

13. **[does not affect a conclusion]** The blocked reasons in cell 0 ("not runnable") are not one of the allowed categories.

14. **[does not affect a conclusion]** `responses` fills NaN values with `np.roll`, which wraps around the end of the array. NaN fraction is at most 5e-5. The scipy exact tests differ slightly from MATLAB's normal approximations, but no p-value is close enough to 0.05 to change an outcome.

## C. What I could not check, and the output that would settle it

- **Cause of the locomotion overcount.** Needed: counts for each step split by location, by single against dual fiber, and by session with or without stimuli, plus the list of recordings per mouse (Anxa-I767 has 19), compared with the paper's per-mouse counts if the source data has them.
- **ed9k denominator.** Needed: the fraction of trace(XsᵀXs) that the 160 striatal components capture.
- **RewardNoRest.** Needed: the distribution of Events durations for the long/short rows against the rest rows, and the number of RewardNoRest onsets against the number of rewards minus rest rewards.
- **DAT air puff and deceleration peak timing.** Needed: the DAT air puff split per mouse with the code windows, and the deceleration-triggered average for each subtype plotted with the paper's peak times marked.
- **ed1h depth.** Needed: the range of `fiber_depth_in_mm` and its relation to the DV coordinate, to confirm it is depth from the brain surface as the Methods define it.
- **Blocked claims.** I did not check GEO or Zenodo contents; only the DANDI asset list, which confirms none of these data are in the dandiset.
