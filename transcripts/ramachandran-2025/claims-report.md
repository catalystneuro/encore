I wrote `claims/000945/10.1088-1741-2552-adbb1f.yaml`. The quote checker reports 22 claims, 22 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (J Neural Eng 22(2) 026022, PMC11920894), as served by Europe PMC. It has the main text, Methods, figure legends and Discussion. There was no PDF and no supplement. The supplement holds the headpiece, surgery, training and beam-scan details and Supplementary Table 1 (ISPTA values). No claim rests on it, because the analysis methods and the ISPTA of each PRF condition are in the main text, so I went ahead. The paper links no code (only "custom code" in MATLAB with FieldTrip), so I read no code.

**Claims:** 22, all with quotes. 10 carry statistics (Kruskal-Wallis with Bonferroni-corrected post hoc Wilcoxon, two-way ANOVA, and the rank-sum test on latencies). All 22 have criteria, and 2 have expected values: the Fig 3B unit counts (28 FSU, 32 RSU, 60 in total) and the latencies (0.24 ± 0.08 s anesthetized, 0.51 ± 0.14 s awake). The claims cover cell-type sorting, the PRF and DC effects on RSU and FSU in the time-locked and delayed windows, both two-way ANOVA anesthesia effects, the batch of five rats, the response curves against ISPTA, and the sham.

**Details the paper leaves open, and the readings named:**
- **Excluded units:** "visibly fluctuating" baselines and movement periods were removed by hand. E1: no exclusion. E2: use the dataset's marks, if it has any.
- **Cell type:** K0 uses the paper's labels if the dataset has them. Otherwise k-means per animal (K1) or over all units pooled (K2). The paper's hand sorting of unclear units by spike rate has no rule.
- **Trials:** 500 after cutting the first 5 (T1, from the Methods) or all 505 (T2, from the legends).
- **Groups in the Kruskal-Wallis:** the parameter levels alone (G1) or with sham added (G2). The significance level is never stated; I used corrected 0.05.
- **Two-way ANOVA:** with interaction, type II (A1), or main effects only (A2).
- **Latency:**
  - What the SEM is taken over: the baseline bins (S1) or the trials (S2).
  - Which bin may come first after 67 ms: D1 or D2.
  - Whether a bin's time is its start or its centre: L1 or L2.
  - Which sessions: the PRF series only (Q1) or every on-target 1500 Hz session (Q2).
  - Whether "±" is an SD or an SEM. I used it as the tolerance.
- **Fig 3B example:** the animal is not named, nor whether the count is from one session or all of its sessions (R1 or R2).
- **Delayed RSU peak (Fig 5E):** whether 1500 and 3000 Hz must each beat every other level (strict) or only be the two highest means (R2).
- **Fig 6A–D:** the text does not name the cell type. The claim is judged on time-locked RSU, and the other panels are shown as variants.

**Missing from the paper:**
- **Sham claim (Discussion):** the paper names no test of sham against baseline. Its criterion says this is open and names no reading.
- **Fig 4 time-locked RSU response:** there is no group test of it. It is judged by the paper's own comparison with sham.
- **Fig 4H "two peaks" and Fig 6 "almost linearly":** the paper gives no test or threshold for either. They are shown but do not decide the outcome.
- **Contradictions inside the paper:**
  - The low PRF of the five-rat batch is 30 Hz in the Methods and 300 Hz in the next sentences and the Results. The author takes the PRF the dataset records.
  - Fig 7A: the Results say 6% DC is lower than 60%; the legend adds lower than 30%.
  - Fig 7C: the legend says "all DCs" differ, which the Results do not state.
  - Fig 6A–D: the legend says the panels are 0–67 ms but also that they repeat Fig 5's delayed panels.
  - Latency: the Results give p < 0.001, the legend p < 0.0001.

  In each case the claim follows the Results text and the other version is reported without deciding the outcome.
