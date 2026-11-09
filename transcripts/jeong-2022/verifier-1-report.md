**A. Outcomes** (38 claims in the claims file: 31 tested in the notebook, 7 marked blocked)

| Claim | My outcome | Reason |
|---|---|---|
| session-day-link | partially_reproduced | All subjects exist. 117 of the 119 listed days are sessions with the right condition. HJ-FP-M4 Day38, the Exp 5 start day in two scripts, is missing; I confirmed this in the archive listing. 320 of the 331 integer days in the ranges are sessions (96.7%), which is above the 90% bar but not complete (cell 16). |
| methods-session-counts | reproduced | All 7 means are within tolerance (cell 19): 7.00, 12.71, 4.29, 2.43, Exp 5 7.14 or 7.86 under each count, 5.43, 7.00. |
| exp1-excluded-rewards | reproduced | Reading (a) gives 22.59% (tolerance 22.6 ± 2.4) and 5.66% (tolerance 5.7 ± 0.1); reading (b) gives 22.59% and 5.68% (cell 23). |
| fig3e-reward-response-increases | reproduced | t = 4.405, p = 0.0031, r > 0 in 8 of 8 animals (cell 25). Matches the paper. |
| fig3g-response-iri-positive | reproduced | t = 5.948, p = 5.7e-4 (cell 27). |
| figs8k-iri-correlation-stable | reproduced | Slope t = -0.04, p = 0.97, n = 50; the mean r per session is positive in sessions 1 to 7 (cell 29). |
| figs8b-lick-rates-constant | reproduced | All three slopes have p ≥ 0.44, with t of -0.78, -0.20 and -0.58 (cell 31). |
| figs8d-consummatory-lick-uncorrelated | reproduced | t = 0.231, p = 0.82 (cell 33). |
| figs8e-lick-bout-responses | blocked (methods_underspecified) | The paired and consummatory tests hold under all three windows. The non-consummatory response is below 0 at p < 0.05 only under reading (c) (t = -2.559, p = 0.038); under (a) p = 0.14 and under (b) p = 0.80 (cell 35). The readings differ, so the claims header's rule makes this blocked. |
| figs8g-baseline-unchanged | reproduced | Methods rule p = 0.90, code rule p = 0.95 (cell 37). |
| figs8h-baseline-uncorrelated-with-reward-change | reproduced | r = -0.10, p = 0.81 (Methods rule); r = -0.09, p = 0.83 (code rule) (cell 39). |
| figs8l-lick-rate-tracks-iri | reproduced | Under both regressors the non-consummatory slope is negative (p = 0.015 and 0.019) and the consummatory slope has p ≥ 0.2 (cell 41). |
| fig4ef-dopamine-leads-behavior | reproduced | Under both lick measures, lick abruptness is greater than dopamine abruptness (t = 5.06 and 9.09) and the dopamine change trial comes first (t = 3.32 and 2.93, p < 0.05) (cell 45). The code variant matches the paper's \|t\|, which confirms the paper's sign for the change trial is dopamine minus lick. |
| figs10c-cue-response-at-acquisition | reproduced | Reading (a) gives 0.934 and 0.934 (cell 47), both within tolerance. |
| fig4hi-delay-change-behavior-changes | reproduced | Abruptness t = 15.3, p = 4.9e-6 (the paper has 22.9). Lick ΔAIC t = 7.49, p = 2.9e-4 (k = 4), with k = 3 also passing (cell 49). |
| fig4hi-delay-change-dopamine-unchanged | reproduced | Mean ΔAIC = -18.6, t = -0.73, p = 0.49 (k = 4); t = -0.65 with k = 3 (cell 51). |
| figs10b-no-omission-response | reproduced | The Exp 3 value is ≥ 0 in 7 of 7 animals. The extinction value is below 0 in 6 of 7 and on average. The paired t is 3.03 (p = 0.023, Methods) or 3.42 (p = 0.014, code) (cell 53). |
| fig4kl-extinction-abrupt-behavior | reproduced | Lick abruptness is greater than dopamine abruptness: t = 3.28, p = 0.017 (Methods) and t = 9.73, p = 6.8e-5 (code) (cell 55). |
| fig4jl-extinction-cue-response-positive | reproduced | Reading (a): t = 4.31, p = 0.005. Reading (b): t = 4.16, p = 0.006. Reading (c): 7 of 7 animals (cell 57). |
| fig4p-background-faster-decay | not_reproduced | Background is not below extinction at p < 0.05 under any reading: p = 0.053 for (a) and (c), p = 0.097 for (b); the paper has t = -3.51, p = 0.0126. The "remains positive" part holds (p = 0.015) (cell 59). |
| fig5d-intermediate-cue-positive | reproduced | t = 6.66, p = 5.6e-4, mean ratio 0.435 (below 1) (cell 65). |
| fig5d-intermediate-reward-larger | reproduced | Mean ratio 1.85, t = 2.96 against 1, p = 0.025 (cell 67). |
| figs11de-intermediate-cue-local-baseline | reproduced | All four readings give t > 0 at p ≤ 0.002 (cell 69). |
| fig6b-no-backpropagation | reproduced | p = 0.83 (Methods) and p = 0.876 (code) (cell 61). |
| fig6d-cues-increase-together | reproduced | p ≥ 0.975 under all three baselines (cell 73). |
| fig6d-cs2-below-cs1-late | reproduced | Ratio 0.55 to 0.57, t about -8 to -9 against 1, p ≤ 2e-4 (cell 75). |
| fig6g-inhibition-magnitude | reproduced | Both tests show DAT-Cre lower at p < 0.01 under every baseline. Reading (b) puts the mean inside -0.6 ± 0.06: -0.565 with the CS1 baseline, -0.632 with all code-15 events (cell 77). |
| fig6i-learning-despite-inhibition | reproduced | All four slopes are positive with p ≤ 0.008. In all 6 DAT-Cre animals the last-session CS1 response and licks are above 0 (cell 79). |
| fig6i-lower-cs1-asymptote | not_reproduced | t = 1.70, p = 0.117; the paper has t = 2.80, p = 0.017 (cell 81). |
| fig6i-last-session-licking-similar | reproduced | t = 1.17, p = 0.27 (cell 83). |
| figs12f-pre-cs2-licking | reproduced | Session effect F = 7.39, p = 0.020, with more licks in the last session. Genotype p = 0.47 and interaction p = 0.99 (cell 85). The code variant gives the same outcome. |
| fig2, fig3cf, fig5b, fig6h, figs6, figs5, figs13 (7 simulation claims) | blocked (other) | No recorded data is needed. Nothing was computed because the Matlab code was not run. |

Totals: 27 reproduced, 1 partially reproduced, 2 not reproduced, 8 blocked (1 methods_underspecified, 7 other).

**B. Problems**

1. [does not affect a conclusion] `jeong.auc_aligned`, used for all Exp 2 to 6 smoothed measures, sums with `nansum`. On synthetic input it gives a trial outside dF/F coverage an AUC of 0, not NaN, and a trial at the coverage edge a partial sum: 270 where the full value is about 1000. So cell 8's statement that such trials "get no dopamine value and are dropped" is wrong. Cell 43's "without a dopamine value: 0" reflects this zero-fill. Sessions affected include HJ-FP-M7 Day43-extinction (175 s with no dF/F; this session is used in figs10b, fig4kl, fig4jl and fig4p), HJ-FP-M6 Day48, HJ-FP-F2 Day13, Day17 and Day25, HJ-FP-M2 Day33 and HJ-FP-M7 Day7. Only a few CS+ trials per session are involved, so the outcomes should not change, but this was not quantified.
2. [does not affect a conclusion] Cell 49, `fit_weibull` and the dopamine bounds. The ÷100 dF/F scale is an assumption, and the bounds bind under it: HJ-FP-M3's ΔAIC of -168 means the bounded changing model fits worse than an unbounded constant, which can only happen when the bounds bind. The outcome holds without M3: t = 0.99, p = 0.37 over the other 6 animals (I recomputed this from the printed values). Under the k = 3 variant it also holds.
3. [does not affect a conclusion] Cell 86 gives the simulation claims the reason "not_runnable", which is not one of the protocol's reasons; it should be "other". The block comes from the environment, not the data. A port of `calculateANCCR.m`, or GNU Octave, could have tested them.
4. [does not affect a conclusion] Cell 59: for fig4p, readings (a) and (c) are affine transforms of each other (nc[140] = 1 + 1.8·c), so the two give identical t (-2.403). Only two independent readings were actually tested.
5. [does not affect a conclusion] Cell 57: reading (b) of fig4jl takes the change trial from the code's lick measure only. The Methods measure was not run, but every reading is strongly positive, so it would not change the result.
6. [does not affect a conclusion] Cell 77 scales the 0.5 s baseline to 1 s for the 1 s reward window. The notebook states this as its own choice; it is reasonable given the claims header's equal-window rule.
7. [does not affect a conclusion] Cell 19, which may be a misprint in the paper: the observed SDs for Experiment 7 look swapped relative to the Methods. Wild type is 0.79 here against 2.4 in the paper, and DAT-Cre is 2.45 against 0.7. The means are within tolerance, and the criterion tests only means.
8. [does not affect a conclusion] Several of the notebook's abruptness t values differ a lot from the paper's while the change-trial and ΔAIC t values match it to 3 digits: fig4hi gives 15.3 against 22.9, and fig4kl's code variant gives 9.7 against 5.67. This points to an unidentified difference in how abruptness is computed for conditions 2 and 3. The direction and significance are unaffected.

The claims file: I found no misreading of the paper. The 0.1 tolerance on the no-lick percentage comes from the paper; the spread over animals in the data is 1.04.

**C. What I could not check**

- Whether the day lists, bounds and windows in `jeong.py` were copied correctly from the ANCCR repository at cff4414. The repository is not among my materials. The notebook should print the source lines, or give a diff against the fetched scripts.
- That `cue_acquisition.m` and `backpropagation_pavlovian.m` use the same day lists as `cumsum_pavlovian.m` column 0, which is asserted in a comment only.
- How many CS+ trials per session were zero-filled by problem 1. An output counting trials whose window has any NaN dF/F, per claim, would settle it.
- The dF/F scale the Matlab code used, which matters only for the bounded fits. Running the dopamine ΔAIC with unbounded fits, or at ×100 and ÷100 scales, would show whether the outcome is robust.
- Whether fig4p and fig6i-lower fail because of a session or normalisation choice. Per-animal outputs under alternatives would help: normalising by the random-reward-session reward, and dropping HJ-FP-WT-stGtACR-M3's 25-trial last session.
