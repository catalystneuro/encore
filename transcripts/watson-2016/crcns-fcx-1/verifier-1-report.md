**A. Outcomes** (41 claims in the claims file. The notebook marks all 41 as tested and none as blocked.)

| Claim | Outcome | Reason |
|---|---|---|
| table1-dataset-counts | partially_reproduced | Cell 9: pE 995, pI 126, 27 sessions, 11 rats and mean 36.85 all match. WAKE-SLEEP cycles are 51 against 54, and the tolerance is 0. The criterion has no partial rule. |
| ma-statistics | partially_reproduced | Cell 11: from the files' MA intervals, n 434 (790), median 11.0 s (15.9), 0.184/min (0.32) and 3.7% (9.1) are all outside tolerance. The episode trend holds (20 bins R −0.956, p 4.5e-11), and the SLEEP trend shows no change on bin means (p 0.10–0.15). |
| packet-duration | reproduced | Cell 14: median 111.0 s. The range ratio is only 52.5 (14–735 s), which is short of two orders of magnitude, but the criterion only asks for it to be reported. |
| fig2a-pe-rate-distribution | not_reproduced | Cell 16: 5 of 6 medians are within tolerance (pI REM 5.72 vs 4.25 is not). The shape test fails because the nonREM pE range stops short of 4.5 Hz under both percentile readings (1–99th: 4.05 and 4.17 Hz). See B11 on the criterion. |
| fig2b-wake-nrem-slope | reproduced | Cell 19: log slope 0.684 [0.661, 0.708] with R 0.803 (a), and 0.687 with R 0.824 (b). |
| fig2a-fraction-above-2hz | reproduced | Cell 21, reading (a): 18.8 / 20.6 / 9.3%, chi-square p 4e-16 and 4e-21. Under reading (b) the nonREM-vs-WAKE p is 3.2e-9, which would make it partial (B6). |
| burst-index-by-state | partially_reproduced | Cell 23: Kruskal-Wallis and REM>WAKE hold under every reading. The medians miss under (a) and (b). The best reading, (c), matches nonREM only (4.51 / 11.47 / 6.39%). |
| fig2c-autocorrelogram | partially_reproduced | Cell 25: nonREM peak at 8.5 ms, local maxima near 125 ms in WAKE and REM, nonREM most negative, KW p < 1e-95. No reading puts the medians within tolerance; this is the criterion's partial case. |
| synchrony-skew | reproduced | Cell 28 (a): 62.9% of cells at or below 4% of windows, 0% at or above 50%. This passes only because the criterion treats 15% as a lower bound (B11). |
| updown-durations | reproduced | Cell 30: deposited n 43230 / 86839, medians 0.473 / 0.188 s, both right-skewed. |
| fig1e-up-state-dynamics | not_reproduced | Cell 32: only pI rate and synchrony decrease. The pE rate rises in the last bin and E/(E+I) rises (R +0.47). The sigma peak (bin 0) comes before the gamma peak (bin 3). |
| fig2de-fast-before-slow | reproduced | Cell 34: latency in the two halves R 0.733. Latency vs log rate is negative (R −0.127 to −0.29). |
| fig2f-rate-group-correlations | not_reproduced | Cell 36: the 1–6 group mean is positive (+0.0063 WAKE sextiles, +0.0095 nonREM sextiles), not negative. |
| fig3ab-population-rate-declines | reproduced | Cell 38: R −0.15 to −0.80 with p ≤ 1.5e-9 under every reading. |
| first-last-packet-mean-rate | reproduced | Cell 40 (b): 1.048 vs 0.883 Hz, signed-rank p 1.9e-20. |
| post-sleep-wake-lower | partially_reproduced | Cell 42: lower after, signed-rank p 0.018 (a) and 0.048 (b), against a bound of 1e-6. The immediate-WAKE variant gives p 2.6e-4. |
| fig3d-first-last-packet-slope | reproduced | Cell 44 (b): 0.872 [0.840, 0.904], inside 0.8535 ± 0.0265. |
| fig3b-sextile-changes | reproduced | Cell 46: top sextile R < 0 with p ≤ 3e-8 and bottom sextile R > 0 under every reading. |
| cv-decreases-over-sleep | not_reproduced | Cell 49, criterion reading (b): R −0.003, p 0.73 (clock ii: p 0.2). |
| fig3c-spindles-over-sleep | partially_reproduced | Cell 51: the incidence decrease reaches only reading (b), R −0.021, p 0.03. The incidence of 2.85/min matches Table S1 (2.94) but not the Results (1.94), and the duration of 0.616 s is outside tolerance. Frequency and amplitude match. |
| fig3c-updown-over-sleep | not_reproduced | Cell 53: at most 2 of 5 parts hold (DOWN duration, UP-duration absence). |
| fig3f-within-up-changes | partially_reproduced | Cell 55: the S3C trend holds under (b) (p 9e-16). Fastest sextile −0.65 Hz (p 8e-8) and pI −0.57 Hz (p 0.045) are right. The slowest sextile change is n.s. (p 0.36). |
| figs3a-first-last-rem-ma-slopes | partially_reproduced | Cell 57: REM and MA slopes are within tolerance under (b), WAKE is 0.687 (outside). All intervals lie below 1. |
| fig3e-wake-before-after-sextiles | not_reproduced | Cell 59: only sextiles 6 and 5 hold under (a); 4 and 1 do not (2 of 4). |
| fig4-lfp-within-nrem | partially_reproduced | Cell 61: delta and sigma increases and the packet-length correlation (R 0.387) hold. No single reading has gamma falling over episodes and flat over packets: (b) packets p 6e-8, (c) episodes p 0.28. |
| fig4-updown-within-packets | reproduced | Cell 63, reading (b): all 5 parts hold under either ratio definition. |
| fig4-spindles-within-nrem | reproduced | Cell 65 (b): all four increases are below their bounds and all four durations are within tolerance. The packet frequency does change (p 0.0096), against the absence claim, but the criterion's final rule leaves this part out. |
| fig4e-late-packet-sigma | reproduced | Cell 67 (a): late > early, rank-sum p 3.7e-34. |
| fig4-sextiles-within-nrem | reproduced | Cell 69 (b): all sextile, CV and burst parts hold under clock (ii). Under clock (i) the episode burst p is 2.6e-10, just above the 1e-10 bound. |
| fig4cd-packet-rate-lfp-correlations | not_reproduced | Cell 71: 3 of 6 meet their bounds; the criterion needs 4. All six have the right sign at p < 0.05. |
| fig4e-within-up-sextiles | not_reproduced | Cell 73: at most 1 of 3 groups holds. The slowest sextile increases. |
| figs5-within-wake-rem | not_reproduced | Cell 75: both the WAKE and the REM parts fail (for example, WAKE sextile 6 p 0.77; REM sextiles 1, 4 and 5 n.s.). |
| fig5b-ma-nrem-ma | not_reproduced | Cell 79: no sextile changes at p < 0.05, and S5C R is +0.016 (p 0.64). |
| figs5d-rem-nrem-rem | not_reproduced | Cell 81: R 0.025, p 0.85, from 25 triplets in 3 sessions. The interruption-tolerant variant gives R −0.105, p 0.0076 (B3). |
| fig5c-sigma-ma-change | not_reproduced | Cell 83: R 0.008, p 0.92. |
| fig5b-wake-between-packets | not_reproduced | Cell 85: 8 or 52 triplets (paper 24). The fastest sextile does not increase. Motion vs change: R 0.48, p 0.28 with raw motion (the z-scored variant gives R 0.90, p 0.005, n 7; B4). |
| fig5b-ma-between-packets | partially_reproduced | Cell 87: the lowest sextile per cell-triplet gives p 0.0083 (direction not printed; C). The top sextile falls significantly, where the claim says no change. S5G R −0.169, p 1.3e-7, against a bound of 1e-10. |
| fig5b-rem-between-packets | not_reproduced | Cell 89: sextiles 4–6 increase. REM duration R −0.019, p 0.85. |
| fig5c-delta-change-slow-cells | not_reproduced | Cell 91: slowest sextile R 0.008, p 0.86. |
| figs2d-interneurons-unchanged | not_reproduced | Cell 93: slope 0.836 / 0.888, and neither interval includes 1. |
| sleep-homogenizes-rates | partially_reproduced | Cell 95: only fig3d is reproduced; fig3e and cv are not. |

Totals: 14 reproduced, 11 partially reproduced, 16 not reproduced, 0 blocked. The paper states no chance level for any selection.

**B. Problems**

1. [affects a conclusion] The MA set may not be the paper's (cells 11–12, 57, 77–89, `fcx.triplets`).
   - The files hold 434 MAs inside SLEEP and 345 WakeInterruptions shorter than 40 s, which breaks the 40–120 s definition.
   - Counted together they give n 779 and 0.318/min, against the paper's 790 and 0.32. Table S1 defines an MA as any arousal under 40 s between packets.
   - The combined reading was run only for the counts. It was not run for the MA slope (figs3a), the MA triplets (fig5b-ma-nrem-ma, fig5c-sigma-ma-change, fig5b-ma-between-packets) or the episode trend.
   - In `triplets`, short WakeInterruptions break MA triplets, and `wake_min=40` drops them from PWP_b.
2. [affects a conclusion] The post-sleep WAKE window (cells 42, 47, 57, 59) follows the claims file: the next scored WAKE of 7+ min.
   - Only 23 of 51 cycles have one, and in 17 of them it starts 166 s to 2.9 h after SLEEP ends. This is a claims-file reading at odds with the paper's "5-min post-sleep WAKE".
   - The reading "the first 5 min after SLEEP ends", which would cover all 51 cycles, was not run. It could change post-sleep-wake-lower, fig3e and the figs3a WAKE slope.
3. [affects a conclusion] The triplet adjacency rule (gap ≤ 2 s, `fcx.triplets`) is the author's own choice.
   - Under it, REM-packet-REM gives 59 cells; S5D implies about 136.
   - The paper's tolerance for the arousal at the end of REM plausibly applies to the REM→packet step too. The bridge variant under the linear reading would make figs5d partial by M4.
   - Packet-WAKE-packet also gives 8 or 52 triplets against 24.
4. [affects a conclusion] Movement pooling in fig5b-wake-between-packets (cell 85).
   - Raw motion is pooled across sessions whose means run from 0.55 to 4076, and BWRat19_032513 is all NaN. Pooled that way, the correlation is not meaningful.
   - The z-scored variant matches the data description's own definition and would make the claim partially reproduced, but it rests on only n = 7.
5. [does not affect a conclusion] Unit (ii) in fig4e-within-up-sextiles (cell 73) is one entry per cell and packet (n 4128 for about 165 cells), not one per cell as the criterion says. The outcome is 0 of 3 either way.
6. [affects a conclusion] fig2a-fraction-above-2hz reaches p < 1e-10 only under M1 reading (a), which counts each cell once per cycle (1787 rows for 995 cells). That reading is pseudo-replicated, although the claims file allows it.
7. [does not affect a conclusion] Sextile assignment (`fcx.sextiles`, cell 36).
   - Sextiles use each cell's mean of per-cycle WAKE rates. M2's primary reading is the rate pooled over all of the session's WAKE.
   - M2 reading (b), sextiles from each cycle's WAKE, was not run.
8. [does not affect a conclusion] fig1e (cell 32) uses zero-phase band-passed power, not a spectrogram. At 9–25 Hz this smears about ±50–100 ms, so the sigma peak in bin 0 may come from the DOWN→UP edge. The claim fails on E/(E+I) and the pE rate anyway.
9. [does not affect a conclusion] The 10 s spectrogram windows (`lfp_reduce`, `seconds_table`) spill ±5 s across packet edges.
   - This touches the within-packet gamma trend, the "last 20 s" sigma (cells 71, 83) and the delta change (cell 91).
   - The window follows the claims file, but the size of the effect was never checked.
10. [does not affect a conclusion] The 125 ms local-maximum test in fig2c (cell 25) also fires in nonREM, so it cannot tell theta apart from noise.
11. Claims-file readings, reported and not corrected:
    - fig2a: the criterion requires the 0.05–5 Hz range "in each state", although the paper itself says the nonREM tail is shorter.
    - synchrony-skew: "more than 15%" is made a one-sided bound that a measure four times larger passes.
    - fig2de: first-spike latency is negatively correlated with rate almost by construction.
    - table1: the criterion has no partial rule.
12. [does not affect a conclusion] Two pairs of sessions are simultaneous ACC/mPFC recordings (Dino_061914, Dino_062014) and share states and motion. They enter the state- and LFP-level trends twice.

**C. Not checked, and the output that would settle it**

- Whether the 3 missing cycles (51 vs 54) are absent from the deposit or were dropped by parsing. Needed: every session's raw `WakeSleep`, `Wake` and `Sleep` intervals, and any SLEEP not paired into a cycle.
- Whether the WakeInterruptions under 40 s sit between two packets, which would make them MAs by Table S1. Needed: a count by neighbouring states.
- The pI REM median is 5.724 Hz under both readings (n 188 and 113), which is an unlikely coincidence. Needed: the median cells and a check for duplicated cycles.
- The direction of the per-cell-triplet change for the lowest sextile in packet-MA-packet (cell 87). Only the reading-(b) mean is printed, and the partial outcome depends on this.
- Whether any cycle falls after the ketamine or saline injections noted in the dataset's WatsonSleepHomestasis2016Table.xlsx (BWRat20_101513, BWRat21_121613, BWRat21_121813). Needed: the cycle times printed against `RecordingFileIntervals`.
- The spindle duration averaged over all spindles (Table S1's likely basis). Only the mean of session means is printed.
