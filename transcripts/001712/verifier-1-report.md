**Verification report, round 1: Davatolhagh et al. 2025 (doi:10.1101/2025.09.12.675910) on DANDI 001712 (draft)**

The claims file lists 18 claims. The notebook tests 7 and marks 11 blocked for missing data. No attempt record was among my materials, so these counts come from the claims file and the notebook's code cells. bioRxiv refused every request from this host (Cloudflare error 1015, then HTTP 429), so I read only the abstract, saved as `paper/biorxiv_details_abstract.json`. For methods I relied on the claims file's account of the paper.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1c-psychometric | reproduced | Cell 16: Spearman rho is 1.000 over 9 signed contrasts. P(right) at +100% minus -100% is 0.887 (needs ≥0.5). The lapse-and-erf fit is reported (bias -6.8, sigma 17.0, lapses 0.116 and 0.0). |
| fig1d-psychometric-params-genotype | blocked (data_missing) | One mouse and no genotype anywhere (checked below). |
| fig1e-rt-contrast | not_reproduced | Cell 19: rho is -0.053 with p = 0.15, which fails the p < 0.05 requirement. The median at 0% (0.089 s) does exceed the median at 100% (0.081 s). The result depends on how anticipatory movements are handled: with RT > 0.15 s, p = 0.0006 (see B2). |
| fig1f-rt-genotype | blocked (data_missing) | Genotype comparison. |
| fig1g-learning-genotype | blocked (data_missing) | One session only, and no genotype. |
| fig2bc-prior-shift | reproduced | Cell 21: at 0% contrast P(right) is 74/89 in right blocks against 37/73 in left blocks, one-sided Fisher p = 9.2e-6. Differences at each contrast and per-block biases (+2.9 vs -16.5) are reported and point the right way. |
| fig2bd-ko-smaller-shift | blocked (data_missing) | Genotype comparison. |
| fig2ef-block-adaptation | reproduced | Cell 24: A = 0.48, B = 1.00, tau = 25.1 trials, all within the criterion. Trials 20–39 vs 0–4: 0.827 vs 0.543, Fisher p = 2.7e-6. The fit is weak: B sits at its upper bound and tau has SE 16 (B3). |
| fig2g-ko-slower-adaptation | blocked (data_missing) | Genotype comparison. |
| fig3b-contralateral-visual | not_reproduced | Cell 27: both peaks lie left of the midline, and the Mann-Whitney p values (0.053, 0.14) exceed 0.05. Both peaks are frame-corner pixels outside the brain, so the failure is an artefact of the criterion (B1). Even so, the evidence that the response is visual is weak. |
| fig3c-ko-elevated-activity | blocked (data_missing) | Genotype comparison. |
| fig3d-ko-higher-correlation | blocked (data_missing) | Genotype comparison. |
| fig3e-ko-higher-variance | blocked (data_missing) | Genotype comparison. |
| fig4c-full-cvr2 | partially_reproduced | Cell 33: the best reading is (a), full model cvR2 = 0.471. That is above 0.3 but below the range of 0.486–0.660. Readings (b) 0.422 and (c) 0.126 also miss, as do all three with the intercept subtracted (0.09–0.14). |
| fig4cd-movement-dominates | partially_reproduced | Cell 36: movement ΔR² is 0.104 / 0.119 / 0.067 under readings a / b / c, and task ΔR² is 0.017 / 0.015 / 0.013. Movement exceeds task under every reading and task is below a fifth of movement, but movement ΔR² is nowhere near 0.297–0.440. |
| fig4cd-ko-more-movement | blocked (data_missing) | Genotype comparison. |
| figs2-ko-elevated-motion | blocked (data_missing) | Genotype comparison. |
| figs3-ko-higher-unique | blocked (data_missing) | Genotype comparison, and no unique-variance model was run. |

**Blocked claims, checked against the archive:**
- The draft has 5 assets, one subject (FD-28) and one session. Draft is the only version.
- The asset's `wasAttributedTo` record has sex, strain (C57BL/6) and age, and no genotype.
- The dandiset description says "CNTNALP2 knockout", which contradicts Nrxn1a in the paper and in the file's keywords.
- No genotype contrast can be tested. The single-session quantities behind fig3c–e and figs2 (dF/F level, correlations, variance, motion energy) are in the data and could be computed, but with no comparison group they cannot test these claims.
- fig1g needs the training history, which is not in the archive.
- The notebook's blocked status is correct for all 11.
- The paper states no chance level for any selection, so there was nothing to compare.

### B. Problems

1. **[affects a conclusion] fig3b, cells 27–28.** No brain mask is applied.
   - Both "peaks" are at frame corners: (0,0) and (539,2). Mean fluorescence there is 534 and 926, against a 5th percentile of 1538.
   - With the post hoc mask (bright pixels, 20-pixel margin), the peaks fall on opposite sides of the midline (columns 199 and 481) with p of about 1e-15. That would make the outcome partially_reproduced.
   - However, the evoked window (0.1–0.4 s) contains the choice movement: median onset is 0.086 s (cell 12). The right-vs-left difference first exceeds its null only at 0.256 s (cell 12).
   - So the lateralization could come from the movement, not the visual stimulus. The notebook never separates the two, for example with trials where RT > 0.4 s.
2. **[affects a conclusion] fig1e, cell 19.**
   - The median RT is 0.069 s, and 149 of 899 onsets fall at or before stimulus onset (cell 5). Both point to `wheel_movement_onset_time` capturing many anticipatory movements, not visually driven ones.
   - The verdict changes with the RT floor: p = 0.15 overall, 0.068 for RT > 0.08 s, 0.0006 for RT > 0.15 s.
   - The RT distribution was never compared with the paper's Figure 1E.
3. **[does not affect a conclusion] fig2ef, `adaptation` (cell 24).**
   - B is pinned at its bound of 1.0.
   - tau has SE 16.1, so its plausible range extends past 40.
   - The curve is fitted unweighted to per-trial means whose n varies; the last block has only 9 trials.
   - The Fisher test carries the result on its own.
4. **[affects a conclusion: magnitude for fig4c and fig4cd] cell 30 and `body_video_components`.**
   - The movement set is reduced: no left or right camera video components, and the body video is binned 16×16 down to 1280 pixels.
   - Without the video components, movement ΔR² drops from 0.10 to 0.04. Under reading (c) it falls below task ΔR² (0.010 vs 0.015).
   - Movement ΔR² therefore depends heavily on the video regressors, and the shortfall against 0.30–0.44 may come from this reduced design. The claims file pre-specified this design, so the criterion outcome stands.
5. **[does not affect a conclusion] `segment_frames` and `folds` (cells 30–31).** Train and test data overlap.
   - Folds are random at the row level, so frames from the same trial land in both training and test sets. This follows chiCa.
   - 8,971 of 63,770 rows are the same imaging frame entered twice, because the stimulus and feedback windows overlap. Their Y and movement values are identical.
   - This can only inflate cvR2. The values are already below range, so the outcomes would not change.
6. **[does not affect a conclusion] `fit_model`, reading (b), and the pooled reading (a).** Both are computed over all 345,600 pixels, brain and non-brain, because the files hold no mask or atlas registration (cell 8).
7. **[does not affect a conclusion] "intercept only" model (cell 31).**
   - It shuffles all task and movement columns and keeps them, which is not a true intercept-only model.
   - Its ridge penalty differs (178 vs 56). The "minus intercept" readings may be slightly off.
8. **[does not affect a conclusion] Metadata inconsistencies.** The notebook reports all of these and works around them correctly:
   - The imaging plane says GCaMP6f while the paper and keywords say GCaMP6s.
   - The raw file states an imaging rate of 15 Hz; the timestamps give 31.2 Hz.
   - The wheel description says counter-clockwise is positive, but counter-clockwise choices turn with negative velocity. Choice labels were validated against rewards (cell 5) and used as given.
   - The dandiset text says CNTNALP2.
9. **[does not affect a conclusion] Assumptions never checked.**
   - The three ROI motion energies are assumed to be the whisker pads and body (cell 10).
   - The action-kernel form of the subjective prior is assumed (`fit_action_kernel`).

**Helper tests on synthetic data:**
- `_ridge_fold` matches closed-form ridge to 1e-14, and its GCV-chosen penalty matches a brute-force GCV.
- The per-pixel R² in `fit_model` matches an explicit pixel-space computation.
- `folds` gives equal folds balanced per time point.
- `fit_psychometric` recovers its generating parameters to within sampling error.
- `bin_to_frames` and `frame_index` behave correctly.

### C. What I could not check

- **The paper's full text** was unavailable here because bioRxiv rate-limited the host. I could not verify against the paper:
  - the RT definition and the Figure 1E values;
  - the encoding-model windows, the movement regressors and cameras used, and whether cvR2 is computed over masked or atlas-aligned pixels;
  - the Figure 3B analysis window.
- **Outputs that would have let me check more:**
  - RT histograms, plus the contrast correlation using response time (choice registration minus stimulus onset). This would show whether fig1e fails only because of anticipatory onsets.
  - An evoked map and peak test with a brain mask fixed in advance, restricted to trials with RT > 0.4 s, and a time course aligned to movement onset. This would separate a visual from a motor lateralization for fig3b.
  - cvR2 with folds grouped by trial and duplicate frames removed. This would show how large the leakage in B5 is.
  - The distribution of per-target ridge penalties, including the fraction at the grid edges.
  - Bootstrap confidence intervals for A, B and tau in fig2ef.
  - The fig4c/d readings with the left and right camera video components included, to test whether the reduced movement set explains the low movement ΔR².
