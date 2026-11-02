**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| data-composition | partially_reproduced | There are 5 male mice, but BSD017 has 13 sessions, not 14 (cell 15; the archive also lists 69 files). Photometry is in 48 of 69 sessions (0.696). BSD011 has photometry in all 14 sessions, not the L/R/none sequence. |
| perf-after-pretraining | reproduced | Reading (a)(i), first session pooled: 0.7373. Reading (a)(ii): 0.7315. Both are inside [0.669, 0.767]; chance is 0.5 in both the paper and the notebook (cell 17). |
| fig1f-performance-increase | reproduced | Reading (a): slope 0.00273, inside [0.001, 0.005], p = 0.0057. The regression has 69 points rather than 70 because BSD017 has 13 sessions (cell 19). |
| trials-to-switch | reproduced | Counting from 0, pooled: 2.460 (sessions 1–7) and 2.328 (sessions 8–14), both inside their intervals (cell 21). |
| trials-to-commit | reproduced | Sessions 8–14, counting from 0, pooled: 3.034, inside [3.00, 3.26]. The mean of mice, 3.084, is also inside (cell 21). |
| figs1-switch-measures-decrease | reproduced | All four slopes are negative (cell 23). The block-number slope for trial2asymp has p = 0.48, but the criterion asks only for the sign. |
| fig1e-stay-after-omission | reproduced | Odds ratios 6.496 and 4.016; d = 0.6253 and 0.6749. All are within tolerance with p < 1e-4 (cell 25). The RU and UR counts (9297 and 5649) are the paper's 5719 and 9428 swapped, so the paper's count labels look transposed. |
| figs6a-decaying-history-weights | reproduced | In all 5 mice the lag-1 choice×reward weight is positive and the largest. The mean over mice falls monotonically: 2.40, 0.88, 0.36, 0.08 (cell 27). |
| fig2c-bayesian-beat-rl4p | reproduced | BIfp −535.36 and BRLfwr −530.09, both within tolerance. All Holm-corrected p ≤ 0.0041, in both families and both sides (cell 30). |
| fig2c-complex-rl-beat-rl4p | partially_reproduced | With the code's forgetting rule all four values are within tolerance. The claims file makes the Methods' rule primary, and under it RLFQ3p is −460.66, outside −646.45 ± 53.62 (cell 30). The two readings disagree (see B6). |
| fig2c-rlcf | reproduced | RLCF −364.50, and RLCF − BIfp = 170.87, both within tolerance. BRLfwr is lower than RLCF with Holm p = 0.0097 two-sided (cells 32–33). |
| fig2c-no-bayes-vs-complex-rl | reproduced | Two-sided Holm-corrected p are 0.201–0.214, all ≥ 0.05 (cell 32). |
| fig2b-model-identifiability | reproduced | Conditions (1)–(4) are all True under both simulation readings (cell 38). |
| figs2-parameter-recovery | partially_reproduced | RL_meta is poor (α_ν r ≈ 0). BRLfwr is not good: α r = 0.32–0.40 and sw r = 0.42–0.46 (cell 39). |
| brlfw-alpha-zero | reproduced | α < 1e-6 in 4 of 5 mice (cell 35). |
| figs8-brlwrp-no-difference | not_reproduced | Behaviour: AIC(BRLwrp) − AIC(BRLfwr) = −80.3, p = 0.044. Dopamine: the CI [56.7, 65.4] excludes 0. The BRLfw variant's dopamine CI also excludes 0 (cell 62). |
| figs7-no-change-across-sessions | not_reproduced | For BIfp and BRLfwr, under both readings, the slope is negative with p ≤ 0.008 (cell 36). |
| fig2f-adaptation-after-switch | reproduced | Under all three readings BRLfwr and RLCF are above RL4p and closer to the mice (cell 41). |
| fig3b-sse | partially_reproduced | RL4p has the largest SSE under every reading. No reading has all six within tolerance: in (a)(i) PearceHall is 0.0813 against [0.0976, 0.1192] (cell 43). |
| fig3a-both-port-contexts | reproduced | Reading (b)(i): mice 0.2099, BRLfwr 0.1806, RL4p 0.4299, RLCF 0.2226, RFLR 0.2756. All are within tolerance (cell 44). |
| fig3c-aic-around-switch | reproduced | Trials 0–4, 2k − 2logL, mean of mice: −165.42, −164.59 and −166.20, all within tolerance (cell 46). |
| rl4p-learning-rates | reproduced | Per-mouse fits: α+ = 0.848, inside [0.77, 0.94]; α− = 0.731, inside [0.71, 0.75] (cell 34). |
| fig4bc-reward-omission | partially_reproduced | Signs hold with p < 1e-5 everywhere. No reading puts both coefficients inside their CIs: S38 cleaned DA-PT gives reward 1.717 and omission −1.559 (cell 51). |
| fig4bc-switch-effect | reproduced | S38 cleaned DA-PT: 0.517, inside [0.454, 0.552]. Rewarded switch 2.345 > stay 1.669; unrewarded stay −1.564 < switch −1.132 (cell 53). |
| fig4bc-no-laterality | blocked (methods_underspecified) | The readings disagree. Cleaned trials give p = 0.0003 and < 1e-4 (S38) and 0.010 and 0.002 (S46); all trials give p = 0.14–0.82 (cell 54). Under the cleaned-trial reading that the Methods use for neural analyses, it is not reproduced. |
| fig4de-port-duration | partially_reproduced | (1) ρ = 0.467, p ≈ 0. (2) ρ = 0.062, p = 9e-12. But the median of (trough − port_dur) is 1.70 s, not in [0, 1] (cell 56). |
| trial-cleaning-counts | partially_reproduced | 22,370 cleaned trials is within 20,952 ± 2,095, but over 38 sessions, not 34 (cell 48). |
| fig4f-bayesian-rpe-fit | partially_reproduced | Ordering and CI-above-0 hold under (a), (b) and (c). PearceHall (−14.2) falls outside [6.04, 32.83] under every reading (cell 60). |
| figs3-other-metrics | reproduced | All four metrics put BIfp and BRLfwr above RL4p, RLCF, RLFQ3p, RL_meta and PearceHall (cell 61). |
| fig4g-history-decrease | reproduced | ρ = −0.163, p = 7e-39. AAA mean over 0–1 s = 0.327, CI [0.293, 0.359] (cell 64). |
| fig4h-rpe-only-llk | not_reproduced | On the Fig 4G trials RL4p, not BRLfwr, has the highest llk. No reading is near −986: values are −575, −2877, −1964 and −9819 (cell 68). |
| fig4h-nonnegative-rpe-aaa | reproduced | AAA RPE: BRLfwr 0.278 and BIfp 0.591, both above every RL model (≤ 0.018) (cell 65). |
| fig4-consistent-after-reward | partially_reproduced | The ANOVA gives p = 0.17, so (1) holds. For (2) the smallest range ratio is BIfp's (0.0007), and RL4p (0.144) is also below BRLfwr (0.192) (cell 66). |
| fig4i-lmer-switch | reproduced | Reading (a-i): R_chosen:Switch −0.165 [−0.216, −0.115]; R_unchosen:Switch 0.100 [0.036, 0.164]. Both are inside the paper's intervals (cell 70). |
| fig4j-lmer-stay | reproduced | R_chosen:Stay is −0.099, inside [−0.11, −0.07], and every model's coefficient is negative (cells 70, 74). |
| fig4i-model-runchosen | reproduced | Under all three readings BIfp, BRLfwr and RLCF are positive with p < 1e-4, and the other four models show "little or none" (cell 73). |
| figs5-per-animal | reproduced | 4 of 5 animals show the Bayesian sign pattern; 5 of 5 show the switch/stay pattern (cell 77). |
| reward-switch-reward-count | reproduced | S38: 94 sequences out of 33,415 trials, both within tolerance (cell 49). This rests on the author's S38 session set. |
| figs4-lmer-feature-sets | reproduced | OLS: 3R+Sw(4) − L0:R(4) = −0.0051, and 3R+Sw's best minus 3R+Sw(4) = 0.0044. MixedLM: −0.0050 and 0.0000. All are within 0.01 (cell 79). |

That covers 39 claims: 25 reproduced, 9 partially reproduced, 4 not reproduced, 1 blocked.

**B. Problems**

1. [affects a conclusion] Session selection, cells 8–11. The claims file's AUC > 0.9 rule keeps no session; every AUC is 0.46–0.51. The author substituted their own rule: the per-session reward-vs-omission t > 5 (S38). That selects on the very contrast that fig4bc-reward-omission tests, and it gives 38 sessions, not 34. Every dopamine outcome rests on it. S46 is shown as a variant for fig4bc and trial counts, but not for fig4f, the LMER claims, fig4g/h or figs4.
2. [affects a conclusion] The claims file misreads the paper's AUC rule. An AUC between 470 nm samples and 415 nm samples rescaled by regression onto 470 nm is near 0.5 by construction, because the fit centres both series. I confirmed this on synthetic raw-scale data: AUC 0.4998. The paper's ">0.9" must refer to some other quantity. The notebook's `q.roc_auc` (on detrended signals) inherits this.
3. [affects a conclusion] fig4bc-no-laterality. The outcome turns on the trial-set reading, and the notebook does not resolve it.
4. [affects a conclusion] Cells 60 and 62, the `boot` function. Bootstrap CIs are taken over repeated random 70/30 splits of the same trials, and those repeats are not independent samples, so the CIs are too narrow. This matters for figs8, where "CI contains 0" decides the outcome. No animal-level test (n = 5) or per-animal Δllk is shown.
5. [affects a conclusion] figs8 behaviour, cell 62. p = 0.044 is borderline, and one mouse (BSD019) shows +0.04. With fits from a single optimiser start (`fit_model`), a local minimum in BRLwrp, which has 6 parameters, could move this p across 0.05. Multi-start fits were not checked.
6. [affects a conclusion] fig2c-complex-rl-beat-rl4p, cell 30. The claims file makes the Methods' forgetting rule primary. Its readings rule then makes the outcome depend on a variant that the paper's numbers plainly did not use: the code rule matches the paper to within 2 AIC on RLFQ3p. The cell-31 text says "reproduced" and does not apply the Methods-primary rule.
7. [does not affect a conclusion] Cell 30. RLFQ3p_methods is tested alone, not inside the Holm families, and the no-difference tests are not run with it. My hand calculation from cell 29 gives a non-significant difference, mean −69 with large spread.
8. [does not affect a conclusion] Cells 65–66. BIfp_methods RPEs are not shown for fig4h-nonnegative-rpe-aaa or fig4-consistent-after-reward, though the claims file asks for both BIfp variants. Neither outcome can flip: for the second, RL4p already beats BRLfwr.
9. [does not affect a conclusion] Cell 52. The Lasso preprocessing variant is run only for the four-factor OLS.
10. [does not affect a conclusion] Conclusion text was not removed from cells 22, 31, 33, 71 and 75. I formed my outcomes from the outputs, not from that text.
11. [does not affect a conclusion] I tested the helpers on synthetic inputs: `block_switch_measures`, `history_counts`, `three_trial_history`, `llk_cv` (matches the scipy log-density), `da_measures`, block lengths from `generate_frame` (7–23), and both RLFQ3p forgetting rules. All are correct. Cell 13 also shows the re-implemented models match the paper's code (likelihood differences ≤ 5e-11).

**C. What I could not check**

- **Which 34 sessions the paper used.** The dataset does not mark valid sessions; that is a paper/dataset gap, not something an output could fix. Showing fig4f, fig4i/j, fig4g/h and figs4 on S46 as well, or on the 34 sessions with the highest reward t, would show whether those outcomes depend on the S38 choice.
- **Per-animal effects.** Per-animal Δllk for fig4f and figs8, with an across-animal test, would settle problem 4.
- **Fit robustness.** Multi-start fits, at least for BRLwrp, BRLfwr and RL_meta, would show whether the figs8 behavioural p and the figs2 recovery values hold.
- **lme4 vs MixedLM.** lme4 was not run. An rpy2/lme4 fit of the cell-70 formula would confirm the statsmodels estimates.
- **Missing BIfp variant.** Cells 65–66 should also print BIfp_methods.
