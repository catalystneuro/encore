**Verification report, round 1: Carrier et al. 2026 (doi:10.1152/jn.00294.2025)**

The claims file has 29 claims. The notebook tests 21 and treats 8 as blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-cb-075-frequency-unchanged | reproduced | Cell 27: n = 10, 1x 1.175 Hz and 0.75x 1.183 Hz (tolerance ±0.07 around 1.18), paired t P = 0.816. The table has only one 1x value, so the two baseline readings cannot be told apart. |
| fig1d-cb-125-frequency-unchanged | reproduced | Cell 29: n = 10, 1.176 and 1.169 Hz (1.2 ± 0.04), P = 0.748. |
| fig1e-cb-salinity-crash-fractions | blocked (data_missing), partly testable | 0.5x and 1.75x are not in the table. Cell 29 does show three of the five counts: 0.75x 10/10 with values, 1.25x 10/10, and 1.5x 9/10 (888_141 missing), which matches "all but one" if a missing value means a crash. The notebook does not report these. |
| fig2b-cb-crash-temp-075-unchanged | reproduced | Cell 31: n = 11, 29.35 and 30.62 °C, Wilcoxon P = 0.401. Levene's test centred on the mean gives P = 0.0497 with the 0.75x SD lower (4.49 vs 2.47 °C). Centred on the median it gives P = 0.102, so the variance part holds only under the mean-centred reading. |
| fig2e-cb-crash-temp-125-lower | reproduced | Cell 32: 31.27 vs 26.17 °C, paired t P = 0.003 (paper 0.008), lower in 9 of 9. The variant using the Prism value (36 °C for 963_106) gives P = 0.0145 and 8 of 9. |
| fig2f-cb-125-frequency-rises | reproduced | Cells 38–39: 1.25x Q10 = 1.705 (above 1) and shared-slope P = 0.769. The step means are lower in 1.25x at every step, which is consistent with the paper's other sentence ("a decrease"). |
| fig2g-cb-q10-075-unchanged | reproduced | Cell 37, reading Q-a: Q10 1.723 and 1.712, F(1,171) = 0.006, P = 0.936. The degrees of freedom match the paper exactly. |
| fig2h-cb-q10-125-unchanged | reproduced | Cell 38, readings W-a and Q-a: 1.673 and 1.705, F(1,148) = 0.087, P = 0.769, with 152 points. This matches the paper exactly. |
| fig2f-cb-mixed-model | partially_reproduced | Cell 41: no reading gives the full pattern. Two of three terms hold under 6 of 8 readings. Under S-b (n = 11) salinity is significant (P = 0.015); under S-a with frequency the interaction is not (P = 0.28). The tests are Wald tests, not lmerTest's, but the problem 3 argument shows this cannot move the outcome. |
| fig2i-cb-neuron-crash-counts | reproduced | Cell 33: 9 of the 10 counts match exactly. For "all three crashed at the same temperature", the cell 33 table has exactly 9 of 20 ramps where all three neurons crashed, each within ≤1 °C (less than one 2 °C step). The notebook's own two readings give 4 and 9, but its "9" counts a different set of ramps (problem 2). |
| fig2i-cb-neuron-crash-temps-similar | reproduced | Cell 34: P = 0.32, 0.069 and 0.20 (Wald χ²) and 0.34, 0.11 and 0.25 (F scale), all above 0.05. A Geisser-Greenhouse correction would only raise them. |
| fig3b-ha-frequency-q10 | reproduced | Cell 44, readings Q-a and P-a: Q10 1.434 [1.24, 1.66], F(1,8) = 35.72, P = 0.00033. This matches the paper exactly. |
| species-frequency-at-10c | reproduced | Cell 45, reading R-a: n = 19 and 15, 1.206 and 0.563 Hz (tolerance ±0.03), Welch P = 2e-15. |
| fig3c-ha-phase-constant | reproduced | Cell 46: only PY on is below 0.05 (P = 0.024 for Q-a). All five Q10s are within tolerance (0.915, 0.910, 1.010, 1.160, 0.979). |
| fig4b-ha-075-frequency-unchanged | blocked (data_missing) | No lobster salinity-series file appears among the Lobster STNS.zip names (cell 18), and no table holds the series. This is plausible but rests on file names only (section C). |
| fig4d-ha-125-frequency-unchanged | blocked (data_missing) | Same as fig4b. |
| fig4e-ha-salinity-crash-fractions | blocked (data_missing) | Same as fig4b. |
| fig5b-ha-lp-crashes-before-py | blocked (data_missing / too_large) | Per-neuron lobster crash temperatures are not tabulated. LP and PY burst files exist for 6 of 19 preparations (cell 65), so only a subset below the paper's n could be tested. The `1x saline` sheet and the `.mat` files were never shown (section C). |
| fig5c-ha-mixed-model | partially_reproduced | Cell 48: temperature and the interaction are significant under every reading, salinity under none (P = 0.07 to 0.79). The model used 14/19/14 ramps where the paper used n = 10/14/8 (problem 4), so this is provisional. |
| fig5d-ha-q10-salinity-unchanged | not_reproduced | Cell 49, Q-a: the 0.75x set gives F(1,210) = 4.04, P = 0.046 (paper F(1,209) = 3.50, P = 0.063). The 1.25x set gives P = 0.098 under Q-a and 0.034 under Q-b. All four Q10s are within tolerance, but the criterion counts a P just below 0.05 as not reproduced. The miss is marginal and rests on one data point per set (problem 5). |
| fig6a-ha-py-crash-temp-salinity | blocked (data_missing) | Depends on fig5b. |
| fig6b-ha-lp-crash-temp-salinity | blocked (data_missing) | Depends on fig5b. |
| fig7a-species-q10-075 | reproduced | Cell 51, Q-a: 1.716 and 1.404, F(1,250) = 12.18, P = 0.0006. This matches the paper exactly. |
| fig7b-species-q10-1x-similar | reproduced | Cell 52, Q-a: 1.604 and 1.436, F(1,353) = 3.042, P = 0.082. This matches the paper exactly. Under Q-b, P = 0.0025. |
| fig7c-species-q10-125 | reproduced | Cell 53, readings T-c and Q-a: 1.609 and 1.253, F(1,175) = 9.371, P = 0.0026. This matches the paper exactly. |
| fig7e-species-crash-temp-1x | not_reproduced | Cell 54: both means match (30.21 and 27.62 °C), but crab n = 20, not 21, and Welch P = 0.0603. The deposited Prism result gives the same P = 0.0603 with n = 20. |
| fig7df-species-crash-temp-075-125-similar | reproduced | Cell 55: Mann-Whitney P = 1.000 at 0.75x and Welch P = 0.145 at 1.25x (paper 0.08), both above 0.05. All four means are within tolerance. Crab 1.25x has n = 9 against the paper's 10. |
| fig8-invivo-rhythm-maintained | partially_reproduced | Cell 63: all 58 exposures pass readings B-a and B-b. However, the rule also passes shuffled traces in 90–99% of windows (problem 6), so it cannot detect a crash. Each "1-h" exposure holds only 32 min (cell 62), so the full-hour part of the claim cannot be tested. A noise-calibrated variant holds in 51 of 58. |
| fig9-15h-mortality | blocked (data_missing) | The deposit has one 32-min "15Hours" recording (cell 58) and no survival records. The Zenodo descriptions, which I queried, mention none. |

### B. Problems

1. **[affects a conclusion] fig8, cell 63 and `band_present`.** The "peak above 3× median" rule cannot fail. The notebook's own shuffled traces pass it in 0.90–0.99 of windows. On synthetic data I got 0.96 for white noise and 1.00 for brown noise. The criterion also requires every spectrogram to be shown, and cell 64 shows 2 of 58. Two crab exposures (animal 18 at 0.25x and 0.5x) have a median peak at 2.3–2.4 Hz, and nobody checked whether that is the pyloric band.
2. **[does not affect a conclusion] fig2i counts, cell 33 `same_ii`.** Reading (ii) is the author's own and is not in the paper or the claims file. It counts ramps where one neuron never crashed (953_092, 888_090, 888_112, 888_150, 888_155). Its total of 9 is a coincidence. The paper's wording ("all three neurons crashed") fits "all three crashed, within one step", which also gives 9 of 20 from the same table.
3. **[does not affect a conclusion] `mixed_model` (cells 41, 48) and `neuron_mixed` (cell 34).** These use statsmodels Wald tests, not lmerTest's Satterthwaite F tests or Prism's Geisser-Greenhouse correction. Wald tests are anti-conservative, and none of the decisive P values would cross 0.05 in the direction that changes an outcome. Random-effect structures whose fit failed get AIC = inf and are dropped silently. The Bayes-factor step was skipped. In cell 41, salinity as a factor (S-c) has 2 df while the paper prints 1.
4. **[affects a conclusion] fig5c, cell 48.** The paper's n = 10 (0.75x), 14 (1x) and 8 (1.25x) almost exactly matches the ramps with a "Crash" mark in Sheet4: 10, 13 and 8 (cell 7). The notebook fitted all 14/19/14 ramps and never ran the subset the paper's n points to. Whether salinity becomes significant under that subset is untested.
5. **[affects a conclusion] fig5d, cell 49.** The deposit gives 214 and 176 points where the paper has 213 and 175: one extra point in each set. The extra point was not identified. Since P sits on 0.05 (0.046 against the paper's 0.063), the outcome depends on it. Removing the 111122 duplicate gives P = 0.052, but the paper's degrees of freedom show it kept that copy.
6. **[affects a conclusion] fig8, cells 59 and 62.** Seven pairs of identical recordings are filed under different animals or salinities, so there are 51 distinct recordings among the 58 one-hour exposures. Every exposure holds only the first 32 min, so reading B-a ("in at least half the windows of the hour") cannot be applied as written.
7. **[does not affect a conclusion] Cell 15.** It says `Lobster_Q10s_1x&075x.mat` carries 120722's values under 111122. No cell reads any `.mat` file, so this statement has no output behind it.
8. **[does not affect a conclusion] fig1e, cell 66.** The blocked reason ignores the three counts that can be read from the salinity table (0.75x, 1.25x, 1.5x). The notebook could have reported them as a partial test.
9. **[does not affect a conclusion] fig1d, cell 29.** The rows "888_136 (1)" and "888_136 (2)" (cell 21) enter as two preparations. The paper's n = 10 implies it did the same, but there are only 9 distinct animals.
10. **[does not affect a conclusion] `abf_signal`.** It is annotated as returning a 2-tuple but returns 3 values. Files are decimated separately and joined across gaps of up to 1130 s (crab 16 at 1.5x), so some windows straddle a gap.

Checks that passed:
- On synthetic data, `semilog_fit`, `zero_slope_test` and `shared_slope_test` behave correctly: the Q10 is recovered, and P is small only when the slopes truly differ.
- They reproduce the deposited Prism outputs exactly in 7 comparisons.
- `rhythm_crash` reproduces the Prism crab crash temperatures exactly at 1x and 0.75x.

### C. What I could not check, and the output that would have let me

- **Lobster per-neuron crash data (fig5b, 6a, 6b).** I could not see whether it is in the lobster `1x saline` sheet (43×34, mostly unshown), the four `.mat` files, or the crab `Phase (Salinity)` sheet. A printout of those sheets' headers and a key listing of each `.mat` file would settle it.
- **Lobster salinity series (fig4b, 4d, 4e).** I could not confirm they are absent. The names of the 14 xlsx and 1404 txt files in Lobster STNS.zip, and the member list of at least one inner Raw Crab zip, would have done so.
- **fig8 crash judgement.** All 58 spectrograms (the criterion asks for them), plus the per-window peak frequency, would show whether the 2.3 Hz peaks in crab 18 are the pyloric rhythm.
- **fig5c.** A mixed-model run restricted to the Sheet4 ramps with a Crash mark (10/13/8).
- **fig5d.** A diff of the 1x-control points against the Prism or `.mat` fit data, to find the one extra point per set.
- **fig2i "same temperature".** A step-binned count (crash temperature rounded to the 2 °C ramp step), to confirm my 9 of 20 reading in code and not by eye.
