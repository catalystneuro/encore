The verifier agreed with the only proposal, so I applied it. Nothing is left proposed.

**Outcome changed**
- `fig6e-kinematics-predict-location` goes from `reproduced` to `partially_reproduced`, and the `proposed` block is removed. The reason: once the three unstable units are left out, M1-N's kernel value is 90.9% (SVD basis) and 91.2% (skew-normal basis), above the 62.1 to 89.1% range. No kernel reading then has every dataset in range, but the effect is above all 1000 permutations everywhere.
- The outcome now points to `reproduce_sabatini_2024_stable_units.ipynb`, which gives the values. The outcome's notes and units deviation say this. They also give the verifier's caveat: M1-N misses the bound by 1.8 to 2.1 points, and with all units every value is in range.
- No other outcome changed. The counts are now 10 reproduced, 13 partially reproduced and 11 not reproduced.

**Other updates**
- **Main notebook:** the fig6e result cell, the summary table and the paragraph on how the analysis differs from the paper's give the new outcome. I also corrected the header, which said "two units" where three are left out.
- **Stable-units notebook:** the header now says this claim's outcome is taken from it, and a result cell follows the fig6e claim cell.
- **README:** the counts and the stable-units paragraph are updated.
- **Attempt record:** round 3 is recorded under `verifications` with the verifier's reasons and my response.

**Re-run:** `python tools/entry.py all entries/sabatini-2024` finished with 0 errors and all three notebooks passed, taking 103 minutes in total. The fig6e values in the re-executed stable-units notebook are the same as before (0.909 and 0.912). Nothing is committed.
