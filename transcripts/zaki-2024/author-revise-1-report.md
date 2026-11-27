I've answered every point in the round-1 report and re-run the entry. No outcome changed. `python tools/entry.py all entries/zaki-2024` passes with 0 errors in 263 s, and the conclusions match the new numbers. Nothing is committed.

**Outcomes.** All 26 stay as they were, and the verifier agreed with all 26 in round 1:
- `offline-bursts-above-shuffle`: reproduced, resting on reading (b).
- `fig5c-wake-overlap-neutral-coburst`: partially reproduced, resting on reading (b).
- `burst-locomotion-pause`: not reproduced.
- The other 23 are unchanged.

The two outcomes resting on reading (b) are the criterion's verdict, but both are fragile. The record now says so and adds a question for a reader about each.

**What I added or corrected:**
- **Burst-frequency reading (b) (B1):** I added a synthetic check. On cells with no bursts that share only a slow drift, reading (b) still passes (5.90 bursts/min against a surrogate 95th percentile of 2.60). Reading (a) fails (surrogate mean 8.55), which is the same pattern as the real data. On independent cells neither reading passes. So the reproduced result shows only that the cells co-vary. I removed my earlier claim that (b) was the better-supported reading and added a question to `questions/zaki-2024.yaml`.
- **Skew claim:** the same synthetic cells fail the skew test (skew −0.276 against a surrogate 95th percentile of 0.105). So that outcome is not an artefact of co-variation.
- **Quiet wake (B2, C3):** the file's sleep-state description defines quiet wake as a waking state. Scoring the week of telemetry the way the paper's Methods describe puts 64 of the 68 quiet-wake epochs in wake. Reading (a), which counts quiet wake as wake, is therefore the better match to the paper, and under it overlap-neutral co-bursting is below overlap-aversive. I added a question for a reader. I also corrected finding 2, which wrongly said quiet wake had no description, and lowered it from major to minor.
- **Locomotion clock (B3, B4, C1):** I aligned the telemetry to each recording's lag of peak correlation, which gives p = 0.805, 0.982 and 0.863. I also swept shifts from −8 to +8 s: no shift gives the result in all three recordings. A 1 s baseline window gives the same negative result. The notebook now prints the description of the movement signal.
- **Ca_EEG3-4 cell registration (C2):** the notebook now prints the processing modules of every file. The only cell-registration module in the dataset is in Ca_EEG2-1's Week file.
- **Two blocked claims, shown descriptively:** both stay blocked.
  - `ed9c-eeg-cohort-linking`: the low-shock mouse's neutral and novel recall freezing is printed.
  - `ed9-ed10-sleep-unchanged`: one mouse's 9.36 days of telemetry are now scored by the Methods' procedure. Time asleep is 47.81% in the 24 h before neutral encoding, 53.12% after it and 57.15% after aversive encoding. The scoring cannot settle REM (its REM bouts of about 10 s are not physiological).
- **New finding (9):** the offline files' session descriptions describe the one-hour webcam experiment, not the 10-minute home-cage recordings they hold.
- **Other record edits:**
  - A deviation on ed9b notes that its 30 s bins are autocorrelated.
  - Round 1 is recorded under `verifications`.
  - The README now includes these points and gives a runtime of about six minutes.

**Not done:** B4 (unequal window lengths), B5 (the claims are tested on different mice and a different movement measure than the paper's) and B6 (autocorrelated bins) come from the criterion, so I recorded them and left the criterion alone. C5, the amendment record, was only missing from what the verifier was given; it is in the questions file.
