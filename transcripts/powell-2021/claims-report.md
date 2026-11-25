I wrote `claims/powell-2021.yaml`. The quote checker reports 22 claims, 22 quotes, 7 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC7889077, open access JATS). It includes the Results, Discussion, Methods, the legends of Figures 1 to 6 and the legends of all four figure supplements. The paper has no other supplementary text. The Figure 5f legend is garbled ("were n across temperature"), so that claim quotes the matching Results sentence instead. I did not open the PDF.

**Code read:** github.com/marderlab/gastric at the commit the paper cites (`fa07d36`), and the later head (`7a82b1f`), which adds a per-preparation Rayleigh test. I did not read the libraries it depends on, `crabsort` (which does the burst detection) and `srinivas.gs_mtools`.

**Claims:** 22, all with quotes. 7 carry statistics, 10 have expected values and all 22 have a criterion.

What they cover:
- Spontaneous rhythms from 11 to 30 °C, and less regular in the warm example.
- Evoked rhythms from 7 to 21 °C in 9 of 10 preparations.
- Spontaneous and evoked rhythms similar in 3 of 4 preparations.
- Periods shorten with temperature in all 10 preparations.
- Q10 near 2 in 8 of 10 preparations; PD and LG Q10 not different (paired t-test, p = 0.235).
- The gastric rhythm slows with time after stimulation.
- With the PD neurons hyperpolarized, the rhythm persists, and the counts per temperature.
- Example ratios, LG–PD integer coupling (KS test), no DG coupling, coupling areas, and the ratio not changing with temperature (Spearman, p = 0.88) with its range.
- LG phase locking (Rayleigh test), burst start counts, a constant phase near 0.5, LG spiking dropping near the end of the PD burst, and no DG locking and no DG drop.

**Details fixed from the code where the Methods are silent:**
- PD bursts split at gaps over 0.18 s with at least 2 spikes.
- Temperature bins are ±1 °C around 7, 9, …, 23 °C.
- Outlier cut-offs for periods.
- How the mean PD period within an LG cycle is computed.
- How the coupling area and its bootstrap are computed.

**Details left open, with the readings named:**
- **Q10:** the Methods average one Q10 per temperature step; the code computes one per burst and drops values above 10. The Methods version is the main analysis and the code's is a variant. "~2" is read as 1.8–2.2 or 1.5–2.5.
- **KS shuffle:** either the code's 100 independent resamples or a permutation of the same size. Since the shuffle is random, it is repeated over many seeds and the median p reported.
- **Rayleigh sample:** the first 40 per preparation and temperature (Methods), the first 50 (later code), or pooled per temperature (archived code). With 40 burst starts z cannot exceed 40, so the reported z of 45 does not fit the Methods as written.
- **"~35% of data" excluded:** a fraction of preparation–temperature combinations, or of burst starts.
- **Thresholds the paper gives none for:** what counts as a rhythm being present, "similar" for spontaneous against evoked, the test for "decrease" in periods, "low temperatures" for the ratio range, and a measure of the drop in spiking near the PD burst end.
- **Slowdown burst rule:** the code needs 7 spikes per LG burst here, the Methods 5; both are run.
- **Example cycle:** which LG cycle is drawn in Figure 5a.
- **Thresholds I set myself, each marked in its criterion as my choice:** a 20 °C split for regularity, percentiles for the ratio range, and half the LG drop for the DG comparison.

**Nothing missing from the paper.** Two things for the author to confirm in the dataset, since I did not look:
- The spontaneous recordings (2013, first reported in Haddad and Marder 2018) and the PD-hyperpolarization experiments (2020) may not be in the record. The archive description names only the evoked experiments.
- The paper calls the 3799 cycles in the Spearman test "PD cycles", but the code counts LG cycles.
