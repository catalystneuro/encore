**A. Outcomes** (25 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| figs1-ih-reduced-11c | blocked (data_missing) | In 310115, VoltageClampData.mat has one trial per experiment, and none is a Cs+ trial (cell 19). Only 2 cells at 11 °C have both conditions (VoltageClampTraceData); a paired test on 2 cells cannot meet the criterion. The values typed into the deposited script reproduce the paper (cell 23), but they are not derived from data. |
| figs1-ih-reduced-21c | blocked (data_missing) | Same as above: 2 paired cells at 21 °C. |
| fig1-cs-lower-frequency-11c | reproduced | Saline 1.17±0.15 Hz, Cs+ 0.86±0.22 Hz, both within tolerance. Paired t p=8e-7, Cs+ lower in 20/20 (cell 25). n=20, not 21: 969_070 has no 11 °C cycles in Cs+, and the deposited value is NaN too. |
| fig1d-difference-grows-with-temperature | reproduced | 19 complete experiments, F(5,90)=44.0, p=1e-22. Mean difference rises from 0.31 Hz at 11 °C to 0.83 Hz at 21 °C (cell 27). |
| fig1e-q10-lower-in-cs | reproduced | Reading (a): saline 1.68±0.32, Cs+ 1.35±0.45, p=4.5e-5. Readings (b) and (c) agree (cell 29). |
| fig1f-two-saline-frequency-change-same | reproduced | 0.89±0.30 against 0.78±0.30 Hz, paired t p=0.137 (cell 31). This re-runs the test on the authors' ControlTable means, because only 981_025 has spike data. Swapping in 981_025's recomputed values gives p=0.130 (my check). |
| fig1e-two-saline-q10-same | blocked (data_missing) | Reading (a) needs six holding-temperature means per protocol; the archive lists no spike or raw file for 5 of the 6 controls. Variants: deposited Q10 p=0.144, reading (c) p=0.133 (cell 33). |
| fig1e-saline-q10-same-across-designs | blocked (data_missing) | Same reason. Variants give p=0.24–0.26 (cell 33). |
| fig2c-decrease-by-depolarizing-phase | reproduced | Reading (a): depolarizing share 1.30 and 1.63 in the 2 Cs+ experiments with PD traces (cell 35). Reading (b): >0.5 in 4 of 5 intracellular experiments (cell 36). The Cs+ + PTX example is outside the criterion and was not tested. |
| fig3d-freq-decrease-while-warming | reproduced | Centred smoothing, window span: saline 6.3±4.8%, Cs+ 31.0±15.7%, Cs+ higher in 20, p=4e-7. All four variants are also within tolerance (cell 38). |
| fig3e-freq-increase-when-stable | reproduced | Saline 13.2±5.4%, Cs+ 26.9±6.2%, Cs+ higher in 20, p=3e-9 (cell 38). |
| fig4c-ptx-restores-frequency-change | partially_reproduced | Under the criterion's 0.3 °C rule, 981_035 (both entries) has no 21 °C value: n=4, F(2,6)=4.20, p=0.072. Only with the author's 0.5 °C widening and the paper's six entries are all conditions met, and only under O5(b) (Cs+ vs Cs+ + PTX p=0.037; multcompare p=0.106). The five-preparation variant fails (cell 40). |
| fig4d-ptx-keeps-decrease-while-warming | reproduced | Six entries: F(2,10)=13.0, p=0.0017. Saline is below both Cs+ conditions under both O5 readings; Cs+ vs Cs+ + PTX p≈0.95. Holds for five preparations and all smoothing variants (cell 41). |
| fig4e-stable-increase-ordering | reproduced | F(2,10)=79.5. Means 7.5 < 24.6 < 38.0. All three pairs p≤0.012 under both readings (cell 42). |
| fig5b-pd-burst-shorter | reproduced | 164±36 against 145±19 ms, Wilcoxon p=0.012, n=20 (cell 45). |
| table1-pd-off-advanced | reproduced | 0.198 against 0.126, p=6e-8 (cell 46). |
| table1-lp-on-advanced | reproduced | 0.404 against 0.295, p=2e-7 (cell 46). |
| table1-lp-off-advanced | reproduced | 0.671 against 0.571, p=4e-7 (cell 46). |
| table1-py-phase-unchanged | reproduced | n=12. PY ON paired t p=0.73, PY OFF Wilcoxon p=0.42 (reading b: 0.79). All means within tolerance (cell 47). |
| fig5d-pdoff-lpon-delay-smaller | reproduced | 0.206±0.062 against 0.169±0.044, p=0.008 (cell 48). |
| lp-duty-cycle-preserved | reproduced | Mean difference -0.009, p=0.449 (cell 49). |
| matched-period-lp-earlier | reproduced | Under reading (b): PD shortening 63±35 ms, LP advance 96±71 ms, PY 23 ms, LP > PD, r=0.10, p=0.69 over 19 pairs. Reading (a) fails (LP advance 39 ms, r=0.50, p=0.02) (cell 51). |
| fig6a-lp-off-advances-saline | reproduced | Advance 0.076 per 10 °C, adjusted Wilcoxon p=1e-4 (reading a); reading (b) 0.069, p=2e-4 (cell 53). |
| fig6a-lp-advances-cs | partially_reproduced | LP OFF holds (0.096 and 0.116, adjusted p 0.004 and 0.002). LP ON means are within tolerance (0.010 and 0.030), but adjusted p is 0.029 and 0.033, above 0.01 (cell 53). |
| fig6a-pd-py-phase-constant | reproduced | No adjusted p below 0.05 for PD OFF, PY ON or PY OFF in either condition under either reading (minimum 0.27). LP ON in saline is also not significant (0.37–0.38) (cell 53). |

Totals: 19 reproduced, 2 partially reproduced, 0 not reproduced, 4 blocked. The paper states no chance level for any selection.

**B. Problems**

1. **fig4c, cell 40 [affects a conclusion].** The claim passes only by widening the 21 °C margin to 0.5 °C, which departs from the criterion's 0.3 °C. The notebook says so, and the paper's own N=6 includes 981_035, which never got within 0.3 °C of 21 °C, so the widening is a reasonable assumption. It also changes the other experiments' 21 °C values slightly. Even then, the outcome depends on the O5 reading.
2. **Cells 8–10, "one preparation entered twice" [does not affect a conclusion].** This is asserted, not shown. Identical temperatures fit two preparations sharing one thermocouple just as well. The two trains have different cycle counts (9176 against 6950, cell 4) and very different Cs+ responses (frequency change 0.571 against 0.011 Hz; jag 19.5% against 54.4%), which two PD neurons in one rhythm could not produce. Burst onsets of `PD` and `PD2` were never compared, so the "five preparations" variant may not be the right correction.
3. **`extract_bursts` [does not affect a conclusion].** I tested it on a synthetic train with one stray spike. After the outlier removal, the start times of the remaining cycles are no longer consecutive, while `freq` and `period` are kept from before. `phase_calc` and `cycle_temperature` then treat the gap as one cycle spanning several real ones, with the old period as the divisor. This is rare, but it is not checked against the deposited MATLAB.
4. **`jag_measure`, cell 38 [does not affect a conclusion].** The main reading defines stable cycles as |dT| < 0.01 (deposited code and the Fig 3A legend). The Methods and the claims header define them as dT ≤ 0.01. The "steps" variant uses dT ≤ 0.01 and also reproduces. O3(b), the whole recording including cooling, was never run, because the Timings windows end at the 21 °C hold. Smoothing is applied across condition boundaries.
5. **`hold_means` `strict_cs` [does not affect a conclusion].** Cell 25 uses a strict < 0.3 °C bound for Cs+, while cells 44 and 53 use ≤. The asymmetry is presumably copied from the deposited code but is not stated in the notebook.
6. **`first_hold_cycles` reading (b), cell 44 [does not affect a conclusion].** It is limited to the span of reading (a)'s cycles, so it cannot reach the full yellow holding period of O4(b) and is barely an independent reading. The slope reading (b) in cell 53 likewise uses only cycles within 0.3 °C of each target rather than "all cycles".
7. **`ih_readings`, cell 22 [does not affect a conclusion].** It gives negative Ih in every Cs+ cell and in the saline LP cell at 11 °C, with "reductions" of -87% to 319%. The step's end or the steady-state window was most likely misplaced, and it was not checked against the voltage trace. It is not used for an outcome.
8. **Clock check, cell 11 [does not affect a conclusion].** It is weak: the best lag is within 0.5 min in only 8 of 21 experiments. The close agreement with SummaryStatistics.mat (cell 15) is the real support. The large outliers there (LP ON in Cs+ up to 0.85, frequency up to 0.2 Hz) were not explained.
9. **Claims file wording, not corrected [does not affect a conclusion].** It calls the controls "two consecutive saline step protocols"; the paper says "two consecutive temperature changes in saline". ControlTable shows the second protocol was a ramp in 3 of 6 (cell 17).
10. **fig2c, cell 34 [does not affect a conclusion].** The notebook says the Cs+ + PTX example cannot be identified, but the archive holds Raw_Expt_969_147.mat, a PTX experiment, and Raw_Expt_969_087.mat, which the notebook did not open. Either may carry the Figure 4G trace, or a third Cs+ PD trace for reading (a).

**Blocked claims, checked against the archive (Dryad API file lists of 310115 and 290160)**

- **Ih claims.** In 310115, VoltageClampData.mat is 98 MB; in 290160 it was 814 MB, so the earlier version probably holds every trial, Cs+ ones included. Within the pinned version, only the 4 paired cells in VoltageClampTraceData can be tested, which is a descriptive look at most.
- **Control Q10 claims.** Neither version has spike or raw files for 965_129, 965_134, 965_139, 965_146 or 982_005. The raw files are 969_087, 969_113, 969_115, 969_137, 969_147, 981_007 and 981_037, none of them a control. Reading (a) can be computed only for 981_025; readings (b) and (c) only from ControlTable.

**C. What I could not check**

- The deposited MATLAB scripts (not available to me), so whether the ports match them, including the `strict_cs` choice and the outlier removal. A cell running the ports and the MATLAB code side by side on one experiment would settle this.
- Whether 981_035's `PD` and `PD2` come from one rhythm. A cell printing the coincidence of their burst starts would settle it.
- How ControlTable's Deg_11, Deg_21 and Q10 values were computed. The script's code for them, printed, would settle it.
- The Ih step timing. A plot or printout of V and I across the whole step for one cell would settle it.
- Which channels Raw_Expt_969_147.mat and Raw_Expt_969_087.mat hold. Their `nerve_names` would settle it.
