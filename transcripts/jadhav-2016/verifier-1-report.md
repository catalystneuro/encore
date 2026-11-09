**A. Outcomes (39 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| wtrack-learning | reproduced | Cell 8: day 3 correct is 0.85/0.80/0.75 with binomial p ≤ 0.0006 at every radius. Day 8 is 0.93/0.88/0.92, all above 0.8. |
| ytrack-learning | blocked (data_missing) | The archive listing (`hc-28/live/data/`) holds only the HPa, HPb and HPc archives. |
| tables1-cell-counts | partially_reproduced | Cell 10: PFC after exclusions is 167 against 165, within tolerance. Before the spike criterion, CA1 is 509 against 446, iCA1 81 against 69 and PFC 193 against 172, all outside 10%. Reading (b) cannot be counted because the data have no cross-day unit ID (checked). |
| swr-detection-stats | partially_reproduced | Cell 12: no single reading meets all three tolerances. Reading a on runs gives 414.6 per day (inside) but 79 ms and 0.17/0.34 Hz (outside). The mean-envelope reading gives 94 ms and 0.113 Hz at low speed (inside) but only 139 per day. |
| figs2-swr-at-reward-wells | reproduced | Cell 14: at 20 cm the fraction is 0.703 ± 0.032, inside 0.71 ± 0.03. |
| fig3-pfc-swr-modulation-fractions | not_reproduced | Cell 18: 12 excited, 7 inhibited and 148 unmodulated of 167, against 30/26/109. Every variant has 10 to 16% modulated cells, and none meets the "similar" rule. |
| ca1-swr-modulated | partially_reproduced | Cell 20: 255 of 392 (0.651). Most cells are modulated, but the value is outside 0.80 ± 0.08. |
| fig3-transient-responses | not_reproduced | Cell 22: inhibited cells return at 480 ms under both readings. Excited cells return at 330 ms under (b) and 480 ms under (a). |
| fig3de-ca1-precedes-pfc-peak | not_reproduced | Cell 24: CA1 against excited p = 0.35 (a) and 0.22 (b). |
| fig3e-onset-later-in-pfc | not_reproduced | Cell 26: CA1 against excited p = 0.58/0.40, CA1 against inhibited p = 0.093/0.052. |
| fig3f-swr-cross-covariance-lag | not_reproduced | Cell 66: the inhibited trough is at 200 ms, the edge of the window, under (a), and 35.9 ms under (b). The excited peak under (b) is 1.3 ms. |
| fig4-theta-locked-fraction | partially_reproduced | Cell 30: 89 of 167 (0.533), just outside 0.60 ± 0.06. |
| fig4a-preferred-phases | partially_reproduced | Cell 32: CA1 at 39° is in the falling phase and earlier than PFC. The PFC modal bin (90 to 135°) comes from a binning artifact (problem 1). Corrected for it, the 180 to 225° bin is densest, but only narrowly, so the PFC part cannot be decided. |
| fig4-swr-modulated-more-theta-locked | not_reproduced | Cell 34: inhibited against unmodulated p = 0.055. Only 7 inhibited cells. |
| fig4b-kappa | not_reproduced | Cell 36: excited against unmodulated p = 0.16 (a). Inhibited against unmodulated p = 0.78 (b), with inhibited kappa below unmodulated. |
| fig4c-theta-locked-more-swr-modulated | partially_reproduced | Cell 38: p < 0.01 under all three index readings. No reading's values match 5.2 and 2.5. |
| fig4-preferred-phase-concentration | not_reproduced | Cell 40: excited against unmodulated p = 0.32 (all cells) and 0.75 (locked cells). |
| theta-lag-past | reproduced (marginal) | Cell 42: reading (b) gives −25 ms, exactly at the edge of −15 ± 10. Reading (a) gives +5 ms and the mean-kappa curve is nearly flat. |
| fig5b-mean-rates | not_reproduced | Cell 46: excited against unmodulated p = 0.048, 0.043 and 0.051, never below 0.01. |
| fig5c-spatial-coverage | not_reproduced | Cell 48: excited coverage (0.27) is below inhibited (0.53), the reverse of the claim. The maps behind this have a defect (problem 2). |
| figs3-arm-and-direction-selectivity | not_reproduced | Cell 50: excited against unmodulated direction index p = 0.90 (mean) and 0.039 in the wrong direction (peak). |
| fig5e-speed-correlation | not_reproduced | Cell 52: excited against inhibited p ≥ 0.40 under every reading. |
| fig5f-pre-swr-vs-movement | not_reproduced | Cell 54: both group means are negative and p = 0.87. |
| figs3e-reward-modulation | not_reproduced | Cell 56: p = 0.091 (a) and 0.80 (b). |
| fig5g-ensemble-cofiring | not_reproduced | Cell 58: only 2 excited-excited, 1 inhibited-inhibited and 3 excited-inhibited pairs, so no comparison is near p < 0.01. In practice untestable because of the upstream classification. |
| fig6-swr-correlated-pairs | partially_reproduced | Cell 62 (a, a): 0.227 against a shuffled 0.045 (paper about 5%), z = 5.27, p = 7e-8. The fractions (0.227, 0.220, 0.239) are outside tolerance. |
| fig6ab-both-signs | reproduced | Cell 64: excited 21 positive and 7 negative, inhibited 7 positive and 10 negative. |
| fig6c-theta-predicts-swr-correlation | partially_reproduced | Cell 68: r = 0.48/0.46/0.58, all p < 1e-7, and the groups do not differ (shuffle p = 0.26). The r values are outside 0.39 ± 0.039. |
| figs4b-ca1-leads-in-theta | partially_reproduced | Cell 70: the mean peak is at +20 ms (excited) and +60 ms (inhibited). Pair counts are 21 and 7 against 46 and 26. |
| fig6e-glm-swr-prediction | reproduced (fragile) | Cell 78: above chance (p = 6e-5), modulated better than unmodulated (p = 0.005), excited and inhibited not different (p = 0.58), ensemble groups (b) ANOVA p = 0.019. The group means are not monotonic (0.052, 0.033, 0.101), only 16 modulated cells, and tertiles give p = 0.62. |
| fig6e-theta-trained-glm | not_reproduced | Cell 80: model type × group interaction p = 0.49 (the criterion's test). The other three parts hold. |
| figs4c-pfc-predicts-ca1 | not_reproduced | Cell 82: modulated against unmodulated p = 0.90, and unmodulated ensembles perform better (0.011 against 0.005). |
| fig7c-spatial-correlation | not_reproduced | Cell 72: inhibited stronger than excited, shuffle p = 0.079 and 0.163. Excited r = 0.172, p = 0.053 (concatenated maps). |
| figs5-matched-selectivity | not_reproduced | Cell 74: excited r = 0.236, p = 0.18. The match uses an IQR taken from 7 cells. |
| figs6-replay-content | blocked (other: not run) | Cell 92 estimates 22 min of shuffles for 1797 candidate events. The data (CA1 spikes, position) are in the archive, so the claim is testable and the block is not justified. |
| fig8a-no-prerest-swr-correlation-relation | reproduced | Cell 86: r = 0.065, p = 0.48 and r = 0.127, p = 0.29. The n (120, 71) is below the paper's 219 and 196, which weakens this absence result. |
| fig8bc-no-prerest-theta-spatial-relation | reproduced | Cell 88: none of the four relations is significant. |
| fig8d-glm-epoch-specific | not_reproduced | Cell 90: pre-rest-to-pre-rest against pre-rest-to-task p = 0.49. The other comparisons hold; n is 16/16/11/11. |
| figs7-both-tracks | blocked (data_missing) | Y-track animals are not in the archive (listing checked). |

**B. Problems**

1. [affects a conclusion] `hc28.hist_peak_phase` returns centres of 20° bins, and cell 32 counts them into 45° bins. The 90 to 135° and 270 to 315° bins each receive three centres, the others two. On uniform synthetic phases this gives 45° counts of [2806, 2576, 3691, 2244, 2053, 2044, 2865, 1721]. The PFC modal bin in cell 32 (90 to 135°, 18 cells) is exactly one of the inflated bins. Per centre, the 180 to 225° bin is densest (7.5 against 7.0). The fig4a outcome is unsettled; the same quantisation also creates ties in the cell 40 Kuiper tests.
2. [affects a conclusion] `hc28.rate_maps` sizes its bins from the first run (wtr1) and pools the wtr2 run of days 6 to 8 into the same bins. wtr2 is a different, larger track (x up to 218 cm, cell 4), and positions past the wtr1 arm length are clipped into the last bin. This corrupts coverage, arm and direction indices, and spatial correlation for 9 of 24 days (fig5c, figs3, fig7c, figs5, fig8bc spatial).
3. [affects a conclusion] The wtr2 runs (the novel environment used by Tang et al. 2017) are included everywhere, and this choice was run under one reading only. Whether the paper's "2 sessions on the W-track" include wtr2 is open, and it changes the SWR counts, the modulation classification and every claim downstream.
4. [affects a conclusion] SWR detection reading a appears to over-detect. Its low-speed rate is 0.335 Hz against the paper's 0.12 Hz (cell 12), and CA1 population rate 0 to 200 ms after onset is only 1.36 times the run mean (cell 6). All classifications after cell 18 use reading a. The PFC fraction is low under every variant tried, but the downstream claims were never re-run under the mean-envelope reading, the only one whose rate and duration match the paper.
5. [affects a conclusion] Position units were never checked. Cell 4 prints a wtr1 span of 130 × 116 cm for a track the paper gives as about 80 × 80 cm, without reconciling the two, and the `cmperpix` field is not inspected. The 4, 5 and 10 cm/s thresholds and the well radii all depend on the scale.
6. [affects a conclusion] Everything after cell 18 rests on 12 excited and 7 inhibited PFC cell-days. The failures in fig3de, fig3e, fig4*, fig5*, fig5g and figs5 are mostly the classification failure carried forward with little power, not independent evidence against those claims.
7. [affects a conclusion] theta-lag-past: 5 ms shifts are read on the 6.7 ms (150 Hz) phase grid by rounding (`theta_mask_times`), so neighbouring shifts can return identical phases. The −25 ms that reproduces the claim sits exactly on the tolerance edge.
8. [affects a conclusion] figs6-replay-content was skipped for time, by the notebook's own estimate about 22 minutes. That is not a block reason the protocol allows.
9. [does not affect a conclusion] Cell 18 computes `null_rate` (the shuffle's false-positive rate) but never prints it. My synthetic test of `swr_modulation` gave 5% false positives at 3 Hz, 100% detection of a 2× excitation and 98% detection of a 0.5× inhibition, so the function itself is correct.
10. [does not affect a conclusion] fig3-transient reading (a) requires a 7-cell mean to stay within ±1 SD of baseline until +500 ms, which noise nearly guarantees will fail. This is how the criterion is written, and reading (b) fails as well.
11. [does not affect a conclusion] Cell 66's SWR-aligned cross-covariance uses maxlag 0.505 s on ±0.5 s rasters, so a few spike pairs from neighbouring SWRs can enter. The inhibited extremum at the 200 ms window edge means no trough was found.
12. [does not affect a conclusion] figs4c uses 500 splits instead of 5000 (stated). Ensemble groups (c) cannot be tested because the smallest CA1 ensemble is 3 cells. In cell 80, groups (a) and (b) print identical results; this is plausible but was not shown.

Other checks passed on synthetic inputs: `std_xcov` sign (+30 ms recovered), Rayleigh false-positive rate (0.05), `vm_kappa` (0.48 for a true 0.5) and `detect_events`. I found no misreading of the paper in the claims file.

**C. What I could not check, and the output that would have settled it**

- Position scale: print `cmperpix` and the distances between wells from `linearcoord` against the roughly 80 cm track.
- SWR validity: print the CA1 rate gain per detection reading and the number of events per tetrode.
- Effect of wtr2: re-run the PFC modulation counts (cell 18) and coverage (cell 48) on days 1 to 5 only, or excluding wtr2 epochs.
- Fig4a: the 45° histogram built from raw spike-phase peaks taken directly at 45°, with no 20° pre-binning.
- Per-animal comparison: the expected Table S2 per-animal counts printed beside cell 18. The notebook only says they are in the supplement.
- Shuffle chance level on the real data: `null_rate` from cell 18.
- Downstream claims (fig3–fig8) re-run under the mean-envelope SWR reading.
