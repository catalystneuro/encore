**A. Outcomes (26 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| dataset-counts | reproduced | Cell 17: 291 rats, 184 M and 107 F, median 71 sessions and 33,493 trials, all exact. The Methods' other figure of 160 M / 114 F does not match the files. |
| zenodo-link | partially_reproduced | Cell 19: 273 of 291 rats (93.8%) match in full, which clears the 90% bar. 8 rats are missing 9 Zenodo sessions (3,645 trials). 10 rats hold the same sessions in a different order. |
| fig1f-wait-time-block | reproduced | Cell 22: reduction is 10.58% (reading a) and 10.79% (b), both within 10 ± 2.5. Signed-rank on z-scored means gives p = 4.6e-47, with high below low in 279 of 291 rats. |
| fig1i-initiation-block | reproduced | Cell 24: p = 1.82e-49, with high below low in 290 of 291 rats. This p is the test's floor for N = 291, the same value the paper reports. |
| figs2-unrewarded-drive | reproduced | Cell 26: median difference is 0.347 after unrewarded trials and -0.017 after rewarded ones; p = 1.8e-49, larger after unrewarded in 291 of 291 rats. |
| figs12-no-sex-difference | reproduced | Cell 28: rank-sum p = 0.238 for the wait ratio and 0.557 for the initiation ratio. |
| fig2a-wait-time-converges | reproduced | Cell 30: after/before = 0.067, under the 0.25 limit. Females alone give 0.207. |
| fig2b-initiation-previous-block | reproduced (literal criterion: not_reproduced) | Cell 30: the low-minus-high difference reverses after the switch (after/before -2.12, below zero in 290 of 291 rats, p = 1.8e-49). The criterion asks for "above zero", but the paper describes this reversal ("reminiscent of incentive contrast effects"; an "overshoot after transitions from high to mixed"). The data match the paper; the criterion's sign is wrong. |
| fig2cd-regression-kernels | reproduced | Cell 32: current-reward coefficient for wait times > 0 (p = 3.8e-49); previous-reward coefficient for initiation < 0 (p = 1.3e-37). Wait 1-back/current = 0.016. Initiation magnitudes at 1, 3 and 6 back are 0.031, 0.011 and 0.0009. |
| fig2e-tau-differ | reproduced | Cell 33: initiation tau median 1.63 against 0.00 for wait times; p = 1.5e-44, initiation larger in 262 rats and smaller in 5. |
| fig2f-tau-uncorrelated | reproduced | Cell 34: r = 0.023, p = 0.70. |
| fig2gh-fast-slow-groups | reproduced | Cell 36: initiation p < 0.002 (printed 0.000), wait p = 0.205, N = 115 (116 in the 10-back variant). The wait-time result is fragile (problem 4). |
| fig2j-wait-time-previous-reward | reproduced | Cell 38: 38 rats with p < 0.05, exactly the paper's 38 (chance would be about 15); population rank-sum p = 0.71. |
| fig2k-initiation-previous-reward | reproduced | Cell 39: 265 rats with p < 0.05, within 256 ± 25.6; population rank-sum p = 9.7e-25, slower after low offers in 227 rats. |
| fig2l-sensitivity-differs | reproduced | Cell 40: p = 2.2e-8 with the Methods' selection and 6.1e-38 with the code's (paper 6.21e-38). |
| fig3c-catch-probability | reproduced | Cell 42: counts 3/188/61/151/40 are all within tolerance. Mean wait falls strictly: 12.93, 11.77, 11.31, 10.60 s. |
| fig3j-model-comparison | reproduced | Cell 45: the inferential model wins in 291 of 291 rats, p = 1.8e-49. This is stronger than the paper's 1.07e-37 (problem 6). |
| figs9-misinference | reproduced | Cell 46: 10.87 s when inferred high against 11.91 s when inferred low; p = 1.1e-22, shorter in 230 rats. |
| fig3l-inference-quality | reproduced (weakly) | Cell 47, 20th/80th split: wait right asymptote (mixed to high) p = 0.003; initiation p = 0.32, 0.11. The criterion passes, but the inverse-temperature differences that the paper's text and legend stress (p = 0.02) are not reproduced (p = 0.34, 0.16). The groups are 61 and 108 tied rats (problem 3). |
| fig3h-dynamic-learning-rate | blocked (methods_underspecified) | I agree. The paper simulates the models with hand-set parameters and judges them qualitatively (Supplementary Fig. 7); the claims file gives no criterion. |
| fig4a-wait-ratio-learning | partially_reproduced | Fig4 notebook, cell 7: initiation ratio of the first pair is below 1 (median 0.749, p = 5.4e-7). The wait ratio of the first pair is not above pairs 16 to 25 (0.936 against 0.917, p = 0.23, 64 of 126 rats). |
| fig4bc-regression-learning | reproduced | Fig4 notebook, cell 9: \|block\| and \|reward\| coefficients are larger late (p = 9e-8 and 6e-9). Initiation coefficient, last/first 50 sessions = 0.99. |
| fig4de-overshoot-learning | blocked (other: not attempted; the stated reason does not hold) | The notebook says the `S_Structs` are needed. Yet `A_Structs_all`, which the Fig4 notebook already loads, holds ITI, block and per-session trial counts for every final-stage session. That is enough to compute the overshoot in the first and last 10 sessions (Fig. 4d) and its course over training (4e). |
| fig5b-precue-offer | reproduced | Cell 50: cue slopes are below zero in 16 of 16 rats (p = 3e-5) and below the original-task slope in 12 of 12 (p = 4.9e-4). |
| fig5c-precue-previous-reward | reproduced (marginal) | Cell 51, main selection: 14 rats, within 13 ± 1.3; population rank-sum p = 0.04. With the Methods' selection (after 30 cue sessions), 10 rats and p = 0.47, which fails (problem 7). |
| fig5d-precue-previous-block | reproduced (literal criterion: not_reproduced) | Cell 52: same sign reversal as fig2b; below zero in 15 of 16 rats, p = 9e-5. |

Tally (my outcomes): 21 reproduced (2 of them only after correcting the criterion's sign), 2 partially_reproduced, 0 not_reproduced, 2 blocked plus fig4de, which is untested.

**B. Problems**

1. [affects a conclusion] Claims file criteria for fig2b and fig5d; `transition_summary` (cells 30, 52). The criteria require the low-minus-high difference to persist with the same sign. The paper describes a contrast effect, and the data show that reversal in 290 of 291 rats. The notebook prints the numbers but does not address the conflict. Read literally, both claims fail.
2. [affects a conclusion] fig4de block (cell 48). "Data missing" is not justified: `A_Structs_all` contains the needed fields and is already loaded in the Fig4 notebook. The dandiset's own included sessions would also allow a later-training version.
3. [affects a conclusion] `fit_rat` (cell 44), fig3l. At each λ the model is refit from a single start, `x0=p_inf`, the optimum of a model almost identical to λ = 1 (99.7% argmax agreement on synthetic sequences). The fitted λs pile up at 0 (61 rats) and 1 (108), with none at 0.2 or 0.3. That points to an optimiser bias. The percentile split then becomes tied groups of 169 rats, against the paper's N = 116 (legend) or 180 (text).
4. [affects a conclusion] `tau_shuffle_test`, fig2gh, wait-time part. The wait coefficients include the current-reward term, so 10 × mean is about 2.1 at lag 1. The amplitude bound of 1 cannot reach that. On synthetic means, the shuffle-style fit returns a = 1, tau = 2.4 and the observed-style fit a = 1, tau = 0.61, both bound-limited. When the observed groups are fit the same way as the shuffles, wait p = 0.000. So "no difference in wait coefficients" rests on inconsistent fits. The docstring says this comes from the paper's code.
5. [affects a conclusion] fig5c (cell 51). The dandiset omits cue sessions that the inclusion criteria removed. The paper kept those sessions for this analysis (Methods, Pre-initiation cue task), so its selection cannot be rebuilt; the selection that follows it fails (10 rats, p = 0.47). Of the 14 significant rats, 4 go the opposite way (E005, G069, M043, M044).
6. [does not affect a conclusion] `retrospective_kappa`: `k0` is the mean of natural logs (3.0), while R is in log2 (mean 4.32). For female rats, R comes from 4 to 64 uL. This handicaps the retrospective model at each session start, which fits with the 291/291 margin being stronger than the paper's.
7. [does not affect a conclusion] `regress_initiation_on_rewards`: tau is set to 0 when `b[1:-1] == 0`. For initiation times that slice skips the 1-back coefficient, so rats with only a lag-1 effect get tau = 0 (25 rats are at 0). The effect on fig2e is conservative.
8. [does not affect a conclusion] fig2k, Methods selection (cell 39): 265 rats significant but only 227 in the expected direction, so at least 38 are significant the other way. This fits the paper's note that initiation slows after larger rewarded trials. The count criterion ignores direction.
9. [does not affect a conclusion] `training_pairs` (Fig4 notebook): no stage filter, so the first sessions include stage 1 to 8 trials (cell 3), which enter the z-scoring and regressions of pair 1. The plotted population wait ratio reaches 1.849 (cell 7), so outliers survive in the plot.
10. [does not affect a conclusion] Cell 11 checks raw against processed initiation times only after unrewarded trials. The alignment after rewarded trials is never checked.
11. [does not affect a conclusion] fig3c (cell 42): there is an unreported 0.30 cohort (8 rats, 10.21 s) whose mean wait is below the 0.35 cohort's (10.60 s). The decrease is monotonic only with that cohort left out. Cohorts are different rats; the paired 0.15 against 0.25 check (56 of 59 rats) helps.
12. [does not affect a conclusion] zenodo-link: the 10 reordered rats come from start times in the files (several sessions dated 2020-06-22) that disagree with the order of the structs. Every analysis orders sessions by those start times.
13. [does not affect a conclusion] Cell 32 prints mean coefficients only after zeroing, and the fig2cd criterion on falling magnitudes is judged on those zeroed values.

**C. What I could not check**

- Whether problems 4, 6 and 7 copy the MATLAB code. I did not read the code repository. Outputs that would settle them: the unzeroed coefficient means; the fig3j ΔBIC with `k0` in log2 units; the wait-time tau fits with the amplitude bound removed.
- fig3l: the per-rat negative log-likelihood across λ, and a refit with multiple starts at each λ, would show whether the clustering at 0 and 1 is real.
- fig4de: an overshoot computed from `A_Structs_all` (maximum z-scored initiation time after a high-to-mixed switch minus the value at trial 20, first against last 10 sessions).
- fig4a: per-pair ratios using only stage-9 trials.
- fig2k and fig5c: the direction of the effect among the significant rats only.
- Post-rewarded initiation-time alignment: the raw-event check of cell 11, rerun on trials that follow rewarded trials.
- The Fig. 2b direction I took from the paper's text; I did not check the figure itself.

The paper text is saved under `paper/` (`PMC10663503_bioc.json`, `mah2023_fulltext.txt`).
