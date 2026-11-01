**A. Outcomes** (24 claims, from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig1f-tone-response-inverse-u | reproduced | Kruskal-Wallis p is 2e-7 to 1e-4 in all 32 readings, and the top bin is 32-43 every time (cell 11). Only one inclusion reading gives a count within tolerance: 318 cells. The others give 339, 215 and 241, against 295±29.5. |
| fig1g-reliability-intermediate | reproduced | p is 1e-8 to 9e-7 in all 8 readings, and the top bin is always 21-32, which is interior (cell 15). |
| fig1h-cgc-largest-intermediate | reproduced | p is 3e-17 to 1e-9, and the top bin by mean is interior in all 8 readings (cell 17). The top bin is 54-65 in 7 of the 8, not the paper's 43-54. The means are driven by outliers: factors range from -109 to 38, and some HIGH peaks are ≤0. |
| fig1h-cgc-evident-all-bins | not_reproduced | No reading is significant in all 7 bins. Bin 32-43 has a mean near 1.0 and p = 0.2–0.9 under every test (cell 18). |
| fig1i-baseline-contrast-interaction | reproduced | Counts are within tolerance only for the "values_in = both" readings with SD over time (1830 and 1932 values). Under those, p_bin < 1e-43 and p_int = 0.006–0.040 (cell 20). |
| fig1i-contrast-effect-intermediate-only | not_reproduced | On the ANOVA readings whose counts match, both Bonferroni families flag only 54-65. 43-54 is not significant: p_bonf7 = 0.10–0.22 (cell 21). The "all" readings, whose counts do not match, would give methods_underspecified, because the families disagree there. |
| fig2b-evoked-pd-whole-drc | not_reproduced | All 6 group-by-unit readings have p ≥ 0.096 (cell 23). Only the variant without the 50% limit is significant (p = 0.011). |
| fig2c-evoked-pd-1-2s | blocked (methods_underspecified) | Group A+B pooled by trials gives p = 0.0098. The other 5 readings give p = 0.12–0.63 (cell 24). The criterion assigns this outcome when readings disagree. |
| fig2e-drc-responses-no-difference | not_reproduced | HIGH > LOW at p = 1e-9 to 1e-14 in every reading, with a median difference of about -1.3% dF/F (cell 26). Cell counts (225–375) are never within 520±52. Group B is 12 mice of mixed genotype, against the paper's 14 C57BL6/J. |
| fig3b-lme-coefficients | reproduced | Baseline PD p = 1e-4 to 7e-3 in every reading. Evoked PD p = 0.13–0.29 and the interaction p = 0.56–0.98 (cell 28). |
| fig3c-lme-likelihood-ratio | not_reproduced | LRT p = 0.0012–0.048 in all 8 readings (cell 29). The effect comes mainly from the contrast term, which the null model leaves out, as the paper's Methods also state. |
| fig4c-wt-contrast-zx1-effects | not_reproduced | contrast × ZX1 has p ≈ 0.25 in every reading (cell 31). Only 1 to 3 of the 5 terms are significant, so even the partial condition fails. |
| fig4-wt-posthoc | not_reproduced | HIGH−LOW in CTRL has Tukey p = 0.078. ZX1 on HIGH has p = 0.83 (cell 33). |
| fig4f-ko-no-contrast-effect | blocked (methods_underspecified) | The contrast slope is significant (p = 0.006–0.009) in 3 of 4 readings. In the full factorial with reference coding it is not (p = 0.245) (cell 34). |
| fig4f-ko-zx1-slope | not_reproduced | The notebook marks this blocked, but its own criterion can be evaluated. The KO ZX1 slope has p = 0.20–0.52 in all 4 readings. Neither weight is within tolerance: KO -0.55 to -3.1 against -0.64, WT -3.8 to -7.7 against -1.41 (cell 35). |
| fig5-contralateral-zx1-increases | blocked (data_missing) | Confirmed against the API: 30 files, all `behavior+image+ophys` two-photon/pupil sessions. variableMeasured lists only TwoPhotonSeries, PupilTracking and related items. No asset metadata mentions widefield imaging or a cannula, and no session label points to a Fig. 5 analysis. |
| fig5-ipsilateral-zx1-reduces | blocked (data_missing) | Same as above. |
| fig5c-no-dye-in-other-hemisphere | blocked (data_missing) | Same as above. The two-photon red channel, if present, is ipsilateral to the injection, so it does not test this claim. |
| fig6a-baseline-pd-drift | partially_reproduced | Both slopes are positive with p < 1e-15. The ZX1 slopes (0.12–0.19) lie within the paper's ZX1 CI. But the ACSF slope is 0.326 (CI 0.28–0.37), above the paper's ACSF CI, and it overlaps no ZX1 CI (cell 38). The criterion has no partial outcome; read strictly, this is not_reproduced. |
| fig6b-acsf-contrast-effect | not_reproduced | The contrast slope is not significant in any reading: p = 0.07 for (a), 0.27–0.83 for (b). In reading (b), the within-ACSF HIGH−LOW contrast has p = 0.37 (cell 40). Only reading (b) has a row count (2604) that matches the df. |
| fig6c-no-baseline-evoked-correlation | reproduced | Two readings match the count: B all (n = 262, p = 0.072) and the pupilBaseline_vs_evoked label, DRC CTRL (n = 222, p = 0.66). They agree (cell 42). This is fragile: C CTRL misses the count by one trial (215) and has p = 0.011. |
| methods-baseline-evoked-correlation | partially_reproduced | Only the label reading, DRC all, matches both counts (598 and 379). There r_all = -0.218, p = 7e-8, which is outside -0.35±0.035, while the correlation below 50% is not significant (p = 0.20) (cell 43). Using the claims file's readings only, none match both counts and they disagree, which would give methods_underspecified. |
| fig6d-ko-reduced-high-contrast | reproduced | tPoly1 × genotype has b = -6.5 (KO below WT), p = 0.006, under both codings. Rows: 3024 against about 3870 (cell 45). |
| discussion-zx1-wt-like-ko | reproduced | Peak rise is 10.4 for WT after ZX1 and 10.8 for KO under both readings, all within 10±2.5 (cell 47). The test cannot discriminate, though: WT CTRL HIGH (11.9) and both LOW sets also pass. |

**B. Problems**

1. **[affects a conclusion]** Cell 35 / notebook table: fig4f-ko-zx1-slope is marked blocked because "it depends on the claim above". Its criterion stands on its own, and every reading fails it, so it is not_reproduced.
2. **[affects a conclusion]** `clean_pupil` / cell 6: the main cleaning still leaves an artifact maximum for AA0319 (max 332.7, median 28) and probably AA0334 (162 against 26). The notebook does not flag either. As a result every trial of AA0319, and most of AA0334, falls below 50% of the animal max with a compressed baseline PD. These mice are in group B, the drift readings and the pupilBaseline_vs_evoked readings, and AA0334 is in group C. This affects fig6c and methods-corr, where baseline PD itself is the variable, and the trial selection for Fig. 2 (B), Fig. 4 WT and fig6d.
3. **[affects a conclusion]** Cells 42–43: the readings for fig6c and methods-corr are chosen by trial counts. Those counts depend on the author's cleaning rules: the Hampel filter is not in the paper, and trials with more than 50% missing frames are dropped. Under the single-pass cleaning, 1447 trials fall below 50% against 1179 under the main cleaning. The correlations were not re-run under the single pass. C CTRL misses the 240 tolerance by one trial and gives a significant correlation.
4. **[does not affect a conclusion]** `gca` / cells 31, 33, 45: several MixedLM fits are degenerate, and `warnings.filterwarnings("ignore")` hides the warnings. The cell means of the full-factorial fits omit an intercept of about 0 (cell 33: LOW CTRL = 1.5e-15). The fig6d genotype intercept is -52.5 with p = 1. I reproduced this behaviour on synthetic data with a between-subject factor: statsmodels gives p = 1 and warns of a singular covariance. Within-subject terms and pairwise differences look stable across readings (contrast b 1.021 against 1.018), but random-effect variances are never reported.
5. **[does not affect a conclusion]** Cell 4: group A comes from a file label that covers 10 mice (4F, 6M, including ZnT3-WT AA0335). The paper has 8 C57BL6/J mice. No C57-only variant was run. The Fig. 1 p-values are far from the threshold, but fig1i's interaction p (0.03–0.04 in some readings) is not.
6. **[does not affect a conclusion]** Cell 26: group B is inferred as mice with CGC trials before and after ZX1. That gives 12 mice, including 2 ZnT3-KO and 4 ZnT3-WT, while the paper has 14 C57BL6/J. No C57-only variant was run. The cell counts never reach 520. The effect (p ~1e-10) is too strong for this to change the outcome.
7. **[does not affect a conclusion]** Cell 28: Fig. 3 runs only the "SD over time" inclusion readings, not the "SD across trials" ones. fig3c fails at p ≤ 0.003 in the all-trials readings regardless.
8. **[does not affect a conclusion]** `load_file` / `trial_kind`: a DRC trial's contrast is taken as that of its first 10 s block. The files hold LOW→HIGH and HIGH→LOW switches that the paper never describes. The assumption is stated and reasonable for 0–2 s and 0–8 s windows. The notebook never checks stimDelay = 10 for DRC trials, or whether block order is balanced across contrasts.
9. **[does not affect a conclusion]** Cell 42: dead loop code (`for kind in ks + ...: kk = ...`). Readings B-all and the files' label were added beyond the claims file's list, and the notebook does not say so.
10. **[does not affect a conclusion]** Claims-file issue, reported only: the criterion for discussion-zx1-wt-like-ko accepts every condition tested, including WT CTRL HIGH. It therefore cannot show that ZX1 makes WT responses resemble KO.

Checks that passed:
- `orth_poly` matches R's `poly()` (first row -0.36038, 0.42286; orthonormal).
- `pd_bin` edges are correct.
- `clean_pupil` removes isolated and 12-frame spikes and keeps real dilations.
- The Tukey p uses `studentized_range` with √2·|t|, 4 groups: correct.
- The Pearson reliability code is correct.
- The ANOVA uses Type II sums of squares. The interaction F is the same under Type III.
- The clock check (cell 8) puts the tone response at 2.0 s.

**C. What I could not check**

- **Residual artifacts:** a per-animal list of the top 5 cleaned pupil values, against the per-trial median, would show whether more animals than AA0319/AA0334 are affected.
- **Single-pass variant:** cells 38, 42, 43 and 45 (fig6a, fig6c, methods-corr, fig6d) and Fig. 1 were not re-run under single-pass cleaning, or with AA0319 and AA0334 excluded.
- **GCA fits:** random-intercept variances and the converged/boundary status of every fit, plus an lmer/Satterthwaite fit to set against the Wald z.
- **DRC trial structure:** a crosstab of DRC trials by stimDelay and by block order (first block LOW or HIGH), by group.
- **Fig. 1 cohort:** results restricted to the C57BL6/J mice of group A, to match the paper's 8.
- **Fig. 2e cohort:** results for group B restricted to C57BL6/J mice.
- **FRA inclusion reading:** the claim that mapping trials exist for only one group A mouse could not be verified from the outputs. A per-subject count of mapping trials would settle it.
