I wrote the claims file at `claims/000489/10.1016-j.bioelechem.2022.108319.yaml`. The quote checker passes: 21 claims, 21 quotes, 7 statistical values, 0 problems.

**Text read:** the accepted author manuscript in PubMed Central (PMC9729435), with the Methods, Results, Discussion and the legends of Figs. 1 to 7. The paper has no supplement and no PDF was supplied, so values shown only inside figures were not used. The paper links no code or data deposit, so there was no repository to read. The dandiset's title and description match the Fig. 2 experiment: BPAE cells given 5 pulses at 1 Hz, with the second phase at 0, 25, 50, 75 or 100% of the first.

**Claims:**
- **Count:** 21 claims, all with quotes and none inferred.
- **Statistics:** 5 claims carry them (7 entries), all two-sided Student's t-test bounds plus the two Fig. 7 fit correlations.
- **Criteria:** all 21 claims have one; 13 also have expected values.
- **Coverage:** Fig. 2 has 6 claims, and these are what the dandiset is meant to hold. Figs. 3 to 7 have 14 and the heating measurement has 1.

**Details the paper leaves open, and the readings named:**
- **Field strength per ROI (outside input):** the field strength for each measurement area comes from the paper's simulation, which was never deposited. If the dataset lacks it, the author recomputes it from the geometry in Methods 2.3, with the paper's 15.1 kV/cm maximum as a check.
- **Measurement areas along the bb' line:** spacing and number are not given. Readings: contiguous areas on both sides of the centre, or on one side. A named field strength uses the area closest to it.
- **t-test pairing:** not stated. Read both paired and unpaired where areas of the same dishes are compared.
- **Fig. 2B exponential fit:** low-signal cutoff read as 6, 7 or 8 kV/cm. Fit method read as nonlinear least squares or regression of log YP. The slope test is read on per-dish fits or on fits to the means.
- **Fig. 2C "~20%":** read as the mean over 8.7 to 15.1 kV/cm, or the minimum. The p < 0.01 comparison is read against unipolar pulses, or against the 25% and 100% amplitudes, each on raw or normalized values. The unnamed "selected" field strengths are taken as all areas in that range.
- **Figs. 3 and 4 cutoff and fits:** background cutoff read as 7 or 8 kV/cm. Which durations got exponential and which got polynomial fits is not given, so both are run. "Moderate field" for the 1200 ns pulses is read as the curve minimum or the middle of the range.
- **Fig. 5 test:** the text does not say whether the p < 0.01 for the anode side covers bipolar pulses.
- **Fig. 6 "difference between 1 Hz and kHz-rate trains":** read against the mean of all kHz rates, or against each rate.
- **Fig. 7 fits:** the 425 datapoints are read as per-cell points pooled (about 18 cells times 24 steps, which the count supports), or as the averaged trace.
- **Fig. 2A vertical scales (1200 and 250 a.u.):** these are axis limits, so the claim treats them as upper bounds. It is blocked on the absolute values if the images are not in the units the paper measured.

**Missing from the paper:** nothing the protocol requires. The field simulation output and the exact positions of the measurement areas were never published. For the Fig. 1E heating claim, the paper describes only the method (photographs of thermochromic sheets), and the dandiset is not meant to hold those photographs.

Nothing was committed.
