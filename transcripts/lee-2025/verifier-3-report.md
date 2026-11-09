# Round 3 verification report: fig6no-cea-clusters

The attempt record (`001195-lee-2025-01.yaml`) proposes one change of outcome, on one of its 38 claims. The claims file also has 38 claims.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig6no-cea-clusters | not_reproduced | Yes | — | The claim passes only if every cell in the late-firing cluster is excited. That part fails in all 16 readings the criterion asks for, and the readings agree, so no reading gives a passing result. The criterion has no partial clause, unlike fig6pq, so the verified "partially reproduced" does not follow from it. Details below. |

## Checks on the analysis (cell 31, with the result in cell 32)

**The numbers come from the data.**
- Cell 31 clusters the cells for each combination of ramp ratio (absolute or from deflections) and sag steady state (100 or 200 ms). It then labels the cells at each detection threshold (k = 2, 3, 5 SD) and each IEI reading (a, b), and prints all 24 rows.
- The k = 2 and 3 rows are the 16 readings the criterion asks for. In every one of them the late-firing cluster has 17 or 18 cells: 11 to 13 excited, 2 or 3 inhibited, and 3 with no response data.
- The regular-firing cluster has 6 of its 9 or 10 cells inhibited, which is more than half.
- Summed over the readings at each k:
  - "late_all_excited" holds in 0 of 8 at each of k = 2, 3 and 5.
  - "regular_over_half_inhibited" holds in 8, 8 and 0 of 8 for k = 2, 3 and 5.
- The per-cell table names the inhibited late-firing cells:
  - C20 is a mix with a negative area of −0.286 mV·s.
  - C53 is labelled inhibited from its IEI.
  - C41 is a mix at 2 SD only.
- The cell 32 text and the record's notes and reason match these printed counts.

**The outcome was not steered.**
- The change makes the outcome harsher, and it is the outcome I gave in rounds 1 and 2.
- The labels follow the rule in the criterion: IEI first, then EPSP or IPSP, then the sign of the area for mixes.
- The proposal does not depend on which reading is chosen. Even if the 3 cells with no data were left out, the 2 or 3 inhibited late-firing cells would still fail the "every cell excited" condition.

**The criterion is applied as written.**
- Proportions are taken over all cells in each cluster, as the criterion specifies.
- The readings agree, so the criterion's "blocked if the readings disagree" clause does not apply.
- The cell count gives a second, separate failure. All readings cluster 27 cells, against an expected 26 with tolerance 0, and the cell prints "cells clustered: [27] (expected 26)".
- The 5 SD labels are only a variant. They also fail: 1 inhibited late-firing cell, and 3 of 9 or 10 regular-firing cells inhibited.

## Possible misreading in the claims file (reported, not corrected)

- The paper says only that the late-firing cells were "excited" (Results, paragraph 3: "cluster 1 'late-firing' neurons excited", Figure 6O). The claims file turns this into "every cell of the late-firing cluster is excited", while it counts proportions over all cells, including those with no response.
- If the Figure 6O pie for cluster 1 contains cells that were not excited, the requirement is stricter than the paper. I could not check this because the PDF figures cannot be rendered here (poppler is not installed).
- The outcome stays "not reproduced" under the criterion as written.
