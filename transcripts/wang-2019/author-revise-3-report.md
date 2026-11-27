One outcome changed, and no proposals are left open.

**Changed:** fig2a-rabbit-monotonic went from partially_reproduced to not_reproduced, and I removed its `proposed` block. This was the only claim with a proposal, and the round-3 verifier agreed with it. The reason is that the criterion has no partial result, and no combination of readings makes heart rate, APD80 and CaTD80 all monotonic and significant at 60 s.

**Text updates:**
- **Weak point now stated:** under reading (b), the outcome rests on one unadjusted step test of heart rate, at p = 0.047. Under reading (a), heart rate fails regardless, because 5 of its 9 steps go the wrong way. This is now in the claim notes, the notebook's result cell for fig2a (cell 25) and the entry README.
- **Summary row:** it now names heart rate as not monotonic under either reading and CaTD80 under reading (a) only, as the verifier asked.
- **README row:** it now gives not_reproduced.
- **Round 3 record:** added under `verifications` with one result for fig2a: agrees, outcome not_reproduced, the verifier's reasons, and my response.

No other outcomes changed. `python tools/entry.py all entries/wang-2019` passed with 0 errors. Nothing is committed.
