# Verifier report, round 1: Guan, Aflalo et al. 2022 (eLife 74478), dandiset 000147 version 0.221122.2256

Bash would not start in this session (the sandbox needs `socat`, which is not installed). So I read the notebook's outputs from its JSON with Grep, and I did not run any helper on synthetic inputs. I saved the paper excerpts to `paper/guan2022_excerpts.md`, taken from PMC9555862.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| recording-counts | reproduced | Cell 9: units 95.8 (SD 6.7), trials 408.0 (SD 40.8), total 4080. All match the claim exactly. |
| fig1b-online-accuracy | reproduced | Cell 10: 0.8596 (trial-weighted SD 0.036) over 4016 trials, against 0.86 ± 0.01. Chance from shuffling is 0.169 and 1/6 is 0.167, which matches the paper's 17%. The data have 64 No-Go trials in the first session where the paper says 84, but 4080 − 64 = 4016 agrees with the paper's own total. |
| fig1b-errors-middle-ring-pinky | partially_reproduced | Cell 12: 0.697 only when errors involving No-Go are dropped from the denominator. Over all online errors the fraction is 0.468, and over errors on finger trials it is 0.592. The paper does not define the denominator, and the denominator that matches was picked after seeing the numbers. |
| fig1s4a-offline-accuracy | reproduced | Cell 14: diagonal LDA with leave-one-out gives 0.934 (weighted SD 0.016) over 4080 trials, against 0.92 ± 0.02. It sits 0.014 above the paper. The authors' 8-fold pipeline gives 0.924. |
| fig1s4b-calibration-accuracy | blocked (data_missing) | Checked in the archive: the 10 assets are all main-task files ("individual-finger press, main task"), and the dandiset metadata mentions no calibration task. |
| fig1s5-tuned-fraction | reproduced | Cell 16: 0.879 with FDR over all pooled tests, against 0.89 ± 0.05. The other FDR families give 0.875 and 0.839, also within tolerance. No unit falls below 0.1 Hz. |
| fig1s6a-gaze-regression | blocked (metadata_insufficient) | `cue_location` is an index from 1 to 12 with no description and no map to screen coordinates. The paper's legend asks for [x, y] coordinates. The test could be run under an assumed row-major 3×4 layout, but the notebook did not do this. |
| fig1s6b-gaze-classification | not_reproduced | Cell 18: pooled location accuracy is 0.1154, outside the shuffled 95% range (0.0755 to 0.0944, maximum 0.0998), with 0 of 500 shuffles reaching it. It stays above chance within-finger (0.117) and with the authors' pipeline (0.112). The finger half of the criterion holds (0.934 against 0.155 to 0.181). The effect is small (chance is 0.083) and 6 of 10 sessions are individually significant. One caveat is in B2. |
| fig1s6c-control-task | blocked (data_missing) | Checked in the archive: there is no control or passive-viewing task in any of the 10 assets or in the metadata. |
| fig2d-rdm-structure | reproduced | Cell 20: in the mean RDM the largest middle/ring/pinky distance is 0.482 and the smallest thumb distance is 0.641, so the criterion holds. It also holds in 9 of 10 individual sessions. |
| fig2f-able-bodied-over-unstructured | reproduced | Cell 22: the WUC difference is 0.0998 with bootstrap 95% CI 0.074 to 0.127. All 10 sessions favour the PC-IP model, and the bootstrap p of 4.4e-5 compares with the paper's 5.7e-5. The model RDM comes from the authors' repository, not the dandiset. |
| fig2s5-mc-over-pcip | reproduced | Cell 24: MC minus PC-IP is 0.088 with CI 0.060 to 0.112. Mean WUC with MC is 0.9686, which is at or above the lower ceiling minus 0.05 (0.9838 − 0.05 = 0.934). The p-value is 7.9e-5 here against 1.9e-6 in the paper, and only 1 of 10 sessions reaches its own lower ceiling. |
| fig2-typical-among-individuals | blocked (data_missing) | Checked: the individual fMRI RDMs are in neither the dandiset nor the authors' repository `models/` folder at commit 6915bf8, which holds only the MC, PC-IP and unstructured models. |
| rdm-consistency | reproduced | Cell 26: mean r 0.928 (SD 0.041, min 0.817, max 0.990), against 0.90 ± 0.03. This is at the edge of the tolerance and runs high. |
| fig3a-no-trend-to-unstructured | reproduced | Cell 28: interaction t(16) = 1.47, one-tailed p = 0.080, so the criterion (p > 0.05) holds. This is weaker than the paper's t(6) = 0.50, p = 0.32. The PC-IP WUC itself falls over sessions (slope −0.009, p = 0.038), which the paper does not report. |
| fig3b-confused-pairs-no-increase | reproduced | Cell 30: the session and run coefficients are negative in all six variants, with one-tailed p for an increase between 0.73 and 0.996. |
| fig3s1-all-pairs-small-decrease | reproduced | Cell 32: the session coefficient is −0.049 and the run coefficient −0.075, both negative. Cohen's f2 is 0.0064 and 0.0119, both below 0.02. In the primary variant the session decrease is not significant (t(8) = −2.28, p = 0.052, against the paper's −4.0, p = 0.004). It is significant in the shared-noise variant (p = 0.0055). |
| fig4e-muscle-before-somatotopy | blocked (data_missing) | Checked: the Ejaz et al. 2015 muscle and somatotopy RDMs are in neither the dandiset nor the repository `models/` folder. The neural side could be tested, since the files carry spike times that the notebook already bins in 50 ms steps. |
| fig4s1-model-selection | blocked (data_missing) | Same reason: the component model RDMs are not available. |
| fig4s4-well-isolated-units | blocked (data_missing) | The dandiset metadata lists only Units and ElectrodeGroup, with no L-ratio or waveforms. I did not inspect the units columns myself. The notebook's statement rests on its own reading of the files. |

## B. Problems

1. [affects a conclusion] Cell 12: the 70% figure matches only under the denominator "errors between two fingers", and that choice was made after seeing all three results. Over all errors the fraction is 47%.
2. [affects a conclusion] Cell 18, `diag_lda_cv` with `folds=8` and no `rng`: the folds are unshuffled, so each one is a block of time. Both nulls permute labels across the whole session. If cue locations are unevenly ordered across runs, slow drift could raise location accuracy, and these nulls would not control for that. A null that permutes within run, or a check that cue locations are balanced per run, is missing. The not_reproduced verdict holds by the criterion, but its cause is not established.
3. [affects a conclusion] `run_rdms`, cells 30 and 32: per-run crossnobis distances with per-fold OAS covariances average 5.06, against 0.68 for the session RDMs. The notebook explains this by folds holding only one or two trials per finger. The primary session t-values depend on this inflation: −2.28 against −3.76 with the shared covariance. The fig3s1 significance claim depends on which variant is taken as primary.
4. [does not affect a conclusion] Cells 30 and 32: the regressions use the file's `Run` values directly as the run index. The notebook never prints them, so it is unclear whether they restart at 1 in each session or are contiguous. The data hold 85 run RDMs, while the paper's t(82) implies 84 or fewer. The df of n − 2 is also an interpretation, since the paper says the df is "the number of RDMs".
5. [does not affect a conclusion] Cell 28: OLS treats the 20 WUC values as independent even though they come in pairs from the same sessions, so df = 16. The paper reports t(6), which suggests a different model.
6. [does not affect a conclusion] `load_model_rdm`: the condition-order assert runs only if `pattern_descriptors/condition` exists in the file. The notebook does not show that it ran, so the T,I,M,R,P order of the model vectors may be assumed. The printed vectors look plausible (largest distances involve the thumb, and I–M is smallest).
7. [does not affect a conclusion] `crossnobis_rdm` uses OAS shrinkage where the paper names Ledoit-Wolf (disclosed in the module docstring). Each fold pair's precision comes from the same two folds whose means it whitens. This is a minor departure, with no train/test leakage.
8. [does not affect a conclusion] Cell 24: the bootstrap p (7.9e-5) is about 40 times the paper's 1.9e-6. The paper's exact bootstrap t-test is underspecified, and the claim criterion does not depend on the p-value.
9. [does not affect a conclusion] Data checks (cells 3, 5 and 7) are sound. The decoding curve stays at chance before t = 0 and rises from about 0.6 s, which confirms that `start_time` is the cue. Unsorted spike times are sorted before counting, and no analysed trial window touches an unsorted span. The `diag_lda_fit`/`predict` code, the window counting in `load_session`, and `weighted_sd` (matching DescrStatsW with ddof=1) read correctly. I checked these by reading the code, not by running it.

## C. What I could not check, and what output would settle it

- I could not test the helper functions on synthetic inputs. A notebook cell that recovers known distances with `crossnobis_rdm`, and known accuracies with `diag_lda_cv`, on simulated Gaussian data would settle this.
- Cue-location balance over time (B2). The fix is a run × cue_location count table per session, plus location accuracy against a null that permutes within run.
- Run numbering (B4). The fix is to print `sorted(set(trials.run))` for each session.
- Model condition order (B6). The fix is to print whether `pattern_descriptors/condition` exists in each model file, and its contents.
- Units table columns for fig4s4. The fix is to print the keys of `f["units"]` to show that no L-ratio or waveform field exists.
- The fig1s6a regression under an assumed grid layout. Printing cross-validated r² per session for a row-major 3×4 mapping would make that claim at least conditionally testable.
- The paper's exact denominator for the 70% error claim, and its bootstrap test. The paper text I fetched gives neither.
