**Verifier report, round 1: Hazon et al. 2022 on CRCNS hc-30 (29 claims in the claims file)**

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| data-sessions-and-neurons | reproduced | NB1 cell 10: 110 of 110 sessions meet the rule, 12 mice, 27,898 neurons, median 235, range 151 to 497. The >200 reading gives 73 large-data sessions from 10 mice. |
| single-cell-variability | reproduced | Cell 12: the SD reading gives 0.7263 +/- 0.6117, an exact match. The 40-class SNR mean is 0.437, inside 0.41 +/- 0.041; its spread of 0.464 is outside, but the criterion judges means only. |
| suppl-table1-place-field-properties | not_reproduced | Cell 14: taking the best reading for each quantity, only 2 of 7 are within 10%: running rate 0.362 and max rate 1.461 (cells with >100 events per 10 min). The other five are far off: out-of-field 0.15–0.25 vs 0.034, width 16–18 vs 37.8 cm, trial-by-trial variability ≤0.90 vs 1.2, spatial information 0.15 or 1.06–1.30 vs 0.24. |
| fig1d-noise-correlation-by-field-distance | reproduced | Cell 16: both directions pass. Distance 0 is 0.0386 / 0.0374, against means of 0.0064 / 0.0058 at distances ≥10. The shuffled curve is separated from the unshuffled one, with non-overlapping intervals, at distances 0 to 10, for both the session-mean and pooled-pair readings. |
| noise-correlation-not-physical-distance | blocked (data_missing) | I listed the bucket `hc-30/`. It holds only event_traces.mat, checksums.md5, filelist.txt and the descriptor files. The descriptor lists four fields (mouse_name, session_ID, traces, position) and no cell coordinates or footprints, so no part of this claim can be tested. |
| fig2d-rms-error-ensemble-vs-shuffled | reproduced | NB2 cell 8: medians are 9.36 cm for the ensemble (tolerance 9.38 ± 0.94) and 4.80 cm shuffled (tolerance 5.15 ± 0.52). The ensemble error is larger in 109 of 110 sessions. The shuffled IQR is 1.73 against 2.40, outside tolerance but not part of the criterion. |
| fig2cd-shuffle-better-in-all-bins | reproduced | NB2 cell 12: the ensemble error is worse in 20 of 20 positions and 40 of 40 classes, and the shuffled correct fraction is higher in 40 of 40 classes on the session average. Median misclassification is 1 bin. The largest error with at least 1% of misclassified samples is 5 bins, against the paper's "up to three" (reported only). |
| fig2ef-imse-saturates-with-correlations | reproduced | NB2 cell 14, 110 sessions: I0N has p = 3.5e-17 and N has p = 5.2e-15, shuffled higher in both, and shuffled I0N is higher in 12 of 12 animals. Fits are often degenerate: 7 unshuffled and 78 shuffled fits have N outside 0 to 1e6. For the shuffled data that fits "no apparent bound". |
| suppl7b-initial-slope-lower-with-correlations | reproduced | NB2 cell 16: p = 9.8e-16. Median I0 is 0.00010 unshuffled and 0.00019 shuffled, so I0 is lower with correlations. |
| saturation-ensemble-size | not_reproduced | NB2 cell 18: the 5% slope range is 105 to 3076 neurons under reading (a) and 105 to 4.9e6 under (b), against 346 to 1402. The author's cleaned variant gives 717 to 2487. No bound is within tolerance under any reading. |
| position-measurement-noise | reproduced | NB1 cell 18: mean 0.277 cm, min 0.118 cm, max 1.001 cm; all three are within tolerance. |
| fig3cd-signal-and-noise-growth | reproduced | NB1 cell 22: (1) the signal is identical by construction and was checked (bin means change by at most 7e-16). (2) The unshuffled noise slope is positive in the median session with line R² 0.983. (3) The median ratio of shuffled to unshuffled noise slope is 0.084, but only 72 of 110 sessions are below 0.1. |
| suppl10-asymptotic-snr-lower-with-correlations | reproduced | Cell 24: p = 8.8e-20, shuffled higher in 110 of 110 sessions and in 12 of 12 mouse medians. |
| fig3f-signal-slope-beginning-vs-end | reproduced, resting on the code's direction | Cell 28: the legend's direction (beginning greater) gives p = 1.0. The code's direction gives p = 1.1e-18, against the code's printed 2.19e-18. The signal slope increases over the run, opposite to the claim statement. |
| fig3g-noise-slope-decreases-over-run | reproduced | Cell 30: beginning greater, p = 1.9e-9 on 110 sessions and 1.2e-10 on 73. |
| fig3h-snr-higher-at-run-end | reproduced | Cell 32: beginning lower, p = 2.8e-26 on 110 sessions and 5.7e-21 on 73. Rightward-only runs also give p < 0.001. |
| fig4a-snr-along-noise-pcs-peaks-at-6 | partially_reproduced | Cell 34: the session-mean curve peaks at component 7, which the criterion counts as partial. The curve is flat there: 0.0719 at component 6, 0.0730 at 7, 0.0720 at 8. The first six components carry 0.36 of the 14 common components (median 0.10 over all components), so "small" holds. |
| fig4b-correlations-increase-noise-signal-overlap | reproduced | Cell 36: the overlap change is positive in 73 of 73 sessions and in 10 of 10 animal means, under both component readings and both matrix readings. |
| fig4c-overlap-predicts-asymptotic-snr | reproduced | Cell 38: r = -0.743, adjusted r² 0.496, p = 0.0139. This matches the code's printed -0.744, 0.498 and 0.0136. |
| fig5f-pf-width-variance-vs-nsv | reproduced | Cell 40: r = -0.658, p = 0.0385, against -0.65 ± 0.065. |
| fig5hi-nsv-predicts-noise-correlation-effect | reproduced | Cell 42, unfiltered: across animals r = 0.869 (p = 0.0011), across sessions r = 0.716 (p = 1e-12). The filtered reading gives the same result. |
| suppl-table2-nsv-best-predictor | reproduced | Cell 44: NSV has the highest adjusted R², 0.51 on all 73 sessions and 0.49 filtered; the next best is 0.19 / 0.23. NSV at a fixed 200 neurons gives p = 2.2e-5 across sessions. |
| pf-width-variance-not-predictive | reproduced, resting on the confidence-interval filter | Cell 46: unfiltered, the session-level test gives p = 0.041 (<0.05, so not reproduced). With the filter Supplementary Table 2 describes, p = 0.10 for sessions and 0.077 for animals. The amplitude variance correlates across animals (r = 0.75, p = 0.013), which goes against the text's "or amplitudes"; the criterion only asks for it to be shown. |
| suppl11b-i0-vs-single-cell-snr | partially_reproduced | NB2 cell 22: the main reading gives r = -0.07, p = 0.84, because Mouse2011's mean I0 is 23.7, set by one failed fit. Excluding failed fits and misaligned sessions gives r = 0.75, p = 0.0125: positive and p < 0.05, but not p < 0.01, and r² = 0.56 is outside 0.73 ± 0.073. |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | reproduced | NB2 cell 24, log10 reading: r = 0.894, r² = 0.80 (inside 0.88 ± 0.088), p = 4.8e-4. The linear reading fails (r = 0.04) because of degenerate fits. |
| suppl8-task-performance-and-accuracy | not_reproduced | NB2 cell 26: performance against trials gives r = 0.847, a match. Accuracy against trials (r = -0.05) and against performance (r = 0.19, p = 0.11) do not match the paper, and in the path model trials is significant (p = 3.5e-4). |
| suppl6-twenty-bins-near-optimal | reproduced | NB2 cell 28: 11.84 cm with 20 bins and 11.94 cm with 30, both within tolerance. No bin count is more than one SEM below 20 bins. This rests on only 2 repetitions per session. |
| fig5cd-synthetic-narrow-widths-broader-nsv | reproduced, resting on the legend reading | NB1 cell 48: under the legend's uniform widths, narrow gives the higher NSV at 50 cells and up to 10,000. Under the Methods' log-normal widths the result reverses (0.0030 < 0.0044). |
| suppl9-fit-recovers-saturation | reproduced | NB2 cell 30: N = 704 ± 554 (500 neurons) and 338 ± 87 (2000 neurons); the intervals overlap. This is a weak test because the 500-neuron interval is about ±80%. |

Tally: 23 reproduced (3 of them resting on one reading), 2 partially reproduced, 3 not reproduced, 1 blocked.

### B. Problems

1. [affects a conclusion] NB2 cell 1 and `decode_series`: 4 neuron subsets per size (paper 80) on a 1, 25, 50… grid (paper 1, 10, 20…). Fits are unstable as a result: 7 unshuffled fits have N outside 0 to 1e6, and Mouse2011 has a mean I0 of 23.7. This drives the failures of saturation-ensemble-size, suppl11b and suppl8. No check of how N depends on the number of subsets was run, so these three outcomes may reflect the reduced repetitions and not the data.
2. [affects a conclusion] NB2 cell 26: suppl8 is not run with failed fits and misaligned sessions excluded, although cells 22 and 24 run that variant for 11b and 11c. Degenerate I0N values (up to 1e5 or more) enter log10 I0N.
3. [affects a conclusion] NB1 cell 42, the `filt` filter: the confidence intervals that decide pf-width-variance-not-predictive (p = 0.041 → 0.10) are the author's delta-method construction from slope standard errors, not the paper's method. It keeps 69 sessions where the code kept 72. The outcome depends on about 4 sessions.
4. [does not affect a conclusion] `OvOLinearSVM`: the docstring says C defaults to 100 "to approximate the code's unregularized fit", but the notebook uses C_SVM = 1.0, labelled "assumed". The two disagree. Cell 10's C variants (0.1 and 10) move the RMS medians by about 0.3 cm, so no outcome flips. The decoder also uses majority voting where MATLAB uses loss-weighted decoding.
5. [does not affect a conclusion] Cell 14: the "modulated cells" subset (max > 0.2·SD) does nothing. Its n is identical to all cells, and on synthetic non-negative data the test passes 100% of the time. The minimal-modulation reading in the criterion was therefore never applied. The 1180 cm width cap that drops 195 fits is the author's own choice. Neither can lift the width from 16 to 37.8 cm.
6. [does not affect a conclusion] Cell 14: the spatial information "skaggs" reading assumes uniform occupancy. The literal footnote formula, H/20, cannot exceed log2(20)/20 = 0.216, so it can never reach 0.24.
7. [does not affect a conclusion] NB1 cell 7: in 6 sessions the event trace does not follow position at lag 0. Two of them (sessions 83 and 84, Mouse2011) decode near chance at every lag within ±10 s, and two others align at -80 to -90 frames. All six stay in the main readings. Because fig4c and fig5f match the code's printed values to the third decimal, the paper probably used the same deposit, so keeping them is right for the main reading.
8. [does not affect a conclusion] `eigen_snr` takes the first h trials of each direction, not a random set, and the curve is truncated to the 14 components every session shares. The peak at 7 against 6 is within about 1.5%.
9. [does not affect a conclusion] fig3cd (3) holds for the median but in only 72 of 110 sessions, with 20 subsets against the paper's 80.

Helper checks on synthetic inputs:
- `shuffle_tensor` keeps each bin's values and removes correlation (0.89 → 0.04).
- `fit_imse` recovers I0 = 1e-4 and N = 300 (gives 292). On purely linear data it returns N around 3e9, consistent with the shuffled fits.
- `jitter` recovers 0.05 and 0.10 cm.
- `select_trials` finds 59 of 59 runs on a clean trajectory.

### C. What I could not check

- The figures: only text outputs were readable to me. A printed table of each session's fitted curve against its IMSE points would have let me judge fit quality directly.
- Whether the saturation, suppl11b and suppl8 failures come from the 4 subsets per size. N re-fitted with 80 subsets on the 1, 10, 20… grid for a few sessions would settle it.
- suppl8 with failed fits and misaligned sessions excluded (see problem 2).
- The paper's MATLAB code. The code citations in the claims file and hc30.py (Cloud.m, adjacent_metrics, Org.m filters, one_hwhm) could not be verified. The close match to the code's printed values for fig4c, fig5f and fig3f is indirect support.
- Which session is Fig. 2c's. The session average was used, which the criterion allows.
