## A. Claim outcomes

The claims file lists 7 claims. I had no separate attempt record, so the counts and outcomes below come from the claims file and the notebook outputs. The paper is not open access: Europe PMC shows no PMC copy, and the publisher page gives only the abstract and the figure titles, which are saved in `paper/abstract.txt` and `paper/nn0300_209.html`. That abstract states no chance level.

| Claim | My outcome | Reason |
|---|---|---|
| flight-spatial-code | partially_reproduced | Cell 23: Rat1 FD9 has 13 of 25 units significant (0.52, binomial p 3.6e-11), and Rat2 FD9 has 3 of 28 (0.107, p 0.16, not above chance). Under the criterion that is "reproduced in one only". The result is fragile: the same Rat1 epoch run with 200 shuffles and another seed (cell 19) gave 12 of 25 (0.48), which would make the outcome not_reproduced. |
| three-orthogonal-surfaces | blocked (metadata_insufficient) | I checked the archive. Position is one 2-D pixel series (0 to 255), and neither the asset nor the dandiset metadata describes track geometry or camera view. No part can be tested beyond the whole-track result of flight-spatial-code. |
| si-comparable-to-preflight | reproduced (weak) | Cell 27: rate-map spatial information, FD9 ES 1.385 against preflight 1.448 bits/spike (n 64 and 53), two-sided Mann-Whitney U p = 0.45. The variants agree (p 0.20 to 0.98). The measure cannot tell real tuning apart from sampling bias (problems 3 and 4). |
| fd4-abnormal-selectivity | not_reproduced | Cell 30: the FD4 median (1.214) is below preflight (1.441), but one-sided p = 0.055, so it misses p < 0.05. The variants split (peak ≥ 1 Hz p = 0.0095; Rat1 alone p = 0.032). The spike-based fraction is not lower on FD4 (21/71 against 16/53, Fisher p 0.55). |
| fig3-stability-across-sessions | reproduced (borderline) | Cell 32: the median same-unit r is 0.538, which is above the 95th percentile of re-paired medians (0.091) and above 0.5. It depends on sigma: with sigma 0.5 the median is 0.312, which would be partial. It also rests on the unchecked assumption that a cluster id names the same neuron in both epochs. |
| theta-normal | blocked (data_missing) | I confirmed this in the archive. Asset `variableMeasured` lists only Units, ProcessingModule, ElectrodeGroup, SpatialSeries and Position, with no ElectricalSeries or LFP. The files are 2.5 to 8.9 MB, too small for continuous EEG. Nothing is testable. |
| ripples-normal | blocked (data_missing) | Same as theta-normal. |

## B. Problems

1. **[affects a conclusion]** Cells 22, 23 and 19: the flight-spatial-code outcome hinges on one Rat1 FD9 unit (13 of 25 against 12 of 25 across two shuffle runs). Neither the Monte Carlo error on the shuffle p-values nor the per-unit p-values near 0.05 are reported. Cell 23 shows three units with p between 0.01 and 0.05.
2. **[affects a conclusion]** Cell 19: it is unclear whose position the shared trace holds in Rat2's ES epochs. Rat2's units are at or below chance in their own ES epochs (0 of 16 on FD4, 3 of 28 on FD9). Rat1's units are significant in Rat2's FD4 ES window (7 of 15), when Rat1 is labelled BL. The notebook still judges Rat2 FD9 under the criterion. That failure may be a data problem and not biology. The Rat2 rate maps used for the two rate-map spatial information claims come from the same trace (cell 15).
3. **[affects a conclusion]** `rma_info` and `skaggs_info`, as used by `rma_table` (64 x 64 bins, no minimum occupancy, no spike-count correction): Skaggs information is dominated by sampling bias. In my synthetic test, uniformly random spikes on 32 x 32 bins gave 4.40, 2.55, 0.85 and 0.16 bits/spike at 50, 200, 1000 and 5000 spikes. Preflight ES epochs last 465 to 614 s, against 1611 to 2664 s on FD9. Every session, including Rat2 with 0 of 16 significant units, has "info>0.5_bits" = 1.00 (cell 23). So si-comparable and fd4 compare bias as much as tuning.
4. **[affects a conclusion]** The dandiset description says the preflight recordings were on "a flat rectangular track", but the files label them ES. Cells 27 and 30 compare "ES against ES" across different apparatus and never mention it.
5. **[affects a conclusion]** Cell 32 (fig3): the median r of 0.538 sits close to the 0.5 bound. Whether a cluster id names the same neuron in both epochs is assumed and not checked (cell 18). In Rat3 FD4 the median unit has spikes in only one epoch (cell 17). Epoch 1 has 9 of 16 significant units against 2 of 19 in epoch 2 (cell 33), which sits oddly with stable fields and is not explained.
6. **[does not affect a conclusion]** `PositionLookup`: a spike whose own sample is the lost position (0, 255) takes the nearest valid sample within 0.25 s. The claims file says such samples are dropped. I confirmed this behaviour on synthetic input (t = 1.1 maps to the sample at t = 1.0).
7. **[does not affect a conclusion]** `epoch_units` shuffle: a shifted spike is dropped when no position sample lies within 0.25 s. Samples exist only at spike times, so these drops cluster in low-activity periods. Fewer null spikes push the null spatial information up, which makes the test conservative. The fraction of shuffled spikes dropped is never reported, and this may contribute to the low MC and Rat2 fractions.
8. **[does not affect a conclusion]** Cell 34 says no file holds EEG and cites the listing in cell 3, but that listing is filtered by prefix and hides `acquisition/` and other processing modules. The archive metadata does support the absence.
9. **[does not affect a conclusion]** Zero inter-spike intervals make up 2 to 15% of intervals (cell 17, 15% in Rat2 FD4). These may be duplicate spikes from merged, overlapping epoch files, and they are left unresolved. Separately, a peak rate of 277.8 Hz in a Rat1 FD9 rate map points to single low-occupancy bins, which are included in the rate-map spatial information.
10. **[does not affect a conclusion]** Checked and correct:
    - `skaggs_info`: one bin of 16 gives 4 bits; a flat map gives 0.
    - `merge_bins`, `rma_info` (-999 bins and bin [63, 0] handled), `bin_xy` (x to column, y to row), and the nearest-sample logic in `PositionLookup`.
    - The binomial and Mann-Whitney sidedness matches each criterion.
    - The test p < 0.05 with p = mean(null ≥ info) is equivalent to "exceeds the 95th percentile".
    - No numbers are hard-coded; all derive from the loaded files.

## C. What I could not check, and which outputs would have let me

- **The paper itself:** its Methods, selection, chance level, and which sessions Figure 3 compares. It is not open access.
- **Robustness of flight-spatial-code:** needs per-unit p-values for Rat1 FD9 and Rat2 FD9, plus repeats over several seeds or 2000 shuffles.
- **Shuffle drops:** needs the per-unit fraction of shifted spikes dropped for lack of a sample within 0.25 s.
- **Bias in the rate-map comparisons:** needs the spike count and epoch duration for each rate map, and a shuffle-corrected or spike-count-matched spatial information value.
- **Rat2 attribution:** needs, for each Rat2 ES window, the overlap between the Rat1 and Rat2 position samples and spike counts restricted to that window.
- **Cluster identity in fig3:** needs per-unit spike counts in each Rat3 ES epoch and any evidence that cluster ids carry across epochs (the files hold no waveforms).
- **Absence of EEG:** an unfiltered `h5_tree` of every file, including `acquisition/` and all processing modules.
