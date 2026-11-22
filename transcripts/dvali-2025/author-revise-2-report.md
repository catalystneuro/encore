None of the 39 outcomes changed and none is proposed. The re-run passes (`python tools/entry.py all entries/dvali-2025`: 0 errors, 8.2 min), the attempt record validates against the schema, and nothing is committed.

**Corrected after the verifier's points**
- **anatomy-network-properties:** the record and cell 33 now say all four values fall outside tolerance under the White N2U variant (density 0.0823 is below the 0.0828 lower bound), not three of four.
- **fig5a-signaling-rich-club:** the record and cell 54 now say that with 100 rewired networks the local maxima also include k = 1.
- **ed6-signaling-not-feedforward:** the table for the other four seeds now prints the fraction measure as well as the count measure. No leg is above the null for either measure under any seed. The smallest p for the fraction measure is 0.0011 to 0.0020, always for values below the null. The record's 0.0149 is corrected to 0.0148.
- **Edge-swap port:** draws that the original skips (same source twice, a source with no successors, same target) no longer count towards `max_tries`, matching the original. The notebook now prints how many swaps each null network got, and every one got its full count.
- **ed6-anatomy-feedforward:** now marked `assumed: true`, with its criterion recorded as an assumption, because the claims file gives it none.
- **Round-1 entry:** it now says the verifier's report named no misreading, not that the verifier "found" none.

**One more error, found while checking the port.** The paper's code calls the edge swap with 6000 swaps and up to 9000 attempts for the anatomical network (`SIM_doubleedge.py` line 493). The notebook had used the signaling network's 2000 and 4000. It now uses 6000 and 9000. The new edge-swap results are:
- **Anatomy:** z = 0.45, 0.60 and 8.31 (previously 0.35, 0.58 and 6.61).
- **Signaling:** p = 0.062, 0.55 and 0.74.

The same four of six tests are significant under all five seeds and under the variants, so both outcomes stand.

**Recorded:** round 2 is under `verifications`, with all 39 claims agreed, the verifier's reasons in its own words, and my responses. No finding is rated critical, so there was nothing to review under the round's `findings`.

**Not done, and why**
- **README runtime:** I kept "about eight minutes". The verifier saw 5.1 min, but the larger anatomical edge swap brings the run to 8.2 min, so the line is now right.
- **Round-1 fig5c response:** left as is. It answers a point the verifier did not raise, but the verifier called it harmless.
- **Questions file:** no question added to `questions/dvali-2025.yaml`. The verifier found no place where the claims file misreads the paper.
- **The one-SD rule in fig5a:** left as is. The verifier said it is degenerate at small k, but called it the claims file's choice and did not report it as a misreading.
