The verifier agreed with all three proposed changes, so I applied all three and no proposals are left open.

**Outcomes changed:**
- `fig3e-phase-peak-index`: partially_reproduced → blocked (methods_underspecified)
- `fig3d-saddle-phase-plane`: partially_reproduced → blocked (methods_underspecified), because its criterion takes fig3e's outcome
- `fig4i-peak-index-ais-distance-real`: not_reproduced → blocked (methods_underspecified)

**Other edits:**
- **`proposed` and `assumed` removed:** I removed `proposed` from all three. I also had to remove `assumed: true` from them, because the schema does not allow it on a blocked outcome, and the round-3 record says so. No other outcomes changed.
- **Notes:** the fig3e notes now carry the verifier's caveats:
  - The drop under noise holds only for the slow-rising AP; the fast AP still scores 0.666 and 0.698 at 0.02 and 0.03 mV.
  - The index does not correlate with noise among shoulder-branch cells (Spearman 0.07).
  - The 0.30 mV noise in the HEKA files is above the 0.1 mV the synthetic test reaches.
  - The p = 0.54 comes from groups of 1 to 10 cells, so it has little power.
  - Blocking goes beyond the letter of the criterion, and a reader should confirm it.
- **fig4i notes:** these now say that none of the 62 values in the mat file is in the per-cell tables, so the hand-read result does not decide the claim either.
- **Notebook, README and record:** the notebook's result cells and summary and the entry README now give the blocked outcomes and the caveat. The summary now says two outcomes rest on assumptions instead of three. Round 3 is recorded under `verifications`, with the verifier's agreement, outcome and reasons in its own words for all three claims.

`python tools/entry.py all entries/001746-liu-2026` gave 0 errors, and the notebook re-ran in 319 s. The numbers I checked in the new executed copy match the record. Nothing is committed.
