# Round 3 verifier report: sabatini-2024-01

The attempt record has 34 outcomes and the claims file has 34 claims. Only one outcome carries a `proposed` block: fig6e-kinematics-predict-location, at line 695 of the attempt record. The record's round-2 response points to the same single proposal (line 1554).

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig6e-kinematics-predict-location | partially_reproduced | Yes | — | See below. |

## Reason

**The numbers come from the data.**
- Stable-units notebook, cell 74. M1-N's OU kernel value is 0.909 under the SVD basis, and 0.892–0.896 under the four other seeds. Under the skew-normal basis it is 0.912, and 0.893–0.898 under the other seeds. All are above the claims file's upper bound of 89.1%.
- In the same cell, the other 15 values stay in range:
  - every linear value lies in 33.3–78.1% (0.384–0.715);
  - every other OU value lies in 62.1–89.1%;
  - every real value is above all 1000 permutations (p = 0.001).
- The Gaussian kernel is below the range in every dataset (0.321–0.554).
- Main notebook, cell 99: with all units, M1-N's OU value is 0.887 (SVD basis) and 0.891 (skew-normal), just inside the bound.
- The figures in the proposal (90.9, 91.2, 89.2–90.9, 89.3–91.2) match these outputs.

**The unit exclusion was not chosen to reach the result.**
- Stable-units cell 11 sets the rule before any claim cell runs. It drops units whose block rate ratio is above 5, plus units whose spike train is split across two rows.
- Unit 170 (M1, monkey N) has a ratio of 13.69. The next largest is 2.53 and the median is 1.14.
- Unit 170 averages 175 spikes/s in segment 3, with 229 of 532 trials above 100 spikes/s. In the other segments it averages 28–40 spikes/s, with no trials above 100.
- Dropping it explains the segment-3 anomaly I raised in round 2. Decoding within segment 3 goes from 0.179 (main notebook, cell 9) to 0.425 (stable-units cell 11).
- The paper says "Both single-units and stable multi-units were included for analysis" (Methods). A unit that changes its rate several-fold partway through one recording is not a stable unit, so the stable-units set is closer to the paper's method.
- The change moves the outcome away from the author's earlier `reproduced`, so it is not a choice made to get a favourable result.
- Units 0 and 1 of monkey J are PMd, so they do not affect M1-N. M1-N goes from 96 to 95 units (stable-units cell 13).

**The criterion is applied as written.** The claims file says "Reproduced when, under one reading, every dataset's linear value lies in 33.3 to 78.1% and kernel value in 62.1 to 89.1%".
- Without the unstable units, neither kernel reading passes for every dataset:
  - the OU kernel fails on M1-N under both kinematic bases;
  - the Gaussian kernel fails on all four datasets.
- The effect itself holds everywhere: both models are above chance in every dataset, and the linear values are in range. So `partially_reproduced` fits.

## Caveats (they do not change my agreement)

- **Small margin.** M1-N misses by 1.8–2.1 points, and in the direction of a stronger effect. The range of 62.1–89.1% is itself a tolerance around the paper's 69–81%. With all units, M1-N sits 0.2–0.4 points inside the bound. The outcome depends on a 1–2 point difference near the bound.
- **Records that would need updating if the change is accepted.** These are bookkeeping fixes; I am reporting them, not correcting them.
  - The outcome's `notebook` and `output` fields name the main notebook, whose cell 99 gives the in-range values. They would need to point to `reproduce_sabatini_2024_stable_units.ipynb`, cell 74.
  - Stable-units cell 0 says "The conclusions, and the outcomes, are in the main notebook". That would no longer be true for this claim.
  - The README says only that the record proposes a change for this claim.
- **No misreading of the paper found** in this claim's criterion.
