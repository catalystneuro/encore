No outcome changed and nothing is under `proposed`. The final run of `python tools/entry.py all entries/000223-xue-2022` passed with 0 check errors in 19.3 min. Its numbers are identical to the two runs before it.

**Why the numbers moved between runs.** Re-run unchanged on this machine, the notebook printed exactly the numbers the round-1 text was written from. The verifier's copy was executed on another runner. I found the likely cause in the burst detection: a burst ends where the smoothed spike count falls to an integer baseline. In every recording, many smoothed values equal that baseline up to rounding error (within 1e-9) but sit just above it, so the burst edges depended on the last bits of the arithmetic. `spineca.py` now rounds the smoothed counts to 9 decimals before the comparison. A new data-check cell counts these near-equal values per recording, and the change is recorded as a deviation. I could not get the verifier's executed copy, so I can't confirm the next runner will print the same numbers, but this one source of drift is gone.

**Effect on the outcomes, all recomputed after the fix:**
- **table1-best-r:** 17 of 20 match (was 18; row 14 now falls just short, 0.354 against a bound of 0.355). That is still partially reproduced. As the verifier said, the outcome does not rest on the row-to-file tie-break: the notebook now prints 16, 17 and 16 of 20 with the tied rows swapped. I removed `assumed` from this outcome.
- **fig5d (OUT/IN correlation):** With the Methods classification, R is 0.585 in region 0 and 0.582 in region 2, below the 0.605 bound, but 0.615 in region 1, inside it. So the outcome depends on the noise region again. I kept `assumed` and the region-0 deviation, and recorded my disagreement with the verifier's request to remove them.
- **All other outcomes** are unchanged. For example, 7 spines are accepted with 18 decisions agreeing in every region, and OUT/IN matches 6 of 19 recordings.

**Added or corrected:**
- Every conclusion cell, the Summary, the README and the record's notes and measured values are rewritten from the final run. This covers each sentence the verifier flagged.
- The verifier's note on row 10's background squares is now stated in the notebook and the notes: regions 0 and 2 sit on bright processes. Row 10's decision is the same with every square, and the 19-recording reading of fig5d, which leaves row 10 out, still gives R = 0.598 with region 0.
- The round-2 entry under `verifications` records, for each of the 13 claims, the verifier's reason in its words and my response.

**Not done:**
- No question was added to `questions/000223.yaml`, because the verifier found no place where the claims file misreads the paper.
- I kept the background-square rule unchanged despite the row 10 problem. It was fixed before any R was computed, and no outcome depends on it.
- Nothing was committed. `tools/runner/chain.sh` was already modified when I started, and I did not touch it.
