**A. Outcomes** (30 claims in the claims file; the notebook treats none as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| source-data-cluster-link | reproduced | With the cube's `cubeScript.m` normalization, all 1812 cue rows and all 1812 outcome rows match exactly one unit (largest difference 5e-15), and the L1 sizes equal the claims file's (cell 11). The claims file's own readings n-a to w-b give 0 exact matches; their best r > 0.99 covers 91.8% of cue rows and 95.4% of outcome rows. |
| fig1c-suppression-order | reproduced | Means 0.914, 0.709, 0.230. Under a-a, F(2,142) = 147.9 (149.2 ± 14.9), p ≈ 0. All three empty-trial rules pass, and all 73 session rows equal Source Data (cell 13). |
| figs2-each-rat-discriminates | reproduced | Under c-c, all 8 rats with at least 3 sessions meet it. Under c-a it is 7 of 8 (rat 9's U−S interval spans 0) and under c-b 5 of 8 (cell 15). Only the weakest reading passes fully. |
| units-sessions-subjects | reproduced | 1812 units, 965 from females, 73 sessions, and all ten per-subject totals equal. Subjects 5 and 10 each have one session fewer than Supplementary Table 1, which explains 73 against 75 (cells 4, 17). |
| fig1e-regions | reproduced | 21 regions. PMnR 236, DRV 208, DLPAG 179, VLPAG 147, DPG 145, and every region equals Source Data (cell 19). |
| fig2b-cue-clusters | reproduced | Medians over 20 seeds: min 24.0, max 218.5, median 75.0. All are within tolerance, the median only just (lower bound 74.7) (cell 21). |
| fig2c-cue-pc1-ordered | reproduced | PC1 is 29.73%. Mean cue weights are D 0.266 > U 0.128 > S 0.006 (cell 23). The 47.1% from Source Data comes from the baseline-subtracted heat-plot rows (all 1812 match). |
| fig2c-pc1-contribution | partially_reproduced | Under L1, k1 to k9 are the nine largest, k1 = 0.1214 and k2 = 0.1129, matching Source Data to 4e-4 (cell 25). Under L2, the criterion's "must" part fails: the nine largest clusters hold 411 units, outside 505 ± 50.5 (cell 26). |
| fig2d-danger-latency | not_reproduced | Both readings the criterion allows are negative but not significant: l-a R² = 0.067 (p = 0.26), l-b R² = 0.065 (cell 28). Only the k1–k9 < k10–k21 latency part holds. A 12-s window variant, which is not in the criterion, gives R² = 0.64. |
| fig2e-cue-subnetwork | reproduced | Under r², within k1–k9 is 0.445 against 0.184 with the other clusters, and k3 is lowest, for both 36 and 42 columns (cell 30). Under r only the first part holds, because k8 is lowest (k7 and k8 are anticorrelated with the others). |
| fig2f-cue-hubs | partially_reproduced | On the criterion's danger 14-interval r², k2 and k1 are the two highest (0.503, 0.462, both within tolerance). k1 does not exceed k3 or k4, and k2 does not exceed k3 (cells 32–33). Source Data equals the all-42-column r² instead, under which every test passes. |
| fig2g-cue-anatomy | reproduced | Every cluster spans at least 6 regions. The SC/PAG share is 0.436 in the subnetwork against 0.340, and 0.612 for k1 and k2 (cell 35). |
| fig3a-cluster-signals | partially_reproduced | Onset (k5) and offset (k15) hold under all four regression readings. Sustained (k10) fails: 0.77 < half of 1.69. Mid-cue (k6) fails: first second 0.60 is above half the peak (cell 37). |
| fig3b-signal-pca | reproduced | Recomputed matrix equals Source Data. PC1 62.73% and PC2 26.21%, and all five shape tests pass (cell 40). |
| fig3c-subnetwork-lesion | partially_reproduced | Under s-c/v-a, the PC2 first-second probability weight falls (0.201 < 0.268) and PC1 behaviour stays at 0.264, which is at least 75% of 0.274. But it is not above the supranetwork lesion's 0.268. The Source Data matrix gives the same result (cells 42–43). |
| fig3d-supranetwork-lesion | reproduced | Under s-c, PC1 behaviour is 0.268 < 0.274. PC2's |probability| peaks at second 2 and |behaviour| at second 10 (cell 43). The PC1 margin is very small. |
| fig3e-network-anatomy | reproduced | LPAG 7.41 and DPG 5.93 are the two largest and equal Source Data (cell 45). L2 gives the same top two. |
| fig4b-outcome-clusters | partially_reproduced | Medians over seeds: min 29 (46 ± 4.6, fails), max 304.5, median 161. Two of three are within tolerance (cell 47). |
| fig4c-positive-prediction-error | reproduced | PC1 17.68%. Uncertainty shock 0.194 > danger 0.071 > safety −0.032, and omission −0.005 ≥ safety (cell 49). |
| fig4b-phasic-network | partially_reproduced | Phasic indices (t-a and t-b) and the k1, k2, k3 profiles hold. With the criterion's Pearson r, the network part fails: within −0.329 against 0.008 with the rest. It passes only under r² (cell 51). |
| fig4b-tonic-network | partially_reproduced | The k6 to k8 profiles and the sustained test hold. With r, the network part fails: within −0.250 against 0.000. It passes only under r² (cell 51). |
| fig4e-network-pca | reproduced | Phasic PC1 37.01% and tonic PC1 29.20%, all shape tests pass, and the same values come from Source Data (cell 53). |
| fig4f-outcome-hubs | reproduced | r² values equal Source Data. k1 0.274 and k2 0.260 each exceed k3 0.148 (p < 0.05/3). k6 0.264 is highest and exceeds k7 to k9 (p < 0.05/6) (cell 55). |
| fig4g-outcome-anatomy | reproduced | Phasic share 0.600 > tonic 0.594. Tonic spans 20 regions, phasic 17 (cell 57). The effect is negligible (χ² p = 0.92); the criterion accepts it. |
| fig5a-outcome-cluster-signals | reproduced | The r-a, i-a matrix equals Source Data. k1 shock and PE are both transient, and for k6 mean |PE| / |shock| = 12.3, under all readings (cell 59). |
| fig5b-outcome-signal-pca | reproduced | PC1 53.74% and PC2 33.43%. PC1 is opposing and PC2 is dynamic (cell 61). |
| fig5c-phasic-lesion | reproduced | s-d gives 79.99% and 16.81%, and the shape tests hold (cell 63). |
| fig5d-tonic-lesion | reproduced | s-d gives 61.18% and 29.88%. The shapes hold and r with the intact PC2 is 0.895 (cell 63). |
| fig5e-no-anatomical-bias | partially_reproduced | Under p-b (k1–k5), the largest differential is 4.48, exactly Source Data, but the threshold is taken from that same quantity, so this cannot fail. Under p-a (the Results' phasic network k1–k3), PMnR is −9.82 and MnR −9.29, more than 6.72 (cell 65). I gave partially because the two readings disagree; this is my call, not one of the criterion's levels. |
| cue-outcome-membership-independent | reproduced | Under L1, 85/265 (χ² 2.30, p 0.13) and 159/613 (χ² 1.17, p 0.28); the 2×2 tests give p 0.10 and 0.19 (cell 67). Under L2 both fail (tonic goodness-of-fit p < 0.001, phasic 2×2 p = 0.004). |

Count: 20 reproduced, 9 partially_reproduced, 1 not_reproduced, 0 blocked.

**B. Problems**

1. [affects a conclusion] Cell 51, fig4b-phasic/tonic-network: the criterion says Pearson correlation, and under r both network tests fail. The notebook also runs r² without stating it as an assumption for this claim. The Methods passage ("Pearson's correlation coefficient (R2)", which covers the outcome period too) does allow r². This is a claims-file inconsistency: it allows r and r² for fig2e but not here.
2. [affects a conclusion] Cells 32–33, fig2f-cue-hubs: the Supplementary Methods say danger only, 14 intervals. The criterion follows that, and so the claims file does not misread the paper. Source Data matches the 42-column r² exactly, so the paper's figure was computed differently from its Methods. Under the criterion the claim is only partially reproduced.
3. [affects a conclusion] Cell 65, fig5e: the claims file's threshold (4.48) is the maximum of the p-b quantity itself. p-b therefore reproduces by construction once the data match. The non-circular reading, p-a, fails by more than 1.5×. This is a design flaw in the claims file.
4. [affects a conclusion] Cells 26 and 47, `kmeans_sizes`: the L2 labels come from one seed, the best of 20, while the claims file's standard is the median over 20 seeds. The L2 subnetwork total of 411 (fig2c-pc1-contribution) and every other L2 result therefore rest on a single solution.
5. [does not affect a conclusion] Cells 27–28: the markdown says the Source Data latencies "turn out to follow" the 12-s variant. The cell's own counts contradict this: l-a shares 513 values with Source Data against the variant's 413, and neither reproduces Source Data's 1498 units or its k1 mean of 182 ms. Even on Source Data's own latencies, R² is 0.508 under c-a and 0.394 under c-b.
6. [does not affect a conclusion] Cell 43: v-b is run on the s-a beta shuffle, not on s-c.
7. [does not affect a conclusion] Cell 55: in the Source Data Fig. 4f sheets, k7 has 171 rows and k8 has 111, which is the reverse of the Fig. 4b sheets (111 and 171). So the paper's labels for these two clusters are inconsistent between sheets. The notebook prints this without comment. Values are compared only as a set, and k6 is unaffected.
8. [does not affect a conclusion] Cell 5: the cube's `z.s1` is verified against the spike times, but `z.ms500` (the source of every outcome result) is not. It does match Source Data exactly.
9. [does not affect a conclusion] fig3c/3d: the criteria compare unit-norm PC weights between lesions, so "diminished" or "intact" measures shape, not magnitude. This is a weakness of the claims file.

Helper tests on synthetic inputs all passed: `change_point`, `mixed_anova_cue_by_group` (F and df agree with pingouin for both the mixed and the repeated-measures ANOVA), `pca` against eigenvalues, `pc1_percent`, `shuffle_rows`, `differential` and `suppression_ratios`. The archive file list (data.zip, two descriptor files, checksums.md5) agrees with cell 1.

**C. What I could not check**

- The MATLAB scripts inside data.zip, so none of the script-based choices could be verified: the outcome hub measure is r² (`outcomeAnalysis.m`); the beta columns run PE then shock; the regTerms order; the Shuffle dimensions; the region remap; the js10 to subject 1 mapping; and the empty-trial ratio set to 1. Some of these are supported indirectly by exact matches with Source Data, and the PE/shock column order is consistent with k6's firing pattern. Printing the cited script lines in the notebook would settle them.
- How the paper's Fig. 2d latencies were computed. Printing the latency block of `cueAnalysis.m` would have let me judge whether the 12-s variant is the paper's method.
- Whether L2 conclusions are stable. The fig2c contribution total and the cue–outcome tests, recomputed for each of the 20 seeds with their median reported, would answer this.
- Whether the s-c lesion result (fig3c PC1 0.264 against 0.268) is stable. The spread over iterations or seeds would show it.
