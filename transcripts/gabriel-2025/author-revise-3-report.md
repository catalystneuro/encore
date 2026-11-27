Round 3 is applied: one outcome changed and one proposal stands. The entry check gives 0 errors, and the full run with `python tools/entry.py all entries/gabriel-2025` passed. It took 3525 s, close to the 60-minute limit. The figures I quote in the text match the new outputs of cells 57, 72 and 73.

**Outcome changed**
- `figs2-innate-behaviors` goes from `blocked` (`not_runnable`) to `not_reproduced`. The verifier agreed: the criterion needs all of its parts to hold, and the escape-excited part fails on day 1 in all 24 runs (p = 0.397 to 0.993). The claim therefore fails whatever the untestable jumping part would give. I removed `blocked_by` and `proposed`.

**Proposal stands, outcome kept**
- `fig3a-decoding-shock-gt-ns` stays `reproduced` (assumed C1 N1 and the clock tone windows). The verifier did not agree with `partially_reproduced`:
  - The criterion as written is met in all three cohorts.
  - The shuffled-label control is not in the criterion, and the paper reports no such control.
  - Under C1 N1 with all mice the control also fails for the shock epoch (p = 0.054), and citing C2 N1 to keep that part mixes readings.
  - The control is weak: 5 permutations per mouse, and 5 of 16 mice score 0 in every epoch.

  `proposed` remains, with the verifier's view added to its reason. The notes now give the control as a caveat outside the criterion, using the verifier's figures.

**Other edits**
- The notebook's result cells 58 and 74, the summary table and the intro table now match these outcomes.
- The entry README's table rows for both claims are updated.
- Round 3 is recorded under `verifications` in the attempt record, with one result per claim reviewed: `agrees`, the verifier's outcome, its reason in its own words, and my response.

Nothing is committed.
