I wrote `claims/andrews-2024.yaml`. The quote checker passes except for one flag, which is the checker failing to match how the paper prints a value. Nothing was committed.

**Text read:** the NIH author manuscript in PubMed Central (PMC11881784, NIHMS2047739). It includes the Methods, figure legends, Tables 1 and 2, and the Extended Data legends. Both supplement files were there: the Inventory of Supplemental Information, and Supplemental_Information.pdf with Figs. S1 to S3 and Tables ST1 to ST6. I did not read the version of record. Nothing the claims need was missing.

**Code read:** braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit 6865bf68cc3c. The R code for the t-tests, logistic regression and chi-square test is not in it.

**Claims:**
- 29 claims, all with quotes; none are inferred.
- 10 claims carry statistics (52 values), 14 carry expected values, and all 29 have a criterion.
- One claim is `data: elsewhere`: the simulation, rerun from the repository at the pinned commit.
- One is `data: with_inputs`: it uses Table 2's histology transduction values.
- The flag is p = 3.634e-04 (ST5 and the Fig. 5 legend). The checker does not generate that printed form. I confirmed the value by reading and noted this in the file.

**Details the paper leaves open, and the readings named:**
- **Which recording and trials make each slice and condition:** (a) the recording whose unit count matches the N in the Extended Data legends; (b) the file the code names; (c) all light trials. Mapping the code's file names to slices is left to the author.
- **Table 2 percent decrease:** averaged over trials first, per trial then averaged, or the code's per-trial share. Denominator: all units, or units with a nonzero pre rate. For rows 9E to 12G, 0-mg is the main reading and 0-mg+KA the second.
- **Burst detection (0-mg isolated bursts, 0-mg+KA rhythmic bursts):** no detector is given. I used the population-rate and find_peaks method from the Methods' propagation section, with the peak threshold either mean + 3 SD or 5 times the median.
- **KLD coherence:** phase binning of 18 or 36 bins; all electrodes or only electrodes with a unit in the burst; the LFP low-pass step uses a standard choice.
- **Propagation:** a 2 s window (Methods) or 1.5 s (code). The code also uses a different recording of patient F. The hilar-to-outer axis comes from histology. Theta propagation has no test in the paper, so I named a plane-wave fit with shuffles.
- **Intensity threshold:** at least a 50% rate drop, or a significant paired test.
- **Simulation "dampening":** event duration, event count, or spike count during events.
- **Supplemental Fig. S3 adjustment:** Holm or Bonferroni.
- **Fig. S2 regression slope:** the paper reports no test, so the absence is judged on the regression slope.
- **Waveform clustering:** 3681 waveforms (paper) or 3405 (the code's saved labels, after excluding positive spikes). Seeds are not fixed, so ten are run.
- **GCL association:** units labelled by slice or by electrode over histology; the six non-GCL slices are not named; one-against-rest models or a single factor model; clusters matched to the paper's numbering via the code's labels or waveform features.
- **Opto-response clustering:** the Methods say 1 ms bins but 200 dimensions, which fits the code's 100 ms bins, so I used those. UMAP output is 10 dimensions (Methods) or 5 (code). Significance is p < 0.05 corrected (Methods) or p < 0.01/n (code). Recordings are the 41 the code lists, or all light recordings. HDBSCAN noise units are excluded or kept as a category.

**Inconsistencies in the paper, noted in the file:**
- The supplementary table cross-references are mismatched.
- ST2 prints identical amplitude rows for 5C and 7D.
- The cluster 5 confidence interval is 5.8 to 18.3 in the Fig. 5 legend and 5.810 to 18.030 in ST5.
- The Fisher's exact test used for 8D amplitude is not described, so 8D is reported and left out of that verdict.

**Missing data, likely:** the histology claims (transduction range, reporter location) and the patch-clamp claim need data the paper does not say were deposited. The Methods also say the opto-response analysis used 1 ms bins, which conflicts with its own 200-dimension count; I followed the code there.
