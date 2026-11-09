**A. Outcomes** (20 claims in the claims file; 14 tested on recorded data, 2 simulation-only, 4 others blocked)

| Claim | My outcome | Reason |
|---|---|---|
| dishes-analysed | reproduced | Cell 12: under S1 with "only a recorded day without activity breaks the run", all 7 dishes have runs of more than 10 days (11 to 33). It is fragile: if a missing date also breaks the run, the count is 6 (dish 23317 has a 10-day run), and under S2 it is 2 or 4. The claims file allows S1 or S2; the missing-date rule is the notebook's own reading (problem 6). |
| activity-onset | blocked (metadata_insufficient) | Confirmed in the archive: no DIV or plating date. The age field is the same `P18D` on the first and last recordings of dishes 19880 and 23302, so it is not DIV. Cell 14 can only show that 3 dishes are near silent on their first recording. |
| fig1b-async-to-bursts | reproduced | Cell 16: Spearman of both synchrony measures with day is positive with p ≤ 0.007 under S1 and S2. With d0 = 2 or 3 the late dish median beats the early one in all 8 cases. With d0 = 1 that comparison fails for sync_frac under S1 and for both measures under S2. d0 = 1 means activity at 1 DIV, which contradicts the paper's 2 to 3 DIV. Per dish, 2 of 7 trends are negative. |
| fig1d-power-law-emerges | blocked (methods_underspecified) | Cells 9, 19 and 20: active recordings have b ≈ 0.001 to 0.03, and no dish meets the criterion under any reading. My synthetic test shows uncorrelated Poisson data give the same b (≈ 0.008). With x = rank over all ranks, b ≥ 0.1 would need λ₁₀₀/λ₁ ≲ e⁻¹⁰, so the paper's 0.1 threshold cannot be the same quantity as the b computed here. The fit-range variants (top 30 or 100 PCs, x/n) don't separate early from late either. |
| fig1e-example-dish | blocked (methods_underspecified; also no DIV) | Cell 23: b < 0.1 from the first recording in nearly every dish, which only reflects the scale problem above. Exponent readings (b) and (c) were never computed. |
| fig1f-transition-15div | blocked (methods_underspecified; also no DIV) | "Established" rests on the 0.1 threshold. The part that needs no threshold: Spearman of b with day is negative under all 4 readings but significant only under S1/F1 (ρ −0.256, p 0.004). |
| fig1f-exponent-1p2 | blocked (depends on fig1f-transition-15div) | For the record, median c after the "transition" is 0.76 to 0.82 (F1) and 2.25 to 2.34 (F2). Neither is within 1.2 ± 0.12. |
| fig1d-shuffle | blocked (methods_underspecified) | Cell 25: the "Exponential group" has 0 to 6 near-silent recordings because of the scale problem. Shuffled b ≥ 0.1 in at most 4.5% of late recordings, which is structurally expected. |
| fig2b-spatial-structure | partially_reproduced | Cell 32: at about 15 DIV the first 10 PCs are more local than the last 10 in 7/7 dishes, for S1 (M1 and M2) and S2/M2. The early half fails: at about 3 DIV the locality ratio is within 10% in only 0 to 2 of 7 dishes there. It passes only under S2/M1, where fig2c fails. No reading satisfies both fig2b and its dependency fig2c. |
| fig2c-locality-spectrum | blocked (methods_underspecified) | Cell 27: the readings disagree. It holds only under M2 with L1 (ρ −0.32 for S1, −0.40 for S2, p < 0.001), and fails under M1 and under L2 (w_ii = 0). Even under M2/L1 the early slope is not flat (median −104 at 3 to 5 DIV against −106 later, d0 = 2). |
| fig2d-locality-slope | not_reproduced | Cell 34: no reading holds. The moving average falls under M2/L1 (ρ −0.73 to −0.77), but its first value is 19% of the most negative one, above the 10% bound for "absent". |
| fig2d-shuffle-locality | partially_reproduced | Cell 36: shuffled slopes are less negative under every reading (Wilcoxon p < 1e-7). "Nearly independent" (below 10%) fails for M2/L2 in every set (ratios 0.12 to 0.73), and the criterion requires all of M1, M2, L1 and L2. |
| fig3c-avalanches-emerge | blocked (metadata_insufficient) | The exponent part needs no DIV and could be tested. Under reading (b) and S1 it fails for every fit and size reading: median c is 1.71 to 1.99 against 1.5 ± 0.15 (cell 38). The shift DIV for d0 = 1 to 3 would be about 3.5 to 6 (F1) or about 25 (F2), not 15 ± 1.5. Reading (a) and S2 were not computed. |
| fig3d-decay-rates-correlated | not_reproduced | Cell 41: Spearman and Pearson are both positive with p < 0.05 under none of the 8 readings. Only S1/F1/A2 has a significant Pearson (0.48), and its Spearman is not significant. |
| fig3ef-groups-cooccur | blocked (methods_underspecified) | Cell 44: the 0.1 split leaves 0 to 6 recordings in the Exponential group (scale problem). |
| figs1-classified-by-avalanches | blocked (methods_underspecified) | Cell 45: grouping by avalanche b works, but the test needs PCA b ≥ 0.1 in the Exponential group, which the scale problem rules out (median 0.01). Reading (b) was not computed. |
| figs2-shuffle-breaks-cooccurrence | blocked (methods_underspecified) | Cell 47: the readings disagree. (a) fails everywhere, partly because shuffled PCA b cannot reach 0.1. (b) holds for A1 in 3 of 4 readings and fails for A2. |
| no-temporal-structure | not_reproduced | Cell 49: only 22% to 45% of recordings from 15 DIV on lack a significant negative ρ, under both time-scale readings and every d0. So dominant PCs do have longer time scales in most recordings. Effect sizes are small (problem 7). |
| fig4d-cauchy-model-power-law | blocked (methods_underspecified) | The model is not specified in the text, as the claims file says. |
| fig4d-gaussian-model-no-power-law | blocked (methods_underspecified) | Same as above. |

**B. Problems**

1. [affects a conclusion] Possible misreading in the claims file ("Fit"). Taking x = PC rank over all positive ranks cannot produce b on the scale of the paper's 0.1 threshold: real data and an uncorrelated synthetic null both give b ≈ 0.005 to 0.008. Under the claims file's own rule (block only where readings disagree), F1 and F2 agree here, and the claims would come out not_reproduced rather than blocked. The 0.1-threshold claims are blocked for this reason, so the x scaling or fit range should be raised with the authors. The Methods say "mean squared error with respect to variance spectrum", which points to F2 if anything.
2. [affects a conclusion] Cell 38 (fig3c) is incomplete:
   - only reading (b) and S1 are computed; reading (a), the pooled 3-day moving average, is missing;
   - `pivot_table` silently drops dish 23302 (all NaN);
   - the dish medians skip dishes whose b never stays below 0.1, which biases the shift DIV early.
3. [affects a conclusion] For fig1b and the windowed claims, d0 is one value for all dishes and only 1 to 3 were run. Five dishes are already active on their first recording, so a larger d0 is plausible for them, and per-dish d0 was not explored.
4. [does not affect a conclusion] Cell 23 (fig1e): exponent readings (b) and (c) are not computed, and `fit_power` is defined but never used.
5. [does not affect a conclusion] Cell 45 (figs1): reading (b), pooled spectra per avalanche group, is not computed.
6. [does not affect a conclusion] Cell 12: rule (ii) is the notebook's own reading of "continuously" and decides 7 against 6. Under S1 every recording counts as active, so the count only measures recording coverage.
7. [does not affect a conclusion] In `time_scales`, tau_e is quantized to 100 ms, and the median for both the top-10 and bottom-10 PCs is one bin. Significance across about 1,000 PCs comes from small, tie-heavy differences (median ρ −0.09 to −0.39). The outcome follows the criterion, but the evidence is weak.
8. [does not affect a conclusion] Under each fit reading, one of the two b's in fig3d sits mostly at the bound 0: avalanche b under F1 (≈1e-15), PCA b under F2 (≈1e-17). The correlation tests are run largely on bound-hitting values.
9. [does not affect a conclusion] `fit_decay` with F2 drops zero-count cascade sizes even though the fit is on raw values, where zeros are valid data. This biases the avalanche b under F2.
10. [does not affect a conclusion] Under S1 the absolute L1 slope grows with the number of electrodes kept. S2 keeps electrode counts nearly constant and gives the same result for fig2c.
11. [does not affect a conclusion] Smaller points:
    - Cell 32: ties toward the earlier day pick the near-silent day 0 as "3 DIV" for dish 19880.
    - `analyse`: rates count spikes after 1,800 s, but the bins drop them.

The helpers I tested synthetically behave correctly: `fit_decay` recovers known (b, c) under F1 and F2, `avalanche_distribution` gives correct A1 and A2 sizes, `locality` scores a smooth map above a random one, `time_scales` gives about 1.1 to 1.2 s for an AR(1) process with τ = 1 s, and `circular_shuffle` shifts each row correctly.

**C. Not checked**

- **DIV text in the files.** I could not confirm the NWB string "Days in vitro are unknown" without downloading; I checked only the asset metadata (constant age, session description). Printing the NWB subject and session description fields would settle it.
- **Fit quality.** I could not judge PCA fits or the b scale directly. Printing λ₁/λ₁₀ and λ₁/λ₁₀₀ for early and late recordings, and the share of b values at the bound (below 1e-8) per reading, would have allowed it.
- **Avalanche-claim readings.** fig3c reading (a) and S2, fig1e readings (b) and (c), and figs1 reading (b) were never computed, so I could not apply those parts of the criteria.
- **Time-scale distributions** per PC, beyond medians, were not shown.
