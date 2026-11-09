One outcome changed and no proposals are left open.

**Changed:** `flight-spatial-code` went from `partially_reproduced` to `not_reproduced`. The round-3 verifier agreed with the proposed change, so I removed the `proposed` block.
- **Why it changed:** after the position-lookup fix, the pre-specified run of 500 shuffles gives Rat1 12 of 25 units significant on flight day 9 (0.48). Rat2 gives 3 of 28, which is not above chance. That meets neither the reproduced rule nor the partially reproduced rule. The five repeats with 2000 shuffles agree.
- **Caveat kept in the record:** Rat1 sits right at the 0.5 bound. Across the seven runs it ranges from 11 to 13 of 25, and the single 13 comes from the least precise run, with 200 shuffles.

**Unchanged:** the other six claims keep their outcomes. The verifier only reviewed this one in round 3.

**Files updated:**
- In the notebook, the flight-spatial-code conclusion (cell 33) and the summary table (cell 51) now say not reproduced.
- The entry README's outcome table says the same.
- In the attempt record, the notes now say round 3 agreed with the change and that the pre-specified run decides the outcome. Round 3 is recorded under `verifications` with one result for flight-spatial-code: the verifier agreed, its outcome is `not_reproduced`, its reason is in its own words, and my response is included.

`python tools/entry.py all entries/001754-knierim-2000` passed with 0 errors. The notebook took 320 s, and its reported run time of 5.1 minutes still matches the README. Nothing is committed.
