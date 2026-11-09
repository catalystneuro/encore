**A. Outcomes (32 claims in the claims file)**

| Claim | My outcome | Reason |
|---|---|---|
| fig1ab-baseline-transmission | blocked (data_missing) | I listed the zip's contents: only spike/position TS files from `big_box`, `stationary_cylinder` and `rotating_cylinder`. There are no slice recordings. |
| fig1cd-potentiation | blocked (data_missing) | Same as above. |
| figs1-avoidance-equal | blocked (data_missing) | There are no avoidance sessions in the zip. |
| unit-and-cell-counts | blocked (data_missing) | The deposit holds 8 WT and 7 Fmr1-null mice (cell 11; I confirmed this from the zip listing), against 12 and 9 in the paper, so the counts cannot be checked from a subset. Cells 226/334 need isolation measures. The cluster match in cell 11 (490/557) appears only when cluster-0 noise files are counted, which is a coincidence. |
| interneuron-proportion | partially_reproduced | WT is lower and the difference is significant (R1 p = 0.018, R2 p = 0.0009, cell 13). The percentages are far outside tolerance under every reading (WT 33.5–41.4% vs 12.4%; Fmr1-null 44.5–55.7% vs 29.3%). |
| place-cell-proportion | not_reproduced | No reading gives Fmr1-null lower (cell 15). R2 principal cells give Fmr1-null higher (53.0 vs 37.7%, two-sided p = 0.010). All counts and percentages are outside tolerance. |
| figs3-nonspatial-properties-similar | partially_reproduced | Burst probability and ISI (mean and median) show no genotype effect under R1. Firing rate does (R1 p = 0.004, R2 p = 0.0005), and burst probability does under R2 (p = 0.029) (cell 17). Width cannot be tested. |
| fig2-spatial-quality-similar | not_reproduced | Genotype effects for coherence (p = 0.003), active pixels (p < 1e-4), information (p = 0.008) and number of fields under reading (a) (p = 0.011) (cell 19). Only in-field rate and fields under reading (b) are null. The class effect holds. |
| tables1-place-cell-properties-similar | partially_reproduced | All five place-cell comparisons are null (cell 21). The interneuron rate differs (U test p = 0.0105, Fmr1-null higher). All 12 means are outside the Table S1 tolerances. |
| tables1-nonspatial-active-pixels | not_reproduced | 0.15 vs 0.22, U test p = 0.10 (cell 23). Variants: p = 0.09–0.23. Both means are outside tolerance. |
| figs4-remapping-similar | blocked (metadata_insufficient) | In the session table (cell 2), every box session is on a different date and uses a different cut file from that mouse's arena sessions. There are no waveforms, so the same cell cannot be identified across the two. Nothing is testable. |
| fig3b-place-cell-modulation-similar | blocked (data_missing) | No LFP. I confirmed this from the zip listing and the bucket's `filelist.txt`, which holds only `data.zip` and docs. |
| fig3bc-weaker-modulation-nonspatial-interneurons | blocked (data_missing) | No LFP. |
| fig3b-phase-preference | blocked (data_missing) | No LFP. |
| fig3d-stereotypy | blocked (data_missing) | No LFP. |
| overdispersion-passes | not_reproduced | Variances 3.69 vs 3.55 (R2), both outside tolerance. Levene p = 0.998. Under R1 the direction reverses (cell 27). Pass counts are about twice the paper's. |
| overdispersion-cells | not_reproduced | Means 3.68 vs 3.53, one-tailed p = 0.32 (R2); R1 is reversed (cell 29). Both means are outside tolerance. |
| fig4b-covariance-30-passes | partially_reproduced | t test on Fisher z: p = 0.023 (R2) and 0.033 (R1), Fmr1-null lower. WT mean 0.061 is within 0.09 ± 0.03; Fmr1-null mean 0.021 is outside 0.04 ± 0.01. Shuffle p = 0.21, consistent with the paper (cell 31). See problem 1. |
| fig4b-covariance-40-passes | partially_reproduced | The difference holds (p = 0.021). Both means (0.061, 0.020) are outside tolerance. It does not get larger, because the 40-pass threshold drops only one pair (cell 31). |
| fig4cd-kendall-place-cells | not_reproduced | 0 of 3 short timescales are significant under any of the 8 readings (cell 35). Under K1, 1 s and 5 s are significant (p = 0.001–0.05), which is the opposite pattern to the claim. |
| fig4d-network-state-recurrence | not_reproduced | No reading has ≥ 5 significant Fmr1-null half-tests; the most is 1 (K2/H2/R1). WT is significant at 2 timescales under K1/H2 (cell 37). WT PCo > Fmr1-null PCo at 5–6 of 6 timescales does hold. |
| kendall-nonspatial-pyramidal | not_reproduced | Under K1 the significant differences have Fmr1-null higher. The best reading gives 1 of 4 (cell 39). |
| kendall-quiet-states | not_reproduced | The low-speed reading: 25/40 ms are null as claimed, but 0 of 3 for 125 ms, 250 ms and 1 s (cell 41). The sleep/rest reading is blocked: there are no such recordings in the zip. |
| locomotion-similar | reproduced | Genotype p = 0.63 and interaction p = 0.67 with recordings as units; p = 0.44 and 0.32 with mice as units (cell 43). This is fragile (problem 7). |
| fig5b-frame-specific-ipos | partially_reproduced | Room frame: Fmr1-null higher with p = 0.012 under reading B (10/8 cells) but p = 0.21 under reading A (9/7 cells) (cell 47). Under B the arena frame is equally significant (p = 0.02), so the "only marginally" contrast is not seen. There are 3 mice per genotype, against the paper's 20/31 cells. |
| fig5c-ensemble-coordination | not_reproduced | Fmr1-null is higher in all 8 readings. The one significant result (p = 0.009) is in the wrong direction (cell 49). |
| figs6-room-frame-preference | partially_reproduced | Reading B: environment p = 0.0012 and interaction p = 0.58. The arena frame is below Stationary I by Tukey (p = 0.011) but not below Stationary II (p = 0.53). Reading A: environment p = 0.067 (cell 51). Room vs arena is not significant in either reading. |
| fig6-covariance-sem-predicts-errors | blocked (data_missing) | No avoidance sessions or shock-zone entries in the zip. |
| fig6-kendall-predicts-errors | blocked (data_missing) | Same. |
| discussion-single-cell-measures-no-relation | blocked (data_missing) | Same. |
| fig6-avoidance-behavior | blocked (data_missing) | Same. |
| figs5a-power-spectra-similar | blocked (data_missing) | No LFP. |

**B. Problems**

1. [affects a conclusion] Pass rule, `hc16.passes`, cells 25–31. The rule is read literally: the expected count in 5 s must be at least the cell's mean rate in AP/s. This passes almost every interval.
   - On a synthetic place cell it passed 340 of 360 intervals.
   - In the real data every place-cell pair has ≥ 39 joint passes (cell 31), so the 30- and 40-pass thresholds do nothing.
   - The 2/10/30 minimum-pass readings give identical samples (cell 29).
   - Pass counts are about twice the paper's.
   - The dimensionally consistent reading (expected count ≥ mean rate × 5 s, i.e. real in-field passes) was not run. The claims file names only the literal reading; this is a claims-file gap to report.
   - Affects overdispersion-passes, overdispersion-cells and both fig4b claims.
2. [affects a conclusion] Population, cells 0 and 9, `classify`. All non-zero clusters are used with no isolation criteria, and interneuron means only rate > 2 AP/s.
   - The interneuron fraction is roughly 3× the paper's for WT, and interneuron rates are 5–10 AP/s against the paper's 16.
   - The genotype effects in fig2, figs3 (rate) and the tables1 interneuron rate may come from misclassified multi-unit clusters.
   - The notebook says the data hold no isolation measures but never prints a full TS header to show this.
3. [affects a conclusion] Spatial scale, `Session.px_per_cm` and `pixel_index`. The scale is taken from the tracked extent and assumed enclosure sizes, and no variant was run (for example the code's 32 × 32 grid for single-cell measures). Place-cell active pixels (0.24 vs 0.45) and information (2.3 vs 1.57 bits/spike) are far from Table S1, so the place-cell classification and the fig2/tables1 measures may depend on this assumption.
4. [affects a conclusion] unit-and-cell-counts, cell 11, is treated as tested. The deposit is a subset (15 of 21 mice), so the claim is data_missing, not a mismatch.
5. [affects a conclusion] Rotating-arena claims, cells 45–51. The samples are 16–18 cells from 3 mice per genotype. The fig5b outcome changes between readings A and B, and the paper does not say which session classifies the cells.
6. [affects a conclusion] locomotion-similar, cell 43. Pooled across environments the interaction is null, but within each environment it is significant (box p = 0.021, arena p = 0.0076). The paper's 27 df fit neither 34 recordings nor 15 mice. The direction per environment is not printed.
7. [does not affect a conclusion] R2 counts the stationary-1 and stationary-2 sessions of the same day separately, so the same cells and pairs enter twice (cells 25–41). R1 is shown and agrees.
8. [does not affect a conclusion] `slow_mask` in cell 41 keeps a bin when the speed at its centre is below 2 cm/s, so 1 s and 5 s bins can include movement.
9. [does not affect a conclusion] The Tukey HSD in cell 51 ignores the repeated measures. The paired-t variant gives the same pattern.
10. [does not affect a conclusion] `ipos_series` counts the 10-visit minimum per 133 ms interval; the code counts it per position sample.
11. [does not affect a conclusion] figs4 is declared blocked in cell 0 with no code cell showing why. The evidence (dates and cut files) is only in the session table of cell 2.
12. [does not affect a conclusion] In cell 4, the 0–15 and 15–30 min parts of P0C2 do not match the full spike train, and this is not explained. Only full files are used.

What checked out:
- `kendall_tau_b` matches scipy's tau-b exactly.
- `information`, `coherence`, `fields`, `prop_test` and `passes` behave correctly on synthetic inputs (Poisson z variance 0.995).
- The `.times` files match 107 of 107 cells, and the clock re-estimation (spikes 0–1 sample after their sample's time) is sound.

**C. What I could not check**

- Whether the TS headers carry isolation measures (IsoIBG/IsoINN) or a spatial scale. Printing one full header would settle it.
- Problem 1. The overdispersion and covariance results under the expected count ≥ mean rate × 5 s rule, with pass counts and the per-pair joint-pass distribution.
- Problem 3. Class counts and Table S1 measures on the 32 × 32 code grid, to see whether classification depends on the assumed scale.
- Problem 6. Speed change per genotype within each environment, and which recordings give 29 units.
- fig4cd. Per-mouse Kendall results with M16 left out (it supplies 52 of the 122 WT pairs), to tell a mouse effect from a genotype effect.
- fig5b. Per-cell values under readings A and B, to see which cells drive the difference.
