I worked through the round-1 report, re-ran the entry, and recorded the round under `verifications`. `python tools/entry.py all` passes: 0 check errors, notebook ran in 368 s, and the clean run gave the same numbers as my development run. Nothing is committed.

**Outcomes now:** 8 reproduced, 19 partially reproduced, 7 not reproduced, 12 blocked (before: 6, 10, 3, 27).

**Changed outcomes**
- **Blocked to tested.** Eighteen claims were blocked only because a test or tolerance band cannot be met with 5 or 3 units. The claims file's "Unit samples" paragraph says to compare values and directions on the subset, so they are now tested:
  - partially reproduced: fig3a (all three), swr-shift-control, kc-fraction, xcorr-stronger-in-spindles, fig5c-spindle, thalamus-at-spindle-nested-swrs, mua-coupled-swrs
  - not reproduced: fig3c, spindle-mua-modulation, fig4b
  - reproduced, with notes saying the test cannot reject at this n: phase-robust-to-spike-count, fig6g
- **fig6-modulation-with-ripple-power** is now not reproduced (the verifier had partially, unreliable). With the corrected modulation index, no reading has a majority of units more modulated in high ripple power cycles (1 of 3 at most).
- **fig1s3-spindles-not-theta** goes from partially to not reproduced, and no longer rests on an assumption. Neither raw nor state-relative power meets both parts of the criterion.
- **fig7c-run-units-in-spindles** goes from not to partially reproduced. The ripple-power effect holds; the run effect goes the paper's way but is not significant.
- **thalamus-not-selective-for-run-cells** stays blocked, now as `data_missing`, because the co-modulated pairs need maze spikes.
- **Kept against the verifier:** fig2c stays partially reproduced. The rises in SWR rate before and after KCs hold in every reading; the minimum timing does not. The disagreement is recorded.

**Fixes and added outputs**
- **Autocorrelogram peak finder (fig4):** now uses the first minimum after lag 0, under three smoothings, and returns 100 ms on a synthetic 10 Hz process. Per-curve plots mark the minimum and the peak. The outcome stays not reproduced.
- **Modulation index (fig6 family):** the histogram is now smoothed over ±1 s and then cropped. Flat Poisson firing gives 0.06 to 0.17, where the old code gave 0.39.
- **Rayleigh test:** the deposited script calls `circ_rtest` without a bin spacing, so I removed the bin-spacing correction from the helper. The numbers barely moved.
- **Quantities that were never computed** are now printed: the 22.58 % subset; all fig6e and fig6f percentages and tests, including the Spearman and F-tests; the fig6g Wilcoxon tests with median differences; the S3 pair's correlogram index; and the run vs not-run thalamic comparison.
- **Pair correlogram control:** a cycle-permutation null for the in-cycle correlograms. The in-cycle peaks stay high (z 7.09 and 4.18), so restricting both trains to the cycles does not explain them.
- **SWR shift control:** each SWR is now shifted 20 times instead of once; the counts did not change.
- **Sleep detection, readings (b) and (c):** the Methods' rule as written finds no sleep in S1 and S3 and at most 2 min in S2. I added a variant that fills dips under 30 s, and a `methods_unavailable` finding asking the authors how the deposited sleep periods were made.
- **Deposited scripts:** the data check now prints the relevant lines of the `.mlx` scripts (the MD unit, the thalamic pairs, the phase binning and normalisation).
- **Text:** the GLM relation now reads b1' = 4 b1, the fig5c line is reworded, and the header table, summary and README are updated.
- **Question for a reader:** added `questions/crcns-hc-24.yaml` for rebound-delta-phase-trend. Its criterion is met by r = -0.011, which is no trend, against the paper's r = -0.32.

**Not done**
- **Kappa near 125** for sparse units in the Methods reading of fig7b is unchanged. Kappa decides no outcome.
- **What the S3 mPFC epoch is** (the 24 min before the LFP starts) cannot be settled from the data; it stays a finding.
- **The verifier's problems 8 and 9:** phase bins that drop phases above 3.058 rad are kept because they follow the deposited script. The glm readings (i) and (ii) being the same number is a flaw in the claims file, not a misreading, so I did not ask a reader about it.
