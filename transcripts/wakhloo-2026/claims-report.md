I wrote `claims/wakhloo-2026.yaml` and nothing is committed. The quote checker reports 27 claims, 27 quotes, 7 statistical values and 0 problems. The file has no em dashes, never uses "rather", and has no ": " inside plain scalars.

**Text read**
- **Paper:** the version of record (Nat Neurosci, published 4 February 2026), from the publisher's HTML. It has the main text, the legends of Figs. 1 to 7, the Methods, and the data and code statements.
- **No PDF:** no figure was seen.
- **Supplementary Information is missing.** That is SI sections 1 to 8, Supplementary Figs. 1 to 12 and Supplementary Tables 1 and 2. I went ahead anyway: every rat finding, with its test and P bound, is stated in the main text or Methods, and the Methods give the pipeline. Each claim that cites the supplement says so.
- **Code:** `awakhloo/population_geometry_optimal_coding` at commit 9674a6c. It fills in what the Methods leave open: the smoothing bandwidths, the speed definition, the task filtering, the 0-to-7 session coding of the mixed models, the Benjamini-Hochberg correction, the GLM grid and chosen basis, and the fact that Fig. 7e plots the theoretical error. Its `rat_stats.csv` holds the mixed-model coefficients and P values that the paper reports in Supplementary Table 2.

**Claims:** 27, all with quotes and all with criteria.
- **Testable on DANDI:000978:** 15 rat claims (Fig. 7, the mixed-effects models, the GLM D², and the SVC comparison for the PFC and CA1 part).
- **Outside the dataset:** 5 claims are `data: elsewhere` (the pose-network data from DeepLabCut, and the macaque data from Brain-Score).
- **Theory and simulation:** 7 claims, which the dataset cannot test.
- **Statistics:** 6 claims carry 7 entries. These are the mixed-effects quadratic and linear models (P < 10⁻⁵, > 0.05, < 0.01, < 10⁻³) and the macaque paired t-tests (P < 0.01, FDR). 4 claims have expected values. There is one absence claim: no non-monotonic trend in SSF, judged on the quadratic term at 0.05.

**Details left open, with the readings named**
- **Units per subset in CA1:** the Methods say 24 units; the code uses 19 for both areas. The Methods are the main reading and the code is a variant.
- **Error shown in Fig. 7e and used for R²:** the theoretical error (what the code plots) or the empirical one.
- **P bounds in the mixed models:** on raw P values or on the BH-adjusted ones.
- **Session coding:** 0 to 7 as in the code, or 1 to 8 as a variant. This changes the linear term.
- **Trend after session four:** session 8 against session 4, or a mixed-effects slope over sessions 4 to 8.
- **"Monotonically" for the task-relevant dimension:** rises from session 1 to 4 and from 1 to 8, or no fall between consecutive sessions.
- **D² standard deviation:** computed with ddof 0 or ddof 1, and with units later replaced by the null model counted at their own D² or at 0.
- **"Strong" SVC correlation:** a significant positive Pearson correlation, or r² of at least 0.5.
- **Readings I set myself where the paper gives no test.** Each is labelled as such in its criterion:
  - Fig. 7d and 7e: what counts as a decrease followed by a plateau.
  - Fig. 7f: what counts as good agreement between theory and the empirical error.
  - Fig. 7g, 7h and 7h–k: comparing session 1 with session 4, and reading "nearly every" as at least 3 of the 4 measures.

**Gaps a claim needed**
- **R² for CA1:** the Results give 0.48 and the Fig. 7 legend gives 0.49. The code printed 0.477, and both are within tolerance.
- **Macaque comparisons:** which pairs are significant is shown only in Fig. 5e–h and Supplementary Table 1, neither of which was read.
- **Proofs:** the proofs of Eqs. 1 and 2 are in the missing SI.
- **PFC fit and SVC values:** the poorer quadratic fit in PFC and the SVC correlation values are in Supplementary Figs. 12 and 3, which were not read.
