**Verifier report, round 1: Su et al. 2026 on DANDI:001950 (version 0.260928.2230)**

The claims file has 39 claims. My outcomes: 10 reproduced, 13 partially_reproduced, 5 not_reproduced, 11 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| lc-definition-counts | blocked (data_missing) | Anatomy data. The API lists only 385 session NWB files (84 behavior, 163 behavior+ecephys, 136 behavior+fib, 2 ecephys), in both the pinned version and the draft. |
| fig1-dense-axon-distribution | blocked (data_missing) | Same: no SPIM axon volumes in the archive. |
| axon-length-and-branching | blocked (data_missing) | Same: no single-neuron reconstructions. |
| fig2c-primary-targets | blocked (data_missing) | Same. |
| fig2ef-dorsal-ventral-projections | blocked (data_missing) | Same: no reconstructions or retrograde tracing. |
| fig3a-gene-expression-continuum | blocked (data_missing) | Same: no snRNAseq data. |
| fig3c-pseudospace-dorsal-ventral | blocked (data_missing) | Same: no MERFISH data. |
| fig3d-retroseq-targets | blocked (data_missing) | Same. |
| fig3e-axes-separated | blocked (data_missing) | Same. |
| figs14k-patchseq-by-target | blocked (data_missing) | Same: no slice or patch-seq data. |
| figs12-trials-per-session | reproduced | Reading (b), the sessions of the selected units, gives mean 334.3, min 94, max 558 (cell 49). The minimum and maximum equal the paper's exactly. Readings (a) and (c) fail. |
| iti-mean | partially_reproduced | The mean is 4.43–4.96 s under every reading, all within 4.83 ± 0.483. The range fails under every reading: max 292 s, min 0.22 s (cell 13). |
| fig4c-choice-history | partially_reproduced | McFadden R² is 0.600 and 0.895 of choices are predicted. Rewarded coefficients are positive and decay under R+N. The decay constant tau is 1.2–2.3 trials against 3.95 ± 0.395 under every reading (cell 15). |
| fig5a-engagement-reward-history | reproduced | Lag-1 reward coefficient 1.63, 95% CI 1.43 to 1.84, positive in 40 of 40 mice (cell 17). |
| fig5e-switch-history | reproduced | Lag-1 no-reward coefficient is positive with a CI excluding zero at 5, 10 and 15 lags; at 5 lags 1.54, CI 1.38 to 1.70 (cell 19). |
| fig6c-choice-change-rpe | reproduced | Reading (a), binned: rho = 0.833 with 8 bins, 0.917 with 9. Reading (b), pooled trials: rho = 0.55. As the criterion requires, this is recorded as resting on the binning, and on a refitted model (cells 47, 51). |
| fig4g-go-cue-excitation | reproduced | 251 of 252 neurons, both readings (cell 21). |
| fig4h-tonic-phasic-anticorrelation | reproduced | r = −0.381 (p = 4e−10) for reading (a) and −0.379 for (b) (cell 23). |
| figs15f-tonic-modulation-vs-engagement | not_reproduced | Top panel r = −0.266; bottom r = +0.258 (cell 27). Both are far from −0.59 ± 0.059. |
| fig5b-baseline-predicts-ignore | reproduced | 48.4%, 50.0% and 44.8% of all 252 neurons are within 46.5 ± 4.65. Rates are higher before ignored cues: paired t = 7.38, p = 2.8e−12 (cell 25). |
| fig5c-ignore-ventral | not_reproduced | Linear R² 0.029–0.030, p 0.34–0.36 under all three regressor sets. kNN R² 0.012 (cell 29). |
| fig5d-ignore-on-anatomy-axes | not_reproduced | r = 0.157–0.170, p 0.068–0.093 on both axes (cell 31). |
| fig5g-switch-dorsal | not_reproduced | Linear p 0.09–0.64 and R² 0.013–0.051 under all four readings (cell 33). |
| fig5h-switch-on-anatomy-axes | partially_reproduced | One of four readings (previous trial, code regressors) gives positive, significant r: 0.211 (p = 0.017) and 0.203 (p = 0.022). Neither is within 0.32 ± 0.032 or 0.30 ± 0.03. The other three readings give r between −0.06 and 0.14, none significant (cell 35). |
| fig5k-cortical-input-switch | partially_reproduced | Photometry: 54–55 of 63 sessions positive against about 155 of 252 neurons, Fisher p 1.4–2.5e−4 (cell 37). The cortex-projecting part is untested because the pinned version has no label; see Section C. |
| figs17i-baseline-axons-vs-spiking | partially_reproduced | Axons against neurons: p 0.019–0.040, which is below 0.05 but far weaker than the paper's 4.2e−4 (cell 39). The cortex-projecting part is untested. |
| fig6-outcome-responsive-fraction | reproduced | Reading (a): 76.2% of 252 neurons (cell 53). |
| fig6a-outcome-space | partially_reproduced | The distribution is nonuniform: linear p = 0.0014, kNN p = 0.001. The gradient is anterior (AP −0.98) but slightly ventral (DV −0.15), not dorsal as claimed (cell 55). |
| figs18d-outcome-not-on-anatomy-axes | reproduced | Every axis has \|r\| ≤ 0.103 and p ≥ 0.25 (cell 57). |
| fig6f-outcome-angles-nonuniform | partially_reproduced | Rayleigh p = 2.8e−13, and the expected modes are present (87 neurons in −45° to 0°, 68 at ±135° to 180°). z = 28.13 is outside 19.53 ± 1.95, and would be about 26.9 even at n = 241 (cell 59). |
| fig6f-cortex-projecting-rpe-biased | blocked (metadata_insufficient) | The pinned version has no antidromic label. The draft adds `antidromic_tier_1` (45 units, 9 of the 252 selected; cell 8), so this is testable only from the unpublished draft, with a very small group. |
| fig6g-rpe-vs-no-reward-populations | reproduced | Reward-excited rate rises monotonically across RPE quartiles (−0.25 to 0.27). No-reward-excited neurons: ANOVA p = 0.41, Friedman p = 0.37 (cell 61). |
| fig6h-opposing-behavior | not_reproduced | Both group mean slopes are positive: 0.0125 for reward-excited and 0.0022 (p = 0.12) for no-reward-excited. The two-sample p = 1.7e−8 shows a difference, not opposite signs (cell 63). |
| fig6i-axons-rpe | reproduced | RPE signs and Watson-Wheeler p < 0.05 hold under all eight readings: per session p = 0.0002, per mouse p 0.004–0.019 (cell 65). W is on a different scale from the paper's 0.1 and is not in the criterion. |
| fig6j-cortical-input-more-positive | reproduced | Reading (a): 53–55 of 63 photometry sessions positive against 149 of 252 neurons, Fisher p 1.4e−5 to 2e−4 (cell 67). Reading (b) is untestable at the pinned version. |
| figs14-waveform-space | partially_reproduced | Slope symmetry: linear p = 0.013, but kNN p = 0.40. \|symmetry\| against DV gives r = +0.09 (n.s.), so "more symmetric dorsally" is not shown. Post-trough width does increase dorsally (r = 0.19, p = 0.005) (cell 41). |
| figs15q-spontaneous-vs-task-licks | partially_reproduced | r is positive with p < 0.001, but 0.612 or 0.803, depending on the author's minimum-bout threshold, is outside 0.49 ± 0.049 (cell 45). |
| figs15t-crosscorrelogram-outcome-axis | not_reproduced | The outcome axis is significant (p = 0.001 and 0.003). The absences fail: switch axis p = 0.001 under reading (a), respond-versus-ignore p = 0.041 under reading (b) (cell 69). |
| figs16-pupil-spiking | partially_reproduced | Mean tau 3.28 s is within 3.37 ± 1.03. The spike–pupil correlations go the opposite way: 34 neurons significantly negative against 4 positive, from 4 mice (cell 43). |

### B. Problems

1. **[affects a conclusion] Population (cells 7, 47).** The selection has 252 units, 21 mice and 112 sessions, against the paper's 241, 19 and 106.
   - The model-based session criteria `aN` and `bias` were computed (207 units, 19 mice would pass) but never applied.
   - No result was rerun on that subset or on the draft's `opto_NE_paper` population as a sensitivity check.
   - This matters for the borderline spatial claims: fig5c, fig5d, fig5g, fig5h and figs15f.
2. **[affects a conclusion] Drift regressor (cells 25, 33, 53).** The per-trial waveform amplitude is absent from the dataset.
   - The "methods" readings therefore have no drift regressor at all.
   - The trial-index stand-in is used only for fig5b and fig5c, not for fig5g or the outcome regressions.
3. **[affects a conclusion] Q-learning model (cell 47, `fit_q_session`).** The notebook fits it by maximum likelihood per session, not with the paper's hierarchical fit.
   - In my synthetic test (500 trials, true aN 0.3, aP 0.6) it recovered aN 0.56 and aP 0.94, so parameters are poorly identified.
   - 107 of 382 sessions sit at the aF = 0 bound.
   - Every RPE and chosen-value result rests on this: fig6c, fig6a, fig6f (z), fig6g, fig6h, fig6i.
4. **[affects a conclusion] ITI range (cell 13, iti-mean).** The trial table's `ITI_duration` column is loaded (`TRIAL_COLUMNS`) but never used.
   - The paper's range of 1.1–20 s describes the generated draws, which have a 20 s maximum.
   - The measured intervals include pauses up to 292 s and a 0.22 s minimum in behavior-only sessions, so the range test fails for reasons the designed values might not share.
5. **[affects a conclusion] figs15t (cell 69).** Several choices here are the author's own and unstated:
   - Each feature's "axis" is this notebook's own linear gradient.
   - The switch axis comes from one of four t variants (prev_responded, methods), whose own spatial test is not significant (p = 0.44), so its direction is noise.
   - Only one respond-versus-ignore variant is used.
   - The kNN runs on a one-dimensional projected pair position, and pairs from the same session are treated as independent.
   - The switch-axis significance that fails the absence could change under the other variants.
6. **[affects a conclusion] figs15q (cell 45).** Several choices are the author's own, with no source given:
   - the definition of spontaneous bouts (no cue within −1 to +5 s);
   - the minimum bout counts of 5 and 20;
   - the ±0.5 s, 50 ms PSTH window.
   r moves from 0.61 to 0.80 with the bout threshold alone.
7. **[affects a conclusion] figs14 (cell 41).** The Methods specify a 50–8000 Hz filter before waveform extraction; the notebook uses the stored raw mean waveforms unfiltered. "More symmetric" is operationalised two ways with conflicting signs. The waveform amplitude units (the `>50` gate in `wf_features`) are never checked.
8. **[does not affect a conclusion] Pupil autocorrelogram (cell 43).** No confidence filter, low-pass filter or exclusion of bad periods is applied, and the 30 s maximum lag is the author's choice. The spike–pupil result comes from 4 tetrode mice only and is not detrended. The Methods do not require detrending for this analysis, but the strong negative majority was not investigated.
9. **[does not affect a conclusion] fig6g (cell 61).** The one-way ANOVA treats repeated within-neuron quartiles as independent groups. The Friedman variant agrees.
10. **[does not affect a conclusion] fig6f (cell 59).** Rayleigh z scales with n (252 against 241); it stays out of tolerance after rescaling.
11. **[does not affect a conclusion] kNN permutations (`knn_spatial_test`).** 1,000 permutations set a p floor of 0.001, so p values like the paper's 5e−4 cannot be reached. No pass/fail at 0.05 changes.
12. **[does not affect a conclusion] fig5a (cell 17).** `rewarded` is 0 on ignored trials, so the lag-1 reward coefficient partly measures whether the previous cue was responded to. This is as the Methods specify.
13. **[does not affect a conclusion] Helper checks.** On synthetic inputs, `rayleigh` matches the large-sample p, `watson_wheeler` and `linear_spatial_test` are calibrated under the null (5% nominal: 1% and 2% rejections), and `go_trials` switch coding, `rate_in_windows` and `auroc` behave correctly.
14. **Possible misreadings in the claims file (reported, not corrected):**
    - iti-mean: the Methods define ITIs as "the times between consecutive cue onsets"; the criterion uses end of trial to next cue.
    - fig4c: the legend's "exponential fit (coefficient of 3.95)" is read as the decay constant in trials. It could be the amplitude, which is 4.28–4.33 for the pooled R+N fits, within tolerance.

### C. What I could not check

- **Paper code.** I could not see the paper's code, so I could not confirm:
  - the port of the waveform features (`wf_features`);
  - the Stan forgetting rule (`Q*aF` against `(1−aF)`);
  - the `auc_windows` lags and the printed axes;
  - the photometry quality metric on `G_PL-L_tri-exp_mc`, z-scored over the whole session.
- **Antidromic stimulation in the pinned files.** The dandiset description says some sessions include antidromic stimulation. Whether the pinned NWB files hold the stimulation event times, from which cortex-projecting neurons could be identified, is unchecked. Printing the `stimulus/` and `intervals/` groups of one such session would settle it.
- **Outputs that, if added to the notebook, would have let me check more:**
  - the distribution of `ITI_duration` (min, max, mean);
  - all 5, 5b to 5h, 15f and 6 results rerun on the 207-unit `aN`/`bias` subset and on the draft's `opto_NE_paper` units;
  - figs15t under all four switch-t and three ignore-t variants;
  - figs15q across bout thresholds, with the code's spontaneous-bout definition;
  - pupil–spike correlations with linear detrending, by mouse;
  - a parameter-recovery check of the per-session Q fit, or the hierarchical fit itself;
  - fig6c and fig6h with the Q variables restricted to sessions passing the model criteria.
