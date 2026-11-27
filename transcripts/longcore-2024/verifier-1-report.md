**A. Outcomes**

None of the 13 claims in the claims file is treated as blocked. I checked the Dryad API file list for version 300765: the four SHA-256 values match `alan.SHA256`, and version 300765 is the only version listed.

| Claim | Outcome | Reason |
|---|---|---|
| table1-suppression-0p5-and-above | reproduced | Cell 11: the mean is above 0 at all 8 named treatments. The margins are thin, though: 0.5 lx/1950 K is 0.79 (t-test p=0.84) and 0.5 lx/3000 K is 2.98 (p=0.49). The 50 lx means (90.44 at 3000 K, 53.73 at 1750 K) match the abstract's 91% and 53%. |
| table1-increase-0p01 | reproduced | Cell 13: the mean is below 0 at all 4 named treatments (-12.32, -4.71, -3.04, -2.66), with n=14 or 15, not 16. The 0.01 lx values match the abstract's 12.3% and 3%. |
| tukey-illuminance-within-cct | not_reproduced | Cell 15, reading (a): at 1950 K and 3000 K, 50 lx also differs from every lower illuminance, and at 3000 K so does 5 lx. Reading (b): CCT pairs differ at 5 lx as well as at 50 lx, and at 50 lx it is 3000 K, not 1750 K, that differs from both others. The single-family variant (cell 16) does not rescue either reading. |
| cct-0p01-not-significant | reproduced | Cell 18: no Tukey pair differs at 0.01 lx (smallest p-adj 0.51). The mean increase is 12.32 at 1750 K against 3.04 at 3000 K. |
| glm-illuminance-cct-interaction | partially_reproduced | Cell 21: no reading meets every bound. The interaction p is at least 0.0063 in every reading (the paper reports <0.002). With identity link, lux, centered: whole model 1.6e-43, CCT 2e-6, illuminance 6e-45. All three terms have p<0.05 in the 8 identity-link readings. |
| effect-size-illuminance-over-cct | reproduced | Cell 23: identity-link ratios are 3.10 to 3.84, all at least 2; reading (b) in lux gives 3.72 (the abstract says 3.6). Only log-link reading (a) is below 2 (0.80). |
| cct-effect-grows-with-intensity | not_reproduced | Cell 25: the raw CCT spread at 0.01 lx (9.28) is larger than at 0.5 lx (5.64), so the criterion's "smallest at 0.01 lx" fails, although the interaction is significant (p=0.0063). The GLM-predicted spreads do grow monotonically, but with a linear interaction term that follows almost automatically, so I give it little weight. |
| lower-cct-less-suppression | reproduced | Cell 27: the 1750 K mean is below the 3000 K mean at 0.5, 5 and 50 lx (by 5.64, 23.87 and 36.71). |
| aicc-individual-sex | reproduced | Cell 29, identity link, lux: 1612.30 < 1628.26 < 1643.90. The differences are 15.64 (expected 15.7±1.6) and 15.96 (expected 16.5±1.7). The absolute values are about 4 above the paper's but within tolerance. |
| sex-males-less-suppressed | reproduced | Cell 31, identity link, lux: the sex term has LR p=2.4e-5 and Wald p=2.2e-5, and the F parameter is +6.32, so males are less suppressed. Under the log link p is 0.003 to 0.007, which would only be partial. |
| sex-predicted-suppression | reproduced | Cell 33, identity link, lux: predictions are -10.90, 1.75, 85.57 and 98.22, all four within tolerance. The 95% CIs (-17.7 to -4.1; 75.2 to 95.9; 87.9 to 108.6) are close to the paper's. |
| individual-variation | reproduced | Cell 35, identity link, lux: the extremes are -27.86 (6FC2, P6; CI -38.0 to -17.7) and +21.46 (6FC1, P2; CI 7.3 to 35.7). The paper gives 27.9 (18.3 to 37.4) and 21.5 (8.1 to 34.8). |
| cfos-no-cct-difference | reproduced | Cell 37: t(10)=0.9409, p=0.3689, identical to the paper. The means are 123.74 and 113.40. |

**B. Problems**

1. [does not affect a conclusion] Claims file, cfos-no-cct-difference. The paper's "113.4±8.22 s.d." is the s.e.m.: the data s.d. is 20.13 and the s.e.m. is 8.22 (cell 38). The claims file's remark that the paper's means and s.d. give t of about 1.28, and its 8.22 tolerance on the 3000 K mean, both rest on that error in the paper. The notebook finds it but never says that it changes the claims file's reasoning.
2. [does not affect a conclusion] Claims file, opening comment (iii). The abstract says "Multiple linear regression confirmed the influence…". Together with how closely the identity-link reading matches the paper's AICc differences, CIs and mouse effects, that is strong evidence the paper's model was effectively identity-link. The claims file and the notebook keep the log link as the primary, Methods-stated reading and do not note this.
3. [does not affect a conclusion] Claims file, cct-effect-grows-with-intensity. The primary measure (raw spread of the CCT means) is the claims author's own choice. The paper's sentence follows the GLM result, so it may refer to the model. The two disagree here: raw spreads fail, GLM spreads pass. I kept the criterion as written.
4. [does not affect a conclusion] `Fit` / `fit`, cells 20, 29 and 33 (log link). The negative responses push the log-link mean toward 0 at low lux and the parameters drift without bound. Symptoms: Wald p=0.89 for illuminance against LR p=4e-19 (cell 20), and a 95% CI upper bound of 1e8 at 0.01 lx (cell 33). Cell 29 still prints "All fits converged: True". The log-link Wald numbers are meaningless and the notebook does not say so. No outcome rests on them.
5. [does not affect a conclusion] Cells 3, 6 and 11 to 13. Nine of 192 values are missing (6FC1, P2 at 0.01 and 0.5 lx; 6FC2, P8 at 0.01 lx), while the paper gives n=16 per treatment. The notebook reports this. The criteria's "mean over the 16 mice" therefore runs over 14 or 15 mice at the 0.01 and 0.5 lx treatments. The most suppressed mouse (6FC1, P2) is the one missing six low-lux treatments.
6. [does not affect a conclusion] Cells 11 and 13. Whether a mean counts as a "reduction" or an "increase" is judged by its sign alone, as the criterion says. At 0.5 lx, 0.01 lx/3000 K (median 0.03, 7 of 14 mice below zero) and 0.5 lx/1750 K, none of these means is distinguishable from zero. That fragility belongs in the conclusion.
7. [does not affect a conclusion] Cell 31. The GLM treats 183 mouse-by-treatment rows as independent. On per-mouse means, the sex difference has Mann-Whitney p=0.083. This is the paper's method, but it explains why the GLM's p<0.0001 for sex is so strong.

Helper check: on synthetic data, `fit`, `design` and `effect_codes` match the statsmodels GLM (both links) to 1e-11 in coefficients and standard errors. Log-likelihood and AICc agree for the identity link, and `effect_codes` gives correct sum-to-zero coding. All numbers in the notebook come from the staged Dryad files. I found no data from outside the dataset and no hard-coded results apart from the paper values used for comparison.

**C. What I could not check**

- The interaction p under a GLM that also includes sex or mouse ID. The paper's p<0.002 may come from one of those models. Adding to cell 20 the interaction LR and Wald p from the sex and mouse models would settle whether the GLM claim fails only because of the choice of model.
- Whether JMP's GLM personality centers the crossed continuous term. This matters only for the CCT main-effect p. Both variants are shown and both have p<0.05 under the identity link, so the outcome does not change.
- The source of the roughly 4-point AICc offset. Rerunning cell 29 at n=192, or with JMP's exact AICc parameter count, would show it.
- Why 9 values are missing. The README does not say, and only the raw wheel counts (not deposited) would show whether a mouse with no prior-day activity was dropped.
- Table 1 cells. The notebook could print the four abstract values next to cell 11 so a reader sees they match. I checked them by hand and they match.
