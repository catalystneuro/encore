**A. Outcomes** (20 claims in the claims file; the notebook tests 14 and treats 6 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| dataset-structure | reproduced | Cells 3, 5 and 14: 9 flies, 30,456 volumes, 1.880 Hz, 1,605,632 voxels of 2.61 × 2.61 × 5 µm, FicTrac at 50 Hz, 1800 s per session. |
| fig2c-fraction-correlated | partially_reproduced | Cell 18: reading (a) gives 31.1%, which is below the 35.1–42.9 band but above 19.5. Reading (b) gives 54.9%, which is above the band. The paper's Results quote 39% at the Bonferroni supervoxel threshold, i.e. reading (b), and that reading misses by 16 points. |
| fig2c-venn-categories | partially_reproduced | Cell 20: under (a) the values are 11.9 / 15.9 / 3.2 / 11.5%, all outside tolerance. The ranking holds and "all three" is below 20%. |
| fig2-symmetry | reproduced | Cell 22: VF mirror r = 0.823; VL vs mirrored VR 0.672 against 0.449 for VL vs its own mirror; VL A/B = 2.38 and VR A/B = 0.31. Per fly the pattern is inconsistent (see B6). |
| fig2e-region-fractions | blocked (data_missing) | No neuropil labels anywhere in the archive (see section C). |
| fig3-topographic-maps | blocked (data_missing) | Same reason. |
| fig4bcd-pc-structure | reproduced | Cell 26: all three criteria hold under both readings. PC3 above threshold: VL +0.114 (p 3e-14), VR −0.259 (p 6e-72). |
| fig4fg-ridge-r2 | partially_reproduced | Cell 28: medians are 0.155, 0.196 and 0.212, all ≥ 0.15 but none within 0.27–0.33. VF clears the 0.15 bar by only 0.005. Mean R2 peaks at 100 PCs for all three components. Only the interleaved-fold variant gets near 0.3. |
| fig4h-r2-vs-movement | partially_reproduced | Cell 31: Spearman ρ is positive for all three components (0.017, 0.383, 0.683), but the pooled rank r = 0.361 has p = 0.064. The largest R2 is 0.534, outside 0.54–0.66. The VF ρ of 0.017 is effectively zero. |
| fig4i-weights-stereotyped | reproduced | Cell 33: median pair r 0.646 / 0.732 / 0.761; 9/9, 7/9 and 9/9 flies on (ii)–(iv). Criteria (i) and (iv) have no null (see B9). |
| fig5a-unique-variance | partially_reproduced | Cell 35: VF is uniquely encoded in 0.75% of blocks and walking in 0.09%, so VF beats walking but misses the 5% bar. At a 0.005 threshold walking reaches 1.88% against 2.24% for VF, and with the walking state as the code intended, walking (0.97%) exceeds VF (0.91%). |
| fig5c-global-below-threshold | partially_reproduced | Cell 37: the "own component" part holds under both readings. The below-threshold part fails under (a): left region vs VR r = −0.008, p = 0.2. Under (b) it passes only on r = 0.013, p = 0.031, and that p-value treats 27,054 autocorrelated samples as independent; the left region is only 4 blocks. |
| fig5f-ipsi-contra | not_reproduced | Cell 39: the mirror blocks of the top-increase blocks rise instead of falling (medians +0.0064 and +0.0022, Wilcoxon p ≤ 4e-5 in the wrong direction). This holds at 50 and 150 deg/s and in 8 of 9 flies for both turns. Only the opposite-halves part holds. |
| fig6-peak-time-range | reproduced | Cell 43, reading (b): 99th-percentile lead 0.32 s and 1st percentile −1.23 s. The 0.03 s tolerance is far smaller than the ±0.27 s timing error, and the volume-start variant fails both parts (0.58 s and −0.95 s). See B2. |
| fig6h-peak-vs-width | reproduced | Cell 45: r(lag, FWHM) = 0.672, p = 2e-281. Not controlled for plane (B2). |
| fig6fg-ipsi-leads-contra | reproduced | Cell 47: the ipsilateral minus contralateral lead has median +0.16 s for VL (868 pairs) and +0.14 s for VR (849 pairs), Wilcoxon p ≈ 0. Mirror pairs share a plane, so plane timing roughly cancels. |
| fig6eg-region-sequence | blocked (data_missing) | Needs neuropil labels. |
| fig7-within-region-gradients | blocked (data_missing) | Needs neuropil labels and plane times; neither is in the archive. |
| figs2-tdtomato-control | blocked (data_missing) | The motion-corrected tdTomato is not deposited. A weaker partial test was possible (section C). |
| figs4a-supervoxel-number | blocked (too_large) | Defensible for the full sweep over 91 planes. A partial sweep on the 12 streamed planes was feasible but not attempted. |

Totals: 7 reproduced, 6 partially reproduced, 1 not reproduced, 6 blocked.

**B. Problems**

1. [affects a conclusion] Cell 37, fig5c: the p < 0.05 test on below-threshold correlations ignores autocorrelation. The pass under reading (b) rests on r = 0.013, which would not survive any effective-sample-size correction. This is why I downgrade fig5c to partial.
2. [affects a conclusion] Cell 43, `bw.neural_times`: the median VF lead changes steadily with FDA plane, from +0.36 s at plane 17 to −0.30 s at plane 80. That 0.66 s spread is about one volume period (0.53 s), which is the pattern unknown per-plane acquisition times would produce. The earliest leads come from the low planes. So the fig6 match within 0.03 s is not meaningful, and the fig6h lag–width correlation may be partly driven by plane. No within-plane control is shown.
3. [affects a conclusion] Cell 39, fig5f: the paper derives Fig 5F from the demixing model (Results, "the demixing linear model revealed"). The notebook uses raw means of turn minus slow walking. Turns come with higher global activity, which could mask a contralateral decrease. The outcome follows the criterion as written, but the test differs from the paper's method.
4. [affects a conclusion] Cell 35, fig5a: the outcome depends on `UNIQUE_MIN` = 0.01 against a median full-model R2 of 0.0019, and on how the walking state is defined. Both alternatives shown reverse or erase the VF advantage.
5. [does not affect a conclusion] Header of the claims file: the fig2c, venn and symmetry criteria were written after the prototype results were seen. The symmetry threshold of 0.7 is a choice made after seeing r = 0.82.
6. [does not affect a conclusion] Cell 22, per-fly table: the expected sign pattern (VL A > B and VR A < B) holds clearly in only 5 of 9 flies (087, 089, 094, 100, 101). fly_098 and fly_105 have VR on the same side as VL, and fly_099 has VL reversed. In cell 11, fly_105's half-difference correlates negatively with rotation, and its VF R2 is −0.50. The pooled result hides this heterogeneity, and a possible left-right flip in fly_105's registration is never checked.
7. [does not affect a conclusion] Cell 11, clock check: the observed statistic is the maximum |r| over 101 lags, but the null is |r| at a single random shift. The null is therefore not comparable and the margins are overstated, though the lag peaks still look sensible.
8. [does not affect a conclusion] Cell 28, `fly_scores`: alpha is chosen on test-fold scores (as the paper's code does), and the PCs use all time points. The nested variant in cell 29 shows the bias is small.
9. [does not affect a conclusion] Cell 33, fig4i: criterion (iv) is close to automatic. PC1 is signed positive with VF and correlates positively with VL and VR. No shuffled-behaviour null is given for the pairwise weight correlation in (i).
10. [does not affect a conclusion] Cell 18, reading (b): the denominator is `brain_blocks.sum()` (186,298) where it should be `brain.sum()` (191,119), so 54.9% would become about 53.5%.
11. [does not affect a conclusion] Cell 0 and `brainwide.py` docstring: the 9 behaviour-video AVI files that make up half of the 18 assets are never mentioned. The raw tdTomato series is asserted to exist but never printed.
12. [does not affect a conclusion] Cell 22, plot: the colour range is ±0.3 while the largest voxel r is 0.12, so the maps look faint.

Helpers I tested on synthetic inputs, all correct:
- `pooled_r` and `r_threshold` (p = 1.0e-4 exactly).
- `ridge_scores`, `ridge_fit` and `multi_ridge_r2` match sklearn `Ridge` to 1e-15.
- `fwhm`: 1.18 s for a Gaussian with s.d. 0.5 s (expected 1.177 s).
- `mirror_block` (an involution mapping x to 313 − x) and the block means in `reduce_plane`.
- Lead sign through `deconvolve`: true leads of +0.3, −0.5 and 0 s are recovered as +0.32, −0.48 and +0.02 s.

**C. What I could not check, and the output that would have settled it**

- Blocked claims, checked against the archive through the REST API: version 0.240106.0043 has 18 assets, 9 NWB files and 9 AVI behaviour videos. Asset `variableMeasured` lists only OpticalChannel, ImagingPlane, Position, ProcessingModule, TwoPhotonSeries and SpatialSeries. There is no ImageSegmentation, PlaneSegmentation, Images or atlas file.
  - fig2e, fig3, fig6eg and fig7 are blocked. The only sub-part testable without labels would be a positional proxy, such as "optic lobes lag" using the lateral-most blocks, which is not rigorous.
  - figs2-tdtomato: a partial test on the raw tdTomato channel (uncorrected), compared with raw GCaMP6f in the same space, was possible. A null result there would support the claim.
  - figs4a: a partial sweep was possible on the 12 planes. To judge both, I would need the names, shapes and chunk layout of every acquisition series, which the notebook never prints.
- fig6 and fig6h:
  - Per-plane leads and the lag–FWHM correlation within each plane, or a partial correlation controlling for plane.
  - The orientation of the FDA's 91-plane axis relative to the acquisition z-order.
- fig5c, and the fraction in fig2c: a circular-shift (behaviour-rolled) null for the below-threshold correlations and for the fraction of correlated voxels. The paper states no chance level for either, and the notebook gives one only for ridge R2 (median −0.023).
- fig5f: the turn-condition contrast computed from demixing-model predictions, as in the paper.
- fig2-symmetry: a check of fly_105's left-right orientation, such as its own mask mirror overlap or its own VF map against the pooled map.
- I could not confirm that the in-brain masks, block signals and FicTrac values are right, since I did not re-run anything; I relied on the printed outputs.

I saved the paper's full text to `paper/full.txt`.
