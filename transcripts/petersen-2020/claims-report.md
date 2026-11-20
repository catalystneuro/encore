I rewrote `claims/petersen-2020.yaml` from the full text. The quote checker finds every quote word for word. Its one remaining flag is P = 8.0e-5 for Figure 5H: the legend prints it garbled as "P = 8.0 −5". I confirmed the value by reading, and the criterion notes it. Nothing was committed.

**Text read:** the accepted author manuscript from PubMed Central (PMC7442698), not the version of record. That covers the main text, figure legends and STAR Methods, plus the Supplemental Information (Figures S1 to S6 and Table S1). The paper links no analysis code ("available ... upon reasonable request"). It links only spike-sorting and cell-classification tools, so I read no code.

**Counts:** 46 claims, all with quotes and none inferred. 20 have statistics, 25 have expected values, and all 46 have criteria.

**What changed from the old file:**
- **Dropped:** the old file had been written after seeing the data. Its session sets, pilot-session fixes, and choices taken from a GitHub repository the paper does not link are gone. Every method is now cited to the paper or named as open.
- **Figure 5:** compression and period now come from the surface fit in the Methods, not from peaks picked per pair.
- **Ids kept:** every old id is kept, since each finding is the same.
- **8 new claims:** suppl2ab-rates-correlated, fig4f-speed-theta-power, suppl2e-trial-speed-theta-frequency, suppl3-theta-cycle-duration, suppl3e-precession-temperature, fig5e-phase-period-below-2pi, suppl5gh-rates-follow-temperature and suppl5j-errors-best-theta-frequency.
- **Values added from the supplement and legends:**
  - Figure 6E: P < 1e-7.
  - Figure 5J: the legend's three P values (0.28, 0.006, 0.0005).
  - Figure S2D: the 14% slowing.
  - The control experiment's MS and hippocampal time constants (45 s, 11 s, 115 s, 48 s, 72 s).
- **Removed:** the `dataset` key, which a paper's own claims file leaves out.

**Details the paper leaves open, and the readings named:**
- **Cooling-state boundaries:** (a) the dataset's trial labels, (b) trials starting within 12 min of onset, (c) within 10 min.
- **Trial theta frequency and power:** Hilbert instantaneous frequency and amplitude, or the peak of the spectrogram.
- **Running filter:** all frames, or frames above 10 cm/s.
- **Unit of correlation for Fig 2G/H and 6F to I:** trials aligned on cooling onset and averaged over sessions, binned, pooled trials, or per rat. The printed P values imply about 170 to 190 points, which favours the aligned averages.
- **Correlation type:** Pearson or Spearman.
- **Place fields for Figures 3 and 4:** they were defined by hand. Readings are the dataset's own boundaries, or the Figure 5 automatic rule with a peak above 10 Hz; bins of 3 or 5 cm.
- **fLFP:** taken at spikes, or over the time in the field.
- **Field size, and the speed v in S = v/(fp − fLFP):** two readings each.
- **Which comparisons the stars mark:** Fig 4B, 4D and 6E.
- **Precession slope "decreased":** flatter, or more negative.
- **Fig 5 spikes per pair:** each cell's own field, or the union of the two fields.
- **Choice of the τ peak:** the largest peak within half a theta cycle, or the peak nearest zero.
- **Surface equation:** the extracted text lost its fraction bars, and the +1 could sit inside or outside the cosine. The density grid and start values are standard choices.
- **Fig 5F/G session set:** 18 or 10 sessions. P = 0.002 matches 10 sessions all changing in one direction.
- **Fig 5H/I tests:** P values below 0.002 rule out signed-rank tests over 10 sessions, so they are read as tests over pairs.
- **Fig 5J:** place cells (the text) or all neurons (the legend).
- **Smaller open details:**
  - The width of the 80-point Gaussian window (MATLAB default).
  - Waveform measures.
  - Information measure (bits per spike).
  - The variable set for the partial correlations.
  - Interneuron class (narrow only, or narrow and wide).
  - The exponential fit for the time constants.
  - Whether the 14% of Figure S2D applies per class or pooled.

**Missing from the paper:**
- The sessions in each analysis set are not listed (53, 21, 18, 10 and 19 sessions).
- The speed unit for 87.3 and 86.2 is not printed; I read it as cm/s.
- The paper's own numbers disagree in places, and the criteria allow either value:
  - the 12% fall in theta frequency, against 8% from Fig 4B;
  - an 11% fall in within-field firing rate in the Results, 12% in the Discussion;
  - cooling peaking at 60 s in the Methods, 45 s in the Results.
- Not given claims: Figures S1B, S1F, S4 and S6, which are single-session illustrations, show no stated finding, or are a model.
- suppl1-hippocampal-temperature needs the control-experiment recordings of hippocampal temperature. Whether the dataset holds them is for the author to find.
