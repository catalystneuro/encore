**A. Outcomes** (20 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig4d-mean-correlation-j-array | not_reproduced | Cell 14: none of the 18 runnable readings has a positive mean at p<0.05. Mean r runs from −0.148 to 0.095, and the main reading gives −0.079 (n=19). Low power (split-half reliability 0.20/0.28, cell 11) means this is a failure to detect, not evidence against. |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | The archive API shows 1 subject (Jenkins), 2 files and no EMG. None of the A, B or single-electrode J data is there. |
| fig4-broad-near-zero | not_reproduced | Cell 17: every range (O1a) reading fails the IQR ≥ 0.3 test (IQR 0.17–0.29). The only passes are the SD readings, with n = 3–5 units. An IQR near 0.26 is what pure noise gives with 27 conditions. |
| fig4e-correlation-time-course | reproduced (criterion met, but not informative) | Cell 19: 18/30 readings pass, including every O1a reading (r falls from 0.30–0.41 at −200 ms to about 0 at onset). My noise-only simulation passes the same test (problem 1), so the data cannot separate this from shared trial noise. |
| suppfig1-population-averages-lose-tuning | reproduced (criterion met, but not informative) | Cell 21: 36/36 runs pass. Untuned Poisson data also pass: spread 8.3 in the preparatory window, −0.55 at onset, strongest trace on top at −150 ms (problem 1). |
| fig6d-perimovement-best-j-array | partially_reproduced | Cell 23: 64 runs reproduced and 32 partial (initial vel. ≥ peri under O3/O4 a,b / b,a / b,b). The criterion needs every reading to hold. Under O1a every space has negative performance, and the gaps are about 0.005; cell 32 gives peri vs kinematic p=0.62 and peri vs initial vel. p=0.81. |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | Confirmed on the archive: no single-electrode data, no EMG. |
| fig6-perimovement-best-each-dimensionality | not_reproduced | Cell 26: 0/96 readings reach 0.8; fractions are 0.07–0.36. |
| fig6-maze-endpoint-speed-space-poor | not_reproduced (depends on O1) | Cell 28: under O1a the gap to the 3-D peri space is only 0.01–0.07, short of the 0.1 required. All 12 O1b readings pass, so the outcome depends on the stated O1a assumption. |
| fig6-dimensionality-trend | not_reproduced | Cell 30: under O1a the best k is 2, so there is no rise. The decline holds everywhere (−44 at k=20), but that alone is not the partial outcome. 3 of the 6 O1b readings pass. |
| fig6e-summary-rank | blocked: data_missing | Confirmed: there is no EMG and no A/B/J data. The J-array variant (cell 32) ranks peri top but not significantly above kinematic or initial vel., and all means are negative. |
| prep-dimensionality-7-to-10 | not_reproduced | Cell 34: 16–17 components under O1a and 5–6 under O1b; none fall in 6.3–11. Shuffling condition labels gives 17, so the O1a count measures noise. The O1b count is capped by the 7–8 units. |
| fig7a-shuffled-space-poor | reproduced (weak) | Cell 36: 12/12 pass. Under O1a the intact best is negative, so "below half of intact" is satisfied trivially. The real evidence is O1b (8 units): 0.209 intact vs −0.06 shuffled. |
| fig7b-window-start-slide | not_reproduced | Cell 38: 0/6 ratios within 0.97±0.097. The O1b ratios are 0.50–0.76; the O1a ratios divide negative numbers and mean nothing. The A/B part (0.94) cannot be tested on this dandiset. |
| ap-location-no-effect-j-array | reproduced (low power, proxy) | Cell 41: p ≥ 0.05 in 17/17 readings, and swapping the arrays only flips the sign. AP location is reduced to array identity, and n is 19 under the main reading. |
| ap-location-no-effect-other-datasets | blocked: data_missing | Confirmed on the archive. |
| fig7c-anterior-posterior-performance | blocked: other | Cell 44: the upper limit is ≤ 0 in 8/10 rows, so the normalised measure the criterion uses does not exist. Raw 6-D performance is about −1.1 to −1.5 at both sites. Which array is anterior is also unverified (problem 4). |
| prep-activity-more-anterior | blocked: metadata_insufficient | Cell 46: with prefix 1 taken as PMd, PMd 0.61 vs M1 0.70 (p=0.29) is not_reproduced. With the arrays swapped it would be partially_reproduced. Neither the file nor the API metadata says which array is which. |
| fig7d-pd-consistency | not_reproduced | Cell 48: peri wins only 7 of 12 comparisons and loses to segment dirs. in all 4. |
| fig8-linear-dynamics-simulation | reproduced | Cell 50: median \|r\| is 0.11 (disk) and 0.15 (square), below 0.3; median r 0.004/0.012 is within 0.08±0.3; minimum PD performance is 1.0. |

**B. Problems**

1. **[affects a conclusion] No noise control for fig4e, suppfig1 or the inclusion rule (cells 19, 21, 9).**
   - There are 1–4 trials per condition and split-half reliability is low (0.20 preparatory, 0.28 peri-movement).
   - I simulated untuned Poisson units with the helper functions and the same epochs and reaction-time spread (median about 320 ms). Mean r fell from 0.50 at −400 ms to 0.21 at −200 ms and −0.002 at onset. The largest 50 ms drop started at −260 ms. The suppfig1 spread fell from 8.3 to −0.55, with the strongest trace on top at −150 ms.
   - So both criteria pass on pure noise. The cause is that the go+100 ms end of the preparatory window sits about 200 ms before movement onset. The passes for these two claims carry no evidence.
2. **[affects a conclusion] The > 5 spikes/s range criterion admits noise (cells 14, 23, 34).** In my simulation, 63 of 93 untuned units passed it. In the data, median preparatory range is 6.6–10.2 spikes/s while mean preparatory rates are only 2.4–3.7 spikes/s, and only 13/142 units beat a condition-shuffled null (cell 46). The paper justifies the 5 spikes/s threshold by the high trial count ("acceptable given the higher signal-to-noise ratio provided by the higher trial count"), which this dandiset does not have. The notebook states the trial-count gap (cell 0) but never says how it affects selection.
3. **[affects a conclusion] Rankings, ratios and normalisations are taken on negative performances with no uncertainty (cells 23, 26, 28, 36, 38, 44).**
   - fig6d, fig6-each and fig6-maze are decided by mean differences of about 0.005–0.04, with no SE or test per reading; cell 32 shows these gaps are not significant.
   - fig7b ratios of negative numbers (1.24, 2.15) and fig7c normalisation by an upper limit ≤ 0 are undefined.
   - For O1b units, the "upper limit" (0.123) is below peri best (0.209), so it does not bound anything.
4. **[affects a conclusion] The array mapping is unverified and the promised swap is missing (cells 39, 44, 46; `load_train`).**
   - Cell 39 says "every result is also shown with the two arrays swapped". Only cell 41 does this, and only in a printed sentence. Cells 44 and 46 do not.
   - Every unit's electrode index points to the PMd group for both prefixes, so the "prefix 1 = PMd" reading has no support in the file.
   - The prep-activity-more-anterior outcome flips with the mapping, and the anterior > posterior part of fig7c depends on it.
5. **[affects a conclusion, fig7d] The fig7a/b/c/d cells were run on a subset of readings only (cells 36, 38, 44, 48).** They use 3, 3, 1 and 2 of the six O3/O4 configurations, and fig7d uses O1a only. O1b changed the outcome of fig6-maze and fig6-trend, so fig7d under O1b could differ and was not run.
6. **[does not affect a conclusion] The peri T matrix uses all 142 recorded units, untuned ones included (`leave_one_out_scores` in cell 23).** The Methods say "all neurons except the neuron whose preparatory activity we were trying to capture", which could mean recorded or included neurons. Only the first reading was run. Rates are not normalised, so near-silent units have little weight.
7. **[does not affect a conclusion] The `simulate_rotation` docstring mentions a `hold` that is never applied.** Holding a static state would change nothing.
8. **[does not affect a conclusion] Checks on the helpers passed.** On synthetic inputs, `loo_performance` matches brute-force leave-one-out (−0.289685 both). `pca_scores` and `leave_one_out_scores` match an SVD, and `n_components_for` returns 3 for a rank-3 matrix. The fig7a reflection, the epochs, the units and the delay > 400 ms rule all follow the claims file. Kinematic readings (a) and (b) are checked to be identical (cell 23).

**C. Not checked, and what would have allowed it**

- **A noise-only baseline in the notebook.** The same pipeline on condition-shuffled trials, or on preparatory and peri-movement means taken from disjoint trials, for fig4e, suppfig1, fig4d and fig6d. My simulation stands in for this but is not the notebook's data.
- **Which array is anterior.** Nothing in the file or the API metadata says, so the AP claims cannot be settled. Unit-level array labels from the source, or the swapped-mapping output for cells 44 and 46, would have helped.
- **Spread of the fig6d comparisons.** Per-reading SEs or paired tests (peri vs best other space) were not output, so I could not judge whether any of the 96 fig6d runs is more than chance.
- **fig7d under O1b and the remaining O3/O4 configurations.** These were not run.
- **Whether this session is the paper's J-array session.** The dandiset holds 27 of 108 conditions; data-to-paper provenance would be needed.
- **The figures.** Plots are images and were not inspected; all judgements rest on the printed tables.
