## A. Outcomes

The claims file has 7 claims. I judge 3 reproduced, 1 not reproduced and 3 blocked.

| Claim | My outcome | Reason |
|---|---|---|
| flight-spatial-code | not_reproduced | Under the claims file's criterion, cell 33 gives Rat1 FD9 10/25 significant (0.40, binomial p 1.6e-7) and Rat2 FD9 2/28 (0.071, p 0.41). Rat1 is above chance but below 0.5, and Rat2 is not above chance, so neither "partial" branch applies. This is weak evidence against the claim: no one has shown that the trace in Rat2's windows is Rat2's position (cells 27 and 29). |
| three-orthogonal-surfaces | blocked (metadata_insufficient) | The abstract says the code covers "three orthogonal surfaces". The archive holds only a 2-D pixel position from one camera, with no camera view, track layout or pixel scale (cell 5, cell 38). I queried the DANDI API: all 8 assets list only Position/SpatialSeries, and no part of this claim can be tested. |
| si-comparable-to-preflight | reproduced | Cell 40: FD9 ES median 1.385 bits/spike against preflight 1.448, Mann-Whitney p 0.45 (n 64 / 53). Every variant also has p > 0.12 (cells 41, 42). The test can hardly fail, though (problem 3). |
| fd4-abnormal-selectivity | reproduced (fragile) | Cell 44: FD4 median 1.177 against preflight 1.441, one-sided p 0.024, so the criterion is met on the draft. The same test on the previous version's distinct maps gives p 0.055 (cell 45). Only Rat1 passes on its own (p 0.03; Rat2 0.12, Rat3 0.18), and the spike-based significant fraction is not lower on FD4 (24/71 against 12/53, p 0.94). |
| fig3-stability-across-sessions | reproduced | Cell 47: Rat3 FD4 ES1 against ES2, 15 units, median same-unit r 0.537. That is above the re-paired 95th percentile (0.102) and above 0.5, but only just: σ 0.5 gives 0.315, and the dandiset's own maps give 0.340 (cell 48). Which sessions the paper's Figure 3 compares is unknown. |
| theta-normal | blocked (data_missing) | No file has an ElectricalSeries or LFP (cell 3). The asset metadata I queried agrees: variableMeasured is only ProcessingModule/Units/ElectrodeGroup(/Position). Nothing here can be tested. |
| ripples-normal | blocked (data_missing) | Same as theta-normal. |

The paper is not open access. I saved its abstract and figure titles to `paper/abstract.txt`. The abstract states no chance level; the notebook uses 0.05 as the criterion specifies. MC epochs, where no claim is made, come out at 0 to 0.11 significant (cell 32), which is consistent with that chance level or a slightly conservative test.

## B. Problems

1. **[affects a conclusion]** Cells 27, 29 and 33, and fd4 in cell 44: it is unresolved whose position the trace is in Rat2's windows.
   - Rat1's units are selective in Rat2's FD4 ES window (10/15) while Rat1 is labelled as resting (BL). So either the FD4 labels or the trace attribution is wrong.
   - Cell 23 shows that the original Rat2 rate maps were built from this same trace. Both the judged Rat2 FD9 session and the Rat2 FD4 maps (the lowest group, median 0.872) therefore inherit the problem.
   - The notebook keeps both with a caveat but never reports fd4-abnormal without Rat2.
2. **[affects a conclusion]** Cell 45, fd4-abnormal: the pass depends on the conversion dropping every copy of the duplicated maps.
   - The criterion says "each distinct map once". Applied to the previous version that way, the test gives p 0.055.
   - The draft drops three near-empty Rat2 FD4 ES maps (7.58 bits, mean rate ≈ 0), which moves p to 0.024.
   - The CEL-names-only variant also fails (p 0.073).
3. **[affects a conclusion]** Cells 40 to 42, si-comparable: rate-map spatial information cannot tell selective units from non-selective ones.
   - Rat2 FD9 rate maps have median 1.343 bits, equal to Rat2 preflight (1.321), while only 2/28 of its units beat their shuffles.
   - A "no difference" test with no equivalence margin cannot fail under these conditions.
   - The main comparison may also be ES in flight against a different apparatus on the ground: the dandiset description says the preflight track was flat and rectangular (cells 21 and 22). Rat2's preflight tetrodes also share none with its flight tetrodes (cell 10).
4. **[affects a conclusion, magnitude unknown]** `neurolab.epoch_units`: shuffled spikes are dropped more often than real ones.
   - The drop is 6% against 2 to 3% in FD9, and about 21% against 4 to 6% in Rat3 FD4 (cell 35).
   - The shuffled spikes that survive land at times when other units fire, which can inflate the null. The count-matched variant corrects only the spike count, not where the spikes land.
   - Rat1 FD9 sits near the 0.5 threshold (0.40 main, 0.44 at 2000 shuffles, 0.48 count-matched).
   - My synthetic check: 60 independent non-spatial Poisson units, 200 shuffles, position sampled only at ensemble spike times. It gave 5/60 false positives each time, so the test is calibrated when drops are near zero. I did not test it at the drop rates seen in the real data.
5. **[does not affect a conclusion]** Cells 47 and 49: in Rat3 FD4, ES1 has 11/16 significant units and ES2 has 1/19, although the maps are stable (median r 0.54) and the null 95th percentiles are similar (2.14 and 2.18). The notebook does not discuss this. It is a further sign that the shuffle test is sensitive to something other than spatial tuning.
6. **[does not affect a conclusion]** Cell 47, fig3: the outcome holds at the criterion's σ of 1 bin, but whether the median clears 0.5 depends on smoothing (problem list in A).
7. **[does not affect a conclusion]** Cells 17 and 18: occupancy runs at 38 to 57 counts/s against a stated 60 Hz. It is used only as relative weights, so it would matter only if frames were dropped unevenly across space.
8. **[does not affect a conclusion]** Helper functions check out:
   - `skaggs_info`: uniform map gives 0; one bin out of 64 gives 6 bits.
   - `merge_bins` is correct.
   - The `PositionLookup` test in cell 13 passes.
   - x→column and y→row are confirmed by the swap test in cell 23.
   - The p-value (`null >= observed`) matches the 95th-percentile criterion.
   - There is no train/test leakage; no fitted model is involved apart from the count-adjustment variant.

## C. What I could not check, and the output that would settle it

- **The paper's methods, chance level, thresholds and Figure 3 sessions** (not open access). No notebook output can supply these.
- **Whose position is in Rat2's windows.** These outputs would settle it:
  - path length or speed of the trace in each window;
  - Rat1 units tested against the trace in Rat2's FD9 MC window and in its FD4 MC window;
  - fd4-abnormal and si-comparable recomputed without Rat2 (Rats 1 and 3 FD4 against preflight).
- **Shuffle calibration at the real drop rates.** Needed: the false-positive fraction per session when each unit's spike times are replaced by a rate-matched Poisson train in the same window, run through `epoch_units`.
- **Whether the rate-map spatial information discriminates at all.** Needed: rate-map information split by the unit's spike-shuffle significance (cell 33 results joined to the `maps` table), and a confidence interval for the FD9 minus preflight median difference.
- **The Rat3 ES1/ES2 asymmetry.** Needed: per-unit information against null95 in both epochs, and the occupancy-bin count used in each.
