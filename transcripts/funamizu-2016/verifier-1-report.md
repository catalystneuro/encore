**A. Outcomes (40 claims, from the claims file)**

The claims file says that when readings disagree, the claim is blocked as methods_underspecified. I applied that rule throughout, so several claims below are blocked even though the notebook settled them by adopting one reading.

| Claim | Outcome | Reason |
|---|---|---|
| session-counts | reproduced | Cell 8: 94 sessions, 8 mice; sessions per mouse match as a multiset; area/layer counts are 17, 15, 14, 16, 15, 17. |
| neuron-counts | reproduced | Cell 10, reading (a): ROIs per group match exactly (41,031 total). Per-session means match Supp. Table 1. |
| behaviour-timing | not_reproduced | Cell 12: start to reward is 9.30 ± 0.11 s (paper 7.4 ± 0.1). Zone time is 1.009 s under (a) and 0.896 s under (b), both outside 0.86 ± 0.01. |
| lick-goal-correlation | not_reproduced | Cell 14: the best reading (Pearson, onset "change") has every P < 0.01 (largest 0.0079), but r runs 0.218–0.822. Two sessions fall below 0.232 (0.218, 0.227). Close miss. |
| fig1c-licking-without-sound | reproduced | Cell 16: 4/4 no-sound comparisons and 4/4 continuous comparisons have P < 0.01. |
| supp1-licking-speed | blocked (methods_underspecified) | Cell 18: zone reading (b) passes under both speed readings (largest P 0.0066); zone reading (a) fails (P 0.08–0.79). The notebook picks (b) from the Supp. Fig. 1 panel titles; I could not verify those (see B2). |
| fig1d-muscimol-correlation | blocked (data_missing) | The archive's 94 assets are all behavior+ophys files from the 8 imaged mice. The 3 muscimol mice, which were never imaged, are absent. Nothing is testable. |
| fig1e-muscimol-variance | blocked (data_missing) | Same as fig1d. |
| fig1fg-muscimol-no-sound-licking | blocked (data_missing) | Same as fig1d. |
| supp2d-muscimol-overrun | blocked (data_missing) | Same as fig1d. |
| muscimol-locomotion | blocked (data_missing) | Same as fig1d. |
| sound-responsive-layer3 | blocked (data_missing), not independently confirmed | Archive metadata can't settle it. Each file has 1,085–1,240 `speaker_presentations` rows. The notebook says all of them are one-frame rows at trial starts, but prints no check of this (B7). |
| neuron-classes | not_reproduced | Cell 22: 2/12 counts within tolerance under O1 a, 0/12 under O1 b; gd and after-reaching counts run about 20–80% high. All readings agree. |
| fig2d-task-relevant-proportions | not_reproduced | Cell 24: 0/6 values within tolerance under every reading. Layer 3 PPC > PM has P = 0.051 under O1 a. |
| fig2d-goal-distance-ppc-more | reproduced | Cell 26: PPC is higher with P < 0.05 in 3/3 layers under all 8 combinations of reading and measure. |
| fig2d-after-vs-before | blocked (methods_underspecified) | Cell 28: the criterion is met under O1 a. Under O1 b, no PPC layer has P < 0.05 (P = 0.07–0.52). |
| fig2d-layer-distance-preference | blocked (methods_underspecified) | Cell 30: met under O1 a (PM L2 vs L5, P = 0.0083). Under O1 b, PM L2 vs L5 has z = −0.88, P = 0.38. |
| fig3b-distance-over-time | blocked (other: not run, compute time) | The data are present; "too_large" refers to the notebook's 14 h estimate, not to the data (B8). |
| supp6-distance-not-sound | partially_reproduced | Cell 82: 23/24 comparisons under all 16 readings. The miss is Step vs Distance, PM L5 after-reaching, P = 0.10. |
| tuning-similar-ppc-pm | blocked (methods_underspecified) | Cell 84: only one combination (O1 a, frames b, width) shows no layer with P < 0.05; the other 15 show differences. The criterion itself says blocked when readings disagree. |
| fig3c-continuous-ramp | reproduced | Cell 34: 12/12 under all 8 readings. |
| fig3c-ppc-ramp-without-sound | reproduced | Cell 36: 12/12 under all 8 readings. |
| supp8a-pm-no-sound | blocked (methods_underspecified) | Cell 38: met only under O1 a with trace a. Every other combination has PM L5 intermittent 1 positive with P < 0.01. |
| supp8b-slopes-lower-without-sound | blocked (methods_underspecified) | Cell 40: PPC 6/6 everywhere. PM is 4/6 under O1 a but 3/6 under O1 b (4 needed). |
| supp8c-ppc-steeper-than-pm | blocked (methods_underspecified) | Cell 42: met only under O1 b with trace b. Elsewhere, layer 3 at 25.1–8.4 cm is not significant. |
| supp9-preserved-representation | not_reproduced | Cell 44: group reading (a) fails under every O1/O3 reading; PM's median is nearer zero in 2 comparisons with P < 0.05. The criterion needs both group readings. |
| fig4-above-chance | blocked (methods_underspecified) | Cell 48: against the flat prior, 18/18 in all 8 configurations. Against permuted chance, 17/18 in 6 of 8 (PPC L3 intermittent 1 has z = +13.6). Reading (b) is not a real chance level (B3). |
| fig4c-ppc-lower-error | blocked (methods_underspecified) | Cell 52: met in 14 of 16 configurations. It fails under O1 b, shift 0.1, 0.42-cm bins, where PM is significantly lower in 1 bin. |
| fig4d-map-near-goal | blocked (methods_underspecified) | Cell 54: met with 4.2-cm bins. With 0.42-cm bins, PM is closer with P < 0.01 in 3–8 bins under every configuration. |
| fig4e-ppc-lower-uncertainty | partially_reproduced | Cell 56: 100% of bins in 14 of 16 configurations and 99.8% in 2. Every reading gives at least "partially". |
| supp11-sound-reduces-error | reproduced | Cell 74: PPC 3/3 with P < 0.01 under every reading. |
| fig5a-map-follows-continuous | reproduced | Cell 60: 24/24 under all 8 configurations. |
| fig5a-map-decreases-without-sound | not_reproduced | Cell 62: PPC L3/L5 pass in 13–14 of the 16 tests required. In intermittent 1 at 8.4–0 cm the median slope is exactly 0 (B10). |
| fig5b-map-slope-lower-without-sound | reproduced | Cell 66: PPC 6/6 and PM 4–5/6 under all configurations. |
| fig5-layer3-steeper-than-layer2 | not_reproduced | Cell 68: MAP slope for layer 3 vs layer 2 has P = 0.07–0.56 under all configurations (both medians 0). |
| supp13-map-speed | not_reproduced | Cell 76: at most 3 of the 4 required PPC L2/L3 tests pass under any of the 32 readings. |
| fig5cd-uncertainty-updating | reproduced | Cell 70: PPC 6/6 with P < 0.05 under all configurations. |
| fig5c-uncertainty-decreases-with-sound | reproduced | Cell 72: 6/6 under all configurations. |
| lognormal-decoder-better | not_reproduced | Cell 78: by RMSE, log-normal is better in 0/18 settings (Gaussian better in 15–18). By MAP error, 11–12/18 (16 needed). |
| svm-correlations | blocked (other: not run, compute time) | The data are present; the notebook's estimate is 1.4 h per reading (B8). |

The paper states no chance level for the decoder. The notebook's flat-prior chance has a median RMSE of 26.97 cm, against 15.64 cm for the decoder (continuous trials, main reading).

**B. Problems**

1. **[affects a conclusion]** Cells 27, 37, 47 and 53 settle disagreeing readings by adopting one as an assumption: O1 a ("91 of 94 sessions decoded" matches the paper), trace a, chance a, and 4.2-cm bins. The claims file's header requires blocked methods_underspecified when readings disagree. This bears on fig2d-after-vs-before, fig2d-layer-distance-preference, supp8a/b/c, fig4-above-chance, fig4c and fig4d. O1 a also fails to reproduce the class counts it is supposed to justify.
2. **[affects a conclusion]** Cells 17–18 (supp1) narrow O9 to the nearest no-sound zone, citing the Supp. Fig. 1 panel titles. The claims file names two zone readings. If the titles really fix the zone, the claims file left open a detail the paper gives, and supp1 would be reproduced. I could not render the figure to check.
3. **[affects a conclusion; claims-file issue]** Chance reading (b) of fig4-above-chance permutes distance traces across trials. In `F.decode(permute=True)` the traces are time-warped by trial fraction, so every trial still runs 67→0 cm and the tuning survives. On a synthetic test, the permuted "chance" decoder gave an RMSE of 1.07 cm, the same as the real decoder (flat prior 25.9; noise-only neurons 25.8). This reading does not measure chance.
4. **[does not affect a conclusion]** In `ppc_pm_bins` (cell 50), `np.median` over trials that include NaN (sessions without goal-distance neurons) returns NaN. That produces the printout "PPC lower in 0% of bins … significant 40" for layer 5, and the printed n counts NaN trials. Layer 2, which is what gets judged, has no NaN.
5. **[does not affect a conclusion]** In `classify` (cell 3), k-means runs pooled over all sessions. That is the author's choice, not the claims file's. It can't rescue neuron-classes, because the after+reward pool is already too large (PM L2: 808 vs the paper's 408). It may shift the marginal supp8 results; the per-session version was not run.
6. **[affects a conclusion]** `fit_single` profiles the width on a 25-point grid, so widths are quantized (medians 16.48, 21.15, 27.14) and heavily tied. The width-reading Mann-Whitney tests in tuning-similar-ppc-pm depend on this grid. With a continuous optimizer, the one reading that "passes" might fail, which would turn blocked into not_reproduced.
7. **[affects a conclusion]** Cell 5 asserts two things no output shows: that all `speaker_presentations` rows start at trial starts and last one frame, and that trial frames sum to the series length. The sound-responsive block rests on both. Having 1,085–1,240 rows for 150 trials is unexplained.
8. **[affects a conclusion]** fig3b and svm-correlations are blocked as "too_large" for compute time (14 h; 1.4 h per reading). The full 35 GB dataset was streamed in 40 min, so the data are not too large. Both claims are testable.
9. **[does not affect a conclusion]** In `supp11` zone reading (a), zones 58.6–25.1 cm are labelled sound or silent by condition alone, ignoring the first 33 cm that always have sound (`zone_slopes` does handle this). Reading (b) is unaffected and gives the same outcome.
10. **[affects a conclusion]** The MAP slope in intermittent 1 at 8.4–0 cm has a median of exactly 0 in every group: about 28% of trials have a constant MAP, and `wilcoxon_z` drops them (n = 284 of 390). This may be an argmax artifact of the 0.84-cm grid, and it was never checked. fig5a-map-decreases-without-sound and fig5-layer3-steeper-than-layer2 both hinge on it.
11. **[affects a conclusion]** The lick onset is taken as a change in the held lick frequency. This is a stated assumption forced by the data, but untested. The "any" variant collapses (r down to 0.003), which suggests the rate does not drop to 0 between bouts. lick-goal-correlation misses by 0.014 in r, so this detail could decide it.
12. **[does not affect a conclusion]** Decoder neurons are selected using all trials, including the trials being decoded. The paper does the same.

Helper checks on synthetic inputs all came out correct: the signs of `mwu` and `wilcoxon_z`; the `sound_zone` boundaries for both intermittent conditions; the P values of `_ttest_logp` (matched `scipy.stats.ttest_1samp`); leave-one-out `decode` (RMSE 1.07 cm with tuned neurons, 25.8 cm with noise).

**C. What I could not check, and the output that would settle it**

- **Supp. Fig. 1 panel titles:** no PDF renderer was available. A quoted or cropped image of the panel titles, added to the notebook, would settle B2.
- **Sound-mapping data:** print the start times of `speaker_presentations` relative to the trial starts, their durations, and a check that the sum of trial frames equals T for every session.
- **Reward time 9.3 s vs 7.4 s, and 0.48% vs 2.85% excluded trials:** print the NWB timestamps or rate against the constant FS = 30.9, and the distribution of reward times.
- **Lick-rate form:** print the fraction of frames at 0 Hz and a sample trace around a lick bout.
- **MAP in intermittent 1, 8.4–0 cm:** print the distribution of MAP values in that zone and the fraction of trials with a constant MAP.
- **K-means:** class counts and the supp8 results with k-means run per session.
- **fig4c layers 3 and 5:** medians recomputed with NaN removed.
