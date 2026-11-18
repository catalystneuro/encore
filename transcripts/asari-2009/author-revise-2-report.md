I've finished the round-2 revision. No outcome changed, and I propose one change, for fig8a-proportion-by-property, for a third verification round. I re-ran the entry with `python tools/entry.py all entries/asari-2009`: the checks show 0 errors and both notebooks pass. Every number that was already recorded came out the same, and the new outputs match my development run exactly.

**Outcomes**
- **fig8a-proportion-by-property:** I agree with the verifier. The claims file says each property's probes follow Table 1's columns. The reading that matches Table 1 counts probes for amplitude, frequency and higher-order, and probe x ensemble entries for AM and FM. Under that reading the order AM > FM > higher-order fails (0.427, 0.354, 0.489), so the partial rule fails. The outcome stays partially reproduced as verified in round 1, with `proposed: not_reproduced`, its reason, and a new notebook cell that does the analysis. The notebook summary and README show the proposal.
- **The other 20 claims:** unchanged. The verifier agreed with all of them in round 2, and round 2 is recorded under `verifications` with its reasons and my responses.

**Added**
- **fig8c, trial resampling:** this reading now runs, with 200 resamples of trials within each probe and context, on its own random generator. Its resampled areas come out about three times too large (1.515 s against 0.520 s for natural sounds), and it fails the criterion for every population. The outcome stays partially reproduced.
- **Table 1 reading for the other fig8 claims:** now printed for fig8b, fig8c and fig8-natural-synthetic. None of their outcomes changes.
- **fig3b:** the fit before the swapped fragment lists are corrected is now computed and printed: 0.464 to 0.468 and 1.74 to 1.78 s. The notes and the finding now give these values in place of the unsupported "0.46 and 1.7 s".
- **fig9-example-first-bin:** the passing probes are now printed for each spike detector.
- **figs1:** all 22 early periods are printed, and 19 of them start within 0.1 s.

**Corrected**
- **fig4-strf:** the record and the STRF notebook now say the main reading departs from `STRFanalysis.m` in two places. It pools validation over folds, and it scores every window on the same samples. They also give the reason for not using the one combination that meets the criterion: it gives the LN model negative performance at every window (−0.112 to −0.198).
- **fig8 deviation text:** rewritten in all five fig8 claims. It now says which count gives which Table 1 total, and that higher-order matches under neither count.
- **Smaller text fixes:**
  - fig3a: the unbounded-fit numbers are now split by whether silence counts as a context.
  - fig3a Result cell: the constant is now described as fixed at the noise floor, not fitted.
  - fig9: the size is now given as 5.27 to 5.57.
  - README: the fig2-example-long-context row now names its assumption.
- **methods-recording-counts:** I removed the 0s recorded as measured values for the two voltage-clamp counts. The schema doesn't allow an empty entry, so the record has no measured list for this claim; the notes give the five counts that were measured.

**Not done**
- **Claims file `checks` section:** it doesn't record the amended fig2 criterion. I left it alone because the claims file belongs to the readers; the amendment is recorded with the answer in `questions/asari-2009.yaml`.
- **fig4-predictability (1 − Q):** this is still the open question for a reader; I added nothing.
- **Runtimes in `entry.yaml`:** they still say 22 and 23 minutes, but this run took 30 and 42. Editing the file would have made the clean run stale, so I left it.
- Nothing is committed.
