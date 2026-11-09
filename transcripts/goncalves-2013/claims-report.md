I wrote `claims/crcns-ssc-8/10.1038-nn.3415.yaml`. The quote checker reports 28 claims, 28 quotes, 35 statistical values and 0 problems.

**Text read:** the version of record, PMC3695061 (open access), taken from the Europe PMC full-text XML. It has the main text and the Online Methods. Three things were missing:
- **Figure legends:** not in the text.
- **Supplement:** Supplementary Figs. 1 to 4 are cited but were not supplied.
- **PDF:** none was supplied.

I went ahead because every number the claims use is printed in the Results text. The paper links no analysis code, so none was read.

**Claims:** 28 findings, every one with a quote and none under `inferred`. 23 have statistics (35 tests in all), 23 have expected values, and all 28 have a criterion. Where the paper gives an s.e.m., that is the tolerance. Mouse counts have tolerance 0, with the reason stated. Every claim uses the default `data` (the paper's own recordings). The dataset can test 11 claims: group sizes, Fig. 1d, Fig. 1e, the genotype difference pooled over ages, Pearson, P14-16, P30-40, Fig. 2b, Fig. 2c, imaging firing rates, and the unanesthetized P14-16 values. The other 17 need whole-cell, EEG, isoflurane or 15.6 Hz data, which the CRCNS description does not list.

**Details the paper leaves open, with the readings named:**
- **Trace used for correlation:** T-a, the deconvolved traces (the dataset's estimated rates); T-b, ΔF/F traces, which would mean segmenting the cells again.
- **Correlation measure:** it is not Pearson, since Pearson is given as the alternative. C-a, Spearman at zero lag; C-b, zero-lag normalised cross-correlation without mean subtraction.
- **Fig. 1d ANOVA form:** A-a, distance bin as a between factor; A-b, mouse as a repeated measure.
- **Fig. 1e age test:** E-a, a within-genotype contrast in the 2×3 model; E-b, a Welch ANOVA for each genotype.
- **Pooled-ages comparison:** which pairs (P-a, under 100 µm; P-b, all pairs) and how the mean is formed (M-a, over all mice; M-b, the mean of the three age means).
- **Peaks of synchrony:** when a cell is active (R-a, rate above 0; R-b, at least 1 spike per frame), how traces are shuffled (S-a, permutation; S-b, circular shift), and how participation is measured (Q-a, per event; Q-b, at least one event).
- **Fig. 2b group sizes:** n is printed as 9 KO and 10 WT, the reverse of Fig. 1e.
- **Fig. 5g group sizes:** n is printed as 10 WT and 13 KO, the reverse of Fig. 5c. G-a, as printed; G-b, swapped.
- **Fig. 6 KO correlation:** the text does not say which value is under isoflurane. I-a, 0.21 is isoflurane; I-b, 0.21 is unanesthetized.
- **Unit of the estimated rates:** the descriptor does not say, so the rates are either Hz or per frame (times 3.9).
- **Unanesthetized Fig. 6 groups:** read as the Fig. 1e P14-16 mice, because the counts match.
- **Fitting the unequal-variance ANOVA:** I used weighted least squares with Satterthwaite degrees of freedom as a standard choice.
- **Imaging firing-rate absence claim:** the paper names no test, so it uses the Methods' default t-test.

**Missing material a claim needed:** Supplementary Fig. 2, for the measures and test behind "action potential kinetics were indistinguishable"; readings are named in that claim. Supplementary Figs. 1 and 4a, and the Fig. 1 legend, which may have named the correlation measure; I treated it as open.

Nothing was committed.
