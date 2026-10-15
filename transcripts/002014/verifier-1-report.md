**A. Outcomes by claim**

The claims file lists 13 claims. The notebook tests 5 and treats 8 as blocked. I checked the archive through the API: one asset (`sub-Monkey-T/sub-Monkey-T_ses-09272024_ecephys.nwb`), `numberOfSubjects` 1, and only two versions (draft and 0.261012.0921).

| Claim | My outcome | Reason |
|---|---|---|
| fig8a-single-trial-dopamine | reproduced | Trial id 133 (1-based, a successful large-reward trial) gives an SD ratio after/before V of 2.02 with no NaN in either window. Index 133 gives 2.04 (cell 19). This is a weak test: 60% of successful trials also exceed 1 (median 1.27). |
| fig8b-dopamine-large-vs-small | reproduced | V to RW: large 1.87 against small 1.11, difference 0.76, Mann-Whitney p = 0.0037, n = 434/466, with 18/33 trials dropped (cell 21). Before V there is no difference (p = 0.52). RW to RW+3 s gives p = 0.0002. The effect is weaker in the first half of the session (p = 0.089). |
| fig9a-spikes-task-aligned | reproduced | (i) 100% of the 951 successful trials have a spike in V−1 to V+3 s. (ii) Modulation is 0.49 against a null 95th percentile of 0.06 (max 0.07, p = 1/201) (cell 23). This depends on the 11812.1 s clock offset, which is well supported: r 0.977 to 0.998 at 8 points against ≤0.35 elsewhere (cell 12). With the times as stored, the test fails (0.01). |
| fig9bc-unit-waveform-isi | reproduced (by the criterion; weak evidence) | 0 of 101,732 ISIs are under 1 ms. The mean waveform extreme is −56.4 µV against an SD of 11.8 µV, ratio 4.8 (cell 25). Both sub-criteria are close to guaranteed by threshold detection (problem 1). |
| fig9d-beta-suppression-large | partially_reproduced | Median log-ratio is −0.158 for large and −0.125 for small trials (both below 0, large lower), Mann-Whitney p = 0.108, no trials dropped (cell 27). No variant reaches p < 0.05; the 0–0.3 s window reverses the sign (+0.001). |
| recordings-two-monkeys | blocked (data_missing) | The archive holds only monkey T. The monkey T half is testable and is supported by fig8b and fig9a. |
| scfe-functional-yield | blocked (data_missing) | The electrodes table has 4 sites from one session. There are no per-electrode background-current or noise values for the 40/51 sCFEs. Nothing can be tested. |
| scfe-background-yield | blocked (data_missing) | Same as scfe-functional-yield. |
| mcfe-functional-yield | blocked (data_missing) | Same as above; the archive has no mCFE inventory. |
| dopamine-signal-yield | blocked (data_missing) | The archive has one FSCV site (c8ds) and no functional-CFE list. |
| asepsis-cultures | blocked (data_missing) | The archive has no culture records. |
| fig6-drainage-volume | blocked (data_missing) | The archive has no aspiration volumes. |
| fig7-bone-growth-margins | blocked (data_missing) | The archive has no imaging or histology. |

**B. Problems**

1. [affects a conclusion] Cell 25 / fig9bc criterion cannot really fail. The shortest ISI is 1.562 ms, about the length of the 48-sample (1.5 ms) waveform, so the detector's dead time rules out ISIs under 1 ms. The 40 µV threshold also all but forces |mean| > 2 SD at the peak sample. The "single unit" reading is unsupported. Only 54,411 of 90,912 Plexon spikes fall within 0.2 ms of a thresholded spike (cell 10), and thresholded unit 1 has 101,733 spikes, so it likely includes multi-unit crossings. The Plexon unit has 1 ISI under 1 ms and 39 under 2 ms.
2. [affects a conclusion] Cell 19 / fig8a criterion is weak. A random successful trial passes 60% of the time. The claims file also notes the author printed trial 133's dopamine values before writing the criterion. The outcome stands, but it carries little evidence.
3. [does not affect a conclusion] Cell 21 and cell 27 run Mann-Whitney tests that treat trials as independent. Dopamine and LFP drift slowly within the session, which inflates significance. The fig8b effect is p = 0.089 in the first half and p = 0.0098 in the second.
4. [does not affect a conclusion] The cell 27 plot is distorted at its edges. `band_power_around` filters 6 s segments and the plot runs to +3 s, the last sample. On synthetic white noise I get normalized power of 2.3 at +3 s and a minimum of 0.41 at 2.98 s, against about 1.1 mid-segment. The printed plotted minimum of 0.059 is probably this artefact. The windows used in the test (±1 s) are not affected.
5. [does not affect a conclusion] `reference_at`: when the sample at V is NaN, the fallback averages samples within ±0.2 s, and floating-point edges can make that window asymmetric. On a synthetic linear ramp this gave a 0.13 offset. It only applies to trials where V itself falls on a NaN sample.
6. [does not affect a conclusion] Cell 23 leaves the stored spike times about 7 ms late against raw c5d (found in cell 12). The lag-corrected variant gives 0.48, against 0.49 for the main test.
7. [does not affect a conclusion] Cells 6 and 7 keep trial 1411, which the Zenodo large-reward list omits (1 trial in 452). Cell 6 reads Zenodo files named "c8c", while the dandiset site is "c8ds"; the notebook never addresses the mismatch.
8. [does not affect a conclusion] The dandiset description says "all data are expressed relative to the start of the Neuralynx recording". The data contradict this: the raw ephys and spikes sit 11812.1 s off the trial clock. The notebook measures the offset and does not take it from the metadata, which is correct. The mismatch should be reported upstream.
9. [does not affect a conclusion] Cell 27 tests the median of per-trial log ratios. The paper's Fig. 9D shows trial-averaged power. The notebook prints no number for the trial-averaged normalized curves over 0 to 0.5 s.

**C. What I could not check**

- I did not see any figures; the notebook's images were not rendered. I could not compare the PSTH, waveform, ISI histogram or beta curves with the paper's Figs. 8 and 9.
- I could not confirm the HDF5 layout of `thresholded_units/waveforms` (flat samples with `waveforms_index`) without opening the file. The 48-sample output is consistent with how `thresholded_waveforms` indexes it.
- The paper gives no beta band, windows or statistics. The fig9d result depends on choices made in the claims file.

Outputs that would have let me check these:
- Trial 133's percentile rank among the per-trial SD ratios.
- The mean trial-averaged normalized beta power over 0 to 0.5 s per condition, with a bootstrap CI, and the curve restricted to ±1.5 s.
- The fraction of ISIs under 1.6 ms for the Plexon unit, and the detector's dead time.
- The numeric PSTH values per condition.
- The shapes of the `waveforms` and `waveforms_index` datasets.

I saved the paper text to `paper/choi2025_pmc.txt` (PMC13250822, CC BY). The synthetic tests of `psth`, `window_mean` and `trial_table` gave the expected results.
