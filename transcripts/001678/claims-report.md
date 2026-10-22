I've written `claims/001678/10.1162-imag.a.1066.yaml`. The quote checker reports 45 claims, 43 quotes, 37 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record, open access, from Europe PMC (PMC12779756): the main text with Methods, figure legends and Tables 1 to 4, plus the full supplement (sections S1 to S3, Tables S1.1 to S3.1, Figures S1.1 to S2.4). Nothing the claims need is missing from the text.

**Code read.** I read github.com/m-bellvila/Parametrizing-alternating-current-stimulation-for-neuromodulation at commit 3b89bf2. It holds four scripts:
- `MUAartrem.m` removes the stimulation artifact with a comb filter.
- `concatdataforspikesorting.py` joins each rat's trials for spike sorting.
- `phaseextract.py` computes spike phases and decides which neurons are included.
- `nulldistribution.py` builds the permutation null distributions.

Several pieces are not in the repository:
- `signeurons.py`, which compares observed changes with the null. The README names it.
- The R mixed-model code, the regressions, the LFP power and phase-amplitude coupling code, and the electric-field and finite-element-model code.

The Science Data Bank deposit the paper points to (doi:10.57760/sciencedb.32375) asks for a login, so I could not read its files.

**Claims.** There are 45. 43 have quotes; 2 are marked `inferred`, because their numbers appear only in Tables 2 and 4. 21 claims record statistics (37 tests in all), 45 have criteria and 37 have expected values. Three finite-element-model claims use outside inputs (the ViZOO rat model in Sim4Life); every other claim uses the dataset.

**Details the paper leaves open, with the readings named.** These are listed in the opening comment, labelled [S] to [M], and the criteria refer to the labels.
- **[S] Spike sorting:** the Methods say "per trial" recordings, but the code sorts each rat's trials concatenated. Both readings are named.
- **[W] Analysis windows:** the Methods use the full periods; the code drops the first 5 s. In the 20-min code, the firing-rate null also uses only 5 to 60 s of each period.
- **[P] Entrainment test sidedness:** two-sided on the absolute change, as for firing rate, or one-sided. The missing `signeurons.py` would settle this.
- **[G] Grubbs outlier removal:** per response group or over all affected neurons together; iterated or a single pass.
- **[R] Regression points:** one point per neuron and trial, or per-rat medians. Table S1.2 implies about 100 points, which fits per neuron. The share slopes in Tables S1.4 and S1.5 are in fractions.
- **[L] LFP analysis:**
  - Which channels count as "mixed response" and are excluded.
  - What family the Bonferroni correction covers.
  - Natural log or base 10.
  - A rectangular or Hann FFT window.
- **[M] Phase-amplitude coupling:** whether values not significant against the surrogates are zeroed; whether order normalization pools all values or each band pair apart.

Some open details apply to single claims:
- **Electric field:** how values are combined (per-rat median or all channel pairs pooled), and the band-pass filter, which is not named.
- **Ellipsoids:** whether the axis lengths are radii or diameters.
- **Inclusion windows for the 20-min paradigm:** the Results say 1-minute windows, the Methods and code use 10-second windows.
- **1-min LFP:** the windows, since the Methods say LFP was analysed only around the 20-min trials.
- **Sham:** power windows of 3 s or 2 s, and the power units (printed as "mV/Hz").

**Inconsistencies in the paper, and how I resolved them:**
- The Results give p = 0.001 for the amplitude-by-frequency interaction on firing-rate decrease; Table 3 gives 0.0131. I used the table.
- "50 and 10 μA" in the Results is read as 50 and 100 μA, as in the legend (10 μA was not tested).
- One of the "decreases across all bands" is printed as +0.09; I read it as -0.09.
- The text says 60% of neurons were inhibited; Table 1 gives 69.23%. The criterion accepts any value within Table 1's confidence interval.
- The text gives -2.30e-3 "% per Hz" for the 200 μA share of excited neurons; Table S1.4 gives the same number as a fraction per Hz. I followed the table and report both.

**Missing from the paper.** Nothing in the text is missing. The one gap is in the code: the comparison script, `signeurons.py`, which leaves the entrainment test's sidedness open. Also, the dandiset description names only the 9 and 13 rats, not the single sham rat; whether the dataset holds that recording is for the author to find.
