**A. Outcomes (39 claims, all tested in the notebook; none blocked)**

| Claim | Outcome | Reason |
|---|---|---|
| fig1c-total-suppression | reproduced | With 20 s total-fear baseline, 0/0 = 1 and trial mean (cell 18), means are 0.799 / 0.531 / 0.030 and F(2,174) = 595, t = 12.3 and 21.0. The paper reports 0.80 / 0.53 / 0.03, F = 592, t = 12.36 and 20.85. All 8 amended readings pass. |
| fig1c-nonlinear-scaling | reproduced | Uncertainty is above the danger/safety midpoint under every amended reading (cell 20; 0.531 vs 0.415 on the primary reading). |
| fig1d-interval-suppression | reproduced | Primary reading (2 s, 0/0 = 1): cue F = 493, interaction F(18,1566) = 6.15, and both pairs significant in 10/10 intervals (cell 22). The paper reports 489.4 and 6.21. The 0/0 = 0 and NaN readings drop to 8–9/10. |
| fig1s1a-nose-poke-rates | partially_reproduced | Danger and both uncertainty types fall and safety does not, in every window (cell 24). Baselines do not differ only with the 10 s window (p = 0.066). With the 20 s window that the Methods table supports, they differ: F(3,261) = 3.47, p = 0.017. |
| fig1s1b-sr-poke-correlation | reproduced | Danger and uncertainty r are about −0.70 with p < 1e-12, and the pooled r is −0.785, under all amended readings (cell 26). |
| fig1e-two-clusters | reproduced | Pre-cue baseline reading: 197/48 raw or 198/47 scaled, rate F = 835 (p < 0.001), duration and amplitude-ratio p = 0.97 and 0.51 (cell 28). The session-rate reading gives HFR 51, outside tolerance. |
| onset-population | reproduced | 29 neurons from 5 rats, all 29 in the LFR cluster under every clustering reading (cell 30). |
| ramping-population | reproduced | 17 late-responsive, 3 HFR, 14 Ramping from 4 rats (cell 32). |
| fig2a-onset-anova | reproduced | Cue F(2,56) = 8.64, p = 5e-4; bin p ≈ 1e-197; cue×bin F(218,6104) = 1.89, p = 1.6e-13 (cell 36). Cue F is just under the paper's "Fs > 9", which the criterion does not test. |
| fig2b-onset-first-interval | reproduced | D vs U t(28) = 5.05, p = 2.4e-5. U > S in mean, with p = 0.185. 60-bin cue×bin p = 0.024 (cell 38). |
| fig2b-onset-last-interval | reproduced | D vs U p = 0.062 and U vs S p = 0.57 (cell 40). D vs U is close to the threshold. |
| fig2c-ramping-anova | reproduced | All effects p < 1e-7, interaction F(218,2834) = 4.29. Last-second Z orders D 1.93 > U 1.20 > S −0.10 (cell 42). |
| fig2d-ramping-first-interval | reproduced | p = 0.67 and 0.63 (cell 44). |
| fig2d-ramping-last-interval | reproduced | t(13) = 3.14, p = 0.008 and t = 8.09, p = 2e-6 (cell 46). The paper reports 3.17 and 8.26. |
| fig2e-departure-times | partially_reproduced | Danger departs before uncertainty at both thresholds under all readings. No reading puts all four times within tolerance: the danger Bonferroni time is 4.5–4.7 s against 5.8 ± 0.58 (cell 48). |
| fig2e-rate-no-difference | reproduced | No reading matched for departure times, so all were checked: p = 0.84 and 0.63 (cell 50). |
| fig2s1-single-trial | partially_reproduced | Onset is above baseline at 32/32 positions and Ramping at 22/22 danger and uncertainty positions. Ramping is also above baseline at 6/10 safety positions, against the criterion's limit of 5 (cell 52). |
| fig2s2-nose-poke-cessation | reproduced | Holds with the differential measure under both ITI readings (cell 54). Onset: r = −0.02, sign 26/29, p = 1.5e-5. Ramping: r = 0.48, p = 0.08, sign 14/14, p = 1.2e-4. With raw rates, r ≈ 0.8 and p < 0.001. |
| fig3-onset-ramping-independent | partially_reproduced | Only 3 Onset–Ramping same-session pairs, against 4 with tolerance 0. Of 30 regressions, none has a negative beta at p < 0.05 (cell 56). |
| fig4abc-onset-single-unit-biases | reproduced | A: r = −0.47, p = 0.010, sign p = 0.008. B: r = −0.55, p = 0.002, sign p = 0.46. C: bias p = 0.008, r p = 0.07 (cell 58). Both correlations are negative (see problem 5). |
| fig4d-onset-patterns | reproduced | D>U>S = 14, the largest. Under the within-neuron shuffle it is the only one of the four categories above chance, by both rules (cell 60). The across-neuron shuffle flags S>U>D instead. |
| fig4efg-ramping-single-unit-biases | partially_reproduced | Panel E fails (r = −0.45, p = 0.11). F holds (r p = 0.09, sign 14/14) and G holds (cell 62). |
| fig4h-ramping-patterns | reproduced | D>U>S = 12, within 11 ± 1.1, the largest, and the only category above chance under the within-neuron shuffle (cell 64). |
| fig1s5-hfr-units | reproduced | All three HFR neurons fire most to danger, by raw rate and by Z (cell 66). |
| fig5a-onset-probability-first-interval | reproduced | P vs total fear t = 3.74, P vs interval fear t = 4.55; P against 0 p = 6e-5; fear betas p ≥ 0.58 (cell 70). The paper reports 3.75 and 4.57. Holds under 18/18 readings. |
| fig5bc-onset-beta-bias | reproduced | Primary reading: P 22/29 positive, p = 0.008; fear p ≥ 0.46 (cell 72). Holds under 17/18 readings. |
| fig5d-onset-all-intervals | reproduced | Primary reading: F(2,56) = 7.16, interaction F(18,504) = 2.35 (p = 0.0014), peak in interval 1, P significant in 4 intervals, smallest fear p = 0.156 (cell 74). The paper reports 7.16 and 2.38. Holds under only 7/18 readings (problem 7). |
| fig5s1-regressor-combinations | reproduced | Primary reading holds under both significance readings and both "weaker" readings (cell 76). Holds under 9/18 readings, and fails under every type-mean baseline reading. |
| fig5e-onset-tuning-curve | reproduced | Peak at 0.375, then 0.25 and 0.5 (cell 78). |
| fig5s2-binary-regressor | reproduced | 3-way F(18,504) = 2.49, p = 6e-4; first-interval F(2,56) = 7.75, p = 0.001; probability 0.863 vs binary 0.675 (cell 80). The paper reports 2.51 and 7.80. |
| fig5f-ramping-last-interval | reproduced | t = 3.62, 4.62 and 1.14 (p = 0.28) (cell 82). The paper reports 3.61, 4.68 and 1.11. |
| fig5gh-ramping-beta-bias | reproduced | All 4 parts hold on the primary reading (cell 84). Holds under 9/18 readings. |
| fig5i-ramping-all-intervals | reproduced | Means 0.577 / 0.120 / −0.026 with SEMs 0.136 / 0.100 / 0.050 (paper: 0.58 / 0.12 / −0.03 with 0.14 / 0.10 / 0.05). F(2,26) = 9.14 and F(18,234) = 2.19 (cell 86). |
| fig5s1-ramping-regressor-combinations | partially_reproduced | F and G hold. Total fear on its own (I) differs from zero (p = 0.0067) under all 18 readings, so the H–J part fails (cell 88). |
| fig5j-ramping-tuning-curve | reproduced | Peak at 0.625 under 18/18 readings (cell 90). |
| fig6ab-post-cue-firing | reproduced | Onset: all p ≥ 0.09. Ramping: interaction F(132,1716) = 3.14, the paper's value. Mixed ANOVA neuron-type interactions all p ≤ 0.0011 (cell 92). |
| fig6c-onset-post-cue-regression | reproduced | Regressor p = 0.48, interaction p = 0.77, smallest p against zero = 0.077 (cell 94). |
| fig6d-ramping-post-cue-regression | reproduced | Interaction F(8,104) = 7.00, P significant in 4/4 delay intervals, post-shock mean below delay mean (cell 96). |
| fig6ef-beta-correlations | partially_reproduced | Counts are Onset 3/20 and Ramping 0/20 at p < 0.05 (paper: 13 and 4), and 1/20 and 0/20 at p < 0.01 (paper: 6 and 1). The chi-square tests are not significant (cell 98). This is "partial" only because the criterion's partial branch needs Onset > Ramping, which 3 > 0 meets. On the main quantity it is not reproduced. |

**B. Problems**

1. **fig6ef, cell 98** [affects a conclusion]. The criterion's partial branch is met only by 3 > 0 and 1 > 0. The reported counts (13/20, 6/20) are missed by a factor of 4 under every reading, so I would read this claim as close to not reproduced.
2. **fig1s1a, cell 24** [affects a conclusion]. Baseline equality holds only with the 10 s window. The notebook's own data check (cell 13) favours the 20 s total-fear window, and there baselines differ (p = 0.017). Taking the null under the one window that passes amounts to choosing a reading.
3. **fig3, cell 56** [affects a conclusion]. Three pairs are found, against 4 with tolerance 0. The notebook does not show screen p-values for neurons near the 0.017 threshold, so it cannot be seen whether a fourth pair is a borderline unit.
4. **fig2s1, cell 52** [affects a conclusion]. Ramping is above baseline at 6/10 safety positions, two of them by 9–11 spikes/s. The claims file's ≤5 rule fails. The notebook prints the numbers but no outcome.
5. **`interval_z` / `cue_means`, fig4abc and fig4efg** [does not affect a conclusion]. Z-scoring across the 32 trials forces 6·D + 16·U + 10·S = 0 for every neuron. That alone pushes cross-neuron D–U and U–S correlations negative, and all four printed r values are negative (−0.42 to −0.57). The notebook reports them without comment. The paper's trendlines probably come from this procedure too, but the figure cannot be read. Panel E failing may come from this as well.
6. **`cluster_features(baseline="session")`** [does not affect a conclusion]. Pre-cue rates run about 3× the "session" rates: LFR 14.9 vs 4.67, HFR 92.8 vs 28.8, maximum 169.9 vs 51.5 spikes/s (cells 9 and 28). That suggests the spike trains have gaps, for example spikes stored only around trials, so spikes divided by span is not a session rate. This was never checked. Only the reading that failed anyway is affected.
7. **Reading sensitivity, cells 74, 76, 84 (and 86)** [does not affect a conclusion]. fig5d, fig5s1 (Onset) and fig5gh hold under only 7–9 of 18 readings. fig5d and fig5s1 fail under every type-mean baseline reading; fig5gh fails under both 2 s / 10 s readings. fig5i also holds under only 7/18, though its primary reading reproduces the paper's means almost exactly. Each outcome rests on the primary reading, which the Methods table pins down for details 1, 2 and 4. The fit is on one unit, but it is exact to 0.004, and fig5i, fig5d, fig6ab and fig1c match the paper's numbers nearly exactly. I judge the primary reading justified.
8. **fig2s2 (cell 54) and fig4d/h (cells 60, 64)** [does not affect a conclusion]. These pass under one reading of an open detail: the differential measure, and the within-neuron shuffle. The other readings fail. The claims file allows choosing a reading, and both chosen readings are the more literal ones.
9. **`waveform_features`** [does not affect a conclusion]. Polarity and the choice of peak and trough are the author's own reading. Half durations of 0.037–0.287 ms were not compared with the per-neuron values in Fig. 1, supplement 4. Neither waveform feature drives the clusters, so the outcome is unaffected.
10. **Helper tests** [does not affect a conclusion]. On synthetic data:
    - `rm_anova` matches statsmodels `AnovaRM` for 2- and 3-way designs.
    - `mixed_anova` matches pingouin for G, A, A×G, B and B×G. Its A×B and A×B×G terms were not checked against a reference.
    - `ols` matches statsmodels.
    - `sign_test` gives 27/29 → 1.62e-6 and 14/14 → 1.22e-4, matching the paper's p-values for those splits.
    - `suppression`, `counts` (half-open bins) and `waveform_features` behave as documented.
11. **Cell 6** [does not affect a conclusion]. Mean onset-to-onset time is 2.72 min against the stated 3.5 min ITI. This is a data finding that no claim uses.

**C. What I could not check**

- Whether spike trains have gaps (problem 6). A per-unit table of the longest inter-spike gap, or the fraction of the session covered by spikes, would settle it.
- Whether a fourth Onset–Ramping pair is a near-threshold unit. Screen p-values for every unit with 0.017 ≤ p < 0.05, with their session, would show this.
- The figure-only values (Fig. 4 R² and correlation sign, Fig. 5 tuning curves, the waveform features in Fig. 1 supp. 4). Printing per-neuron waveform features for the Onset neurons would allow a comparison if a PDF becomes available.
- `mixed_anova` A×B and A×B×G terms. A check against a reference implementation, or printing the sum-of-squares decomposition, would close this.
- The Methods-table match is shown for one unit only. Showing that the same windows also reproduce a second paper value, such as the Fig. 2, supp. 2 danger mean of 0.83, would strengthen the primary reading.
- I did not query the archive, since no claim is blocked.
