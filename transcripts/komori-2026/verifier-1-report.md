**Verifier report, round 1: Komori et al. (2026) on DANDI:001425 0.250705.0947**

The claims file has 24 claims. The two notebooks test the 6 resting-state claims and treat the other 18 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| rest-decoding-above-null | not_reproduced | Main run: model AUC 0.670 vs null 0.667, paired t p = 0.867 (decoding cell 14). Over 5 seeds the model AUC is 0.65–0.70 and no p is below 0.05 (cell 16). None of the 5 one-at-a-time readings beats null (cell 17), and the R4 b variant gives p = 0.454 (features cell 16). The model AUC is outside 0.82 ± 0.082. |
| rest-loss-accuracy-vs-null | not_reproduced | Loss 0.642 vs 0.640 (p = 0.757); accuracy 0.640 vs 0.638 (p = 0.911) (cell 19). The only seed with p < 0.05 (+3000) goes the wrong way for both: model loss higher, model accuracy lower. |
| rest-needs-0-1-hz | not_reproduced | 0.1 Hz is never above null: main p = 0.88, R5 b p = 0.18 (cell 21), and 0/5 seeds (cell 22). The 2 Hz model is also never above null, so that half holds. But the main 2 Hz AUC (0.718) is not below the 0.1 Hz AUC (0.668), against the paper's 0.51 and 0.86. |
| rest-ic-count-and-window | not_reproduced | The highest median AUC is at 13 ICs (0.710 vs 0.662 for 10) and at a 3.0 s window (features cells 7–8). The differences are tiny and come from models that are not above null, so this result says little either way. |
| rest-vif-below-10 | not_reproduced (partially_reproduced on a lenient reading) | The 10-IC maximum is 5.47: below 10, but outside 9.0 ± 0.9. 7 ICs are lower than 10 (Holm p = 0.024) and 13 do not differ (0.15), but 15 ICs do differ (p = 0.024; the claim says they don't) (features cell 10). Strictly, "the 10-IC maximum holds" fails because 5.47 is outside the tolerance. The value may also rest on a VIF definition that differs from the paper's (B4). |
| rest-shap-medial-anterior-first | not_reproduced | Reading (a): no IC has a window with p < 0.05 above null under either SHAP reading. Reading (b): the "medial anterior" IC peaks last (0.0 s, against −0.10 and −0.13 / −0.03 s) (features cell 14). The match itself is doubtful (B6). |
| fig1-ssp-then-pupil, fig1-roi-vif-vs-ica, fig1-somato-exclusion-window, fig1-somato-selection-rates, fig1-somato-spectra-correlation, fig1-somato-decoding, fig2-visual-pattern-sessions-ics, fig2-architectures-similar, fig2-visual-pattern-decoding, fig3-oddball-no-group-response, fig3-oddball-decoding, supp4-context-classifier-mos, supp8-permutation-importance, fig4-shap-somato-ic5, fig4-shap-visual-ics, supp10-top-shap-ics, fig4-mapped-shap-regions, supp2-session-selection-needed (18 claims) | blocked: data_missing | I checked the archive. It holds 1838 assets: task, resting-state and 33 `sensory-stim` files. Asset metadata describes the sensory-stim sessions as anaesthetised mice given a left-eye flash, right whisker-pad vibration and white noise. Those files are `_widefield.nwb` only, so there is no pupil. There is no hindpaw electrical stimulation, drifting grating or oddball task, and no Emx1-GCaMP6f mice. No part of these claims can be tested. |

### B. Problems

1. **[affects a conclusion]** Epoch selection, reading R5 (decoding cells 11, 17, 21).
   - The main run uses R5 a, no epoch selection. But the paper says the early- or never-crossing sessions "were therefore excluded from all datasets" (Results, somatosensory, paragraph 1). The Summary of Results says "Reliable prediction was achieved after excluding sessions…" without limiting it to stimulus data.
   - The claims file's line "for resting data it states no rule" is therefore a misreading; reporting it, not correcting it. R5 b is the better-supported main reading.
   - The notebook runs R5 b only at one seed per claim. It keeps 17 of 117 epochs (1802 samples, about 3 epochs per fold), so the test has very little power.
   - R5 b gives the only above-null results anywhere (0.2 Hz p = 0.018, 0.5 Hz p = 0.040). It was never combined with more data (R1 b) or with more seeds.
   - The "not reproduced" verdict under the reading most likely to be the paper's rests on one underpowered run.

2. **[affects a conclusion]** Readings not run (decoding cell 17).
   - R1 b (all 25 mice) and the "all available sessions" variant were not run.
   - The other readings were run one at a time, never in combination, although the criterion asks whether "some combination" reproduces.
   - So the claims are not reproduced under the combinations tried, not under every combination the paper allows.

3. **[affects a conclusion]** The null model is close to the real model by construction under the main reading (`make_dataset`, `shuffle_within`; cell 11).
   - Under R4 a + R5 a, 42 of 117 epoch windows have no positive label and 37 are entirely positive. Shuffling labels within an epoch therefore changes almost nothing.
   - The null is then nearly the same model (null AUC 0.667 vs model 0.670). The main-reading paired test cannot separate model from null, and the notebook does not point this out.
   - Only R5 b and R4 b give a null that actually differs from the model. Both were run once.

4. **[affects a conclusion]** The VIF definition (`pw.vif`, `select_ics`; features cells 4, 7, 10).
   - The helper computes a centred VIF (inverse correlation matrix) and says this equals statsmodels `variance_inflation_factor`. That is true only if a constant column is passed.
   - The paper's code (Python 3.6, so an older statsmodels) regresses each feature on the others without an intercept unless a constant is added. On features scaled to [0, 1] that gives an uncentred R².
   - Synthetic test: independent, 0.1 Hz-filtered, min-max features give a centred VIF of 1.0 but an uncentred VIF of 6.6 (OLS without constant).
   - The paper's values (1954 for ROIs, 9.0, 7.8) fit the uncentred definition. This reading was not run.
   - It changes the 10-IC VIF value. It also changes IC selection: under the centred VIF no IC is ever removed (all 30 ICs have max VIF 3.57), which makes readings (a) and (b) of rest-ic-count-and-window identical.

5. **[affects a conclusion, cannot be resolved]** The decomposition and features look nothing like the paper's (features cell 4 image vs Supplementary Figure 5A).
   - The kept ICs are broad and bilateral; IC 1, 5 and 6 cover most of the cortex. The paper's ICs are compact patches.
   - The per-component hemodynamic regression slopes of F470 on F405 range from −2.05 to 1.83 (decoding cell 5). Negative slopes add the 405 nm signal instead of removing it, so global or hemodynamic structure may remain.
   - The compactness heuristic standing in for visual inspection is an author choice. It is stated as an assumption, but its consequences are not checked.

6. **[does not affect a conclusion]** IC matching for the SHAP claim (features cell 13).
   - The "medial anterior" IC 16 has 0.675 of its positive weight in MOs and 0.31 in the midline band. It is a bilateral anterior map, not the paper's narrow midline band (IC7).
   - Under the criterion, "no IC matches" also means not reproduced, so the outcome does not change.

7. **[does not affect a conclusion]** Attribution method (`integrated_gradients`; features cell 12).
   - Integrated gradients from the mean validation input replace Deep SHAP; this is a stated deviation and reasonable.
   - "First sample per experiment" is taken per 40 s epoch, not per recording. This choice is not flagged as an assumption.

8. **[does not affect a conclusion]** Pupil cleaning (`clean_pupil`; decoding cells 5, 11).
   - The 3× median cutoff leaves values just under 3× the median (max 174.9 against a median of 58.3 in #51 day0; 171 against 59.4 in #53 day1).
   - Those two sessions correlate only 0.638 with the keypoint width. With the whole-recording min-max scaling, #53 day1 gets no positive label at all.
   - This affects 2 of 9 recordings. The R3 b variant (keypoint width) is also negative.

9. **[does not affect a conclusion]** Peak detection (`epoch_labels`).
   - The peak is the argmax within each epoch. On a monotonic trace it lands at the epoch edge (synthetic test: 39.97 s of 40). The label window can then run up to 0.5 s into the next epoch, which may sit in another fold, a small train/validation overlap.
   - No output reports how many peaks fall at epoch edges.

10. **[does not affect a conclusion]** Smaller items:
    - The 1.5 s window gets a +1 frame (46) and the other windows don't (features cell 8).
    - 3 of the 9 files were replaced between dandiset versions and were not compared (cell 4).
    - The metadata's swapped excitation wavelengths were correctly caught by the channel check (cell 5).

### C. What I could not check

- **The VIF definition the paper used.** I could not see `07_vif_calc` or whether it adds a constant. Needed: the per-fold maximum VIF computed without an intercept, and IC selection rerun under that VIF.
- **Whether the hemodynamic correction is valid.** Needed: the correlation of the corrected ROI-averaged signal with the deposited `dFF`, and the distribution of the slopes.
- **The labels.** Needed: the number of epoch peaks at epoch edges, and plots of the pupil trace with labels for #51 day0 and #53 day1.
- **Statistical power under R5 b.** Needed: R5 b over five seeds, per-fold AUCs, and R5 b with R1 b (all mice with pupil).
- **Comparison with the paper's training.** Needed: per-epoch loss and accuracy curves comparable to Supplementary Figure 5B–C. The models' best epoch was 1–2 of 10, with training AUC 0.72 against the paper's 0.928.
- **Rerunning anything myself.** I did not download data or rerun the notebook. I tested helper functions only on synthetic inputs (`epoch_labels`, `shuffle_within`, `folds_by_mouse`, `vif`), and they behave as documented apart from points B4 and B9.
