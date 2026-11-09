I wrote `claims/000579/10.1016-j.neuron.2022.05.012.yaml`. `tools/claims_check.py` reports 41 claims, 41 quotes, 45 statistical values and 0 problems. The file has no em dashes, no "rather", and no plain scalars containing ": ". Nothing was committed.

**Text read**
- **Version:** the PMC accepted author manuscript (PMC9357051), not the version of record. It includes the Results, figure legends and STAR Methods.
- **Supplement:** the one supplement file, with the legends of Figures S1 to S8.
- **No main-text PDF:** Figures 1 to 8 were read from their legends and the Results only.
- **Code:** `github.com/sytseng/GLM_Tensorflow` at commit 75a1314, the repository behind the paper's Zenodo link. It holds only the GLM fitting functions. Its `make_prior_matrix`, which groups the predictors for the penalty, is called but not included. The paper says its other analysis code is shared on request.

**Claims**
- 41 claims, all with quotes and none `inferred`.
- 19 claims carry statistics (45 entries), 14 carry expected values, and all 41 have criteria.
- All are `data: dataset`. The paper uses no outside data apart from the Allen CCF and field-sign maps it registers neurons to.
- They cover the behaviour and models (Fig 1, S1), photoinhibition (Fig 1L–M, S1M), dynamic choice (Fig 2, S2L), neuron counts and GLM fit (Fig 3I, S3), the encoding gradients (Fig 3M/O/Q, 4B/C/G/H, S4, S5), distributedness (Fig 5), location decoding and NMF (Fig 6), encoding correlations (Fig 7) and shattering dimensionality (Fig 8). Robustness checks are included: L2 regularization in place of group lasso, and a looser fit threshold.

**Details left open, with the readings named**
- **How the GLM's penalty strength (lambda) is chosen:**
  - (a) the minimum mean cross-validated deviance, as the Methods word it (main reading);
  - (b) the code's rule, the largest lambda within a number of standard errors of the minimum. The code does not give that number, so 1 is used (run as a variant).
  - The code's default lambda grid differs from the Methods; the Methods are followed.
- **Drift exclusion:** whether it is applied before or after the 93,881-neuron count is not said; both orders are shown.
- **Stem epoch edge:** bins wholly in the stem, or bins whose centre is in the stem.
- **LSTM accuracy SD:** taken over sessions or over mice, and on all sessions or only those above 0.65 correct.
- **Windows and bins:**
  - switch windows of 10 or 20 trials;
  - position grids of 11 or 20 bins;
  - strategy bins as 5 or 10 quantiles, or a Spearman correlation.
- **Population decoders:** the elastic-net strength (the minimum-deviance or the one-SE choice that MATLAB's `lassoglm` returns), and how groups of about 100 neurons are formed (k-means on positions, or equal-count tiles).
- **Location decoders:** the L2 strength (chosen by leave-one-mouse-out loss, or fixed at 1e-3).
- **Other choices:**
  - PCA standardization (centred only, or z-scored);
  - which neurons enter the epoch activity maps and the active-neuron pool;
  - whether "choice" means dynamic or reported choice in Fig 5 and Fig 8;
  - the epoch used for strategy in Fig 5;
  - scikit-learn default settings for `LogisticRegression`.
- **Choices the file sets itself**, because the paper gives none:
  - |r| < 0.2 as "near zero" for the encoding correlations;
  - 0.1 from 0.5 as "near chance" after a switch;
  - a standard lapse form for the reinforcement-learning model, whose formula is garbled in the text.

**Missing from the paper**
- **Exact conjunctions of Fig 8G:** they appear only in the figure; the Methods' list is used.
- **Photoinhibition sessions:** the 7 VGAT mice and 164 sessions may not be in the dandiset, whose title names imaging only. That is for the author to check.
- **Value conflict:** the L2 against group-lasso fit difference is printed as −0.0175 in the Methods and 0.018 in the S8D legend. The Methods' value is used.
- **Tests the paper does not report:** six claims (Fig 2C, 2F, 4H, S4P, the cue-biased running claim, and Fig 8C/D) report no test. They use the Methods' default, a two-tailed hierarchical bootstrap, which the criteria say.
