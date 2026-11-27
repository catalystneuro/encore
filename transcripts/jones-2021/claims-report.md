I wrote `claims/jones-2021.yaml`. The quote checker passes it with no problems: 41 claims, 41 quotes, 160 statistical values. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC9069800): main text, STAR Methods and figure legends, plus the main supplement PDF (Figures S1 to S7, Tables S1 to S6). I did not read the version of record. I also read the paper's code: github.com/emilyasterjones/interneurons_modulate_drive, tag v1.0.0, commit 63b1acb (Zenodo 10.5281/zenodo.5618979).

**Missing.** Supplementary Table S7 (sex-stratified effects, an xlsx file) is not under `paper/`. Only one claim, `sex-stratified-effects`, needs it. That claim is written from the Results text and has no statistics. The rest of the paper's results do not depend on it.

**Counts.** 41 claims, all quoted, all with criteria; 37 have statistics and 11 have expected values. Most claims are LMM treatment and genotype effects from Figures 2 to 6 and S2 to S7. They share one method, "Method M", set out in the opening comment with each part cited to the Methods or code. Every claim also has its own criterion.

**Details the paper leaves open, with the readings named**
- **Log transform:** (a) only for features whose residuals are right-skewed, as the Methods say (main); (b) every feature, as the code does.
- **SWR threshold:** 3 SD in the Methods (main); the code counts SWRs at 5 SD for rate, length and chains (variant).
- **Holm-Bonferroni family:** 24 rest or 36 run comparisons, as the Methods define. When the whole family isn't computed, p < 0.05/24 or 0.05/36 counts as significant and p ≥ 0.05 as not.
- **SG z-scoring during SWRs:** the Methods z-score CNO sessions by the vehicle session of the day before (main); the code z-scores every session by its own mean and SD (variant).
- **Per-animal change in the correlation claims (Figures S2C-D, S4E):** difference of means, or difference of the LMM fitted responses.
- **Percent of SWRs longer than 100 ms:** denominator is valid SWRs or all detected events; values pooled over sessions or averaged per session.
- **Others:**
  - SWR frequency data points: one mean per SWR, or every interpeak value.
  - SW amplitude: one CA1-sr site, or every CA1-sr site.
  - Run coherence: per 1 s bin, or over all run periods.
  - Rest SG power measure: filtered envelope, or multitaper power.
  - Running speed: averaged over run periods, or over the whole session.
  - CA3 overlap average: over sessions, or pooled over events.
  - Sign of the input resistance change.

**Inconsistencies in the paper, noted in the claims**
- The text says SST+ suppression increased CA3 SWR rate, but the legend gives p = 0.77. It is a separate claim, judged as the text states it.
- The Results say input resistance decreased; the Figure S1F legend says it increased.
- Some cross-references point to the wrong item: "Table S3" should be S2, "Figure S3C–D" should be S2C-D, "S5D" should be S4D.
- Figure 5G's genotype difference has p = 0.95 in CA1, but the text says the effects were "detectably different".
- The Methods give the single-shank probe to cohort 3; the Results give it to cohort 1.

**Data a claim needs that may not be deposited.** The fast-ripple analysis needs signal above 300 Hz, while the deposit is described as 0–300 Hz LFP. Histology and the ex vivo slice recordings are not among the deposited data either.
