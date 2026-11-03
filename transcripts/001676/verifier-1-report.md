**Verifier report, round 1: Skromne Carrasco et al. 2026 on DANDI:001676, 0.251205.2137**

The claims file has 32 claims. The notebooks test 26 and treat 6 as blocked: fig1k, edf7g, fig3de, fig3e and fig3fg, with edf9 tested only in part.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| roi-counts | partially_reproduced | Neither reading gives 388 sessions (402 for all mice, 367 for mice 1 to 5; tolerance 0). Under reading (a), min 22, max 291 and mean 102.1 are within tolerance. The Spearman trend is significant in 2 of 5 mice, so "stable" holds (cell 13). |
| edf1e-hd-proportion | not_reproduced | At most 1 of 5 proportions is within tolerance under any reading. Under the main reading the values are 0.12, 0.40, 0.035, 0.29, 0.07 against 0.2, 0.7, 0.4, 0.7, 0.2. Recording counts match exactly; ROI means fail for mice 3 and 5 (238.8 and 129.8 against 197±18 and 102±25) (cell 15). |
| edf1h-ring | reproduced | Under z-score normalization the correlation is significant in 5 of 5 mice, but \|r\| is only 0.19 for mouse 1. Under max normalization 4 of 5 sessions keep too few bins to embed (cell 44). |
| fig1f-example-stable | reproduced | Reading (b), mouse 2 (n = 18): V 17.01, median absolute deviation 4.6°, p < 0.001, all within tolerance. Reading (a), mouse 4, fails under every configuration (cell 19). |
| fig1g-all-mice-stable | reproduced | Pooled V 75.58 with p ≈ 0, and 5 of 5 per-mouse means within tolerance. n is 85, not 84; the expected list sets tolerance 0 on n, but the criterion does not use it (cell 21). |
| edf4ab-vtest-per-animal | reproduced | Main reading: 5 of 5 V within 10%, and every V is above its shuffle median. The pooled shuffle median is 30.8 against 18.6±1.86, outside tolerance under every configuration (cell 23). |
| edf4c-previous-session | reproduced | Pooled V 70.00 with p ≈ 0; 4 of 5 per-animal V within tolerance under the main reading. The shuffle median is 26.6 against 21.9±2.19 (cell 25). |
| edf2ab-jaccard | reproduced | Under 12deg/raw, reading (a), 5 of 5 mice keep at least 80% of the 1-day index. Under the main reading only 2 of 5 (reading a) or 3 of 5 (reading b) do (cell 31). |
| edf2-no-registration-confound | partially_reproduced | Both absence tests are non-significant under every configuration. Displacement against score is significant only under pooled raw HDI with ×3 correction (p 0.0416). It would be 0.056 with four tests, and the main reading gives 0.50. n is 28 or 56, against 72 (cell 33; problem 4). |
| fig1h-drift-rate | reproduced | Main reading, population value, slope reading (a): 6.71°/week against 7.1±4.4 (cell 36). |
| edf4ef-not-diffusive | reproduced | Reading (a), main configuration: 4 of 5 mice. Fragile, since reading (b) gives 2 of 5 (cell 29; problem 9). |
| edf4f-change-below-shuffle | partially_reproduced | No configuration meets both parts. Under the main reading medians are 3 of 5 within tolerance but mouse 3 has p 0.079. Under 12deg/raw all p < 0.05 but medians are 2 of 5 (cell 27). |
| edf4g-pairwise-offset-stable | reproduced | 5 of 5 medians within tolerance and below all shuffled medians, for both signed and unsigned offsets. 25,441 values against 25,901±2,590 (cell 38). |
| fig1i-offset-drift | reproduced | 5.32°/week against 4.1±4.8. Wilcoxon p 0.19 and paired t p 0.13, both non-significant (cell 40). |
| fig1k-decoding-across-days | blocked (other: compute time) | No decoder output exists. The data are in the archive and the claim is testable (problem 6). |
| edf4ij-pv-decay | reproduced | Negative and significant in 4 of 5 mice under both readings; the mean at the longest interval is above 0 in every mouse (cell 42). |
| fig2e-offset-across-environments | reproduced | Medians within tolerance and below all shuffles. Drift is 2.41 (a) and 2.00 (b) with mouse 2 excluded, within 1.9±1.02 (cell 48). |
| edf5c-stable-within-environment | reproduced | All four V-tests are significant. 3 of 4 V are within tolerance under the main reading (square 13.81) and 4 of 4 under raw HDI. The ANOVA is non-significant (p 0.42 and 0.50), and the session counts 45, 39, 44, 43 match exactly (cell 50). |
| edf7-ephys-offsets | reproduced | Every median (6 to 12°) is below all shuffles, about half the paper's values but within its s.d. There are 254 PoSub units, matching 125 + 129. HD cells: 99 with smoothed HDI, 118 with raw HDI (cell 70). |
| edf7g-waveforms | blocked (data_missing) | Confirmed in the archive: the Units table holds only `electrode_group`, `id` and spike times, and `acquisition` has only Position and head-direction. |
| edf8-same-vs-mixed | partially_reproduced | Non-significance holds (p 0.125 and 0.062) and single is lower than mixed on average. W = 0 occurs only for linear variance, whose means (1.91, 3.15) are far outside 0.58 and 0.74. Circular variance and offset change have means within tolerance but are lower in only 4 of 5 mice (decoding cell 8). |
| fig2g-environment-classifier | reproduced | 0.64 against 0.28 (single split 0.70 against 0.21); W 15, p 0.031 (cell 58). Caveat in problem 5. |
| fig2i-random-remapping | partially_reproduced | Circular to square p 0.292 and square to radial maze p 0.517 are non-significant. Radial maze to circular gives p 0.069 (z 2.58) against 0.032 (cell 54). Run only under the main reading. |
| fig2h-coherent-remapping | not_reproduced | 10 of 15 mouse and environment pairs are coherent (67%, against the 80% threshold). The >30° part holds in 3 to 5 mice per pair (cell 56). Run only under the main reading. |
| fig3de-probe-memory | blocked (metadata_insufficient) | Confirmed: each protocol has its own CellReg table (mouse 5 example: 409×35 for the two-week protocol, 276×15 for the random one). No table links the last two-week visit to the probe week. From the asset dates, mice 1 to 4 have the probe week as the start of the random protocol, so the data exist but cell identity across the two protocols does not. |
| fig3e-mvl-delay | blocked (metadata_insufficient) | Depends on fig3de. |
| fig3fg-probe-drift | blocked (metadata_insufficient) | Same reason; the offset changes also need cell identity across the two protocols. |
| edf9-interference | partially_reproduced | All V-tests are significant. V is within tolerance for week 2 (10.38) and week 4 (10.56) but not week 3 (8.91). The drift rate (0.68, −0.11, 11.7) misses 1.6±0.16 under every reading. "Reduced retention" needs the blocked fig3de (cell 60). |
| fig4d-single-visit-memory | partially_reproduced | Both one-sided tests give p 0.031 and the group test p 0.188, matching the paper. The single-visit mean is 21.9° against 6.6±4.1, driven by mouse 8, which has 2 cells. With the groups swapped, both means would fit (cell 64). |
| fig4e-decoder-single-visit | reproduced | 42.5 and 48.8° are within tolerance, the group test p is 0.312, and all 10 decoders are below chance (83 to 97°) (decoding cell 6). |
| edf10c-environment-identity | reproduced (under the sign reading not run) | As run, square is −12.8°, outside tolerance under both assignments by 0.3°. Negating the printed means (sign convention, problem 1) puts both within tolerance under the first assignment. The Wilcoxon is non-significant either way (p 0.312) (cell 66). |
| edf10b-per-animal-change | reproduced (under the sign reading not run) | As run, 3 of 5 are within tolerance (not reproduced). Negated, the means are 3.25, −3.07, −12.43, 4.68, −7.71 against 4.7, −0.4, −15.5, 5.4, −6.2: all 5 within tolerance with every sign matching (cell 68). |

### B. Problems

1. [affects a conclusion] cells 66 and 68 (`xcorr_shift`, `pd_change`): the sign of the change in preferred direction is never run both ways. The Methods do not fix the cross-correlation direction. I checked on synthetic curves that `xcorr_shift` gives PD_b − PD_a. Flipping the sign turns edf10b from 3 of 5 into 5 of 5 and fixes edf10c. Under the flipped sign fig1g still passes (4 of 5), and every V and Rayleigh statistic is unchanged.
2. [affects a conclusion] cell 10 states that every claim resting on HD cells is also run under the other readings where it can change the outcome. That is not true. The following run only under the main reading:
   - fig2h (67% against the 80% threshold)
   - fig2i (p 0.069 against 0.05)
   - fig2g and edf4ij
   - edf9, fig4d, edf10b and edf10c
   - the edf8 and fig4e decoders
   - the edf7 offsets, computed with the 99 smoothed-HDI cells when the raw-HDI set (118) matches 125.

   The main reading keeps very few cells: median 3 per compared session for mouse 3, minimum 1 (cell 17). With 1 to 3 cells the identity shuffles are close to degenerate. This is a likely cause of the shuffle V medians above the paper's (11.9 against 5.7 for mouse 3; 30.8 against 18.6 pooled) and of the edf1e proportions, which are 3 to 10 times too low.
3. [does not affect a conclusion] cell 10 / `hd_table`: choosing the main reading to match the paper's session counts is partly supported. The Wilcoxon p values in Extended Data Fig. 4f imply n = 16, 18, 18, 16, 16 (for example, W = 0 with p = 3.81e-6 means n = 18), and the main reading gives 16, 18, 18, 16, 17. But it conflicts with the Extended Data Fig. 1e proportions, and cell 10 does not say so.
4. [affects a conclusion] cell 33: edf2 keeps only cells with CellReg score above 0.8, so the score range is 0.80 to 1.00. The paper tests "all cells" (n = 72) and separately "cells with CellReg score over 0.8", so the main tests include lower scores. Restricting the range weakens the score regressions. The correction is also over 3 tests where the claims file lists 4: with 4, the one significant result (0.0139) becomes 0.056.
5. [may affect a conclusion] cell 58, fig2g: cells absent from a recording enter as NaN, and 77 to 89% of features are NaN. The pattern of which cells are present follows the session date. Because each environment is visited in a two-week block, the classifier may be decoding time or detection from that pattern, not correlation values. No control keeps the NaN pattern while removing the values.
6. [affects a conclusion] decoding cell 10, fig1k: the block is a compute budget, not data size. The data are all present. The estimate is 101 min at 3.2 s per fit; the header of cell 0 says 3.7 h. Fits are serial although loading uses 12 workers. The partial criterion (pairs up to 10 days apart) needs only a subset of the fits.
7. [may affect a conclusion] decoding cell 4 (`decode`): test-session cells must pass the HD rule in the test session. The Methods say only "HD cells in common between each training and testing session" and give the rule for the training session. The looser reading is not run (edf8, fig4e).
8. [does not affect a conclusion] cell 44, `corrcc`: the p value assumes independent 0.25 s bins, which are autocorrelated. Mouse 1 has r = −0.19, which is weak evidence of a ring even though it passes the claims file's test.
9. [does not affect a conclusion] cell 29, edf4ef: a variance is unchanged by a constant shift, so readings (a) and (b) should agree except for which cells enter each session mean. They give 4 of 5 and 2 of 5. The pass under (a) rests on noisy session means.
10. [does not affect a conclusion] cell 59: "the random protocol's first week is the probe week" is stated without an output. I checked the asset dates. For mice 1 to 4 the random protocol follows the two-week protocol with no gap over 4 days. Mouse 5 has an 80-day gap (2021-07-09 to 2021-09-28), consistent with its exclusion from Fig. 3.
11. [does not affect a conclusion] I tested the helpers on synthetic inputs and they are correct:
    - `xcorr_shift` gives +30° for a 10-bin shift.
    - `hdi` gives 0 for a uniform curve and log2(120) for a delta.
    - `vtest` and `rayleigh` follow the pycircstat formulas.
    - `offset_changes`: the unsigned shuffle median for uniform offsets is 54°, the signed one 90°.
    - `drift_rates` recovers a slope of 7°/week.

    The unsigned reading treats +60° and −60° offsets as identical. Both readings are run and agree for edf4g, fig2e and edf7.
12. Claims file: I found no place where it misreads the paper.

### C. What I could not check

- Whether fig2h, fig2i, fig4d, edf10, edf8 and the edf7 offsets change under the raw-HDI reading. Needed: cells 52 to 68 and decoding cells 6 and 8 rerun with `CONFIGS[1]`.
- The sign reading for edf10b and edf10c. I got it by negating the printed means; the notebook should print both signs.
- edf2 with all CellReg scores (`score_min=-inf`) and Bonferroni over 4 tests, with n per mouse against 72.
- fig2g with a control that keeps only the NaN pattern (features set to 1 where present), and with a split that separates recordings in time.
- fig1k: errors against time-reversed chance by day difference, at least up to 10 days.
- The decoders with test cells "registered in the test session" in place of "passing the HD rule in it".
- HD cells per animal against Supplementary Table 2, which is not available. A per-session count of HD cells under each reading would show which reading matches the paper's cell numbers.
- I did not view the Isomap figure. The judgement rests on the printed table only.
