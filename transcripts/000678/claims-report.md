I've written `claims/000678/10.1016-j.celrep.2024.113709.yaml`. The quote checker reports 28 claims, 28 quotes, 37 statistical values and 0 problems. Nothing is committed.

**Text read**
- The accepted author manuscript of the Cell Reports version of record (PMC11016285, NIHMS1970871): Results, Discussion, STAR Methods and figure legends.
- Its supplement, the legends of Figures S1 to S8, as extracted text.
- The bioRxiv preprint (v2) is also under `paper/`; I did not use it.
- The main-text PDF is not under `paper/`, so I never saw the main figures. The supplement PDF could not be rendered either (pdftoppm, from poppler-utils, is not installed). Where a significance mark exists only in a figure (Figures 4A, 4B, 4D), I took it from the figure code that draws it, and the file says so.

**Code read**
- Zenodo doi:10.5281/zenodo.10306018 (`hulsey2023.zip`): the processing scripts 1 to 7, the scripts for every figure, and the paper's copies of uobrainflex and ssm.
- The same scripts are in github.com/sjara/uobrainflex at commit ef48985.
- Most p-values in the paper are not computed in the code.

**Claims**
- 28 claims, all with quotes; none needed `inferred`.
- 17 claims carry statistics (37 entries), 15 have expected values, and all 28 have criteria.
- All use the dataset itself; the paper names no outside data.
- The archive describes 391 sessions where the paper includes 381. The `cohort-inclusion` claim checks this.

**Details the paper leaves open, and the readings named**
- **O1, number of states:** the larger of the MLE and MAP plateaus (Figure S2), or the MLE plateau alone (the code).
- **O2, the paper's own state labels:** if the dataset holds them, they are run as an extra reading beside the refit model.
- **O3, which sessions feed the per-state means** (distance from optimal pupil, raw face energy, raw locomotion): sessions with more than 10 optimal-state trials, or all sessions.
- **O4, Figure 2D test:** the Results say signed-rank and the legend says rank-sum. Signed-rank is run (paired mice; 2.4 × 10⁻⁴ is its smallest exact p for 13 mice) and rank-sum is shown.
- **O5, bins for the r² of face energy, locomotion and movement index:** the code's plotting bins, or 50 equal-width bins per mouse.
- **Within single claims:**
  - **Inverted U per mouse:** the fit's maximum lies inside the data range, or the quadratic term is negative.
  - **"Nearly all":** at least 12 of 13 mice, or at least 11.
  - **Stationary trials:** speed exactly 0, or below 0.02 m/s.
  - **Average dwell of 37 and about 15 trials:** mean of per-mouse medians, mean of per-mouse means, or all epochs pooled.
  - **"10.8% improvement":** percentage points, or relative to the one-state model.
  - **Classifier significance:** z > 1.96, z > 1.645, or above the 95th percentile of the null.
  - **Figure S7 comparison:** S7A or S7B, on accuracy or on z-score.
  - **Figure 5C comparison:** accuracy or z-score.
  - **Distractor response rate:** pooled trials, or mean over sessions.
  - **Evoked pupil response:** peak change, or mean change over 0 to 4 s.
  - **"Weak" correlation:** |r| below 0.1, or below 0.2.
  - **"Highly correlated":** r above 0.7, or above 0.5.
  - **"Across mice" for regression weights:** Wilcoxon test against zero, or the sign of the median.
  - These thresholds come from no text or code: the paper gives none, and I proposed them. The checker should look at them.

**Where the code differs from the Methods (each named as a variant)**
- The classifier code uses 8 features, adding the movement index and its SD; the Methods say six.
- In `5_decoding.py`, the "movement index only" condition also leaves the pupil value unshuffled, unlike the Figure 5C legend.
- The code's null shuffles all training features; the Methods say class labels are permuted.
- The Results and the Figure S7 legend print different p-values (0.106 against 0.14, and 3.9 × 10⁻³ against 0.004). Both are recorded.

**Missing from the paper**
- No code computes the r² comparisons (0.72, 0.49, 0.44, 0.63), the per-state distance from optimal pupil, or the raw face and locomotion means. Their methods rest on the Methods plus the nearest code.
- The disengaged SEMs are printed as 0.3 a.u. and 0.2 m/s, larger than the values themselves. I read them as misprints and used 10% tolerance.
- No significance threshold is given for the classifier, and no test for the shape claims (Figure 3E, Figure S8A).
- Training sessions before stage 5 and the 18 excluded mice are probably not in the dataset, so `training-duration` may not be testable.
