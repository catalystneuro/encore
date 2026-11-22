I wrote `claims/rozsa-2023.yaml` with 31 claims. The quote checker passed (`tools/claims_check.py`): 31 quotes, 18 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, open access (Europe PMC, PMC10569705), with its one supplement (`sciadv.ade4511_sm.pdf`: Figs. S1 to S6 and Table S1). The main figures were not available as images, so their values come from the Results and the legends. The reference list was not in the text, so I could not read refs. 28 (sag fraction) and 38 (cellular states). The paper links no code; it names only Fitmaster and custom MATLAB scripts.

**Claims:**
- 31 claims, all with quotes.
- 14 record the paper's statistics: paired and two-sample t tests, Mann-Whitney tests, Rayleigh tests, and one correlation whose type is not named.
- 22 have expected values. Every claim has a criterion.
- The claims cover RAF patterns and proportions in human and rat, cell-type dependence, soma versus bleb initiation order, ZD7288 effects, sag fraction, the 5 mM KCl puff, AP states and pre-AP fluctuation in slices, phase coupling in slices and in vivo, in vivo frequencies and RA-AP share, and Figs. S3 to S5.
- All claims use `data: dataset`. Two need morphology, genotype or anesthesia labels that the dataset may or may not hold; that is for the author to find.

**Details the paper leaves open, and the readings named:**
- **AIS-AP versus RA-AP boundary** (no numbers given): (a) labels in the dataset, (b) a two-component Gaussian mixture on threshold and pre-AP slope for each preparation, (c) in induction recordings, APs during the current pulses versus APs after them. Fig. 1C is tested without (b), which would be circular.
- **AP detection beyond the 5 mV/ms threshold:** peak above 0 mV as the standard choice, peak at least 30 mV above threshold as the variant.
- **RAF epochs:** one per cell, or one per induction run.
- **Sag fraction definition:** sag divided by the peak deflection, or by the steady-state deflection. The step used is also open: the most hyperpolarizing one, or the one whose peak is nearest -90 mV.
- **Up, transition and down states:** a two-Gaussian fit to the membrane potential histogram, or the range between the two modes cut in thirds.
- **Pre-AP SD window** ends at the threshold or at the AP peak. APs are pooled across cells, with per-cell medians as a variant.
- **Phase method:**
  - Butterworth filter order 2 (standard) or 4.
  - A zero-phase filter is the standard choice.
  - The 4 s window is centred on the AP.
  - Which 22 cells were used, and whether the AP counts are before or after the delta-power selection.
- **Medians or means** for the ZD7288 values and for the "average" 17% RA-AP share.
- **Median RA-AP frequency of 0.004 Hz in vivo:** it cannot be a median over all 242 cells, since 162 have none. Readings are all cells, cells with RA-APs, or cells with any APs.
- **Correlation in Fig. S4I:** Pearson or Spearman, over 242 or 75 cells.
- **Fig. S5 genotype and anesthesia** (no test named): pairwise Mann-Whitney with Bonferroni correction, or Kruskal-Wallis.
- **In vivo up/down balance** (no measure given): the cycle split into halves, or quarters centred on 0 and 180 degrees.
- **Tolerances:** the paper gives SD as spread (for example 88 ± 1828 RA-APs), so the expected values use 10% tolerances and the SDs are reported but not judged.

**Inconsistencies inside the paper, each recorded as alternative readings:**
- Human RAF cells are 87 of 385 in the Results but 83 of 358 in the sag analysis.
- Rat RAF cells are 102 of 259 in Fig. S1B but 97 of 254 in the sag analysis.
- In vivo, 242 minus 75 is 167 cells, but the paper says 162 cells had no RA-APs.

**Missing:** nothing the claims needed is missing from the paper and supplement. The definitions behind refs. 28 and 38 are cited but not stated in the text, so those two details are named as open.
