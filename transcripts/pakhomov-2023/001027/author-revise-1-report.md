I've handled the verifier's round-1 report. No outcome changed, because the verifier agreed with all 18: fig8a-equal-center-uptake, fig8a-more-uptake-near-electrodes and fig8b-packet2-best-targeting stay not reproduced, and the other 15 stay blocked because their data are not in the dataset. The last full run of `entry.py all` passed with 0 errors (346 s), the check passes, and I rebuilt the handover. Nothing is committed.

**Added to the notebook**
- **Per-dish profiles:** a new figure shows each dish's profile, raw and with its background subtracted. Each dish has its group's shape: every Protocol 3 dish peaks at the center, and every Protocol 2 dish is highest at the electrode ends. So no group difference comes from a single dish.
- **Reading (b), the region next to electrode e1:** the files don't say which electrode is e1, so I ran it with each electrode label as e1 in every dish, with the most favourable electrode chosen in each dish, and over all 1,048,576 ways of assigning e1 across the ten dishes.
  - fig8a-more-uptake-near-electrodes: no assignment gives reproduced or partially reproduced, in any reading.
  - fig8b-packet2-best-targeting: this goes further than the verifier's check, which looked only at the main raw reading. With the most favourable electrode picked in each dish, 27 of 64 readings meet the "partially reproduced" condition. All 27 use 92 regions per diagonal, where a single end region is narrow and noisy. Over all assignments, none gives reproduced, none gives partially reproduced with 46 regions per diagonal, and at most 1.5% do with 92. I kept the outcome, because the reading that can actually be run (reading (a)) decides it, and the notebook and record now say this.

**Corrected or stated more plainly** (notebook summary, README, attempt record)
- **Imaging day:** the fig8a-equal-center-uptake failure rests largely on the Packet 1 dishes, which were imaged on a different day with about twice the background. The files record no exposure or gain, so this can't be resolved.
- **Possible label swap:** the files labelled Protocol 2 and 3 behave like the paper's Packets 3 and 2. The data are tested as labelled, and the record now calls this unresolved.
- **Smaller points in the deviations and notes:**
  - The background is measured inside the electrode footprints, the only region where cells were not exposed.
  - When one region sits at the center, the outermost regions reach about half a step past the stated span.
  - Dish 10, which has different metadata, has a center value (382.7 a.u.) between the other two Protocol 3 dishes.
- **Round 1 recorded:** it is under `verifications` with the verifier's reasons and my responses.

**Not done**
- **Other dandisets:** the verifier found other dandisets from the same group (000875, 001025, 001028) that may hold the data for Figures 6, 7 and 9. I named them in the notes on those claims but did not analyse them, since they are outside the dataset the claims file names.
- **No reader question:** I added nothing to `questions/001027.yaml`, because the verifier found no place where the claims file misreads the paper.
- **Missing metadata:** nothing could be added on physical electrode identity, gain, exposure or a cell-free background region, because the files don't contain them.
