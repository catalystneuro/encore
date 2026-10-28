I wrote `claims/000233/10.1038-s41586-021-03811-w.yaml`. The quote checker passes it with no problems (34 claims, 34 quotes, 6 statistical values). Nothing is committed.

**Text read.** I used the accepted author manuscript from PubMed Central (PMC9214835, NIHMS1804409): main text, Methods, Data and Code availability, and the legends of Figs 1–4 and Extended Data Figs 1–10. I also read the Supplementary Information PDF, which has Supplementary Table 1 (the list of animals) and the Supplementary Discussion. No PDF of the main article was supplied, so I could not see any figure.

**Code.** The paper links only https://github.com/buzsakilab/buzcode; I read commit e615663b2b100782d1f378580f6d7aaa35c12937. It holds the ripple detector `bz_FindRipples.m`, the sleep scorer and a circular-shuffle utility. It has no code for the glucose analysis, the cross-correlograms, the regression models or the DREADD analysis. The detector's default settings differ from the Methods (130–200 Hz against 120–200 Hz, and different duration limits), so I followed the Methods.

**Counts.**
- **Claims:** 34, all with quotes, none marked `inferred`.
- **Statistics:** 5 claims carry them (6 values):
  - Student's t-test P < 1e-24 and Rayleigh test P < 1e-18 (Extended Data Fig. 5)
  - minimum P = 0.53 for hour of day
  - opto dose-response P < 0.01, test not named
  - Kolmogorov–Smirnov P = 0.00015
  - histology correlations P < 0.05
- **Criteria:** all 34 claims have one; 14 also carry expected values.
- **Data:** all claims use the dataset except the histology-score claim, which is `with_inputs` because the scores are printed only in the Extended Data Fig. 10e table.

**Details the paper leaves open, with the readings named:**
- **Glucose change (delta current):** (a) the difference between successive raw readings, or (b) the same after high-pass filtering; the filter cutoff is not given.
- **Correlation type:** Pearson or Spearman.
- **Unit of analysis:** one cross-correlogram per rat over all its recording, or one per session averaged per rat.
- **Lag search range:** 0 to +100 min, or ±100 min.
- **Which rats make up n = 30:** every rat with ripples and glucose recorded together, or only the ripple-and-glucose cohort. No cohort in the Methods has 30 rats.
- **Fig. 2g clustering threshold:** more than 30 SPW-Rs per minute, or more than 30 per 5-min epoch. "Isolated" is not defined; I chose 1 to 5 per epoch.
- **Influence of SPW-R features:** the bin width (deciles or 5-percentile bins); the influence measure itself is not defined, so I chose the range across bins.
- **Phase dispersion (Fig. 2h):** the band used to extract phase, 15–75 min or 15–90 min.
- **The 63% effect size:** three readings of what is measured (trough depth, minimum from 0 to +30 min, or the mean at +10 min).
- **The test behind opto "P < 0.01":** a signed-rank test on per-rat R, or a pooled correlation.
- **What the Fig. 3f histogram holds:** 8 per-rat values against 800 shuffled values, or repeated subsamples.
- **Dorsal and ventral comparison:** paired or unpaired per-day values.
- **DREADD measure:** correlation at +10 min, or integrated over +5 to +20 min.
- **DREADD test units:** unpaired per-day values, or paired per-rat means.
- **Fig. 4e sliding window:** its time read at the window's centre or its start.

**Other choices I made where the paper gives no method:**
- the comodulogram filters
- the GLM family and ICA algorithm
- theta cycle detection, which is given only in ref. 26
- tests for several qualitative claims (circadian and meal effects, sensor decay, stability across days, the stimulation protocol, decoupling from brain state)

**Missing from the paper:**
- The main figures were not available, so the subregions marked significant in Extended Data Fig. 10e are unknown.
- The ± spreads are not said to be s.d. or s.e.m.
- Animal counts disagree between the Methods, Supplementary Table 1 and the legends (PPC 6 against 5 rats; DREADD 6+7 against 7+3+8; dorsal/ventral 3 against 4).
- The Supplementary Discussion cites some panels under old figure numbers.
