**Verifier report, round 1: Watson et al. 2016 on DANDI:000041 and CRCNS:fcx-1**

How I judged: the claims file has 53 claims and the notebook tests all 53 on both datasets. I gave each claim one outcome, judged mainly on CRCNS:fcx-1. It holds all 27 sessions, 995 pE and 126 pI cells, and the lab's own intervals; the Table S1 durations and the UP/DOWN and spindle values match exactly (cells 10, 14, 38, 58). DANDI holds 22 of the 27 sessions, cell-type labels that differ in 7 sessions, and states rebuilt by `derive_states`. I mention DANDI where it differs. The paper states no chance level for any selection; there is no decoding and no train/test split.

Totals: 27 reproduced, 10 partially reproduced, 16 not reproduced, 0 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-dataset-counts | reproduced | CRCNS: 11 rats, 27 sessions, 1121 stable units of 1360 clustered, 995 pE, 126 pI, 36.85 pE per session; per-rat Table S1 matches. DANDI is a subset (10 rats, 850 pE). |
| wake-sleep-cycles | reproduced | CRCNS deposited cycles: 51 (tolerance 48.6–59.4), 1.89 per session, no session without one. DANDI has 47 and Dino-072114 has none. |
| tables1-state-durations | reproduced | CRCNS medians 1192, 2421, 297, 98 and 647 s, all exact. DANDI fits 4 of 5 (REM 64 s misses). WAKE-SLEEP median is 4214 s against the 5918 s the paper prints. |
| ma-statistics | not_reproduced | CRCNS: 434 MAs inside SLEEP (paper 790), median 11.0 s (15.9), 0.184/min (0.32), 3.7% (9.1). All four miss, on both datasets. |
| ma-fraction-over-nrem-episodes | partially_reproduced | Episode decrease holds (reading c R=-0.816, p=5.3e-13), but the SLEEP correlation is significant (c: R=-0.331, p=0.019), so the stated absence fails. |
| packet-duration | reproduced | CRCNS median 111 s; longest/shortest ratio is only 52, and the shortest packet is 14 s, below Table S1's 20 s minimum. DANDI 144 s misses. |
| fig2a-median-rates | partially_reproduced | 5 of 6 medians within tolerance (reading b); pI REM is 5.80 Hz against 4.25 under every reading. |
| fig2a-skewed-wide-distribution | partially_reproduced | Skewness is positive (2.57) and log skewness negative, but no percentile reading covers 0.05–5 Hz within 10% (e.g. 5–95% is 0.070–3.26 Hz). |
| fig2a-fraction-above-2hz | reproduced | CRCNS reading b: WAKE 19.2%, REM 19.7%, nonREM 8.7%; chi-square p 2.7e-11 and 5.1e-12. DANDI p is only about 1e-8. |
| fig2b-wake-nrem-slope | reproduced | CRCNS reading b: slope 0.685 [0.655, 0.715], R=0.820. DANDI 0.711 is just outside tolerance. |
| burst-index-by-state | partially_reproduced | Order nonREM > REM > WAKE holds, Kruskal-Wallis p is tiny and REM > WAKE at p<0.05. No reading has all three medians in tolerance (b: 4.3/13.4/6.0; c: 4.5/11.3/6.4). Readings a and b are biased (B1). |
| fig2c-acg-peaks | partially_reproduced | Theta local maxima at 134.5 ms (WAKE) and 113.5 ms (REM) are within tolerance; the nonREM peak bin is 9–10 ms (centre 9.5 ms), outside 8±0.8 ms. |
| fig2c-acg-decay | partially_reproduced | Reading c medians −0.67/−1.52/−0.58 (WAKE/nonREM/REM) have the right order with Kruskal-Wallis p=4e-73, but all three are just outside tolerance. |
| synchrony-skew | reproduced | 62.9% of cells at ≤4% of windows and 0.0% at ≥50%; this meets the criterion's direction-only test, but the values are far from the paper's. |
| updown-durations | reproduced | Deposited medians: DOWN 0.188 s, UP 0.473 s, both right-skewed; counts 43230 and 86839 exact. DANDI detections also within tolerance. |
| fig1e-up-state-dynamics | partially_reproduced | pE rate, pI rate and synchrony decrease, but E/(E+I) rises (R=+0.47, last bin above first); sigma peaks at 0.0 s, before gamma at 0.1 s. |
| fig2de-fast-before-slow | reproduced | Latency in first vs second half R=0.616; latency against log rate R=−0.13 (WAKE rate) and −0.23 (nonREM rate), both significant. |
| fig2f-rate-group-correlations | not_reproduced | Fastest–slowest correlation is positive (0.0064, p=1.7e-12) under both sextile readings and on both datasets. |
| fig3ab-population-rate-declines | reproduced | Reading a R=−0.283, p=2.4e-14; readings b and c agree. |
| first-last-packet-mean-rate | reproduced | 1.03 → 0.90 Hz, signed-rank p≈1e-18; DANDI 0.99 → 0.91 Hz also passes. |
| post-sleep-wake-lower | reproduced | CRCNS WAKE-after reading ii, signed-rank p=3e-11 (by cell and cycle) and 8e-7 one-sided (by cell). DANDI best is 1.2e-5, which would be partial. |
| fig3d-first-last-packet-slope | reproduced | CRCNS reading b slope 0.872 [0.840, 0.904]. The reverse slope is 0.860 (B4). DANDI 0.825 is just outside tolerance. |
| fig3b-sextile-changes | reproduced | Top sextile R=−0.368, p=1e-19; bottom sextile R=+0.10 (reading a), on both datasets. |
| cv-decreases-over-sleep | reproduced | Reading a (per packet) R=−0.116, p=0.0022; reading b fails (p=0.19). |
| fig3c-spindles-over-sleep | not_reproduced | No incidence decrease under any reading (p 0.19–0.56). Incidence is 2.85–2.95/min: it matches Table S1 (2.94), not the Results value of 1.94 used by the claims file. |
| fig3c-updown-over-sleep | not_reproduced | Only DOWN duration increase and UP duration absence hold (2 of 5); UP and DOWN incidence do not fall and "other" time does not rise. |
| fig3f-within-up-changes | reproduced | S3C reading b R=−0.089, p=1.6e-16; mean changes top −0.43, pI −0.67, bottom +0.077 Hz. |
| figs3a-first-last-rem-ma-slopes | reproduced | Reading b with WAKE ii: REM 0.807, MA 0.656, WAKE 0.820, all within tolerance (same on DANDI). |
| fig3e-wake-before-after-sextiles | reproduced | Reading ii: S1 increases (p=0.0025); S4, S5, S6 decrease (p 0.039, 3e-6, 3e-13); same on DANDI. See B3. |
| fig4i-band-power-within-nrem | reproduced | Reading c: delta and sigma rise over episodes and packets, gamma falls over episodes (p=0.011) and not over packets (p=0.29). |
| fig4-delta-packet-length | reproduced | R=0.166, p=1e-5 (DANDI R=0.253). |
| fig4-late-packet-sigma-delta | partially_reproduced | Reading a: sigma rises (+0.148 SD, p=6e-13) and delta falls; but the delta–sigma correlation is higher in the final portion (0.162 against 0.129), not lower. |
| fig4-updown-within-packets | reproduced | Reading b: all five changes hold at their bounds (UP incidence p=1.3e-5; UP/DOWN duration ratio R=−0.157). |
| fig4-spindles-within-nrem | partially_reproduced | All four increases and all four durations hold, but frequency changes (packets b p=0.011; episodes c p=0.011), so the absence fails under either reading. |
| fig4e-late-packet-sigma | reproduced | Last third above first third, rank-sum p≈0 (reading a), on both datasets. |
| fig4iv-sextiles-within-nrem | reproduced | Reading b: top sextile negative and bottom positive, p<1e-4, in both episodes and packets. |
| fig4v-cv-within-nrem | reproduced | Reading b: R=−0.113 (episodes) and −0.139 (packets), p<1e-34. |
| fig4vi-burst-within-nrem | reproduced | R=0.12 and 0.116, p<1e-32; the burst grid bias (B1) is unquantified here. |
| fig4cd-packet-rate-lfp-correlations | not_reproduced | All six have the reported sign at p<1e-3 and the four absences hold, but only 3 of 6 meet their p bound (delta 6e-4, gamma 5.7e-10, late sigma 5.6e-6 miss), below the "at least four hold" needed for partial. |
| fig4e-within-up-sextiles | not_reproduced | The slowest sextile increases under every reading; the top-sextile drop never reaches p<1e-8. |
| figs5-within-wake-rem | not_reproduced | REM: only one sextile significant. WAKE reading b: sextile 2 does not increase (p=0.16). |
| fig5b-ma-nrem-ma | not_reproduced | Top two sextiles p=0.18 and 0.24; S5C R=0.009. |
| figs5d-rem-nrem-rem | not_reproduced | R=−0.183, p=0.11, n=78 cells (DANDI R=+0.047). |
| fig5c-sigma-ma-change | not_reproduced | R=−0.034, p=0.68 (DANDI R=−0.247). |
| fig5b-wake-between-packets | reproduced | Reading a: 24 triplets exactly; S6 increases p=0.017; S1 p=0.33 and S5E p=0.82, both not significant. DANDI also passes (26 triplets). |
| fig5c-wake-movement | not_reproduced | CRCNS R=0.222, p=0.36 (n=19); fraction of time moving R=−0.14. DANDI has no motion signal (see C). |
| fig5b-ma-between-packets | partially_reproduced | Lowest sextile increases (p=0.012), but the top sextile falls (p=3e-9) and S5G p=2.3e-8 misses the 1e-10 bound. |
| fig5b-rem-between-packets | not_reproduced | Only sextile 2 decreases; sextile 5 increases (p=0.02). |
| fig5c-rem-duration | not_reproduced | \|R\| < 0.08 and p > 0.3 under all three readings. |
| fig5c-rem-theta | not_reproduced | Slowest sextile R=−0.149, p=0.06 (reading a) and R=+0.03 (reading b). |
| fig5c-delta-change-slow-cells | not_reproduced | Slowest sextile R=−0.033, p=0.43 (negative on DANDI). |
| figs2d-interneurons-unchanged | not_reproduced | 95% intervals exclude 1: [0.766, 0.906] and [0.802, 0.973]. |
| sleep-homogenizes-rates | reproduced | The three claims it depends on (fig3d, fig3e, cv) are reproduced on CRCNS. |

### B. Problems

1. **[affects a conclusion]** `prepare()` (`same = kk == k[:-1]`) drops every ISI that crosses a 1-s grid boundary, not only those spanning two state intervals as the criterion says. On synthetic Poisson trains with 10% bursts, the true short-ISI fraction of 0.104 becomes 0.602 at 0.2 Hz, 0.105 becomes 0.288 at 0.7 Hz, and 0.115 becomes 0.187 at 2 Hz. This invalidates readings a and b of `burst-index-by-state` (cell 30). Every reading of `fig4vi` (cell 86, `burst_a`, `burst_pooled`) uses this grid, so its trend may partly come from within-packet rate changes.
2. **[affects a conclusion]** `norm_points` reading c (`concat_time_bins` + `secs`) uses whole grid seconds only. Bins under about 2 s keep 0 or 1 second: in a synthetic 64 s episode cut into 50 bins, only 14 bins hold any data. This hits the REM part of `figs5-within-wake-rem` (cell 92, where c is the only reading run; REM episodes have a median of 98 s on CRCNS and 64 s on DANDI) and every packet-level reading c.
3. **[affects a conclusion]** Cell 0 states an outcome rule — partially reproduced when a claim holds on only one dataset — that is not in the claims file. DANDI is a subset with rebuilt states and different labels, so that rule would downgrade at least `wake-sleep-cycles`, `tables1-state-durations`, `packet-duration`, `fig2b`, `fig3d` and `post-sleep-wake-lower` from the outcomes above.
4. **[affects a conclusion]** In cell 16 the deposited CRCNS MAs (2130 in total, 434 inside SLEEP; e.g. BWRat21_121613 has 350 MAs with 6 packets) disagree with the paper on count, duration and fraction of SLEEP. The notebook never checks where the other 1696 lie or whether this variable is the paper's MA. Every MA-based claim inherits this: ma-fraction, the S3A MA slope, fig5b-ma-nrem-ma, fig5c-sigma-ma-change and fig5b-ma-between-packets.
5. **[does not affect a conclusion]** Regression to the mean, which changes what the reproductions show:
   - The sextiles (`sextiles`/`wake_rate`) are ranked on all WAKE of the session, which includes the 5-min pre-sleep window (cell 66, fig3e) and the first tenth of WAKE (cell 92, figs5 reading b). That bias produces exactly the claimed pattern, and no variant ranked on held-out WAKE is shown.
   - In cell 52 the reverse slope roughly equals the forward slope (0.860 against 0.872; 0.807 against 0.788). That is what regression to the mean alone predicts. No reverse slope is shown for figs3a or figs2d.
6. **[does not affect a conclusion]** In cell 40, `SHORT_WIN` (200 ms windows) is an assumption. The lag-0 window straddles the DOWN state, which has low gamma by detection, so the gamma/sigma order cannot be resolved. fig1e is partial either way.
7. **[does not affect a conclusion]** Cell 26 runs the chi-square on paired per-cell rates as if the samples were independent (this is the paper's test). Cell 66 runs only M1 reading a, which repeats cells across cycles. Cell 80 uses 10–25 Hz for sigma instead of 9–25 Hz, and the S4B per-pixel map the criterion asks for is not shown. In cell 104, 5 of the 24 WAKE triplets drop out for lack of motion data, without explanation.
8. **Claims-file readings (reported, not corrected):**
   - fig3c-spindles is judged on 1.94/min, though the deposited data match Table S1's 2.94/min exactly.
   - fig2c-acg-peaks: "7 to 9 ms in whole bins" is ambiguous for the bin [9, 10) ms.
   - fig4cd: "hold" is undefined against M4's three levels; a lenient reading would make that claim partial.
   - synchrony-skew: the direction-only criterion passes 63% against the paper's 15%.
   - figs2d: an interval of 0.996–1.005 is implausibly narrow for about 126 cells.

### C. What I could not check

- Where the 1696 CRCNS MAs outside SLEEP lie (in WAKE, or outside cycles) and how their durations are distributed. A per-session table of MAs inside WAKE, inside SLEEP and outside cycles would settle problem 4.
- The burst-index bias on the real data. Medians from a spike-time ISI computation that keeps ISIs crossing second boundaries, set beside readings a and b, would settle it.
- Reading c computed from exact spike times instead of the 1-s grid, for REM episodes and packets.
- The fig3e and figs5 sextile tests with sextiles ranked on WAKE excluding the test windows.
- DANDI LFP alignment. The code ignores the LFP `starting_time` value, and the alignment check only covers spikes against UP states. Printing `starting_time` for each file would settle it.
- `fig5c-wake-movement` on DANDI. The notebook does not mark it blocked; it tests it on CRCNS only. The version's API metadata lists only DecompositionSeries, LFP, SpikeEventSeries, ElectricalSeries, ProcessingModule, Units and ElectrodeGroup, with no motion or EMG series. Reading c (EMG) could only be tested by deriving EMG from the wideband ElectricalSeries, if it is wideband. Opening one file's ElectricalSeries rate would show that.
