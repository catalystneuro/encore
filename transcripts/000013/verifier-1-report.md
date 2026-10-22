**A. Outcomes** (45 claims, counted from the claims file. My tally: 23 reproduced, 4 partially reproduced, 10 not reproduced, 8 blocked.)

| Claim | Outcome | Reason |
|---|---|---|
| recordings-counts | reproduced | Cell 21 gives 31/10/11 cells and 115.0 ± 60.6 trials. |
| recordings-mice | not_reproduced | Cell 23 finds 23 subjects, not 21; the archive API also lists 23 `sub-*`. C57BL6 has 9 mice/22 neurons (paper 7/21) and Ai32×PV 3/7 (paper 3/8). Recordings (52) and PV-Cre (8/17) match. |
| behavior-performance | reproduced | 0.741 ± 0.085 (cell 25). |
| behavior-sample-epoch | reproduced | Reading (a): 2.394 s mean, 1.543 to 4.049 s, all within tolerance (cell 27). |
| behavior-whisking-bouts | not_reproduced | Mean bout duration is 70 to 92 ms against 261 under all four claimed combinations (cell 29). Only the non-claim variant of bouts with at least one cycle reaches the duration, and its amplitude then fails. |
| behavior-touches-reaction | not_reproduced | Touches before the response are 3.00 (reading a) and 3.51 (reading b), against 2.33 ± 0.233. The reaction time of 190 ms passes only because its s.d. is 700 (cell 31). |
| example-cell-rates | reproduced | Cell 23: 0.727 / 1.754 spikes/s, 2.41-fold, p = 1.4e-7. Its pooled rates give 1.909 and 2.63 (cell 33). |
| example-cell-sample-ff | reproduced | Reading (a), cell 23: FF = 7.51 (cell 35). |
| example-cell-touch-window | not_reproduced | Time fraction is 19.0 to 20.2% against 15.3 ± 1.53 in all 8 criterion readings (cell 37). |
| example-cell-ff-around-touch | reproduced (weak) | Cell 23 fails: pre-touch mean count is 0.003 against 0.03. Under reading (b) one cell (cell 11, one touch group) matches out of about 600 cell × group tries, which is what the criterion asks (cell 91). |
| text-spikes-per-touch | reproduced | Reading (a), cell 23: 1.47 to 1.51, 0.302 to 0.307, latency 8 ms (cell 39). |
| text-whisking-rates | not_reproduced (provisional) | Cell 23's non-whisking rate of 0.227 matches 0.23. Its whisking rate is 1.26 against 0.67, but the whisking mask is not the Methods' (problem 1). |
| example-cell-phase-modulation | reproduced | Depth 1.000 and zero rate at phase 0, but from only 13 spikes (cell 43; problem 3). |
| table1-l4-c2 | reproduced (marginal) | Exactly 15 of 18 under the criterion readings, the threshold. The failures are the spt_first median, the depth median (1.0, problem 3) and the whisking median (0.86, problem 1) (cell 46). |
| table1-l4-outside | not_reproduced | 7 to 9 of 17 values under the criterion readings; 52 of 64 combinations fall below 9. Latency is 8.1 against 18.5, and the spikes-per-touch medians are never 0 (cell 47). |
| table1-l5 | partially_reproduced | 11 to 13 of 18 (cell 48). |
| latency-determinable | not_reproduced | L4 outside cells with a latency: 7 (first touches) or 10 (all touches), against 4 (cell 50). |
| l4-outside-weaker-touch | reproduced | 32 of 32 readings give p < 0.05 with C2 higher; peak rate p = 1.6e-5 and 1.1e-5 (cell 52). |
| l5-higher-rates | reproduced | All four comparisons p < 0.01 with the L5 median higher (cell 54). |
| phase-mod-l4-inside-outside | reproduced | p = 0.94, but the depths sit at a ceiling of 1.0 (problem 3) (cell 56). |
| phase-mod-l4-vs-l5 | reproduced (fragile) | p = 2.6e-4 and 0.0039. Restricted to cells with at least 20 phase-analysis spikes, p = 0.051 and 0.050 (cell 57; problem 3). |
| whisking-rate-l4-no-change | partially_reproduced (provisional) | L4 outside p = 0.43. L4 C2 p = 5e-5 / 3e-9, with 26 of 31 cells higher. Likely caused by problem 1 (cell 59). |
| whisking-rate-l5-increase | reproduced | p = 0.024 / 0.014, median difference positive (cell 60). |
| fig3c-touch-spikes-l4c2 | blocked: methods_underspecified | 5 of 8 criterion readings pass. The r200 readings put the time fraction at 16.0 to 17.6% against a ceiling of 16.39 (cell 63). |
| fig3c-touch-spikes-outside | not_reproduced | Time fraction is 17.5 to 26.3% against 3.5 ± 0.35 under every criterion reading (cell 64). |
| fig3c-touch-spikes-l5 | blocked: methods_underspecified | 8 of 16 criterion readings pass (cell 65). |
| fig3d-touch-phase-l4c2 | blocked: methods_underspecified | 4 of 16 criterion readings pass, only "total" width with r100 (cell 68). |
| fig3d-touch-phase-outside | not_reproduced | Time fraction is 27 to 42% against 16.9 ± 1.69 under every criterion reading (cell 69). |
| fig3d-touch-phase-l5 | blocked: methods_underspecified | 8 of 32 criterion readings pass (cell 70). |
| fig3d-phase-only | blocked: methods_underspecified | 11 of 16 criterion readings pass; the readings disagree, under the same rule as the parent claims (cell 71). |
| fig4a-touch-detection-c2 | blocked: methods_underspecified | Percent-correct readings give N95 = 13, 17, 25 and 30; none lies in 15 ± 1.5. The "detected" readings (1 to 11) are invalid (problem 2) (cell 74). |
| fig4a-touch-detection-outside | partially_reproduced (provisional) | The criterion holds under all four percent-correct readings: 0.53 to 0.55, upper bound below 0.60, near the 50% chance level. It fails under the "detected" readings, which problem 2 invalidates (cell 75). |
| fig4b-touch-time-precision | not_reproduced | Minimum RMS error is 1.09 to 1.48 ms, the 95% half-width 2.0 and 1.96×RMS at least 2.14, against 0.55 ± 0.055, in every combination (cell 78). |
| fig4c-phase-decoding | blocked: methods_underspecified | C2 ranges from 12 to 84 deg depending on smoothing. C2 is never better than outside under any criterion reading. The single-cycle reading never reaches 76% and stays at about 50% even at 180 deg (cell 81). |
| fig5c-modulation-index | reproduced | All means lie in 0.66 to 0.74 under every criterion reading (cell 84). |
| fig5-modulation-correlations | partially_reproduced | Reading (a): 16 of 64 sub-readings match. Reading (b): 0 match. r_vc ranges from 0.62 to 0.79 and is often not the largest (cell 86). |
| fig6s1b-clusters-less-variable | reproduced | 0.90 of cells under all 4 readings (cell 89). |
| fig6cd-ff-near-binomial | reproduced | 16 of 16 combinations (cell 94). |
| fig6d-not-refractory | blocked: methods_underspecified | For the compensated model, comparison (a) fails in 6 of 6 combinations and (b) holds in 4 of 6 (cell 97). |
| fig6e-sample-epoch-ff | reproduced | 6.58 ± 5.40 (cell 99). |
| fig6e-random-38ms-ff | reproduced | 1.56 and 1.59 (cell 100). |
| fig6e-touch-38ms-ff | reproduced | 1.34 to 1.39 (cell 101). |
| fig6e-touch-10ms-ff | reproduced | 0.70 to 0.86 (cell 102). |
| fig6e-similar-touch-ff | reproduced | 16 of 16 combinations: 0.50 to 0.69, conditions in order (cell 103). |
| whisk-cycle-spikes | reproduced | 0.092 to 0.124 spikes per cycle under all readings (cell 105). |

**Blocked claims:** none is blocked for lack of data. The archive API shows all 52 assets and 23 subjects, so every blocked outcome above comes from readings that disagree, not from missing data.

**B. Problems**

1. **[affects a conclusion]** `hires.whisk_mask` (used in cells 13, 41, 54 and 59) treats every sample with amplitude above 2.5 deg as whisking. It does not apply the Methods' exclusion of time during licking or within 70 ms after touch. The claims file's definitions include that exclusion, and text-whisking-rates says "as in the Methods".
   - Touch-evoked spikes after the touch ends (touch median 21 ms, window 8 to 36 ms) therefore count as whisking spikes.
   - The likely effects are the 0.86 L4 C2 whisking median (paper 0.33), cell 23's 1.26 (paper 0.67), and the significant L4 C2 whisking increase (p = 5e-5).
   - Affected claims: text-whisking-rates, the whisking values of table1-l4-c2, table1-l4-outside and table1-l5, whisking-rate-l4-no-change and whisking-rate-l5-increase.
2. **[affects a conclusion]** `hires.touch_detection`, measure (2a): when no threshold beats chance, the arg-max of percent correct falls on the lowest candidate, which classifies everything as touch (hit rate 1). Cell 74 then takes the maximum of hit rate over time points.
   - Synthetic test: a neuron whose touch and non-touch responses are identical gives "detected" = 1.000 with percent correct 0.515.
   - This explains N95 = 1 for pre_start and pre_all, and the upper bounds of 1.0 for the outside group. Every "detected" reading of fig4a-touch-detection-c2 and fig4a-touch-detection-outside is invalid.
3. **[affects a conclusion]** Phase tuning (cell 13, `cycle_table` with `in_sample`) keeps only cycles lying wholly inside the pole-in-reach time. The Table 1, phase-mod and fig4c criteria do not ask for this; it is the author's own choice.
   - L4 C2 cells keep a median of 4 spikes; 6 cells have none, and 14 of the remaining 25 sit at a depth of exactly 1.0.
   - `cos_fit` with B ≥ 0 is biased upward on sparse counts. Synthetic test: a true depth of 0.4 from about 6 spikes gives a median fitted depth of 0.87, with 36% of fits at exactly 1.
   - Affected claims: the depth medians in Table 1, phase-mod-l4-inside-outside, phase-mod-l4-vs-l5 (p ≈ 0.05 once cells with fewer than 20 spikes are dropped), example-cell-phase-modulation and fig4c, whose cycles are cut to a third (5,377 against 17,669, cell 105).
4. **[does not affect a conclusion]** Cell 45: the line `EXPECT["L4out"] = EXPECT["L4out"][:2] + EXPECT["L4out"][2:]` does nothing. The zero-median check is computed but not added to `n_ok`, so `n_ok` counts out of 15 against thresholds set out of 17. It does not change the outcome, because the medians are never 0.
5. **[does not affect a conclusion]** Cell 9, choice of clock: under the spike clock, files with the 10 ms offset still peak 4 ms later than the others (12 against 8 ms, p = 0.016), so the alignment is not fully settled. Cell 23's latency of 8 ms supports the clock the notebook chose.
6. **[does not affect a conclusion]** Cell 74: only 20 repetitions per population size, and the mean is not monotonic in N. N95 values of 13 and 17 lie next to the tolerance band.
7. **[does not affect a conclusion]** Cell 31: the pooled reaction time includes 544 negative values (lick before first touch). The claim fails on the touch counts regardless.
8. **[does not affect a conclusion]** Cell 89: only 8 of 31 cells yield five touch groups, because N ≥ 20 and the median number of selected touches is 84 to 96. The fig6cd and fig6e-similar claims therefore use 1 to 4 groups for most cells.
9. **Claims file, reported and not corrected:**
   - The "cross" cutoff rule says nothing about cells with no real rise. For L4 outside and L5 cells, noise crossings place long windows: 17 to 26% of exploration time, where the paper gives 3.5%; the literal-start variant gives 1.3 to 2.6%.
   - example-cell-ff-around-touch reading (b) accepts any of about 600 cell × group tries, which invites a match by chance.
   - The latency rule (mean + 2 s.d. over sparse 1 ms bins) returns noise latencies of 0 to 3 ms (cells 3, 9, 13, 36 to 38, 40, 46, 50), which bears on latency-determinable.

**C. What I could not check, and the output that would have let me**

- **Whisking rates (problem 1):** the per-cell whisking rates, and the signed-rank tests, with the 70 ms post-touch and licking exclusions applied.
- **Phase depths (problem 3):** per-cell depth and spike count with phase cycles not restricted to pole-in-reach time, and the same with the ≥ 20-spike rule applied to the claims' tests.
- **fig4a "detected" (problem 2):** the hit rate taken at the time point that maximizes percent correct, with a tie rule that does not default to "all touch". Also the percent correct at N = 1, and more than 20 repetitions.
- **example-cell-ff-around-touch:** the row in which cell 11 matches (its readings, group, counts and FFs), and how many cell × group units were tested.
- **Clock alignment:** each file's touch-peak latency plotted against its spike-clock offset, or a check of spike samples against the voltage peaks, to settle the residual 4 ms.
- **fig3c time fractions:** per-cell t_on and time fraction for the L4 outside and L5 cells, to see whether noise crossings drive their 17 to 26%.
