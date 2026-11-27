Round 3 is applied. The check reports 0 errors and the notebook runs clean with `python tools/entry.py all entries/wei-2023` (1754 s). Nothing is committed.

**Outcome changed**
- **figs3b-fs-faster** goes from partially reproduced to **not reproduced**, because the verifier agreed with the proposal. FS units fire faster under every reading, but the criterion only allows "reproduced" and no reading puts both medians within tolerance. `proposed` is removed, and the notes, notebook conclusion (cell 21) and summary table now give the new outcome.

**Proposal that stands**
- **figs5-depth-distribution** stays **not reproduced** (assumed), and its `proposed: partially_reproduced` is kept. The verifier disagreed with "partially reproduced" but would give **reproduced** (assumed), not "not reproduced":
  - With the depth method the criterion names and the attempt's own clusters (reading c), the test gives p = 0.044, which meets "p < 0.05".
  - The criterion has no partial clause, which is the same reason used for figs3b.
  - It also called the result fragile, since it rests on forcing FS to three clusters and on a depth reference that is not validated.

  Its view is added to the proposal's reason and to the notes, notebook conclusion (cell 42) and summary table.
- The verifier also pointed out that a second depth reference the helper computes (`depth_csd_min`) is never tested. I did not run that test: the protocol leaves a change that needs a new analysis to a new attempt, and the round-3 response says so.

Round 3 is recorded under `verifications` with one result per reviewed claim (figs3b agrees; figs5 disagrees and would give reproduced). The entry README states no outcomes, so it did not need changing.
