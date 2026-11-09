**A. Outcomes**

The claims file has 39 claims. The notebook tests 32 and treats 7 as blocked. My outcomes: 8 reproduced, 9 partially reproduced, 15 not reproduced, 7 blocked. The paper states no chance level for any selection, and the notebook uses none.

| Claim | Outcome | Reason |
|---|---|---|
| dataset-composition | not_reproduced | Cell 9: 10 rats and mean 286.8 min are in tolerance; 22 sessions, 826 pE and 96 pI are not (2 of 5). The archive holds 22 of the 27 sessions its own description lists, so the misses come from missing data, not from the counting. |
| fig2a-median-rates | partially_reproduced | Cell 11, reading (a): pE medians 0.755, 0.662 and 0.825 Hz are in tolerance. pI medians 3.92, 2.73 and 3.06 Hz miss by 30 to 40% (3 of 6). |
| fig2a-skewed-wide-distribution | partially_reproduced | Cell 13: skewness 4.57 > 1 and the 97.5th percentile (7.17 Hz) is in range. The 2.5th percentile is 0.0124 Hz, outside 0.025 to 0.1. |
| fig2a-fraction-above-2hz | not_reproduced | Cell 15: WAKE 17.0% is outside 19.2 ± 1.92. Chi-square p is 3.5e-6 and 3.4e-8, not < 1e-10, so the "partially" condition (tests hold) also fails. |
| fig2b-wake-nrem-slope | reproduced | Cell 17, reading (a): R = 0.862, slope 0.757 (CI 0.727 to 0.788), inside 0.594 to 0.781 and excluding 1. See B3. |
| fig2-burst-index-by-state | partially_reproduced | Cell 19, reading (b): NREM 11.67% matches, but WAKE 4.95% and REM 6.71% miss. Order NREM > REM > WAKE holds and Kruskal-Wallis p = 7e-38. |
| fig2c-acg-peaks | partially_reproduced | Cell 21: NREM peak at 7.5 ms passes. The theta maximum sits at the 60.5 ms window edge in REM and WAKE, so that part fails. |
| fig2c-acg-decay | blocked (methods_underspecified) | The fit form is not in the main text; see C. |
| fig2f-rate-group-correlations | partially_reproduced | Cell 23: (6,6) is the largest pair mean (0.042). (1,6) is positive (0.0089, t = 10.9, p = 9e-26), against the stated negative correlation. |
| ma-statistics | not_reproduced | Cell 25: median duration 19.0 s is in tolerance. Frequency (0.096 or 0.127 per min) and fraction (3.2 or 4.2%) are far below 0.32 and 9.1% (1 of 3). |
| ma-fraction-over-nrem-episodes | partially_reproduced | Cell 27: reading (a) gives R = -0.45, p = 0.19. Reading (b) gives R = -0.087, p = 1.7e-5, which is negative with p < 0.05. The bin profile is an inverted U. |
| packet-duration | reproduced | Cell 29, reading (a): median 108 s, inside 99.9 to 122.1. |
| wake-sleep-cycles | not_reproduced | Cell 31: 1.43 cycles per session and 3 sessions with none. The variant gives 1.62 and 1 session with none. |
| fig3b-population-decline | partially_reproduced | Cell 33: R = -0.267 (a) and -0.285 (b), both p < 1e-5, but well outside -0.11 ± 0.011. |
| fig3-first-last-packet | reproduced | Cell 35: 1.092 and 0.968 Hz, Wilcoxon p = 3.9e-6, last lower. The last mean clears the bound (0.968) by 0.0001. |
| fig3d-first-last-slope | reproduced | Cell 37, reading (a): slope 0.801 (CI 0.768 to 0.834). The within-packet control gives the same slope; see B3. |
| fig3e-wake-before-after | partially_reproduced | Cell 39, reading (a): population p = 4e-9. Sextiles 4, 5 and 6 decrease (p = 0.03, 6e-4, 2e-5). Sextile 1 does not increase (p = 0.3, mean change -0.002). |
| fig3b-sextiles-over-sleep | reproduced | Cell 41, reading (a): sextile 6 R = -0.447 (p = 3e-11), sextile 1 R = +0.163. |
| fig3b-cv-over-sleep | not_reproduced | Cell 43: R = -0.026 (p = 0.66) and -0.014 (p = 0.81). |
| fig4iv-sextiles-within-nrem | reproduced | Cell 47: episodes s1 +0.060 and s6 -0.083; packets s1 +0.061 and s6 -0.055; all p < 1e-5. Effects are small and per-subject signs disagree; see B5. |
| fig4v-cv-within-nrem | not_reproduced | Cell 49: R = -0.005 (episodes) and +0.011 (packets), both not significant, in every variant. |
| fig4vi-burst-within-nrem | not_reproduced | Cell 51: R = +0.029 and +0.024, p ≈ 0.02, far from p < 1e-10. |
| fig4i-band-power-within-nrem | not_reproduced | Cell 53: delta over packets R = -0.005 (p = 0.61), and gamma rises over episodes (R = +0.062). The delta and sigma part fails, so "partially" does not apply. |
| fig4-delta-packet-length | reproduced | Cell 55: R = 0.334, p = 3e-25. |
| fig4cd-packet-rate-lfp | partially_reproduced | Cell 57: R = -0.416, +0.570 and +0.104. All three have the stated sign with p < 0.05; none is in tolerance. |
| fig5b-nrem-between-ma | not_reproduced | Cell 61: sextile 5 p = 0.24, sextile 6 p = 0.077. The per-cell variant gives sextile 6 p = 0.029, still not < 0.01. |
| fig5b-wake-between-packets | not_reproduced | Cell 63: sextile 6 change is -0.051 Hz (p = 0.09), the wrong sign. The notebook finds 265 triplets against the paper's 24; see B2. |
| fig5b-ma-between-packets | not_reproduced | Cell 65: sextile 1 +0.003 Hz (p = 0.08, not significant). Sextile 6 decreases (p = 7e-5). |
| fig5b-rem-between-packets | not_reproduced | Cell 67: only sextiles 4 and 5 decrease significantly (2 of 6), from 17 triplets. |
| fig5c-rem-duration | not_reproduced | Cell 69: R = -0.047 (p = 0.86, n = 17) and -0.061 (p = 0.21). |
| fig5c-sigma-ma | not_reproduced | Cell 71: R = 0.033, p = 0.71. |
| fig5c-delta-change | reproduced | Cell 73: R = 0.183, p = 5e-6. 4 of 8 subjects have a negative R. |
| figs5-within-wake-rem | not_reproduced | Cell 75: in WAKE, sextiles 5 and 6 decrease (R ≈ -0.12) instead of increasing. No REM sextile is significant. |
| fig5c-wake-movement | blocked (data_missing) | Confirmed in the archive: `acquisition/` is empty and `processing/behavior` holds only the state table. There is no EMG, accelerometer or position data. |
| updown-durations | blocked (methods_underspecified) | No UP/DOWN event tables in the files; partly testable, see C. |
| fig3c-slow-oscillation-spindles-over-sleep | blocked (methods_underspecified) | No UP/DOWN or spindle event tables; detectors are described only in the supplement. |
| fig4ii-iii-updown-spindles-within-packets | blocked (methods_underspecified) | Same as above. |
| fig2de-up-state-sequences | blocked (methods_underspecified) | Needs UP onsets; partly testable, see C. |
| fig3f-4e-within-up-rates | blocked (methods_underspecified) | Needs UP states; partly testable, see C. |

**B. Problems**

1. [affects a conclusion] Microarousals are not labelled in the archive. `classify_states` derives 391 MAs in 21 sessions; the paper reports 790 in 27. Derived frequency is about 0.1 per min against 0.32, and min duration is 7 s. Another 345 Awake epochs under 40 s are left as WAKE (cell 25). Every MA-based claim (ma-statistics, ma-fraction, fig5b-nrem-between-ma, fig5b-ma-between-packets, fig5c-sigma-ma) and the episode definition rest on a reconstruction that does not reach the paper's MA density. Those not_reproduced outcomes may reflect the labels and not the biology.
2. [affects a conclusion] `triplets` (cell 59/63) finds 265 NREM-WAKE-NREM triplets against the paper's 24 "uninterrupted" triplets. The selection plainly differs from the paper's, so fig5b-wake-between-packets tests a different set. REM-between-packets has only 17 triplets (49 of 534 REM epochs are followed directly by NREM), so it has little power.
3. [affects a conclusion] Regression to the mean (cells 17 and 37). For fig3d, the control of second half against first half of the same packet gives slope 0.855 (CI 0.829 to 0.881). That is almost exactly the paper's 0.827 to 0.880, so a slope below 1 is expected from sampling noise alone. The numeric criterion passes, but the claim's reading ("fast cells slow down, slow cells speed up") is not supported. For fig2b, the reverse regression slope is 0.982 (CI includes 1). The notebook has no noise-matched control there.
4. [affects a conclusion] Clock checks (cells 4 and 6). For BWRat21_121813, the state labels could not be confirmed against the spikes (contrast is negative at every shift). For 7 of 21 sessions the LFP could not be confirmed against the spikes. Only Dino_061914's LFP is dropped, and no analysis is re-run without these sessions. The LFP claims (fig4i, fig4cd, fig4-delta, fig5c-sigma, fig5c-delta) and all state-based claims include them unexamined.
5. [affects a conclusion] Pooled points are treated as independent: 10 bins × hundreds of intervals (fig4iv, fig4v, fig4vi, fig4i), cell × cycle pairs (fig3-first-last, fig3e), cell × triplet pairs (fig5b). p-values are inflated. The reproduced fig4iv rests on R ≈ 0.06, and per-subject sextile-6 signs disagree (Rizzo +0.121, BWRat20 +0.05). This follows the criterion, but the reproduced outcomes are fragile.
6. [affects a conclusion] `sleep_periods`/`cycles` (cell 31): 3 sessions have no WAKE-SLEEP cycle, yet the dandiset description says only sessions with one were included. The SLEEP and cycle definition probably differs from the authors'. All fig3 claims use 30 cycles against the paper's 54.
7. [affects a conclusion] Cell 39: the post-sleep window is shorter than 300 s in 23 of 30 cycles, while the pre window is always 300 s. The comparison is therefore weighted toward the first minutes after waking. This may drive both the population decrease and the sextile results.
8. [does not affect a conclusion] fig3-first-last: the last-packet mean clears its bound by 0.0001 Hz. SDs are 1.48 and 1.24 against the paper's 1.20 and 0.91.
9. [does not affect a conclusion] `fig2c` criterion: a smoothed, monotonically decaying ACG always peaks at the 60 ms edge, so the theta test can hardly pass. The cell 21 variant puts WAKE at 118.5 ms (in range) and REM at 149.5 ms (out).
10. [does not affect a conclusion] `read_packet_lfp` assumes the LFP starts at t = 0 at 1250 Hz and never reads `starting_time`. I checked all 22 files: it is 0.0 at 1250 Hz in each.
11. [does not affect a conclusion] `autocorrelogram`: on a synthetic 10 ms periodic train, counts split between adjacent 1 ms bins because of float rounding at bin edges. This is negligible at real-data resolution.
12. [does not affect a conclusion] Cell 19 runs Kruskal-Wallis on paired per-cell values. The paired Wilcoxon gives the same verdict.
13. [does not affect a conclusion] Cell 23 accumulates `n_pairs_all` through `globals()`, and cell 53 temporarily rebinds `sessions`. Both are correct on a single top-to-bottom run (20933 pairs matches the sum of n(n-1)/2 over sessions) but wrong if re-run.
14. [does not affect a conclusion] I tested the other helpers on synthetic inputs and they behave as specified: `classify_states`, `nrem_episodes`, `sleep_periods`, `burst_index` (both readings), `binned_intervals`, `isis_in` and `band_power`.

**C. What I could not check, and outputs that would have let me**

- The paper's supplement (UP/DOWN and spindle detection, decay fit, unit classification, triplet selection) is behind a browser check at PMC, and Europe PMC reports the article as not open access. I read the main text from NCBI efetch, saved under `paper/`.
- Blocked claims, checked in the archive:
  - **Movement (fig5c-wake-movement):** confirmed absent. A high-frequency LFP "EMG" proxy could be computed, but it would be a different measure.
  - **UP/DOWN and spindle claims:** the files have no event tables. The UP, Spindle and Theta DecompositionSeries hold only theta (4 to 10 Hz) and gamma (30 to 80 Hz) phase. All-unit spikes, LFP and a flagged `up_reference` channel are present, so a stated detector could test parts. One example is DOWN states as silence in pooled spikes during NREM, after Vyazovskiy 2009, which the paper cites. The fig2de latency-to-rate correlation and the ordering parts of fig3f/4e would hold up across detector choices; the median durations and R values would not.
  - **fig2c-acg-decay:** an assumed power-law fit could test the ordering (NREM decays fastest), but not the exponent values.
- Outputs that would have settled open points:
  - Awake-epoch durations by neighbouring state, and MA counts under looser rules (for example, one-sided NREM adjacency).
  - Triplet counts against a minimum WAKE duration, to match the paper's n = 24.
  - All claims re-run without BWRat21_121813 and without the 7 sessions whose LFP alignment could not be confirmed.
  - Per-session or mixed-effects versions of the pooled tests (fig4iv, fig3e, fig5b).
  - A split-half WAKE-on-WAKE control slope for fig2b.
  - fig3e with post windows matched in length to the pre windows.
  - SLEEP periods and their dropped segments for the 3 sessions with no cycle.
