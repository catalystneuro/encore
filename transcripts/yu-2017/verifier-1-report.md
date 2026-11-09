**A. Outcomes** (all 32 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig1-iap-map-counts | blocked (data_missing) | The pooled count needs the W-track rats. hc-6 is on the archive (9 rats, about 23 GB), but the paper does not say which six rats or days it used, and some come from Kay et al. 2016. The foraging part is tested under fig1s4b and fails, so the pooled count could not be reached anyway. |
| fig1s4b-foraging-counts | not_reproduced | Cell 17: 14 IAPs / 180 MAPs under O2(a) and 17 / 177 under O2(b), against 33±3.3 and 244±24.4; neither count is in tolerance. The author's no-width-rule variant gives 16 / 250 (MAP count in tolerance), but that is not a reading the claims file allows. |
| fig1d-well-specificity | reproduced | Cell 19: IAP median index 0.998 (n=14), above the 0.8 and 0.9 bounds. MAPs score 0.992 too, so the index barely separates the two classes. |
| fig1e-iap-lower-speed | reproduced (foraging-only variant) | IAP median speed 11.8 vs MAP 27.8 cm/s, p=2e-5. The pooled test was not run. |
| fig1s4d-foraging-speed | reproduced | Cell 21: p from 2e-5 to 1e-6, IAP lower, under all O2/O3 readings. |
| fig1f-iap-smaller-coverage | not_reproduced | Cell 25: p=0.62–0.70 under both readings and both movement variants. Under the square-bin reading the IAP median is not smaller (208 vs 203). |
| fig1s1d-transition-interval | not_reproduced | Cell 27: the peak is at 14.3 or 16.5 s (4.1 s for the 15 cm variant), outside 5.76–7.26 s. Only O1(b) was possible. |
| fig2c-continuous-transition | reproduced (weak test) | Cell 48: the lower notch is above 0 in 50 of 50 bins at both entry and exit. The criterion is nearly trivial, and the windows probably cover most of task time (problem 3). |
| fig2s1cd-theta-autocorrelation | reproduced | Cell 50: during movement, MAP and IAP peaks fall at 0.115–0.125 s. Peak depth is larger moving than still in all four cases (IAP depths are tiny: 0.0010 vs 0.0004). |
| fig2s1ij-theta-behavior-correlation | not_reproduced | Cell 52: \|r\| ≤ 0.07 and p ≥ 0.41 for all four pair-type × window cases, under Pearson and Spearman. |
| fig2s2-fewer-coincident-spikes | not_reproduced | Cell 54: MAP-IAP 0.0075 vs MAP-MAP 0.0076, p=0.7. There are only 2 IAP-IAP pairs. |
| fig3c-iap-swr-activation | partially_reproduced | Cell 56: MAP not-in-field holds (p=9e-11). IAP not-in-field holds only under reading (b) (p=0.0044). IAP in-field fails under both readings (7.32→6.99 Hz, p=0.63). The criterion needs all three. |
| fig3s3-iap-same-well-coactivity | blocked (other: sample) | Cell 58: 2 IAP pairs, none at the same well, so the groups cannot be formed. |
| fig4a-swr-counts | partially_reproduced | Cell 31: fractions 0.720 and 0.238 are in tolerance; 0.042 is not (0.07±0.007). Observed "both" is far below expected (293 vs 1482, p≈1e-265), and the same holds in T1 and S2 separately. |
| fig4b-coactivity | partially_reproduced | Cell 60: MAP-IAP is below MAP-MAP under all four O6/O7 readings (p from 2e-5 to 0.016). The IAP-IAP comparison has n ≤ 1, so it cannot be tested, and that one pair is lower than MAP-IAP. |
| fig4s1b-offset-matched-coactivity | partially_reproduced | Cell 62: all four 1–5 s bins pass only under O7(a)+O6(a). With O6(b), the 2–3 s bin fails (p=0.074). With O7(b), only 1 of 4 bins passes. The (a) 4–5 s bin is likely inflated by peaks pinned at the ±5 s edge (problem 4). |
| fig4s2c-spatial-proximity-control | not_reproduced | Cell 64: panel B is significant in only 2 of 4 bins (MAP-IAP n=3 and 4 in the near bins). Panel C: Kruskal-Wallis p=0.28 and 0.22, with no IAP-IAP pairs. |
| fig4s3-overlapping-pairs | partially_reproduced | Cell 66: MAP-IAP is below MAP-MAP at entry and exit (p≤3e-8). Against IAP-IAP (n=2): p=0.23 under O6(a); under O6(b) p=0.027, but MAP-IAP is higher. So 2 of 4 comparisons pass. |
| fig4c-iap-swr-shorter | reproduced (foraging only) | Cell 33: medians 52.7 < 74.0 < 79.3 ms; all three KS tests p<0.05 (the weakest is 0.019). The order also holds in S2 and T1 separately. |
| fig4d-iap-swr-lower-power | partially_reproduced | Cell 35: IAP-SWR power is below both other types (p<1e-25), and IAP-SWR 25–35 Hz power is above 0. MAP vs MAP & IAP fails: p=0.34, and the median for MAP & IAP is lower. |
| fig4s5-cells-spikes-per-swr | not_reproduced | Cell 37: the cells test holds (1.03 vs 1.20, p=1.6e-14). The spikes test fails (2.12 vs 2.16, p=0.059), and the MAP spike mean 2.16 is outside 2.49±0.249. The criterion's partial outcome needs both tests to pass. |
| fig4s67-matched-subsamples | reproduced | Cell 39: in all 8 matching × reading × measure combinations, the median p is about 0 and the MAP-SWR median is higher in 100% of subsamples. |
| fig4s8-interspersed | reproduced (at the bound) | Cell 41: 18 of 360 bins (5.0%) have \|z\|>2, exactly at the ≤5% limit; the maximum z is 3.79. |
| fig4e-iap-spike-earlier | reproduced | Cell 43: IAP spikes are earlier under both readings (raw p ≤ 7e-14; duration-matched median p ≤ 4e-7; earlier in 100% of resamples). |
| pfc-unit-selection | partially_reproduced | Cell 70: 732 PFC unit-days is in tolerance of 712. 94 selected under both readings is below 112±11.2. The no-width-rule variant gives 113. |
| fig5-pfc-modulated-fraction | not_reproduced | Cell 73: 31 of 94 modulated (0.33) vs 0.63±0.063. |
| fig5dg-pfc-groups | not_reproduced | Cell 75: groups of 2 / 12 / 17 / 0 vs 14 / 20 / 33 / 3. IAP-SWR+ is significantly below its expectation (p=0.013), where the paper reports n.s. |
| fig5s1d-shuffle-control | not_reproduced | Cell 77: shuffle 0.331 vs data 0.394, p=0.17, so not significantly lower. The matched set does not differ (p=0.75). |
| pfc-regression-joint-swr | not_reproduced | Cell 79: R² = 0.272 (n=20, p=0.067) and 0.044 (n=82), vs 0.73. |
| fig6c-similarity-index | blocked (data_missing) | The archive holds only data.tar.gz with six file types per animal, and the task struct holds only `type`. There are no beam-break times, and the claims file allows only O1(a) for Fig 6. |
| fig6e-coincidence-index | reproduced (fragile) | Cell 81: IAP-SWR+ median +0.156, MAP-SWR+ −1.708, p=0.00058. But this rests on 2 IAP-SWR+ PFC units, and the PFC groups themselves did not reproduce (fig5dg). |
| fig6s2-no-proximity-difference | reproduced | Cell 83: p=0.52 for distance and 0.34 for offset. The test has low power (n=14 within-group and 28 across-group pairs, vs 39 and 169). |

Totals: 12 reproduced, 8 partially_reproduced, 9 not_reproduced, 3 blocked.

**B. Problems**

1. [affects a conclusion] SWR detection (`noise_threshold`, `process_animal`). The reading the claims file allows (mirror the z-scored amplitude below its mode, threshold at the 99.99th percentile) puts the threshold at −0.04 to 0.84 z. That gives 1.3–2.4 events per second of immobility. I checked on a synthetic Rayleigh-noise envelope: the same procedure puts the threshold at about 1.06 z, and 15% of pure-noise samples exceed it. So the event set probably contains many non-ripple events. That could plausibly dilute the PFC modulation results (fig5, fig5dg, fig5s1d, pfc-regression) and the IAP in-field activation (fig3c). The notebook shows no check of its own: no event rate compared with the literature, no fraction of immobile time inside events, no fixed 3-SD comparison. It does flag the low thresholds in cell 10 but carries on. This follows the claims file's reading; the claims file may be misreading the paper's "power" histogram.
2. [affects a conclusion] Scope (cell 0). Every `with_inputs` claim except fig1-iap-map-counts is judged on the foraging rats alone, which the claims file calls a variant. The pooled test was not run for any of them, and hc-6 is on the archive. The outcomes in table A for fig1e, fig4c and the like are therefore variant outcomes.
3. [affects a conclusion] Entry/exit windows (cell 45, `union`, O1(b)). Every immobility run counts as an entry/exit. Runs number up to about 1,950 per day, with a median length of 0.23–0.37 s, so the ±1.5 s windows around them likely cover most of task time. Two outputs suggest this: 94 of 113 MAP-IAP pairs pass the >100-event cut, and the entry and exit counts are almost identical (94/93; MAP-MAP 249/253). fig2c, fig2s1cd, fig2s1ij and fig4s3 then do not isolate transitions. The fig2c criterion (lower notch above 0, on non-negative normalized counts) is close to automatic.
4. [affects a conclusion] O7 edge pile-up (cell 46, `off5`/`off10`/`off33`). The offset is the argmax inside a truncated window, so pairs whose correlogram keeps rising toward the edge land at the window boundary. The 4–5 s bin holds 189 MAP-MAP pairs, against 86 in the 3–4 s bin, and drops to 56 under the 10 s window. The fig4s1b reproduction depends on that bin. `off33` is affected the same way and adds noise to fig2s1ij.
5. [affects a conclusion] fig5s1d (cell 77) uses a single permutation and a single matched draw per unit. The p=0.17 carries that sampling noise; averaging over many shuffles per unit could change the result.
6. [does not affect a conclusion] fig4s3 (cell 66) reports direction only for the MAP-MAP comparison. The O6(b) IAP-IAP p=0.027 goes the wrong way (MAP-IAP higher), and a reader could count it as support.
7. [does not affect a conclusion] fig4a (cell 31) pools the expected count over Q1 and N2 days, which have no IAPs and so cannot produce "both" SWRs. This lowers observed vs expected. The T1 and S2 tests on their own still give p<1e-100.
8. [does not affect a conclusion] fig6e (cell 81) and fig5dg treat overlapping pairwise comparisons from 2 PFC units as independent (the paper's test too), so p=0.00058 overstates the evidence.
9. [does not affect a conclusion] `coverage_linear` uses only the 4 perimeter segments. The paper says "Paths connect all reward wells", which may include diagonals; this is the author's choice, not stated as one. Neither rate-map function sets a minimum-occupancy rule. Both readings are null, so the outcome stands.
10. [does not affect a conclusion] 11 unit-days with an empty area field are dropped silently (cell 7). The statement in cell 34 that the stored LFP is referenced to corpus callosum is not supported by the descriptor.
11. [does not affect a conclusion] The no-spike-width-rule variant (R1 and N2 stored widths run about 0.2 ms longer) brings the MAP count (250) and the PFC selection (113) into tolerance. It is reported as a variant and correctly not used for outcomes, but the count failures depend heavily on it.

Helper checks on synthetic inputs all passed: `coactivity_z` matches a 5000-permutation estimate (4.035 vs 4.013); `noise_threshold` on a Gaussian gives 3.82 vs the true 3.72; `lags`, `detect_events`, `in_intervals` and `speed_from_rawpos` behave as intended.

**C. What I could not check, and the output that would settle it**

- **Whether the entry/exit analyses test transitions (problem 3):** the fraction of task time covered by the union of ±1.5 s entry and exit windows, per day.
- **Whether detected events are ripples (problem 1):** the fraction of immobile time inside detected events, and event counts and key outcomes (fig4a, fig5) under a fixed 3-SD threshold as a sensitivity check.
- **The edge pile-up (problem 4):** a histogram of the `off5`, `off10` and `off33` peak offsets.
- **Whether the 4-perimeter-segment linearization fits the maze (problem 9):** an image of immobile occupancy with the detected wells, and of the maze paths.
- **The shared-clock check for R1 and Q1:** cell 13 has no rows for them (no pyramidal cell in R1, no IAP in Q1, R1 or N2); a check using PFC spikes against SWRs would cover them.
- **The cause of the long R1/N2 spike widths:** the data hold no waveforms, so this cannot be checked from the data set.
- **fig5s1d's sensitivity to the single shuffle (problem 5):** the data-vs-shuffle p over many shuffles per unit.
