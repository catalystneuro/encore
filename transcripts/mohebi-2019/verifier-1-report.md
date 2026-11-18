**A. Outcomes** (37 claims in the claims file: the notebook tests 17 and treats 20 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| fig1b-latency-scales-with-reward-rate | reproduced | Cell 16: r < 0 in all 21 sessions, mean r −0.307, t-test p = 6.6e-11. The observed r falls below the 1st percentile of the shuffled-latency null (which also selects tau) in 19 of 21 sessions. Only electrophysiology sessions exist. |
| ed1b-latency-depends-on-recent-outcomes | blocked (data_missing) | There are no microdialysis sessions in the archive (see section B, item 12). |
| fig1cd-nac-core-dopamine-reward-rate | blocked (data_missing) | No microdialysis data. |
| fig1ce-ventral-prelimbic-dopamine-reward-rate | blocked (data_missing) | No microdialysis data. |
| ed1-behavior-similar-across-subregions | blocked (data_missing) | No microdialysis sessions. |
| fig2-tagged-dopamine-cells | partially_reproduced | Cell 19: the SALT light test alone passes 26 of 27 VTA-l cells and 2 of 2 IM-1078 cells, both within tolerance. With the criterion's waveform r > 0.9 added, only 23 of 27 pass on the largest wire (18 of 27 on all four wires), which is outside 27 ± 2.7. Two units had no 5 or 10 ms pulses, so the author tested 1 ms pulses instead, which is the author's own choice. |
| fig2d-dopamine-firing-rates | reproduced | Cell 21, bandit-task reading: mean 7.77, min 3.77, max 12.93 Hz, all within tolerance for both the 27-cell and 29-cell sets. Under the whole-recording reading the max is 11.60 Hz, which misses the tolerance by 0.01 Hz. |
| fig2d-dopamine-lower-rate-than-other-vta | blocked (data_missing) | Untagged units are not deposited. |
| fig2d-dopamine-longer-waveforms | blocked (data_missing) | There is no comparison group. |
| fig2d-non-dopamine-cluster | blocked (data_missing) | Untagged units are not deposited. |
| ed5-pavlovian-dopamine-click-responses | partially_reproduced | Cell 25: the means are ordered as claimed (47.3 > 42.3 > 37.5 Hz), but the ANOVA has p < 0.05 in only 12 of 27 cells, short of more than half. The tone-set count is 8 against 9 ± 0.9, outside tolerance (cell 9). |
| ed5-pavlovian-dopamine-cue-responses | partially_reproduced | Cell 28: the means are ordered as claimed (36.3 > 31.8 > 29.6 Hz), but p < 0.05 in only 10 of 27 cells. |
| ed5a-pavlovian-behavior | reproduced | Cell 30: in the 75/25/0 sessions, the 75% cue is highest and p < 0.05 in 5 of 7, and p < 1.2e-6 in 5. This holds under both per-trial measures. |
| fig2efgh-tonic-firing-indifferent-to-reward-rate | partially_reproduced | Cell 32: reading (a), the 1 min bins, finds 18 or 19 of 27 cells significant. Reading (b), the block means, finds 2 of 27 (median block dropped) or 0 of 27 (median block counted as low), but that test has almost no power (item 4). Across cells, high blocks run a median +0.5 Hz above low blocks (signed-rank p = 6e-4). |
| fig2fh-non-dopamine-no-tonic-change | blocked (data_missing) | No untagged units. |
| fig2i-burst-rate-no-change | reproduced | Cell 34: Wilcoxon p = 0.645, paired t p = 0.491; the median difference is 1.28 bursts/min. |
| fig2i-no-inactive-states | reproduced | Cell 36: the median time in long ISIs is 4.7%, 0.13% and 0% for the 0.5, 1 and 2 s thresholds, and every test has p > 0.16. The 0.5 s reading only just meets the 5% bound. |
| ed3-ctb-retrograde-labelling | blocked (data_missing) | No histology. |
| retro-tagged-cells-resemble-others | reproduced | Cell 38, reading (b): neither cell changes (p = 0.076 and 0.75), and here 5 or 6 blocks per side give the test real power; both rates are in range. Under reading (a), IM1078180827t14a is significant (p = 5.8e-5). |
| fig3a-dlight-specific | blocked (data_missing) | No in vitro data. |
| ed5-dlight-pavlovian-responses | blocked (data_missing) | No photometry. |
| fig3cd-dlight-reward-rate-minutes | blocked (data_missing) | No photometry. |
| fig3fh-dlight-tracks-state-value | blocked (data_missing) | No photometry. |
| fig3g-dlight-lag | blocked (data_missing) | No photometry. |
| fig4ac-dopamine-cue-responses | partially_reproduced | Cell 40: Go cue 27 of 27 and rewarded Side-In 24 of 27 meet the 75% bar. Light-On reaches only 16 of 27 (59%) with the 0.5 s window and 13 of 27 (48%) with the 1 s window. |
| fig4bc-dlight-cue-responses | blocked (data_missing) | No photometry. |
| fig4a-no-dopamine-firing-ramp-before-approach | reproduced | Cell 43: one-sided tests for an increase give Wilcoxon p = 0.99 (Center-In) and 0.41 (Food-Port-In), and sign-test p = 0.997 and 0.78. |
| fig4ef-dlight-ramps-before-approach | blocked (data_missing) | No photometry. |
| fig4e-light-on-alignment | not_reproduced | Cell 45: 16 cells respond to Light-On against the expected 25 ± 2.5 (22 even without correction). Under reading (a), 15 of 16 are better aligned to Light-On, not all. The short-versus-long latency part holds: 22 of 27 cells, p = 8e-5. |
| fig5a-early-trial-firing-not-reward-rate | not_reproduced | Cell 47: 8 of 29 cells (after Light-On) and 6 of 29 (before Center-In) correlate with reward rate at p < 0.01, against 1% expected (binomial p ≤ 4e-7), and most correlations are positive. The Friedman tests are not significant (p = 0.08 and 0.19), but the criterion requires that neither test show a dependence. |
| fig5a-positive-rpe-reward-cue | reproduced | Cell 49: tercile means 38.2 > 31.4 > 28.2 Hz, median r −0.31 (Wilcoxon p = 3.7e-8), 21 negative and 0 positive significant (17 and 0 after correction). This holds for the 27-cell set, Spearman, and the SD 4.5 ms kernel. |
| fig5ab-weak-negative-rpe | partially_reproduced | Cell 52: the pause count is 2 of 29 only under the "ISI-only" reading; the window-edge reading gives 8 (5 after correction). The valley part is never really tested, because the valley is 0 Hz on 100% of 3695 trials (item 1). Population pause duration rises with reward rate (Friedman p = 9.7e-5). |
| ed8-other-reward-expectation-estimates | partially_reproduced | Cell 54: the rewards-in-last-10 and actor-critic estimates meet the fig5a criteria. Q-learning fails because its terciles are not monotone (29.8 against 30.1 Hz), although 16 negative and 0 positive correlations are significant. The negative-weaker test passes only because the valley is degenerate (item 1). |
| fig5cd-dlight-positive-not-negative-rpe | blocked (data_missing) | No photometry. |
| fig5cd-dlight-early-trial-value | blocked (data_missing) | No photometry. |
| ed7-dlight-470-not-405 | blocked (data_missing) | No photometry. |
| ed7-non-dopamine-movement-activity | blocked (data_missing) | No untagged units. |

Tally: 8 reproduced, 7 partially_reproduced, 2 not_reproduced, 20 blocked.

**B. Problems**

1. [affects a conclusion] `vta_measures.bandit_pass` (valley), cells 52 and 54. With a 20 ms SD kernel (or the 4.5 ms variant), the minimum over a 2 s window is 0 Hz on every unrewarded trial (cell 52 prints 100.0%; I get the same on a synthetic 7 Hz Poisson train). Pearson r is then undefined and counts as "not significant". The criterion's "fewer valley than peak cells" therefore holds by construction, in both fig5ab and ed8. The authors' `Fig5_replicate.m` is in the data set and was not consulted for how they compute the minimum.
2. [affects a conclusion] `max_gap(edges=False)` (the "pause_isi" reading), cells 52 and 54. Trials with fewer than 2 spikes in the 2 s window become NaN and are dropped. Those are the longest pauses, so the dropping biases this reading toward no correlation, and this is the only reading that gives 2 of 29. The edge reading counts the silence from Side-In to the first spike, which is part of a pause, and it gives 8 of 29.
3. [affects a conclusion] Kernel reading, cells 25, 28 and 45. The claims header makes "variance 20 ms" (SD 4.5 ms) the primary reading and SD 20 ms the variant. The notebook reverses this on the strength of `getFiringRate.m`, which is a defensible source. But the Pavlovian peaks, Light-On peaks and alignment were run under SD 20 ms only. The ed5 per-cell ANOVA counts (12 and 10 of 27) could change under the primary reading.
4. [affects a conclusion] Reading (b) in `tonic`, cell 32. With 2 against 2 blocks a rank-sum test cannot go below p = 0.12, and with 3 against 3 its minimum is 0.0495 (checked). The 7 IM-1037 cells and 6 others have 2 or 3 blocks per side, so their "no change" was guaranteed. The 0 of 27 under `median_block="low"` therefore cannot be read as absence of an effect. Reading (a) treats autocorrelated 1 min bins as independent and is anticonservative; the variant that adds a time regressor still gives 16 of 27. The across-cell signed-rank test (p = 6e-4) is the sound test here, and it shows a change.
5. [affects a conclusion] Cell 47 (fig5a-early). The per-trial Pearson p-values ignore serial correlation within a session. Slow drift in firing that co-varies with reward rate, the same drift seen in item 4, would inflate the count of significant cells. On the criterion as written the outcome is still not_reproduced.
6. [affects a conclusion] Cell 19. The 1 ms pulse substitution for two units is the author's own choice and is not in the criterion. The waveform-wire reading changes the VTA-l total from 18 to 23, and neither total is within tolerance.
7. [does not affect a conclusion] `vta.salt` uses a 400 ms baseline, which gives 40 windows and 780 null distances, so the smallest nonzero p is 0.0013. "p < 0.001" therefore means p = 0 exactly. On synthetic data the test is calibrated (null p from 0.17 to 0.69; a responsive train gives 0).
8. [does not affect a conclusion] Cell 9. The deposited data have 8 IM-1037 cells, not the 9 the Methods give. This explains 8 against 9 in the ed5 tone-set count, a miss the notebook prints without flagging.
9. [does not affect a conclusion] `best_alpha`, cell 54. Several sessions hit the edge of the alpha grid (1.00 in up to 6 sessions; 0.01 once), so for those sessions the latency fit is weak.
10. [does not affect a conclusion] Cell 7. `rate_all_segments` divides by each segment's last spike time, not the segment's duration, so it slightly overstates the rate.
11. [does not affect a conclusion] `vta.bursts` follows the 80/160 template correctly. It does flag about 77 bursts/min on a 7 Hz Poisson train, so burst rate here mostly tracks firing rate. `cue_response` gave 0 of 40 false positives on Poisson data and detects a 30% added response.
12. [does not affect a conclusion] I listed the archive myself (the S3 bucket listing, `filelist.txt` and `checksums.md5`). It holds only `data_and_code.zip` and the descriptor documents, and the descriptor describes a 29-unit struct. The blocked claims are blocked. ed1b could be run on the 21 electrophysiology sessions only as a proxy, which would not test the microdialysis claim or its expected counts of 26 sessions and 7113 trials.

**C. What I could not check**

- How the authors compute the "minimum firing rate" and the pause. The notebook would need to print the relevant lines of `Fig5_replicate.m` and `getFiringRate.m`, plus the number of NaN `pause_isi` trials per cell.
- The ed5 click and cue ANOVA counts and fig4e reading (a) under the claims file's primary kernel (SD 4.5 ms).
- Whether the 0.5 s Light-On window overlaps Center-In, given median latencies around 0.5 s in IM-657 and IM-1078. A count of responding cells using only trials with latency > 0.5 s would settle it.
- Reading (a) with serial dependence handled, for example a block-permutation or circular-shift null of the high/low labels. The same applies to per-trial correlations in fig5a-early.
- The plots (cells 17, 26, 41, 50), which I read only through their printed summaries.
