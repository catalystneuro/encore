## A. Outcomes (50 claims in the claims file; the notebook tests 49 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| exp1-units | reproduced | Cell 13, caudal singles with sham (a): 160 units, 144 responsive, layers 36/48/46/14. All are within tolerance. |
| fig1b-somatotopy | reproduced | Cell 16: the CW mean is largest (0.517), followed by rostral (0.368) and caudal (0.327) within-row. |
| exp1-cw-tuned-fraction | reproduced | Cell 18 (a): 87 CW-tuned, 57 SW-tuned, fraction 0.604. All within tolerance. |
| exp1-cw-sw-comparable-firing | not_reproduced | Spontaneous rates fit: 1.33 and 2.05 Hz. Maximal evoked firing is 0.58 and 0.60 spikes per stimulus against 4.8 and 4.56 (cell 20). Read as Hz over the 125 ms window, the same values are 4.65 and 4.80, which would match (see B4). |
| supp1d-sw-tuning-broader | reproduced | Cell 22 (a): p = 0.00072, SW-tuned broader. |
| fig1d-best-sequence-exceeds-single | reproduced | Slope 1.211 with intercept (1.345 through the origin); 143 of 144 units (99.3%) above the diagonal. |
| fig1e-best-combination-includes-cw | partially_reproduced | Main reading: 0.688 and 0.862 pass, but SW-tuned 0.421 is below the bound of 0.423 by about one unit. Same-direction variant (ii): 0.694, 0.851, 0.456, all within (cell 33; see B5). |
| fig1f-cwsw-exceeds-swsw | reproduced | Cell 28: 99 of 144 units above the diagonal, paired p = 1e-6, under both readings. |
| fig1g-cwsw-sharper | reproduced | CW-SW sparseness above SW-SW at 55 of 55 values of N. |
| supp2-sw-tuned-sharpest-cwsw | reproduced | SW-tuned above CW-tuned at 55 of 55 values of N. |
| exp2-units | reproduced | 247 units in the files (246 after dropping a duplicate). Under O2 (a) and sham (a), 231 correlated and 232 anti-correlated sets are responsive; all within tolerance. |
| methods-dt-modulation | not_reproduced | Cell 40: monotonic 0.574 (expected 0.33) and unsmoothed 0.000 (expected 0.23). Only the constant total, 2127, is within tolerance. Zero padding (cell 41) gives 0.011. |
| exp2-combination-selective-prevalence | not_reproduced | Cell 43: 318 selective and 145 nonselective sets (expected 187 and 264); 189 cells (expected 129); fractions 0.77, 0.64, 0.73. Both FDR families fail. |
| fig2f-shuffle-abolishes-tuning | reproduced | Measured CSI 0.033 against 0.000 shuffled. Under (a), the shuffled first point is 0.011 above the rest, inside that point's s.e.m. of 0.027. This is computed on 318 sets, not 187 (B1). |
| fig2f-most-selective-lower-firing | reproduced | Both spontaneous and evoked firing are lower in the most selective quarter, p < 1e-9 (cell 49). Same 318-set caveat. |
| supp4-selectivity-at-high-rates | not_reproduced | Group counts are 178 / 140 / 28 against 95 / 92 / 91. The peak test after spontaneous subtraction holds (ratio 22.9). |
| fig2g-best-combination-bias | reproduced | Rayleigh p = 1.1e-22. All 8 SWs appear as a best combination; rostral within-row is the most frequent (150); ventral 210 against dorsal 63. |
| fig3a-sharper-than-linear | reproduced | O3 (a) / O2 (a): p = 3e-43, and 91.1% of sets have measured CSI above linear. |
| fig3b-sharper-in-both-groups | reproduced | Both groups p < 1e-7 with measured higher (cell 57), but the groups are 318 and 145 sets. |
| fig3b-linear-sharper-in-selective | reproduced | p = 7.3e-5 with the selective sets higher (cell 59). Same group caveat. |
| supp6-layers | partially_reproduced | ANOVA p = 2.4e-5, with the L2/3 and L4 means above L5 and L6. Layer count L6 = 53 is outside 45 ± 4.5. |
| fig3e-identity-decoder | not_reproduced | At N = 187: 0.135 (expected 0.42). Rostral within-row 0.986, every other combination at most 0.04. The linear-prediction decoder is not lower by more than the sum of the s.d.s. |
| fig3g-binary-decoder | not_reproduced | N = 10: 0.61 to 0.62 under the best readings, below 0.63. N = 100: 0.82. |
| fig4a-sw-tuned-sharper | reproduced | O2 (a): 174 CW-tuned and 289 SW-tuned, both within tolerance; p = 3.6e-7 with SW-tuned higher. |
| fig4c-sw-tuned-decoding | not_reproduced | Reading (a): SW-tuned is lower at N = 100 and 150. Reading (b): CW-tuned at N = 150 is 0.132, not above 0.125 + 2 × 0.061. |
| fig5a-global-scaling | reproduced | Slope 0.636, R² 0.926 (centred), 3704 combinations. |
| fig5bc-linearity-index | partially_reproduced | No reading has both means within tolerance. Under (b, a), best 0.964 is within and nonoptimal 0.652 is within 10%; p = 1.8e-77. |
| fig5c-pseudo-unit-shuffle | reproduced | 0.680 and 0.671 (0.684 and 0.678 with 10,000 pseudo-units). |
| fig5c-sublinear-at-all-dt | reproduced | Peak nonoptimal index 0.703 against 0.909 for the best combination, p = 2e-61. |
| supralinear-best-8-percent | reproduced | Only under (a) with the selective sets: 0.0723, against a bound of 0.072. All-sets reading gives 0.093 (fails). Fragile, and the selective set is inflated (B1). |
| fig6b-best-above-worst-below-scaled | reproduced | All four paired tests p < 1e-6 in the stated directions. |
| fig6b-enhancement-not-different | not_reproduced | p = 0.0096; the difference is 0.045 (cell 77). |
| fig6b-suppression-greater-selective | reproduced | Bonferroni ×8: 0.0085 and 0.0008, with the selective sets more negative. |
| fig6c-enhancement-strongest-sw | partially_reproduced | Selective: p = 1.6e-9 with rank 1 largest. Nonselective: p = 0.17, so the second part fails. |
| fig7a-dt-half-width | partially_reproduced | All 318 sets: 16.5 / 14.9 / undefined. Excluding the 70 sets whose best curve is constant (an alignment artefact, B2): 11.5 ms under (a). The suboptimal curve is lower at the best dt, but its half-width is undefined. |
| fig7b-inbound-best-outbound-suboptimal | partially_reproduced | Best peaks at −50 ms, suboptimal at +42 ms and lies below. The minimum is at 0, −6 or −3 ms under the three readings, never −10 ± 1. The criterion gives no partial rule. |
| fig7c-pca | partially_reproduced | Modulated counts 373 and 1204 are within tolerance; PC1 crosses zero at 0 ms; PC2 is U-shaped. Three PCs explain 0.836, above the 0.825 bound. |
| fig7e-pc1-best-suboptimal | partially_reproduced | Selective: best −2.37 against suboptimal +0.21, p = 8.9e-8. The nonselective difference is 0.59 of the selective one (needs under a third), and PC2 differs (p = 0.005). |
| fig7f-inbound-sharper | partially_reproduced | Only reading (c) passes both tests (p = 0.03 and 1.3e-7). Its counts are 134 and 112 against 121 and 56. Under (a) and (b), the CSI test gives p ≈ 0.1. |
| fig7g-inbound-decoding | not_reproduced | Inbound-minus-outbound differences are 0.014 to 0.019 against mean bootstrap s.d. 0.057 to 0.075. |
| supp8-order-decoding | not_reproduced | 0.581 and 0.570 at N = 100, against a bound of 0.585. The selective-set miss (0.004) is within Monte Carlo error (s.e. ≈ 0.0065), so this outcome is fragile. |
| exp3-units-cw-tuned | reproduced | 81 units, 74 responsive, 46 CW-tuned; mean single-whisker tuning is largest at the CW. |
| fig8c-awake-cw-stronger | not_reproduced | Ratio 1.71 is within tolerance and the awake tuning is sharper, but t-test p = 0.0021, not < 0.001. |
| fig8d-awake-best-sequence | reproduced | Slope 1.234 (b) or 1.300 (a); 98.6% of units above. |
| exp3-combination-selective | reproduced | 27 of 74 (0.365); CW-containing best sequence in 0.704 of selective and 0.784 of all units. All within tolerance. |
| fig8h-awake-linearity | partially_reproduced | Best 0.941 is within; suboptimal 0.723 misses 0.71 ± 0.009 but is within 10%; p = 1.5e-16. |
| fig8i-awake-sharper-than-linear | reproduced | p = 9e-9; 94.6% of units above linear. |
| fig8j-awake-inbound-stronger | reproduced | Both readings: p < 1e-13, and −40 ms is highest. |
| fig8k-awake-binary-decoder | reproduced | Accuracy rises with N, reaching 0.815 (a) and 0.829 (b) at N = 25. |
| fig8b-awake-behavior | blocked (data_missing) | I checked the archive: the S3 listing and filelist.txt hold only data.zip, checksums and the descriptor. The zip holds only 23 per-session .mat files, and the descriptor documents no lick or Go/No-go fields. No part is testable. |

Totals: 28 reproduced, 10 partially reproduced, 11 not reproduced, 1 blocked.

## B. Problems

1. **[affects a conclusion]** The shuffle selectivity test is anti-conservative (cell 36; `L.fast_dt_smooth`, `L.shuffle_csi`, `L.mahalanobis_p`), and the notebook never checks its calibration.
   - On synthetic Poisson units with no combination or dt tuning, run through the notebook's own helpers, p < 0.05 for 33% (λ = 0.3) and 43% (λ = 1.0) of units.
   - With every curve held constant the test is calibrated (3%). With a fixed kernel it gives 10%; with the cross-validated kernel, 30%.
   - So the inflation comes mainly from choosing the kernel on the measured data, which is what the Methods describe, plus small-sample bias from the pseudo-inverse Mahalanobis distance.
   - The result is 318 selective sets against 187. That changes the group used in every selective-group claim: fig2f ×2, supp4, fig3b ×2, fig3e, fig3g, fig4c, fig6b ×3, fig6c, fig7a/b/e/f/g, supp8 and supralinear (d).

2. **[affects a conclusion]** `derive` (cell 45): when the best combination's curve is constant (90 sets, 70 of them selective), `argmax` breaks the tie at dt = −50 ms. The markdown flags this, but most analyses still use it:
   - fig7a aligns flat curves at lag 0, which raises the half-width from 11.5 to 16.5 ms.
   - fig7f readings (a) and (b) count these 70 sets as inbound.
   - The decoder windows and O3 (b) for these sets sit at an arbitrary ±5 ms around −50.

3. **[affects a conclusion]** methods-dt-modulation (cell 40, `fast_dt_smooth`): "unsmoothed" never wins (0%). In my synthetic runs at λ = 1, where the 1e-3 floor rarely binds, it also never won. So the paper's 23% likely comes from a scoring choice the notebook does not explore. The zero-padding reading (1.1%) shows the outcome is very sensitive to these details.
   - Minor: the unused `dt_smooth` defines "monotonic" differently from `fast_dt_smooth`.

4. **[affects a conclusion]** exp1-cw-sw-comparable-firing: this is a claims-file issue, copied from the paper. The paper's "4.8 ± 0.48 spikes per stimulus" cannot be a per-stimulus mean: the Fig. 1d axis tops out near 4 spikes per stimulus. The notebook's values in Hz (0.581/0.125 = 4.65; 0.601/0.125 = 4.80) match all four expected values. The claims file should name a Hz reading; the notebook did not run one.

5. **[affects a conclusion]** Cell 11: the main experiment 1 analysis pools opposite-direction pair trials in the two 20170510 recordings into sequence means. The paper's 261 stimuli include no opposite-direction pairs. Variant (ii), which drops them, flips fig1e from a one-unit miss to a pass.

6. **[affects a conclusion]** Two outcomes sit on a boundary at the level of sampling noise:
   - supp8 (cell 103): 0.581 against a bound of 0.585, with Monte Carlo s.e. ≈ 0.0065.
   - supralinear (cell 73): 0.0723 against a bound of 0.072, and only on the inflated selective set.

7. **[does not affect a conclusion]** fig7a reading (b) averages over only 74 of 318 sets that have a defined half-width.

8. **[does not affect a conclusion]** fig7g (cell 101): the positive dt ranges (0–9 … 30–39, 41–50) leave out +40 ms and are not mirror images of the negative ranges. The decoder is near chance either way.

9. **[does not affect a conclusion]** supp4 runs only O3 (a). The counts are too far off for O3 (b) to rescue them.

10. **[does not affect a conclusion]** Two recordings in experiment 2 have no sham trials, so their units are tested on the nine whiskers alone. Experiment 3 cannot apply the lick exclusion. Both are stated in the notebook.

11. **[does not affect a conclusion]** The decoder helpers (`heldout_prob_rows`, `Pool.accuracy`) pass a synthetic check: accuracy rises with N, there is no train/test leakage, and they do not collapse under a 35% preference bias. The near-chance real decoding therefore reflects weak single-trial tuning in the inflated selective pool, not a bug I could find.

Things I checked that hold: the whisker grids for both experiments match the descriptor's figure order and its D1 example; dt = t_SW − t_CW; the experiment 3 epoch clock is consistent with the PSTH and clock checks (cells 7 and 9); the MD5 matches; no numbers are hard-coded.

## C. What I could not check, and the output that would settle it

- **Calibration on real data:** shuffle-test p-values for real sets with counts permuted across combinations within each dt (a real-data null), and a histogram of `p_shuffle`.
- **Experiment 3 field names:** printing `u._fieldnames` for one experiment 3 unit, which would confirm there are no lick or trial-type fields. The descriptor does not document `DeltaT` or `experiment`, nor the spikes up to 424 s after epoch onset.
- **The 20170510 direction coding:** raw `directionWs` and `timeWs` for a few mixed-direction trials, to tell whether this is a coding flip or real stimuli.
- **Experiment 1 claims under sham (b):** fig1e, fig1d and fig1b recomputed with the 147-unit, 89-CW-tuned set.
- **Fig. 7a, 7b and 7f with the constant-curve sets excluded or given NaN best dt:** reported under every listed reading.
- **Monte Carlo s.e. for decoder accuracies near a bound** (supp8, fig3g), with more ensembles.
- **Selective-group claims on a group of the paper's size:** for example the 187 sets with the smallest shuffle p-values, to show whether the decoder and Fig. 6 and 7 results depend on the inflated selective set.
