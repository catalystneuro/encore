I've corrected the claims file for ds004752 and it is ready for an attempt. I edited only `claims/openneuro-ds004752/10.7554-elife.78677.yaml` and did not commit.

**Checker:** `21 claims, 20 quotes, 17 statistical values, 0 problems`. The first run gave 18 statistical values; one entry was removed, as described below. All quotes match the paper word for word, and the per-participant numbers copied from Table 1 match the table. I also read the paper's code (vdimakopoulos/verbal_working_memory at commit 395ae13).

**Changes, by claim:**
- **table1-left-hemisphere-sources:** removed the statistics entry. The p < 0.05 cluster test is what picks the "significant" sources being counted, so it is a threshold, not a result.
- **fig4bc-auditory-strongest:** the reported p = 0.0009 and p = 0.001 belong to the Kruskal-Wallis test alone. Dunn's test and the Bonferroni correction apply to the comparisons of other areas, so I removed them from the statistics; they stay in the criterion. The criterion now also lists the open choice of auditory cortex source, which it had left out.
- **fig2bc-gamma-encoding-p1:** the criterion said the paper never describes the z-score test, but the code defines it (`Statistics/PSD_fix_vs_enc_Permutation_test.m`). I wrote that test in, and added the band and window for contact H3 from the Figure 2b legend.
- **fig2fg-plv-theta-p1:** the comparison period was left open between fixation and encoding. The Figure 2f legend and the code both use fixation, so comparing with encoding is now a variant. I also added the check on individual contacts behind Figure 2g, which the criterion did not test.
- **fig2h-gc-reversal-p1** and **fig3-gc-reversal-p2-p3:** the [4 10] Hz window was invented; I replaced it with overlap with the paper's theta band [4 8] Hz. For fig2h, I named an open choice: the Methods describe the test at each frequency separately, the legend calls it cluster-based. I added the code's own significance script as a variant.
- **fig3no-p4-right-no-gc:** the paper names no band for the absence of Granger causality, so it is now judged over the full 4 to 20 Hz range rather than theta only; theta is still reported.
- **hipp-beta-maintenance:** added the per-participant beta bands from the Figure 3c, 3h and 3m legends as a second reading.
- **scalp-temporal-laplacian:** the paper reports no test for this finding. I named that as open, with two readings: the paired test of Figure 4d and the group test of Figure 4a.

**What remains open (recorded under `checks`):**
- The Figure 4d legend says its values and significance come from a 10% subsample of correct trials, while the Results present that subsample as a separate check. So `fig4d-reversal-all` and `balanced-correct-subset` may describe the same computation. Both readings are already in the criteria.
- The reported p-values (4.1e-10, and below 0.0005) are smaller than 200 permutations can produce, so both claims judge significance at 0.05 instead.
- Table 1's maximal source and t-value columns and the power spectra of Participants 3 and 4 (Figure 3g, 3l) have no claim. They are secondary; every main finding has a claim, and all claims come from this paper.

**Ready:** yes (`ready: true`).
