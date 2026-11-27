**Verifier report, round 2: Zaki et al. (2024) on DANDI:000718 v0.261122.2159**

The claims file holds 26 claims, and the attempt record gives 26 outcomes: 6 tested and 20 blocked (data_missing).

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| source-data-link | reproduced | Yes. Both readings give 4 of 4 within tolerance (cell 19). | none |
| ed9b-aversive-freezing-high-vs-low | reproduced | Yes. 64.09 vs 8.82, 10 of 10 bins, U = 100, p = 1.83e-04 (cell 22). | none |
| offline-bursts-above-shuffle | reproduced, `assumed: true` | Yes, as the criterion gives it (cell 25). | Stated clearly (deviation 2, cell 28). It is not a well-supported reading: the record itself says (b) is "not the better-supported one" and is passed by drift-only cells (cell 27). The outcome follows from the criterion, but on a reading that cannot really fail. |
| offline-skew-above-shuffle | reproduced | Yes. True skew is above all surrogates, and every seed's 95th percentile is far below it (cell 30). | none |
| burst-locomotion-pause | not_reproduced | Yes. 0 of 3 recordings under both readings (cell 33). This holds at the lag of peak correlation and at every shift from −8 to +8 s (cell 34). | The shared clock is stated, and it is now tested by the shifts. |
| fig5c-wake-overlap-neutral-coburst | partially_reproduced | Yes, as the criterion permits (cell 37). | **Not marked `assumed`**, although the outcome rests on wake reading (b) alone. The record itself calls (b) the worse match to the paper. Under (a), OxN < OxA (25.9 vs 35.3; 8.2 vs 17.6). It should carry `assumed: true`, as the burst claim does. |
| fig5c-sleep-no-coburst-difference | blocked | Yes. Only wake and quiet wake are present (cells 3, 8). | — |
| fig5c-low-shock-wake-no-difference | blocked | Yes. Ca_EEG3-4's files hold the ophys and sleep modules only, and the only cell_registration module is in the Week file (cell 8). | — |
| ed9c-eeg-cohort-linking | blocked | Yes. The descriptive values are printed (cell 40). | — |
| ed9-ed10-sleep-unchanged | blocked | Yes. The one-mouse description is in cell 41. | Log RMS as the EMG feature is stated as an assumption, and it is reasonable. |
| The other 16 claims | blocked | Yes. The archive holds 2 subjects (cell 3). | — |

### 2. Statements the printed numbers do not support

- **Cell 35, with the same sentence in the record's burst-locomotion notes:** "Under neither reading is movement in the second before a burst lower than 3 to 5 s before it in any recording." The medians *are* lower before the burst in two recordings: 0.0303 vs 0.0356 for Ca_EEG2-1, and 0.0761 vs 0.0917 (0.0847 vs 0.1002 under onset) for Ca_EEG3-4 Day2 (cell 33). What the data support is "not significantly lower".
- **Cell 44, Summary:** "no pre-burst slowing in 0 of 3 recordings" is a double negative that says the opposite of the result. It should read "pre-burst slowing in 0 of 3".
- **Cell 45:** "Ensemble sizes … agree with the paper's source data." No comparison of ensemble sizes with the source data is printed. Cell 7 only prints the sizes (97/80/166/282).
- **Cell 28:** "above every surrogate in all three recordings … under the second generator's seed and the four others." Maxima and fractions are printed only for seed+1 (cell 25). For the other four seeds only 95th percentiles are printed. The statement is very likely true but not shown. Cell 31 says the same of the skew claim ("above every one … under all five seeds"), where again only the seed+0 maxima are printed (cell 30).
- **Cell 35 and the record's notes:** "Around random times movement in the later window is lower in Ca_EEG2-1 (p < 0.001), as movement declines over the recording."
  - The first generator gives p = 0.000 (cell 33), but the second gives 0.003 (cell 34), which is not below 0.001.
  - "Movement declines over the recording" is not printed anywhere.
- **Record, ed9-ed10 notes, and cell 42:** "awake 67% (after neutral) and 49% (after aversive) … against 93% at the same clock time the day before." The 93% reference is printed only for the post-neutral window (cell 41). There is no same-clock-time reference for the post-aversive window.
- **README:** "It takes about six minutes." Cell 44 prints a run time of 3.7 min.

Everything else in the Result cells, the Summary, the README and the record's notes matches the printed outputs. I checked in particular:
- the bursts under (a) and (b), and all five seed sets for each;
- the synthetic check (5.90 vs 2.60 under (b), mean 8.55 under (a), and the independent-cell values);
- the skew values;
- the shift table;
- the 1 s baseline variant;
- the fig5c tables and the source-data values 10.37 / 8.39;
- the 64 of 68 quiet-wake epochs scored as wake;
- the clock and dropout figures (−3780 to −2560 s, 113 s, 47 and 17 min);
- the sleep features.

The paper does say "during brief periods of quiet wake" (Results).

**Round-1 reasons:** the record's `reason` fields state my round-1 reasons faithfully, close to my own wording. The finding numbering in `reviewed` is correct: the webcam-description finding is 9.

### 3. Round-1 points

**Resolved:**
- B3, clock sensitivity: the shifts in cell 34 leave the result negative.
- B4, unequal windows: the 1 s baseline variant is in cell 34.
- B6 and B7: recorded as deviations.
- B9: now findings 4, 6 and 9.
- C1 to C3: cell 8 prints the ActivitySignal description, the processing modules and the quiet-wake definition.
- C4: done in cell 34.
- The descriptive tests for ed9c and ed9-ed10: cells 40 and 41.
- B5: recorded as deviations (the criterion's choice).

**Acknowledged but still bearing on a conclusion:**
- **B1:** offline-bursts-above-shuffle is reproduced only under reading (b). The record now documents, with its own synthetic check, that this reading is passed by co-variation alone, and has put the question to a reader. Under reading (a), the one that tests burst structure, the result is not reproduced. This remains a claims-file issue.
- **B2:** fig5c-wake rests on wake reading (b). The files define quiet wake as a waking state, and the Methods' scoring puts it in wake (cell 16), so reading (a) is the better match, and under it OxN < OxA. This is put to a reader, but the outcome is not marked `assumed` (see 1).

**Not resolvable from my materials:** C5, the amendment record `questions/zaki-2024.yaml`, which I do not have.

### 4. Critical findings

No finding in the attempt record is rated `critical`.

One rating I would change: finding 1 (rated `major`). It says the behaviour sessions of Ca_EEG2-1 are timestamped about 1 h later than the offline recordings and telemetry, and cell 15 shows this:
- the EEG match at +0.002 s with a difference of 0 V;
- telemetry dropouts that each fit their session if it started 1 h before its timestamp;
- OfflineDay2Session1 starting 2817 s before FC.

This is the "signals on different clocks" case of the definition. The files do not say which clock is right. Only a dropout analysis shows that the offset is about 1 h, and an analysis that takes the timestamps as given would misorder the first two post-FC offline recordings and misplace the post-encoding windows. I would rate it **critical**. The record's case for `major` is that the epochs table visibly contradicts the protocol, but that contradiction shows something is wrong, not what, and it does not undo the wrong result.
