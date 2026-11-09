All 35 outcomes are unchanged and still `reproduced`. Nothing needed a `proposed` change. I re-ran the entry with `python tools/entry.py all entries/crcns-pfc-1-rodgers-2014` (it passes in about 190 s), `check` reports 0 errors, and every corrected sentence matches the new outputs. Nothing is committed.

**fig5ab-single-unit-onset (the verifier's main point).** This outcome is now marked `assumed: true`. The assumption, stated in a new deviation, is that the median is taken over all rule-encoding units, including the 7 mPFC and 2 A1 units that have no significant interval containing the bin just before onset. The paper's wording ("the median rule-encoding unit") and the counts in Figure 5C (n = 76 and 36) support that reading.
- Cell 64 now prints those nine units' onsets and a new variant that counts them as having no preference before the stimulus (onset 0).
- The results under the three readings:

| Reading | A1 median (expected 0.55 ± 0.05) | mPFC median (expected 0.625 ± 0.05) |
|---|---|---|
| Kept, as the code does | 0.550 s | 0.625 s |
| Kept, with onset 0 | 0.550 s | 0.600 s |
| Left out | 0.650 s (fails) | 0.650 s |

- Only leaving them out fails. The notebook conclusion, record notes, summary and README now say so.
- I added a `methods_unavailable` finding that asks the paper's authors how these units count.
- I added a question to `questions/crcns-pfc-1.yaml` asking a reader to settle the criterion's wording. The claim itself is unchanged.

**Sentences the numbers did not support, now corrected:**
- **Cell 33 and the fig3c notes:** under reading (b), all of 81, 37 and 44 are within tolerance (44 is at the edge), so the claim holds under both readings.
- **Cell 19:** 54 sessions were tested (the catch-trial session is left out) and all 54 pass.
- **Cell 123 and the fig8 notes:** the low values are now described as performance, not task signals. Below a task signal of 0.3 times the noise, task 1 runs from about 0.63 to 0.988 (the 0.988 is at gain 1.194).
- **Cell 111:** in mPFC a reduction of about half is not excluded; in A1 even a complete loss is not excluded (0.442 against 0.401).
- **Summary and the `selection_undocumented` finding:** the difference in auditory responsiveness is now attributed partly to the code table's unstated classes and partly to the threshold and trial choices of the recomputation (6 units the table calls "nothing" become responsive, 13 it counts as responsive do not).
- **README:** the list of outcomes that rest on the code's choices now includes fig5ab's dependence on keeping those units.

**Round 2 under `verifications`.** All 35 claims are recorded as agreeing, with the verifier's reasons and my responses.
- I recorded fig5ab as agreeing (`agrees: true`) even though the verifier's agreement was conditional ("only under a reading the record does not mark as assumed"). That condition is quoted in the reason.
- The verifier's round-1 reason for fig3c contains the same arithmetic mistake. I left it as the verifier gave it.

I did not do two things. I did not read the code's scripts beyond what round 1 had used, because the report asked for no new analysis that needed them. I did not change any claim's statement, expected values or criterion.
