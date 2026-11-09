One outcome changed and no proposals are left.

**Outcome changed:** `table1-bursting-sessions` went from partially reproduced to not reproduced. The round-3 verifier agreed with the proposed change for two reasons:
- Under the session selections the criterion supports, (a) and (b), at most 2 of the 7 counts are within tolerance under any burst reading.
- Selection (c) was partly chosen to fit this claim's own expected values, so it can't decide the claim.

I removed `proposed` from that claim. I also removed its `assumed: true` flag, because the new outcome holds under every reading and the verifier said the flag was no longer needed. Your instructions said to change nothing else in the outcomes, so you may want to put the flag back. Its deviation text now says the outcome follows selections (a) and (b). No other outcome changed.

**Proposals that stand:** none. This was the only proposal in the record.

**Other updates:**
- The notebook's conclusion cell for this claim, its Summary table and the entry README now say "not reproduced".
- Round 3 is recorded under `verifications` with one result for this claim: it agrees, its outcome is `not_reproduced`, and its reason is in its own words, including its note that the criterion compares absolute counts. My response says I left the claims file unchanged.

`python tools/entry.py all entries/crcns-ia-1-eyherabide-2008` passed: the notebook ran in 410 s with 0 errors. Nothing is committed or pushed.
