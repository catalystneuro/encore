One outcome changed and no proposals remain open.

**Changed**
- **fig7g-model-prior-reconstruction** is now reproduced (it was partially reproduced). The verifier agreed with the round-2 proposal: the criterion names no partial outcome and its test passes as written. The rare-trained models give −0.098 bits and the frequent-trained models give +0.626 bits. Both signs are as expected, and both magnitudes are below the neural means of 0.223 and 1.125. The `proposed` block is removed.

**Still standing:** none. This was the only proposal, so the verifier disagreed with nothing.

**Updated**
- **Attempt record:** the fig7g notes now carry the verifier's caveat. The rare half of the comparison carries little evidence, because the rare neural mean has the wrong sign and the Methods formula gives an ideal rare observer +0.547.
- **Round 3 under `verifications`:** one result for fig7g, recording that the verifier agreed, its outcome (reproduced), its reason in its own words, and my response.
- **Notebook 2:** the fig7 and fig7g conclusion and the summary table now say reproduced, and the summary has a short paragraph on round 3.
- **README:** the table row now says reproduced, with a one-sentence version of the caveat.

**Re-run:** `python tools/entry.py all entries/plitt-2021` passed with 0 errors in 73 minutes. Notebook 1 took 3,106 s and notebook 2 took 1,291 s. The fig7g values in the new run are the same as those in the records, and `entry.py check` reports 0 errors. Nothing is committed.
