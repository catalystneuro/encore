I went through every point in the round-1 report and re-ran the entry with `python tools/entry.py all`. It passed in 29.6 min, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **Four claims now agree with the verifier:** fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling and figs8-halves-and-phase-order go from blocked to `not_reproduced`, marked as resting on an assumption. I applied each criterion with the threshold grid started at every value from 3 up to the top of its range (190 or 240 starts), and at four named starts: the paper's value of about 7, the 99th and 99.9th surrogate percentiles (6.51, 10.43), and the maximum over windows with at least 128 units. Every start fails under the CV readings (a) and (c). From 7, the scaling hit rate is 0.615 against 0.655 for no-scaling windows. Above 7, the non-natural image phase has 0.499 of windows, the active phase 0.311.
- **figs3-exponents-stable-with-threshold goes from blocked to `not_reproduced`**, although the verifier had agreed with blocked. Here the grid start does change the result: from 7 and from the 99th percentile it fails (non-natural image z departs by 0.083 against an SD of 0.058, and mu has no threshold with 10 sessions in two phases). From the 99.9th percentile only mu fails, which would be partially reproduced. I adopted the paper's value of about 7 (claims file, M4) as an assumption, and round 2 will review this change.
- All other outcomes are unchanged.

**Outputs added for the verifier's open checks**
- **Which windows set the surrogate maximum:** the largest surrogate value (34.29) comes from an ordinary window with 182 active units. Dropping windows with fewer than 64 or 128 units leaves it at 34.29. Only 13 of 28,335 surrogate windows lie above 15.
- **Correlation-matrix kurtosis** (z-scored counts, a new `kappa_z` column in `criticality.py`): surrogate minimum 4.09, median 15.88. It overlaps the real windows and does not recover the paper's reference of about 6 either.
- **Trial density:** counting aborted trials as failures gives a median of 5 trials per window, matching the paper's "three to five", but an overall hit rate of 0.236. The fig3c tests still fail under it.
- **mu fitted over ranks 1 to K/2:** 99.9% of windows now pass the r² rule, but mu is 1.06 against the paper's 0.73, so the exponent outcomes stay the same.
- Smaller fixes:
  - figs3 now evaluates every grid point, not every tenth.
  - fig4bc has a paired Wilcoxon test against the surrogates (p = 1.2e-17).
  - fig3d gives its largest gain restricted to thresholds with at least 30 trials on each side.

**Record and questions**
- `questions/cambrainha-2025.yaml` (new) asks a reader two things: whether O5 should count aborted trials, and whether O9 should fit mu over the upper ranks only. I did not change the claims.
- In `attempts/cambrainha-2025-01.yaml`, round 1 is recorded under `verifications` with the verifier's reasons and my responses. I updated the notes of the changed claims and the statements of four findings, keeping the findings in order. The notebook's conclusions, summary and README match the new numbers.

**Not done**
- No `findings` entry for round 1: none of the findings is rated critical, and that review only happens in round 2.
- No change to the 10⁴ Poisson bootstrap or to the 97-session analysis set; both are stated as deviations, and the verifier rated neither as affecting a conclusion.
- I could not compare against the paper's figures, because there is no PDF renderer here.
- `runtime_minutes: 30` in `entry.yaml` is left as it is, since the run took 29.6 min and editing the file would force another full run.
