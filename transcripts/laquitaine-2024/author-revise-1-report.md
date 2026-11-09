I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all`. Checks report 0 errors and the notebook passes in 2,694 s, so I raised `runtime_minutes` to 45. Nothing is committed.

**Outcome changes.** Three claims go from partially reproduced to not reproduced, where the verifier disagreed. Their criteria require every part to hold and allow no partial outcome:
- `ground-truth-neuron-counts`: the counts are exact, but 78 NS neurons and 213 neurons of the 1-hour evoked recording have no spike in the first 600 s.
- `fig4a-yield-deep-layers`: Marques-Smith has one single unit in layer 2/3, where the criterion requires none.
- `fig5a-evoked-more-units`: the single-unit ratio is 2.212, just outside 1.8 to 2.2.

The verifier agreed with the other 36 outcomes and they stand. The totals are now 7 reproduced, 6 partially reproduced, 11 not reproduced and 15 blocked.

**Added or corrected:**
- **10-minute extremes (problems 1 and C):** the maxima and amplitude-to-noise extremes are now taken over the whole first 600 s, not 60 s.
  - `fitted-trace-maximal-amplitude` is still reproduced, now with preprocessed maxima of 331.1, 363.5 and 387.0 µV.
  - `fig2q-anr-within-vivo-range` stays not reproduced, and the dense probe now also falls outside the Horvath range.
- **Clock and coverage of every sorting (problems 3 and 4):** the notebook now prints the first and last spike of every sorting and runs the clock check for every sorter.
  - The 10-minute Kilosort2 sorting of the evoked recording ends at 240 s, as the Methods say it sorted 4 minutes. Its rates and scores now use 240 s. The counts behind `supp4-other-sorters-firing-rates` and `fig6gh-selection-bias-layer5-pyramidal` do not change. This is recorded as a new finding.
  - I scanned lags from −100 to +100 ms for the depth 3 dense probe sortings: they match none of the three dense probe ground truths at any lag. Those scores now carry that caveat.
- **Which evoked recording the sortings belong to:** the evoked Kilosort4 sorting has 250 units with an agreement of 0.5 or more against the 1-hour ground truth and none against the 10-minute 40 kHz one. The verifier's point 12, that this is probably the paper's evoked recording in Figures 4 and 5, is now a question for a reader in the new `questions/001250.yaml`. No claim was changed.
- **WaveMap (problem 10):** the main reading now uses the largest-amplitude site and its five nearest neighbours, as the Methods describe. Marques-Smith now gives 6 clusters with all three seeds, but the simulation gives 8, 9 and 7, so the claim stays not reproduced.
- **Quality tags (problem 5):** the helper's `qualify_units` was fixed. A unit is now tagged "partial" only through the neurons it matches above chance, and tags are computed over all sorted units. The Kilosort4 numbers do not change, and the conclusion now says the "merged" part is met almost by chance.
- **`fig6c-f-accuracy-predictors` (problem 11):** I ran the regression on the 19 features that need no waveforms, which meant adding statsmodels to the requirements.
  - Firing rate, excitatory class and layer 5 come out positive and distance negative in both regimes, so four of the five signs the claim names hold.
  - It stays blocked, because the sign of spatial extent and the full 21-feature fit need waveforms.
  - In the evoked regime none of the fits converged within the paper's 100 iterations. The notebook reports this.
- **Smaller fixes:**
  - The "silent over the whole file" column was wrong: none of the silent neurons is silent over its whole file. The notes and the finding are corrected.
  - The unsupported "mean of M and NS" print is removed.
  - The layer test in `fig6gh-selection-bias-layer5-pyramidal` now requires p < 0.05 only for the layers that differ, as the criterion says.
  - The 2.212 ratio is now printed with whether it is within range.
  - The dense probe part of `fig5a-single-unit-counts` is now called incomplete, with the paper's own numbers giving chi² = 1.82.
  - SpikeInterface's filtering matches the scipy filter to within 1.4e-05 µV.
- **Records:** the attempt record now has a `verifications` round for all 39 claims, giving the verifier's reasons and my responses. The notebook conclusions and summary, and the README, match the new numbers.

**Not done:**
- The code repository could not be reached (GitHub returned 504), so I could not read the code's `qualify_sorted_units`, its evoked config, or its definitions of snr and spatial extent.
- Medians, noise, spectra and WaveMap templates still use the six 10 s blocks. The verifier expected these to be unaffected by duration, and the extremes, which do depend on it, now use the full 600 s.
