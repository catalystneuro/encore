**Verification report, round 1: Mah et al. 2023 on DANDI:001169 (0.260825.1909)**

The claims file has 33 claims (32 from the paper plus the link claim). The notebook tests 25 and blocks 8.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| cohort-size | reproduced | Cell 13 finds 291 rats, a median of 33,493 trials and 71 sessions, all exact. |
| fig1e-wait-time-increases-with-reward | reproduced | Cell 15: the mixed-block means are 10.45, 10.77, 11.11, 13.03 and 13.81 s, rising at every step. |
| fig1f-wait-time-block-effect | reproduced | Cell 17: the mean ratio is 0.894 (0.90 ± 0.025 expected). The signed-rank p is 4.6e-47 z-scored and 8.2e-47 raw. 244 rats have per-rat p < 0.05. |
| fig1i-initiation-block-effect | reproduced | Cell 19: the mean ratio is 0.56. p is 1.82e-49 z-scored and 1.84e-49 raw (paper 1.82e-49). |
| suppfig2-initiation-block-effect-after-unrewarded | reproduced | Cell 21: after unrewarded trials p is 1.8e-49 two-tailed and 9.0e-50 one-tailed, faster in high blocks for 291 of 291 rats. After rewarded trials the one-tailed p is 1. The two-tailed p (3.9e-9) points the opposite way (high slower), which the criterion allows. The paper's p = 1 fits the code's one-tailed test. |
| suppfig3-wait-time-not-affected-by-previous-outcome | reproduced | Cell 23: the ratios are 0.899 after rewarded and 0.897 after unrewarded trials, both below 1. The difference test gives p = 0.64. |
| fig2a-wait-time-converges-in-mixed-blocks | reproduced | Cell 25: the relative gap is 0.33 (1..20) and 0.08 (10..20) for wait times, against 2.0 to 2.4 for initiation times under both detrend readings. Part (2) gives p = 1.8e-49 with 291 of 291 rats higher after high blocks, on concatenated and within-session readings. |
| suppfig5-mixed-to-adaptation-transitions | reproduced | Cell 27: the pre-transition initiation gap is +0.062 (pooled) and +0.049 (per session). The relative gap is 0.134 for wait times against 0.244 and 0.204 for initiation times. |
| fig2c-d-regression-on-previous-rewards | reproduced | Cell 29: the current-offer wait time coefficient is 0.211, CI [0.204, 0.218], larger than any previous coefficient. Initiation lags 1 to 3 are negative and shrink, under 9 and 10 lags, zeroed and raw. |
| fig2e-tau-differ | reproduced | Cell 31: p = 1.7e-45 (Methods) and 2.3e-44 (code). Mean tau is 2.06 for initiation times against 0.07 for wait times. |
| fig2f-tau-uncorrelated | reproduced | Cell 33: r = −0.032, p = 0.59 (Methods) and r = +0.023, p = 0.69 (code). Both p ≥ 0.05; the first is close to the legend's r = −0.03. |
| fig2g-h-fast-slow-tau-groups | reproduced, with a caveat | Cell 35: initiation p = 0.000 and wait time p = 0.151 or 0.214, with N = 116. The wait-time part is an absence claim resting on a test whose null is fitted under a different D bound than the observed fit (problem 3). |
| fig2j-wait-time-not-sensitive-to-previous-offer | reproduced | Cell 37: 38 of 291 rats have p < 0.05 (38 ± 4 expected). The population rank-sum gives p = 0.71. |
| fig2k-initiation-sensitive-to-previous-offer | reproduced | Cell 39: the code reading gives 255 rats, all slower after smaller offers, p = 9e-97 (rank-sum) and 1.8e-49 (signed-rank). The Methods reading gives 265 rats, p ≤ 1e-24. Under that reading only 202 of the 265 are in the claimed direction (see problem 7). |
| fig2l-sensitivity-greater-for-initiation | reproduced | Cell 41: p = 6.09e-38 (code; paper 6.21e-38) and 2.2e-8 (Methods). Initiation time sensitivity exceeds wait time sensitivity under both. |
| suppfig6-results-without-detrending | reproduced | Cell 43: without detrending the post-high mean is +0.147 and the post-low mean −0.109, with 291 of 291 rats ordered. Part (2) is computed without detrending. |
| fig3c-wait-time-by-catch-probability | reproduced | Cell 45: cohorts are 3, 188, 61, 151 and 40 rats, all within tolerance. Wait times fall from 0.15 to 0.2 to 0.25 at 5 of 5 offers. |
| fig3i-retrospective-model-captures-initiation | partially_reproduced | Cell 47: the Equation 10 model shows both an overshoot and a gap, and in cell 48 the model is higher after smaller offers in 290 of 291 rats. The alternatives do not lack one feature at every alpha_0: vanilla at 0.8 and RPE at 0.4 and 0.8 show both. Even without noise, RPE at 0.4 shows both (+0.074 and +0.025). |
| bayes-observer-offer-reduces-uncertainty | reproduced | Cell 50: the posterior is less uncertain in 291 of 291 rats under both variance readings and both transition matrices, with p = 1.8e-49 across rats. The test over trials is run for J004 only (p ≤ 5e-257). |
| suppfig12-no-sex-differences | reproduced | Cell 52: 184 males and 107 females. p = 0.238 (wait time ratio) and 0.557 (initiation ratio); the paper gives 0.23 and 0.59. |
| suppfig14-contextual-effects-without-threshold | reproduced | Cell 54: unthresholded, p = 1.0e-43, and the unthresholded mean is longer in all 11 offer-block cells. |
| fig3j-inferential-beats-retrospective-for-wait-times | blocked (too_large, overstated; also methods_underspecified) | Cell 64 estimates 162 h. That figure rests on a pure-Python per-trial loop and an assumed 200 evaluations per start (problem 5). The fitting code, free parameters and folds are not in the paper's repository. |
| suppfig8-belief-state-not-distinguished | blocked (too_large / methods_underspecified) | Needs the fits of fig3j. |
| fig3f-inferential-model-not-sensitive-to-previous-offer | blocked, but partly testable | It needs only the inferential fit on all data. By cell 64's own timing that is about 0.4 h, within the 1 h limit. |
| suppfig9-wait-times-reflect-misinferences | blocked (too_large / methods_underspecified) | Needs cross-validated inferential fits, about 2.3 h by cell 64's own timing; the folds are unspecified. |
| fig3l-lambda-groups-wait-time-dynamics | blocked (too_large / methods_underspecified) | Needs a fit of the sub-optimal model. For that model the belief depends on lambda, so cell 64 understates its cost. |
| fig4a-wait-time-block-sensitivity-emerges | blocked (data_missing) | Confirmed on the archive: the dandiset's `relatedResource` says it IsDerivedFrom Zenodo 10031483, the A structs, which hold only included sessions. Cell 8 finds a positive slope in 87% of sessions. A partial run on the included sessions was possible but not attempted. |
| fig4c-initiation-previous-reward-stable | blocked (data_missing) | Same as fig4a. |
| fig4d-overshoot-grows-with-training | blocked (data_missing) | Same as fig4a. Comparing the first and last 10 included sessions was possible as a stated deviation. |
| fig5b-pre-cue-initiation-sensitive-to-offer | reproduced | Cell 58: the pre-cue means fall at every step under both readings. 14 of 16 rats (date) and 11 of 11 (after 30 sessions) reach ANOVA p < 0.05, against 0 of 12 on the original task. |
| fig5c-pre-cue-initiation-still-sensitive-to-previous-reward | partially_reproduced | Cell 60, code reading by date: 13 of 16 rats, p = 1.9e-6, which passes. Methods reading (20 uL trials, as the Fig. 5c legend says): 14 of 16 rats but rank-sum p = 0.068 by date and 0.47 after 30 sessions, which fails. The after-30-session reading has only 11 rats, so the count cannot reach 13 ± 1. |
| fig5d-pre-cue-initiation-depends-on-previous-block | reproduced | Cell 62: higher after high blocks in every rat under all 4 readings, p = 3e-5 (date) and 1e-3 (after 30 sessions). |
| pre-cue-session-link | partially_reproduced | Cell 56 links 14 of 16 rats; S042 (p = 0.15) and S050 (p = 0.60) are not. The rule was written after a first look at the same check. |

### B. Problems

1. **[affects a conclusion]** fig3i, cell 47. "Overshoot" is the maximum of a noisy, smoothed curve over trials 1..20 minus its value at trial 20. That measure is positive even on a flat noisy curve. On synthetic flat noise with 15-point smoothing it averaged +0.03 and was positive 66% of the time, the same size as the alternatives' "overshoots" (0.02 to 0.08). It also exceeds the Equation 10 model's own value at noise 8 (+0.016). The "both present" test has no threshold, so gaps of +0.004 or +0.012 count as present. As run, the test cannot separate the models; under the criterion as written the alternatives still fail.
2. **[affects a conclusion]** fig5c, cell 60. The Fig. 5c legend analyses 20 uL trials, which is the Methods reading, and under that reading the population test fails. On the pre-cue task the code reading (all mixed-block trials) is confounded: post-violation trials repeat the previous offer (Methods, Pre-initiation cue task), and on this task the current cued offer drives initiation time. The notebook reports both readings but does not mention this confound.
3. **[may affect a conclusion]** fig2g-h, `tau_shuffle_test` with `BW = b_wt`. The wait-time coefficients include the current offer, about 0.21. In the shuffled fits that becomes 2.1 after the ×10 scaling, against a D bound of 1; the observed fits are not scaled. On a synthetic test the same vector gives tau 2.43 under the shuffle bounds and 0.61 under the observed bounds. The null is therefore not on the observed scale, which pushes p towards absence. The Methods reading (previous 9 coefficients only) was not run for the test; the Methods taus were used only to form the groups.
4. **[does not affect a conclusion]** Claims file header, misreading. It says "A further 16 rats ran a pre-initiation cue task", but the paper says "a subset of rats" (Methods; Results). The dandiset's 291 rats include all 16, among them M045 to M048, who trained only on the pre-cue task. The exact match of the trial and session medians suggests the paper's 291 included them too. As a result, the Fig. 1 and Fig. 2 analyses include pre-cue sessions; 16 of 291 rats cannot change those outcomes.
5. **[affects the blocked status]** Cell 64. The 155 h retrospective estimate times the Python loop in `retrospective_kappa` (8.7 ms per evaluation) and assumes 200 evaluations per start; a compiled loop would be orders of magnitude faster. The "inferential" evaluation timed there is an ad hoc formula, not the model. fig3f (inferential fit on all data, about 0.4 h by this cell's own numbers) and an inferential-only part of fig3j were feasible. The more defensible block reason is methods_underspecified.
6. **[does not affect a conclusion]** Blocked Fig. 4 claims. A partial test on the included sessions was possible as a stated deviation and was not run.
7. **[does not affect a conclusion]** fig2k, Methods reading, cell 39. 63 of the 265 significant rats are significant in the opposite direction, and only 202 are significant and slower, which is below 256 − 26. The paper's wording ("significantly modulated") is non-directional, so the criterion passes.
8. **[does not affect a conclusion]** `regress_wt` and `regress_iti` use the raw female volumes (log2 of 4, 8, 16…), citing the code. The claims file's common method says to use male volumes. This is only a shift of log2(0.8), but it does not cancel in `regress_iti`, where unrewarded trials are 0.
9. **[does not affect a conclusion]** Smaller points, none of which can move a conclusion:
   - In `wt_by_previous` and `iti_by_previous`, `prev_vol` crosses session and block boundaries.
   - `wt_dynamics` windows cross sessions, while `lat_dynamics` windows do not.
   - `wt_by_pcatch` uses catch trials without the opt-out filter.
   - The bayes test over trials is run for J004 only, not pooled over rats.
10. **[does not affect a conclusion]** fig5b is not independent of pre-cue-session-link: the link is validated with the same ANOVA that fig5b then reports. The dates do come from Figure5.m, not from the data.

Helper checks on synthetic inputs:
- `fit_exp_decay` recovers tau of 0.7, 2 and 6 accurately.
- `zero_after_first_ns` behaves as specified.
- `transition_codes` gives the right codes and positions.
- `lognormal_noise` gives the right mean and variance.
- `matlab_smooth` shrinks its window at the ends, like MATLAB's `smooth`.

### C. What I could not check

- **Paper's MATLAB code.** Its scripts were not available to me. That leaves unverified the per-script D scalings (×25, ×10, ×15) and initial kappas, the 10-draw averaging for the vanilla model, and whether the retrospective model uses offered or received rewards. It also leaves open whether myTauShuffleTest includes the current wait-time coefficient and whether FigureS4 detrends.
- **Notebook outputs that would have settled points above:**
  - fig2g-h: the shuffle test on the previous-only wait-time coefficients, plus the share of shuffled wait-time fits that hit D = 1.
  - fig3i: overshoot computed with a noise-only control, or on noise-free curves with an unsmoothed endpoint, and the full curves for each alternative.
  - fig5c: the per-rat table under the Methods reading, and the code reading with post-violation trials removed.
  - Blocked model claims: a timing of a vectorised or compiled retrospective evaluation, and an actual inferential-only fit for fig3f.
  - fig4: the first session date in the dandiset against each rat's stage 8 start, to show directly that early sessions are missing.
  - bayes: the test over trials pooled across all rats.
