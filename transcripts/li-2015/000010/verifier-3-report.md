**Verifier report, round 3: Li et al. 2015 (doi:10.1038/nature14178) on DANDI:000010 v0.220126.1905**

The attempt record proposes a change of outcome, under `proposed`, for one claim: imaging-selectivity-counts. No other claim in the record has a `proposed` entry.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| imaging-selectivity-counts | not_reproduced (recorded: partially_reproduced) | Yes | — | See below. |

**Reason for imaging-selectivity-counts**

1. **The numbers come from the data.**
   - Cell 60 runs all 16 readings in the claims file: response epoch (r1) 1.3 s or (r2) 1.5 s, span (a) or (b), rank (i) or (ii), and correct or all non-early trials.
   - It uses `alm.classify_plane`, which applies the test exactly as the criterion states it: a Kruskal-Wallis test on 5-frame bins at P < 0.01 in contra or ipsi trials, then a rank-sum test at P < 0.05 on the mean over epochs or on each epoch. Preference comes from the mean DF/F.
   - These counts are the same as in rounds 1 and 2:
     - Cells: 4,706 and planes: 59 in every reading.
     - Task-related cells: 2,551 to 2,772 with span (a), and 3,104 or 3,134 with span (b). The tolerance is 2,466 to 3,014.
     - Selective cells: 1,315 to 1,417 with the mean over epochs and span (a); 1,469 to 1,513 with the mean and span (b); 1,844 to 2,138 with each epoch. The tolerance is 1,417.5 to 1,732.5.
     - Contra fraction: 0.547 to 0.590.
   - Cell 60 prints "Readings with every value within tolerance: 0 of 16".
   - The new tally in cell 62 matches cell 60 row by row. I checked how many values are within tolerance and the selective miss for every row: 12 readings have four values within tolerance, and the selective count is within tolerance in 4.
   - It is true that the selective count fits only in the 4 readings with span (b) and the mean over epochs, and that the task-related count is above tolerance in exactly those readings (3,104 and 3,134, against an upper limit of 3,014).
2. **The outcome does not rest on a choice made to reach it.**
   - The only combination in which all values fall within tolerance is the F0 cut at 0.1 (cell 61): 1,419 selective cells under (1.5 s, a, mean, non-early).
   - That cut is a sensitivity check the author chose, not a reading in the claims file. Both the record and cell 63 say so, so it cannot decide the outcome.
   - With a cut at 0 the same reading gives 1,416, which is outside the tolerance again. The result sits on the edge either way.
3. **The criterion is applied as written.**
   - The claims file gives only one condition: "Reproduced when all values are within tolerance under one reading." It sets no partial condition.
   - No reading meets it, and the selective count is measured, and misses, in every reading. So partially_reproduced has no basis here. The units-classification precedent, where the missing class is one the dandiset does not hold, does not apply.
   - The proposal treats this claim the same way as fig2d-preparatory-perimovement, which is recorded as not_reproduced (attempt record, line 96).
   - My round-1 report gave not_reproduced, and so did my round-2 report, so the proposal's statement "Both verification rounds gave not_reproduced" is correct.

**Points that do not bear on the outcome**
- The record's `measured` values (4,706, 2,551, 1,315, 0.579, 59) come from reading (1.3 s, a, mean, correct). The notes call a different reading the closest: (1.5 s, a, mean, non-early), with 2,772, 1,417 and 0.588. The record does not say which reading `measured` reports.
- Cell 61 now prints how long each dip of the neuropil-corrected F at or below 0 lasts:
  - The longest run is 1 frame in 2,034 ROIs, 2 to 7 frames in 1,199, and 8 or more in 170, up to 518 frames.
  - This replaces the earlier "single frames" statement, which the record now says was wrong, and resolves my round-2 point 6.
- Early-lick trials still cannot be excluded, because the imaging files flag none. This is recorded as a deviation.

I found no place where the claims file misreads the paper for this claim.
