**A. Outcomes** (29 claims, from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| conditions-per-session | reproduced | Cell 17: the mean is 17.46 under reading (a) and 16.23 under (b). Both lie in 14.4–18.7, and the maximum is 20, within the paper's "up to 24". |
| figs1b-conditions-per-command | reproduced | Cell 19: the pooled mean is 7.06 and the mean of session means 6.98, both in 6.3–7.7. The median is 7, within 4.5–11. |
| figs1d-command-subtrajectories-differ | reproduced | Cell 21: G 1.953 and J 2.330 are within tolerance. Session tests give p<0.001 in 9/9 and 4/4, and both pooled p<0.001. |
| figs1e-next-commands-differ | partially_reproduced | Cell 21: all tests hold (9/9 and 4/4 at p<0.01, pooled p<0.001). J 2.218 is within tolerance, but G 1.873 is above the 1.508–1.844 range. |
| fig3d-population-distance | reproduced | Cell 23: under all four reading combinations, G is about 1.237 and J about 1.77, both within tolerance. Session means run from 1.10 to 1.98, inside 0.99–3.3, and every session and pooled p is below 0.001. |
| fig3b-single-neuron-distance | reproduced | Cell 24: G 1.166 Hz and J 1.222 Hz, with all tests p<0.001. The shuffle means (1.002 and 0.752) match the code's printed 1.004 and 0.745. |
| fig3e-fractions-significant | partially_reproduced | Cell 25: at best 4 of the 6 values are within tolerance. G tuples is 0.373 against 0.27–0.33 under every reading. J neurons is 0.89–0.90 (outside) except under the subsample null with significant tuples (0.878), but that combination puts G neurons at 0.471 (outside). Every fraction is well above the 0.05 chance level. |
| fig4c-dynamics-predict-activity-given-command | reproduced (on the notebook's own reading) | Cell 29, "analysed" pairs: R² is 0.1705/0.2574 (full), 0.1674/0.2497 (command left out) and 0.1680/0.2471 (condition left out), all within tolerance. All tests are 9/9 and 4/4, and pooled p=0. On all pairs, the full model's R² is 0.194/0.291, outside tolerance, which would make this partially_reproduced. (Problem 1) |
| fig4de-condition-specific-activity-predicted | reproduced | Cell 35, reading "all": single-neuron error 1.241/1.198 Hz and population error 0.892/0.833, all within tolerance, and every p=0. The shuffle 5th percentile (1.356 for G) matches Table S1's 1.359. |
| fig4f-condition-specific-component | partially_reproduced | Cell 36: the means are within tolerance under both readings (G 0.215 and J 0.303 on all tuples; 0.243 and 0.333 on significant ones), and all tests hold. But G5–G8 and J3 fall below 0.18 under both readings, so not every session is in 0.18–0.44. |
| fig4g-majority-predicted | reproduced | Cell 37: the mean session fractions for tuples, commands and neurons are 0.89/0.98/0.75 (G) and 0.91/0.96/0.91 (J), all above 0.5. |
| figs3-low-dimensional-decaying-dynamics | not_reproduced | Cell 39: the full model's dimensionality reaches 5 in G4 and the decoder-null model's falls to 1 in J3. The G mean frequencies (0.083 and 0.068 Hz) are outside 0.09–0.11 and 0.054–0.066. J0's full model has a complex long-timescale eigenvalue (0.024 Hz). |
| fig5c-next-activity | partially_reproduced | Cell 32, "analysed": all 8 R² values are within tolerance. The decoder-null model beats the shuffle in only 7 of 9 G sessions (G1 p=0.85, G5 p=0.77) under both readings. The criterion has no partial clause for a failed test; I judged partial because 3 of 4 models pass fully and the decoder-null model passes pooled. |
| fig5d-four-dimensions | reproduced | Cell 41, reading (a): the median is 4 for G and 3 for J, both in 3–5. Under reading (b), G is 6. |
| fig5e-next-command | partially_reproduced | Cell 33, "analysed": all tests hold (J3 command left out p=0.027 still leaves 3 of 4; decoder-null never beats the shuffle). All G values are within tolerance, but J full (0.254), command left out (0.237) and condition left out (0.233) are outside. |
| fig5f-condition-specific-next-command | reproduced | Cell 43: errors are G 3.973 and J 7.052, within tolerance. All p=0, and the mean fractions of significant tuples (0.805 and 0.617) are above 0.5. |
| fig5h-turn-predicted | partially_reproduced | Cell 44: all four values are within tolerance and the pooled tests p=0. The sign test reaches p<0.001 in only 7 of 9 G sessions (G6 p=0.005, G7 p=0.001), short of the 8 the criterion needs. |
| figs5b-dynamics-beyond-behavior | reproduced | Cell 46: paired t-tests give G T=-8.85, p=2.1e-5 and J T=-5.63, p=0.011, with dynamics higher in every session. |
| figs5f-nonlinear-no-better | blocked (too_large, contested) | Not run. The data are present (see C), and at least the J sessions and the code's own G subset look testable. |
| figs3f-residual-early-late | reproduced | Cell 48: the late-minus-early slope is -0.075 (p=4e-133) for G and -0.026 (p=3.7e-6) for J. |
| figs4b-generalize-command-sets | reproduced (on the "analysed" reading) | Cell 30: angle left out 0.162/0.232 and magnitude left out 0.164/0.245, all within tolerance. Session tests are 9/9 and 3/4 (angle) and 9/9 and 4/4 (magnitude), and pooled p=0. |
| figs4g-generalize-condition-classes | partially_reproduced | Cell 31: all 7 R² values are within tolerance (analysed). The diagonal-1 class in J beats the shuffle in only 2 of 4 sessions (J1 p=1, J3 p≈1); the criterion needs 3 of 4. |
| figs6cd-pairwise-distances-predicted | reproduced | Cell 50: pooled r is 0.594/0.680 (neurons) and 0.646/0.789 (population), all within tolerance. Every session and pooled p is far below 0.001 with positive slope. Caveat: Problem 4. |
| figs6g-distance-tracks-behavior | reproduced | Cell 51: the mixed-model slope is positive with p≈0 for true and predicted distances in both monkeys. |
| figs6k-next-command-pairs | reproduced | Cell 52: pooled r is 0.774 (G) and 0.654 (J), within tolerance. Sessions are significant in 9 of 9 G at p<0.05 (8 at p<0.001) and 4 of 4 J. |
| fig6c-dynamics-reduce-input | reproduced | `ofc_simulations` cell 8: mixed-model p is 1.9e-29 (G) and 1.9e-50 (J), with full-dynamics input lower. Wilcoxon p<0.05 in 9 of 9 and 4 of 4 sessions. |
| fig6d-decoder-null-dynamics-no-saving | reproduced | `ofc_simulations` cell 8: mixed-model p is 0.998 (G) and 0.988 (J), and no session's Wilcoxon reaches p<0.05. |
| fig6g-ofc-uses-distinct-patterns | partially_reproduced | `ofc_simulations` cell 10: the full-dynamics effect holds and both No Dynamics absences hold. The decoder-null absence fails for J: mixed-model p=0.020 (shuffle null) and 0.021 (subsample null). |
| monkey-j-linear-command | not_reproduced (unsafe) | Cell 54: the fit accounts for 98.92, 98.89, 99.57 and 99.25% of the variance. Two sessions are below 99% and three differ from the paper by more than 0.5 points. But the fit departs from the criterion (Problem 2). |

**B. Problems**

1. [affects a conclusion] `analyses.run_session` `score`, cells 29–33: the "all"/"analysed" choice of which pairs R² is scored on is the notebook's own reading. It is not in the claims file. It decides fig4c and fig5c (on all pairs the full model's R² is out of tolerance) and the session counts in figs4b. On top of that, the "all" rows for the command, angle and magnitude left-out models are invalid comparisons. Those models only predict pairs in magnitude bins 0–3, but they are compared with shuffle R² over all pairs. The spurious failures that result are the command left out in G0, G1, G5 and J3 in cell 29, and the angle-bin J pooled p=1 in cell 30.
2. [affects a conclusion] `bmi.fit_decoder` (Monkey J), cells 6 and 54: the fit departs from the claim's criterion in three ways:
   - It is fit on every 5 ms frame of the session, including frames between trials; the criterion says rewarded trials only.
   - It includes the state offset, which acts as an intercept; the criterion says no intercept.
   - The "update" it explains is defined using a fitted transition F, not the PPF's own update.

   Any of these can move the variance accounted for by tenths of a percent, which is the size of the tolerance.
3. [affects a conclusion] figs5f is marked blocked as too large, but it was not attempted even on the 4 J sessions (20–21 units, 5–9k bins) or on the code's subset of G sessions without G2 and G4.
4. [does not affect a conclusion] `analyses.pairwise`: the criterion asks for pairwise command matching as in the code; the notebook uses per-condition means without it. The r values are within tolerance anyway. The regression is true-on-predicted (slopes above 1), the reverse of the paper's slopes of 0.2–0.45; the criterion only checks the sign.
5. [does not affect a conclusion] Cell 25: the second reading of fig3e, the fraction pooled over all items, was never computed (`pooled_frac` is unused). Recomputing it from the printed per-session fractions and counts gives G tuples ≈ 0.39, still outside tolerance.
6. [does not affect a conclusion] `subtrajectory_distances`: a tuple qualifies on its 15 occurrences before the edge occurrences are removed.
7. [does not affect a conclusion] `_shuffle_with_stats` and `shuffle_models` permute across the whole session before the fold split, so the shuffled training data contain activity from the test-fold bins.
8. [does not affect a conclusion] `behavior_models`: the ridge parameter is chosen and R² reported on the same cross-validation folds. The bias is the same for both models.
9. [does not affect a conclusion] Dynamics are fit on counts while the code appears to use Hz. That shifts the effective ridge grid by a factor of 100. The ridge parameter is cross-validated, so the effect should be small, but it could move a borderline eigenvalue count in figs3.
10. [does not affect a conclusion] figs3f: the slopes (G -0.075, J -0.026) and N (2774 for G) are not on the paper's scale (-0.242; N=4746). Only the sign and p-value are tested.

Helper checks on synthetic inputs all passed:
- `command_bins` puts the angle-bin edges at 22.5°.
- `_perm_within` stays within command bins.
- `condition_on_command` reproduces the command exactly.
- `null_basis` is orthogonal to the decoder.
- `match_pool` keeps the condition's own points.
- `fig3_distances` on random data gives normalized distance ≈ 1.01 and a false-positive rate of about 7%.

**C. What I could not check, and what would settle it**
- Archive: version 0.230605.2024 holds 13 NWB files totalling about 1.05 GB (9 G, 4 J; queried through the API). The data for figs5f are present. An rsLDS run on the J sessions and the code's G subset would test it at least partially.
- The J condition classes (`CLASSES["J"]`), `J_CW_FIXED` and the use of `jeev_obs_positions_from_amy.mat` cannot be checked against the paper's code from here.
- Left-out models: an output showing shuffle R² computed on exactly each left-out model's test pairs, and the full model scored on all pairs, would remove the dependence on the "analysed" reading.
- monkey-j-linear-command: the variance accounted for, restricted to rewarded-trial frames and fit with no intercept, would settle it.
- figs6cd: r with pairwise command matching.
- The J OFC simulations use an estimated 100 ms decoder whose velocity gain differs from the summed 5 ms gains by 14–26% (`ofc_simulations` cell 3). A sensitivity run using the summed 5 ms gain would show whether fig6g's J decoder-null result (p≈0.02) depends on it.
