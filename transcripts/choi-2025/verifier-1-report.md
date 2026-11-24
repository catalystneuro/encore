**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| fig8a-single-trial-dopamine | reproduced | Cell 9: the after/before SD ratio is 2.025 for trial id 133 (row 132, no NaN in either window) and 2.199 for row 133. The criterion needs either reading above 1. For reference, the median over all 951 successful trials is 1.257, 62.7% are above 1, and trial 133 sits at the 0.775 quantile. |
| fig8b-dopamine-large-vs-small | reproduced | Cell 12, V to RW window over all trials: large minus small = +0.751, Mann-Whitney p = 0.0031, n = 449/498, 4 trials dropped for NaN. The 0 to 2 s variant is null (p = 0.59), and the first half alone gives p = 0.051. |
| fig9a-spikes-task-aligned | reproduced | Cell 15: (i) every successful trial has a spike in −1 to 3 s. (ii) The PSTH variance is 0.4825, against a null 95th percentile of 0.056 to 0.062 over 5 seeds × 200 random alignments, and no null draw reaches it. The stored-time and Plexon variants agree. |
| fig9bc-unit-waveform-isi | reproduced | Cell 18: no intervals under 1 ms (0 of 101,732). The peak of the mean waveform is 56.4 µV against an SD of 11.8 µV, a ratio of 4.79, well above 2. Both halves of the session agree (4.78 and 5.05). |
| fig9d-beta-suppression-large | partially_reproduced | Cell 21, main measure with N=4: median large −0.158, median small −0.125. Both are below 0 and large is lower, but p = 0.109. N=2 gives p = 0.111. Of the 12 variants only one has p < 0.05 (15–30 Hz with N=2, p = 0.0496). |
| recordings-two-monkeys | blocked (data_missing) | I checked the archive: every version (draft, 0.261012.0921, 0.261120.0528) holds one asset, `sub-Monkey-T/...ses-09272024`. Monkey J is absent. The monkey T half is in effect shown by the five tested claims (see B8). |
| scfe-functional-yield | blocked (data_missing) | The single session has 4 electrodes. There are no per-electrode yield or background/noise data for the 40 and 51 sCFEs, in the archive or in the 6 Zenodo files (cell 24). |
| scfe-background-yield | blocked (data_missing) | Same as above. |
| mcfe-functional-yield | blocked (data_missing) | Same as above. |
| dopamine-signal-yield | blocked (data_missing) | Needs every functional CFE in both monkeys. The file has one FSCV site (c8ds). |
| asepsis-cultures | blocked (data_missing) | There are no culture records in the dandiset metadata or assets. |
| fig6-drainage-volume | blocked (data_missing) | There are no drainage records. |
| fig7-bone-growth-margins | blocked (data_missing) | There are no images or histology. |

**B. Problems**

1. [does not affect a conclusion] `trial_table`: the last row (id 1411) has no next trial start, so its span is open-ended (`next_start = inf`). The code classes it as large, but the paper's Zenodo list leaves it out (cell 3: "events only [1411]"). The notebook keeps it, giving 452 large trials where the paper has 451.
2. [does not affect a conclusion] Cell 5 measures a 0.5 ms offset between the raw ephys clock and the trial clock. The claims file reports 11812.1 s. The claims file's data check was probably run on version 0.261012.0921, whose asset size differs. The notebook does not mention the discrepancy. Its ±5 s search could not have found an offset that large, but r = 0.94 at lag 0 (1–8 Hz) shows the clocks agree in this version.
3. [does not affect a conclusion] Cell 5: in the 13–30 Hz band the stored LFP correlates only weakly with raw c7b−c5c (r = 0.14 to 0.16) and has about 0.15 of its SD. At 1–8 Hz the two agree (r ≈ 0.9, SD ratio ≈ 1). The dandiset description calls the stored LFP "beta-band", yet it carries 1–8 Hz content. A likely cause is FSCV interference at 20 and 30 Hz (harmonics of the 10 Hz scan) in the raw trace, removed from the stored trace, but the notebook neither checks nor discusses this. The criterion fixes the stored LFP, so the fig9d outcome stands; the beta signal it tests is just not characterised.
4. [does not affect a conclusion] The trial-aligned FSCV is tied to the trial clock only through its stored start/stop times. The `iox` cross-check "gave no consistent lag" and was not run in the notebook (cell 4). Cell 7's contrast is a weak check: the large−small difference first appears at +1 to +2 s, and there is already +0.28 at −2 to −1 s.
5. [does not affect a conclusion; claims file] fig9bc: the shortest interval is 1.562 ms, about the length of the 48-sample, 1.5 ms waveform window. So "fewer than 1% of ISIs under 1 ms" probably holds by construction (detector dead time). Threshold-selected spikes also tend to pass the peak/SD > 2 test. The criterion is weak.
6. [does not affect a conclusion; claims file] fig8b: the claim says the difference is largest "especially between V and RW", but the criterion tests only V to RW > 0. The data show a larger difference after RW (RW to RW+3 s: +1.53, p = 0.00015; 1 s bins from +5 to +8 s: about +1.6). The "especially" part is not supported, and the claims file does not test it.
7. [does not affect a conclusion] fig9d, cell 22: the trial-averaged power ratio plot shows a deeper dip for large (minimum 0.53) than small (0.70), which looks like the paper's figure. The per-trial median test is not significant. The mean is outlier-sensitive and the criterion uses medians, so the outcome stays partial.
8. [does not affect a conclusion] recordings-two-monkeys is blocked as a whole. The monkey T half could have been marked as supported by the fig8 and fig9 results. Only monkey J is missing.
9. Helper checks on synthetic inputs all passed: `_first_in`, `_any_in`, `psth`, `da_times` (−30 to +30 s), `value_at`, `window_mean`, `lfp_segment` (NaN propagation), `beta_suppression` (index windows correct; −0.584 against an expected −0.602, with the gap due to the Hilbert envelope's edge spread). I checked the `thresholded_waveforms` indexing by hand. I found no units errors and no leakage; nothing is trained.

**C. What I could not check**

- Whether every `midpoint_time` equals a code-128 event time. The classes match the Zenodo lists for 950 of 951 trials, which suggests it does. Would have needed: a printed max |midpoint − nearest code-128 event|.
- Whether the FSCV is aligned to the trial clock (B4). Would have needed: the `iox` against raw-scan cross-correlation output, or the dopamine trace aligned to RW with large and small separated, to see whether the response is locked to the event.
- Why the stored and raw LFP differ in the beta band (B3). Would have needed: power spectra of the stored LFP and the raw c7b−c5c over a few trials, marking 10, 20 and 30 Hz.
- Whether the trial 133 trace and the plotted means match Figures 8A, 8B and 9D. The paper text gives no values. Would have needed: the trial-133 `da` samples from −5 to +5 s and the per-condition mean traces printed numerically.
- Whether the PSTH dip at +0.1 s and the peak at +0.3 to +0.5 s are free of the FSCV blanking. Would have needed: the phase of the V events relative to the FSCV scan cycle.
