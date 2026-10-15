## 1. Outcomes

The claims file lists 7 claims, and the attempt record gives an outcome for each of the 7.

| Claim | Recorded | Do I agree? |
|---|---|---|
| flight-spatial-code | partially_reproduced, with not_reproduced proposed | I agree with the proposed not_reproduced and no longer with partially_reproduced. The pre-specified run in cell 29 gives Rat1 FD9 12 of 25 (0.48) and Rat2 FD9 3 of 28 (p 0.16), and the criterion maps that to not_reproduced. The five repeats with 2000 shuffles give 11 or 12 of 25 (cell 30). The result still sits on the 0.5 bound: cell 23, which uses the corrected lookup with 200 shuffles, gives 13 of 25 (0.52). |
| three-orthogonal-surfaces | blocked (metadata_insufficient) | Agree. |
| si-comparable-to-preflight | reproduced | Agree under the criterion: p = 0.45, and every variant gives p ≥ 0.20 (cells 36 to 38). It is an absence claim, and it carries the caveats about the preflight apparatus and Rat2's position trace. |
| fd4-abnormal-selectivity | not_reproduced | Agree. The one-sided p is 0.055 (cell 41), so the call is borderline and the variants split. |
| fig3-stability-across-sessions | reproduced | Agree under the criterion: median r 0.537 against a null 95th percentile of 0.102 (cell 44). It depends on the smoothing and on the cluster-identity assumption. |
| theta-normal | blocked (data_missing) | Agree. The unfiltered listing in cell 3 now supports it. |
| ripples-normal | blocked (data_missing) | Agree. |

## 2. Statements the printed outputs do not support

- **Cell 33, cell 49 (Summary) and the attempt record (notes and proposed reason):**
  - The repeats are reported as "repeats with 2000 shuffles and five other seeds give 11 or 12 of 25 (0.44 to 0.48)", with "Rat1 FD9 0.48 of units significant (0.44 to 0.48 in repeats)" in the Summary.
  - The proposed reason says "With spikes at the lost position dropped … 12 of 25", and cell 33 says "with them dropped … the count is 12".
  - All of this leaves out cell 23 (shown again in cell 32). It uses the same corrected `PositionLookup` inside `epoch_units` and gives 13 of 25 (0.52) for the same epoch.
  - Across the seven runs the count is 11 to 13, which straddles the 0.5 bound. These sentences should say so.
- **Cell 49 (Summary): "Three claims come from the dandiset's description … and one from a figure title alone."** The claims file sources four claims to the dandiset description: si-comparable, fd4, theta and ripples. Cell 0 makes the same miscount ("Three claims come from the dandiset's own description") while its own table lists four.
- **Similar spike counts:**
  - Cell 39 says "The compared sessions have similar spike counts". The si notes and the si response repeat this.
  - For Rat2 the numbers do not support it. In cell 38 the FD9 median is 205 spikes against 352 preflight, and the median rate x occupancy is 5226 against 7628. Rat1 is similar (437 against 359).
- **The fig3 notes ("with similar occupancy, spike counts and shuffle drops") and the fig3 response ("similar occupancy, spike counts and drops"):** cell 46 gives a median of 301 against 455 spikes used, and cell 47 itself says "more spikes per tested unit". Occupancy and drops are similar; spike counts are not.
- **Cell 39 and the si notes, on rate x occupancy:** both state that rate x occupancy "is proportional to the spike count" without a qualifier. Cell 20 shows this only for flight maps (about 22 per spike) and says the preflight maps cannot be checked. The count-adjusted variant relies on this for the preflight maps.
- **Not checkable from the printed outputs:**
  - The OSD-968 contents: "two synchronised cameras" (cell 34 and the three-orthogonal notes) and "lists … no EEG" (cell 48 and the theta notes).
  - The statement that the conversion code does not describe the track layout (three-orthogonal notes).
  - The five-minute run time in the README.
  
  These are not wrong, but nothing in the notebook shows them.

Every other number in the five Result cells, the Summary, the README and the attempt record's notes and findings matches the printed outputs. I checked each one against cells 15 to 46.

The verification `reason` fields restate my round-1 reasons faithfully, in close paraphrase. Two small notes:

- The flight-spatial-code reason folds in my problems 6 and 7 without my "does not affect a conclusion" labels. That is fair, because the lookup fix did change the count.
- The fd4 and fig3 reasons keep my round-1 figures (16 of 53, r 0.538, null 0.091). The responses correctly give the updated ones.

## 3. Round-1 points

**Resolved:**

- 1: per-unit p-values, Monte Carlo SEs and repeats are reported. What remains is the cell 23 omission above.
- 6: the lookup is fixed, and the synthetic assert in cell 9 would fail with the old lookup.
- 7: drop fractions and a count-matched variant are reported (cell 31).
- 8: the listing is unfiltered (cell 3).
- The 277.8 Hz part of 9: that peak sits in a bin with 55 occupancy counts.

**Mostly resolved:**

- 3: the bias variants (bins with ≥ 5 occupancy counts, count-adjusted) agree with the main tests. The caveats are the spike-count wording above and the unchecked proportionality for preflight maps.

**Remaining, bearing on a conclusion:**

- **2, whose position the trace holds in Rat2's epochs:** this is disclosed but unresolved (cells 23 and 25). It decides whether Rat2 FD9 is a valid judged session for flight-spatial-code. It also affects whether Rat2's rate maps belong in si-comparable and fd4.
- **flight-spatial-code sits on the 0.5 bound:** the count is 11 to 13 of 25 across runs. The proposed not_reproduced follows the pre-specified run and the better-resolved repeats, but it is not robust.
- **4, the preflight apparatus:** this is now stated (cells 17 and 18) but cannot be settled. It bears on si-comparable and fd4.
- **5, fig3:**
  - Cluster identity is still assumed. The mean-rate correlation is consistent with identity but does not show it.
  - At 0.5 bins of smoothing the median r is 0.315 or 0.341, which would make the claim partially reproduced.
  - In the second epoch 1 of 19 units is significant against 10 of 16 in the first, and this is unexplained. For example, TT4 cluster 1 has r = 0.820 but p = 0.14 in epoch 2.
- **fd4 is borderline:** the criterion's test gives p = 0.055, while the peak ≥ 1 Hz and count-adjusted variants give p < 0.01.

**Remaining, not bearing on a conclusion:** the zero inter-spike intervals (2 to 15%) are disclosed and unresolved.

I saved the paper's abstract and figure titles in `paper/abstract.txt`, and the publisher page in `paper/nn0300_209.html`. The abstract says "a robust spatial code for three orthogonal surfaces", which matches the claims file.
