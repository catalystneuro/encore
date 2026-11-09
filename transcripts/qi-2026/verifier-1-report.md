**Verifier report, round 1: Qi et al. 2026, DANDI:001960 v0.261013.2016**

The claims file has 56 claims. The attempt tests 45 and blocks 11, across three notebooks (`qi2026_excitability_connectivity` = EC, `qi2026_spontaneous` = SP, `qi2026_excitability_spontaneous` = ES). My outcomes: 31 reproduced, 7 partially reproduced, 5 not reproduced, 13 blocked.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| jf608-brighter | blocked (data_missing) | The archive API lists 7 assets (3 sessions × 2 mice plus a raw excerpt). There is no JF585/JF608 comparison. |
| targeting-signal-to-background | blocked (data_missing) | There are no wide-field and targeted images of the same field. The excerpt is a targeted-illumination movie. |
| spike-snr-and-detection-errors | not_reproduced | SNR (1/noise) is 3.18–3.45 under every reading (SP cell 6), below 4.5 ± 0.7. The Methods' definition (s.d. of the 1-frame difference, no √2) matches the notebook's. The false-discovery and false-negative rates were not computed. |
| snr-decay-one-hour | reproduced | Mean of ratios is 72.9% (QC) and 77.3% (all); ratio of means is 69.8% and 73.4%. All are within 76 ± 13 (SP cell 8). |
| fig1d-stimulation-fold-change | blocked (data_missing) | No 76-cell periodic-stimulation session in the asset list. |
| off-target-length-constants | blocked (data_missing) | No lattice experiment. |
| l1-sampling-density | blocked (data_missing) | No z-stack, only a GFP maximum projection. |
| adaptation-vadp-correlation | reproduced | Reading (a): R = 0.232, p = 4.5e-8, n = 543 (EC cell 13). |
| fig2c-three-bins | reproduced | Cluster sizes are exactly {94, 110, 116} (EC cell 15). |
| fig2gk-bin-profiles | reproduced | 8 of 8 orderings hold under both readings (EC cell 17). |
| two-mice-intrinsic-distributions | blocked (methods_underspecified) | The named readings disagree: all cells give 4/5 (time constant p = 0.101), QC cells give 5/5 (time-constant p = 0.048). The header rule therefore blocks it. See problem 5. |
| synaptic-connection-counts | reproduced | 802/7280 and 667/7032 in 60–400 µm (828/7426 and 679/7150 within 400 µm). Per cell: 2.62 out, 25.3 tested, 10.8% (EC cell 21). |
| ipsp-median-amplitude | partially_reproduced | The pooled median IPSP of −0.0297 is within tolerance. The cross-STA fluctuation averages 0.234 (0.217 and 0.250 per mouse) against 0.20 ± 0.02 (EC cell 23). |
| detection-limits | blocked (other) | Blocked as methods_underspecified, but the claims file gives readings. What is missing is the per-pair statistic or null, which could be rebuilt from stored data (problem 3). |
| gap-junction-connection-counts | reproduced | 3553 and 2199; 9.99 out, 9.99 in, 40.9%; median spikelet 0.0120 (EC cell 25). |
| hadamard-stimulation-rates | reproduced | 26.5 Hz on, 3.6 Hz off, 12,929 evoked spikes. There are 650 stimuli if "stimuli" means 750 ms on-steps (the Methods' step); 360 if it means on-blocks (EC cell 27). |
| spikelet-not-scatter | blocked (too_large) | The excerpt is 356.8 GB (API), but a subset of frames would allow a partial test (problem 10). |
| highmag-footprint | blocked (data_missing) | No 7.5× recordings. |
| lasso-off-target-correction | blocked (other) | The stated block reason is wrong: 1755 = 955 + 800 stored synaptic flags, the penalty readings are in the claims file, and per-trial responses can be derived from the stored data (problem 2). |
| connection-distance-structure | partially_reproduced | Probabilities 23.5% and 83.0% match; gap-junction λ under (b) is 156–161 µm. Synaptic λ is 151–362 µm under every reading against 105, and M-YQ0201-29 out-degree fits a power law better (EC cell 30). |
| fig3eg-amplitude-falls-with-distance | reproduced | Nearest bin median exceeds farthest for both measures in both mice; Spearman ρ < 0, p ≪ 0.05 (EC cell 32). |
| fig3h-conduction-speed | reproduced | Pooled 0.265 m/s, within 0.28 ± 0.028 (EC cell 34). |
| amplitudes-log-normal | not_reproduced | Spikelet log-skew is 0.73, above 0.5 (EC cell 36). The selection deviates from the claims file, so this is provisional (problem 4). |
| interaction-kernel | not_reproduced | Peak 33.0 ms is in range, but the decay of 39.4 or 47.9 ms, FWHM 22.7 ms and λ of 72 or 96 µm are all outside tolerance (EC cell 38). |
| fig3jk-presynaptic-sets-amplitude | reproduced | R = 0.609 and 0.263, n = 497 and 482: exact (EC cell 40). |
| fig3mn-postsynaptic-sets-decay | reproduced | Incoming R = 0.330 (p = 4.7e-18); outgoing R = 0.075, p = 0.056 (EC cell 40). |
| fig3lo-variance-components | reproduced (fragile) | Amplitude pre > post in 100%; decay post > pre in 99.95% of converged refits. Non-converged refits were excluded (problem 6). |
| gap-junction-no-identity-effect | not_reproduced | R = 0.214, 0.298, 0.268, 0.314; three of four are ≥ 0.26 (EC cell 44). |
| subthreshold-correlation-length | reproduced | 0.638 / 0.518; 2.42 / 4.03 mm (SP cell 10). |
| subthreshold-low-dimensional | reproduced | Reading (a), averaged: 70.7% quiet, 67.5% whisking, quiet > whisking (SP cell 12). |
| quiet-state-oscillations | reproduced | Quiet/whisking 1–10 Hz power ratio is 4.94 and 2.92 (SP cell 14). |
| traveling-waves | blocked (other) | No analysis was run although the data and a Methods procedure exist (problem 1). |
| spike-synchrony-localized | partially_reproduced | Reading (a): 277.1 and 270.7 µm, half-width 2.54 ms. FWHM averaged over mice is 71.1 ms against 80 ± 8 (M-YQ0201-27 alone, 78.7, would pass) (SP cell 17). |
| voltage-to-spike-sigmoid | reproduced (marginal) | At the spike frame, 52% of cells have R² ≥ 0.9 and both CVs are > 0.2 (SP cell 19). The Methods (V(t_s)) and the code agree on this reading; the −8-frame variant fails at 24%. |
| fig4g-private-depolarizations | reproduced | Slope ratio 2.89 pooled (SP cell 21). |
| fig4hi-self-sta-diverges | reproduced | Increase 0.176 and 0.182 against s.d. 0.015 and 0.007; self above cross at −30 ms (SP cell 23). |
| fig5a-rheobase-predicts-spontaneous-excitability | reproduced | ρ = −1.00 in both conditions for M-YQ0201-27 code bins (ES cell 5). |
| supp22-rheobase-correlations | reproduced | Reading (a): R = −0.573 and −0.311, n = 543 (ES cell 7). |
| fig5b-adaptation-dvdt | reproduced | R = 0.274 (Methods reading) and 0.262 (code reading); M-YQ0201-27 top bin is highest (ES cell 9). |
| fig5c-adp-bursting | reproduced | Main reading R = 0.546 (ES cell 11). |
| fig5e-inhibition-in-spontaneous-voltage | partially_reproduced | Under (c), −0.0213 and −0.0095 with p ≪ 0.05. The controls' +1% rise is not matched: control medians are 0.003–0.008, means 0.012–0.019 (EC cell 46). |
| fig5e-inhibition-in-spontaneous-rate | partially_reproduced | Under (a), rates are 0.190 and 0.083 Hz, but spikes lost fail under every reading (EC cell 46). |
| fig5g-gap-junction-synchrony | partially_reproduced | Under (a), 0.80 and 0.29 Hz, but spikes gained (0.0022 and 0.0009) fail (EC cell 46). |
| inhibition-gap-balance | blocked (methods_underspecified) | Readings give ratios of 6.96, inf, 1.37 and −0.19 (EC cell 48); reading (c) gives about 1.96. Its inputs did not reproduce. |
| npy-fraction-and-similarity | reproduced | NPY+ counts are within tolerance in every session; SNR and rate similar; KS p ≥ 0.08 (SP cell 25). |
| npy-intrinsic-differences | reproduced | 5 of 5 at p ≤ 0.001 (EC cell 51). |
| npy-classifier | reproduced | 76.8% against chance 50.0% (paper: 78% against 50% [46, 55]; the notebook's chance CI is [42.2, 57.5]). V_adp is top under both readings (EC cell 53). |
| npy-connection-probability | reproduced | 13.7% against 7.4%, n = 307 and 269, p = 1.4e-9 (EC cell 55). |
| npy-ipsp-amplitude | reproduced | −0.0372 (977 pairs) against −0.0311 (490 pairs), p = 8e-7: counts exact (EC cell 55). |
| npy-ipsp-duration | reproduced (fragile) | QC 60–400 µm: 77.4 against 65.2 ms, n = 760 and 709, p = 3e-13. The NPY− count is just inside 646 ± 65 (problem 13). |
| npy-gap-junction-no-difference | not_reproduced | Consistent-direction outgoing effects in probability and spikelet amplitude, and incoming effects in amplitude (EC cell 57). |
| npy-subthreshold-similar | reproduced | M-YQ0201-29: R = 0.973, slope 0.933 or 1.015 (SP cell 27). |
| npy-umap-groups | reproduced | Medians over seeds 158.5/205 and 201/300; Fisher p ~1e-23 (SP cell 29). |
| npy-whisking-onset-rates | reproduced | NPY+ 1.06 → 2.20 Hz (p = 6e-8); NPY− 1.27 → 1.50 Hz (p = 0.76) (SP cell 31). |
| npy-oscillation-peak-rates | blocked (methods_underspecified) | Reading (b) passes. Reading (a) fails because the voltage differs (p = 0.022) (SP cell 33). |
| npy-state-dependent-excitability | reproduced | All four comparisons hold at p ≤ 0.05 (SP cell 35). |

### B. Problems

1. **[affects a conclusion]** SP cell 15, traveling-waves: blocked with no analysis run. The voltage, coordinates and masks are already in memory, and the Methods give events, the speed slope and the phase-gradient direction. The open details should have been run under the readings the paper allows.
2. **[affects a conclusion]** EC cell 28, lasso-off-target-correction: the block reason is factually wrong. 1755 equals the total stored synaptic flags (955 + 800, EC cell 6). The claims file gives the penalty readings. Per-trial evoked spikes and IPSP responses can be derived from `spike_times`, `blue_stimulation_per_cell` and `normalized_voltage`.
3. **[affects a conclusion]** EC cell 28, detection-limits: the notebook never lists the full contents of `analysis/pairwise_connectivity_metrics`, so whether per-pair statistics are stored is unchecked. The null (pulses aimed at cells more than 800 µm away) could be rebuilt from stored data for the ~200 pairs near the cutoff.
4. **[affects a conclusion]** EC cell 36, amplitudes-log-normal: it uses all stored flags (7443 spikelet pairs, including non-QC cells and pairs under 60 µm). The header requires QC cells and drops pairs under 60 µm from gap-junction analyses (5752 pairs). The excluded close pairs are the scatter-contaminated largest ones, and the log-skew of 0.73 is near the 0.5 cut.
5. **[affects a conclusion]** EC cells 5 and 19, two-mice-intrinsic-distributions: M-YQ0201-27 has 7 membrane time constants of exactly 0 (EC cell 5), which look like failed fits. They are kept as values in reading (a), where the time-constant p = 0.101; treating them as missing may make the two readings agree.
6. **[affects a conclusion]** EC cell 42 / `bootstrap_variances`, fig3lo-variance-components: the fractions count converged refits only (1971 and 1969 of 2000). For decay, 1 of 1969 already has pre > post, and the 99.9% threshold allows at most 2 of 2000. Two adverse non-converged refits out of 31 would flip it, and their variances are not shown.
7. **[affects a conclusion]** SP cell 5, spike-snr-and-detection-errors: it says the matched-filter output and mixture fit are not stored. The raw-excerpt asset's DANDI metadata says it holds "the demixing and spike-finding products"; the excerpt's contents were not checked for them.
8. **[affects a conclusion]** SP cell 19, voltage-to-spike-sigmoid: the pass is marginal (262 of 505 cells). The caption variant is implemented as one sample 8 frames before the spike, not the caption's "10 ms interval". The fitted maxima have CV 4.54, which means the tops are unconstrained extrapolations that pass the CV test by default.
9. **[affects a conclusion]** EC cell 46, fig5e-inhibition-in-spontaneous-voltage: the controls' rise is never measured on the control-average waveform (`vsupp(cavg)`). Only medians and means of per-control values are printed.
10. **[affects a conclusion]** EC cell 28, spikelet-not-scatter: "too_large" assumes the whole 357 GB movie must be read. A subset of blocks or frames (at the measured ~45 MB/s, one block of ~90 GB) would give a scatter STA for a partial test.
11. **[does not affect a conclusion]** EC cell 38, interaction-kernel: the FWHM baseline is the median of lags outside ±40 frames on a trace with a slow hump, which gives 22.7 ms. The decay and λ fail anyway.
12. **[does not affect a conclusion]** EC cell 53, npy-classifier: features are z-scored on all cells before the train/test split (mild leakage).
13. **[affects a conclusion]** EC cell 55, npy-ipsp-duration: the header-consistent selection (QC cells, all flags within 400 µm, no 60 µm cut) was not run. It adds ~38 pairs and would likely push NPY− above 711. Means include fits capped at 0.4 s. No selection reproduces 699/646.
14. **[does not affect a conclusion]** SP cell 17, spike-synchrony-localized: averaging FWHM over mice is an unstated aggregation choice. M-YQ0201-27 alone meets all four values.
15. **[does not affect a conclusion]** Claims-file misreadings, reported not corrected:
    - voltage-to-spike-sigmoid says "the Methods/caption say V in the 10 ms before spikes". The Methods say V(t_s), the voltage at spike times; only the Results and the Fig. 4E caption say "10 ms".
    - fig5e-inhibition-in-spontaneous-voltage's criterion requires "both values" while its expected values list three quantities.
    - lasso-off-target-correction says the 1755 pairs are not given; they are the stored flags.
    - synaptic-connection-counts and npy-ipsp-amplitude cite "800" connections for M-YQ0201-27 in the 60–400 µm band. The data have 802 flags there, 800 of them with a finite amplitude.
16. **[does not affect a conclusion]** Helpers checked on synthetic inputs, all correct: `matlab_prctile` (9.5, 1, 3), both exponential fits (λ = 105 recovered), `spike_frames`, `chunk_guard`, and `CrossedLMM` (true 0.15/0.05/0.14, fitted 0.168/0.048/0.145). The speed-fit grid being absolute rather than peak-relative makes no difference for delays of 0–2.6 frames. The cubic over −2 to +4 frames has a sub-frame bias of up to −0.4 frames, which comes from the code's method.

### C. Could not check

- Any number against the data itself; I did not stream the files.
- Whether `analysis/pairwise_connectivity_metrics` and the raw excerpt hold per-pair p-values, nulls, matched-filter traces or mixture fits. A cell listing all their HDF5 datasets would settle problems 3 and 7.
- Problem 6: the share of pre > post (and post > pre) over all 2000 refits, non-converged ones included.
- Problem 5: two-mice-intrinsic-distributions rerun with time constant = 0 treated as missing.
- Problem 4: amplitudes-log-normal on QC pairs in 60–400 µm.
- Problem 13: npy-ipsp-duration on QC pairs within 400 µm, and with the fig3mn time-constant mask.
- Problem 9: `vsupp` of the weighted control average.
- The raw excerpt's HDF5 chunk layout and a timing for one block, to judge whether a subset test of spikelet-not-scatter is feasible.
- A run of traveling-waves under the Methods procedure with its open parameters varied.
