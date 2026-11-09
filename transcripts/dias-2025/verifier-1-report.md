**A. Outcomes (32 claims in the claims file)**

| Claim | My outcome | Reason |
|---|---|---|
| sample-sizes | reproduced | Reading (a) matches the paper's model counts exactly: 177/11798, 174/12318, 171/3250, and 11731/11481/3122 for the preliminary models (cell 12). The file holds 27486 specimens, within the 10% tolerance of 27366, and 27366 is exactly the number of specimens across the three main models. |
| table1-hy-wintering-temperature | blocked, too_large | The HY Stan fit was not run; the timing run in stan_models.ipynb estimates about 57 min. |
| table1-hy-prebreeding-temperature | blocked, too_large | Same as above. |
| s4-s6-spring-migration-temperature-none | blocked, methods_underspecified | Seed reading (1): the HPD of spring AHY MinTempNextSpringMig excludes 0 under readings (a) and (c), with upper bounds -0.0002 and -0.0005 (cell 21). Seed reading (2): no term excludes 0 in most of the 10 seed sets (cell 22). The criterion blocks the claim when the two seed readings disagree, and they do. |
| s5-s6-ahy-prebreeding-wintering-temperature-none | reproduced | Every listed term and its interaction includes 0 under both interval readings and all filtering readings (cell 24). |
| table3-autumn-ahy-prior-breeding-temperature | reproduced | Intercept -0.093/-0.094/-0.094 with pd 98.1/99.7/99.4%; slope pd 74/73/66%; all means within tolerance. Convergence caveat in B1. |
| s6-autumn-ahy-recent-breeding-temperature-none | reproduced | Both intervals include 0 under every reading (cell 26). |
| s4-hy-autumn-migration-temperature-none | reproduced | Both intervals include 0 under every reading (cell 28). |
| table2-spring-ahy-breeding-temperature | blocked, too_large | The spring AHY fit was not run (estimate about 75 min). |
| table2-spring-ahy-autumn-migration-temperature | blocked, too_large | Same as above. |
| table3-autumn-ahy-prior-autumn-temperature | reproduced | Both pd are below 90% (66 to 78%) and the means are within tolerance under (a), (c) and (d). |
| table3-autumn-ahy-recent-autumn-temperature | partially_reproduced | Slope pd is 89.98% (a), 90.01% (c) and 85.1% (d), so it falls below 90% under (a) and (d). Signs and means hold, and the intercept pd is below 90% under all readings. |
| table1-hy-wintering-prebreeding-precipitation | blocked, too_large | HY fit not run. |
| table2-spring-ahy-wintering-prebreeding-precipitation | blocked, too_large | Spring AHY fit not run. |
| table3-autumn-ahy-prior-wintering-precipitation | partially_reproduced | Intercept pd is 90.3% (a), 88.7% (c) and 89.4% (d); slope pd is 88.7%, 88.0% and 93.6%. Means are within tolerance and the preliminary intervals include 0 (cell 35). Under (d) two effects are on the wrong side of 90% (see B9). |
| table2-spring-ahy-recent-wintering-precipitation | blocked, too_large | Spring AHY fit not run. |
| s6-autumn-ahy-recent-wintering-prebreeding-precipitation-none | blocked, methods_underspecified | The seed readings disagree only under filtering reading (d): the chain-4 HPD of the tarsus by PrevPrecipWinMo interaction has upper bound -0.0003 with the recorded seed (cell 30), but excludes 0 in only 1 of 10 seed sets (cell 31). The criterion requires blocking in that case. |
| tables1-3-breeding-precipitation | blocked, too_large | The autumn AHY part is consistent with the paper: intercept -0.046 to -0.049, pd 92.6 to 94.5%, slope pd below 70%. |
| s6-autumn-ahy-recent-breeding-precipitation-none | reproduced | All intervals include 0 (cell 33). |
| tables1-3-year-intercept | blocked, too_large | The autumn AHY part is consistent: 0.191 to 0.193 with pd at least 99.6%. |
| table1-hy-year-slope | blocked, too_large | HY fit not run. |
| tables2-3-ahy-year-slope-none | blocked, too_large | The autumn AHY part is consistent: slope pd 72 to 79%. |
| table-s1-species-consistency-hy | blocked, too_large | HY fit not run. |
| s7-low-phylogenetic-signal | reproduced | The lambda modes (0.04 to 0.09) lie inside the paper's HPDs under every reading (cell 38), which is what the criterion asks. The fitted HPDs are much wider than the paper's; see B3. |
| s4-s6-no-multicollinearity | reproduced | Largest VIFs are 3.339, 2.427 and 6.084 against the paper's 3.34, 2.43 and 6.08, and all are below 10 (cell 42). |
| s4-s6-climate-variable-selection | reproduced | Under interval reading (i) the selected variables match the main-model predictors exactly in every class and every filtering reading (cell 44). |
| s4-s5-climate-size-interactions | reproduced | Under reading (i) the two named interactions are positive and exclude 0, and no other tarsus by climate interaction does, under all filtering readings (cell 46). This is fragile; see B5. |
| s8-climate-trends | reproduced | All 8 trend calls match the paper and the 6 means are within tolerance, under both data readings and both interval readings (cell 50). |
| climate-trends-cannot-explain-wing-increase | blocked, too_large | Needs the HY and spring AHY effects. The autumn AHY part has a positive trend with a negative effect for both breeding temperature and breeding precipitation. |
| climate-explains-little | blocked, too_large | Needs all three models. |
| s9-s11-expanded-ranges | blocked, too_large | No sensitivity model was fitted. |

Totals: 12 reproduced, 2 partially_reproduced, 2 blocked as methods_underspecified, 16 blocked as too_large.

**B. Problems**

1. [affects a conclusion] The autumn AHY Stan fits, cell [5] of `autumn_ahy_main_{a,c,d}`, do not converge well: 711 to 912 divergent draws out of 8000, largest R-hat 1.075 to 1.162, smallest bulk ESS 18 to 41. With an ESS that low, a pd has a Monte Carlo error of several points. The two partial outcomes rest on pd values within about 1.3 points of 90% (89.98 against 90.01, and 88.7 to 90.3), so neither partial outcome can be told apart from reproduced. Cell [6] also says the paper "reports no diagnostics"; the Methods (paragraph 6) say convergence was confirmed with R-hat and trace plots.
2. [affects a conclusion] Cell [6] of the autumn notebooks says an earlier run on another machine with the same seed "gave other draws" and that its numbers are not used. That run is not shown. When the outcomes sit on the 90% line, an unshown run that may give different calls amounts to selective reporting.
3. [does not affect a conclusion] s7, cell 38: the fitted lambda HPDs reach 0.30 to 0.48, against 0.16 to 0.21 in Table S7, and the modes are 2 to 3 times the paper's. The fixed effects and VIFs match closely, so `gibbs_glmm` does not reproduce MCMCglmm's variance-component posterior, or chain 4 alone is noisy. The criterion (mode inside the reported HPD) is still met.
4. [does not affect a conclusion] I tested `hpd`, `pd_direction`, `pmcmc`, `vif`, `outlier_mask` and `gibbs_glmm` on synthetic data and they behave as documented (for example, the HPD of N(0,1) is ±1.96, a VIF at r = 0.9 is 5.25, and the sampler recovers the slope and residual variance). `posterior_mode` with adjust 0.1 is noisy (0.91 for a Gamma(2,1), whose mode is 1), as MCMCglmm's function is.
5. [does not affect a conclusion] Cells 44 and 46: several bounds that decide an outcome are within 0.003 of 0: spring AHY tarsus by PrevPrecipWinMo, lower bound 0.0003 under (a); autumn AHY PrevPrevPrecipWinMo, lower bound 0.0028. The ten seed sets were already computed in cell 19 but were not consulted for these two claims, whose criteria have no seed rule.
6. [does not affect a conclusion] The 16 too_large blocks are about compute time, not data size. The estimates (57 and 75 min) come from a 200-iteration run that includes early warm-up (stan_models.ipynb cell 5). The Dryad file list (version 333377: Data.zip and README.md, SHA-256 matching the notebook) holds every input these claims need, including the B1 and B2 climate columns (cell 7). Some parts could be tested now:
   - The autumn AHY B1 and B2 sensitivity models (about 11 min each) fit within the limit but were not run.
   - Reading (a) of climate-explains-little for autumn AHY follows from the printed Table 3: every |climate effect| is below 0.03 except PrevTempBreedBase (-0.093) and PrevPrecipBreedBase (-0.048), and all are below the year effect of 0.19.
7. [does not affect a conclusion] s4-s6-spring-migration is blocked on a single chain-4 HPD bound of -0.0002, which excludes 0 in at most 2 of 10 seed sets. The block follows the criterion, but the evidence points towards the absence claim.
8. [does not affect a conclusion] The column numbers and dropped rows in `prepare` and `r_merge` are checked against the code's hard-coded row indices, and they match for all six models (cell 11). Year coding, class split and units (Time = Year - 1980, per year; year in decades in the main models) follow the claims file. There is no train/test split, so leakage does not apply.
9. [does not affect a conclusion; a gap in the claims file] For table3-autumn-ahy-prior-wintering-precipitation, the criterion defines "partially" for one effect on the wrong side of its line and gives no not_reproduced rule. Under reading (d) two effects are on the wrong side (intercept pd 89.4%, slope pd 93.6%), which the criterion does not cover.

**C. What I could not check**

- Script01, Script02 and lm_mod.stan are not among my materials, so I could not confirm the Stan port beyond the printed diff, whether Script02 prunes chitree.rds to the five species, or how it builds lambda. The diff is syntax only.
- The discarded earlier autumn AHY run. Its Table 3 should be printed.
- The Monte Carlo error of each pd. A per-chain pd, or MCSE and ESS per reported mu_i and mu_s, would settle B1.
- Seed robustness of the near-zero bounds in B5. A `seed_majority` call on those terms would settle it.
- Pooled-chain lambda HPDs and modes, to separate chain-4 noise from a sampler difference in B3.
- The HY and spring AHY main models and all sensitivity models were never fitted, so 16 claims have no evidence beyond the autumn AHY parts noted in A.
