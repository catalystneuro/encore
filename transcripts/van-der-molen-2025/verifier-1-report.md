**Verifier report, round 1: van der Molen et al. 2025 on DANDI:001603 (0.260923.0623)**

The claims file has 50 claims. The notebook tests 47 of them and marks three as blocked: supp8, supp27 and supp5.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| methods-burst-count | reproduced | Cell 11: the mean is 35.7, inside 38 ± 4. The SE is 6.2 against the paper's 4, and the agreement is fragile: four murine organoids have 0 bursts, offset by MO1 (113) and MO7 (156). |
| fig1c-example-burst-count | reproduced | Cell 13: HO1 has 46 bursts at both 700 and 800 ms. |
| ed1c-lognormal-rates | reproduced | Cell 16, reading (a) with all units: all-unit R² is 0.949 and backbone R² is 0.487 (7 fits, because HO7 has no backbone unit). Both are within tolerance. |
| fig1d-burst-duration | reproduced | Cell 18: HO1 to HO4 medians are 472 to 892 ms. |
| fig1e-peaks-near-burst-peak | blocked: methods_underspecified | Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree. |
| fig2-backbone-fraction | reproduced | Cell 22, reading (b) (units with at least 30 spikes): mean 0.331, SD 0.150, both within tolerance. Under reading (a) the SD of 0.166 is outside tolerance. |
| fig2e-b2b-correlation | reproduced | Cell 24: p 5.9e-36 (30% rule) and 1.5e-19 (70% rule). The test used 216 units. The 507 printed is all sorted units, which is a different quantity. |
| fig2g-variance-latency | reproduced | Cell 26: positive slope, p 3.6e-4 under reading (a) and 4.5e-5 under (b). |
| ed3f-burst-cluster-variability | reproduced | Cell 28: non-rigid CV is higher under all four readings, p ≤ 5e-48. |
| ed4b-gabazine-more-bursts | reproduced | Cell 32: +7.0 bursts per minute, p 5.5e-6. There are 4 paired organoids (MO12 has no baseline sorted file). |
| ed4b-nbqx-cpp-abolish-bursts | reproduced | Cell 34: treated recordings have 0, 0, 1, 0 and 0 bursts; p 3e-53. |
| ed4c-gabazine-participation | reproduced | Cell 36: +0.138, p 9e-4 pooled; the matched variant gives p 1e-8. |
| ed4d-gabazine-rank-order | blocked: methods_underspecified | Cell 38: the z-score reading gives gabazine higher, p ≈ 0. The (A−B)/(A+B) reading gives −1.14, p 0.6. That reading is degenerate here (problem 6). |
| supp2a-backbone-fraction-declines | partially_reproduced | Cell 40: holds for the human organoids under both readings. The archive holds no murine longitudinal recordings (every MO subject is P45D), so the murine half is missing data. |
| supp2c-b2b-increases-with-age | partially_reproduced | Cell 41, human organoids: age effect p 3.4e-8 (with unit type) and 4.8e-6 (with organoid); the paper gives 4.14e-6. Means rise with age, and backbone exceeds non-rigid at every age. The murine half is missing data. |
| supp8-backbone-stable-4h | blocked in the notebook, but testable | The notebook's reason does not hold. In the archive, HO2's 8M and 8M_4H files have 90 units each with identical x_pos/y_pos in the same order. HO3's 4H file equals its 0H file once its unit 24 is dropped. Units are therefore linked. No outcome. |
| ed5-shuffle-reduces-b2b | reproduced | Cell 43: (a) p 8.6e-26; (b) one-sided p 0.0072. This uses 10 shuffles, not 100. |
| fig3e-pairwise-correlation | reproduced | Cell 45: bb−mix and bb−nr p ≈ 0. |
| fig3f-backbone-pairs-in-tail | blocked: methods_underspecified | Cell 47: above the 75th percentile in all four organoids. At the 90th, HO3 fails (87th percentile). |
| fig4c-similarity-variance | reproduced | Cell 51: in HO1, inside < outside under both readings, and in all of HO1 to HO8. |
| fig4d-burst-similarity | reproduced | Cell 53: HO1 is significant at 100% of frames against both comparisons. HO8 is not (67% and 21%), but HO8 is only reported. |
| fig4e-similarity-rises-at-backbone-onset | partially_reproduced | Cell 55: holds in 7 of 8. HO7 has no backbone period. HO8 is marginal (0.329 against 0.326). |
| supp13-top-correlated-units-similarity | reproduced | Cell 57: top 20% higher and bottom 20% lower at 100% of frames. |
| fig4f-pca-variance | partially_reproduced | Cell 59: HO1 backbone is 75.4% (inside tolerance) but non-rigid is 17.4%, outside 25 ± 2.5. No organoid matches both. The across-organoid ordering holds in all 7 testable organoids; HO7 cannot be tested. |
| supp18-hmm-likelihood-real-above-shuffled | reproduced (not secure) | HMM notebook cell 6: real data beat the surrogate in 120/120 and 40/40 combinations. The real and surrogate data are scored differently, in a way that favours real (problem 3). |
| fig5c-states-converge-at-peak | not_reproduced | HMM notebook cell 8: 1 of 8 organoids meets reading (a) and 4 of 8 meet (b); 6 are needed. |
| fig5d-backbone-more-states | reproduced | HMM notebook cell 11: both readings p ≈ 0. |
| fig5f-svm-states-beat-rate | not_reproduced | HMM notebook cell 12: rate accuracy 73.9% is just outside 63.2 ± 10.4. The paired test gives p 0.081, and the per-organoid test is significant in only 4 of 7. |
| fig6f-slice-b2b-correlation | reproduced | Cell 61: p ≤ 2.4e-9 under all four readings. |
| fig6g-slice-pairwise-correlation | reproduced | Cell 62: all contrasts p ≈ 0. |
| fig7a-backbone-higher-rate | reproduced | Cell 66: all four model types p ≤ 2e-31. The murine organoid set is 5 of 9 recordings. |
| fig7a-primary-higher-rate | partially_reproduced | Cell 67: 5 of 6 contrasts hold; PR−MO backbone gives p 0.66. |
| fig7b-normalized-b2b | partially_reproduced | Cell 69: the within-type contrasts hold in HO, MO and MS. Backbone units of these types are not above primary-culture backbone units (p 0.11, 0.41, 0.22). |
| fig7b-primary-no-b2b-difference | reproduced | Cell 70: p 0.76. |
| fig7c-normalized-pairwise | reproduced | Cell 73: HO p 1.7e-4, MO p 6.6e-6. |
| fig7c-slices-primaries-no-pair-difference | reproduced | Cell 74: MS p 0.24/0.27 and PR p 0.46/0.49. |
| fig7c-backbone-pairs-above-random | not_reproduced | Cell 75: MO is not above 0 (p 0.35), and primary cultures are above 0 (p 0.004). |
| fig7d-lag-times | partially_reproduced | Cells 77–78: HO−PR and MO−PR are larger with p < 1e-6 under both readings. HO−MO is not significant (p 0.28/0.21). |
| fig7d-murine-organoids-slices-same-lag | blocked: methods_underspecified | Cell 79: MO−MS gives p 0.035 (drop zeros) and 0.059 (zero set to 1 ms). With Satterthwaite-type df it would probably be non-significant under both (problem 7). The secondary contrast, slices against primaries, fails under both readings (p 0.0037/0.0027 against the paper's 0.53). |
| fig7e-pca-backbone-variance | not_reproduced | Cell 81: the MO contrast fails under both readings (−0.04, p 0.23; +0.03, p 0.23). |
| fig7f-hmm-dimensionality | reproduced | HMM notebook cell 14: PR < HO (p 3e-6) and PR < MO (p 0.0033). This is a GEE, not the paper's GLMM. |
| supp24c-nonrigid-more-variable | reproduced | Cell 83: all four types significant for both raw and z-scored CV2. |
| supp24d-backbone-non-poisson | reproduced | HMM notebook cell 16: backbone median > non-rigid in every type, and non-rigid medians are ≤ 0.001. |
| supp10b-rank-order-by-model | blocked: methods_underspecified | Cell 85: the ratio reading gives main effect p 0.65 and HO−PR p 0.45; the z reading gives p 0.015 and 0.033. The z-reading HO−PR p would likely pass 0.05 with t-tests (problem 7), which would make this not_reproduced. |
| supp26-state-traversal | reproduced | HMM notebook cell 18: PR > HO (p 3e-6), PR > MS (p 0.0095), HO vs MO p 0.37. |
| supp27-d2-near-critical | blocked: methods_underspecified (counts only) | The notebook gives no reason; the attempt record is not available to me. The spike matrices for all 31 recordings are in the archive, so the intact-against-shuffled Welch test of d2 was testable. Only the AR fit-check counts are underspecified. |
| ed2d-alam-el-din-rates | not_reproduced | Cell 87: the Alam El Din fit is significant (p 0.0018); the paper has 0.40. |
| ed2e-alam-el-din-b2b | reproduced | Cell 88: p 0.0051 and 1.1e-5. |
| ed2f-backbone-pairs-above-zero | partially_reproduced | Cell 89: backbone pairs are above 0 in both sets, but Sharf mixed pairs are also above 0 (p 0.0085). |
| supp5-murine-organoid-forebrain-identity | blocked: data_missing | The data are on GEO, not in the dandiset, which holds electrophysiology only. |

### B. Problems

1. **[affects a conclusion]** `detect_bursts`. When two findpeaks peaks fall inside one burst whose rate never drops below 10% of the peak, the function emits duplicate bursts with identical start, end and peak. I confirmed this on synthetic input: one 3 s burst came out as two identical entries. The paper says min_dist "was increased up to 2000 ms" for long-burst recordings to avoid exactly this, and the notebook runs only 700/800 ms. Long bursts are present in HO5 to HO8 (up to 4.7 s), MO3, MO9 and the slices (cell 18). Duplicates inflate burst counts and produce identical burst pairs, which correlate at 1 in the burst-to-burst and rank-order measures. This could change ed2d, ed2e, ed2f, fig7 and methods-burst-count.
2. **[affects a conclusion]** supp8 is wrongly blocked (notebook cell 0 and cell 4). The archive links the units across the 0 h and 4 h recordings (table A). Both recordings were already analysed in `L` (cell 40), so the test needed only the backbone cross-table and a cross-recording burst-to-burst correlation.
3. **[affects a conclusion]** HMM notebook, `cv_recording` (cell 5). Real data are scored as log p(X_held | X_train), the difference of two likelihoods. The surrogate is scored as `loglik(m, S, ~train)`, the marginal likelihood of the held-out entries alone. On synthetic HMM data this asymmetry alone favours the conditional score by about 0.005 nats per entry on identical data. The smallest margin observed is 0.009. The surrogate should be scored as `loglik(S) − loglik(S, train)`.
4. **[affects a conclusion]** Recording-length reading (b), the shortest segment holding about 40 bursts, is not run anywhere. The claims file requires it where the outcome could depend on it. Slices have 7 to 24 bursts in 180 s of recordings 378 to 2187 s long, and MO7 has 156 bursts. Backbone sets for MS, MO and PR would change, and with them the borderline Fig. 7 results.
5. **[affects a conclusion]** Bursts are missing in murine organoids (cell 9): MO2, MO4, MO5 and MO6 have 0 bursts and MO3 has 4. All Fig. 7 murine organoid results rest on 5 of 9 recordings, and MO3 (4 bursts, 160/234 backbone) is kept. The notebook states this but never checks the cause; it prints no RMS against peak heights.
6. **[affects a conclusion]** `normalize` is applied to signed Spearman correlations (`rank_table`, cells 38 and 85). Because B ≈ 0, (A−B)/(A+B) is about 1 for most pairs and explodes when A ≈ −B; for example −0.01 against B = 0.01 gives −inf. That is why ed4d's estimate is −1.14 and why this reading gives no information. The notebook does not flag it.
7. **[affects a conclusion]** `lmm` uses Wald z where lmerTest uses Satterthwaite t. The docstring says this "matters only with few groups", but every between-type contrast here has 4 to 9 recordings per group. Borderline results that would likely move: fig7d MO−MS (p 0.035), supp10b HO−PR (p 0.033), fig7e reading (b) PR (p 0.046) and fig7c MS (one-sided p 0.043).
8. **[does not affect a conclusion]** `burst_to_burst` applies the 30-spike rule to `Mc.sum(1)`, which counts only spikes inside the cut burst neighbourhoods, not the whole recording.
9. **[does not affect a conclusion]** `burst_segments_compressed` says it is "exact", but it lengthens inter-segment gaps shorter than 351 frames to 351. I confirmed on synthetic input that a 1000 ms peak gap became 1222. This drops cross-burst lag terms in `pairwise_xcorr`; burst-only rates there are near zero.
10. **[does not affect a conclusion]** In fig2e, fig3e, fig6f and fig6g, the expected n is "units/pairs in the test". The notebook prints all-sorted-unit counts, which match the paper exactly (507, 34056, 959, 125607). The tested counts are 216, 9648, 715 and 89881. The exact match suggests the paper's tests included all units; that reading was not run.
11. **[does not affect a conclusion]** Deviations from the methods:
    - 10 shuffles instead of 100 (3 for the pairwise and similarity measures).
    - 11 of 21 values of K, with a 300-iteration cap; 34 of 341 models hit the cap.
    - A custom EM fit in place of SSM. This could bear on fig5c, which hinges on the very low entropy far from bursts in HO3 and HO4.
    - K is a fixed effect in fig5d, where the claim asks for a random intercept.
    - ed5 fits separate unit and organoid intercepts where the claim asks for both together.
    - ed4c's matched variant leaves out MO13 without saying why.
12. **[does not affect a conclusion]** No chance level is reported for fig5f. For HO5 and HO8 the rate-only accuracies (0.497 and 0.429) are below the majority-class rate (0.565 and 0.60). The paper does not state a chance level.
13. **[does not affect a conclusion]** Unit counts in fig7a: human organoids give 699 tested units and 930 sorted in the whole dandiset, below the paper's 1048. The archive appears to hold fewer human organoid units than the paper reports.

### C. What I could not check, and the output that would settle it

- **Duplicate bursts in the real data.** Needs the number of unique (start, end, peak) per recording against `n_bursts`, and the burst counts with min_dist 2000 ms.
- **Cause of the missing murine organoid bursts.** Needs RMS, the threshold and the top peak heights of the coarse rate for MO2 to MO6.
- **Shuffle quality.** Needs the swaps completed against those requested in `okun_shuffle` (`done` is discarded), especially for the dense MO and PR recordings.
- **supp18 with fair scoring.** Needs the surrogate scored conditionally, and each margin per fold.
- **Borderline mixed-model results.** Needs Satterthwaite-df (or parametric-bootstrap) p-values for the borderline contrasts in problem 7.
- **Recording-length reading (b).** Needs the Fig. 6 and 7 tables recomputed under it.
- **supp8.** Needs the backbone cross-table and the cross-recording burst-to-burst correlation, from the linked units.
- **supp27.** Needs intact and shuffled d2 per recording with the Welch test.
- **fig4f with the code's rates.** Needs the PCA run on burst-only rates that hold the inverse ISI across inter-burst gaps, as the code does. The non-rigid 17.4% may come from the notebook's zeroing between bursts.
