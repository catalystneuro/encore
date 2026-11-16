I wrote `claims/see-2018.yaml`: 31 claims from the full text, Methods and supplement. The quote checker passes every quote. It flags one value it can't match, which I checked by hand (below).

**Text read**
- **Paper:** the version of record (PMC6017807, Europe PMC full-text XML), with all figure and figure-supplement legends and the Materials and methods.
- **Supplement:** Supplementary file 1 (`elife-35587-supp1-v2.xlsx`), the table of statistical tests giving the test, N and exact p for each panel. It is also printed at the end of the text file.
- **Figures:** no PDF was supplied, so figure axes were not read. Every value used is printed in the text, a legend or the supplement.
- **Code:** the only repository the paper links is CorBinian (Macke lab), the implementation of its dichotomized Gaussian (DG) model, used as a surrogate data model. I read it at commit 8ebb12d (2021); the paper cites the 2017 state, which can't be pinned. The paper's own MATLAB analysis code is not linked.

**Counts**
- 31 claims, all with quotes, none inferred.
- 13 claims record statistics (24 p-values in all, most of them exact values from Supplementary file 1).
- 31 have criteria and 16 have expected values.
- The checker flags p = 8.70e-12 (Figure 10, figure supplement 1E) as not found. I read it in Supplementary file 1 (text line 457) and it is correct. The checker misses it only because the paper prints a trailing zero. I left the checker and the value as they are.

**Details the paper leaves open, with the readings named**
- **cNE detection** (used in most claims):
  - Marčenko–Pastur bound: the standard (1+√(n/T))², as in Lopes-dos-Santos et al. (2013).
  - Independent component (IC) scale and sign: (a) unit length, largest weight made positive; (b) as fastICA returns them.
  - Activity: (a) the quadratic form with the diagonal set to zero; (b) a linear projection.
  - What counts as an event: (a) every bin above threshold; (b) one per run of bins above threshold.
  - fastICA settings and random seeds: standard choices, stated as such.
- **Pairwise correlation functions** (Figures 2 and 6): the lag bin and range, either 1-ms bins over ±50 ms or ±100 ms, with the fit on linear or log axes.
- **Pairwise distance:** depth difference, or Euclidean distance on the probe.
- **Stability matching** (Figure 4, supplement 2, and Figure 8): the number of shuffles and what the shuffled ICs are correlated with (shuffled against shuffled, or real against shuffled).
- **Averaging:** pooled over all cNEs, or per penetration first, for the Figure 6 sharpness means and the Figure 7 sizes and fractions.
- **Penetrations recorded with both stimuli:** which file the paper used; the reading is the set whose unit counts sum to 655.
- **Figure 9 events on the 5-s repeats:** the ICs from the 10-min recording projected onto the repeats, or detection run on the repeats themselves.
- **Noise correlation:** the spike count per trial, or rates per bin.
- **Figure 11A/B:** how the 30% rate-stability rule is computed.
- **PR surrogate model** (spikes reshuffled while each neuron's receptive field is kept): the shuffle bin, 5 ms or 10 ms.
- **Figure 11D:** whether model runs that yield no cNE are dropped or counted as zero.
- **Figure 5A:** how mutual information is summarised over cNEs (mean or median). The STRF window and the number of projection bins are standard choices.

**Thresholds I had to supply** (the paper reports no test, so each is marked in its criterion as a reading, not the paper's method):
- the depth-bias test (KS test or Mann–Whitney);
- the bin-size trends (Spearman correlation);
- "much narrower" versus "often as wide" in Figure 6C;
- "close to zero" in Figure 11, supplement 3B (absolute value below 0.1).

**Inconsistency in the paper:** "9 cNEs (8.3%)" doesn't match 104 cNEs (9/104 is 8.7%). The criterion judges the count of 9 and reports the percentage.

**Nothing a claim needed is missing from the paper.** Several claims need experiments that may not be in the dataset: the 5-s repeats (Figure 9), the 15 repeats of the 10-min stimulus (Figure 11A/B and the "repeat" coincidence ratio in Figure 11E/F), and the eight 64-channel spontaneous and evoked recordings (Figure 8). The descriptor lists only the long-stimulus files; whether the dataset holds the rest is the author's to find. Nothing is committed.
