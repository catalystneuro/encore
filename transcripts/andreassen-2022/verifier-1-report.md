**A. Outcomes** (28 claims in the claims file: 17 reproduced, 2 partially reproduced, 9 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig1c-ctmax-5dpf | reproduced | Cell 16: mean 41.363 °C over n = 12, which is within 41.4 ± 0.1. |
| fig1c-ctmax-similar-across-ages | reproduced | Cell 18, Model 2 (n = 39): p = 0.659, 0.073 and 0.178, so no pairwise p < 0.05. F(2,36) = 1.89, p = 0.165. Means are 41.258 and 40.953 °C, within tolerance. Model 1 gives adult against 5 dpf p = 0.038, as in Table S3. |
| figs1a-swim-speed-no-treatment-difference | reproduced | Cell 20: treatment β = 0.760, SE 0.622, p = 0.233, matching Table S1. Interval 1 is 2.897 and interval 5 is 1.720 mm/s. Time 5 has t(100) = −2.435, p = 0.0167. |
| figs1bc-spiral-swimming | blocked (data_missing) | There are no per-fish spiral-swimming scores. The R script types the counts in as `matrix(c(0,14,10,2))` (cell 13), and they match Table S2. I ran the corrected chi-squared on them: 15.60, p = 7.8e-5. That checks the paper's arithmetic, not its data. |
| figs1d-loss-of-equilibrium | reproduced | Cell 22: W = 27 with control first, p = 0.0035, r = 0.577. The heat-ramp median (15.3%) is above the control median (0.8%). |
| figs1e-loss-of-response-specific | blocked (data_missing), uncertain | The notebook gives no loss-of-response record as the reason. However, LOEData.csv has an unexplained 0/1 `Response` column (problem 1), so this block is not established. |
| fig2f-medulla-control-stable | reproduced | Cell 24: control time p = 0.392 and time² p = 0.274. Control mean is 1.577 peaks/min under both readings. |
| fig2f-medulla-heat-rise-then-fall | reproduced | Cell 26: interactions β = 0.226 (t = 8.00) and −0.0061 (t = −8.81), both p < 0.001. Under reading (a) the peak is 3.591, 2.08 times the first bin, and the last bin (0.288) is below the control mean (1.577). Reading (b) gives 4.30 and fails. The criterion allows either reading. |
| figs2a-medulla-decrease-39-41 | blocked (data_missing) | CalciumPeaksLong.csv has no temperature, and the experiment-2 onsets are not deposited (cell 13). Agreed. |
| fig2g-depolarization-onset-temperature | blocked (data_missing) | The only onsets in the item are the 40 from experiment 5. Agreed. |
| fig2e-depolarization-spread | blocked (data_missing) | The archive's file list (I queried the API) has 12 files and no imaging. Agreed. |
| fig2d-recovery-after-depolarization | blocked (data_missing) | There is no time series. Agreed. |
| fig3d-ctmax-precedes-depolarization | reproduced | Cell 28: means 40.857 and 41.357 °C, difference 0.500 (SE 0.111), t = 4.49 with 6 df, p = 0.0041. All 7 fish have depolarization above CTmax. |
| fig4c-heart-rate-rises-to-34 | reproduced | Cell 30: 4.448 Hz at 28 °C and 5.665 Hz at 34 °C. Q10 is 1.497. The 34 against 28 °C contrast has t = 6.89, p < 0.001. |
| fig4c-heart-rate-falls-then-stable | reproduced | Cell 32: 37 against 34 °C is −0.910 (t = −4.92), p < 0.001. Depolarization against 37 °C has p = 0.573. Mean at 37 °C is 4.734 Hz. Q10 is 0.550, inside 0.54 to 0.66 but only just. |
| figs2b-medulla-lateral-mount | blocked (data_missing) | Heartbeat.csv holds heart rate only. Agreed. |
| fig5a-ctmax-oxygen | reproduced | Cell 34: within-treatment outlier removal takes out the paper's 3 fish (2 hyperoxia, 1 hypoxia), leaving n = 73. F(2,70) = 11.67. Hypoxia is −0.576 (p = 0.0068) and hyperoxia +0.492 (p = 0.0248). Means are 39.071, 39.646 and 40.138 °C. The overall-quartile variant also passes. |
| fig5b-depolarization-oxygen | reproduced | Cell 36: hypoxia −2.69 (p < 0.001), hyperoxia +1.22 (p = 0.0034), F(3,36) = 45.5. Means are 40.15, 37.71 and 41.49 °C. |
| figs3b-amplitude-no-oxygen-effect | reproduced | Cell 38: contrasts 14.88 (p = 0.32) and −10.60 (p = 0.48), matching Table S8. |
| figs3c-recovery-longer-in-hypoxia | reproduced | Cell 40: hypoxia +2.565 min, p < 0.001. Hyperoxia −0.706, p = 0.119. |
| figs3d-medulla-drops-before-depolarization | reproduced (fragile) | Cell 42, last-2-min reading: ratios 0.415, 0.286 and 0.486 are all below 0.5. The last-5-min reading fails for hypoxia (0.641). The result rests on the reader's 0.5 threshold and on the author's conversion of temperature bins to time (problem 3). |
| fig5d-medulla-normoxia | reproduced | Cell 44, reading (a): maximum 2.511 at 36 °C, Q10 1.715 (tolerance 1.62 to 1.98). |
| fig5d-medulla-hyperoxia | reproduced | Cell 46, reading (a): maximum 3.226 at 37 °C, Q10 1.837. Hyperoxia × temperature is +0.089, p = 0.0002. |
| fig5d-medulla-hypoxia | partially_reproduced | Cell 48: Q10 from 28 to 34 °C is 0.883, just outside 0.8 ± 0.08. Q10 from 34 to 38 °C is 0.027, below 0.1. Hypoxia × temperature is −0.161, p < 0.001. |
| figs4ab-light-response-amplitude-falls | blocked (data_missing) | LightResponse.csv holds response counts only, no amplitudes. Agreed. |
| fig6c-light-responsiveness-by-oxygen | partially_reproduced | Cell 50: all three initial percentages are within tolerance under every reading. Normoxia holds to 31 °C and hypoxia falls from its first bin. Under the criterion's decline rule, hyperoxia holds only to 29 °C (the 30 °C bin is 31.6%, below the 32.9% threshold), not 36 °C, in all four readings. |
| tables10-light-response-model | reproduced | Cell 52: hypoxia −0.845, hyperoxia +0.486 (p = 0.0075), temperature −0.126, hyperoxia × temperature +0.066 (p = 0.030), each significant in the stated direction. Probabilities are 26.2, 36.6 and 13.2%. |
| discussion-depolarization-magnitude | blocked (data_missing) | Medulla peak amplitudes are not deposited. The `Peak` column is the experiment-5 depolarization amplitude. Agreed. |

**B. Problems**

1. **[affects a conclusion]** Cells 4 and 13: LOEData.csv has a numeric `Response` column with 26 values from 0 to 1. The notebook never says what it is or tabulates it by treatment. Cell 13 then says LOEData has "no … loss of response". If `Response` is loss of response, figs1e is testable and its block is wrong.
2. **[does not affect a conclusion]** Cell 13 / figs1bc: the claims-file criterion takes its counts from the Table S2 caption, so the chi-squared part could have been computed. It gives 15.60, p < 0.001, matching. The notebook reports the claim as fully blocked without showing this.
3. **[does not affect a conclusion, but the result is fragile]** Cell 42 / figs3d:
   - The 2-min window lies mostly inside the partial onset bin. The notebook never establishes how the deposited frequency of a partial bin was normalised.
   - The hypoxia ratio (0.486) is close to 0.5.
   - The onset-frame slope for experiment-5 period 1 (0.086 °C/min, r = 0.56) is unexplained.
   - The outcome holds at both ramps tried, 0.3 and 0.225 °C/min.
4. **[affects a conclusion, possibly]** Cell 48 / fig5d-hypoxia: only lower-bound bin labels from 28 °C on were used. The 27 °C bin is in the data but never shown. The notebook does not say whether the R script computes the Q10s, which would settle the 0.883 against 0.8 gap.
5. **[does not affect a conclusion]** Cell 50 / fig6c: the hyperoxia failure comes from a one-bin dip under the claims file's decline rule, not from a sustained decline. The "stays below" variant gives 36 °C, and the notebook correctly labels it as outside the criterion. I am reporting the fragility of the rule, not correcting it.
6. **[does not affect a conclusion]** `thermal` module docstring: the script takes p-values by Kenward-Roger, while the notebook uses Satterthwaite and normal approximations. No p in the notebook is near a threshold where the methods would disagree.
7. **[does not affect a conclusion]** Cell 48: the per-fish Q10 variant (2.03) is a mean of ratios dominated by low 28 °C rates, and it says nothing about the claim.
8. **[does not affect a conclusion]** Cell 5 has a garbled sentence ("Two columns are not described… and nothing else"). It asserts that the Readme covers every column, but the Readme text is never printed.
9. **[does not affect a conclusion]** Cell 3 takes version 3 by list position (`versions[2]`). It is correct for the printed list [1, 2, 3, 4].

Helper checks on synthetic data:
- `LMM` matches statsmodels' REML estimates and SEs to 4 decimals.
- Its Satterthwaite test on a 7-fish paired design gives 6 df and the paired-t p.
- `extreme_outliers` matches type-7 quartiles.
- `q10` reproduces 1.497.

Selection, units (seconds converted to minutes, peaks per 3 min converted to per minute), reference levels and n all match the claims file. There is no train/test split, so leakage does not apply.

**C. Could not check**

- **Meaning of LOEData `Response`.** Printing the Readme's entry for LOEData and a crosstab of `Response` by `Treatment` would settle figs1e.
- **R script contents.** I could not check the script lines the notebook cites (outlier filters, `p.val = "kr"`, Fig 5D/6C binning), or whether it computes any Q10. Printing those lines, and any Q10 code, would settle fig5d-hypoxia's endpoints.
- **27 °C medulla bin.** Its values for the experiment-5 treatments are not shown.
- **Partial onset bins.** How the frequency of the partial onset bin in CalciumPeakExperiment.csv was normalised is not shown; the Readme text or the script would answer it for figs3d.
- **Kenward-Roger p-values.** The p-values the script itself reports were not available for comparison.
