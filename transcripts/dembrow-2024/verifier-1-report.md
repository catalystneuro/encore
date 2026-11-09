**Verifier report, round 1: Dembrow, Sawchuk et al. 2024 on DANDI:001065 (0.241028.1559)**

The claims file has 42 claims: 41 from the paper plus the link claim `link-cells`. The DANDI API shows the dataset holds only 294 icephys NWB files from 57 subject folders. There are no transcriptomic files and no morphology files.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| link-cells | reproduced | Cells 6 and 9: all 294 files match a table row. Donor agrees for 293 of 294 and species for 292 of 294, both ≥99%. Median Spearman is 0.952, at least 0.9. All 68 cells of the 4 nA series were found. |
| cohort-animals | reproduced | Cell 12: 57 animals (58 ± 5.8), 22 M (23 ± 2.3), 34 F (35 ± 3.5), 48 nemestrina, 9 mulatta (10 ± 1). The mulatta count depends on subject Q19.01.001: the file says mulatta, the table says nemestrina (cell 6). If the table is right, the count is 8, outside tolerance. |
| cohort-recordings | reproduced | Cell 14: 294 files, inside reading (b) (300 ± 30) but outside reading (a). This only counts files; nothing shows the 294 are the 300 new cells, and 35 of the 47 table cells not in the dataset are Nikolai's. |
| patchseq-qc-177 | blocked (data_missing) | The archive has no Patch-seq reads or mapping. The only other source is the paper's own QC calls in cell_list_L5.csv, and counting those would just repeat the paper's labels. |
| cs-map-to-l5et | blocked (data_missing) | Same reason as patchseq-qc-177. |
| fig3a-cs-with-l5et | not_reproduced | Cell 18: reading (a) holds for 48 of 52 CS cells, but it needs all 52. Reading (b) holds for 18 of 52 (0.346), and it needs at least 0.9. Both readings fail. |
| fig3e-classifier-accuracy | reproduced (marginal) | Cell 20: stratified f1 gives [95.2, 79.2, 75.7, 99.5, 91.7], and all five are within tolerance. The 50% value passes by 0.09 points (lower bound 79.11). Unstratified runs fail at 50%. |
| fig3-spc-classifier | reproduced | Cell 22: all 5 scores are within 10 points under every reading. |
| fig3h-projection-largest-effect | reproduced | Cell 24: median partial η² is 0.067 for projection, 0.021 for preparation and 0.008 for area. The code's formula gives the same order. |
| fig4a-top-subthreshold | not_reproduced | Cell 26: the top three are min_dvdt, min_dvdt_short and MaxZ. Cutoff ranks 8th, Fr 9th, and MaxRn/SSRn are outside the top 10. See problem 2. |
| fig4c-et-higher-resonance | reproduced | Cell 29: BH p = 4e-14, and L5 ET is higher in both areas and both preparations. n is 132/162 against the paper's 147/177. |
| fig4e-et-lower-rin | reproduced | Cell 31: BH p = 2.3e-7, and L5 ET is lower in all four groups. |
| fig4g-et-faster-spikes | reproduced | Cell 33: all three features are significant in the stated direction, and min dV/dt is faster in every group. |
| fig4-interaction-small | not_reproduced | Cell 37: reading (a) fails because the max_ifreq_gain interaction (η² 0.080) exceeds the median projection effect (0.067). Reading (b) fails for 4 of 15 features. |
| species-no-effect | not_reproduced (unreliable) | Cell 39: 11 features (projection-class reading) and 1 feature (rmp, subclass reading) have BH species p < 0.05. Both readings fail. The four-way models are probably rank-deficient (problem 1). |
| tcx-et-types-no-difference | reproduced | Cell 41: no feature reaches BH p < 0.05 under the Welch test (smallest 0.060) or the ANOVA (smallest 0.133). Largest \|d\| is 1.06. n is 21/17 against the paper's 25/19. |
| fig4h-patchseq-genes-et | blocked (data_missing) | Needs the SRA reads; the archive has none. |
| patchseq-genes-area | blocked (data_missing) | Same: SRA reads not in the archive. |
| fig1-snrna-genes-et | blocked (data_missing) | Needs the NeMO references; not in the archive. |
| fig1-snrna-genes-area | blocked (data_missing) | Same: NeMO references not in the archive. |
| fig5-tap-root-dendrites | reproduced (paper's feature table) | Cell 92: Euclidean MCx maximum is 1.39 mm, and every TCx value is below the MCx median. The input is the 19-cell RawFeatureWide.csv, not the reconstructions. |
| fig5b-dendrite-depth | blocked (data_missing) | The reconstructions are not in the dandiset. I could not check whether RawFeatureWide.csv holds per-layer lengths (section C). |
| fig5c-basal-apical-features | reproduced | Cell 94: max path distance, extent_x, apical branches and apical max branch order all have BH p < 0.05 in the stated direction. Two d values are outside tolerance (1.94 against 2.22; 2.11 against 1.55), but under the criterion d does not decide the outcome. Total length (another reading of "longer") is not significant. |
| fig5e-morph-classifier | partially_reproduced | Cell 96: stratified gives 100 / 80.3 / 71.5. The 100% and 75%-held-out values are within tolerance; the 50% value is below 82.7. The criterion gives no rule for a partial outcome; this is my call. |
| fig6a-area-variation | reproduced | Cell 45: 16 of 39 features have BH p < 0.05, with subthreshold and suprathreshold features among them (the code's table had 19). |
| fig6b-mcx-higher-resonance | reproduced | Cell 47: Fr BH p 0.013 and cutoff BH p 0.0026, both higher in MCx. |
| fig6d-mcx-deeper-fahp-symmetric | reproduced | Cell 49: fAHP (6.9e-5), up/down ratio (0.0013), AP_HW (0.035) and min_dvdt (0.048) are all in the stated direction. |
| figs6b-mcx-lower-rin | reproduced (fragile) | Cell 51: SSRn BH p 0.037 with MCx lower. Within culture the gap is small (26.6 against 28.9 MΩ). SSRn has broken values (problem 3). |
| figs6b-mcx-higher-rheobase | not_reproduced | Cell 53: BH p 0.16 (uncorrected 0.08), though MCx is higher (268 against 193 pA). |
| figs6b-avg-gain-no-difference | reproduced | Cell 55: BH p 0.59. |
| fig6h-tcx-steeper-instantaneous-fi | reproduced | Cell 57: BH p 0.036 (initial) and 0.0019 (maximum), both TCx higher. The initial-slope feature agrees poorly with the table (ρ 0.47; problem 6). |
| figs6c-mcx-higher-max-rate | reproduced | Cell 64: p 1.5e-4, d 1.04 (1.0 ± 0.1). |
| figs6d-equal-max-instantaneous | reproduced | Cell 66: p 0.62. |
| fig6-depolarization-block | partially_reproduced | Cell 68: both readings give MCx 5/42 and TCx 17/26. Both counts are outside tolerance, but the TCx proportion exceeds the MCx one. |
| fig6j-spike-width-ratio | not_reproduced | Cell 71: MCx 1.24 (needs 1.5 ± 0.15), TCx 1.55 (needs > 2), \|d\| 1.28 (needs 2.02 ± 0.2). Only the direction and the p value hold. |
| fig6k-upstroke-ratio | reproduced | Cell 73, reading (a): MCx 0.498, TCx 0.198, d 1.79 (1.69 ± 0.169), p 2.5e-11. All within tolerance. |
| figs7-cv-isi-higher-mcx | partially_reproduced | Cell 77: area p is 0.010 or 0.017, with MCx higher, under both bin widths. p is below 0.05 but not below 0.001. |
| fig7-oscillation-frequency-vm | partially_reproduced | Cell 80: MCx is positive with p < 0.001 for both measures. TCx FFT has p 0.24, but TCx autocorrelation has p 0.028 (r −0.32), which fails "p ≥ 0.05". The criterion has no partial clause; partial is my call. FFT MCx r² is 0.27, outside 0.32 ± 0.032. The spline step was not done (problem 4). |
| fig7k-oscillation-power-vm | not_reproduced | Cell 82: MCx r = 0.057, p = 0.63. The strength measure is the author's own and has no spline (problem 4). |
| figs7-oscillations-with-blockers | partially_reproduced | Cell 84: oscillations are present with blockers (42 cells), and the mean is lower (5.43 against 5.58 Hz), but p is 0.72 or 0.82. |
| fig7l-firing-tracks-oscillation | partially_reproduced | Cell 86: MCx p < 1e-27 but r² 0.44–0.45 (needs 0.63 ± 0.063). TCx p is 0.22 or 0.13. |
| figs7g-modal-rates-long-isis | reproduced (narrow) | Cell 88: holds only for sweeps with 1–200 spikes and 1 Hz bins (MCx 30.5, TCx 8.5). With 2 Hz bins TCx is 9.0 (> 8.8); with all sweeps it is 147.5 / 99.5. Limiting to 1–200 spikes is the author's assumption, but a reasonable one: the paper ties the 650 ms window to the oscillation analysis, which it restricts to ≤ 200 spikes. |

### B. Problems

1. **[affects a conclusion]** species-no-effect (cell 39, `d.anova`): four-way OLS with all interactions and type II sums of squares. The subclass reading has 7 levels, one of them with 1 cell, and species is likely confounded with area or preparation. Cell 1 suppresses the rank-deficiency warnings, and the notebook never shows the species × area × preparation × subclass cell counts. On a synthetic rank-deficient design, statsmodels returned zero sums of squares for main effects. The 11-against-1 split between readings also points to unstable models. The not_reproduced outcome is unreliable.
2. **[affects a conclusion]** fig4a (cell 26) and the extracted features (cell 9): parametric effect sizes are computed on features with outliers. MaxRn has Spearman 0.976 with the table but Pearson only 0.508 (maximum 2575 MΩ). Fr has Pearson 0.642 (maximum 38.8 Hz, at the 40 Hz edge), SSRn 0.268, sag_ratio 0.237. The low Fr and MaxRn ranking may be an extraction artefact, and the notebook never ranks the table's values for the same cells to separate the two explanations.
3. **[affects a conclusion, possibly]** `vi_features`: SSRn goes as low as −460.7 MΩ, and sag_ratio and rebound take negative values (cell 7). That is physically wrong, and nothing checks or excludes it. It bears on figs6b-mcx-lower-rin, where the culture difference is only 2.3 MΩ, and on fig4a.
4. **[affects a conclusion]** `oscillation_segments` and cells 75 and 80–86: the claim criterion and the STAR Methods call for a smoothing spline over segments to get each sweep's peak frequency and strength. The notebook does not fit it. Instead it uses per-segment FFT peaks, averaged per 5 mV bin (fig7, fig7k) or per sweep (`osc_f`, fig7l and the blockers claim). The strength measure (Hann-window peak amplitude in mV) is the author's own and is not stated as replacing the spline. The fig7k not_reproduced outcome and the r² shortfalls rest on this. 10.6% of FFT peaks sit at the 3 Hz band edge.
5. **[affects a conclusion]** fig6j (cell 71): the width ratios are far from the code's (MCx 1.24 against 1.53, TCx 1.55 against 2.27), while the upstroke ratios match closely. That points to a difference in how threshold or half-width is defined for late spikes, such as 20 V/s against a fraction of the upstroke. Only one definition is run.
6. **[does not affect a conclusion]** `fi_features`: initial_gain and initial_ifreq_gain agree poorly with the table (ρ 0.63 and 0.47), and so does i_max_gain (ρ 0.33). When the first step already fires, the slope is taken from 0 pA, which is the author's own choice, though it is stated. The fig6h direction holds, but the TCx mean of 0.575 differs from the code's 0.28.
7. **[does not affect a conclusion]** In figs7-cv and the blockers claim (`shared_bins`, cells 77 and 84), sweeps in bins that lack both groups are dropped (43, 36, 11 and 8 sweeps), because the model has all interactions. This is an unstated departure; an additive model would keep them.
8. **[does not affect a conclusion]** In the blockers claim (cell 75), blocker status comes per cell from the Zenodo table's `drug` column (substring "dnqx"), not from the recording metadata the criterion names. Sweeps recorded before wash-in would be labelled as with blockers.
9. **[does not affect a conclusion]** The morphology claims (cells 90–96) re-run the statistics on the paper's derived RawFeatureWide.csv: 19 cells, against 23 in the paper. That is not an independent reproduction from the data. For fig5-tap-root, the "including CS neurons" and "more complex apical tufts" parts are not checked.
10. **[does not affect a conclusion]** Preprocessing (`preprocess`, cells 16 and 96) imputes and z-scores on all cells before the classifier splits. This is a mild train/test leak, but it matches the paper's procedure.
11. **[does not affect a conclusion]** zap_tau is dropped, so 39 features are used instead of 40. This is stated, and it changes the BH denominators only slightly.
12. **[does not affect a conclusion]** In cell 61, five cells have 200 pA series with commands up to 16 nA, beyond the 4 nA headstage limit. Steps above 4 nA are silently excluded, and the commands are not investigated.

### C. What I could not check

- **species-no-effect:** a crosstab of species × area × preparation × subclass, plus the model rank and condition number, would show whether the four-way models are estimable.
- **fig4a, fig4-interaction-small, figs6b-mcx-higher-rheobase:** the same ANOVAs run on the table's feature values for the same 294 or 132 cells. This would show whether failures come from feature extraction or from the cell subset.
- **SSRn and Fr:** the count of cells with SSRn ≤ 0 or Fr > 30 Hz, by class and area, and the results with those cells excluded.
- **fig6j:** per-cell width ratios against the pickles' values, if MCx.pkl and TCx.pkl hold them.
- **fig7k and fig7-oscillation-frequency-vm:** a version with the sweep-level smoothing spline, and a plot of spectra for example segments.
- **Blockers claim:** the value counts of the `drug` column, and whether the NWB files record drug wash-in per sweep.
- **fig5b-dendrite-depth:** the RawFeatureWide.csv column list (the notebook prints only "45 features"). It would settle whether per-layer dendrite lengths exist, which would make fig5b partly testable.
- **cohort-animals:** which source is right on the species of subject Q19.01.001 (file says M. mulatta, table says M. nemestrina).
- Feature extraction itself: I did not re-run it. On synthetic spikes, `detect_spikes` returns the correct half-width and max dV/dt, and `cohen_d` and the partial η² in `anova` are correct.
