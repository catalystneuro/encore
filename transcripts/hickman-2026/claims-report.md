I wrote `claims/000774/10.1016-j.celrep.2026.117420.yaml`. The quote checker reports 42 claims, 42 quotes, 62 statistical values and 0 problems. Nothing is committed.

**Text read.** The NIH author manuscript of the version of record (PMC13404931, NIHMS2190715): main text, figure legends and STAR Methods, plus Document S1 (13 pages, legends of Figures S1 to S12).

**Missing from the paper.** Table S1, the second supplementary file, is not in the text. The paper points to it for "full model results". The Results and legends print the main statistics, so I wrote the claims anyway. Only the reaction-time claim (Fig S10E) lost its test entirely, and it names two possible tests instead.

**Code read.** `github.com/denmanlab/estim_populations` at commit c4aaa608. It was written for the preprint, so from the code's figure 6 onward its figure numbers run one ahead of the paper. It holds the notebooks, cached ZETA p-values, CCF coordinates and cached evoked-potential boundaries. It has no code for the Gaussian mixture of spike latencies, the 5 and 10 ms early windows, the high/low-state split, the stability flags or the FS/RS classifier.

**Claims.** 42 findings, all with quotes. 30 carry statistics, 32 have expected values, and all 42 have criteria. Nine are claims of absence, each judged on the paper's own test.

**Data.** The evoked-potential and saturation claims (Figs 1L, 2, 3, S1, S2) need the raw AP band, which the paper says is not in the NWB. The code's cached boundaries are named as an outside input for the author to judge. The behaviour claims (Fig 7, S10) use data the paper does not list as deposited; its code reads them from local CSV files.

**Details left open, with the readings named in each criterion:**
- **Trial selection:** only contacts in or near layer 5 (the Methods), or the first matching run (the code).
- **Modulation index window:** three versions.
  - Methods: 500 to 1000 ms, 5 ms bins.
  - Fig 6C legend: 0 to 500 ms, 5 ms bins.
  - Code: 0 to 500 ms, 10 ms bins. Only this one reproduces the printed magnitudes, because the code's measure (area under |MI|) scales with the number of bins.
- **Spatial-extent mixed model:** which interactions, and whether amplitude is numeric or categorical. The code has no mixed model at all; its OLS is a variant.
- **"One-way" or "linear" ANOVA (Figs 4I, 4J, 7G, 7I):** a categorical ANOVA, or the code's regression on numeric amplitude.
- **Responders inside the evoked potential (Fig 4F):** all responders, or RS only. The printed numbers match the code's RS-only count.
- **Proportion inside the evoked potential (Fig 4I):** each amplitude's own boundary or the 100 µA one, and relative or raw distance. The printed values are not in the code.
- **Amplitude clustering:** raw or max-scaled features.
- **Polarity clustering:** 99 units (legend) or 220 (code). The printed percentages match 220.
- **Centre-of-mass test (Fig 3H):** the Methods' centre of mass, or the code's sphere-centre shift.
- **Gaussian mixture:** 4 components fixed, or chosen by BIC.
- **Baseline for the 5 and 10 ms windows.**
- **High/low-state analysis:** which population is counted, DRP or nDRP, and all units or responders.
- **What the FS/RS early-firing KS test compares.**
- **Region groups:** HVA as the legend defines it (LM, AM, PM), or the code's text filter, which wrongly takes in dentate gyrus and superior colliculus.
- **Fig 6F:** the text and legend swap the two r values, so both peaks are tested.

Other discrepancies are recorded in the criteria:
- The code uses Welch's t-test where the text names Student's.
- It subtracts 15 saline channels, where the Methods say 20.
- It prints cumulative SDs for the spatial extents.
- A typo in its convex-hull code reuses a point from an earlier recording.
- Its anodal-vs-cathodal test effectively has 3 mice.

**Tolerances.** 10% by default. Where a legend states mean ± SEM over mice or recordings, I used the SEM. Where the ± is the spread across units, I kept 10% and said why.

**One test that cannot be matched:** the early-windows claim reports p < 0.001, which a Wilcoxon test over 9 recordings cannot reach (its smallest possible p is about 0.004). That claim is judged at p < 0.05 and the deviation is recorded.
