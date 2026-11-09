**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| recording-counts | reproduced | Cell 8: 95.8 (SD 6.7) units and 408.0 (SD 40.8) trials per session, 4080 trials in total. |
| fig1b-online-accuracy | reproduced | Cell 10: 0.8596 over 4016 trials, trial-weighted SD 0.036. The paper's chance level is 17%; the notebook's shuffle null has mean 0.169 (1/6 = 0.167), so the two agree. Session 1 has 64 No-Go trials in the data, not the 84 in the Methods; 4080 − 64 = 4016 matches the paper's own total. |
| fig1b-errors-middle-ring-pinky | reproduced, under one reading | Cell 12: 264/379 = 0.697 when the denominator is errors between two fingers. With all errors it is 0.468, and with errors on finger trials 0.592. The paper does not name the denominator, but only the first reading gives "the majority (70%)". |
| fig1s4a-offline-accuracy | reproduced | Cell 14: diagonal LDA with leave-one-out gives 0.934 (SD 0.016) over 4080 trials. That is within ±0.02 of 0.92. The authors' 8-fold pipeline gives 0.924. |
| fig1s4b-calibration-accuracy | blocked (data_missing) | The archive has 10 assets, all with the session description "individual-finger press, main task". The trial counts (4080) match the main task only. |
| fig1s5-tuned-fraction | reproduced | Cell 16: 0.879 with FDR over all units pooled (0.875 with FDR per session), against 0.89 ± 0.05. No units fell below 0.1 Hz. |
| fig1s6a-gaze-regression | blocked (metadata_insufficient), partly testable | `cue_location` is a 1–12 index with no map to screen coordinates. The authors' repo config (`task/override/cue_location.yaml`) also lists only 1–12. The regression could have been run under row-major and column-major 3×4 layouts. Given 1s6b, it is not safe to assume r² ≈ 0. |
| fig1s6b-gaze-classification | not_reproduced | Cell 18: pooled cue-location accuracy is 0.1154. The shuffle null's 95% range is 0.0755–0.0944 (max 0.0998), and 0 of 500 shuffles reach the observed value. The within-finger null and finger-mean removal give the same picture (0.117), and 5 of 10 sessions have binomial p < 0.05. The finger half of the criterion holds (0.934 against a null of 0.155–0.181). The effect is small (11.5% against 8.3%), but the criterion fails. |
| fig1s6c-control-task | blocked (data_missing) | The control task is not in any of the 10 assets (same evidence as for 1s4b). |
| fig2d-rdm-structure | reproduced | Cell 20: the largest of the middle/ring/pinky distances is 0.482 and the smallest thumb distance is 0.641 (max-scaled). The criterion holds in 9 of 10 individual sessions. |
| fig2f-able-bodied-over-unstructured | reproduced | Cell 22: the WUC difference is 0.0998, bootstrap 95% CI 0.074–0.127, higher in 10 of 10 sessions. Paired p = 5.9e-5 against the paper's 5.7e-5. |
| fig2s5-mc-over-pcip | reproduced | Cell 24: MC minus PC-IP CI is 0.060–0.112. Mean WUC with MC is 0.969, against a lower noise ceiling of 0.984 (margin −0.015, within the criterion's −0.05). The MC WUC reaches the lower ceiling in only 1 of 10 sessions. The p-value is 7.9e-5 against the paper's 1.9e-6. |
| fig2-typical-among-individuals | blocked (data_missing) | Individual-participant fMRI RDMs are in neither the dandiset nor the authors' archived repo. The repo's `models/` holds only three .hdf5 files: MC, PC-IP and unstructured. |
| rdm-consistency | reproduced (borderline) | Cell 26: mean r = 0.928 (SD 0.041, min 0.817, max 0.990) against 0.90 ± 0.03. |
| fig3a-no-trend-to-unstructured | reproduced, weakly | Cell 28: interaction t(16) = 1.47, one-tailed p = 0.080, so the criterion is met. The statistic is three times the paper's t(6) = 0.50, the p-value is near the threshold, and WUC with PC-IP itself falls over sessions (p = 0.038). |
| fig3b-confused-pairs-no-increase | reproduced | Cell 30: the session coefficient is negative (t = −3.56, one-tailed p = 0.996) and so is the run coefficient (t = −1.05, p = 0.85). The same holds in all variants. |
| fig3s1-all-pairs-small-decrease | reproduced on the criterion; significance only partly | Cell 32: both coefficients are negative and f² is 0.0064 and 0.0119 (< 0.02). The paper's significant session decrease (p = 0.004) appears only with the session noise covariance (p = 0.0055). In the main variant it is p = 0.052. |
| fig4e-muscle-before-somatotopy | blocked (data_missing) | The Muscle, Somatomorphic and Usage RDMs are named in the repo's configs (`muscle_somatomorphic.yaml`), but the .hdf5 files are gitignored and not in the archived commit or the dandiset. Time-resolved RDMs could be computed from the data; the decomposition cannot. |
| fig4s1-model-selection | blocked (data_missing) | Same component models missing. |
| fig4s4-well-isolated-units | blocked (data_missing) | The asset metadata lists only Units and ElectrodeGroup as measured variables. No waveforms or L-ratio are described, so the well-isolated subset cannot be defined. |

**B. Problems**

1. [affects a conclusion] Cell 12: three denominators are reported and only one matches the paper. Nothing in the paper fixes that choice, so the outcome for the 70% claim depends on an assumed definition.
2. [affects a conclusion] Cell 18: cue location is decodable above every shuffle, contrary to the paper's 1s6b. The notebook shows this robustly (two nulls, finger-mean removal, the authors' pipeline at 0.1115). It does not show screen- or run-level location counts, which would rule out a temporal-structure artefact. The design (each location once per 12-trial screen) makes such an artefact unlikely.
3. [affects a conclusion, weakly] Cell 28: the df is 16 against the paper's 6, and the model specification may differ from the authors'. With p = 0.08, a slightly different specification could cross 0.05.
4. [does not affect a conclusion] `crossnobis_rdm` / `run_rdms` (cells 30, 32): per-run RDMs use fold covariances from about 8 trials. In folds holding one trial of a finger, that finger's residuals are exactly zero. The covariance therefore has rank of about 3 across about 95 units, OAS shrinks toward a tiny identity, and the distances inflate. Per-run means are 5.06 against 0.68 for whole sessions; my synthetic test gave about 5× inflation, while session-sized data was unbiased (null mean 0.009). Directions are unchanged across variants, but the significance of the fig3s1 session term depends on the variant.
5. [does not affect a conclusion] `load_model_rdm`: the condition-order assert runs only if `pattern_descriptors/condition` exists, and the notebook never prints whether it did. The printed vectors are consistent with T, I, M, R, P order (thumb pairs are largest in the PC-IP model).
6. [does not affect a conclusion] Cell 30: the run-term df is 83 (85 runs), against the paper's 82. The paper itself also reports t(74) for the same test.
7. [does not affect a conclusion] Cell 22/24: the bootstrap "t-test" is a reconstruction, which explains p = 7.9e-5 against the paper's 1.9e-6. The criteria use CIs, so outcomes are unaffected.
8. [does not affect a conclusion] `tuning_pvalues`: the 0.1 Hz exclusion uses the in-window rate across all trials (minimum 0.113 Hz), while the paper may mean the session-wide rate. At most a few units could change.
9. [does not affect a conclusion] Helpers I tested on synthetic data: `weighted_sd` matches DescrStatsW(ddof=1), `diag_lda_cv` sits at chance on null data, and `crossnobis_rdm` recovers known distances (about 10% shrinkage bias) with a zero-distance pair giving −0.001. I found no train/test leakage in the classification or RDM code. Model RDMs come from the authors' repo, not the dandiset, and the notebook says so.

**C. What I could not check**

- Whether `start_time` is exactly the cue. The notebook infers it from the decoding curve (chance before the start, above 0.4 at 0.6 s). A trials-table column description, or the epoch/screen structure, would settle it.
- Whether the location decoding in 1s6b reflects gaze or trial structure. A table of `cue_location` against run and screen (trial_number // 12), and location accuracy with folds split by screen, would decide it.
- What the gaze regression would give. Cross-validated r² under row-major and column-major layouts would make 1s6a partly testable.
- The units table's column names (waveform_mean, quality metrics). Printing them would have confirmed the 4s4 block directly; the API metadata only implies it.
- Whether the model .hdf5 files carry condition descriptors. Printing that would close problem 5.
- The authors' exact regression specification for fig3a (the df of 6 is unexplained).

I saved the paper's full text (PMC9555862) under `paper/`. I did not download the dandiset or run the notebook.
