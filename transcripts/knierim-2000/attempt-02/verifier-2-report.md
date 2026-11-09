## Round 2 verification: Knierim, McNaughton & Poe (2000) on DANDI 001754 (draft)

### 1. Outcomes

The claims file has 7 claims. The attempt record gives 1 not_reproduced, 3 reproduced and 3 blocked. I agree with all seven.

| Claim | Record | Agree | Note |
|---|---|---|---|
| flight-spatial-code | not_reproduced | Yes | Cell 34: Rat1 FD9 10/25 (0.40), Rat2 FD9 2/28 (0.071, p 0.41). The outcome holds even if Rat2 is set aside: Rat1 alone is below 0.5, so the "reproduced in one only" branch does not apply either. |
| three-orthogonal-surfaces | blocked (metadata_insufficient) | Yes | Cell 41: no camera view, track layout or pixel scale. |
| si-comparable-to-preflight | reproduced | Yes | Cell 43: p 0.45. Every variant has p ≥ 0.12 (cells 44, 45). It is a weak test (see 3). |
| fd4-abnormal-selectivity | reproduced | Yes, fragile | Cell 49: p 0.024. Without Rat2 it is 0.035 on both versions (cell 51). It fails on the earlier version's maps with Rat2 (0.055, cell 50), on CEL names (0.073) and on MC maps (0.060). |
| fig3-stability-across-sessions | reproduced | Yes | Cell 54: median r 0.537, null 95th percentile 0.102. At σ 0.5 the median is 0.315, which would make it partial. |
| theta-normal, ripples-normal | blocked (data_missing) | Yes | Cells 3, 5 and 41. |

### 2. Statements the outputs do not support

- **Cell 52 (fd4 Result):** "FD4 is lower than FD9 for Rats 1 and 2 without significance … and on spike-based information minus the shuffle mean (0.025 against 0.211, p = 0.13; with Rat3, 0.232 against 0.211, p = 0.31)." With Rat3, FD4 is higher than FD9 (cell 49: 0.232 against 0.211), so "FD4 is lower" does not cover that case. The attempt record states the same numbers neutrally and is fine.
- **Cell 60 (Summary) and README:** "gives 0.074 false positives over all flight ES epochs and up to 0.21 in one session." These two figures come from different nulls:
  - 0.074 is the plain Poisson pooled rate.
  - 0.21 (0.214) is the maximum under the sample-time null.
  - Under the sample-time null, which the record says "reproduces the real drop rates", the pooled rate is 0.096 (cell 37). The plain-Poisson per-session maximum is 0.160.
  - The sentence should give 0.096, or say which null each number comes from.
- **Cell 47 and the record (si-comparable):** "a difference of up to about a quarter of the preflight level is not excluded." The interval in cell 46 is −29% to +22%, so a drop of up to 29% is not excluded. For Rat1 alone the bound is −40%. "About a quarter" understates the lower bound.
- **Cell 57 (fig3):** "Units with the most stable fields are significant in the first epoch only, and for several of them…" One of the three examples, TT8 cluster 5, has r = 0.436, below the median of 0.537 (cell 56). It is not among the most stable units. This is minor; the null-95th-percentile numbers quoted are correct.
- **Cannot be checked from these outputs:** the earlier-version figures in cell 39 and the record (Rat1 12/25, "11 to 13 over seven runs", shuffle drops 0.307 and 0.074). They come from the first attempt and are not printed here. Cell 7 does support "the draft's trace adds samples at the other rat's spike times".

Every other number in the Result cells, the Summary, the README and the record notes matches cells 21 to 57. That includes 9/122 and 12/125, the per-session rates 0.160, 0.154, 0.037 and 0.214, the binomial p values 0.0035, 0.0026, 0.28 and 0.99, path length 20.5 to 91.6, MC 0 to 2 of 11 to 32, 1.855 against 1.076 (p 9.0e-7), rho 0.791, the interval −0.425 to 0.312, and the Rats 1 and 3 result 1.242 against 1.510 (p 0.035).

**My round-1 reasons in the record:** they are faithful paraphrases of my report, with the numbers right. Problem 7 (occupancy of 38 to 57 counts/s) is left out. I had marked it as not affecting a conclusion, and cell 18 states it.

### 3. Round-1 points

**Resolved:**
- **1. Trace attribution in Rat2's windows.** It is still unresolved, and the data cannot settle it. It no longer decides a conclusion:
  - fd4 without Rat2 passes (p 0.035).
  - si-comparable for Rat1 alone gives p 0.25.
  - flight-spatial-code is not_reproduced with or without Rat2.
  - Cell 30 adds the path length and the MC-window contrasts I asked for.
- **2. fd4's dependence on the duplicated maps.** It is now stated, and the without-Rat2 test does not depend on version.
- **3. si-comparable.** The split by spike-shuffle significance, the bootstrap interval and the missing equivalence margin are now reported (cells 46, 47).
- **4. Shuffle false-positive rate at the real drop rates.** Measured in cell 37, and the outcome holds against it.
- **6. Smoothing dependence** and **7. occupancy rate:** both stated.

**Remaining, bearing on a conclusion:**
- **flight-spatial-code: the test's strictness on real spike trains is untested.** The Poisson calibration measures false positives only.
  - Rat3 ES2 has units with stable fields (TT4/1 r 0.82, TT5/1 0.84, TT3/2 0.85) that do not pass. Their null 95th percentiles jump, for example TT4/1 from 1.33 to 4.31 (cell 56).
  - Rat2 FD9 has the same null median as Rat1 FD9 (2.04) but a much higher median 95th percentile (3.57 against 2.60; cells 33, 36). Per unit it reaches 7.93 for TT13/11 (cell 35).
  - Rat2's real units pass less often (2/28) than non-spatial trains placed at sample times (6/28).
  - So the null is heavy-tailed for real trains in exactly the sessions that come out negative, and the notebook leaves this unexplained (cell 57). A low significant fraction is therefore weak evidence against a spatial code.
  - The output that would settle it: the same test on real spike trains with their temporal structure kept but their positions decoupled (for example, ES1 spikes run against the ES2 trace), or the null's upper tail broken down by burst structure per unit.
- **fd4-abnormal-selectivity: the pass is narrow.** On rate maps it rests on p of 0.024 and 0.035, and the spike-based measures do not show lower selectivity on FD4: 24/71 against 12/53 significant (p 0.94), and corrected information with Rat3 (p 0.31).
- **si-comparable-to-preflight: the result cannot support "comparable".** There is no equivalence margin, the interval allows −29% (−40% for Rat1), and preflight may have been on a different apparatus (cells 21, 22). The outcome follows the criterion, but it shows only that no difference was detected.
