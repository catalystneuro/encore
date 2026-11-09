**Verifier report, round 1: doi:10.7554/elife.112525 on DANDI:002034 (0.261019.2146)**

The claims file holds 17 claims, and the notebook tests all 17; it marks none as blocked. On my reading of the outputs, 13 reproduce, 2 partially reproduce and 2 do not.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| include-list-link | reproduced | Cell 9: 83 sessions and 105 units on both sides, nothing unmatched in either direction. Cell 10: 26 of 26 values match the code's printed output (2 trial counts, 12 population tests, 4 range correlations, 8 LLR counts). |
| data-units-sessions | reproduced | Cell 12: Oz has 42 units in 32 sessions and Ci 63 in 51, all with beep trials, under both the Methods and the code trial rules. Tolerance is 0. |
| fig2-row1-baseline-lc-pupil | reproduced | Cell 14 (M-E1 = M-E2): Oz median 0.0795, p_T1 = 5.5e-4 (paper 8.6e-4); Ci median 0.0926, p = 1.4e-5 (paper 9.85e-6). |
| fig2-row2-evoked-lc-pupil | reproduced | E1: Oz 0.118, p = 0.011; Ci 0.024, p = 0.0028. E2: Oz 0.092, p = 0.020; Ci 0.053, p = 0.0026. Both readings are positive and significant in both monkeys. |
| fig2-row3-pupil-evoked-vs-baseline | reproduced | E1: Oz −0.33, p = 7.9e-6; Ci (51 sessions) −0.45, p = 2.0e-9. E2: Oz −0.37, p = 1.1e-6; Ci −0.37, p = 5.2e-9. The 50-session variant gives the same result. |
| fig2-row4-lc-evoked-vs-baseline | reproduced | Oz −0.382, p = 1.2e-6; Ci −0.297, p = 1.5e-11. |
| fig2-row5-baseline-lc-vs-evoked-pupil | reproduced | E1: p = 0.80 (Oz) and 0.94 (Ci). E2: p = 0.99 and 0.95. Medians are 0.007 to 0.023. |
| fig2-row6-baseline-pupil-vs-evoked-lc | reproduced | Oz p = 0.965. Ci median −0.022, p = 0.034, which matches the paper's pattern. This is fragile: with the code's removal of two units, Ci gives p = 0.064 (see B6). |
| cross-epoch-no-reliable-relation | reproduced | Cell 17: rows 1 and 2 hold in both monkeys under E1 and E2. Rows 5 and 6 are never significant with the same sign in both monkeys. |
| range-baseline-pupil-evoked-lc | reproduced | Cell 19, Methods readings: Oz rho = 0.044, p = 0.78; Ci rho = 0.067, p = 0.60. Both p ≥ 0.05. |
| range-baseline-lc-evoked-pupil | not_reproduced | Cell 20, Oz: E1 rho = −0.04, p = 0.80; E2 rho = −0.13, p = 0.40. Both are non-significant, so E1 and E2 agree and the claim is not blocked. Only the code's 0–800 ms evoked pupil gives −0.332, p = 0.032. Neither variant that mixes the Methods and code choices does (−0.12 and −0.20, both p > 0.2). |
| figs1-raw-baselines-similar | partially_reproduced | Cell 22: 11 of 12 cells match under both E1 and E2. Row 6 in Ci with raw baselines gives p = 0.136, not significant. The code's reading matches 12 of 12. |
| figs2-llr-pupil-baseline-evoked | reproduced | Cell 24, M-E1: Oz 6/32 (expected 7) and Ci 7/51 (expected 6), both within ±1 and under half the sessions. Under M-E2, Oz is 5/32, outside tolerance, but the criterion needs only one reading. |
| figs2-llr-lc-baseline-evoked | reproduced | Cell 25: Oz 3/42 (expected 2) and Ci 4/63 (expected 3), within ±1 under every Methods reading. |
| figs2-llr-cross-epoch | not_reproduced | Cell 26: no Methods reading has all four counts within ±1, because Ci evoked pupil on baseline LC is 6 or 7 against 4. The partial rule (each count below a tenth of the units) also fails: Oz is 5/42 = 0.119 under E1 and 6/42 under E2. Only the code reading reproduces. The paper's broader point, that few relations are quadratic, still holds (all counts ≤ 14%). |
| fig3-pooled-within-epoch | reproduced | Cell 28: 8 of 8 cells match in sign with p < 0.05 under E1 and E2, with either z-scoring grouping. |
| fig3-pooled-cross-epoch-null | reproduced | Cell 30: 0 of 60 cells are significant with the same sign in both monkeys. Only Ci's negative group in column 6 is significant (p = 0.012). |

No claim was treated as blocked, so step 4 does not apply. The archive API confirms that version 0.261019.2146 has 83 files (532,535,376 bytes), consistent with the notebook.

The paper's only chance level is the LLR critical value of 3.841 (χ²(1), α = 0.05), and the notebook uses the same value (`LLR_CRIT`).

### B. Problems

1. **[does not affect a conclusion]** `pupil_trial_measures` and `unit_trial_rates` treat the trial start as fixation onset, and the data contradict this; cell 3 prints the evidence. The Methods put the beep 1–1.5 s into fixation, but only 8.8% (Oz) and 4.4% (Ci) of beeps fall 1000–1500 ms after the trial start; the median is about 2.2 s. The Methods give fixation of 1–5 s, but 26% of Oz fixation-only trials are under 1 s, and some beeps fall before the start or after the end. Cell 4 states the assumption but never resolves it, so the Methods-reading baseline windows may not be the Methods' windows. The files offer no other anchor, the code uses the same one, and the code reproduces the paper's numbers, so no outcome changes.
2. **[does not affect a conclusion]** `pupil_preprocessing_check`, cells 3–4: the conclusion that the stored trace is already z-scored rests on per-session SDs of 0.80 to 0.99 and a boxcar change of about 4%. That supports the claim but does not prove it. It sets the main reading for Figure 3, but z-scoring again would barely change pooled Spearman correlations at these SDs.
3. **[does not affect a conclusion]** `pupil_trial_measures`, `methods_ok`: under the Methods rule a beep trial needs only one 50 ms window before end − 20 ms, so the beep can be as little as about 70 ms before the trial ends. `unit_trial_rates` still counts spikes over 0–200 ms after the beep. The notebook never checks whether spikes are stored past `stop_time` or how many trials this affects. If spikes stop at the trial end, the evoked rate is biased low on those trials.
4. **[does not affect a conclusion]** `fig3_pooled`: the positive and negative unit groups come from all 63 Ci units. The claims file says the code forms its groups after the two-unit legacy removal, and that variant was not run. No cell is near significance in both monkeys, so the outcome is safe.
5. **[does not affect a conclusion]** Cell 10 rounds medians to 3 decimals before applying the 0.0015 tolerance (row 6 Ci: −0.0375 is rounded to −0.038, against the code's −0.037). The true difference is still within tolerance.
6. **[does not affect a conclusion]** In row 6 for Ci, the deciding reading gives p = 0.034 with 63 units, but 0.064 with the code's 61 (cell 14). The outcome rests on the claims file's choice of the paper's denominator. That choice is correct, but the result is fragile and the notebook should say so.
7. **[affects a conclusion; finding, not an error]** The paper's Oz range result in range-baseline-lc-evoked-pupil, and the exact LLR counts in figs2-llr-cross-epoch, appear only with the code's evoked pupil (0–800 ms window, centred movmean). They do not appear with the Methods' definition (50 ms windows, 10 ms steps, beep to 20 ms before the end of fixation). The notebook ran every reading the paper allows, so this is how the outcome comes about, not a fault in the analysis.
8. **Synthetic tests: no errors found.** `_window_means`, `_movmean_omitnan` (against a brute-force window), `llr_quadratic` (against an explicit Gaussian ML log-likelihood), `partial_spearman` (against the Pearson correlation of rank residuals), `_signed_absmax`, and the E1/E2/C windows on a synthetic trial all behave as documented.

No misreading of the paper by the claims file found. One remark: the "below a tenth" partial threshold in figs2-llr-cross-epoch is strict relative to the 5% false-positive rate that the 3.841 cutoff implies (5/42 fails it).

### C. Could not check

- **What the trial start is, and whether spikes and pupil continue past `stop_time`.** I could not settle this without the data. A cell printing the spike times relative to each trial's `stop_time`, plus the number of Methods-rule beep trials with less than 200 ms after the beep, would have settled B3.
- **The code's legacy-row ordering in `unit_order`.** I checked it only indirectly, through the 26/26 match. Printing which units hold rows 43 and 65 and their row-1 group membership would have settled B4.
- **How close the LLR counts are to the cutoff.** Per-unit LLR values near 3.841 under M-E1 and M-E2 for the cross-epoch fits would show how sensitive the not_reproduced outcome is.
- **The paper's 51st Ci session against the code's 50, and its 63 against 61 LLR denominators.** The archive cannot say which units the paper actually used beyond the include lists.
