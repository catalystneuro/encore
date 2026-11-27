**A. Outcomes** (38 claims in `souza-2026.yaml`; the notebook tests all 38 and marks none blocked)

| Claim | Outcome | Reason |
|---|---|---|
| data-sessions-units | not_reproduced | Under the criterion's readings (a) and (b), cell 5 gives 153 sessions / 81 mice / 110,563 or 45,354 units, more than 10% off all three counts. The archive API agrees: 153 session files, 81 subjects. The notebook's own selection (Sst/Vip mice, "good", presence ratio ≥0.95) gives 104 / 54 / 54,045: close, but not exact and not a reading the criterion lists. |
| blocks-no-reward-in-replay | reproduced | Cell 13, in all 104 sessions: block 0 is active, block 5 passive, same image sequence, every reward in block 0, 0 licks and 0 rewards in block 5. |
| reward-interval-min | reproduced | Cell 15: minimum 6.972 s against 6.96 ± 0.696. |
| latency-change-to-reward | not_reproduced | Cell 17. Using change-presentation times: median 0.4065 s (outside 0.467 ± 0.047) and 4.31% of hits beyond 250 ms (outside 3.8 ± 0.38). Using `change_time_no_display_delay`: median 0.451 within, but 4.20% still outside. Hits 15,592 (within tolerance) and SD 0.111 (within) under both. |
| lick-reward-coincide | partially_reproduced | Cell 19: median 9.78 ms and 95th percentile 17.32 ms match. The criterion also needs every delay ≤22 ms; 5 of 15,592 exceed it (max 53.5 ms). |
| fig1e-cohort-size | partially_reproduced | Cell 21: cohort 10,822, testable (a) 34,959, suppressed 7,378, enhanced 3,444, 68.2% suppressed, 11,108 significant in both families: all within tolerance. Discordant signs 286 against 239 ± 24 is outside. |
| fig1d-split-half-above-null | reproduced | Cell 25: both readings hold in all six areas. Reading (b) holds by construction (see B6). |
| fig1c-example-cells | reproduced | Cell 27: 8 enhanced VISam units with r ≥0.99; 32 suppressed VISrl units with r ≥0.98. |
| fig1e-suppressed-fraction-by-area | reproduced | Cell 29: all six fractions within tolerance (87.1 to 53.6%); VISp highest, VISam lowest; VISp n = 2,421 and 2,108 suppressed, VISam n = 1,637, all within tolerance. |
| fig1l-session-gradient | partially_reproduced | Cell 31: VISp 0.911 is within tolerance and Kruskal-Wallis p = 3.8e-17. VISam 0.575 is just above the 0.572 bound. |
| latency-jitter-control | reproduced | Cell 33: 99.14% (range 98.97 to 99.23) against 99.2 ± 0.8; Spearman 0.9959 against 0.996 ± 0.004. |
| waveform-ambiguous-band | not_reproduced | Cell 35. Duration (a): 1,292 and 6,510 ambiguous against 849 and 1,280, and the fit is degenerate (see B1). Duration (b): 405 and 110 against 849 and 227. Only one count (1,205 against 1,280) is in tolerance under any reading. |
| fig1jk-narrow-fraction-by-area | reproduced | Cell 38, duration (b), whole cohort: VISp 25.0%, VISrl 27.1%; the other four areas at 15.2 to 20.1%, inside 12.6 to 20.9%. |
| fig1h-median-isi-narrow-broad | reproduced | Cell 40, duration (b), ambiguous excluded, whole recording: 42.2 / 88.0 ms with n = 2,245 / 8,467, all within tolerance. |
| fig1gi-waveform-separation | reproduced | Cell 42: narrow units have lower median half-width and lower median ISI under both durations. |
| narrow-more-suppressed | reproduced | Cell 44, duration (b): 0.815 / 0.647, and 0.647 with the 0.3 to 0.7 band, all within tolerance. Duration (a) also passes. |
| narrow-more-suppressed-within-layer | reproduced | Cell 62, duration (b), reading (a): narrow higher in 89.0% of 82 sessions, p = 1.6e-11. |
| fig1mn-modulation-index-negative | partially_reproduced | Cell 46: all per-area medians are negative and 75.3% have M < 0 (within tolerance). The median M of -0.174 is outside -0.1323 ± 0.013, smoothed or not. |
| fig1m-narrow-stronger-m | reproduced | Cell 48: narrow median M is below broad under every reading. |
| m-baseline-sensitivity | not_reproduced | Cell 50, baseline -1.5 to -1.0 s: median -0.041 (outside -0.0351 ± 0.0035); enhanced units with M < 0 2.4% (outside 1.9 ± 0.19); VISpm median stays negative (-0.002). VISp is the most negative area under all four baselines. |
| layer-assignment-coverage | not_reproduced | Cell 54: layers assigned to 97.2% of units / 97.3% of the cohort (against 87.5 / 84.9%) and to 97.4% in VISrl (against 48.0%). Only area agreement (66.0% against 63.5%) is within tolerance. |
| layer4-suppression | reproduced | Cell 56, reading (a): 86 sessions, 71 with layer 4 higher, median +0.118, p = 8e-10. |
| layer4-within-waveform | not_reproduced | Cell 58: under every reading, at least one excess and the 6a narrow percentage are outside tolerance. Duration (a) narrow p = 1e-5, which misses p < 1e-6. |
| layer4-controls | not_reproduced | Cell 60: rate-matched +0.125 (against 0.178), unmatched +0.122 (against 0.148), ≥50 µm +0.142 (against 0.176), and 80 sessions (against 72) are all outside tolerance. The partial clause's 50 µm count therefore fails as well. |
| fig2c-cv-lower | reproduced | Cell 66, rate r1, ≥5 RW+ units: RW+ lower in all six areas at p < 1e-7; median CV 0.596 / 0.818; per-area differences -0.139 to -0.247, all inside -0.126 to -0.253. |
| cohort-faster-firing | reproduced | Cell 68, with the 0.2 Hz filter: 4.75 / 2.83 Hz, per-area ratios 1.49 to 1.89. |
| cv-rate-matched | partially_reproduced | Cell 70: the pooled difference shrinks from -0.194 to -0.048 (outside -0.06 ± 0.006). p < 0.01 holds only in VISl, VISal and VISam; VISp (p = 0.025) and VISpm (p = 0.12) fail. |
| cv-unmatched-reverses | partially_reproduced | Cell 72: the pooled median difference is positive (+0.041), but RW+ is the smaller group in only 555 of 576 session-area pairs, not all. |
| fig2d-cv-correlations | partially_reproduced | Cell 74, reading (a): 0.523 / 0.416 / 0.354, in the paper's order and within tolerance. Only 62 of 66 pairs reach z ≥15 against the circular null (min 13.8). |
| cv-correlation-block-excess | partially_reproduced | Cell 76: median excess 0.158 (outside 0.21 ± 0.021); 83% of sessions (within tolerance); p = 1.8e-12, which misses p < 1e-13. |
| fig2f-pre-post-cv | not_reproduced | Cell 78: RW- rises in all 12 cells, but RW+ is significant in all 12 cells; only 7 of 12 match the paper's pattern, below the 8 the partial clause needs. |
| fig3a-archetypes | reproduced | Cell 81, peaks taken as max absolute value: roles fit under both initialisations (-445, -285, -185; -35; 1385 ms). Matrix is 10,822 × 200. |
| fig3b-mixtures | not_reproduced | Cell 83: hard-assignment variance explained 0.53 to 0.55 against 0.36; the mixture-to-hard ratio is 1.3 to 1.4, below the 1.5 the partial clause needs; dominated units 0.89 to 1.87% against 1.0 ± 0.1. |
| fig3c-area-overlap | not_reproduced | Cell 85: η² 0.011 to 0.021 against 0.004, above the 0.01 the partial clause allows. |
| fig3d-anticipatory-gradient | reproduced | Cell 87, reading (a): VISp 91.4%, VISl 78.6%, the other four areas 68.8 to 72.8%. |
| anticipatory-direction-overlap | partially_reproduced | Cell 89, reading (a): agreement, both anticipatory percentages, the gradient (0.227) and the standardised gradient (0.066 / 0.069) are within tolerance. φ = 0.622 is just above the 0.616 bound. |
| hits-vs-false-alarms | not_reproduced | Cell 91: 2 to 10% of the cohort significant against 14.6 to 22.2%; VISp median SI -0.67 / -0.77 against -0.56; median false alarms per session 4.5 (outside 4 ± 0.4). |
| hits-vs-lick-bouts | partially_reproduced | Cell 93, 500 ms gap, baseline (b): 438 bouts per session and every area at 71 to 88%, within range. VISp median SI -0.13 against -0.50 is outside under every reading. |

Tally: 17 reproduced, 10 partially_reproduced, 11 not_reproduced, 0 blocked. The paper states no chance level for any selection, so there was none to compare.

**B. Problems**

1. **[affects a conclusion] Duration reading (a) does not split narrow from broad** (cell 35, `classify`; `vbn.wf_measures`). At the seed used, the two component means are 0.534 and 0.616 ms, although the 10th percentile is 0.30 ms. Seeds +2000 to +4000 converge to a different solution (0.57 / 1.425 ms, 45 ambiguous units). `wf_dur` has only 60 distinct values (1/30 ms steps) and correlates with the stored duration at only r = 0.66. Every reading-(a) waveform result is therefore not a narrow/broad split, and the notebook makes (a) the default labels (cell 36). Outcomes above rest on reading (b).
2. **[affects a conclusion] The waveform channel is picked by an unchecked row layout** (`process_session`, `W[wf_start + probe_channel_number]`). This assumes each unit's `waveform_mean` rows are ordered by probe channel number with all channels present. It is never checked, and it may explain B1.
3. **[affects a conclusion] Only one reading of the ISI null was run** (`isi_null`, cell 21). The criterion's open detail (1b), reshuffling over the whole recording, was not run. It changes the split-half gate that every cohort claim depends on, and fig1e-cohort-size sits at partial.
4. **[does not affect a conclusion] 100 permutations instead of the paper's 1,000** (cells 7 and 23). This is stated as a deviation. It was checked on only 100 units of one session, where 76 units passed with 100 permutations against 80 with 1,000; the p floor is 0.0099.
5. **[affects a conclusion] Session selection is outside the criterion** (cells 5 to 7, `select_units`). Wild-type mice are excluded and the quality filter is "good" with presence ratio ≥0.95. The paper names neither. This is stated as an assumption and is reasonable given the 54-mouse match, but it is not an exact match either: 104 sessions against 103, 6 extra units. No single dropped session can explain both differences, since the smallest session has 262 units.
6. **[does not affect a conclusion] fig1d reading (b) is true by construction** (cell 25). Every cohort unit passed BH on p_split ≤0.04, so it must exceed the median of its own null.
7. **[does not affect a conclusion] Denominator (b) in layer4-controls is degenerate** (cell 60). It uses `test_a`, which already requires a split-half positive unit, so the detection rate is 100% / 100%. The criterion's reference to fig1e's testable set should have used reading (b) or (c) there.
8. **[does not affect a conclusion] `split_layer` maps "CA1" to layer "1"** (tested on synthetic input). Only 17 units carry layer 1, so the effect is negligible.
9. **[does not affect a conclusion] Layers are assigned to any CCF structure with a laminar suffix** (`unit_layers`), including SSp-bfd, TEa and VISli. This follows the claims criterion. The paper's 48% coverage in VISrl suggests it used a stricter rule, but no other reading is open in the criterion.
10. **[does not affect a conclusion] False-alarm change times can mix two clocks** (`session_events`). A false-alarm trial without a sham time falls back to `change_time_no_display_delay`, a different clock from the presentation times. The number of fallbacks is not printed; the cell 91 count of 516 "with a sham change time" includes them.
11. **[does not affect a conclusion] The averaged RW- series is less noisy than RW+** (cell 74). RW- CV(t) is the mean of 20 draws, which lowers its noise relative to the single RW+ series. That may inflate the RW- block correlations in fig2d and cv-correlation-block-excess. It follows fig2c reading (a).

Helpers checked on synthetic data: `_wilcoxon_rows` matches scipy's approximate Wilcoxon exactly; `bh` matches statsmodels' BH; `split_psth` matches a naive histogram, with and without the lookup table; `wf_measures`, `cv_windows` and `rank_biserial` behave correctly.

**C. Not checked, and the output that would allow it**

- The `waveform_mean` row layout. Needed: per unit, the number of rows, and the row with the largest peak-to-trough amplitude compared with `probe_channel_number`.
- The reading-(a) mixture fit. Needed: a histogram of `wf_dur` and the log-likelihood of each seed's solution.
- The cohort under ISI-null reading (1b), and under 1,000 permutations for all units.
- Which session and units account for the 104/103 and 54,045/54,039 differences. Needed: per-session unit counts and session dates.
- How many false-alarm trials use the `change_time_no_display_delay` fallback.
- Layer coverage under a stricter rule (layer only when the CCF structure is a visual area), to see whether it gives 87.5% overall and 48% in VISrl.
- Why the notebook has 15,592 hits against the paper's 16,330. Needed: hits per session, and hits excluded by the reward-window filter.
