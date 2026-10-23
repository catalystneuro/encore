I wrote `claims/000688/10.1016-j.neuron.2018.09.030.yaml`, and the quote checker passes with no problems. Nothing the claims needed was missing, so I wrote the claims.

**Text read:** the accepted author manuscript in PubMed Central (PMC6250582), not the version of record. That covers the main text, legends, STAR Methods and all eight supplement files: files 1 to 7 are the main figures as images, and file 8 holds Figures S1 to S7 with their legends. I opened the PDFs only to read p-values and asterisks printed inside panels (Figures 3E, 4D, 5B, 6C/E, S5F, S6D/E, S7A/D/E). The paper links no code ("may be shared upon reasonable request"), so every method comes from the Methods, legends or Results.

**Claims:**
- **Count:** 28 claims, all 28 with a criterion and 27 with a quote. The one without (per-monkey asterisks in Figure S6D/E) has an `inferred` note.
- **Statistics:** 29 entries across 12 claims.
- **Expected values:** 5 claims. These are neuron counts, GLM cell counts, the dimensionality medians (8.5 and 14), the covariance r values (0.85 and 0.93) and the 35 ms null-leads-potent lag.
- **Data:** every claim uses `dataset`. Whether dandiset 000688 holds the curl field and rotation sessions is for the author to find.

**Details the paper leaves open, with the readings named** (listed as O1 to O10 in the opening comment):
- **O1, Early and Late blocks in Force/Rotation:** Early is the first 8 trials. Late is trials 66 to 73 or 70 to 77. Trials are counted over reward trials only or over all trials.
- **O2, Late Washout block:** Washout trials 21 to 28, 31 to 38 or 41 to 48.
- **O3, part of the trial used for PCA and the GLMs:** target onset to target acquisition, or the whole trial.
- **O4, the 100 ms Gaussian kernel:** read as SD or as full width at half maximum.
- **O5, unit of the model-error t-test:** pooled single-trial values, or one mean per neuron (with a one-sample test against zero as a variant).
- **O6, raised-cosine widths and the 150 ms shift:** standard choices, named as such.
- **O7, subspace rows:** the Methods swap N and R. I read the first 8 rows of V' as potent and the last 8 as null; W is fit by least squares.
- **O8, bootstrap unit:** time bins or trials.
- **O9, dimensionality threshold:** the Results wording (eigenvalues above the noise) or the Methods wording (95% of the variance left after the noise).
- **O10, movement onset:** speed crossing 10%, 20% or 30% of peak.
- **Per-claim open points:** the Figure 6E reference point, windows (read off the figure bars), blocks and test (the test is not named); the CCA time resolution; whether the covariance diagonal is included; and the subsample size for the Baseline-split covariance comparison.
- **Wording claims with no test in the paper:** where the paper only says "similar", "resembled" or "paralleled" (behavior, covariance, Figure 4C time course, Figures S4C, S7E), I wrote thresholds myself and marked each as a deviation.

**Gaps and inconsistencies in the paper:**
- **Session counts:** the Figure 2C and Figure 7 legends show 7 curl field and 5 rotation sessions, but the Methods count 9 and 7.
- **Figure S5F:** the legend calls Null-M1 significant at p = 0.04, above the paper's own 0.01 threshold. That claim reports the outcome at both 0.05 and 0.01.
- **Figure lettering:** the Results' panel letters disagree with the legends (3E/F/G, 4E against 4D, two panels "d" in Figure 6). Each source gives both.
- **No code:** without it, none of the open details above can be settled.
