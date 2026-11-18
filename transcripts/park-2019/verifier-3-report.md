I agree with the one proposed change.

There are 22 claims in the claims file (`park-2019.yaml`) and 22 outcomes in the attempt record (`park-2019-01.yaml`). Only one outcome has a `proposed` entry: figs3-no-head-direction-bias.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs3-no-head-direction-bias | not_reproduced | Yes | — | Cell 57. The criterion names two readings for the n of the weighted Rayleigh test. Under reading (a), n = the number of bins, 1121R157 in the room frame gives r = 0.3434 and p = 0.0134. The criterion says "Reproduced when every test has p ≥ 0.05" and has no partial branch, so the claim is not reproduced. |

How I checked the analysis in cell 57:

- **The numbers come from the data.**
  - Per ensemble and frame, the cell takes the mean ΔIdir in 36 head-direction bins of that frame, computed from the rotating-trial tracks.
  - It normalizes the values as the Figure S3 legend says: it adds the magnitude of the minimum and divides by the maximum.
  - It computes the weighted resultant r = |Σ v·e^{iθ}| / Σ v. The p value comes from `hc20.rayleigh_p`, which is Zar's eq. 27.4, with n = the number of non-empty bins.
  - The criterion's own check holds: r = 0.17 with n = 36 gives p near 0.35. The average r is 0.166 (SEM 0.023), within 0.17 ± 0.02.
- **The choice was not made to reach the result.**
  - Reading (a) is the one the claims file checks against the paper's reported p.
  - The reason for reading (b) does not hold. The weights are mean ΔIdir rescaled so the largest is 1; they are not frequencies. Their sum (9.2 to 26.8, printed in cell 57) is set by that scaling. Rescaled to a mean of 1, the weights sum to 36, which is the n of reading (a).
  - Under reading (a), at least one test has p < 0.05 under every Idir reading: 1, 4, 3 and 4 of 14 tests. The clean variant also has one or two of 12 below 0.05 under every reading. So the outcome does not depend on the Idir reading or on the sessions shown wrong.
  - Reading (b) gives a passing result only with 10° bins and rotating-trial probabilities. The other three Idir readings give 1 to 3 tests below 0.05 even under (b).
- **The criterion is applied as written.**

Points that do not change the outcome:

- The failure rests on a single test out of 14 at p = 0.0134. That is below the 0.05 threshold the criterion sets. It would not survive a correction across the 14 tests (Bonferroni 0.0036), but the criterion does not ask for one.
- Possible misreading in the claims file: the paper reports "p > 0.17", and the criterion uses the looser p ≥ 0.05. The claim fails even at the looser threshold, so this does not change the outcome.
