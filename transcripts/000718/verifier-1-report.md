I checked 26 claims: the notebook tests 6 and treats 20 as blocked. By my reading, 3 reproduce, 1 partially reproduces and 2 do not, and the 20 blocked claims are blocked because the data are missing. No separate attempt record was among my materials, so these counts come from the claims file and the notebook.

Sources: the paper's full text is saved at `paper/zaki2024.txt`, from Europe PMC (PMC11666460). I listed the archive's files through the DANDI API, and read only the internal file structure of two files (the `Week` file and one offline file) by streaming.

**A. Outcomes**

| claim id | outcome | reason |
|---|---|---|
| source-data-link | reproduced | Both mice are found. Their shock amplitudes (1.5 and 0.25 mA) match the source data's groups, and all 4 freezing values fall within tolerance under both readings (cell 18: a = 64.09, 8.82, 17.40, 15.06; b = 63.45, 8.46, 16.91, 14.61). I fetched ExtData9b.csv and ExtData9c.csv at commit a508164 and the typed reference values match them exactly. |
| ed9b-aversive-freezing-high-vs-low | reproduced | Recall1 freezing is 64.09% for Ca_EEG2-1 against 8.82% for Ca_EEG3-4, and the Mann-Whitney test on 30 s bins gives p = 0.00018 (cell 21). This compares two animals, not the paper's groups (n = 5 and 4). |
| offline-bursts-above-shuffle | not_reproduced (as the criterion is written) | At z = 2 the true burst rate is below the shuffled mean in all 3 recordings (8.71 vs 10.94, 6.40 vs 8.79, 5.30 vs 8.48 per min; cell 23). I do not count this as evidence against the paper, because the criterion's shuffle test cannot detect coordinated firing (problem 1). With a fixed threshold, the true rate beats every surrogate (cell 24). |
| offline-skew-above-shuffle | reproduced | True skew is 1.65, 1.34 and 1.72, against shuffled 95th percentiles of 0.72, 0.51 and 0.48; no surrogate reaches the true value (cell 26). Skew is lower than the paper's chance-level data in both arms (paper: true 1.76 to 3.65, shuffled 0.47 to 1.91, another cohort recorded at 30 Hz for 1 h). |
| burst-locomotion-pause | not_reproduced | The one-sided Wilcoxon gives p ≥ 0.39 in all 3 recordings under both time-zero readings (cell 28). The measure is the telemetry probe signal, not the paper's webcam locomotion (problem 4). |
| fig5c-wake-overlap-neutral-coburst | partially_reproduced (by the letter of the criterion) | OxN > OxA only under "wake alone" (32 vs 28% and 8 vs 4%), resting on 2 against 1 discordant bursts, McNemar p = 1.0 (cell 31). Under "wake plus quiet wake", the reading closer to the Methods, the direction reverses (26.4 vs 35.6%, 7 vs 15, p = 0.13). |
| fig1bc, fig1ef, fig1g, ed1n, ed2 | blocked: data_missing | The archive holds only the two Ca_EEG mice (20 assets: 12 NWB files and 8 behaviour videos). No behaviour-only mice. |
| ed3, ed4f, fig3c, fig3f, fig4b, fig4e, ed7 | blocked: data_missing | The one-hour cohort (RLI mice in the source data) is absent. Analogues could be run on Ca_EEG2-1 but would not test these claims. Cell 32 already computes a fig3f-like comparison (neutral vs remaining participation, Wilcoxon p = 0.041 across bursts, bursts treated as independent). ed7 could be run as a one-mouse SVM on the registered neutral-encoding and FC cells. |
| fig6a, fig6b | blocked: data_missing | One-hour cohort missing. Also, the high-shock mouse has no neutral or novel recall session; I confirmed there is no Recall2 or Recall3 asset for Ca_EEG2-1. |
| ed6-overlap-inhibitory, ed8-no-shock-no-coburst | blocked: data_missing | The Gad2 chemotagging mice and the no-shock mice are not deposited. |
| ed9c-eeg-cohort-linking | blocked: data_missing | The high-shock half cannot be tested (no Ca_EEG2-1 Recall2 or Recall3). The low-shock half could be described for one mouse: neutral 17.40% vs novel 15.06% (cell 18), with no test. |
| fig5c-sleep-no-coburst-difference | blocked: data_missing | The deposited offline calcium recordings contain only wake and quiet wake (cell 15). The NREM and REM recordings, among the other 23 per offline period, are not deposited. |
| fig5c-low-shock-wake-no-difference | blocked: data_missing | Ca_EEG3-4 has no CellReg tables. Its neutral encoding, FC and offline day 2 files do hold ROI centroids, so a one-recording test with centroid-based registration was possible but not attempted. |
| ed9-ed10-sleep-unchanged | blocked: data_missing (one part was testable) | The Week file holds 9.36 days of raw EEG, EMG, activity and temperature for Ca_EEG2-1, with a 27-row epoch table and no sleep scoring. ED10 (sleep before vs after encoding) and ED9g (sampled vs total state time) could be checked for one mouse by applying the Methods' scoring (6 s epochs, GMM on EMG, then on theta/delta). ED9d and 9e need the no-Miniscope mice, which are absent. |

**B. Problems**

1. [affects a conclusion] Burst-frequency shuffle, cell 23 and `shuffle_surrogates`: z-scoring each surrogate again makes the test unable to detect coordination.
   - I planted 6/min strongly coordinated bursts in synthetic data. The true rate was 5.9/min against a re-z-scored null mean of 31.7/min. Without coordination: 33.1 against 33.0.
   - The fixed-threshold variant behaves correctly: 5.9 against 0.02 with coordination, 33.1 against 32.9 without.
   - Neither variant matches the paper's chance level. In the paper's ED3m the shuffled rate is 0.72 to 0.96 of the true rate; here it is 1.26 to 1.60 (re-z-scored) and about 0.00 to 0.01 (fixed threshold).
   - So the paper's event definition or null differs, and it is underspecified (the Methods say only that the mean was "re-computed"). The criterion needs revising, or the claim should be treated as blocked: methods_underspecified.
2. [affects a conclusion] fig5c, cell 31: the sleep scoring in the Methods has no quiet-wake class (EMG GMM for sleep vs wake, then NREM vs REM). In paper terms, every deposited frame is "wake", which makes reading (a) the faithful one, and under it OxN < OxA. The "under one reading" rule, across 4 readings, allows a post hoc pick.
3. [affects a conclusion] fig5c, cell 31: the ensemble means are z-scored within one 10-minute recording, whereas the Methods concatenate all 24 offline recordings first. Co-participation comes out at 26 to 36% (inclusive) against the source data's 10.37 and 8.39% for this mouse (Fig_5c.csv, which I verified). The two are not comparable.
4. [affects a conclusion] burst-locomotion-pause, cells 28 and 29: the file describes ActivitySignal as "motion of the probe relative to the receiver". It is not a locomotion measure, and the notebook never printed its description or validated it. The claim's evidence (Fig. 2d,e) comes from webcam tracking in another cohort. Outcome stays not_reproduced, but it is weak evidence against the paper.
5. [does not affect a conclusion] Cell 28: the same Wilcoxon gives p = 0.016 at 300 random times in Ca_EEG2-1. The test on overlapping windows is not calibrated.
6. [does not affect a conclusion] Cells 5 and 6: the order of the Ca_EEG2-1 offline recording after FC rests on inferring a 1-hour clock error. The telemetry gap and the exact EEG match support it. If it were wrong, the fig5c analysis would be invalid.
7. [does not affect a conclusion] The files give telemetry at 500 Hz; the Methods say 100 Hz. The notebook does not note this.
8. [does not affect a conclusion] Cell 21: the 30 s bins are autocorrelated, pseudo-replicated units from two animals.
9. [does not affect a conclusion] Cell 32: outside-burst windows take the sleep state of their first frame only.
10. Helper checks that passed:
    - `shuffle_surrogates` gives the same result as a naive per-cell `np.roll` implementation.
    - `burst_events` (with and without merging), `binned_freezing`, `freezing_percent` and `state_of_frames` behave correctly on synthetic inputs.
    - Ensemble counts (97 neutral, 80 aversive, 166 overlap, 282 remaining) match the claims file.
    - The ExtData3m, ExtData3o, 9b, 9c and Fig_5c values typed into the notebook match the repository. In ExtData9c, Ca_EEG3-4's Neutral and Novel rows sit in the opposite blocks from the other mice; the notebook follows the CSV's Context labels, which agree with the session descriptions.

**C. Not checked, and the output that would have allowed it**

- The paper's burst event definition (minimum duration, peak separation) and its null. The analysis code returns 404. A positive control in the notebook (synthetic coordinated data run through the criterion's test) would have exposed problem 1 directly.
- Whether ActivitySignal tracks movement: print its description and distribution, and its relation to EMG and to the wake/quiet-wake labels.
- How the deposited "quiet wake" label relates to the paper's states: print the SleepIntervals description and the state definitions from the conversion code.
- That OfflineDay2Session1 is the first recording after FC: print the full 27-row epoch table.
- fig5c on all 24 recordings: these are not deposited, so it cannot be checked from the archive.
- I did not re-run the notebook. Every number above comes from its saved outputs, my synthetic tests, the archive file listing and the source-data CSVs.
