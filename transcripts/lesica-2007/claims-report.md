I wrote `claims/lesica-2007.yaml`. The quote checker passes with no problems, the file has no em dashes, no "rather", and no ": " inside plain scalars. Nothing is committed.

**Text read:** the version of record (PyMuPDF text of the journal PDF), with its Results, figure legends, Discussion and Experimental Procedures, plus the one supplement PDF (the legend of Supplementary Figure 1). The paper links no code, so I read none.

**Counts:** 38 claims. All 38 have quotes and criteria, 20 record statistics, and 36 have expected values (all but the two Discussion claims on comparisons across stimuli).

**What the claims cover:**
- Sample composition, firing rates, and the LN models' prediction accuracy.
- Contrast and correlation effects on spatial width, surround strength and temporal width (Figure 3), and on gain, offset and normalized offset (Figure 4).
- The single-trial contrast analysis of Figure 5.
- Reliability and sparseness (Figure 6).
- Effective contrast (Figure 7) and the sparseness model with kurtosis, frame shuffling and added noise (Figure 8).
- The Discussion's comparison of low-contrast natural movies with high-contrast white noise.
- From the Methods: the latency and biphasic-ratio result, the offset that differs across animals, the X/Y and ON/OFF differences, and the spherical-asymmetry simulation.
- The correlations of Supplementary Figure 1.

**Details the paper leaves open, with the readings named:**
- **P1, how a percent change is formed:** (a) the change of the sample means; (b) the mean over cells of each cell's percent change; (c) for increases above 50%, the ratio of the means read as X/100.
- **P2, which responses give rates and fits:** (a) the long segments (15 min movie, 6 min noise); (b) the 12 s repeated trials.
- **P3, the level for "not significant":** the paper states none, so p < 0.05, with p < 0.001 shown as a variant.
- **P8, reliability:** whether the signal spectrum keeps or removes the mean term.
- **Standard choices that cannot change outcomes much:** how the half-wave rectifier is fitted, how q is adjusted per animal, interpolation on the 8 ms lag grid, and population versus sample SD.
- **Readings named inside individual claims:**
  - Inclusion: pass at both contrasts or at either.
  - Prediction correlation: against the trial-averaged response or against each trial.
  - The surround's peak: its largest absolute value or its extreme opposite in sign to the center.
  - Which cells and segments go into the generic RFs.
  - Which natural-movie stimulus has kurtosis 4.06.
  - Whether the generic model uses the normalized or the absolute offset.
  - The measure of contrast within the RF (Figure 5).
  - The test across animals: ANOVA or Kruskal-Wallis.
  - The level for the latency result and for the Discussion's "still significant".
  - "Nearly all" read as at least three of four.

**Missing or unread:**
- **PDF figures:** no PDF renderer was installed, so I couldn't read values shown only in figures: the bar heights of Figures 3, 4 and 6, the contrasts of Figure 7C, the coefficients of Supplementary Figure 1, and which Figure 6 bars are marked ** and which ***. For reliability I therefore judge at p < 0.01, and I require no significance for sparseness. No claim rests on a value I couldn't read.
- **Not stated in the paper:**
  - The number of cats, which the per-animal adjustment of q needs.
  - The noise level used in Figure 8D and 8E.
  - The known RF and the test used in the spherical-asymmetry simulation.
  - Where the movie frames are held: they come from Kayser et al. (2003), with no location given.
- **Other notes:**
  - The ±0.4 ms spread for ON/OFF temporal width looks like a standard error, so that claim uses a 10% tolerance and says why.
  - The sign of r = -0.5 is a garbled glyph in the text. I read it as negative from the context.
