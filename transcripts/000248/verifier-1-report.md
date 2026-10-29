**A. Outcomes**

The claims file has 40 claims: 18 Neuropixels, `supp3-decoder-types`, and 21 on 2p data. Cell 0 marks all 18 Neuropixels claims as blocked (too_large), but every one has full outputs. The outcomes below are my own, read from those outputs.

| Claim | Outcome | Reason |
|---|---|---|
| results-npx-units-per-session | reproduced | V1 has 150.3 ± 19.8 RS units per session (1,804 in total); higher visual areas have 582.8 ± 43.3, within 597 ± 46 (cell 18). |
| methods-npx-ic-encoder-count | reproduced | 159 units are IC-encoders in at least one block (reading a), exactly the paper's 159; reading b gives 163 (cell 20). |
| ed6b-npx-v1-group-counts | reproduced | Reading b1 (all V1 units in the files, ICwcfg1) gives exactly 87 IC-encoders and 636 segment responders. Dropping units labelled noise gives 79 and 566 (cell 22; see problem 6). |
| ed6cd-npx-ic-encoders-all-areas | reproduced | All six areas hold IC-encoders: between 48 and 79 per area, and in 8 to 12 sessions per area (cell 24). |
| fig1e-npx-exclusive-center | not_reproduced | 44 exclusively center-responsive units under reading a and 52 under reading b, against 18 ± 1.8. The V1 RS count of 1,804 matches (cell 26). |
| fig1f-npx-ic-ire-responsive | not_reproduced | No combination puts both fractions within tolerance. IC-responsive ranges from 38.5% to 56.8% against 66.7 ± 6.67; IRE-responsive is within tolerance only under block (ii) (77.3% and 79.5%) (cell 28). This rests on the unit set of fig1e, which did not reproduce. |
| fig1g-npx-orientation-match | not_reproduced | The criterion ties the result to a reading that reproduces fig1f, and none does. The match ranges from 60.0% to 93.3%; only fig1e (a), block (i) gives 75.0%, within 78.6 ± 7.86. Every reading is above its shuffle 95th percentile (cell 30). |
| ed2b-npx-fixed-gaze | partially_reproduced | 10 sessions have eye tracking (matches the paper). Only 8 sessions are valid, against the paper's 9, and the criterion requires an exact match. Under fig1e reading a, 10 units remain (within 11 ± 1.1) and the match is above the shuffle 95th percentile (cell 32). |
| ed2f-npx-rf-match | reproduced | Reading b gives n = 414 with a match of 0.812; reading c gives n = 374 with 0.832. Both are within 398 ± 39.8 and 0.81 ± 0.081 (cell 34). |
| ed2g-npx-pupil-area | reproduced | Friedman p = 0.356 for reading a and 0.898 for reading b, both ≥ 0.05 (cell 36). |
| ed2a-npx-gaze-confined | reproduced | Friedman p = 0.47 for x and 0.37 for y. The confinement extent is reported only in camera pixels (24 to 124 px), so "fits within the gap" cannot be judged (cell 38). |
| fig2d-npx-ccg-hva-input | blocked (methods_underspecified) | Group sizes are exactly 79 and 526, and all 8 combinations give IC-encoders the higher mean with rank-sum p ≤ 5e-4. But under boxcar, raw flank, number of connections, the medians tie at 1 and 1. The criterion requires a higher median under every combination, otherwise blocked (cell 40). |
| fig3a-npx-v1-decoding | reproduced | V1 accuracy is 0.697 (decoder reading a) and 0.719 (reading b), with signed-rank p = 0.00049 against the chance of 0.25 under both. The chance level matches the paper's (cell 45). |
| fig3c-npx-v1-inference | reproduced | Under decoder reading b, TRE is decoded as IC 0.518 and as LC 0.210, both within tolerance, with p = 0.0024. Under reading a, LC is 0.1966, just below the tolerance bound of 0.198 (cell 47). |
| fig3d-npx-areas-inference | reproduced (per the criterion) | Five areas are significant and the three largest mean scores are V1, LM and AL. But the significant set is V1, LM, RL, AL and AM; PM is not (p = 0.092), while AM is (p = 0.0029). The paper has the reverse for PM and AM. Decoder reading a only (cell 49). |
| ed7b-npx-xre-inference | reproduced | All 6 areas are above 0.5, with p from 0.0005 to 0.0137, close to the paper's values. The chance level of 0.5 matches (cell 51). |
| ed7a-npx-no-area-above-v1 | reproduced | Under both readings, every significant V1-versus-HVA difference has the HVA lower. Kruskal-Wallis p-values are 0.0006, 0.0071, 0.0005 and 0.0077, all significant like the paper's (cell 53). |
| ed6ef-npx-ic-not-greater | reproduced | No area gives p < 0.05 in either panel. Eleven of the 12 p-values equal the paper's to 4 decimals (cell 55). |
| supp3-decoder-types | blocked (too_large), questionable | Only the neural network's cost was estimated: about 18 hours on one core (cell 57). The quadratic and RBF SVMs would take minutes and were not run. |
| 21 claims on 2p, mesoscope and holography data | blocked (data_missing) | Confirmed against the DANDI API. Version 0.240502.2344 has 78 assets (66 `_ecephys.nwb`, 12 `_ogen.nwb`), and its metadata lists only ecephys and ogen techniques. DANDI searches for "illusory", "Adesnik", "pattern completion" and "Shin Hyeyoung" return only 000248. |

**B. Problems**

1. **[affects a conclusion]** Cell 0: the status table marks all 18 Neuropixels claims as blocked (too_large), "outputs not reviewed". Yet cell 59 shows the notebook ran in 19.0 minutes, with outputs for every claim. The attempt record contradicts the notebook.
2. **[affects a conclusion]** Cells 43, 49, 51 and 53: decoder reading b was run on V1 only. The claims file says to run both readings, but fig3d, ed7b and ed7a rest on reading a alone. fig3d's significant set differs from the paper's at PM (p = 0.092) and AM, so reading b could change it.
3. **[affects a conclusion]** `il.decode`, reading b: the grid search covers only C from 1e-3 to 1. It does not search C above 1, the coding or the kernel scale, as MATLAB's OptimizeHyperparameters does, and its fits hit max_iter = 200,000 (convergence warnings in cell 43). fig3c reproduces only under reading b, and reading a misses the LC tolerance by 0.0014 with a single cross-validation seed. The outcome is fragile.
4. **[affects a conclusion]** Cell 32: a session counts as valid only if its fixed-gaze standard (non-inverse) RF trials cover all 9 positions. The paper's legend says "at least one trial in each position". Session 630506 covers 8 positions with standard trials only; counting inverse trials as well was not tried and might give the paper's 9 sessions.
5. **[affects a conclusion]** Claims file, fig2d: the "higher median under every combination" rule fails on a tie of integer medians (1 and 1), even though all 8 combinations give p ≤ 5e-4 in the stated direction. The criterion is brittle; I report it here and have not changed it.
6. **[affects a conclusion]** Cell 22, ed6b: the notebook reads "(b) all units not classified as noise" as every unit in the files (b1), including units whose `quality` label is noise. The notebook justifies this with the Methods' packaging sentence. The literal filter (b2) gives 79 and 566, which would fail the claim. The exact 87 and 636 under b1 strongly support the notebook's reading.
7. **[affects a conclusion]** Cell 57, supp3: the quadratic and RBF SVMs would cost about as much as the linear SVM (minutes) and were not run, so part of the claim was testable. The 18-hour network estimate is for one core with sklearn and runs in parallel.
8. **[does not affect a conclusion]** Claims file, fig3d: the criterion counts significant areas without naming them, so the claim reproduces even though PM and AM come out the reverse of the paper.
9. **[does not affect a conclusion]** Cell 36: for trials whose eye frames are all NaN, the `area_max` variant becomes -inf, so its range prints as NaN or inf. The decisive `area_mean` is unaffected.
10. **[does not affect a conclusion]** Cell 40: `stats.ranksums` has no tie correction, and the per-unit connection counts are heavily tied. With p ≤ 5e-4 this changes nothing.
11. **[does not affect a conclusion]** Cell 58 says "These 19 claims" but lists 21; the claims file has 21.

I tested the helpers on synthetic inputs, and they behave correctly:
- `kw_tukey` gives the same p-values as `scipy.stats.kruskal`.
- `auroc` matches `sklearn`'s `roc_auc_score`.
- `holm_reject` matches statsmodels' Holm correction.
- `ccg_counts` puts the peak at +5 ms when the source leads the target by 5 ms.
- `connections` detects that injected 5 ms connection under all four readings and finds none in independent trains.
- `decode` gives 0.23 on null data, near the chance of 0.25.
- `ic_trials` returns the alternating image rows.

Everywhere else, unit selection, response windows (0 to 400 ms and 0 to 1000 ms), training-fold-only z-scoring, the disjoint probe set and the HVA-leading lag sign are as the claims file specifies.

**C. What I could not check**

- I could not compare `holm_exclusive` and the fixed-gaze mode and blink rules with analyzeRFCI.m and analyzeMouseEye.m, because the code repositories were not available. Both fig1e readings are far from 18, so this does not decide fig1e.
- I could not check that XRE1 carries the same 135° real bar as IC1; cell 14 does not state the XRE orientations.
- These outputs, if added to the notebook, would have settled the open points:
  - per-session fixed-gaze position coverage including inverse RF trials (problem 4);
  - fig3c and fig3d repeated over several cross-validation seeds, and decoder reading b for all areas (problems 2 and 3);
  - quadratic and RBF SVM inference scores for V1, LM and AL (problem 7);
  - a count of fig1e units before the exclusivity step, under each reading, to locate where 44 or 52 diverge from 18.
