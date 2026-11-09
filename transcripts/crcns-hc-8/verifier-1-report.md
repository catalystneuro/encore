**Verifier report, round 1: Timme et al. (2016), CRCNS hc-8**

The claims file has 28 claims. The notebooks test 22, mark 5 as blocked (fig7ab, fig7a, figs2, fig7d, fig8-exponents-match-literature), and on review I judge one of those blocked claims, fig7ab, to be testable.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| fig3-chain-model-complexity | reproduced | Complexity is 0 at c = 0 and c = 1 and 0.431 bits at c = 0.8. Integration is 0, 5.84 and 11 bits for c = 0, 0.8, 1 (models.ipynb cell 4). |
| fig5d-bethe-small-avalanches | reproduced (fragile) | The size fit is accepted (p 0.338), but only over sizes 4 to 12. Corrected complexity is 0.00637 > 0. The same network states gave 0.00001 in cell 10, so "above zero" is within the estimator's noise (B1). |
| fig5e-shuffle-removes-complexity | reproduced (unreliable) | Size distribution identical; shuffled/original complexity ratio is 0.003 (cell 8). The original value is itself at noise level (B1). With the no-cut variant the complexity is also removed (−0.050 vs 0.271). |
| fig5f-network-state-poisson-keeps-complexity | not_reproduced (unreliable) | Relative change in complexity is 0.998 against a criterion of < 0.05; the size distribution did change (cell 10). The network states are the same before and after, so the miss comes from the estimator's noise (B1). The no-cut (0.049) and raw (0.020) variants pass. |
| fig6-cb-distribution-curvature | partially_reproduced | Durations pass all three parts (−1.23 at 0.2, +1.39 at 0.3, smallest at 0.25). Sizes fail: +0.087 ± 0.51 at 0.2, and the smallest magnitude is at 0.2/0.21 (cell 12). |
| fig7ab-cb-complexity-susceptibility-peak | not_reproduced (notebook: blocked, too_large) | The susceptibility half was computed by the criterion's method. It rises monotonically to the edge of the range (0.3) under both readings and has no interior peak (cell 16), so the claim fails whatever the complexity shows. The complexity half is untested. |
| fig7a-complexity-boundary-rise | blocked, too_large | Needs the sub-sampled complexity of the cortical branching model, which was not computed. I agree. |
| figs2-recording-length | blocked, too_large | Not run. Reading (b) (whole 100-neuron system, no extrapolation) needs only about 1,000 complexity calls and could have been run. |
| fig7c-cb-curvature-no-peak | not_reproduced | The extrapolated absolute curvature has its only interior maximum at 0.25 (4.667); the full-system curvature also peaks at 0.25 (cell 14). The 0.2 > 0.3 part holds. |
| fig7d-cb-branching-ratio-near-1 | blocked, other | It depends on fig7ab's peak, and there is none for susceptibility. For reference, B_new is closest to 1 at 0.28, which is within 0.0265 of the paper's 0.265. |
| culture-counts | reproduced | 435 recordings and 39,529 neurons, both exact. Median 91 and mode 93.3 neurons per recording, within 90 to 110. Firing-rate 5th/95th percentiles are 0.04548 and 7.70 Hz, inside 0.045 to 22 Hz; the lower one only just passes (cell 6). |
| fig2d-network-isi | reproduced | Median mean network ISI is 6.67 ms, within 7 ± 0.7 (cell 8). |
| fig2e-avalanche-count | not_reproduced | Median 83,289 avalanches and mode 81,707, against 10,000 ± 1,000. Only 2 recordings fall in 9k to 11k (cell 10). I found no error in the rebinning or avalanche code. |
| fig8-subsampling-exponents | reproduced | Sub-sampled τ (2.106 ± 0.407) and α (2.730 ± 0.579) are lower and less spread than full-system τ (2.491 ± 0.623) and α (2.928 ± 0.648). 1/σνz changes 3.6% and 1.6%. Both rebinning readings pass (cell 12). |
| fig8-exponents-match-literature | blocked, other | REFS is empty (cell 15). The reference values come from the three cited papers, and the archive does not hold them. |
| fig8-sigmanuz-methods-agree | reproduced | Differences of 0.056 / 0.130 / 0.133 are each below the larger SD (0.204 / 0.337 / 0.297) (cell 18). |
| eq4-exponent-relation | reproduced | 1.293 ± 0.694 and 1.565 ± 0.778 each lie within one SD of both 1/σνz estimates (cell 20). The test is lax: per recording only 21% agree within 0.1. |
| eq4-relation-randomized | reproduced | For wrap and Poisson the relation holds, and τ and α both differ from the real data by more than one SD (cell 22). |
| fig9-branching-ratio | reproduced | Band 0.05: 73.6% of recordings have B_new in [0.95, 1), and 94.7% have B_basic below 0.95. SD of B_basic is 0.088 against 0.064 for B_new (cell 24). |
| fig10a-complexity-randomization | not_reproduced (unreliable) | Five of six non-swap randomizations lower complexity, but shuffling raises it 74-fold (0.0019 → 0.145) (complexity cell 4). This pattern is what the 10-subset estimator produces (B1). The no-cut variant passes all six with Poisson among the two largest drops. |
| fig10b-susceptibility-randomization | reproduced | Reading (b) N·var(A/N) with BH: all five randomizations lower with p_BH < 0.05, Poisson the largest drop (cell 28). It fails under reading (a) or BY, where jitter1 is not significant. |
| fig10c-curvature-randomization | partially_reproduced | jitter10, jitter100, wrap and Poisson lower with p < 1e-37. jitter1 is +0.139 with p_BH 0.39 (cell 30). |
| figs8-complexity-susceptibility-correlation | not_reproduced (unreliable) | Pearson r is 0.542 (a) or 0.625 (b), against 0.23 ± 0.023 (complexity cell 6). Only the no-correction variant with reading (a) lands inside (0.221). |
| fig11ac-fit-range-randomization | reproduced | Poisson lowers the size and duration ranges (p_BH ~1e-141). jitter10 raises them (+0.047 / +0.070 decades, significant). jitter100 and wrap lower them; jitter1 is not significant (cell 33). |
| figs9-complexity-fit-range-correlation | not_reproduced (unreliable) | r = 0.143 for the size range (expected 0.296) and −0.049 for the duration range (expected 0.197) (complexity cell 8). |
| fig11bd-exponents-randomization | partially_reproduced | τ rises significantly for 4 of 5 randomizations; jitter1 lowers it significantly (p_BH 0.011). α rises for 3 of 5; jitter1 and jitter10 are not significant (cell 35). |
| fig12a-swap-preserves-complexity | not_reproduced (unreliable) | Swapping lowers complexity by 65% (rank-sum p_BH 3e-8) and Pearson r is 0.502 (complexity cell 10). The no-cut (p 0.42, r 0.968) and raw (p 0.81, r 0.996) variants both meet the criterion. |
| fig12b-shuffle-lowers-complexity | not_reproduced (unreliable) | Real complexity exceeds shuffled in only 10% of recordings, and r is 0.234 (complexity cell 12). The no-cut variant meets the criterion (99.4%, p 1e-25, r 0.856). |

"Unreliable" means the outcome rests on the corrected, cut complexity computed with 10 subsets per size (B1). Each of those verdicts should be redone before it is recorded.

### B. Problems

1. **[affects a conclusion]** `N_SUBSETS = 10` (models.ipynb cell 1, complexity_culture.ipynb cell 1, passed to `hc8.complexity`). Methods 2.9 says "the lesser of either all possible permutations of neurons or 100 randomly chosen permutations"; using 10 is the author's own deviation.
   - With 10 subsets the integration curve is noisy. The cut, which takes the first `find_peaks` peak of I(k)/(k−1), then falls on noise peaks.
   - I tested this on synthetic correlated data (60 neurons, 5 seeds). With 10 subsets the cut complexity ranged from 0.002 to 0.216 and kept 5 to 28 sizes. With 100 subsets it was 0.269 to 0.280 and kept 34 to 38. Shuffled data, whose neurons are interchangeable, was stable even at 10 subsets.
   - That explains three outputs: the real cultures keep a median of 8 of 94 sizes while shuffled data keeps 75; shuffling raises complexity 74-fold; and identical Bethe states give 0.00637 vs 0.00001.
   - Affected claims: fig5d, fig5e, fig5f, fig10a, figs8, figs9, fig12a, fig12b.
2. **[affects a conclusion]** models.ipynb cells 0 and 16. fig7ab is marked blocked although its susceptibility half was computed exactly as the criterion asks, and it fails. The claim should be not_reproduced, and fig7d should then be judged against that result.
3. **[does not affect a conclusion]** complexity_culture.ipynb cell 1 runs 180 of the 435 recordings, a subset the claims file does not allow. The p-values are far from the threshold, so the directions should hold.
4. **[does not affect a conclusion]** models.ipynb cell 1. Only p_trans grid reading (b) (0.01) was run. The fig6 and fig7c failures sit at grid points that a 0.005 grid also contains.
5. **[does not affect a conclusion]** culture_criticality.ipynb cell 13. Sub-sampling layout reading (b) was run on one recording only. On that recording it agrees with layout (a) to within 0.04.
6. **[does not affect a conclusion]** `hc8.apply_cuts` + `plmle_full`. After the cuts the tail has gaps, but the MLE normalizes over the whole xmin to xmax range. On synthetic data with τ = 1.6 this gives 1.692, while `plparams` gives 1.621. This follows the paper and the toolbox as the claims file reads them, and fig8's direction is the same either way.
7. **[does not affect a conclusion]** culture_criticality.ipynb cell 4. Exclusion reading (a) removes no recordings, so readings (a) and (b) are identical. The paper did exclude some recordings (Figure 2B).

Checks that passed:
- `fdr` matches `scipy.stats.false_discovery_control` for both BH and BY.
- `branching_new` recovers m = 0.949 for a true 0.95, and still gives 0.949 after 20% thinning, while the basic estimate drops to 0.73.
- `wls_intercept` is exact.
- `shape_collapse` returns 1.92 for a true value of 2, with negative curvature on arched profiles.
- The randomization seeds match between the two culture notebooks, swap and shuffle leave A(t) unchanged, and the Data.zip MD5 matches the archive's `checksums.md5`.

### C. What I could not check

- **The toolbox code.** nicholastimme.com did not respond, so I could not compare the `complexity.m` cut rule (peak of I(k)/(k−1), minimum peak distance max(3, 0.1N)) or the update rule of `cbmodel.m` with the ports. In the port, B_new is closest to 1 at 0.28 and susceptibility rises monotonically. Either the paper's model differs (for example, it has a refractory period) or it does not reproduce. Outputs that would settle this:
  - the corrected, cut complexity with 100 subsets and three seeds on about 10 recordings and on the Bethe raster, with its spread across seeds and the `k_kept` distributions;
  - for the cortical branching model, the mean avalanche size and the one-step branching ratio against 4·p_trans, compared with the toolbox output for one p_trans.
- **fig2e.** I cannot tell whether the axis of Figure 2E is logarithmic, because no PDF of the main article was supplied. A histogram of log10 avalanche count next to the paper's figure would show whether "around 10,000" is meant as an order of magnitude.
- **fig8-exponents-match-literature.** This needs the reference values from Mazzoni et al. 2007, Pasquale et al. 2008 and Friedman et al. 2012. The archive holds only Data.zip, `checksums.md5`, `filelist.txt` and the data description (plus a draft description under `orig/`), so no part of the claim can be tested from the archive.
- **Chance levels.** The paper states none for any selection, so there was nothing to compare.
