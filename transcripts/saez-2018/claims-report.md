I wrote `claims/saez-2018.yaml`: 28 claims, all 28 with quotes. All quotes pass `tools/claims_check.py` word for word. The checker still flags two values it could not find: p < 10^-6 (fig5) and p < 10^-4 (mixed effects). The extraction prints their minus signs as "10�6" and "10�4"; I read them in the text and they are correct as recorded.

**Text read:** the version of record (PyMuPDF extraction plus the PDF), with the main text, legends, STAR Methods (e1 to e3) and the full Supplemental Information (Figures S1 to S7, Tables S1 and S2). Nothing the claims need is missing. The paper links no code; its analysis was in custom MATLAB and R scripts, so no code was read.

**Statistics:** 13 entries in 10 claims. **Criteria:** 27 claims have one; `behavior-risk-neutral` and `methods-electrode-trial-counts` have expected values as well.

**One finding from Table S2:** the paper does not print its column sums, so I added them up. Averaged over the 16 current and past regressors, they reproduce the paper's 20.9% of encoding electrodes for HFA. So Table S2 is the 5-consecutive-window selection, and its sums are used as expected counts.

**Two places where the paper disagrees with itself:**
- **Win probability:** the Methods say a shown 2 means 20%; Table S1 and the worked example say 0.8, i.e. (10 − n)/10. I used the second and kept the first as a variant.
- **"Mean = 7.41 patients":** counting from Table S2 gives 7.75, and past risk appears in only 5 patients, against the text's "at least 6". The criterion names three readings and allows partial reproduction.

**Details left open, with the readings named:**
- **Baseline:** the 200 ms before each epoch's own event, or before game presentation for both epochs.
- **Risk:** p(1−p)x², or p(1−p).
- **Offer value:** read as win probability, with p·x as a variant.
- **Past regressors after a timeout:** drop the trial, or use the last non-timeout round.
- **Behavior summary (55.9%):** the mean of per-patient percentages, or pooled over trials. The ± is not named (SD or SEM).
- **Random-effects logit:** random intercept only, or intercept and slope. For the past-trial effects: one regressor at a time, with or without current win probability as a covariate.
- **Test against healthy participants and reaction-time t tests:** per win-probability level or slope comparison; pooled trials or paired by subject.
- **Past–current R² and collinearity R²:** which pairs of regressors, and whether pooled or averaged over patients.
- **Latency and duration in Figure 3:** three definitions (peak of mean %EV, first window above chance, per-electrode stretch).
- **Figure 5 duration:** how stretch length is counted (window count × 50 ms, plus 150 ms, or start to end), and which epoch it is taken from.
- **Figure 6:** what the t test is run over, and the undefined "Null regressor" line, read as the shuffled chance level.
- **KS test threshold (Figure S5D):** none printed; 0.05 used as a standard choice.
- **Mixed-effects models:** which time point, which regressors per model, and which electrodes.
- **"Similar" in Figure S6B:** rank correlation, or within 10 percentage points.
- **Anatomical gradients:** the threshold (Bonferroni or uncorrected), what "consistent" means, and Pearson or Spearman correlation.
- **Overlap sets:** stepwise selection or the 5-window selection. The denominator of 120 in the Figure S7 chi-square tests is unexplained (it is not 192 nor 160).
- **Example electrodes in Figure 2:** not identified.

**Data the claims need that the paper does not place in the dataset:**
- **Healthy participants:** the paper does not say their data were deposited. This affects the patient-versus-control comparison and half of the reaction-time claim.
- **Broadband field-potential signal:** the dataset description lists only HFA. This affects `hfa-more-than-fp` and `figs4b-power-at-buttonpress`.
- **Electrode coordinates and Brodmann labels:** also not listed in the description. This affects the four anatomy claims.

Whether the dataset holds these is the author's to find.
