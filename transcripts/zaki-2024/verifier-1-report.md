**Verifier report, round 1: Zaki et al. (2024) on DANDI:000718 v0.261122.2159**

The claims file holds 26 claims. The notebook tests 6 and treats 20 as blocked: 4 with their own reasons and 16 because the mice are not in the dataset. I had only the notebook, the helper module and the claims file, not the attempt record, so these counts come from those.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| source-data-link | reproduced | Both mice are found and their shock amplitudes match the source-data groups (cell 17). All 4 freezing values are within tolerance under both readings: (a) 64.09/8.82/17.40/15.06, (b) 63.45/8.46/16.90/14.60. Reading (b) gives the CSV value exactly for 3 of the 4. |
| ed9b-aversive-freezing-high-vs-low | reproduced | Recall1 freezing is 64.09% for Ca_EEG2-1 against 8.82% for Ca_EEG3-4. The high-shock mouse is higher in 10 of 10 bins; Mann-Whitney U = 100, p = 1.8e-4 (cell 19). |
| offline-bursts-above-shuffle | reproduced, under reading (b) only | (b): the true rates of 8.73/6.42/5.31 per min are above every surrogate, whose 95th percentiles are 0.30/0.10/0.00, for all 5 seed sets. (a): the true rate is *below* the surrogate mean in all 3 recordings (fraction ≥ true 0.999–1.000), which is not reproduced. The criterion lets one reading decide, but see B1. |
| offline-skew-above-shuffle | reproduced | True skew is 1.645/1.339/1.721 against surrogate 95th percentiles of 0.708/0.508/0.466. No surrogate reaches the true value, for all 5 seed sets (cell 24). |
| burst-locomotion-pause | not_reproduced | p < 0.05 in 0 of 3 recordings under both the peak and onset readings, with p from 0.45 to 0.92 (cell 26). The mean traces rise at time zero rather than dip in Ca_EEG2-1 (0.22 → 0.26). See B3 and B4. |
| fig5c-wake-overlap-neutral-coburst | partially_reproduced, under wake reading (b) only | Wake alone (24 bursts): OxN is above OxA (33.3 vs 29.2; 8.3 vs 4.2), but on only 2 against 1 discordant bursts, McNemar p = 1.0. Wake + quiet wake (85 bursts): OxN is below OxA under both co-participation readings (25.9 vs 35.3; 8.2 vs 17.6), p = 0.134 (cell 28). See B2. |
| fig5c-sleep-no-coburst-difference | blocked (data_missing) | Confirmed: the three deposited offline files hold only wake and quiet wake (cell 3). The Week file holds no sleep scoring and no imaging. |
| fig5c-low-shock-wake-no-difference | blocked (data_missing) | The archive list has no Week or registration file for Ca_EEG3-4; Ca_EEG2-1's registration is in its Week file. The notebook never prints the processing groups of the Ca_EEG3-4 files, so its claim that they hold no registration rests on the claims file's data check (C2). |
| ed9c-eeg-cohort-linking | blocked (data_missing), partly testable | Confirmed: Ca_EEG2-1 has no Recall2 or Recall3 asset. The low-shock half could be tested descriptively on Ca_EEG3-4: neutral vs novel recall is 17.40 vs 15.06 (a), 16.90 vs 14.60 (b). The notebook does not do this. |
| ed9-ed10-sleep-unchanged | blocked (data_missing / methods_underspecified), partly testable | No mouse without a Miniscope is in the dataset (2 subjects), so the comparison with no-Miniscope mice is blocked. The question of whether sleep structure changes after encoding could be tested for one mouse: score the Week file's continuous EEG/EMG with the Methods' 6 s epochs and two-state GMMs. The notebook does not try. |
| 16 claims of the other experiments (fig1bc, fig1ef, fig1g, ed1n, ed2, ed3, ed4f, fig3c, fig3f, fig4b, fig4e, ed6, ed8, ed7, fig6a, fig6b) | blocked (data_missing) | Confirmed from the archive: `numberOfSubjects` is 2, and the 20 assets are 12 NWB files of Ca_EEG2-1 and Ca_EEG3-4 plus 8 behaviour videos. |

No numeric chance level is stated in the paper's text for these selections (Extended Data Fig. 4n and 8f give only figure panels), so I had none to compare with the notebook's.

### B. Problems

1. **[affects a conclusion] offline-bursts-above-shuffle, reading (b)** (`circular_shift_surrogates` with `normalise=False`, cell 21).
   - A circular shift keeps each cell's mean, so the surrogate mean trace has exactly the true trace's mean but a smaller SD. A threshold at the true mean + 2 SD therefore almost never fires on a surrogate once cells share any positive covariance, burst-like or not.
   - Synthetic check: independent AR(1) cells with only a slow shared drift and no bursts. Reading (b) gives a "reproduced" result (true 2.40/min against surrogate 95th percentile 0.00). Reading (a) gives the same reversal as the real data (true 2.40 against surrogate mean 4.98).
   - So the reproduced outcome is near-guaranteed and does not show burst structure.
   - The Extended Data Fig. 3l legend ("the burst frequency was computed for each of these shuffles") reads most naturally as running the full detection, including z-scoring, on each surrogate. That is reading (a), and under it the claim fails clearly.
   - This comes from the claims file, not the notebook, so I report it and do not correct it.
2. **[affects a conclusion] fig5c-wake, the reading of "wake"** (cell 28).
   - The paper's sleep scoring (Methods, "Sleep recordings and sleep scoring") has only wake, NREM and REM, and the source data (Fig_5c.csv) has only those three states. The files' "quiet wake" has no counterpart in the paper, so the paper's "wake" most plausibly corresponds to reading (a), wake plus quiet wake.
   - Under (a), OxN is below OxA.
   - The Methods also count the triple combination separately, which favours co-participation reading (ii). Under (a)(ii) the result reverses: 8.2 vs 17.6.
   - The partial outcome rests on (b), with 3 discordant bursts. The criterion permits this, so the outcome stands, but it is fragile.
3. **[affects a conclusion] burst-locomotion-pause, clock alignment** (cells 13, 26).
   - In the offline files, population activity correlates best with |ActivitySignal| at lags of +1.5, +5.5 and +6.5 s, not 0 s (cell 13). In the behaviour sessions the best lag is about 0 s.
   - A few seconds of offset between imaging and telemetry would move the −1–0 s and −5 to −3 s windows by more than their width. The notebook states this assumption but never tests the outcome's sensitivity to it.
4. **[does not affect a conclusion] burst-locomotion-pause, window lengths** (cell 26). The test compares a 1 s window with a 2 s window in a paired one-sided Wilcoxon test. On heavy-tailed movement the shorter window's mean has a lower median, so the test leans towards "lower before" when nothing is there.
   - Synthetic check: i.i.d. skewed movement at random times, n = 85, gives a false-positive rate of 0.195 at α = 0.05.
   - Ca_EEG2-1's random-time reference gives p = 0.000 in the same direction.
   - The outcome is negative anyway, so this biases towards a result that did not happen. It comes from the criterion.
5. **[does not affect a conclusion] burst-locomotion-pause and the two shuffle claims, which experiment is tested.**
   - Fig. 2d,e and Extended Data Fig. 3l–o come from the one-hour webcam experiment (8 different mice).
   - The claims file tests them on 10-minute recordings from the EEG mice, with the telemetry signal as the movement measure.
   - So the outcomes speak to these mice and this measure, not to the paper's data. This is a choice in the claims file, which I note rather than correct.
6. **[does not affect a conclusion] ed9b, statistics** (`binned_freezing`). The 30 s bins within one session are autocorrelated, so the Mann-Whitney test treats non-independent samples as independent. The test is the criterion's, and the direction is unambiguous.
7. **[does not affect a conclusion] fig5c, z-scoring.** The paper z-scores ensemble traces over 24 concatenated sessions; here they are z-scored over one session (`ensemble_traces`). With only one session deposited, this is unavoidable.
8. **[does not affect a conclusion] helpers checked on synthetic inputs.** `burst_events`, `burst_frequency`, the circular shift (matches `np.roll`), and `binned_freezing` (10 bins from 8998 frames) all behave correctly. The McNemar test is an exact binomial on discordant bursts, which is correct.
9. **[does not affect a conclusion] metadata inconsistencies.** The archive's offline-session descriptions describe the one-hour webcam protocol, not the EEG home cage. The telemetry is stored at 500 Hz where the Methods say 100 Hz. The Week file's start time is labelled +00:00 but its epoch times match the session files' −04:00 clock times.

### C. What I could not check

1. **What ActivitySignal measures.** The notebook never prints the NWB description or unit of `acquisition/ActivitySignal`, so treating it as locomotion is an assumption. It is a signed, continuous signal (−0.9 to 5), not counts. Printing its attributes would settle this.
2. **Whether Ca_EEG3-4 has cell registration.** Printing `list(f["processing"])` and the `processing/ophys` keys for the Ca_EEG3-4 offline files would confirm or refute the blocking of fig5c-low-shock-wake-no-difference. Archive metadata lists only module types.
3. **What "quiet wake" means.** Printing the SleepIntervals description would show whether it is a sub-state of the paper's wake or something else (B2).
4. **Sensitivity of the locomotion test to clock offset.** Re-running the locomotion test with the telemetry shifted by the lag of peak correlation (cell 13) would show whether the negative result survives B3.
5. **The amendment record.** The notebook cites `questions/zaki-2024.yaml` for the criterion amendment, which I do not have. The claims file I have already contains both readings.
