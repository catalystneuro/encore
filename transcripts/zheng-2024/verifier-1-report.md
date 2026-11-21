**Verifier report, round 1: Zheng et al. 2024 on DANDI:000552 (0.261113.1035)**

The claims file has 32 claims. The notebook tests 29 and treats 3 as blocked (fig7-preexisting-across-days, figs15-imaging-not-artifact, figs1-not-electrode-drift).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1d-pv-decorrelation | reproduced | Cell 11: lags 1–10, slopes negative in 90/90 familiar units (p = 1.7e-16) and 14/14 novel units (p = 1.2e-4). |
| fig1e-novel-drift-faster | reproduced | Cell 13: n = 104 (expected 106 ± 10.6), novel more negative, rank-sum p = 0.015. Cohen's d is 0.51, just under the 0.522 tolerance bound under all five seeds (cell 37). The criterion only asks for d to be reported. |
| fig1e-later-lags-no-difference | reproduced | Cell 13: lags 11–20 p = 0.76 (n = 28); lags 21–30 p = 0.064 (n = 6, of which 2 familiar, d = −2.87). Both p ≥ 0.05, but the 21–30 window is close to significant and rests on 6 units. |
| fig1h-rate-decorrelates-location-stable | reproduced | Cell 17: peak-rate slopes are negative in 52/52 units (p = 3.5e-10). The median rate slope (−0.030) is 83× the median location slope (−0.00036), well above the factor of 2. |
| fig1i-location-mse-increases | reproduced | Cell 19: (a) slope positive in 51/52 units, p = 3.7e-10; (b) OLS p = 1.2e-10. |
| switch-step-size-filter | not_reproduced | Cell 21: 2,770 putative switching fields under every reading, against 3,184 ± 318. Removed fields are 191 (code normalisation, both environments), which is inside 212 ± 21.2 only by 0.2 and falls outside under seed +2000 (187). The 7% fraction itself matches (6.9%). |
| fig2d-switch-fractions | not_reproduced | Cell 23, familiar: 1,889 switching fields (expected 2,310 ± 231), OFF fraction 0.078 (expected 0.081–0.099), ON fraction 0.127 (at the edge of 0.126–0.154). Novel OFF fraction 0.158 is also outside (0.162–0.198). The partial criterion needs the four ON/OFF fractions in tolerance, and two are not. |
| fig2e-switch-fraction-by-experience | reproduced | Cell 25: medians 0.143, 0.208 and 0.306 are all in tolerance. The three tests give p = 4.8e-5, 0.017 and 6.2e-5, in the stated directions. The result is stable over seeds. |
| fig3df-step-beats-polynomial-fields | partially_reproduced | Cell 27: the change-point model is better for 0.966, 0.951 and 0.908 of fields at K = 1, 2, 3. That is above 0.96 only at K = 1 and above 0.90 at every K. Familiar-only K = 3 is 0.895. |
| fig3df-polynomial-beats-step-population | reproduced | Cell 29: the polynomial is better in 0.87, 0.83 and 0.86 of units, Wilcoxon p ≤ 1.9e-10 for each K. |
| figs4g-population-vectors-gradual | not_reproduced | Cell 31: the polynomial is better in only 0.43, 0.51 and 0.40 of units (expected 0.54–0.77). The mean R² difference favours the change-point model (d = +0.20, +0.16, +0.08) and is not significant (p = 0.096, 0.17, 0.073). |
| fig3k-switch-abrupt | reproduced | Cell 33, reading (a): fraction of passage times under two trials is 0.808 (ON) and 0.813 (OFF), inside 0.675–0.847. Reading (b) (durations) gives 0.53/0.54. The chi-squared fit to NB(2, 0.5) rejects strongly (p ≈ 1e-40 and 1e-31); it is reported only. |
| figs5-switchers-drive-drift | reproduced | Cell 35, pooled turns: switchers decorrelate faster in familiar (p = 3.7e-9) and novel (p = 0.0078); the per-turn reading agrees. Median differences (−0.0067 and −0.0096) are outside tolerance; the criterion only asks for them to be reported. |
| fig4-glm-deviance | partially_reproduced | Cells 39–40: in-sample deviance explained is 0.202 (ON) and 0.142 (OFF), both in tolerance. Cross-validated OFF is 0.123, outside. ON's top three predictors are Position, Animal, N_field, as claimed; OFF's are Trial, N_field, Animal. The criterion does not cover "values hold, ranking holds for one of ON/OFF", so this outcome is my judgment. |
| fig4-delay-zone-more-switching | not_reproduced | Cell 42: the central, choice and return-side coefficients are **positive** relative to the delay zone for ON and OFF, with most intervals excluding zero. Per-field rates are also lowest in the delay zone. This is the opposite of the claim. |
| fig4di-switching-decreases-with-trial | partially_reproduced | Cell 46. Reading (ii), trials from the fourth on, gives 1,031/288 trials, matching the paper's 1,029/281. Three of four correlations are negative at p < 0.05; novel ON is r = −0.084, p = 0.15. All four r are well short of the reported −0.15 to −0.23. Reading (i), all trials, gives no significant negative correlation (familiar ON r = +0.073). |
| fig4-behavior-not-predictive | not_reproduced | Cell 42: the Prev_correct interval for ON is [−0.268, −0.022], which excludes zero (p = 0.021). Separately, the median held-out drop for Speed (ON) is above zero (0.0013), though below its SD over splits. |
| figs8-speed-no-trend | not_reproduced | Cell 48: speed-against-trial r = +0.154 (familiar) and −0.148 (novel), against expected 0.01 ± 0.05 and −0.02 ± 0.05. The speed–switching correlations are not clear (\|r\| ≤ 0.03). This outcome is uncertain; see B5. |
| fig4no-head-scans-not-related | partially_reproduced | Cell 50: the head-scan maximum is at bin 50 (111 cm), the reward end of the choice arm. Per bin, the central arm (9.7) is lowest, but only barely below the delay zone (10.0); in raw totals the central arm (253) has more than the delay zone (160). Switch-ON trials per bin correlate positively with head-scan trials per bin (r = 0.255, p = 0.01), so the "no relationship" part fails. |
| figs9-splitter-switching | reproduced | Cell 52: splitter fields switch ON (9.1% familiar, 18.1% novel) and OFF, with switches in every third of the session. |
| figs13-btsp-signatures | partially_reproduced | Cell 54. Holding: width–speed correlation in familiar (p = 0.0099 / 0.0049), familiar backward shift (p = 2.7e-4), trial 0 vs 1 not significant (p = 0.44 / 0.59). Failing: the novel shift is significant (p = 0.014, paper 0.52), and trial −3 vs −2 is not (p ≈ 0.08). That is 3 of 5. |
| fig5c-switchiness-not-intrinsic | reproduced | Cell 56: switchiness t = 1.31, p = 0.19 (not significant). CV t = 6.63 and lap correlation t = 9.20, both significant and positive. n = 1,006 is in tolerance. Both t values are above their tolerance bands (4.8 ± 0.48, 7.9 ± 0.79). |
| fig5d-nrem-rate-relations | reproduced | Cell 56: all six regressions match the paper in sign and significance. |
| multifield-independent-switching | not_reproduced | Cell 60: 271 pairs with 34 (any switch) or 20 (same type) on the same trial, against 781 and 41. The any-turn variant gives 615 and 34, also outside tolerance. |
| figs12-stability-after-switch-on | partially_reproduced | Cell 62: all CV and location-SD tests go in the stated direction with p < 0.05, under both middle-window readings. Most medians are outside tolerance (for example switch-ON familiar CV 0.233 vs 0.283; middle-window familiar CV 0.342/0.349 vs 0.40), and the group sizes are about a third of the paper's (400 vs 1,230 switch-ON fields). |
| fig6-co-switching | not_reproduced | Cell 64, reading (a): familiar sessions 16/45 (ON) and 14/45 (OFF), against about 8 and 9. Novel 4/7 ON matches; novel OFF is 3/7 against 2/7, within one session. Reading (b) is far higher. The result is stable over seeds. |
| fig6f-switching-asynchronous | reproduced | Cell 66: the 95th percentile of per-trial switching fractions is 0.013–0.022 in all four groups. The maxima are 0.037–0.090. |
| figs14-preexisting-fields-ephys | partially_reproduced | Cell 68: within-field rate is above outside for 58–84% of fields in every group, and the session tests give p ≤ 0.0078. The below-threshold fractions do not both match under either reading: mean-rate reading ON 0.658 (in tolerance) but OFF 0.433 (expected 0.2); peak-rate reading ON 0.426 and OFF 0.248. |
| figs2-chr2-no-effect | reproduced | Cell 70: 4,243 place cells; four categories p = 0.215; switching against not switching p = 0.41. The all-pyramidal five-category table (p = 3e-8) adds "not a place cell", which is outside the claim. |
| fig7-preexisting-across-days | blocked (data_missing) | Confirmed: the dandiset holds only electrophysiology; the imaging data are available on request only. |
| figs15-imaging-not-artifact | blocked (data_missing) | Same as above. |
| figs1-not-electrode-drift | blocked (too_large), part testable | The archive has raw_ecephys files for 11 sessions (52–175 GB each), covering 2,000 of the 3,430 switches. The processed units table has only `waveform_mean`. A subset test (one or two sessions, about 38 MB per switch) was feasible; only the full test is too large. |

The notebook states no chance levels for these selections, so there were none to compare with the paper's.

### B. Problems

1. **[affects a conclusion] figs8 speed–trial unit of analysis (cells 46 and 48).** The paper's familiar r = 0.01 with p = 3e-11 implies about 4×10⁵ samples, so it almost certainly correlated per frame or per bin, not per trial. The notebook uses per-trial mean speed (n = 1,166), from linearised velocity, where the Methods use 2D speed. No per-sample reading was run, and that reading could change the outcome. The claims file also leaves the unit open.
2. **[affects a conclusion] fig6 co-switching null (`coswitch_tests`, cell 64).** Each field's switch trials are shifted circularly over all session trials. Turn-specific fields can only switch on their own turn's trials, so the null does not respect turn structure. In my synthetic test with independent, turn-confined switches this gave a 10.5% false-positive rate at α = 0.05, which may contribute to the excess of significant familiar sessions. The criterion's lag-1 window variant was not run.
3. **[affects a conclusion] figs12 selection (cell 62).** The notebook adds "no OFF" to "switched ON once" and requires n ≥ 10 trials for non-switching fields; neither is stated as an assumption. Group sizes come out about 3× below the legend's, which bears on the median tolerances.
4. **[affects a conclusion] fig4-glm-deviance criterion gap.** The partial clause does not cover the observed case (values in tolerance, ranking holds for ON but not OFF). The paper itself says Trial contributes more to OFF.
5. **[affects a conclusion] Upstream field/switch counts (`pooled_map_and_null`, `detect_switch`).** Familiar fields come out about 9% low and switching fields 18% low, which drives the fig2d, switch-step-size-filter and multifield outcomes. Possible causes:
   - The detection map pools counts over trials (cited to the paper's code), whereas the Methods average per-trial maps.
   - Ties in the minimum p across K go to the smaller K, labelled "standard". In my synthetic test, ties occurred in 189 of 200 fields, so this choice can change K and the number of switches.
   - One familiar session (e13_26m1_210913) is missing from the archive; I confirmed it is absent.
   
   None of these alternatives was run.
6. **[does not affect a conclusion] fig4di, reading (ii).** Excluding the first three trials removes structural zeros at the start, but the structural zeros at the end remain (a change point cannot fall on a turn's last trial). This biases r negative. It probably matches the paper's own procedure, given the trial-count match.
7. **[does not affect a conclusion] fig1h (cell 17).** The slope is fitted over all trial pairs rather than over per-lag averages as the criterion says. The margin (×83) is far from the threshold of 2.
8. **[does not affect a conclusion] Cell 5 mislabel.** The data check prints e13_26m1_211116 as a "familiar session with fewer than 7 trials in a turn"; it is the novel linear-maze task.
9. **[does not affect a conclusion] Data version.** The notebook departs from the cited version (0.230630.2304). The justification is shown in cell 7 (the cited version has no cell-type or light-responsive labels; spike times are identical) and is reasonable.
10. **Helper checks on synthetic inputs, all passed:**
    - `optimal_partition` matched brute force in 200/200 cases.
    - `vector_cpm_r2` equals `r2_step` on one column.
    - `passage_times` on a pure step gives 0.764 of passage times under two (0.75 expected) and 0.515 of durations under two (0.5 expected).
    - `lag_slope` recovers the true slope.

### C. Not checked

- **The paper's code.** It is not under `paper/`, so I could not verify any code-cited detail: segment cut points, pooled vs per-trial detection map, tie rule, `gen_circular_shuffle` trial indexing, splitter merging.
- **The processed NWB contents.** h5py was not available. Asset metadata lists an ElectricalSeries in the 5–6 GB processed files; it is probably LFP, but I could not confirm there are no per-spike amplitudes.
- **Figures.** The notebook has no image outputs to look at.

These outputs, if added to the notebook, would have let me check more:

1. Per-session field and switching counts beside the code's stored fig1 outputs.
2. The best-K distribution with ties broken toward the larger K.
3. The fig6 null with shifts within each turn's trials, plus the lag-1 variant.
4. figs8 speed against trial per frame or per position bin, and with 2D speed for the familiar sessions.
5. A plot of segment boundaries on the linearised track with field-peak counts per segment, for fig4-delay-zone-more-switching.
6. figs12 counts under the alternative "one ON switch, OFF allowed" selection.
7. A figs1 test on one raw-file session.
