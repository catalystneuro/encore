No outcome changed. The verifier agreed with all 32 outcomes, and every claim keeps its round-1 outcome. I re-ran the entry with `python tools/entry.py all entries/henry-2022` after the last change: both notebooks pass (34 and 39 minutes), the second run's numbers are identical to the first, and `check` reports 0 errors. Nothing is committed.

**Outcomes now marked as resting on an assumption**
- `fig5-terms-covary` and `fig5de-simulated-discriminability` stay reproduced but now carry `assumed: true`.
- On a neuron selection that does not depend on the stored epoch order (reliability averaged over 20 random half splits), V4's m and a correlate at only r = −0.459, below the criterion's 0.5. The simulated V4 slope is also at or below the measured one at only 1 of 4 spacings.
- Both outcomes therefore rest on the even/odd selection. That choice has support: single random half splits keep about as many neurons as the stored-order split (V4 238 against 244, V1 144 against 146). So the stored order does not explain the V4 excess over the paper's 198.
- The question is added to the `methods_unavailable` finding for the paper's authors.

**Outputs added at the verifier's request**
- **Blank epochs:** a per-session table of contrast values and blank, distractor-only and target means. The contrast parameters are 0 and 0.5 in every session, so only the counts mark the six problem sessions. The files cannot tell whether those epochs are mislabelled.
- **Random-split selection:** the tuning-model claims (`fig5bc`, `fit-quality`, `fig5-terms-covary`, `fig5-negative`, `fig5de`, `figs5`) re-run on it. Apart from the two above, the outcomes are the same.
- **Threshold elevation:**
  - The median and 5th to 95th percentiles of each permutation null are now printed. The nulls sit above 1: V1 medians are 1.37 to 1.63.
  - A no-crowding calibration shows the estimate is biased upward: 1.17 in V1 and 1.09 in V4 when the true value is 1.
  - Estimates on a grid up to 1000 show the main run is not censored by the old bound of 20.
- **Decoders:** the chosen penalties, and the share of folds where no coefficient is nonzero (5% to 18%), so the decoder predicts one class.
- **fig7cd:** d′ per population for the 18° pair, before averaging.
- **figs3:** re-run with 20 draws per size. It still passes at 7 of 8 area and spacing pairs.

**Corrections**
- `figs6` now states that its driven-fraction part covers only 10 of 22 populations per area.
- NaN null draws are now excluded from the modulation-index ranks and counted. There are none in V1 and at most 0.15% in V4, so no percentage changed.
- `figs5` judges "below 1" on the point slopes and still shows the upper-CI check.
- The text now says the two binomial trial-count readings give the same estimate.
- The "closer to 0" reading of the preferred orientation is stated, with its variant (slopes change by at most 0.022).
- The two dataset findings are updated with the new numbers.
- `entry.yaml` runtimes are updated, and round 1 is recorded under `verifications` with a response for each claim.

**Question for a reader:** I added `questions/henry-2022.yaml` on the `fig4a` far-spacing tolerance. A tolerance of 0.25 points is about one neuron out of 396, and each far value misses by exactly one neuron. The claim is still judged as written.

**Not changed**
- `fig2de` stays reproduced on the unrestricted V1 test, because the criterion explicitly allows either reading. Its notes now say the outcome rests on that reading.
- The three blocked claims stay blocked. The partial proxies the verifier describes are not the criterion's tests.
- The pseudo-population notebook no longer runs the permutation test on the recorded populations, which it did not use, to keep 20 draws within the 60-minute limit.
