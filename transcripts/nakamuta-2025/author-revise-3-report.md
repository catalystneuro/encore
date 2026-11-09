One outcome changed and no proposals are left.

**Changed:** `fig3c-avalanches-emerge` goes from blocked (`metadata_insufficient`) to `not_reproduced`, and I removed `proposed`. The round-3 verifier agreed: none of the 56 readings meets both tolerances. Wherever the shift is reached, the exponent is 1.13 to 2.53, outside 1.35 to 1.65. Where the exponent is within tolerance, the median shift is never reached. So the missing DIV does not decide the claim.

**Wording narrowed as the verifier asked.** The text now says the result holds under reading (b) for any DIV offset. Under reading (a) it is shown only for offsets shared by all dishes and for the per-dish onsets O2 and O3; other per-dish offsets were not tried. They would change c under (a), but the shift there is at DIV 21 to 22, far from 15. I also added the verifier's claims-file note as a deviation on the claim: the exponent rests on the claims file's reading of a fitted formula lost from the paper.

**Also updated:**
- the claim's notes in the attempt record;
- the finding on missing days in vitro, which no longer lists the avalanche claim as blocked;
- the notebook's opening table, the fig3c heading and conclusion, and the summary;
- the entry README's table and prose.

Round 3 is recorded under `verifications` with the one result: agrees, `not_reproduced`, the verifier's reason, and my response. No other outcome changed.

**Checks:** `python tools/entry.py all entries/002020-nakamuta-2025` gave 0 errors, and the notebook ran in 408 s. The re-run prints the same numbers the text cites (77 of 112 pairs, c 1.13 to 2.53, the 14 pairs with an infinite shift). Nothing is committed.
