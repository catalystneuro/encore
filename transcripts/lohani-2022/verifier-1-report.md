## Verifier report, round 1: Lohani, Moberly et al. 2022 on dandiset 001172 (0.260129.0829)

There are 26 claims in the claims file. 21 have a `data` field and the notebook tests them; 5 have no `data` field and the notebook marks them blocked. No attempt record is in the working directory, so the counts come from the claims file and the notebook only. The paper states no chance levels, so there is nothing to compare there. The paper text (PMC10661869) is saved in `paper/`.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| allen-parcel-link | partially_reproduced | Mask match: the union of non-zero pixels in each session equals brainMask rotated 180° (1.000; best other orientation 0.982). Left VISp has the largest response in only 2 of 4 mice (ranks 1, 1, 3, 2; cell 20), but the top parcel is a left visual area in all 4 mice and left VISp is above right VISp in all 4. If the mask rule is read per movie, it fails: grabAM08 spont calcium agrees at 0.996, below 0.999 (problem 1). |
| fig2a-r2-differs-across-areas | reproduced | Friedman test across 23 parcels with 4 mice: ACh p = 1.4e-6, calcium p = 6.1e-6 (cell 24). |
| fig2b-ap-gradient-inverted | reproduced | ACh ρ = −0.761, p = 2.5e-5; calcium ρ = 0.555, p = 0.006 (cell 25). The spontaneous-only variant agrees (cell 26). Calcium ρ in grabAM05 alone is −0.01. |
| fig2c-face-best-predictor-ach | reproduced | Single-variable R²: face PC1 is highest in 4/4 mice, Friedman p = 0.018 (exact p 0.005, my enumeration). Unique contribution: face highest in 4/4, p = 0.039 (cell 28). |
| fig2c-face-best-predictor-calcium | reproduced | Face PC1 is highest in 4/4 mice, Friedman p = 0.018 (cell 29). The margin over wheel speed is small in grabAM06 (0.142 vs 0.126) and grabAM08 (0.139 vs 0.121); see problem 3. |
| s7-face-onset-transients | partially_reproduced | ACh 0.728 (tolerance 0.55–0.73, inside by 0.002), t-test p = 0.009. Calcium 0.920 is outside 0.54–0.84, p = 0.006 (cell 32). |
| s7-locomotion-onset-transients | partially_reproduced | ACh 0.761 is within tolerance but p = 0.068. Calcium 1.985 is outside 1.39–1.61, p = 0.027. Both are positive in 4/4 mice (cell 33). |
| s7-ach-transients-same-across-states | reproduced | Onset-type effect p = 0.879 and area effect p < 0.001 (cell 35). This is an absence result with 4 mice, and the per-mouse differences run from −0.29 to +0.63. |
| s7-calcium-transients-largest-at-locomotion | partially_reproduced | The locomotion transient exceeds the face transient in 4/4 mice, but the onset-type effect has p = 0.078 (cell 36). |
| s7-ap-gradient-transients | reproduced | ACh ρ = −0.61 (p = 0.002) and −0.75 (p = 3.5e-5). Calcium p = 0.95 and 0.63 (cell 37). |
| fig3b-ecog-desynchronization | blocked (data_missing) | The files contain no ElectricalSeries (checked in the archive, problem 13). |
| fig3c-ach-sustained-face | reproduced | With 3 mice: low face −0.129 and high face 0.158 are both within tolerance; LSD p = 0.027 (cell 40). |
| fig3c-ach-locomotion-no-further-increase | reproduced | LSD p = 0.336 meets the absence criterion. However, locomotion exceeds high face in 3/3 mice, and the locomotion mean of 0.250 is outside 0.10–0.22 (cell 41). |
| fig3c-calcium-sustained | partially_reproduced | The locomotion mean of 1.106 is outside 0.44–0.82, and the high-vs-low LSD has p = 0.244. Both orderings hold in 3/3 mice (cell 42). |
| s7-ap-gradient-sustained | partially_reproduced | ACh high minus low: ρ = −0.80, p = 4e-6. Calcium locomotion minus high: p = 0.125 (cell 43). |
| fig3d-ach-frontal-above-visual | reproduced | Frontal-motor exceeds visual in 3/3 mice, paired t-test p = 0.049 (cell 44), which is borderline. |
| fig3e-scopolamine-motor-not-visual | blocked (data_missing) | The only session types are spont, airpuffs and vis-stim; there are no drug sessions. |
| fig4a-ach-correlations-up-with-face | reproduced | 64 increases, 0 decreases. Motor-somatosensory pairs: 0.87 significant; other pairs: 0.12 (cell 47). |
| fig4a-ach-correlations-down-with-locomotion | reproduced | 243 of 253 pairs (96%) decrease, 0 increase, and every area group is covered (cell 48). |
| fig4b-calcium-correlations-up-with-face | reproduced | 161 increases (64%), 0 decreases, and every area group is covered (cell 49). |
| fig4b-calcium-correlations-down-posterior | reproduced | 100 decreases, 0 increases. Posterior pairs: 0.83 significant; other pairs: 0.24 (cell 50). |
| fig5-coupling-up-with-face | partially_reproduced | 10 of 23 parcels increase significantly (the criterion needs at least half) and none decrease (cell 51). |
| fig5-coupling-down-frontal-with-locomotion | not_reproduced | No parcel decreases significantly. MOs p = 0.072, MOp p = 0.076; the strongest decreases are PTLp and SSp-tr (cell 52). |
| s3-hemodynamic-correction | blocked (data_missing) | There are no GFP or mCherry control mice. The ACh3.0 part could in principle be tested (problem 13). |
| s2-ach-sensor-validation | blocked (data_missing) | There are no slice or basal forebrain stimulation data. |
| s8-cholinergic-axons | blocked (data_missing) | The only subjects are grabAM05 to grabAM08; there are no ChAT-GCaMP6s mice. |

Tally: 13 reproduced, 7 partially_reproduced, 1 not_reproduced, 5 blocked.

### B. Problems

1. **[affects a conclusion]** Cells 5 and 20, allen-parcel-link. The minimum per-movie mask agreement is 0.996 (grabAM08 spont calcium: 263 pixels inside the mask are zero in every frame), which is below the criterion's 99.9%. Only the union reading passes. Also, the 4 vis-stim sessions this claim uses are never mask-checked; only their 499-frame offset is.
2. **[affects a conclusion]** Cells 17 and 18, fig3c, fig3d, fig4, fig5. These rest on 3 mice. grabAM06 contributes 2 epochs per state (14.6 s in total) but has equal weight in the ANOVA, the LSD and the paired t-test. fig3d's p = 0.049 depends on that. grabAM07 drops out because it has no high-face epoch.
3. **[affects a conclusion]** Cell 23 and `load_session` (`wheel_frame`). The wheel predictor is signed speed (minimum −0.14), not absolute speed. The paper says "locomotion speed". This could change the narrow face-versus-wheel margins in fig2c-calcium. Untested.
4. **[affects a conclusion]** fig3c-ach-locomotion-no-further-increase and s7-ach-transients-same-across-states pass only as absence results at n = 3 or 4. The direction of the data (locomotion above high face in 3/3 mice) goes against the claim. The outcome stands under the criterion but carries little weight.
5. **[does not affect a conclusion]** s7-face-onset ACh is 0.728 against a tolerance edge of 0.73. A tiny change in windows or onsets would flip it to outside tolerance; the outcome would stay partial because calcium is already outside.
6. **[does not affect a conclusion]** `transient_peaks`. The peak is the maximum of a trial-averaged trace in 0 to 1 s, which is biased upward, and it is tested against 0. No null peak (random onset times) is shown.
7. **[does not affect a conclusion]** Cell 23. X is z-scored on the whole session before cross-validation, which is minor leakage. `cv_r2` centres on training data only. On synthetic data `cv_r2` returns about 0.50 for a true R² of 0.5 and −0.004 for noise. The penalty chosen by `ridge_mml_fit` equals a brute-force marginal-likelihood search on the same grid. The grid is 1e-3 to 1e6 in 91 steps, not ridgeMML's own optimiser.
8. **[does not affect a conclusion]** Cells 28 and 29. Friedman p-values are asymptotic with n = 4 and k = 3. The exact p is 0.0046 for χ² = 8 and 0.042 for χ² = 6.5; the verdicts are unchanged.
9. **[does not affect a conclusion]** `lsd` uses the state-by-mouse error of the area-averaged table. Recomputing from the printed means gives state F = 11.14 and 48.48, against AnovaRM's 11.08 and 48.30, so it is consistent with the two-way ANOVA.
10. **[does not affect a conclusion]** `permutation_test` uses p = fraction of |perm| ≥ |obs|, floored at 1e-4. Under a synthetic null with the same epoch counts (10, 2, 13) it is calibrated: 5.0% below 0.05 and 0.9% below 0.01. `max_crosscorr` matches a direct lagged correlation to 1e-15. It takes the value of largest magnitude, as the code does; the Methods say "maximum".
11. **[does not affect a conclusion]** `face_onsets` builds quiescent epochs from `[0, woff[:-1]]` to `won`, which drops the final quiescent period. `sustained_states` includes it. The two functions are inconsistent, and the code's behaviour here is not shown.
12. **[does not affect a conclusion]** Cell 9. grabAM08 spont has a calcium-wheel best lag of −13 frames under pulse timing; every other session is between −4 and +1. This is unexplained, and it is the same movie that has the 263 zeroed pixels.
13. **[does not affect a conclusion]** Blocked claims, checked in the archive. Asset paths contain only spont, airpuffs and vis-stim sessions. The subjects are grabAM05 to grabAM08. `variableMeasured` and the acquisition of grabAM05 11232019 list no ElectricalSeries. They do contain raw `OnePhotonSeriesVioletExcitationGreenChannel` (395 nm, 512×512) and `DFFOnePhotonSeriesViolet`. So the ACh3.0 part of s3 (puff- or visual-evoked negative dips, spatial versus pixel-wise regression) could be tested from raw blue and violet movies of about 50 GB per session. That would need a reimplementation of the spatial regression and native-space areas, because the registration transforms are not in the files. The notebook's "no control mice" reason covers only part of the claim.
14. **[does not affect a conclusion]** `wheel_changepoints` (moving-SD method). On a synthetic steady run with low noise it detects only the speed changes, at 20–22 s and 33–35 s, not 20–35 s. This is inherent to the code's method. All WheelActivation onsets and offsets are recovered to the sample (cell 11).

### C. Could not check

- Whether the archive's ΔF/F includes the code's hemodynamic correction. Not recomputable without the registration transforms. Output that would help: the brain-mean correlation of the archived blue ΔF/F with a pixel-wise 470/395 regression in native space for one session.
- Bias of the transient peak statistic. Output that would help: the same peak computed at random times during quiescence, per mouse.
- Per-movie mask agreement for the 4 vis-stim sessions. Output that would help: the cell 5 table for those sessions.
- Sensitivity of fig2c-calcium to absolute wheel speed. Output that would help: the cell 29 table with |speed|.
- Robustness of the 3-mouse results to grabAM06. Output that would help: fig3c, fig3d and fig5 results without grabAM06, and per-mouse epoch durations by state.
- Expected left versus right VISp asymmetry. The paper does not state which visual field the gratings were shown in. Output that would help: the VisualStimulus screen coordinates with the monitor side.
- Fidelity of the ridgeMML port and of the regression design (signed or absolute speed, lags), because the regression code is not in the paper's repository.
