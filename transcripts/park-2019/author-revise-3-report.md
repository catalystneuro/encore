One outcome changed, and no proposals are left open.

**Changed:** `figs3-no-head-direction-bias` goes from reproduced to not_reproduced, still marked `assumed: true`. The round 3 verifier agreed with the change, so I removed the `proposed` block.

The outcome now rests on reading (a) of the criterion, where n is the number of bins. Under that reading one of the 14 tests fails: 1121R157 in the room frame, p = 0.0134. The verifier noted that this single failure would not survive a Bonferroni correction across the 14 tests, but the criterion does not ask for one. The notebook conclusion and summary, the deviation, the notes and the README now say this.

**Still standing:** none. The verifier reviewed only this one proposal.

**Round 3 recorded:** I added it under `verifications` with one result for this claim. It records that the verifier agreed and would give not_reproduced, its reason in its own words, and my response.

**Added to `questions/park-2019.yaml`:** the verifier reported a possible misreading in the claims file. The paper reports p > 0.17, but the criterion uses the looser p ≥ 0.05. I added this as a question for a reader and left the claim unchanged. It does not affect the outcome, because the claim fails at either threshold.

**Checks:** `python tools/entry.py all entries/park-2019` passed, with 0 errors and the notebook executing in 131 s. Nothing is committed.
