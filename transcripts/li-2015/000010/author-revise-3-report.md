One outcome changed and no proposals are left standing.

**Outcome changed**
- **imaging-selectivity-counts** went from `partially_reproduced` to `not_reproduced`. This was the only proposal, and in round 3 the verifier agreed with it. I removed `proposed`. No `blocked_by` is needed because the claim isn't blocked. The claim's notes now give the reason for the change. They also name the reading the `measured` values come from (1.3 s, span a, mean over epochs, correct trials). The verifier said the record left this out, and the cell 60 output confirms that reading. Every other outcome is as it was.

**Other updates**
- **Notebook:** cell 63 now opens with "Result: not reproduced" and gives the reason in place of the proposal paragraph. The summary table and the methods paragraph of the summary are updated to match.
- **README:** the table row now reads "Not reproduced".
- **Attempt record:** the header comment now mentions the third round. Round 3 is recorded under `verifications` with one result for imaging-selectivity-counts: it agrees, outcome `not_reproduced`, the verifier's reason, and my response.

**Run:** `python tools/entry.py all entries/000010-li-2015` finished with 0 errors, and the notebook passed in 1062 s. Nothing is committed or pushed.
