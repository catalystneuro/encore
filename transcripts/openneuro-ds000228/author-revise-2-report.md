I've handled the round-2 report. No outcome changed, and nothing is under `proposed`. I re-ran the entry twice with `tools/entry.py all`; both runs passed with the same numbers as before, and `tools/entry.py check` reports 0 errors.

**Outcomes**
- **rc-overlap (the one disagreement):** I kept partially reproduced and recorded the verifier's not_reproduced. The claim's test holds (less overlap than chance, p ≤ .01); only the expected count misses (0 overlapping timepoints against the paper's 1). Rule S in the claims file and the protocol both call that partial. The verifier's comparison with irc-williams doesn't carry over: there two of the paper's tests fail. This reasoning is now in the result cell and the claim's notes.
- **The other 41:** the verifier agreed, so they stand as they were.

**Text corrected to match the printed numbers**
- **irc-adult-vs-child** (cell 55 and notes): within-ToM t = -6.23 under one reading (O2a with O3b) is inside tolerance. The other within-ToM values, and all within-Pain and across values, are outside.
- **irc-adult notes:** I weakened the shared-signal claim. That variant moves the across-network value in the paper's direction, but it also pushes both within-network values below the paper's.
- **Summary cell:** it no longer says every behavioural number is recovered "exactly". The counts match exactly and the other values are within tolerance, with examples. beh-fb-tom holds only under reading (a).
- **Summary, README and the first finding:** the "higher within networks" statement now applies to adults only. They add that 3-year-old within-Pain is lower than the paper's (.179 against .23; non-bilateral .146 against .17).
- **README run time:** it now gives the times the tool reported, 146 s and 183 s.

**Added**
- **maturity-across:** within-ToM is significant under O2b with O3b (p = .049).
- **rc-3yo-events:** a deviation and the result cell now say that using the best-matching rc-events reading (O5a) extends the criterion.
- **Round-1 record:** for replication-sample, it now says the verifier gave `data_missing`.
- **Round 2 under `verifications`:** one entry per claim, with the verifier's reasons in its words and my responses.

**Not done**
- No question was added to `questions/openneuro-ds000228.yaml`, because the verifier found no misreading in the claims file.
- The unexplained offset in the inter-region correlations and the per-participant artifact check against the ART thresholds stay open. Both are already recorded, and neither can be settled within this attempt.
- Nothing is committed.
