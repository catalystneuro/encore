No outcome changed and I proposed none. The verifier agreed with all 29 outcomes in round 2, and I recorded that round under `verifications` in `attempts/crcns-ofc-4-schuck-2016-01.yaml`. The final `python tools/entry.py all entries/crcns-ofc-4-schuck-2016` run passed (check: 0 errors; notebook ran in 5.1 min), and the conclusions match its numbers.

**New output (verifier point 5).** The verifier suggested that correct Enter trials score 0.90% (voxel z-scoring) because the scan still shows the previous Exit trial. I added a data-check cell to test this, and the numbers don't support it:
- At the volume used, Enter trials are decoded as the previous Exit state on 10.78% of volumes. That is the same as how often the classifier names that state on any labelled trial (10.90%, t = −0.20).
- The only excess is at stimulus onset (lag 0, t = 3.12).
- The real cause is a bias: with maps z-scored by voxel, the classifier names an Enter state on only 5.60% of labelled volumes, against the 50% expected without bias (56.74% with maps z-scored by map).

So under voxel z-scoring, the three fig4b error-trial comparisons measure this bias, not lag. All three were already not reproduced, so their outcomes stand. The fig4b conclusions now mention the bias.

**Corrections:**
- **supp-errors-stable-over-blocks** is now marked `assumed: true` (one error per block). This is updated in the record, the summary table and the README.
- **fig4b-error-vs-matched:** the conclusion, notes and deviation now say:
  - the paper's matched courses having the same class mix is our inference; the Figure 4B legend only says "seven consecutive trials with no behavioral error";
  - with voxel z-scoring, the class-matched comparison (c) is at floor and could not show a drop;
  - the deciding evidence is the map z-scoring, where Enter trials score 8.02% and error trials are not lower (p ≥ 0.69 under the criterion's readings, p ≥ 0.45 under (c)).
- **Stale numbers** fixed to match the printed outputs, in the notebook, the record notes and the affected round-1 responses:
  - figs2c: 14.79%, p = 0.025, components p = 0.20 to 0.44.
  - fig4b-decline: smallest p = 0.32; slope 1.47, p = 0.039.
  - figs5: partial r 0.072, p = 0.22 and 0.076, p = 0.18; the strict reading is 39 errors in 35 participant-transitions from 16 participants.
  - Errors by trial class: Exit and Internal together are 0.60%. The 1.18% and 1.20% figures are now given only as the most either class could reach with all 44 unknown errors.
  - Designed trials per error block: 0.52 extra after an Exit trial, 0.87 otherwise.
  - fig2b: previous category is stronger under one reading of how the data set coded error trials (O3 a) with map z-scoring (p = 0.013 against 0.038).
  - Summary: 181 of 228 error blocks.
- **Wording:** the README and summary now say Enter trials decode worse only with voxel z-scoring. The README runtime now reads about five minutes, and `entry.yaml` has `runtime_minutes: 6`.

**Not done:**
- I added no questions to `questions/crcns-ofc-4.yaml`, because the report found no new place where the claims file misreads the paper.
- I left the claims file unchanged, as instructed.
- I did not commit, as instructed.
