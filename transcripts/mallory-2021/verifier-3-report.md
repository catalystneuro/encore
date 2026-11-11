# Verifier report, round 3: Mallory, Hardcastle et al. 2021 on DANDI:000053

The claims file lists 47 claims and the attempt record has 47 outcomes. Only one claim has a `proposed` change: `supp12-no-false-eye-detection`, from blocked to reproduced. I checked it in the re-executed `simulated_eye_mallory_2021.ipynb` against `mec_ln.py`, the Methods ("Generating simulated data without eye-encoded information") and the legend of Supp. Fig. 12.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| supp12-no-false-eye-detection | reproduced | Yes | — | Both parts of the criterion are met, applied as written (details below). |

**Part 1: mutual information (cell 6).**
- The criterion asks that the data mutual information exceed all 100 shuffles in most sessions. It does in 11 of 11 sessions for all six pairs, which are the legend's pairs: Eh, Ev, Eh dot and Ev dot with B, and Eh dot and Ev dot with Bs.
- The median data value is 0.026 to 0.115 bits. The median of the shuffle maxima is about 0.004 bits.
- Under the stricter variant (circular shifts of more than 20 s) it holds in 11 of 11 sessions for five pairs and 10 of 11 for Ev with B.
- The values are computed from the session's kept bins. The bin edges are the variables' inner 98% ranges, taken from `prepare`.

**Part 2: simulation and re-fit (cells 4, 8 and 9).**
- **The data fit is the main notebook's (cell 4).** The forward search under readings (1a, 2a) gives 718 eye units: Eh 341, Ev 243, Eh dot 238, Ev dot 137. These are the main notebook's counts.
- **The simulation follows the Methods (cell 8).** The rate is exp of the intercept plus the selected model's non-eye terms, using the full-session parameters (`sel_full`). Spikes are drawn from a Poisson distribution with that rate.
- **The indexing is right.** `_layout` on `encoded` matches how `forward_search` lays out `sel_full`. The design blocks and the simulated trains are both in session order, as `analyse_session` expects. The same folds and bins are used for the re-fit.
- **Counts on the simulated data (cell 9).** Eye variables are detected in 0, 2, 2 and 0 cells, against 341, 243, 238 and 137 in the data. That is at most 0.008 of the original, within the criterion's 10%.
- **The simulation keeps the body tuning.** B is kept in 635 of 635 simulated eye cells that encoded it, and Bs in 456 of 456.

**Choices the result rests on.** None of them was made to reach the result.
- **Which cells are simulated:** the 718 eye cells plus a seeded random 300 of the 1422 other encoding cells. This choice is stated and the Methods leave it open. The sample gives 0 eye detections, so scaling it up to all 1422 cells adds nothing.
- **Full-session parameters rather than the fold mean:** this is also stated. Either way the eye terms are absent from the model that generates the spikes.
- **Higher simulated firing rates:** the simulated eye cells fire faster than the real ones (median 7.48 against 4.84 Hz). This is a direct result of the Methods' instruction to delete the eye terms. A higher rate gives the re-fit more power, so it makes false detections more likely, not less.

**Minor discrepancy.** Cell 12 prints a notebook time of 40.4 min. The record's notes say 41.3 min and the README says "about 41 minutes". This does not affect the outcome.

**Claims file.** I found no misreading of the paper in this claim's criterion. The 10% threshold for "not falsely detected" is the claims file's own reading, and the file says so.
