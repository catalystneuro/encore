I wrote `claims/payne-2020.yaml`, and the quote checker passes it: 31 claims, 25 quotes, 15 statistical values, 0 problems.

**Text read:** the version of record from Europe PMC (PMC7773906, JATS XML): main text, Methods, Table 1, figure legends and Discussion. The paper has no supplement and no PDF was supplied, so I read no figure pages. It links no code; its Data Availability says data come from the authors on request. No method detail is settled by code. I did not open any of the dataset's files.

**Claims:** 31 in all.
- **Quotes:** 25 have one. The 6 Table 1 values have an `inferred` note instead, because no sentence in the text states them.
- **Statistics:** 9 claims carry them. These are the Friedman tests (anaesthetised P = 0.039 and awake P = 0.039), Dunn's test (P = 0.034) and the six 95% CIs from Table 1.
- **Criteria:** all 31 claims have one.
- **Topics covered:**
  - ECAP latencies, conduction velocities and thresholds, anaesthetised and awake
  - electrode impedance and open circuits
  - colonic pressure
  - the Table 1 voiding values and their comparison with Wiedmann et al. (2020)
  - evoked voids (7 of 8 rats, 27 trials) and non-voiding contractions (6 of 8 rats)
  - the 8-week rats
  - ATF3, CGRP and synaptophysin staining
  - the c-Fos distribution, no difference between sides, and no lamina I activation
  - post-mortem findings

**Details the paper leaves open, with the readings named:**
- **Conduction distance:** 2.85 mm (pair centre to pair centre), 2.10 mm (E2 to E3) or 3.60 mm (E1 to E4).
- **Latency:** measured from pulse onset or pulse end, at 2 mA, at the lowest current where all three peaks pass threshold, or as the mean over currents above P3 threshold.
- **Threshold amplitude and step:** amplitude as peak to baseline or peak to trough; threshold at the 0.1 mA step or interpolated between steps. The printed values are not multiples of 100 µA.
- **Central value:** mean or median. The Results say "mean" but the Statistics section says median and IQR.
- **Awake Friedman test groups:** one test over all six groups, one test per population, or week as the factor.
- **Awake pooling:** both weeks pooled, rats averaged over weeks, or week 0 alone.
- **Dunn's P:** unadjusted or Bonferroni-adjusted.
- **Urodynamic definitions:** threshold pressure at contraction onset or at urine release; contraction duration from onset to return to baseline, or time above threshold. The 9-rat mean is taken over per-rat means or over all cycles pooled. HFPO centre frequency is the spectral peak or a count of oscillation peaks.
- **"Immediately followed by a void":** within 30 s (the window the Discussion uses), timed from train onset or train end.
- **"Very early" in the void cycle:** under half, or under a quarter, of the rat's inter-void interval.
- **c-Fos Welch tests with Hommel correction:** one test per region with segments summed, or one per region and segment. A paired test is shown as a variant.
- **Lamina I "no activation":** zero counts, or counts no higher than laminae II to IV.

**Fixed by me because the paper gives no method or test:** the rule for a colonic response, "similar" for the 8-week rats, the order from voiding to non-voiding within a session, "comparable" to published values (judged as overlapping CIs), and the cut-off for "rare" ATF3 nuclei. Each criterion says the choice was mine.

**Inconsistencies in the paper, recorded for the author:**
- The awake ECAP cohort is three rats in the Methods but n = 4 in the Results.
- The kind of ± spread (SD or SEM) is not named for the awake thresholds or the impedances.
- The c-Fos session is 60 min in the Results and 2 h in the Methods.
- The P2 threshold range (595 to 648 µA) has its central value as its upper bound.

**Missing:** nothing the claims needed. Evoked voids are classified by visible urine, and the histology and observation findings were only seen by eye. Those claims can only be tested if the dataset holds the experimenters' annotations or images; otherwise they will be blocked.
