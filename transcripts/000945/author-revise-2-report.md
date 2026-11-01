No outcome changed. In round 2 the rules don't allow it, so all 22 stay as the round-1 verifier agreed them: 13 not reproduced, 7 blocked, 1 partially reproduced and 1 reproduced. The entry re-ran cleanly (`python tools/entry.py all`, 0 errors, notebook passes in about 90 s) and the numbers are the same as before.

**Proposed outcome changes, for round 3 to review.** I agree with the verifier on both claims it disputed. Each keeps its verified outcome (not reproduced) and carries a proposed change to blocked (data missing), with the reasoning in its notebook conclusion:
- **fig5e-rsu-delayed-prf-awake:** part (1) holds and part (2) fails, but part (3) needs the sham, which the dandiset lacks. If a sham held, the claim would be partially reproduced, so the data present don't decide the outcome.
- **fig7a-rsu-time-locked-dc:** part (2) fails. Parts (1) and (4) both need the missing 30% duty-cycle group, and part (3) needs the sham, so partially reproduced is still possible. The notebook now prints the Kruskal-Wallis p for every reading: 0.67 to 0.91 without a 30% group, 1.5e-22 or smaller with a substitute group.

The "Readings" cell now states the rule both follow: a claim is settled as not reproduced only when the tested parts rule out partial whatever the untested parts would show.

**Corrections in the notebook, README and record:**
- "Twelve files are second copies" is now eleven.
- The duplicates finding no longer says spike counts match in every pair. The third BH512 copy has different counts (905,554 against 926,883).
- "Four claims cannot be tested" is now three, with the claims named.
- The dates of the substitute 30% recordings are corrected in the fig7c notes, the data_missing finding and the notebook. Recordings from the same rats are three to five months before the duty-cycle recordings. The other rats' run from August 2023 to 6 March 2024, the last three to four days before the 9 March duty-cycle recordings.
- The README's missing comma is fixed.
- **delayed-anesthesia-factor:**
  - The deviation now says the Methods 2.3 sentence supports the one-recording-per-rat-and-condition assumption only weakly.
  - The notes and conclusion add the result with every recording kept and the doubly filed recording left out. The FSU p rises to 0.048 to 0.052, so with every recording the claim is partial at best.

**Round 2 is recorded under `verifications`:** all 22 claims, the verifier's reasons and my responses.

**Where I did not follow the verifier:** it said that variant would make the claim not reproduced. By the criterion it stays partially reproduced, because the RSU part holds on its own ("or when one cell type holds"). I recorded this in my response; it does not affect the adopted outcome.

**Not done:** nothing was added to `questions/000945.yaml`, because the verifier found no new place where the claims file misreads the paper. Nothing is committed.
