# Verification report, round 1: Grosmark & Buzsáki 2016 on dandiset 000044 (0.261005.2101)

The claims file has 20 claims. The notebook tests 11 and blocks 9 as `methods_underspecified`. Sources I used: the PMC main text and figure legends, saved under `paper/`. The supplement link on PMC returned a browser-check page, so I could not read it either.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| sessions-and-tracks | reproduced | Cell 13: 4 subjects and 8 sessions, all with PRE, MAZE and POST in order. Tracks are 1.6 m linear (4 sessions), 2 m linear (1) and circular (3), which matches "two linear and one circular". |
| place-cell-count | not_reproduced | Cell 15: 417 place cells at 1 Hz, against 491 ± 49. The 0.5 Hz variant gives 480, which is inside tolerance, so the claims file's statement that the variants "do not change the outcome" is false. |
| fig1c-post-gt-pre | not_reproduced | Under the fixed pooled criterion, POST mean rZ (0.763) is below PRE (0.770) and the Tukey-on-ranks p is 0.41 (cell 17). Within sessions, all 8 have POST > PRE, 6 of 8 have p < 0.05, and the pooled test after subtracting each session's PRE mean gives p = 2e-14 (cell 21). The failure comes from pooling across sessions (problem 2). |
| fig1c-maze-gt-pre | reproduced | MAZE mean 1.270 against PRE 0.770, Tukey p ≈ 0, and 8 of 8 sessions have MAZE > PRE (cell 17). |
| fig2b-strong-contributors | blocked (methods_underspecified) | I agree with the block. 307 cells pass against 216, but the fixed test flags 58% of cells when every rate map is shifted (cell 23). The paper's per-cell shuffle test is in the unavailable supplement. The miscalibration comes mainly from the pipeline, not only from the test (problem 1). |
| fig2-pre-post-overlap | blocked (methods_underspecified) | Follows from fig2b. The fixed test gives 93.5% against 73%, with a chance level of 69.8% (cell 25). The paper states no chance level. The shift-test variant gives 81.5% against a chance level of 45.8%. |
| fig2d-shuffle-high-dpcc | partially_reproduced (uninformative) | This claim does not use the strong-contributor selection: it ranks all place cells by dPCC. The block reason therefore does not apply. By the criterion, replay is absent after shuffling the top 10% or 20% but also absent after shuffling the bottom 75% (p = 0.35). However, the unmanipulated baseline has no pooled replay either (p = 0.92, cell 31), so "eliminated" cannot be judged. The within-session variant does show the paper's pattern: top 10% p = 0.20, top 20% p = 0.83, bottom 75% p ≈ 0. |
| fig2e-remove-plastic | reproduced (by criterion; circular) | Replay is absent without plastic cells (p = 1.0) and present without rigid cells (p = 0.020) (cell 35). The result is circular (problem 3), and with the shift-test classes, removing rigid cells leaves no replay (p = 0.11). |
| figs2-track-distribution | not_reproduced | KS p = 0.034 (cell 37). This is fragile: p = 0.051 under reading (b) and 0.12 under the shift-test variant. |
| fig3a-plastic-specificity | partially_reproduced | Spatial information is higher in plastic cells (p = 3e-4). The number of fields does not differ (p = 0.52) (cell 39). |
| fig3b-plastic-improve | partially_reproduced | Both groups increase: plastic p = 0.015, rigid p = 0.032 (cell 41). |
| fig4a-rigid-faster | not_reproduced | Rigid cells have the higher median, but p = 0.059 (cell 43). |
| fig4a-plastic-ripple-burst-coactivation | partially_reproduced | Gain is higher in plastic cells (p = 0.037). Bursting (p = 0.20) and coactivation (p = 0.79) are not (cell 45). |
| fig4c-pre-fast-coactivation | reproduced | Spearman rho is 0.861 on the averaged curve and 6 of 8 sessions are positive (cell 47). |
| fig4c-slow-coactivation-increase | not_reproduced | rho is −0.068, against a threshold below −0.5. 5 of 8 sessions are negative (cell 47). |
| fig4c-slow-replay | not_reproduced | rho is 0.095 and 4 of 8 sessions are negative (cell 47). |
| rate-split-medians | partially_reproduced | Both readings give a low-rate median of 0.435 Hz, outside 0.351 to 0.429, and a high-rate median of about 1.09 Hz, inside 1.008 to 1.232 (cell 51). The strict "both medians" criterion fails. The variant using the rate over all of PRE and POST (0.395 and 1.041 Hz) fits both. |
| figs16-low-rate-info-gain | partially_reproduced | Spatial information is higher in low-rate cells (p = 4e-8). The gain change is not (p = 0.95) (cell 53). |
| fig4d-slow-sequences | not_reproduced | Under the pooled criterion, replay is absent for both low-rate (p = 0.96) and high-rate (p = 1.0) templates (cell 55). The within-session variant finds replay in both, larger for low-rate cells (0.116 against 0.058), which would be partial. |
| fig4e-gain-sequences | not_reproduced | Under the pooled criterion, replay is absent for both groups (cell 57). The within-session variant finds high-gain p ≈ 0 and low-gain p = 0.14, which would meet the criterion. |

Archive check for the 9 blocked claims: the 8 assets of 0.261005.2101 (5 to 9 GB each) hold units with cell type, linearized and 2D position, 128-channel LFP and sleep states. Nothing data-related is missing. The blocks are purely about method. Five of the nine (fig2d, plus figs2, fig3a, fig3b and both fig4a claims on dPCC-based groups) can be and were evaluated. Only the absolute count of 216 and the 73% figure depend directly on the paper's unknown significance test.

## B. Problems

1. **[affects a conclusion]** `cell_contributions` and `decode_events` produce a biased contribution measure. On linear tracks each event is scored with whichever of its two templates gives the larger rZ, and the cell's contribution compares against that winning |r|. Shifting any one cell's map then lowers |r| on average, so contributions come out positive even on noise. Each cell's 20 shifts are also reused across thousands of events, so the event-level signed-rank test counts the same few shifts over and over.
   - Synthetic noise events, run through these same functions: false-positive rate 100% with two templates and 40% with one.
   - This explains cell 23's false-positive rate by track (0.85 to 0.90 on linear tracks, 0.16 on the circular track) and why 28 to 31 of 30 to 31 place cells per linear session come out "strong".
   - The notebook calls the cell-level shift test "better calibrated", but it still has a false-positive rate of 0.30.
2. **[affects a conclusion]** The pooled across-session replay criterion (cell 17 and `replay` in cell 31) suffers from Simpson's paradox.
   - Circular-track sessions contribute 47% of POST events but 36% of PRE events, and they score about 1 rZ lower (cell 21).
   - As a result, the unmanipulated baseline shows no pooled replay (p = 0.92), so every "absent" result in fig1c-post, fig2d, fig4d and fig4e cannot distinguish anything.
   - The within-session variant reverses fig1c-post and fig4e, and gives partial for fig4d.
3. **[affects a conclusion]** Circularity in cell 31 (fig2d and fig2e). dPCC is computed from the same PRE and POST events that are then decoded again. Removing or shuffling high-dPCC cells lowers POST minus PRE by construction. There is no control that shuffles or removes a random X% of cells.
4. **[affects a conclusion]** fig2d is marked blocked because of the PCC test, but `variants_for` (cell 31) ranks all place cells by dPCC and never uses the strong-contributor selection.
5. **[affects a conclusion]** place-cell-count (cell 15): the count depends heavily on the threshold (0.5 Hz gives 480, inside tolerance), which contradicts the claims file. The outcome at the fixed 1 Hz stays not_reproduced.
6. **[does not affect a conclusion]** The re-decoded base in cell 31 uses 50 shuffles, so its rZ (PRE 0.795, POST 0.787) differs from the first pass (0.770, 0.763). Comparisons inside the variant table are internally consistent.
7. **[does not affect a conclusion]** `ranks_tukey` uses scipy's `tukey_hsd` on ranks, not a Kruskal-Wallis-based Tukey-Kramer. With n above 2,000 per group the p-values are 0 or 0.41, far from any threshold.
8. **[does not affect a conclusion]** `prepare_session` defines MAZE immobility from 2D speed, while running for the rate maps uses linearized speed. Spikes from the same events could overlap slightly with the template data.
9. Helpers I checked on synthetic inputs, with no defects found: `column_cycle_null` matches brute force to 1e-15; `weighted_r` returns ±1 on diagonals; `spatial_info` returns 0 and log2(50); `place_fields`, `burst_fraction`, `partial_corr`, `in_intervals` and `rate_map` (peak at the right bin) all behave correctly.

## C. What I could not check, and the output that would have let me

- **The paper's PCC test and other definitions.** These are in the supplement, which is behind a browser check on PMC; the main text only says "cell-specific shuffling technique". Needed: the supplement text.
- **Size of the contribution bias in the real data.** Needed: PCC false-positive rates recomputed with each event's template fixed in advance (not chosen by maximum rZ), and with a fresh shift drawn per event.
- **Whether fig2d and fig2e are circular.** Needed: rows in cell 31 for shuffling or removing a random 10, 20 and 75% of cells.
- **Whether the pooled tests are driven by the circular track.** Needed: per-track (linear only) versions of the cell 31 replay table and of cell 17.
- **Whether the event pipeline matches the paper.** Needed: event counts per session set against the paper's figs. S2 to S4 (also in the unavailable supplement), plus per-session rZ distributions for MAZE.
