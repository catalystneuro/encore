I've revised the attempt for every point in the round-2 report. `python tools/entry.py all entries/crcns-hc-16-talbot-2018` passes with 0 errors and the notebook runs in 140 s. Nothing is committed.

**Outcomes:** none changed and none proposed. The verifier agreed with all 32, and round 2 is recorded under `verifications` with its reasons in its own words and my responses. One variant result does bear on an outcome:
- **fig4b-covariance-40-passes:** with the count pass rule and the code's 32 × 32 grid together, it meets its criterion (r 0.182 against 0.056, both within tolerance, p = 0.0004).
- I kept the verified outcome and did not propose a change. That result needs two choices the claims file does not make: the count rule, which is already asked of a reader, and the grid. Under the claims file's rule and maps the outcome stands.
- I added this result to the existing question in `questions/crcns-hc-16.yaml`.

**Added:**
- **Variants on more claims:** a new notebook section runs the refractory filter and the 32 × 32 grid on overdispersion-passes, overdispersion-cells, both fig4b claims and both Kendall claims (R2 only). Under the literal pass rule neither variant changes any of these results.
  - Under the count rule, overdispersion-passes on the grid gets variances and pass counts within tolerance, but Levene's test gives p = 0.052, so it still misses the criterion.
- **The p = 0.0004 shuffle:** each of the 100 permutations is now also run as a single-permutation test. Under the count rule at 30 passes, 4 of 100 give p < 0.05, as expected from a null. The draw the notebook reported happens to be the most extreme of the 100 (|t| 3.61, median 0.68), so it is chance, not a fault in the shuffle.
- **New question for a reader on figs4-remapping-similar:** the claims file says Table S2 lists box and arena sessions on different dates, but for M32 it lists a small box session on the same day as the arena sessions. The claim itself is unchanged, and its outcome (blocked, data missing) does not depend on this.

**Corrected:**
- **Interneuron conclusion and notes:** they now say only that the refractory filter does not remove the excess. It is a weak proxy for the paper's isolation measures, so whether poorly isolated clusters explain the excess cannot be told from these data.
- **fig4d:** the readings where WT is higher at five of six timescales are now named correctly (K2, H2, R1 and R2; Fmr1-null is higher at 1 s there).
- **figs6:** removed the leftover sentence saying reading B was adopted "as for fig5b". The conclusion, assumption and notes now say this claim settles a question that fig5b leaves open, and that under reading A it would not be reproduced.
- **Summary:** each variant's effect is now stated only for the claims it was run on, and the claims it was not run on are listed.
- **README:** the count rule changes overdispersion-passes in R2 only, and fig4b-covariance-40-passes only together with the grid.
- **Spatial-scale finding:** only M9, M10 and M11 are near 218 px; M1's extent is 188 × 207.
- **fig5b notes:** they now give reading A's values (0.084, 0.103) alongside the reading-B values in `measured`.

**Not done:**
- The two variants were not run on fig4d-network-state-recurrence, kendall-quiet-states, locomotion-similar or the rotating-arena claims. The Summary says so.
- No claim in the claims file was changed.
