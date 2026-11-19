The verifier agreed with the one proposal, so one outcome changed. No proposals are left.

**Outcome changed**
- **fig3b-fractional-power-decay**: changed from `not_reproduced` to `partially_reproduced`, and the `proposed` block is removed. The reason is that it now matches how fig4-predictability-upper-bound is graded. In both claims the size is within tolerance (alpha1 0.457 to 0.464 in all 4 readings that count silence), but the time constant is not (1.50 to 2.01 s, against 1.04 s).
- I added the verifier's caveat to the claim's notes, the notebook's result cell and the summary. What holds is the size from about 0.49 and a decay lasting seconds, far beyond the 71-ms noise autocorrelation. The paper's "long decay constant of about one second" does not hold as a value.

**Proposals still standing:** none. No other outcome changed.

**Other changes**
- **Notebook:** the outcome table in cell 0 and the summary now read "partially reproduced", without the proposal wording. Cell 38 now sets the two claims side by side and says round 3 agreed.
- **Entry README:** unchanged, because it lists no outcomes.
- **Record:** round 3 is added under `verifications` with one result for fig3b-fractional-power-decay: it agrees, gives `partially_reproduced`, and has the verifier's reason and my response.

**Run:** `python tools/entry.py all entries/asari-2009` passed, with 0 check errors. `reproduce_asari_2009.ipynb` took 2953 s and `strf_wehr.ipynb` 960 s. The executed fig3b output matches the numbers in the text. Nothing is committed.
