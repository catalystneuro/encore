**A. Outcomes**

The claims file has 21 claims. The notebook tests 12 of them and treats 9 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 11 matches exactly under both silence readings: 305 natural probes in 39 cells, and 93 MGB probes in 14 cells. The total of A1 cells meeting the criterion is 132 (124 with exclusions), not 123, against a tolerance of 0. The voltage-clamp counts (29 probes, 14 cells) cannot be tested because those recordings are not in the dataset. |
| a1-mgb-firing-rates | partially_reproduced | Cell 13: no reading has both means within 10% (0 of 6 for A1, 0 of 6 for MGB). The partial rule is met: A1 means are below 1 Hz in every reading, and the MGB evoked mean is 8.98 to 12.9 Hz at the 20× and 40× robust-SD thresholds. Under the authors' own automatic rule in GetSpikes.m it is 4.99 Hz, which fails the rule (problem 2). |
| fig2-example-reliability | reproduced | Reading (a), averaged over cells, gives 0.310 ± 0.092 (n = 39) against 0.31 ± 0.09; averaged over probes it gives 0.319. The example values (0.611 and 0.737) also match, but they are circular because those same values were used to pick the cell. |
| fig2-example-long-context | reproduced | The matched probe is 20051222-ha1-001 probe 4. It has significant periods before 2 s and from 3.97 s on, and none between 2 and 3.6 s. The strict reading (none between 2 and 4 s) fails by a 30 ms overlap at 3.97 to 4.008 s. |
| fig3a-proportion-significant | reproduced | One reading passes all three tests: silence counted, all 305 probes in the denominator. It gives 186 significant probes (204 ± 20.4), a fraction of 0.610 (0.669 ± 0.067) and a late fraction of 0.252 (0.237 ± 0.024). The other three readings fail. |
| fig3a-significance-decay | partially_reproduced | Cell 21: with sizes free in sign, the fit finds a negative 15-ms term, so no reading reproduces. With sizes bounded at zero, two exponentials are selected and τ2 is 0.97 to 1.08 s. In every row τ1 (0.25 to 0.27 s, expected 0.20 ± 0.02) and α2 (0.068 to 0.080, expected 0.09 ± 0.009) are out of tolerance. |
| fig3b-fractional-power-decay | not_reproduced | α1 is 0.445 to 0.468, within tolerance. τ1 is 1.29 to 1.78 s in all 8 readings, against 1.04 ± 0.104. |
| timescale-longer-than-membrane | reproduced | The 1/e lags are 0.071 s (noise), 0.075 s (spontaneous) and 0.073 s (spontaneous without the first 1 s). The 0.1 lags are 0.114 to 0.120 s. All are under 150 ms and under 1.04/3 s. |
| fig4-predictability-upper-bound | not_reproduced | Smoothed denominator: 1+α1 is 0.43 to 0.72 and τ1 is 1.66 to 100 s (two fits stop at the bound). Unsmoothed: 1+α1 is 0.50 to 0.54, within tolerance, but τ1 is 1.46 to 1.92 s. |
| fig4-strf-performance-low | blocked (other: not attempted) | The notebook gives "time" as the reason, which is not a blocking reason. The archive has the data: crcns-ac1.zip holds `wehr/Results` with 25 recording folders, `wehr/Summary.mat`, `STRFanalysis.m` and `ridgesvd1.m`. |
| fig5-example-conductances | blocked (data_missing) | Confirmed from the archive. All 346 result files are mV current-clamp or cell-attached traces (cell 3). ReadMe.txt and Methods.txt say "current-clamp mode" with a K-gluconate internal solution (no QX-314 or BAPTA). No experiment in Summary.mat is voltage clamp. |
| fig6-conductance-decay | blocked (data_missing) | Same evidence as fig5. No part of the claim can be tested. |
| fig7-example-frequency-context | blocked (other: not attempted) | Testable. Experiment 2 includes 6 files of a natural sound probe after synthetic variants, and DMR files. |
| fig8a-proportion-by-property | blocked (other: not attempted) | Testable. All 105 synthetic files load and are already cut into probe sets (cell 11). Only the map from stimulus to varied property is missing; part of it is in the file notes. |
| fig8b-decay-by-property | blocked (other: not attempted) | Same as fig8a. |
| fig8a-significance-fits | blocked (other: not attempted) | Same as fig8a. |
| fig8c-relative-effects | blocked (other: not attempted) | Same as fig8a. |
| fig8-natural-synthetic-probes-alike | blocked (other: not attempted) | Same as fig8a. |
| fig9-mgb-fast-decay | reproduced | τ1 is 0.057 to 0.083 s in all 12 readings. The mean after 0.5 s is within 25% of the fitted κ in every reading, and within 25% of the paper's 2.0 only for the 20×SD threshold averaged over running probes (1.69). The sizes and κ mostly fall outside the paper's values; the criterion reports them but does not use them. |
| fig9-example-first-bin | reproduced | At every threshold, 4 of the 12 probes with the Figure 2 design meet the factor-of-two rule, all in cell 20071010-ha2-003. Over all probes it is 35 to 46 of 93. |
| figs1-silence-probe | reproduced | 19 of 38 cells have a significant period starting within 0.5 s of silence onset. Eq. 17 power falls below 10% of its onset value at 0.72 s (Eq. 19 at 0.46 s). |

**B. Problems**

1. [affects a conclusion] Blocked claims section and the summary table in cell 0. Seven claims are marked blocked for "time": the STRF claim, fig7 and the five fig8 claims. The archive holds the data for all of them, so their outcomes are undetermined, not blocked.
2. [affects a conclusion] a1-mgb-firing-rates (cell 13, `spikes_whole_cell`, `analyse_mgb_file`).
   - A1 rates use only the 39 natural-sound cells (`NAT`), although 95 more synthetic-ensemble current-clamp cells are loaded (`SYN`) and the paper's 194 cells span all ensembles.
   - Both spike detectors are the notebook author's own choices and are never checked (no waveforms, no ISI or refractory check). On the A1 side these are the 5, 10 and 20 mV excursions above the median-clipped trace; on the MGB side, the 20× and 40× robust-SD thresholds.
   - The partial outcome rests on the 20× and 40× thresholds. With GetSpikes.m's own rule the MGB evoked mean is 4.99 Hz, which fails the partial rule.
3. [does not affect a conclusion] methods-recording-counts (cell 11).
   - The criterion asks for cell counts per ensemble (TORC 14, DMR 6, MHT 39, MCN 27), the Table 1 rows, and the probes behind any count that differs. The notebook gives only totals by file description (132, or 124).
   - `probes_m4_nosil` is computed but never printed.
   - The outcome stays partial in any case, since the voltage-clamp counts cannot be tested.
4. [does not affect a conclusion] fig3a-proportion-significant (cell 19). The passing reading has a noise floor of 0.0022, outside the paper's 2.8e-3 ± 10%. The paper's chance level is matched only by the running-probes denominator (0.0028), and under that reading the late fraction (0.267) fails. The count match and the chance-level match come from different readings.
5. [does not affect a conclusion] fig4-predictability-upper-bound (cell 23).
   - The legend gives α1 = −0.49 and τ1 = 1.04 s, the same values as Fig. 3B, which suggests the plotted curve is 1 − Q. That reading was not run. Under it, 1+α1 would be 0.533 (within tolerance) and τ1 1.77 s (outside), so the outcome does not change.
   - The smoothed U is erratic: 176 points lie above 1.2, and two fits stop at the τ = 100 s bound. The notebook does not flag either.
6. [does not affect a conclusion] fig3a-significance-decay (cell 21). The proportion rises from about 0.18 to 0.27 over the first ~50 ms (plot in cell 19). With sizes free in sign, the fit spends a negative 15-ms term on that rise. Bounding the sizes at zero is a reasonable reading and is stated as one.
7. [does not affect a conclusion] figs1-silence-probe (cell 27). There is no chance comparison for "a significant period starting within 0.5 s", and the noise floor for silence probes is not printed. The criterion only needs one cell, and 19 of 38 cells pass.
8. [does not affect a conclusion] MGB clock check (cells 8 and 9). The trigger-alignment check fails for 3 files from 2 cells (20071012-ha1-002 and -003). They are kept in the fig9 analyses, and no run without them is shown.
9. [does not affect a conclusion] Helper checks on synthetic inputs.
   - `kw_significance` matches the p-values of `scipy.stats.kruskal` (largest difference 1.8e-7). It uses average ranks with no tie correction, which differs from CxtDep.m; the notebook states this.
   - `runs_at_least` keeps a 50-point run and drops 49- and 40-point runs.
   - `frac_power` is unbiased: 5.05 against an expected 5, and 4.04 against 4.
   - `running_mean_0_2t` agrees with a direct calculation.
   - `fit_exp_select` recovers 0.17, 0.20, 0.09 and 0.90.
   - `psth` drops spikes at exactly t = 0, which is trivial.
   - Eqs. 17, 18 and 42 in the helper match the paper.
10. [does not affect a conclusion] Claims file. I found no misreading of the paper. The 1 − Q reading for Fig. 4 is missing from fig4-predictability-upper-bound's list of open readings (problem 5).

**C. What I could not check, and the output that would have let me**

- Spike detection. Waveform overlays, ISI histograms and spike counts per file for each A1 and MGB detector, plus A1 rates over all 132 current-clamp cells.
- Why τ1 comes out long for fig3b and fig4. Q(t) at 2, 3 and 4 s, the fit residuals, and a fit with κ free. Q at 1 s is 0.191, close to the paper's curve value of 0.188, so the gap looks like it sits in the tail (about 0.1 at 3 to 4 s).
- Chance level for the silence probes. The noise floor and the expected number of cells with an early significant start under shuffling.
- fig9 run without the two cells that fail the clock check.
- The mapping of synthetic files to ensembles and Table 1 columns, which methods-recording-counts and all fig8 claims need.
- Recording types in Wehr's folders were not surveyed. This does not matter for fig5 and fig6, whose voltage-clamp cells are Asari's.
- How often tied values occur at a time point in the int16-quantised traces, which bears on the tie handling in `kw_significance`.
