No outcomes changed. The verifier agreed with all 39 in round 2 and asked for no proposed changes, so none were made. The counts stay at 20 reproduced (lab-link included), 13 partially reproduced, 5 not reproduced and 1 blocked.

**Corrections (wording only):**
- **fig5dg and fig5s2-glm-accuracy:** cells 116 and 119 and both claims' notes in the record now say the criterion *allows* a match under one reading. They no longer say fig5cf-glm-weights matched.
- **fig2s2:** cell 34 and the record now say both means are within tolerance under *every* reading, not "most". The new output confirms this for all 20 rows.
- **fig2bc:** cell 28 now says the early bias range is shifted to the left and the later one is wider than the paper's, with its upper bound above it.
- **fig3s3:** I removed the sentence about an unrecorded run of 100 subsamples.
- **Wheel finding:** I dropped "the timestamps are not monotonic". No output shows it, because the helper returns on the length mismatch before checking order.
- **Loading time:** the README and cells 0 and 2 now say "three to four minutes", not "about six". Cell 3 printed 3.4 minutes in the reviewed run and 3.6 in the re-run.
- **session-end-criteria:** the record now says the per-day count of 5,683 of 6,435 includes the 90-minute rule. It also says the outcome is decided on the per-session count, and the outcome is the same either way.
- **Round-1 record:** a note now says its cell numbers refer to the round-1 notebook.

**Re-run:** `python tools/entry.py all entries/000045-ibl-2021` passed in 1607 s, and `check` reports 0 errors. I compared the numbers in the conclusion cells against the new outputs. Every one that differed from the printed text was a rounding, a different number format, or a value quoted from the paper or a tolerance.

**Record:** I added round 2 under `verifications`, covering all 39 claims, each marked as agreeing with the verifier's outcome. Reasons follow the report's wording, and each `response` says what changed. The points that belong to no claim (loading time, round-1 cell numbers) are noted in the round's `reviewed` field.

**Not done:**
- The Random Forest still runs 50 of the criterion's 2000 subsamples, because the full run would take about 122 minutes. The verifier accepted this as a disclosed deviation.
- Nothing is committed, as instructed.
