## Round-2 verification report: Zaki et al. 2024 on DANDI:000718 (0.260825.1902)

These counts come from the claims file and the attempt record. There are 26 claims. The record gives 3 reproduced (source-data-link, ed9b, offline-skew), 2 not reproduced (burst-locomotion-pause, fig5c-wake), and 21 blocked. Of the blocked claims, 1 is methods_underspecified (offline-bursts) and 20 are data_missing. I saved the paper text to `paper/zaki2024.txt` (from Europe PMC, PMC11666460) and read it from there. I did not re-run the notebook.

### 1. Do I agree with the stated outcomes?

- **source-data-link, reproduced:** agree. Cell 20 shows 4 of 4 values within tolerance under both readings.
- **ed9b-aversive-freezing-high-vs-low, reproduced:** agree. It compares one mouse per group (cell 24).
- **offline-bursts-above-shuffle, blocked (methods_underspecified):** agree. This is the second option I offered in round 1. The positive control in cell 29 shows that the criterion's test cannot detect coordinated firing.
- **offline-skew-above-shuffle, reproduced:** agree. True skew is above the shuffle maximum in 3 of 3 recordings (cell 32), and the control in cell 29 detects coordination. The wording on the paper's range is wrong; see section 2.
- **burst-locomotion-pause, not reproduced:** agree. All p ≥ 0.39 (cell 35). This is weak evidence, as the record says.
- **fig5c-wake-overlap-neutral-coburst, not reproduced:** agree, with one caveat. Strictly by the criterion as written, the outcome would be partially reproduced: under the "wake alone" reading, OxN is 32.0% against OxA 28.0% (cell 39). The record states this departure openly as a deviation, and the case for it holds:
  - The Methods' scoring has only sleep and wake (EMG Gaussian mixture, then theta/delta). Applied to this mouse, it puts 94.1% of quiet-wake frames and all 87 bursts in wake (cells 17 and 39).
  - The paper itself says these bursts occur "during brief periods of quiet wake", which counts quiet wake as part of its wake.
  - One weakness remains: the EMG measure (log RMS) was chosen after the data were seen. Without the log, the mixture puts every epoch in one state.
- **The 20 data_missing claims:** agree with all of them.
  - I need to correct my round-1 grouping. Fig. 1d–g is the calcium-imaging experiment: the legend says "Calcium imaging was performed during all sessions", and Fig. 2a calls it "the same experiment as in Fig. 1d".
  - So fig1ef and fig1g belong to the one-hour imaging cohort, not the behaviour-only experiments. The record's own notes for those two claims say this correctly.

### 2. Sentences the printed outputs do not support

- **Cell 33 (skew conclusion):** "The values lie in the range of the paper's own Extended Data Figure 3o source data (true 1.76 to 3.65, shuffled 0.47 to 1.91)".
  - The true skews are 1.34, 1.65 and 1.72, all below 1.76.
  - The surrogate means are 0.37, 0.40 and 0.60, so two of three are below 0.47. ED3o compares the mean of the shuffled skews, so the means are the right comparison.
- **Attempt record, offline-skew notes:** "The surrogate values are in the range of the paper's own chance level (shuffled skew 0.47 to 1.91 …), so here the procedures agree." This is the same error. It also contradicts my round-1 reason as the record quotes it ("Skew is lower than the paper's chance-level data in both arms").
- **Cell 41 and the fig5c notes:** "co-participation here (26 to 36%) is not on the scale of the paper's values for this mouse (10.37% OxN and 8.39% OxA in wake)". That holds only for the inclusive reading. The exclusive reading gives 8.05% and 17.24% (cell 39), which is on the paper's scale. The underlying point stands, since z-scoring is done within one recording, but the comparison as written is selective.
- **README table, cell 0 and the Summary table (cell 42):** "Behaviour-only experiments … five claims" and "One-hour offline and single-experience experiments … nine claims". These should be three and eleven. The total of 20 is right.
- **Cell 10 (minor):** "about 190 px for random pairs". The printed medians are 196, 185 and 169 px.
- **Cell 18 (wording):** "This is consistent with the data, not shown, as the paper does not name its EMG feature." The sentence is unclear. It should say the mapping is supported by the data but rests on a measure chosen here.
- **Not checkable from the outputs:**
  - The "RLI9" and "RLI5" mouse names in the ed3 and ed4f notes.
  - "the lab did not use it for analysis (conversion notes)" in the locomotion notes.

  The notebook prints neither of these.

Every other number in the "Result:" conclusions, the Summary, the README and the record notes matches the printed outputs. I checked:
- source-data-link and ed9b values, the within-5% and within-1% statements, and the 55.27-point difference.
- The burst values at z = 2 and 2.5, the merged and fixed-threshold variants, and the synthetic controls.
- The locomotion p-values, the 0.30 to 0.60 share of bursts, the post-burst values, decoding r of 0.06 to 0.24, Spearman r of 0.07 to 0.32, and the wake to quiet-wake ratio of 4 to 15.
- The fig5c values at thresholds 1.5, 2 and 2.5, the outside-burst ≤1.02%, and the ensemble-participation p of 0.041 to 0.0003.
- The epoch table, the 113 s gap and the 1800 s spacing.

Statements I checked against the paper: 6 s epochs with an EMG Gaussian mixture, telemetry at 100 Hz, "locomotion" as the name of the telemetry channel, and Extended Data Fig. 10c's roughly 30 min awake after encoding. All match.

**My round-1 reasons in the record:** they are stated faithfully in my own words for every claim. Recording offline-bursts as "agrees: false, not_reproduced" matches what I wrote. The skew reason is quoted correctly, but the author's notes then contradict it, as described above.

### 3. Status of my round-1 points

| Point | Status |
|---|---|
| 1. Burst shuffle | Resolved. Blocked, with a positive and negative control in the notebook (cell 29). |
| 2. fig5c, which reading of wake | Resolved, with the deviation recorded. The open part is the EMG measure chosen after seeing the data. |
| 3. fig5c, z-scoring within one recording | Acknowledged as a deviation. It cannot be fixed from the archive. The scale comparison is selective (section 2). |
| 4. ActivitySignal | Mostly resolved. The description, distribution, correlation with EMG and the wake to quiet-wake contrast are now printed. The wake/quiet-wake labels come from the same sensor, so that contrast partly checks the signal against itself, and nothing shows it resolves a sub-second pause. The outcome does not change. |
| 5. Calibration of the locomotion test | Resolved by disclosure (cell 37). |
| 6. Session order and clock | Resolved. The full 27-row epoch table is printed and the 1800 s spacing is shown (cells 5 and 6). |
| 7. Telemetry at 500 Hz against 100 Hz | Resolved (cell 4 and the findings). |
| 8. Pseudo-replicated freezing bins | Resolved by disclosure (cell 25). |
| 9. Sleep state of outside-burst windows | Resolved. Every frame in a window must now be in the state (cell 40). |

**What remains that bears on a conclusion:**

- **Skew:** the claim that the procedures agree with the paper's chance level should be removed from cell 33 and the record. The outcome stays reproduced.
- **fig5c:**
  - The outcome rests on a departure from the criterion as written and on an EMG measure chosen after the data were seen.
  - The scale comparison should cite both readings.
  - The evidence is one 10 min recording of one mouse, with p = 0.13 in the opposite direction.
- **Claim grouping:** fig1ef and fig1g should move to the one-hour imaging cohort group in the README, cell 0 and the Summary.
