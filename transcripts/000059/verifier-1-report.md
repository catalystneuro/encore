**Verifier report, round 1: Petersen & Buzsaki 2020 on dandiset 000059 (0.250624.0444)**

The claims file has 38 claims. The notebook reports 37 as tested and 1 as blocked. My outcomes: 12 reproduced, 15 partially reproduced, 10 not reproduced, 1 blocked. The paper text is the PMC author manuscript, saved as `paper/PMC7442698.txt`.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| session-structure | reproduced | Cell 28: mean 143.8 trials, range 80–204, medians pre 39, cooling 47, post 44. All are inside the criterion's bounds. |
| cooling-time-course | partially_reproduced | Cell 30: median time to minimum is 121 s against 60 ± 6 s. Duration until back within 1 C of baseline is 12.16 min, inside 9–13.2. The paper's Results say about 45 s, its Methods about 60 s. |
| fig2g-theta-freq-temperature | reproduced | Cell 32: R = 0.789, P = 2.8e-43 (TEMP sessions). |
| fig2h-theta-power-temperature | not_reproduced | Cell 34: R = −0.056 (P = 0.44) on TEMP and 0.123 (P = 0.085) on BEH. Neither is positive at P < 0.05. |
| fig2j-frequency-consistent-across-animals | reproduced | Cell 36: frequency R is positive with P < 1e-22 in all four animals. Its range is 0.27 against 0.72 for power. MS10 has no recorded temperature, so it is absent. |
| fig2i-theta-pre-cooling-post | partially_reproduced | Cell 38: frequency is lower during cooling than pre (P = 1.4e-12) and than post (P = 5.7e-14). Power is lower than pre only marginally (P = 0.048, 26 of 45 sessions) and not lower than post (P = 0.94). |
| disc-theta-frequency-12-percent | partially_reproduced | Cell 40: decreases of 8.9%, 9.2% and 9.2%. All are decreases, none within 12 ± 1.2. |
| fig6d-errors-increase | partially_reproduced | Cell 42: ratios 2.28, 2.31 and 2.53, all outside 3.0 ± 0.3. Over sessions P = 3e-7. MS22 (12 sessions) has P = 0.064. |
| fig6e-errors-recover | reproduced | Cell 44: post against pre P = 0.84, median difference −0.13 points. |
| fig6c-worst-trials-4-to-8 | reproduced | Cell 46: the error peak is at trial 7, and the temperature minimum is also at trial 7. This is fragile: each animal's own peak falls at trials 14–26. |
| fig6f-errors-temperature | partially_reproduced | Cell 48: R = −0.84, −0.79 and −0.87, all with P < 1e-40. Negative, but far from −0.35. |
| fig6g-errors-theta-frequency | partially_reproduced | Cell 50: R = −0.87 and −0.73. Negative, but outside tolerance. |
| fig6h-errors-theta-power | partially_reproduced | Cell 52: only MS10 meets R < −0.3 with P < 0.01. One animal counts, against 2 expected. |
| fig6i-errors-not-speed | not_reproduced | Cell 54: MS13, MS21 and MS22 have P < 0.05 (R = −0.49, 0.22, 0.25). |
| fig4e-speed-decreases-within-session | reproduced | Cell 56: speed falls with trial number in 44 of 45 sessions, median rho −0.45, P = 4e-13. |
| fig5-speed-control-cooling | not_reproduced | Cell 58: reading (a) gives 78.9 and 74.9 cm/s, both outside. Reading (b) gives control 79.6 (inside) and cooling 76.0 (just below 76.3). |
| suppl2-place-cell-rates-decrease | partially_reproduced | Cell 62: decreases of 3.7–7.7% (within-field) and 5.3–6.7% (peak), P = 0.0024 and 0.0013. Both are significant, neither within tolerance, and neither reaches P < 0.001. |
| disc-interneuron-rates-decrease | partially_reproduced | Cell 64: decrease 6.5% (median) or 9.1% (ratio of means), P = 0.0017. The 14% is not reached. |
| fig4b-fp-flfp-decrease | reproduced | Cell 70: all six means are within the stated spreads (n = 361 fields against the paper's 365). Both fp and fLFP decrease during cooling, P < 1e-43. |
| fig4c-fp-flfp-correlation | partially_reproduced | Cell 72: R = 0.23, 0.44 and 0.16, all positive with P < 0.003, all outside tolerance. |
| fig4ac-fp-flfp-difference-preserved | not_reproduced | Cell 74: fp − fLFP is lower during cooling, P = 1.3e-4, median change −0.13 Hz. The mean change is mostly from MS12 (−1.03 Hz); the other animals are near 0. |
| fig4a-frequency-temperature-slopes | partially_reproduced | Cell 76: fLFP R = 0.677 and slope 0.0714 are within tolerance, as is the fp slope (0.086). The fp R of 0.338 is just below 0.342. |
| fig3c-field-size-correlated | reproduced | Cell 78: R = 0.8197 against a lower bound of 0.819, so it passes by 0.0007. The ≥100-spike variant (0.814) falls outside. |
| fig3d-size-fp-negative | partially_reproduced | Cell 80: R = −0.31, −0.31 and −0.32, all with P < 3e-9. Negative, but outside tolerance. |
| fig3e-model-field-size | partially_reproduced | Cell 82: pre R = 0.25 and cooling R = 0.34, both positive with P < 1e-5. Post is 0.33 against 0.11 expected. |
| fig3f-information-unchanged | not_reproduced | Cell 84: pre against cooling P = 0.014 and pre against post P = 0.0064. Problem 3 may explain this. |
| fig3hi-population-vector-unchanged | reproduced | Cell 86: P = 0.97 over n = 11 sessions, which gives the test low power. |
| fig4d-precession-slope-decrease | partially_reproduced | Cell 88: on slope magnitude, cooling is flatter than post (P = 0.022) but not than pre (P = 0.83). The signed reading is not significant. |
| fig4gh-fp-speed | reproduced | Cell 90: the fp slope (0.0136) is larger than the fLFP slope (0.0061), bootstrap interval 0.004–0.011. fp is lower during cooling in all 3 testable bins, which cover only 60–120 cm/s. |
| fig5d-ccg-period | partially_reproduced | Cell 92: the period lengthens during cooling (8 of 9 sessions, P = 0.0195) and the phase period does not change (P = 0.59). The control period is 109 ms against 85 ± 8.5, and that value is biased by the estimator (problem 1). |
| fig5cg-compression | not_reproduced | Cell 94: per-session decrease P = 0.0547, pooled pre compression 0.273 cm/ms against 0.54. Phase compression is unchanged (P = 0.43). |
| fig5h-time-lags-increase | reproduced | Cell 96: time lags are longer during cooling under both readings. Over pairs, against pre P = 1.1e-6 and against post P = 1.3e-10; over sessions P = 0.023 and 0.016. |
| fig5i-phase-lags-unchanged | not_reproduced | Cell 98: cooling against pre P = 0.0015 and against post P = 0.0043. |
| fig5j-fraction-active-unchanged | not_reproduced | Cell 100: pooled rank-sum pre against cooling P = 1.5e-22. Over session means P = 0.73 (problem 4). |
| fig5k-spikes-per-cycle-unchanged | not_reproduced | Cell 102: cooling against post and pre against post both have P ≈ 1e-52. Session means show no difference (problem 4). |
| suppl1g-waveforms-unchanged | not_reproduced | Cell 68: trough-to-peak P = 4.9e-10 and amplitude P = 5.7e-4 (median +0.8%, n = 646). See problem 5. |
| suppl2d-interneuron-oscillation-slows | reproduced | Cell 66: 9.55 to 8.66 Hz, lower in 105 of 114 units, P = 8.7e-16. The 9.4% decrease is close to the LFP's 8.8%. |
| suppl1-hippocampal-temperature | blocked (data_missing) | See the archive check below. |

Archive check for the blocked claim: the assets endpoint lists 100 files, all for the five behaving rats (sub-MS10 to sub-MS22). There is no subject or file for the MS-plus-hippocampus control experiment, and the dandiset metadata lists no temperature variable. The notebook read only the MS `Temperature` series and never printed the full list of series in `processing/behavior`. So "no second temperature channel inside the files" is stated (cell 8) but not shown. The claim's hippocampal part cannot be tested. Its MS onset part is covered by cooling-time-course.

No claim states a chance level, so that check does not apply.

### B. Problems

1. **[affects a conclusion]** `pair_period` (used in cell 92 for fig5d) is biased upward. It takes the largest local maximum 60–200 ms from the main peak. When the period is under about 100 ms, that window holds both the first and the second neighbouring peak. If the correlogram envelope is centred away from zero (field peaks 15 cm or more apart), the second peak is often larger.
   - Synthetic test: two cells oscillating at 10.6 Hz, true period 94 ms. For field separations ≥15 cm the function returned about 140 ms, the mean of a 94 ms and a 188 ms spacing. Separations of 0–10 cm returned 93–94 ms.
   - The control value of 109 ms (above 1/fp ≈ 95 ms) is therefore not a valid test of "85 ms".
   - Speed was lower during cooling (cell 58, P = 0.04), which spreads the envelope further in time, so part of the lengthening may also come from this bias.
2. **[affects a conclusion]** `peak_lag` (window ±70 ms) is used for fig5cg, fig5h and fig5i. The theta period is about 110 ms, so the window often holds two candidate peaks. That ambiguity, plus noise in the x variable (tau), flattens the Ltr-on-tau slope: pooled R is only 0.195 and compression 0.273 against 0.54. The criterion fixes this method, but the compression magnitude cannot be judged from it.
3. **[affects a conclusion]** fig3f, cell 84: Skaggs bits per spike are biased upward when there are fewer spikes. The pre state has fewer trials than cooling or post (medians 39, 47, 44). Information falls in order pre > cooling > post, which matches that bias. No subsampling to equal spikes or occupancy was done.
4. **[affects a conclusion]** fig5j and fig5k, cells 100 and 102: rank-sum tests over theta cycles pooled across sessions are confounded by session make-up. Per-session means range from 0.16 to 0.32 (fraction active) and 18 to 91 (spikes), and states contribute different numbers of cycles from each session. Session-level tests give P = 0.73 (fraction active), 0.57 and 0.13 (spikes), which fits the paper's claims. The outcomes stay not_reproduced under the criterion, but they reflect the test, not a clear effect.
5. **[may affect a conclusion]** suppl1g, `unit_session` / `waveforms_chunked`:
   - Peak-to-peak amplitude of a mean waveform rises with noise when fewer spikes are averaged. The two windows can have different counts (rates fall during cooling; there is a 300-spike cap). The counts per window are never shown.
   - The windows are also 7–30 minutes apart, so probe drift is mixed with the cooling effect.
   - The +0.8% amplitude result may be artefactual. The trough-to-peak shift (higher in 294 units, lower in 143) is less easily explained this way.
6. **[does not affect a conclusion]** cooling-time-course, cell 30: baselines in MS21-180622, -180623, -180720 and MS22-180621 come from artefact-contaminated traces (37–42 C). In MS21-180720 the onset was detected 413 s before the first cooling trial, with a "minimum" of 39 C. The median over 37 sessions is barely affected.
7. **[does not affect a conclusion]** cooling-time-course: the minimum is the argmin over 5 minutes. A slowly drifting plateau pushes it late, so 121 s may not measure "peak effect". The criterion fixes this measure.
8. **[does not affect a conclusion]** Cell 70: the "≥30 spikes" variant is the same as the main result, because `oscillation_frequency` returns NaN below 50 spikes. It tests nothing.
9. **[does not affect a conclusion]** Cell 38: `out[(m, other)] = (p, lower < n - lower)` has its direction inverted. It is never used.
10. **[does not affect a conclusion]** fig4a windows in `unit_session`: `range(0, n_tr - 20)` drops the last 20-trial window. The P value pools about 52,000 overlapping windows, which is pseudo-replication; the paper's code does the same.
11. **[does not affect a conclusion]** `theta_from_lfp` computes the spectrogram on the 4–10 Hz filtered signal. On a synthetic sine of equal amplitude, power reads about 5% lower at 8.5 Hz than at 7.7 Hz, which partly masks a cooling power drop. I checked the paper's `calcInstantaneousTheta.m` (commit aec2f7e) and it does the same, so this is faithful to the paper. It matters only for reading fig2h, fig2i (power) and fig6h.
12. **[does not affect a conclusion]** `stream_lfp` assumes LFP column *i* is electrode-table row *i*, without checking the LFP `electrodes` region. Theta slowing comes out as expected, so the channel is at least hippocampal.
13. **[does not affect a conclusion]** `aligned_series` finds the end of the first block only as a Post-Cooling trial followed by Cooling on. A Cooling off → Cooling on transition would leave the second cooling block in the series.

The other helpers behaved correctly on synthetic inputs: `oscillation_frequency` (7.7, 8.5, 10.6, 12 Hz came back as 7.75, 8.47, 10.87, 11.9), `gausswin`, `circ_lin_regression`, `skaggs_information`, the alignment to position 65, and the instantaneous theta frequency. Every number in the notebook comes from the loaded files. I found no train/test leakage; no claim involves a decoder.

### C. What I could not check, and the output that would settle it

- **Per-pair period estimates (fig5d):** a histogram of per-pair periods and spacings, |Ltr| for each pair, and the fraction of pairs where the chosen neighbour sits near twice the period. The median period over pairs with |Ltr| < 10 cm would show whether 85 ms holds with the bias removed.
- **Waveform spike counts (suppl1g):** `nwf_pre` against `nwf_cooling`, and the amplitude change for units at the 300-spike cap in both windows.
- **Information with equal sampling (fig3f):** bits per spike recomputed with equal spike counts or equal trial counts per state.
- **Cooling time course:** an onset-aligned mean MS temperature trace in seconds, and the time to reach 90% of the drop.
- **Hippocampal temperature:** a listing of every TimeSeries in each file's `processing/behavior` (and `acquisition`), to confirm there is no hippocampal temperature series.
- **Theta channel:** the LFP `electrodes` region indices against the `theta_reference` row.
- **fig5j and fig5k:** session-level tests for all three comparisons, and mean cycle duration by state.
- **fig6c:** the mean smoothed error series for trials 21–40 after onset, and the number of sessions contributing at each position.
- **Second cooling blocks:** state sequences of the two-block sessions, to confirm where `aligned_series` cut each series.
