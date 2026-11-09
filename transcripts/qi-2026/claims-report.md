I wrote the claims file at `claims/001960/10.64898-2026.10.05.756595.yaml`. The quote checker reports 56 claims, 56 quotes and 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint, version 1, flattened from the JATS XML: main text, legends, Discussion and Methods. The supplement PDF (Supplementary Figures 1 to 26) was extracted into the same file.
- I rendered PDF pages 16, 39, 41 and 43 to read the significance marks of Supplementary Figures 10H, 24E, 25 and 26, which the extracted text garbles.
- The Methods equations are lost in the flattened text (signal model, P(spk|V), mixed model, balanced accuracy).

**Code read.** `adamcohenlab/Qi2026WideAreaL1` at commit `181ad47`. It has a script and a loader per figure (2 to 6) that rebuild the panels from the NWB files, and five method tutorials. Tutorial 5 covers the Figure 3L/3O mixed model.
- The code settles the method for Figure 2C, Figure 3E to H and 3J to N, and the Figure 4 text numbers.
- It does not compute the Figure 5 and 6 text statistics or Supplementary Figures 22 to 26. Its header says these come from `sup_fig5_connMap_stats_norm.m`, which is not in the repository.

**Counts.** 56 claims, all with quotes; 21 with statistics, 40 with expected values, and all 56 have criteria. Every claim uses the default data field (`dataset`).

**Details the paper leaves open, and the readings named:**
- **Which cells give n = 564, 543 and 520:** QC cells, or all cells with finite values. QC cells give 576.
- **Ratios and SNR decay:** mean of per-cell ratios, or ratio of means.
- **Signal-to-background:** (cell − background)/background, or cell/background.
- **"Pairs tested" for the connection counts:** ordered QC pairs within 400 µm, or pairs with a stored measurement. For gap junctions, whether pairs under 60 µm count.
- **50% detection limits:** amplitudes of the 100 pairs per mouse nearest the cutoff, or detection of a template injected into null waveforms.
- **Connection probability against distance (no code):** exponential fit by least squares or log-linear fit; 30 or 60 µm bins.
- **Lasso penalty:** minimum cross-validated error, or within one standard error of it.
- **Interaction kernel (Movie 3):** IPSP time zero at pulse onset or pulse end.
- **PCA:** smoothed voltage, or unsmoothed with the lag-1 diagonal; per mouse or averaged.
- **Wave speed:** distance regressed on lag, or lag on distance and inverted.
- **277/270 µm length constants:** the synchrony fit (under 800 µm), or the 2.5 ms-lag fit. Which state the 2.5 ms half-width uses: whisking as in the code, quiet as a variant.
- **Figure 5 numbers** (comparison with controls):
  - Median of connected minus median of controls, median of per-pair differences, or the regressed quintile average.
  - "Median strength" as all connected pairs or the third quintile.
  - The integration window for spikes lost or gained.
- **Classifier:** cells pooled or per mouse; features z-scored or raw; "most impactful" as largest coefficient or largest drop in accuracy.
- **NPY subthreshold R and slope:** all frames or non-running frames; slope direction.
- **Oscillation-peak window:** ±50 or ±100 ms.
- **Sign of the paper's numbers:** the paper reports n = 497/482 and 653/651 where the code README expects 561 and 706. I read the paper's n as plotted points.
- **Methods against code, Methods followed:** "10 ms before spikes" against the spike-frame sample; dV/dt shift of 6 ms against 4 frames; 500 ms moving average against 500 ms bins. The code's choices are named as variants.

For about 12 qualitative claims with no number or test, the criterion is a reading chosen here and says so. Examples: log-normality, sigmoid shape, Figure 4G, the self-STA divergence, and the inhibition and gap-junction balance.

**Missing or doubtful:**
- **Experiments the dandiset description does not list:** the JF585 vs JF608 dye and LED comparisons, the 76-cell stimulation demonstration, the off-target lattice test, the z-stacks, and the high-magnification gap-junction check. The interstitial-pixel scatter control needs movies, and only a 24-minute raw excerpt is deposited.
- **"Mouse 1" for the NPY counts:** the paper does not say which mouse it is.
- **Gap junctions by NPY subtype:** the published Supplementary Figure 25D/E marks some significant pairwise differences. The text says connectivity "did not differ systematically", so that claim's criterion reads "systematically" as a consistent direction.
- **Dandiset title:** it differs from the paper's title, but the paper's Data availability statement names 001960 and the description matches.
