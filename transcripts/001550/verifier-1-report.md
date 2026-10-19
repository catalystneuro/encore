**A. Outcome per claim** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| session-link | reproduced | Cells 11–12: 0.9999 of the paper's sessions with valid trials are in the dandiset (one missing, P189 TaskSwitch6-210516a). Valid-trial count and fraction correct are equal in all 15,277 matched sessions. In the 20-session sample, the per-trial fields and position in block agree on 100% of trials and the 10 ms pulse bins on 99.996%. Per-rat counts match `numsessions_all_rats` for 23 of 26 rats; the 3 differences are explained by 6 extra dandiset sessions and 1 session where the selection differs. |
| subjects | partially_reproduced | Cells 3 and 14: 26 subjects, all male, all Long Evans. Only 0.913 of selected sessions fall in 5.4–26.4 months (minimum age 3.0, maximum 39.1), which is ≥0.90 but below "every session". |
| trials-per-session | reproduced | Cell 16: valid trials per selected session average 551.8, and per task session 494.2. Both are inside 487.8–596.2. |
| blocks-per-session | reproduced | Cell 16: blocks over all task sessions average 13.90, and switches over selected sessions 15.98. Both are inside 13.14–16.06. |
| session-duration | reproduced | Cell 16: median 2.50 h (selected) and 2.57 h (all), inside 1.8–4.4 h. Only about 56% of sessions last 2–4 h. |
| block-min-30 | reproduced | Cell 19: 100% of non-final blocks have ≥30 trials when all trials are counted (81.7% when only valid trials are counted). |
| fig1c-20-rats | reproduced | Cell 21: exactly 20 rats have more than 120,000 valid trials in selected sessions. |
| fig1c-context-selection | reproduced | Cell 22: in all 20 rats both relative weights are above 0.5; the lowest is 0.724. |
| ed1e-switch-four-trials | reproduced | Cell 24 (main selection): at position 4 the relevant weight reaches 0.91 of plateau for one switch direction and 0.963 for the other, so both pass the 0.9 threshold. The margin is thin: the 0.91 is the switch from frequency to location. Position 1 is 0.50/0.56. |
| ed2g-learning-2-5-months | reproduced | Cell 26: three of the four readings have more than half of rats in 1.8–5.5 months (17, 19 and 17 of 26). Reading (ii)(a) gives exactly 13 of 26, which is not more than half. |
| fig4-converging | reproduced | Cell 30: all 36 slope indices are negative, median −0.432. 35 of 36 lie in −0.8 to −0.15 (P189 location is −0.097). |
| fig4-loc-frq-uncorrelated | reproduced | Cell 33: r = 0.18 (95% CI −0.31 to 0.60), p = 0.475. |
| ed3g-halfsplit | reproduced | Cell 35: r = 0.552 against a tolerance of 0.522–0.638, p = 4.7e-5. The fixed-200 variant gives 0.577. |
| ed4-bilateral-fof-impairs | partially_reproduced | Cell 37: full-trial bilateral epochs lower accuracy significantly in P116 and P131. P124 is higher (+2.5 points, p = 0.17), and P127 shows no significant change. The result is the same under every reading. |
| neural-link | not_reproduced | Cell 40: only 67.8% of cells match one session as a contiguous run, against the 80% needed. Even the gap-tolerant variant (93.5%) finds 110–112 distinct sessions against 199 ± 19.9. |
| units-per-rat | reproduced | Cell 39: per-rat and per-region counts equal the paper's (FOF 2047/832/258/94/54, mPFC 112/98). |
| fig3h-neural-uncorrelated | reproduced | Cell 42: r = −0.18 across 7 rats, p = 0.70. I checked `neural_slopes` line by line against `get_neural_slope.m` and it matches. |
| fig5d-behaviour-neural | reproduced | Cell 45 (main): r = −0.697, inside −0.803 to −0.657, with p = 0.0056 < 0.01. Single features: location −0.675, frequency −0.772. |
| choice-axes-parallel | not_reproduced | Cell 43: mean angle 40.3°, against 1.6°. The port is wrong (problem 1), but the paper's code done correctly gives 4.73° by my run, still outside 1.44–1.76. |
| fig1e-choice-axis | blocked (methods_underspecified) | Not in the dandiset (no ecephys; `variableMeasured` is empty). `Figure1e.m` in the paper's code repository only plots and never computes the 81.3% or 73.3%, so the inputs exist but the definition of the variance fraction does not. |
| fig1f-irrelevant-encoded | blocked (other: qualitative, MATLAB mbtdr pipeline not ported) | The data are not in the dandiset. The inputs (`Arrays_Pagan`, `Figure1f.m`) exist on GitHub, so a port is possible in principle. |
| fig3a-trained-rnn-svm | blocked (other) | RNN results are not in the dandiset and live only in the RNN repository. Correct to block for this dandiset. |
| fig5c-engineered-rnn | blocked (other) | Same as fig3a. |

Chance levels: the paper gives one only for the feature selection index (the dashed line in Extended Data Fig. 2g). No claim's selection depends on it, so there was nothing to compare.

**B. Problems**

1. [affects a conclusion, the reason but not the outcome] `taskswitch.choice_axis_angle` (cell 43) ports only the first angle in `ExtDataFigure5ag.m`. The code then overwrites `ango` with a different angle: the two context PC1s projected onto the first 3 PCs of the stacked, norm-scaled choice kernels of both contexts, folded to ≤90°. That projected angle is the one in the histogram. I recomputed it from `combined_kernels_per_context.mat`: per rat 1.1, 4.5, 1.8, 5.5, 4.2, 8.0 and 7.9°, mean 4.73°. The claims file's statement that "the code takes the angle without folding" is also wrong.
2. [affects a conclusion, possibly] `fit_rat` and cell 45 use the Methods selection for P049 and P059, which leaves only about 23–26k trials each. Their location slopes (+0.13, +1.29) disagree in sign with the code-selection fits (−0.43, −0.61). The main fig5d r (−0.697) lands inside tolerance despite this, and only 0.04 from its upper edge, so the outcome is fragile.
3. [affects a conclusion, possibly] Cell 40 searches only TaskSwitch4, TaskSwitch4new and TaskSwitch6 sessions. P100 has 13 TaskSwitch4repeat sessions (asset listing) that were never searched, and P100 has most of the unmatched cells (835 contiguous, 189 with gaps). The search also requires contiguous runs, while the gap variant shows the paper's cells skip trials. The session count would still be far from 199.
4. [affects a conclusion, possibly] Cell 37 never uses `opto_connected` or `opto_type`, although `load_session` reads both. If epochs were logged on trials with the laser disconnected, the stimulation and control groups would be mixed. The decision rests on P124.
5. [does not affect a conclusion] Cell 11: the relative weights agree with the paper's `bdir`/`bfreq` in only 89.8% of sessions, and the notebook does not explain this. The P059 row (1.1119 here, 1.0 in the paper) suggests the paper clips relative weights to at most 1. That clipping alone causes the one session selected here and not by the paper, and the 213-trial difference for P059.
6. [does not affect a conclusion] `fit_cv` draws its folds at random over trials, not sessions, so correlated trials share folds. This only affects which penalty is chosen. The fixed-200 variant gives the same outcomes everywhere.
7. [does not affect a conclusion] `switch_curves` (cell 24) silently drops rat × position cells with fewer than 30 trials, a threshold the criterion does not state. Relative weights are unbounded when weights are small, so the across-rat mean at k = 1–4 is not robust, which matters given the 0.91 margin.
8. [does not affect a conclusion] Cell 14: 18 rats have selected sessions below 5.4 months and one is at 3.0 months. The `date_of_birth` metadata is never checked for plausibility, for example against the age at the first ProAnti session.
9. [does not affect a conclusion] Cell 19 has an unused variable `nxt`. Trials-per-session readings (c) and (d) leave out the 13 unreadable sessions, a negligible effect.

Checks that passed:
- On synthetic inputs: `bin_pulses` (bin edges, pulse at 1.3 s), `relative_weights` (recovers 0.80/0.75), `slope_index` (ramp gives −0.8), `fit_logistic` with the smooth penalty (agrees with an independent BFGS to 3e-5) and `opto_trials`.
- The half-split order is chronological for every rat: sorting by session name gives date order.

**C. What I could not check, and the output that would settle it**

- Whether the neural sessions sit in other protocols, or whether 199 counts something else. Matching cells against all TaskSwitch* sessions, plus a per-rat table of matched and unmatched cells with their trial counts and dates, would show this.
- Whether laser-disconnected trials contaminate ed4. A crosstab of `opto_connected` and `opto_type` against epoch labels per rat, and the ED4g result with connected trials only, would answer it.
- Which three rats the paper means for ed4. The dandiset has 4 rats with epochs and labels none.
- How robust ed1e is. The per-rat relative weight and n at positions 1–5, and a bootstrap interval for the position-4 fraction of plateau, would show this.
- Whether clipping explains the 10.2% relative-weight mismatch. A list of those sessions with both values would show it.
- Whether the ages are real. Each rat's date of birth and age at its first dandiset session would show it.
- Whether the paper's per-trial fields equal the dandiset beyond the 20-session sample. Only the per-session aggregates were compared outside the sample.
