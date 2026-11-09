One outcome changed: **fig3d-distal-first-bap** went from `reproduced` to `blocked` (`methods_underspecified`). The verifier agreed with the proposal, and it was the only one this round, so no proposals are left standing. The re-run passed: `python tools/entry.py all entries/001266-park-2025` finished with 0 check errors and both notebooks ran (about 27 and 35 minutes). The re-executed table gives the same counts: at 5 s.d., file D4 has 84 bAPs, and the first bAP carries a dSpike in 32 (median filter) and 31 (Butterworth) of 54 trials.

The record now has 7 reproduced, 14 not reproduced and 34 blocked outcomes.

What I changed:
- **Attempt record:** I set the new outcome and removed `proposed`. The notes now give the 5 s.d. counts the outcome rests on and say the Butterworth count is one trial outside the tolerance. `measured` changed from 33 to 32, the median-filter count at 5 s.d.
- **`assumed: true` removed:** `tools/entry.py check` rejects that flag on a blocked outcome, so it had to go. The deviations are unchanged.
- **Round 3:** recorded under `verifications` with one result (agrees: true, blocked), the verifier's reason in its words, and my response.
- **Notebook and README:** the fig3d conclusion cell, the summary table row and the summary paragraph on thresholds now match. The README's table row says "Blocked: methods underspecified", and its prose now says 4 s.d. is assumed only for the soma and D4+soma files.

The verifier also flagged two places where the claims file may misread the paper. The first, whether the somatic threshold "cannot change the outcome", is already asked in `questions/001266.yaml`. I did not add the second as a question: it is about how this attempt applied the criterion, not about the paper, and the verifier says it changes nothing here. The round-3 response records this.

Nothing is committed. The changes to `tools/build_site.py` and `tools/site_assets/` were there before this run, and I left them alone.
