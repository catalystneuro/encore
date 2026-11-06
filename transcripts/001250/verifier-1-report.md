**Verifier report, round 1: Laquitaine et al. (doi:10.1101/2024.12.04.626805) on DANDI:001250 v0.251012.1648**

The claims file has 39 claims and the notebook covers all 39. My outcomes: 6 reproduced, 7 partially reproduced, 12 not reproduced, 14 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| ground-truth-neuron-counts | not_reproduced | The counts are exact: 1388, 1836 and 1552, all within 50 µm (cell 13). But 78 NS units and 213 units of the 1-hour E are silent in the first 600 s. The criterion requires that every unit spikes. |
| fitted-trace-maximal-amplitude | reproduced (fragile) | Reading (a) gives NS 325.1, M 336.3 and E40 357.5. Reading (b) gives 360.4, 345.0 and 373.7. With E40 as the evoked recording, both readings are within tolerance (cell 15). This rests on 60 s of traces, and NS under (a) is inside the tolerance by only 0.2 µV. |
| fig2m-peak-amplitude-increases-with-depth | reproduced | For NS, E and DS, Kruskal-Wallis p ≤ 2e-7 and each has one inversion. The in vivo trend holds too. 12 of 15 Mann-Whitney comparisons have p < 0.01 (cell 17). |
| fig2np-noise-increases-with-depth | reproduced | All models give p < 1e-33 with one inversion, under both the mean and the median absolute deviation (cell 19). |
| fig2q-anr-within-vivo-range | not_reproduced | The minimum ANR of NS (−146.5) and E (−141.4) lies outside M's widened range of [−104.2, 39.0]. DS is inside H's range. All distributions reach ±10 (cell 21). This rests on extremes taken from 60 s. |
| fig2r-power-law-spiking-band | not_reproduced | Only 7 of 30 layer fits have a negative slope with R² ≥ 0.9. Every model layer has R² < 0.9, as do three M layers (cell 23). |
| fig2s-v-ap-power-and-scaling-increase-with-depth | partially_reproduced | AP power holds in every model under both the median and the summed reading. Alpha fails: the slope's magnitude fails for NS (two inversions) and the signed slope fails for all three models (cell 25). |
| supp2-no-slow-oscillations | reproduced | H's 0.5–4 Hz share is 0.70, which is 7.6 to 18.7 times that of M, NS, E and DS (cell 27). |
| fig3e-amplitude-decay-with-distance | reproduced | The largest amplitude at 75 µm or more is 0.408 of the nearest electrode's under soma reading (i) and 0.339 under reading (ii). Beyond 200 µm, 122 of 122 electrodes are below 5 MAD (cell 29). |
| fig3c-five-temporal-profiles | not_reproduced | Judged with fig3fg, as its criterion says. |
| fig3fg-wavemap-six-profiles | not_reproduced | NS gives 8, 10 and 8 clusters over three seeds, and M gives 5, at the code's resolution choice with six sites (cell 31). The code's own saved outputs (7–10 and 7) also miss 6. |
| fig4a-lognormal-firing-rates | not_reproduced | Shapiro-Wilk rejects normality for NS layer 6 (p = 0.014) and E layer 5 (p = 0.0006). M passes, so neither simulation meets the partial condition (cell 35). |
| fig4a-yield-deep-layers | not_reproduced (narrow) | M has one single unit in layer 2/3, where the criterion requires none. M's L5/L4 ratio is exactly 20.0. The NS and E parts hold (cell 37). |
| fig4-median-firing-rates | partially_reproduced | Under reading (a), M 2.848, NS 1.155 and E 0.655 are within tolerance (cell 39). S has no sorting, so its value is blocked. |
| fig4bc-lower-median-narrower-distribution | partially_reproduced | For NS and E, both medians and variances are lower than M at p < 0.001 in 4 of 4 comparisons (cell 41). The S part is blocked: no sorting. |
| supp4-other-sorters-firing-rates | not_reproduced | For Kilosort3, 2 of 4 median comparisons and 4 of 4 variance comparisons have p ≤ 0.15. Lower medians at p < 0.05 occur in only 5 of 18 comparisons, so the "tended to be reduced" part also fails (cell 43). |
| fig5a-single-unit-fraction-differs | partially_reproduced | The "differs" part holds: reading (c) gives chi2(4) = 488.6, p ≈ 1e-104. Reading (i) gives NS 0.354, outside 0.41 ± 0.041. Readings (ii) and (iii), which the claims file favours, need NS-2X, which is absent (cell 45). |
| fig5a-single-unit-counts | partially_reproduced | NS 184, M 96 and H 93 are within tolerance. The goodness-of-fit tests give p = 0.167 and 0.061, both ≥ 0.05. NS-2X is absent, and the DS count of 199 lacks depth 1 (problem 2) (cell 47). |
| fig5a-synthetic-mostly-single-units | blocked: data_missing | The archive asset list has no sorting of sub-mearec-synthetics-buccino-rep or of sub-mearec-synthetics-s2. |
| fig5a-evoked-more-units | not_reproduced (narrow) | Total units rise 6.77-fold and the single fraction drops (0.116 against 0.354). But single units rise 407/184 = 2.21, outside 1.8–2.2 (cell 49). The E40 reading is blocked: no sorting. |
| fig5a-dense-probe-more-multi-units | reproduced | Multi-units are M 104 and H 265. M against H gives p = 0.0105 with H's multi-unit share higher. NS against DS gives p = 0.49, or 0.29 as deposited (cell 51). |
| fig5a-downsampling-small-gain | blocked: data_missing | NS-2X has no asset in the archive (confirmed). |
| fig5b-yield-far-below-theory | partially_reproduced | Theoretical yields NS 6.88, E 8.44 (E40 8.27) and S 0.651 are within tolerance. Kilosort4 is 8.0× and 4.8× lower, which meets reading (b) only. DS's theoretical yield is blocked: its ground truth tables hold only unit_name and spike times (cell 55; confirmed on the archive). |
| fig5b-synthetic-redundant-units | blocked: data_missing | No sorting of S. |
| fig5cd-most-units-degraded | reproduced | For Kilosort4, NS has 0.543 of single units below 0.8, E has 0.742; both have 1.000 merged and 0 false positives (cell 57). The merged tag is close to trivially met (problem 5). |
| fig5ef-curation-precision-recall | blocked: too_large | The sorting tables hold only KSLabel, Amplitude and ContamPct (I checked the archive). The quality metrics need waveforms from the full traces. |
| fig5g-mad-ratio-and-firing-predict-quality | blocked: too_large | Same as fig5ef. |
| supp5-cebra-knn-curation | blocked: too_large | Same as fig5ef. |
| fig6a-synthetic-accuracy-range | blocked: data_missing | No sorting of S. |
| fig6ab-biophysical-accuracy-15-percent | blocked: data_missing | S and E40 have no sortings. NS alone gives a mean of 0.093 (cell 59), which does not rule out 0.15 once S and E40 are added. |
| fig6-dense-probe-lower-accuracy | blocked: data_missing | It depends on fig6ab. Also, depth 1 has no sorting, and the DS3 sortings fail the clock check. |
| fig6c-f-accuracy-predictors | blocked: too_large | Only partly blocked: 19 of the 21 features are in the ground-truth tables (problem 11). |
| supp6-sorted-rates-overestimated | not_reproduced | Only 2 of the 5 layers with sorted units fall within 2.7–4.4. Layer 6 is 4.55, just outside (cell 63). |
| fig6gh-selection-bias-layer5-pyramidal | not_reproduced | The excitatory pattern fails for every sorter under both durations; for example, Kilosort4 over 1 hour has layer 6 at 0.81. The interneuron part holds, but the criterion grants a partial outcome only when the excitatory part holds (cell 65). |
| fig7a-ring-manifold | blocked: metadata_insufficient | No stimulus table, intervals or processing in sub-002, sub-002-fitted, sub-npx-evoked-sf-40Hz or the demo evoked file (checked on the archive). |
| fig7b-sorting-halves-capacity | blocked: metadata_insufficient | Same as fig7a. |
| fig7f-undersampling-no-loss-selection-bias-loss | blocked: metadata_insufficient | Same as fig7a. |
| fig7g-assignment-bias-capacity | blocked: metadata_insufficient | Same as fig7a. |
| fig7h-j-manifold-geometry | blocked: metadata_insufficient | Same as fig7a. |

### B. Problems

1. **[affects a conclusion]** `trace_blocks` and cells 10–11 use six 10-s blocks (60 s) where the criteria say 10 minutes. Extreme statistics depend on duration.
   - fitted-trace-maximal-amplitude: NS under reading (a) clears the lower bound by 0.2 µV.
   - fig2q: the ANR ranges come from 60 s.
   - The medians and Kruskal-Wallis tests are unlikely to be affected.
2. **[affects a conclusion]** In cells 33, 47 and 51, "DS" is depth 2 plus depth 3 only, but it is compared with the paper's three-depth totals (206 single units, 562 units). Depth 1 has no real sorting.
   - So the DS part of fig5a-single-unit-counts is incomplete, not reproduced: the DS fraction is 0.414 here against 206/562 = 0.367 in the paper.
   - The paper's own numbers give a goodness-of-fit chi² of 1.83 for H against DS, which confirms the form of the test but not the deposited data.
3. **[does not affect a conclusion]** In cell 8, the DS3 sortings fail the clock check: no unit reaches 0.5, and the coincidence rate is 0.346 against 0.336 after shifting. Only a 50 ms shift was tried.
   - Even so, DS3 scores enter cells 53 and 61 without a caveat. DS3 "well sorted" = 0 for every sorter, which is likely an artefact.
   - Those numbers feed only blocked or reported quantities.
4. **[does not affect a conclusion]** The clock check was run for Kilosort4 only. The 10-minute Kilosort2 sorting of E has 2 of 1378 units at ≥ 0.8 and 1 of 1836 neurons well sorted (cells 53, 59), which looks like a mismatch; the Methods say Kilosort2 sorted 4 min of the evoked recording.
   - It feeds the supp4 rows for Kilosort2 on E, where rate = count/600 may be wrong.
   - It also feeds the 10-minute Kilosort2 column of fig6gh. Kilosort2.5's ratio of 2.9 also qualifies, so the outcome is unchanged.
5. **[does not affect a conclusion]** In `qualify_units`, "oversplitter" is tested over every neuron with a score above 0, not only the unit's above-chance matches. On a synthetic input, a unit scoring 0.005 (below chance, 0.01) on a neuron that another unit matches is tagged oversplitter. The tags are also computed among single units only.
   - "Merged" = 1.000 for Kilosort4 is met almost by chance coincidence across 1388 or more neurons. This follows the claims file's definition.
   - I tested `chance_scores`, `loglog_fit`, `layer_order_ok` and `site_noise_mean_ad` on synthetic inputs; they behave as specified.
6. **[does not affect a conclusion]** In cell 13, the column "silent over the whole file" for NS is computed on spike trains already cut at 600 s, so the label is wrong.
7. **[does not affect a conclusion]** Cell 45 prints "mean of M and NS" = 0.417. That is the author's own reading, not one in the claims file, and it happens to fall near 0.41. It must not be used.
8. **[does not affect a conclusion]** In cell 65, the excitatory rule requires p < 0.05 for every other layer, where the criterion says "for those that differ". The ratio condition fails anyway.
9. **[does not affect a conclusion]** In cell 49, 2.21 is printed next to "(1.8 to 2.2)" without noting that it misses.
10. **[does not affect a conclusion]** In cell 31, WaveMap uses:
    - the top 6 sites by amplitude anywhere on the probe, not the "six nearest";
    - templates from as few as 5–8 spikes;
    - resampling to 50 points, an author's choice that is stated.

    The cluster counts are far from 6, as the code's own outputs were, so the outcome is robust.
11. **[affects a conclusion]** fig6c-f is marked fully blocked. But 19 of the 21 features are in the ground-truth tables:
    - from the tables directly: synapse class, etype, layer, exc_mini_frequency, dynamics_holding_current;
    - computable from them: firing rate from the spike times, and distance to the nearest site from the soma x, y, z.

    The Kilosort4 accuracies already exist (cell 53). The signs for firing rate, synapse class, layer 5 and distance could have been tested, which could have given a partial outcome. Only snr and spatial extent need waveforms.
12. **Possible misreading in the claims file (reported, not corrected).** For fig4 and fig5a, the claims file says the code's evoked recording is the 10-minute 40 kHz E40. But the deposited first 10 minutes of the 1-hour E reproduce the code's printed 0.655 ± 0.083 exactly (cell 39). E's 3520 cortical units also fit the paper's N = 5,241 for M, NS, NS-2X, E and S (implied E ≈ 3489). So the paper's Figs 4–5 probably used the 1-hour E.
13. **[does not affect a conclusion]** In cell 29, the isolated and the summed Reyes files declare the same units but differ in scale about 1000-fold: peak-to-peak 0.042 against 37.9 at the same electrode. The claim is about ratios, so it is unaffected.

### C. What I could not check, and the output that would settle it

- **10-minute extremes.** Needed: the maximum |trace| and the ANR minimum and maximum over the full first 600 s for NS, E40 and M, or at least per-block maxima to show whether they keep growing.
- **Coverage and clock of every sorting.** Needed: the first and last spike time of each sorting (SORT_TABLE's per-sorting "last spike" is computed but only its maximum is printed), and the clock table for all sorters, especially the 10-minute Kilosort2 sorting of E.
- **DS3.** Needed: the agreement at a range of lags, or a cross-correlogram of sorted against ground-truth spikes, to tell a time offset from a mismatched file.
- **Which evoked simulation the E sorting belongs to.** Needed: the agreement of the E 10-minute Kilosort4 sorting with the E40 ground truth.
- **The code itself.** The code's `qualify_sorted_units` and its evoked config were not available to me, so problems 5 and 12 rest on the claims file's description and on numerical coincidence.
- **Filtering.** I could not confirm that the scipy high-pass plus common median reference matches SpikeInterface's. Needed: one block processed both ways.
