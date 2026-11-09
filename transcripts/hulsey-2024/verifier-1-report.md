**A. Outcomes** (29 claims in the claims file; the notebook tests 28 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| cohort-inclusion | partially_reproduced | 13 mice, 8 auditory and 5 visual, all match (cell 7). The archive has 391 sessions and 376 pass the criterion, against 381 in the paper (375 counted by hits). The 500 stage 5–6 sessions and the 18 excluded mice are not in the dandiset. |
| training-duration | blocked (data_missing) | Confirmed against the archive: version metadata gives 391 sessions from 13 subjects, and every file has stage S5 or S6 (cell 3). No part can be tested. |
| distractor-response-rate | reproduced | Reading (c), pooled over all mice, gives 0.052 (cell 10). Under (a) and (b) only 7 of 8 mice are below 0.10 (BW053 is at 0.16–0.17). |
| figs2-n-states | reproduced | Both O1 readings give 3–5 states per mouse (cell 12). The cross-validation used 3 initialisations instead of 10. |
| fig1g-example-mouse-prediction | reproduced | BW046: 4 states, 70.2% one-state, 78.3% best model (cell 25). |
| fig2a-state-types | reproduced | 13 of 13 mice have an optimal, a disengaged and at least one other state (cell 17). The template check is weak; see B4. |
| fig2b-optimal-occupancy | partially_reproduced | Indeterminate is 14.8 ± 2.2%, just outside 13.1 ± 1.6. Optimal beats each other state at p = 0.00024, 0.0024 and 0.0012 (cell 19). |
| fig2c-dwell-times | partially_reproduced | Optimal dwells are longer, all four tests p < 0.001. The indeterminate median is 3.00 ± 0.32 against 3.4 ± 0.3 (out). Disengaged comes out at 11.4–11.9 under readings (a) x/y; (c)(y) brings it to 13.6, in tolerance, but optimal is then 46.1. No reading puts 37 and 15 both in tolerance (cell 21). |
| fig2d-prediction-accuracy | reproduced | 76.0 ± 1.7%; gain 10.9 ± 1.2 percentage points; signed-rank p = 0.00024 (cell 23). |
| fig3c-inverted-u-pupil | reproduced | Reading (i) 12 of 13 mice, (ii) 13 of 13 (cell 27). |
| fig3d-optimal-pupil-modality | reproduced | Auditory median 0.627 vs visual 0.698; rank-sum p = 0.034, exact p = 0.040 (cell 30). |
| fig3e-u-disengaged-pupil | reproduced | The shape holds on all trials and on the stationary subset under reading (b). Reading (a) has no usable bins (cell 32). See B3. |
| figs4-r2-individual-movement | partially_reproduced | Pupil r² is 0.647 ± 0.060 (out of 0.72 ± 0.03). Face 0.486/0.432 is in tolerance, but face vs pupil is not significant (p = 0.24/0.15). Locomotion is in tolerance and significant only under O5 (b) (0.392, p = 0.048) (cell 34). |
| fig3f-movement-index-inverted-u | partially_reproduced | Inverted U holds; vs pupil p = 0.34 as the claim needs. r² is 0.567 under (a) and 0.554 under (b), both just below the 0.57 lower bound (cells 34, 36). |
| fig3f-movement-index-u-disengaged | reproduced | Quadratic term +0.026, vertex at 0.0, inside the range (cell 38). |
| figs5-movement-index-correlations | reproduced | The two r are identical, as they must be by construction. Minimum r is 0.674, so reading (b) holds and (a) does not (cell 40). |
| fig3-distance-from-optimal-pupil | partially_reproduced | Order and tests hold (p = 0.00024 and 0.021). All three values are about 1.5× the paper's: 10.7, 18.0, 13.0 against 7, 12.6, 9 (cell 42). |
| fig3-raw-face-energy-trend | reproduced | 0.487, 0.443, 0.442, all in tolerance; optimal vs sub-optimal p = 0.00049; vs disengaged p = 0.068 (cell 43). |
| fig3-raw-locomotion-no-difference | reproduced | p = 0.74 and 0.68 under (a), 0.54 and 1 under (b); values 0.134–0.136 (cell 44). |
| fig4a-lower-variability | partially_reproduced | All six differences are negative and 5 of 6 tests pass; face optimal vs sub-optimal p = 0.08 (cell 46). |
| fig4b-variability-at-transitions | partially_reproduced | All six signs are right. Of the four marked tests, pupil exit and locomotion exit pass; face entry (p = 0.15) and locomotion entry (p = 0.24) do not (cell 48). |
| fig4d-pupil-movement-decoupling | reproduced | p = 0.00024 and 0.0081 (cell 50). |
| figs6-individual-measure-decoupling | reproduced | Optimal vs disengaged p = 0.0046 for both pupil–face and pupil–locomotion (cell 52). |
| fig5c-state-classification | reproduced | 88.5/88.2% and 77.2/76.4%, all in tolerance; 34 of 34 classifications significant under every reading. There are 21 sub-optimal classifications against the paper's 19 (cell 60). |
| figs7-pupil-best-raw-measure | reproduced | Reading (a), accuracy: pupil 71.1 > face 65.7 (p = 0.00043) and > locomotion 67.7 (cell 62). |
| fig5c-movement-index-best | not_reproduced | Under the Figure 5C legend reading, the movement index is significantly worse than pupil: 67.7 vs 71.1%, p = 0.017. Only the code variants that also keep pupil features go the claimed way (cell 64; B2). |
| figs8a-regression-weights | reproduced | Pupil and locomotion squared and SD terms have the stated signs (p ≤ 0.027); face terms p ≥ 0.13 (cell 56). |
| figs8b-pupil-movement-interaction | reproduced | P×M is 0.34 ± 0.11 for sub-optimal fits and −0.82 ± 0.23 for optimal fits; rank-sum p = 5.6e-5; optimal M×M is −1.52 (cell 58). |
| figs1-iti-independence | reproduced | Median ITI r is between −0.044 and −0.007, all Wilcoxon p ≥ 0.13; four-group Kruskal-Wallis p = 0.23 (cell 54). |

Chance level: the decoders use balanced classes, and the null means come out at 47.6–50.9%. That matches the 50% chance the design implies.

**B. Problems**

1. [does not affect a conclusion] Cell 12, `cv_tasks`: the cross-validation runs 3 initialisations instead of 10. I tested the helper's EM on synthetic 3-state data: it recovers the parameters and the log likelihood rises monotonically, but 2 of 3 random starts ended in a worse local optimum. With 3 starts, the test curves for larger state counts can be understated. The range still matches and BW046 still gets 4 states. Per-mouse counts could shift, which feeds the narrow misses in fig2b and fig3f.
2. [affects a conclusion] Cell 64, fig5c-movement-index-best: the two variants that reproduce the claim cannot test it. Condition 5 keeps the pupil value and condition 1 keeps the pupil value and SD alongside the movement index, so they compare pupil plus movement against pupil alone. Only the "M only" comparison tests the claim, and it goes the other way.
3. [does not affect a conclusion] Cell 32: stationary reading (b) uses `running_speed < 0.02`. Speeds go down to −0.169 m/s, so this also counts backward-moving trials as stationary. It should be `abs(speed) < 0.02`. The size of the effect is not shown.
4. [does not affect a conclusion] `state_types` with `fixed_first_two`, fig2a: every state other than optimal and disengaged is forced onto one of the four sub-optimal templates, so "each other state matches" cannot fail. The notebook's six-template check (cell 14) shows two weak spots:
   - For BW061, state 2 is nearest the optimal template, and the state labelled optimal is nearest bias right.
   - For BW048, two states are nearest bias left.
5. [does not affect a conclusion] `dwell_table` copies `flex_hmm.get_dwell_times` exactly. I confirmed by fetching the code. It inherits a quirk: when a session's last trial differs from the one before it, the function adds a spurious last epoch (dwell 0, run 1). Synthetic test: `[0,0,0,nan,nan,1,1,0,nan]` yields an extra state-0 row with dwell 0.
   - Each such epoch adds a zero gap to the indeterminate dwells.
   - Reading (x) is therefore not a clean run length.
   - The paper's code has the same behaviour.
6. [affects a conclusion] Cell 27, `cv_r2`: pupil r² comes from a single shuffled 5-fold split. BW051's r² of 0.086 is an outlier; its face, locomotion and movement-index r² are 0.54–0.83. That one value pulls the mean to 0.647, out of tolerance. It also makes the movement-index "not different from pupil" test easier to pass.
7. [does not affect a conclusion] Cell 7: reward-series counts and hit counts disagree for some sessions (BW071: 150 vs 79; BW059: 102 vs 97). Both are shown, and neither count gives 381.
8. [does not affect a conclusion] Cell 60: decoding uses 3 runs per condition and 20 null runs. All z ≥ 4.9, so significance does not depend on this. Min-max scaling before the split and shuffled KFold on autocorrelated trials follow `5_decoding.py`.

Checked and consistent with the paper's code (fetched from the linked GitHub commit):
- The test log likelihood is ssm's `log_probability`, which includes the prior (`2_n_states.py`).
- Stimulus values, choice coding and distractor removal match `get_stim_vals` and `format_choice_behavior_hmm`. The 10-trial SDs are computed on target trials only.
- The ITI is the start-to-start difference over target trials (FigureS1.py).
- `permute_hmm`, the 0.8 posterior threshold and MAP `choice_hmm_fit` match.
- Prediction folds are contiguous blocks within each session.
- running_speed is labelled cm/s but its values are in m/s; the notebook treats them as m/s, and they match the paper's 0.14 m/s.

**C. Could not check, and the output that would settle it**

- Per-mouse state counts with 10 cross-validation initialisations: rerun cell 12 with `N_INIT_CV = 10`.
- The BW061 and BW048 labels: print each state's psychometric matrix (`psychos` output).
- How many reading (b) stationary trials have speed below −0.02, and the fig3e shape with `abs(speed) < 0.02`.
- Pupil r² over several shuffled splits per mouse, BW051 especially.
- The trials-table column list: if a `visual_gabor_angle` column exists, `get_stim_vals` takes the visual inputs from it, not from the hard-coded 1/0.8/0.6.
- Which sessions make up the paper's 381: the paper gives no list.
- "No discernible change" in stage 6 is untested, per the claims file.
- I did not re-run the notebook; all numbers above are its saved outputs.
