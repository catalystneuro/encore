**A. Outcomes** (40 claims in the claims file; all 40 are tested in the notebook, none blocked)

| Claim | Outcome | Reason |
|---|---|---|
| sessions-and-trials | reproduced | Cell 13: 25 F and 32 M sessions; 9863 F and 14251 M trials under reading (a), exact. |
| neuron-counts | reproduced | Cell 15: the data set's stored `average_firing_rate` (which the scripts use) gives 189/135/183 kept and 9/21/12 excluded, exact. The claims file's readings (a) and (b) are off by 1 to 4 per region. Totals 198/156/195 over 29 M and 24 F sessions match Supplementary Table 1. |
| choice-accuracy-ev | reproduced | Cell 17: ties left out gives 75.7 / 79.0 (tolerance ±7.7 / ±8.0). Ties counted as correct gives 76.66 / 79.83. |
| chose-on-partial-information | reproduced | Cell 19: the script's joystick-corrected count gives 85.52 / 71.43. The raw fixation count gives 54.2 / 42.6, so the outcome depends entirely on this definition (problem 7). |
| choice-accuracy-observed | reproduced | Cell 21: reading (a) gives 86.0 / 87.75 with npv250, and 79.1 / 81.4 with raw npv. Both are within tolerance. |
| figs1ab-cue-weights | partially_reproduced | Cells 23–24: every model A picture weight is >0 with p<0.05, and the first-side bias on option trials is negative with p<0.05 in both monkeys. Probability and magnitude weights are not "approximately equal" in M: ratio 1.11–1.15, Wald p ≤ 6e-4, and the CIs do not overlap on attribute trials. This fails under both readings and both value codings. |
| figs1cd-fewer-cues-more-accurate | reproduced | Cells 26–27: reading (B) gives 2-cue accuracy above 3- and 4-cue accuracy in both monkeys under every sub-reading with npv250. The mean value difference is largest at 2 cues. Reading (A) (true EV) fails. |
| fig2a-sample-the-favourite | reproduced | Cell 29: slopes of 0.73 (F) and 1.21 (M), p ≤ 3e-190. Chi-square also significant. |
| fig2b-positive-evidence | reproduced | Cell 31: both corners go the right way in each monkey (e.g. M 2.22 vs 3.15). Spearman ρ is −0.36 / −0.50. |
| fig4d-spatial-attention | reproduced | Cell 38: holds under all four O8×O9 readings. DLPFC CPD is 80%; ACC p=0.003 and OFC p=0.018. |
| fig4e-ofc-stimulus-identity | reproduced | Cell 40: OFC T=14.8, p<1e-4, CPD 35.8% (vs 3.6 ACC, 4.9 DLPFC), under all readings. |
| fig4f-ofc-attended-value | reproduced | Cell 42: OFC p=0.002, CPD 8.0% (larger than ACC and DLPFC), under all readings. |
| fig4g-left-right-value | reproduced | Cell 44: ACC p=0.007, DLPFC p=0.004, OFC CPD about 0, under all readings. |
| fig4h-acc-accept-reject | reproduced | Cell 46: ACC T=10.3, CPD 21.3% vs DLPFC 4.7%. Reading (a) holds everywhere. |
| figs2-consistent-across-subjects | reproduced | Cell 48: all 6 coefficients are positive in each monkey under both O9 readings. |
| figs4-dlpfc-top-bottom | reproduced | Cell 50: difference of 0.112 in DLPFC, against 0.042 in ACC and −0.001 in OFC. |
| fig4-t75-latencies | reproduced | Cell 52: all 9 values are within tolerance at a 10 ms step over −100 to 500 ms. At a 1 ms step they match to the millisecond except DLPFC left/right value (358 vs 369). |
| figs5c-latency-order | not_reproduced | Cell 54: fails under both residual readings and both variable sets. In ACC the left/right value range (252–492) overlaps accept/reject (229–272). In OFC the spatial attention range (13–93/99) overlaps attended value (−10/−13 to 286/367). |
| fig5a-ofc-value-cpd | reproduced | Cell 58: peaks at 290/300/290 ms; later epochs stay above baseline under every reading. |
| fig5b-stable-attended-value-subspace | reproduced | Cell 60: OFC r=0.845, p=8e-51. |
| fig5c-attribute-cue2-vs-cue1 | reproduced | Cell 62: r=−0.270, p=2.3e-4. |
| fig5de-option-cue3-vs-stored | reproduced | Cell 64: r=−0.283 (p=1e-4) and r=−0.379 (p=1e-7). |
| fig5f-option-stored-combined | reproduced | Cell 66: r=0.523 at cue 3, and −0.033 at cue 2 (consistent with the Discussion). |
| fig5gj-cross-correlation-dynamics | reproduced | Cell 68: all four maps have a significant cluster of the expected sign at 250 ms. EV6×EV5 across cue 2 and cue 1 is positive (r=0.755). Problem 3 applies. |
| fig5k-ofc-comparison-unique | reproduced | Cell 70: all six comparisons go the paper's way; 5 of 6 have two-sided p<0.05. p-values 0.040/0.067/0.011/0.003/0.0003 match the paper. |
| figs67-no-comparison-acc-dlpfc | reproduced | Cell 72: presence holds (r 0.66–0.85 and 0.52–0.56). None of the six attended-vs-stored r is negative with p<0.05. |
| fig6a-acc-belief-subspace | reproduced | Cell 74: T-statistic reading gives ACC 10/10, DLPFC 3/10, OFC 2/10. The coefficient reading would only be partial (ACC 8/10). |
| fig6b-acc-belief-stronger | reproduced | Cell 77: 19 of 20 larger in ACC; 13 of 20 two-sided p<0.05. |
| fig6c-belief-subspace-rt | reproduced | Cell 81: shortest RT bin is above the longest in 24 of 24 readings and both windows. 98–100 of 100 random splits agree. Problem 1 applies. |
| fig6d-belief-ramp-to-choice | reproduced | Cell 83: all five bins rise in 24 of 24 readings. Problem 1 applies. |
| fig6e-action-subspace-ramp | reproduced (marginal) | Cell 85: holds in only 2 of 48 readings. Elsewhere one bin peaks at −210 to −270 ms, just outside the −200 ms bound. Problems 1 and 2 could flip this. |
| fig7a-ofc-value-difference-neurons | reproduced (marginal) | Cell 87: OFC leads at all three tests under 4 of 12 readings, e.g. Figure 5 trial types, 250 ms, p<0.05: 6.0/4.4/6.6% vs ACC 5.3/3.2/4.8%. The differences are small and the chi-square tests are mostly not significant. Reading (b) never holds. |
| fig7b-ofc-value-difference-any | reproduced | Cell 90: OFC is highest under every reading where fig7a holds. |
| fig7c-acc-belief-neurons | reproduced | Cell 92: ACC is highest for 4 of 4 EVs at both bins and both significance levels. |
| fig8-cue1-value-all-regions | reproduced | Cell 97: p<1e-7 in all regions under all 25 readings. |
| fig8-action-value-acc-dlpfc | partially_reproduced | Cell 99: the tests hold under 7 readings, but in none of them are both fractions within 18±1.8% (e.g. the script reading gives 20.6% / 17.9%). The only reading with both fractions inside the tolerance has OFC above chance (p=0.002). |
| fig8-spatial-value-dlpfc | reproduced (marginal) | Cell 101: holds in 2 of 25 readings, both at α=0.01. There the DLPFC action fraction is 7.5–9%, against the paper's ~18%. It fails under the script reading (binomial p=2e-6 against the 1e-6 threshold) and under every α=0.05 reading. |
| fig8-attribute-value-ofc | reproduced | Cell 103: 6 readings, including the script's, give 23–26% with all tests passing. |
| figs9-ev16-correlation | reproduced | Cell 105: reading (b), averaged over neurons, gives 0.180 / 0.190 (tolerance up to 0.184 / 0.213). The largest other pair is 0.046. Reading (a) gives 0.190 for EV7, out of tolerance. |
| figs11-alternative-value-template | reproduced | Cell 107: the fig4f and fig4g outcomes hold under all readings with the alternative templates. |

Chance levels: the paper says OFC action value is "at chance". The notebook takes chance as the significance level α (or about 5% familywise for the permutation variant). OFC is at chance under the script reading (6.0%, p=0.41) but above chance under reading (a, i, a, 0.05) (10.4%, p=0.002).

**B. Problems**

1. [affects a conclusion: fig6c, fig6d, fig6e] `project` in cell 79 always uses the scripts' design: demeaned weights, a constant, and a column for the mean of EV11 and EV12. The Methods (paper lines 205 and 211) and the claims file's O6 describe regressing the rates on a neurons × 2 weight matrix. The Methods reading was never run, although `project(design=...)` supports it. For 6c and 6d the margins are wide. For 6e, which passes in only 2 of 48 readings, it could change the outcome.
2. [affects a conclusion: fig6e] `RB = 29` (cell 79) puts the action weights at the bin centred at −210 ms, as the scripts do. The Methods and the criterion say 200 ms before the response. Cell 55 says "both are shown where they matter", but Fig. 6 uses only −210. The failing readings for 6e peak at exactly −210 ms.
3. [does not affect a conclusion, probably] `cluster_test`/`PAIRS` (cell 68) compute each map within a single epoch (61×61). The criterion and the cell's own markdown describe cross-correlation over every pair of time points across the cue 1, 2 and 3 epochs. A larger map would raise the null maximum cluster size. The observed clusters are 817–1839 bins against thresholds of about 580, so the outcome probably holds.
4. [does not affect a conclusion] Units 87 and 653 are dropped, following the scripts. The analyses therefore use DLPFC n=134 and OFC n=182, while the paper reports 135 and 183, including for the Fisher tests in cell 70.
5. [does not affect a conclusion] The fig8 conclusions rest on choosing among 24 readings plus the script's. fig8-spatial passes only at α=0.01, where the sibling claim's ~18% action fraction is far off. `binom_p_code` (2·P(X>k)) is anti-conservative compared with an exact test. I re-checked with an exact test: reading (a, i, a, 0.01) still passes (p=1.3e-7), so that outcome holds.
6. [does not affect a conclusion] In cell 79, the O4(b) random halves are drawn independently for each unit, so simultaneously recorded units' weight trials overlap with other units' projection trials. Noise correlations could leak slightly. The odd/even reading has no such overlap and agrees.
7. [does not affect a conclusion; claims file] chose-on-partial-information has no criterion and does not name the definition of "evaluated" as open, although the outcome depends on it (85.5/71.4 with the joystick-corrected count, 54/43 with raw fixations, 96/92 with the 250 ms rule).
8. [does not affect a conclusion; claims file] figs1ab model A reading (b), the raw value signed ± by side, carries a ±0.5 side offset. That makes it partly a regressor for which side was fixated last, which is why the final-picture weight changes so much between codings (0.27 as rank, 2.16 as raw). Both codings pass the test.
9. [does not affect a conclusion] neuron-counts: the claims file asks for a comparison with the per-session counts of Supplementary Table 1. Cell 15 compares only the totals and the session counts.
10. [does not affect a conclusion] `conv_same_200` is shifted by 1 sample relative to numpy `same` (checked on synthetic data, max difference 0.005). On the synthetic checks, `ols` T-statistics, `cpd`, `chi2_yates`, `fisher_z` and `t75` match statsmodels and scipy, the RSA templates are correct, and the GLM bins span ±100 ms.

**C. What I could not check**

- Statements about the scripts: the one-sided RSA test, the thresholds of 1.64 and 1.96, `ttR(30)`, the variable set for Supplementary Figure 5C, the binomial formula, and the dropping of units 87 and 653. `scripts.zip` is part of the data set, which I was told not to download. Printing the relevant script lines in the notebook would settle these.
- The GLM is validated against the stored T-statistics (max difference 1.6e-6). The RSA, the cue 1 regression and the projections are not. The archive holds `neuronal_regression_results/info_gathering_cue1_both.mat` and `info_gathering_ramp_to_choice.mat` (the latter 5.3 GB). Comparing them with cells 95 and 79 would validate fig8 and fig6.
- Fig. 6 outputs that would resolve problems 1 and 2: the Methods' 2-column projection, and the action weights at the bin centred at −200 ms.
- Fig. 5g–j: full cross-epoch maps with the cluster test.
- Supplementary Table 1: a per-session comparison of unit counts.
- Archive: the S3 listing (83 keys) matches the files the notebook reads. No claim is blocked, so there was nothing further to test there.
