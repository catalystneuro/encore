I checked the notebook against the claims file and paper, tested the helper functions on synthetic inputs, and listed the CRCNS bucket (`crcnsarchive/alm-1/`) myself. The claims file has 29 claims: the notebook tests 18 and marks 11 blocked. Of the 18 tested, I find 12 reproduced, 2 partially reproduced and 4 not reproduced; I confirm all 11 blocked claims as data_missing.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| fig1d-photoinhibition-ipsilateral-bias | blocked (data_missing) | The bucket holds only the 99 electrophysiology sessions, their NWB copies, voltage traces, scripts and docs. It has no photoinhibition behaviour. |
| fig1d-sample-epoch-smaller-bias | blocked (data_missing) | Same reason. |
| task-performance | reproduced | Cell 12: 76.4–77.3% correct with 10.9–14.1% lick early under all three ways of averaging on control trials, all within tolerance. Only 19 of the paper's 42 mice are in the data. |
| unit-counts | partially_reproduced | Cell 14: 1,408 units, 19 mice, 99 sessions and 1,245 units over 0.45 ms come out of the recomputed widths. The criterion's width rule gives 158 FS and 5 intermediate units (expected 124 ± 12.4 and 39 ± 3.9). Those two counts match only through the deposited cellType labels. |
| fig2-selective-fraction | reproduced | Cell 16: exactly 912/1,245 (0.733) with lick early trials dropped and a 1.3 s response epoch. All 8 reading and test combinations fall within tolerance. |
| fig2d-response-categories | reproduced | Cell 18: 219 / 389 / 304 exactly under the figure reading (389 is the "both" count). The text reading fails. The text versus figure disagreement is a deviation. |
| fig2c-selectivity-time-course | reproduced | Cell 20: both measures rise from pre-sample to the end of the sample epoch and through the delay, and peak at +0.19 or +0.20 s. Shuffled labels give a median of 54 neurons and the pre-sample value is 60, near the 5% chance level of 62. |
| fig2c-dynamic-single-neurons | reproduced | Cell 22: mean r from sample onset to 0.5 s into the delay is −0.17 to −0.04 (below 0.5) under every reading. Population selectivity stays at or above 1.19 spikes/s. |
| ed2-error-trials-predict-choice | reproduced | Cell 24: r is negative with P < 0.05 in all three epochs and all three readings. The switched fraction exceeds 0.5 throughout, though in the sample epoch it is only 0.507 to 0.524. |
| fig2e-equal-contra-ipsi | reproduced | Cell 26: 427 contra and 485 ipsi exactly, bootstrap P = 0.97 (my exact binomial gives 0.971). The 10-trial reading also passes (436/444, P = 0.60). |
| ed1-no-population-contra-bias | reproduced | Cell 28: P = 0.44, 0.48 and 0.39 for the three neuron sets, none significant. The variants give 0.36 and 0.62. |
| ed1-fast-spiking-properties | not_reproduced | Cell 30: FS baseline rates are higher, but FS are more selective under both of the criterion's measures (0.80 vs 0.73 fraction selective; mean absolute difference 2.29 vs 1.53 spikes/s). Only the out-of-criterion normalised variant agrees with the paper. |
| tagging-counts | reproduced | Cell 32: 45 PT and 27 IT, but these are counts of the deposited labels, not re-derived. The activated-neuron counts (22 and 106) carry no labels and cannot be tested. |
| antidromic-latency-jitter | partially_reproduced | Cell 34: PT latency and jitter (2.67 ms, 0.11–0.13 ms) and PT shorter than IT hold under all readings. IT jitter (0.18–0.20) and the tagged mean (0.14) match only with the author's ±0.5 ms window; with ±1 ms they are 0.27–0.31 and 0.18, out of tolerance (see B1). Activated-neuron values cannot be tested. |
| ed5g-it-second-pulse-jitter | reproduced | Cell 36: second-pulse jitter is below first-pulse jitter in every variant, and 65–87% of IT neurons decrease. |
| fig3ei-both-types-preparatory-and-movement | reproduced | Cell 38: both types have preparatory and peri-movement neurons under all readings. With lick early trials dropped and a 1.3 s response epoch, fractions are PT 0.18/0.42/0.40 and IT 0.22/0.57/0.22, matching the values read from the figure. |
| fig3fj-contra-preferring-pt-not-it | reproduced | Cell 40: with selective neurons only, PT P = 0.033 and IT P = 0.74 (drop, 1.3 s); also passes for keep at 1.3 s and keep at 1.5 s. It fails with all neurons (PT P = 0.08–0.23), so the result rests on one reading. |
| fig3f-late-contra-selectivity-pt | not_reproduced | Cell 42: onset is 310 ms (or 2,480 ms under the second rule), against 570 ± 100. In the window ending at the cue, all task-selective neurons are significant (P = 0.024, 9.2%), against the paper's P = 0.13. In the window ending at response end, PT is not significant. No combination gives the paper's pattern, though PT reaches 34.4%. |
| reaction-time | not_reproduced | Cell 44: the mean across mice is 81.7–188 ms under all 8 settings (expected 61.1 ± 10.5), and the s.d. across mice is about 51–65 ms against the paper's 10.5. Only the per-mouse medians (68 ms), which the criterion does not use, fall within tolerance. |
| fig4-imaging-intermingled | blocked (data_missing) | No imaging files in the archive. |
| fig4h-imaging-pt-contra-bias | blocked (data_missing) | Same. |
| imaging-overall-counts | blocked (data_missing) | Same. |
| contra-ipsi-selectivity-forms | not_reproduced | Cell 46: contra-preferring neurons are a majority of the large group (0.54 and 0.52), but ipsi-preferring neurons show contra-suppression less often than contra-preferring neurons show ipsi-suppression (0.365 vs 0.389). The criterion needs both. |
| fig5-pt-activation-contralateral-bias | blocked (data_missing) | No photoactivation behaviour sessions. The data description says the NaN-type stimulation trials are test configurations not to be analysed (see B8). |
| ed6b-pt-dose-response | blocked (data_missing) | Same. |
| ed6d-it-activation-inconsistent | blocked (data_missing) | Same. |
| ed3-high-power-contralateral-licking | blocked (data_missing) | No untrained mice and no vM1 stimulation sessions. |
| ed3d-non-overlapping-it-pt | blocked (data_missing) | No anatomy files. |
| ed7-pt-stimulation-persistent-activity | blocked (data_missing) | The 2-mouse, 8-session, 91-neuron data set is not identifiable among the 99 sessions, and NaN-type trials are excluded by the description. This was not checked against the trials themselves (B8). |

**B. Problems**

1. [affects a conclusion] Cell 34 and `latency_mode_stats`: whether the IT jitter and the 0.15 ms tagged mean match depends on the author's ±1 ms versus ±0.5 ms window around the modal latency, which the paper does not give. In a synthetic test, the ±0.5 ms window shrinks the s.d.: true 0.3 ms reads as 0.24, and true 0.4 ms as 0.26. The ±1 ms window lets in spontaneous spikes: true 0.2 ms with 30% contamination reads as 0.25. Neither choice is neutral, so the match is not robust.
2. [affects a conclusion] Cell 42 (`cs_curve`, `win_rates`): this claim runs only with lick early trials dropped (`trial_mask` default), though the shared methods require the "kept" reading as well. The all-task-selective P = 0.024, which decides "not reproduced", is close to 0.05. Cells 20, 22, 24, 26, 30 and 46 are also run under dropped lick early trials and a 1.3 s response only; their margins make a flip unlikely.
3. [affects a conclusion] Cell 14 and `spike_width_ms`: 34 of the 39 unlabelled units measure under 0.35 ms, while the paper and the data description call all 39 intermediate (0.35–0.45 ms). The notebook does not investigate why (waveform array orientation, polarity, noise in low-amplitude units). It tries only a spline variant.
4. [affects a conclusion] Cell 44, the reaction-time onset rule in `_reduce`: the rule is the author's own, with thresholds at a fraction of each trial's peak excursion. It is not validated against example traces. Session baselines range from 0.07 to 4.83 V, the sign of the post-cue excursion differs between sessions, and the 5th-percentile onset is 20 ms, which is implausibly fast. Per-mouse means run from 22 to 288 ms. The failure may reflect the detector, not the data. The second trial reading also includes NaN-type and tagging trials.
5. [does not affect a conclusion] `unit_epoch_rates` and `ttest_p`: the selectivity t-test is on rates (count divided by each trial's epoch length), while the Methods say spike counts. 3,707 trials have epoch lengths other than 1.3 s. The 912 match exactly regardless.
6. [does not affect a conclusion] Cell 12: the "all trials" reading includes NaN-type trials, which the description says are not to be analysed. The control-trial reading alone passes.
7. [does not affect a conclusion] Cell 32: tagging counts restate the deposited labels, so the test is circular. Re-deriving the collision test would need the raw voltage traces, about 750 GB of tars by my listing (too large).
8. [does not affect a conclusion] Cell 4: the 3,756 NaN-type trials with light (about 50 ms pulses starting around 0.97 s, inside the sample epoch) are not broken down by animal. The metadata lists an ALM stimulation site for the Sim1 mice. Whether these are ED7-style sample-epoch PT stimulation was not checked; the description's "should not be analyzed" supports keeping ed7 and fig5 blocked.
9. [does not affect a conclusion] Cell 9: lick counts use a fixed 1 V threshold despite session baselines of 0.07–4.83 V. This count is used only as a clock check.

Helper checks on synthetic inputs all passed: `spike_width_ms`, `window_sums` (window centres), `cue_binned`, `counts_in`, and `bootstrap_more_ipsi`, whose P values match the exact binomial (0.035 vs 0.034; 0.972 vs 0.971). I found no leakage between training and test data. The 10-trial split keeps preference and the held-out difference on separate trials, and error trials are separate from correct trials.

**C. What I could not check, and which output would settle it**

- The data reduction itself, since I did not download the data. Printing the `waveforms` array shape for a few units, plus the mean waveforms and widths of the 39 unlabelled units, would settle B3.
- Reaction-time detection. Example lick traces with the detected onsets marked, and per-mouse onset histograms, would show whether the detector works.
- Antidromic responses. Per-neuron latency histograms for the IT neurons, with both windows marked, would show which window fits.
- fig3f-late under the lick-early-kept reading (and 1.5 s), giving the P value for all task-selective neurons.
- NaN-type light trials tabulated by animal, session, onset, pulse width and power, to settle B8 and the ed7 and fig5 blocked status.
- The MATLAB scripts the notebook cites (`analysis_compile_all_data.m` for the "stable trials" span, the >15-trial and >10/>5 thresholds; `Demo_get_performance.m`). I did not read them, so these citations are unverified.
