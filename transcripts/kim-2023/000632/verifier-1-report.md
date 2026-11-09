**Verifier report: Kim et al. 2023 (doi:10.3390/ijms241310921) on DANDI:000632, version 0.231012.1930, round 1**

**A. Outcomes (12 claims in the claims file)**

| claim id | outcome | reason |
|---|---|---|
| fig3-1hz-co-equals-cross | reproduced | Cell 16, reading (b): Student p = 0.32, co/cross ratio 0.68 (n = 5 vs 6); reading (a) p = 0.31; every variant has p ≥ 0.30. This meets the criterion (p ≥ 0.05), but the evidence for "same" is weak: the means differ by 32%, and on 2022-11-29 alone p = 0.023. |
| fig3-770khz-co-enhanced | not_reproduced | Cell 18: the 770 kHz mean is higher (ratio 1.96 under (b), 1.67 under (a)), but Student p = 0.16 and 0.15. No variant reaches p < 0.05 (lowest is YP/MemBrite, p = 0.087). Readings (a) and (b) agree, so this is not blocked. |
| fig3-770khz-cross-same-as-1hz | reproduced | Cell 20, reading (b): p = 0.56, ratio 0.84; reading (a) p = 0.53; all variants p ≥ 0.38. |
| fig3-770khz-co-above-cross | not_reproduced | Cell 22: the co mean is higher (ratio 1.59 under (b)), but p = 0.20 under (b) and 0.19 under (a). The readings agree. |
| fig3-no-area-dependence | reproduced | The criterion judges it by fig3-1hz-co-equals-cross (cell 24, p = 0.32). It carries the same low-power caveat. The Figure 2 evidence the Discussion cites was not tested. |
| fig2-180-cancellation | blocked, data_missing | The Figure 2 recordings are not in 000632; the archive asset list has 24 Figure 3 files only. They are in DANDI:000631 (problem 1). |
| fig2-crossover-angle | blocked, data_missing | Same as fig2-180-cancellation. With 000631 in scope it might still be blocked as metadata_insufficient, because ROI angles come from a simulation the paper does not give. |
| fig2-facilitation-plateau | blocked, data_missing | Same as fig2-crossover-angle. |
| fig2-60-fold-co-counter | blocked, data_missing | Same as fig2-crossover-angle. |
| fig4-unipolar-pattern | blocked, data_missing | Not in 000632. DANDI:000633 holds the single- and paired-pulse images for Figure 4. The apex-versus-base ROI comparison in the criterion looks testable from it. |
| fig5-base-sawtooth | blocked, data_missing | Not in 000632. DANDI:000634 (10 FluoVolt strobe files) holds Figure 5. |
| fig5-apex-larger-polarization | blocked, data_missing | Same as fig5-base-sawtooth. |

**B. Problems**

1. [affects a conclusion] Cell 25 says the Figure 2, 4 and 5 data "are not public elsewhere". That is false. Each of these dandisets lists this paper's DOI in its metadata (relatedResource):
   - 000631: 15 assets, single- and paired-pulse trains at 1 Hz and 833 kHz (Figure 2).
   - 000633: 2 assets, single and paired pulse trains (Figure 4).
   - 000634: 10 assets, strobe FluoVolt imaging (Figure 5).

   The claims file pins dataset 000632, so data_missing is correct within that scope. But the stated reason for 7 of the 12 claims is wrong, and the claims file's dataset scope should be reconsidered. fig4 and fig5 at least look testable.
2. [does not affect a conclusion] Cells 3 and 11: the group sizes after removing the duplicate are 5/5/6/7 (as deposited, 6/5/6/7), against the paper's n = 6 per group. The notebook explains only the duplicate. The extra cross-770 kHz dish and the missing co-770 kHz dish are not discussed. Anisotropy (cell 9) supports the labels as deposited, so relabelling is not indicated, and the "as deposited" variant leaves every outcome unchanged.
3. [does not affect a conclusion] Cell 10 assigns the duplicated image (identical chunk index; file sizes differ by about 9 KB of metadata) to cross 1 Hz. This is a judgement from file numbering and anisotropy (0.13, inside the cross range). Running both assignments covers it: p = 0.32 vs 0.68 for fig3-1hz.
4. [does not affect a conclusion] `find_footprints`: on synthetic square arrays (my test) it puts the array center within 33 µm, puts each footprint within 70 µm, and gives parallelogram deviations of 53 to 185 µm. On the real dishes the deviations are 135 to 683 µm (median about 310, cell 12), so the center ROI may be off by up to roughly 100 to 200 µm in some dishes. The dev ≤ 400 µm variant gives the same outcomes. The radius estimator reads about 25 µm high (775 for a true 750), which is consistent with the measured 794 µm and the assumed 0.65 µm/px.
5. [does not affect a conclusion] Cell 5: centre YP and MemBrite correlate across dishes (r = 0.94), so per-dish YP partly tracks staining or cell density. The YP/MemBrite variant reverses the 1 Hz co/cross ratio (1.06 vs 0.68), but no p-value crosses 0.05.
6. [does not affect a conclusion] Cells 16 to 22: the two experiment days pull in opposite directions in every comparison. For example, for co 770 kHz vs co 1 Hz the ratio is 2.74 on 2022-11-29 and 0.76 on 2022-12-04. The pooled t-tests follow the criterion, and the notebook reports the day split. Still, the absence claims are "reproduced" only in the sense that the test has low power with n = 5 to 7.
7. [does not affect a conclusion] Footprint background is taken from a 200 µm square in the needle lumen. Neither the paper nor the claims file specifies the area. The whole-disc variant agrees within 1%. The background is nearly constant across dishes (260 to 354 counts), which is why readings (a) and (b) never disagree.
8. [does not affect a conclusion] The file metadata and the dandiset description say "triangular array", but the images show a square. The notebook notes this (cell 4) and follows the paper.

Other checks passed:
- Every number derives from the loaded files.
- The tests are the Student two-tailed, unpaired, equal-variance tests the criteria specify (`stats.ttest_ind`), with Welch as a variant.
- The 200 µm centre ROI follows Methods 4.4.
- The channel order is checked against the images.
- `_roi_mean`, `_disc_mean` and `ov_to_px` behaved correctly on synthetic input.
- There is no training/test split, so leakage does not apply.

**C. What I could not check**

- Whether the center ROI lands on the true array center in each dish. The cell 12 figure is an image only, and the cyan box is drawn on 71 × 75 µm overview blocks. Printing each dish's centre-to-centroid offset, or adding a full-resolution crop of the centre ROI with the footprint edges, would let me verify it.
- Whether the 0.65 µm/px assumption holds independently of the footprint fit. A measured inner-lumen diameter (nominal 0.5 mm) would give a second check.
- The Figure 3 p-values and bar heights. The paper text does not hold them, so I could not compare the effect sizes with the paper's.
