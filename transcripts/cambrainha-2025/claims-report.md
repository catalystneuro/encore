I wrote `claims/cambrainha-2025.yaml`. The quote checker passes it: 18 claims, 18 quotes, 12 statistical values, 0 problems.

**Text read.** The paper file is arXiv 2410.23508 version 2, which stands in for the PRX Life version of record. It has the main text, the Methods appendix (sections 1 to 6), and the Supplemental Material (sections I to VIII, Figures S1 to S8). Nothing the claims need is missing. I opened PDF pages only to read Figures 3, 4, S1, S5, S7 and S8. The paper links no code, so no code was read.

**Claims.** All 18 have a quote and all are `data: dataset`. They cover:
- **Session selection:** 62 sessions from 44 mice.
- **Kurtosis:** spread compared with the surrogate data (Fig. 3A).
- **Performance:** scaling windows have a higher hit rate than no-scaling and trial-shuffled windows, and it rises with the threshold (Fig. 3C). The relative gain reaches 24% ± 3% (Fig. 3D).
- **Robustness checks:** 10-s and 60-s windows (S1); stricter unit selection, 43 sessions (S2); the two halves of the active phase (S7, S8).
- **Phases:** windows above threshold are ordered active > passive > non-natural images (Fig. 4A).
- **Exponents:** values for each of the three phases, the active-phase deviation from trivial values and the trend across phases, and stability with the threshold (S3).
- **Other supplement findings:** initial kurtosis is a poor predictor of final kurtosis (S4); firing-rate order (S5A); a non-monotonic hit rate against firing rate (S5C).

**Statistics.** There are 12 entries, all Mann-Whitney U p-values between phases for the exponents, from Supplement V. One is a misprint: the last entry is printed as "μ1 vs μ2" and I recorded it as μ1 vs μ3, with a note saying so.

**Criteria.** 17 claims have a criterion; the 24% gain uses the paper's ±3% and the exponents use the paper's SDs as tolerances. Where the paper gives no measure, the criterion says the threshold is the file's own choice. That applies to S4 (|Spearman| < 0.3), S3 (at least 10 sessions) and the monotonic rise in Fig. 3C.

**Details the paper leaves open, with the readings named (O1 to O11):**
- **O1, units:**
  - Main analysis: all V1 units, or V1 units after the dataset's default quality filters; ">128" and "≥128" are both run.
  - The 43-session variant's "more strict sorting criteria" are not named: the default quality filters, or units the sorter labelled good.
- **O2, CV > 5 exclusion:** the CV of the population count, the mean of the per-unit CVs, or the CV of all unit-bin counts pooled.
- **O3, kurtosis:** pooled over units and bins, or the mean of per-unit kurtoses. Equation 5 also has a misprint (φi inside the sum), which I read as φj.
- **O4, non-natural images phase:** with or without the gray-screen period.
- **O5, trials:** auto-rewarded trials left out or counted as hits.
- **O6, maximum surrogate kurtosis:** taken over the active phase only, or over all phases.
- **O7, threshold grid and range:** a standard choice, step 0.05 over the plotted range.
- **O8, bootstrap:** recompute the pooled hit rate, or average the windows' own hit rates; how the 3% error of the gain is propagated is not said.
- **O9, real-space method:**
  - P_silence: −log of the mean, or the mean of −log.
  - Range of cluster sizes K fitted: up to the largest K with two clusters, or up to N/16.
  - Fit for μ: pooled over K ≥ 16, or a single K = 64.
- **O10, session exponents:** a fit per window then averaged, or one fit per session.
- **O11, test unit:** session values, which the reported p-values fit, or pooled window values as a variant.

Neither the Methods nor the text says which phase Figs. 3A and S4 use; each claim reads it as the active phase and runs all phases pooled as a variant.

**Missing from the paper:** besides the unnamed strict sorting criteria in O1, the paper names no test for "deviate significantly from trivial values" (Discussion). The criterion names two readings: comparison with the surrogate exponents, or a Wilcoxon signed-rank test against 1.

I did not commit anything.
