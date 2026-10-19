**Round 2 verification: Hristova, Fasol et al. 2025 (doi:10.1111/epi.18606) on DANDI 001888 (draft)**

Counts are taken from the claims file and the attempt record. There are 34 claims: 13 reproduced, 9 partially reproduced, 2 not reproduced and 10 blocked (data_missing). Every claim id matches between the two files. I saved the paper text and Supplementary Methods text under `paper/`.

**1. Outcomes**

I agree with all 34 stated outcomes.
- **figs5b-transition-percent (reproduced):** I agree with the change. The Supplementary Methods use "the first 30 seconds (six epochs) prior … to assess SWD initiation in NREM and wake-NREM transitions". The Fig. S5B legend gives "SWDs in NREM" as the denominator. Reading (i) gives 22.93% (cell 86). The record and the claims file both say the criterion was corrected after round 1.
- **Borderline outcomes:**
  - fig3d-rem-hourly (p = 0.048) and fig3g-rem-total (p = 0.048) meet their criteria, though only just.
  - fig5f-swd-wake-correlation (R = −0.81) also meets its criterion. The Supplementary Methods support removing whole SWD epochs: "All epochs identified to contain SWDs were classed separately … the sleep quantification was adjusted accordingly".

**2. Sentences the outputs do not support**

- **Cell 33, and the disc-het-swd-minutes notes in the record:**
  - Cell 33 says: "Counting each epoch the scorer flags as 5 s of SWD gives 110.57 min, so the paper's number matches the event durations, not the flags."
  - The record says: "Counting flagged epochs as 5 s each gives 110.57 min."
  - Cell 32 computes the 110.57 from `A.swd_epochs`, and `A` is the "events" table. Cell 18 prints this same figure as "SWD epochs removed from the states 110.57". So it counts the epochs that SWD events overlap, not the flagged epochs.
  - The `flag6_epochs` column in cell 6 gives a Het mean of 722 flagged epochs per day, which is 60.2 min. That is within 59.97 ± 6.
  - So the paper's figure fits the flags as well as the event durations. The conclusion "not the flags" is contradicted. The outcome does not change.
- **Cell 78, and the fig4c-wake-power notes in the record:** they give the range "+0.0065 to +0.165". The largest value among the raw-EEG variants with both WT is +0.1683 (scorer flags, without 228), so the range should end at +0.168.
- **Cell 48, and the fig3d-rem-hourly notes in the record:** "The outcome holds only with all 16 rats." It also holds with GRIN2B-132 counted as Het: genotype p = 0.038, interaction p = 0.071.
- **Summary (cell 97), "How the analysis differs":** it lists what would change without GRIN2B-228 (fig5c, fig3d, fig3g-rem-total). It leaves out that fig5def-no-other-correlations would meet its criterion, since 0 of 8 tests have p < 0.05 (cells 92 and 93). It also leaves out that without GRIN2B-238 the fig3d interaction becomes significant (p = 0.0001, cell 47).
- **README:**
  - "about six minutes": the printed total run time is 206 s (cell 95).
  - "holds the 24-h … recordings": cell 4 shows 73 to 99 h recordings, each with two 24-h baseline windows.
  - The record's fig6b-systemic-etx-number note has the same error: "17 files are all 24-h baseline recordings".
- **Everything else matches the printed outputs.** That covers all other "Result" sentences, the rest of the Summary, the rest of the README, the record's other notes, and the findings, including the 21 to 73% bad-epoch range and the flags covering a median of 51%.
- **My round-1 reasons:** the record states them faithfully and in my own wording. Some B and C points are folded into the per-claim reasons: B3 into fig3i-wake-total and fig5def, B4 and B5 into fig4a, B9 into fig2c-swd-mean-duration, and C into fig2e. The eight blocked claims I grouped are split into one reason each. I found no misstatement.

**3. Round-1 points**

Resolved:
- **B1:** runs without 228, without 238 and without both are shown for every genotype test.
- **B2:** the figs5b criterion is corrected and disclosed.
- **B3:** SWD-time-only and unsplit-bout variants are added, and the dependence is stated in fig3i, fig5f and fig5def.
- **B4:** coverage per animal and state, the slope rule, and the cleaner-channel variant are added. The slope rule removes no epoch, which fits the Supplementary Methods thresholds (−5 for the slope, 500 mV² for the offset) given a steepest slope of −3.76 and at most 5.34 mV²/Hz at 1 Hz.
- **B5:** stated in cell 42.
- **B6:** MixedLM is added and gives the same genotype and interaction F.
- **B7:** the claims-file comment is corrected (U ≤ 1 gives p = 0.017 or 0.033).
- **B8:** cell 0 is corrected.
- **B9:** stated.
- **B10:** added to the findings.
- **All C items:** the 132-as-WT illustrations, reading (c) named as the main rule, the spectral checks, and MixedLM are all done.

Still bearing on a conclusion:
- **Which deposited rats the paper analysed:** this cannot be settled from the archive. fig3d and fig3g-rem-total drop to p = 0.060 without GRIN2B-228. fig5c and fig5def would become reproduced without it. Every two-WT comparison depends on GRIN2B-238.
- **Wake measures:** fig3i-wake-total, fig3i-wake-bouts, fig5f and fig5def depend on how SWD epochs are removed from wake. This is disclosed and follows the paper's method, but these outcomes are partly built in by that choice.
- **The sentence in cell 33 and the disc note:** they should be corrected to say that flagged epochs × 5 s give about 60.2 min. This changes the stated reasoning, not the outcome.
