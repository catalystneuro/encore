I've answered every point in the round-2 report. No outcome changed: one change is proposed for round 3, and one disagreement is kept on record. The entry was re-run with `python tools/entry.py all` after the notebook edits; it passed (about 31 minutes) and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **fig3d:** stays `reproduced`, with `partially_reproduced` written under `proposed`. The verifier is right: the Methods say each neuron is centred "by subtracting its mean response across the two windows". Under that centring monkey A holds and monkey M reverses (p = 7.3e-12), which the criterion calls partial. The analysis was already in the notebook; the conclusion and summary now say a change is proposed.
- **fig4g:** stays `partially_reproduced`, and the verifier's `not_reproduced` is recorded as a disagreement. The notebook now prints effect sizes to support this:

  | Monkey | Paired effect size (ours) | Paper's | t needed for p < 0.0001 | t observed |
  |---|---|---|---|---|
  | A | 3.78 | 0.90 | 11.2 | 9.26 |
  | M | 1.66 | 1.64 | 7.1 | 4.99 |

  The effect is in the paper's direction in every session and at least as large as the paper's. The test falls short only because the dandiset has 6 and 9 sessions, so the result does not differ from the paper's. I removed the `assumed` flag, since the verifier noted the outcome does not rest on the lapse range.
- **Every other outcome:** unchanged; the verifier agreed with all of them.

**Corrected**
- The re-run printed exactly the numbers the verifier read, so the run is deterministic.
- I rewrote the conclusions for fig2, fig2d, ed2c, ed4d, ed10, ed8, fig2e and fig2f, plus the bank-null check, from those printed outputs. The record's notes, deviations, round-1 responses and the classification finding now match too.
- Four `measured` fields were wrong and are fixed: fig2 (56, not 57), fig2e (-0.695), fig2f (-1.205, -1.495) and ed10 (203, 240).
- The two statements that were no longer true are fixed:
  - fig2e: monkey M is now described as 0.08 s outside the range, not "just outside".
  - fig2f: the text now says the code's window also puts monkey A's second peak in range.
- The round-2 verification is recorded for all 24 claims, with the verifier's reasons and my responses. The runtime in `entry.yaml` and the README is updated to 30 minutes.

**Not done**
- **fig4b, ed6d and ed5efg:** these are still blocked; I did not run the simulations. The protocol says a change that needs an analysis not yet run waits for a new attempt, and the responses say so.
- **`questions/000897.yaml`:** nothing added, because this round reported no place where the claims file misreads the paper.
