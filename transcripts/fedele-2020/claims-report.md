I wrote the claims file at `claims/000576/10.1016-j.neuroimage.2020.116705.yaml`, and the quote checker passes with 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (a PDF supplied by a person, read through its extracted text): main text, legends, Tables 1–2 and Methods 4.1–4.11.
- **PDF:** no page renderer is installed here, so I read Table 2 from the text. Minus signs come out garbled there; the signs I used agree with the counts the Results give.
- **Supplement:** not supplied. The text cites it only for Fig. S2 (waveforms and inter-spike intervals per patient), which carries no finding, so I went ahead.
- **Code:** the paper links none. All methods are cited from the Methods, Results and legends.
- **Data descriptor:** I used the Sci Data paper (doi:10.1038/s41597-020-00790-x) only to describe the data layout.

**Counts**
- 23 claims: 22 with quotes and 1 `inferred` (the Table 2 MI values).
- 16 with `statistics` (22 statistical values checked), 16 with `expected`, and all 23 with a criterion.
- 6 claims are `with_inputs` because they need BOLD. The paper names no public deposit for the fMRI time courses (Schacher et al. 2006 cohort).
- The muHGP claims need continuous microwire signals. The data descriptor says only spike times and waveforms were shared.

**Details left open, with the readings named**
- **HGP upper band edge:** only ">60 Hz" is given; the reading is up to the Nyquist frequency.
- **Filter direction and smoothing window shape:** these can't change the outcome, so I used standard choices (zero-phase filter, boxcar window).
- **z-scoring "within each trial":** (a) over the whole 26 s trial, (b) against the baseline, (c) over all of the patient's trials.
- **Amygdalae in the group test:** (a) the 7 nSOZ, as the Results say, or (b) all 14, as the Fig. 1 legend suggests.
- **Cluster threshold and statistic:** (a) cluster mass, or (b) cluster length.
- **Group test:** the Methods say a mixed model; the Results say unpaired t-tests. The mixed model is the main reading and the t-test a variant.
- **MI window:** (a) the group-level clusters applied to every amygdala, or (b) clusters found per amygdala.
- **Tests behind p = 0.009 and p = 0.019 (Fig. 1E):** not named. Readings are rank-sum, t-test, and Fisher or chi-square.
- **Fig. 1F counts:** the source of "5/5 vs 1/5" is not explained; readings are the specificity counts from Table 2, or the counts as printed.
- **Confidence intervals:** the Clopper-Pearson interval is the reading for "the binomial distribution".
- **FDR family for Table 2:** 9 or 18 tests.
- **Time base for firing correlations:** 100 ms bins with 1 s smoothing, 1.5 s with 5-point smoothing, or 15 s smoothing; each computed over the concatenated time course or per trial and averaged.
- **FRV window:** the 24 s blocks or the 26 s trials.
- **Which microwire gives muHGP:** the neuron's own, or the mean over the bundle.
- **Meaning of r in the regressions:** the multiple R, or Spearman of fitted against observed values. "Described by both" is read as both coefficients with p < 0.05.
- **Interval for the 1 Hz unit cutoff:** all trials, or the whole recording.
- **"Gradual and sustained" firing:** the paper gives no measure, so I named two readings.

**Missing from the paper, or inconsistent within it**
- **"Methods 7.8":** cited for the other spectral bands, but no such section exists, so the no-effect claim can't be checked against it.
- **Microwire coverage:**
  - The abstract says 5 participants had microwires.
  - The Results say 9 amygdalae.
  - Table 1 lists 8 amygdalae in 6 patients, three of them in the seizure onset zone.
  - The Limitations section says no microwires were in SOZ amygdalae.
- **Number of blocks:** 8 aversive and 9 neutral in the Methods; 8 of each in the data descriptor.
- **BOLD–HGP count:** the Table 2 legend says 5/5 positive, but the Results and the table's own values give 3/5.
- **Ambiguous figures:**
  - FRV is reported as 0.26 ± 0.15 without saying whether ± is SD or SEM. I used it as the tolerance, since the protocol says to use the stated spread.
  - "MI < 0.05" is set against a printed value of 0.05.
