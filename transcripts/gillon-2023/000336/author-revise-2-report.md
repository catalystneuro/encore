I answered every point in the round-2 report. No outcome changed and nothing is under `proposed`. The final run of `python tools/entry.py all entries/000336-gillon-2023` passed (0 errors). The main notebook took 11.3 min and the orderings notebook 18.9 min. Every conclusion matches the numbers that run printed. Nothing is committed.

**Outcomes:** all 18 are unchanged, and the verifier agreed with all 18. The one change to an outcome's marking is on inconsistent-event-fraction, which now has `assumed: true` as the verifier asked. It stays reproduced, but it rests on two assumptions, now written as deviations:
- durations are judged on the 1.5 s / 1 s sampling grid of the Methods;
- the block count is judged on its mean over sessions.

Without them the claim would not hold. I added a `methods_unavailable` finding asking the paper's authors about both, and the README and Summary say the outcome rests on assumptions.

**Added:**
- **fig8-ordering-variation, all 13 tracked mice.** The claims file asks for "each tracked mouse", so the notebook now also runs 411400 and 412933 on their sessions 4 to 6, and prints results for the 11 analysed mice and for all 13. With 13 mice the dendritic mean variation is still larger than the somatic under every reading (range over mean 0.104 at 10% and 0.134 at 20%, against 0.004). One added mouse, 412933, does not vary at all at 10%, so with 13 mice it is no longer true that every dendritic mouse varies more than every somatic one. The criterion only compares means, so the outcome holds.
- **Correlations checked against the paper's own code.** Cell 60 now runs the paper's own correlation function, `get_correlation`, through a new helper, `credassign.paper_get_correlation`. It matches our correlations on every pair of two sessions (105 and 20,910 pairs, largest difference under 3e-8). This answers the verifier's open point for fig7c and high-correlation-pairs.

**Corrected:**
- **fig8 text.** I rewrote the Result cell and the notes from the printed values and removed the corrupted fragment ("Xfiles'").
- **fig8 run-to-run difference.** This run's dendritic values do differ from the ones the verifier read: for 433448 the range over mean at 10% is 0.259 here against 0.309 in that run. Running the matching twice on one machine gave identical counts, so the difference seems to come from running on different machines. That repeat was done while preparing and is not in the notebook; the notes say so.
- **fig9.** The notes, the Result cell and my reader question in `questions/000336.yaml` now say that on the Gabor-only variant the criterion gives "partially reproduced", not "not reproduced". I also removed the sentence about a peak after the offset, which only the figure supported.
- **Dataset description.** I removed "mesoscope imaging" and "V1, LM, PM and AM" from the Summary and the notes, since no output shows them.
- **README timings** now match the run, and `entry.yaml` lists the main notebook at 11 minutes.

Round 2 is recorded under `verifications`, with the verifier's reasons in its own words and my response to each claim.

**Not done:** the max projection still stands in for the average projection the matching package expects, because the files contain no average projection. This is stated as a deviation.
