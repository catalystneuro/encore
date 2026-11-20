I've written `claims/mills-2026.yaml`. The quote checker passes with 0 problems: every quote matches the text word for word and every p-value is found. Nothing is committed.

**Text read**
- **Main paper:** the author-accepted manuscript from Europe PMC (PMC13592531), CC BY. It has the full main text, figure legends 1 to 6 and the STAR Methods.
- **Supplement MMC1:** the legends of Figures S1 to S17, as text.
- **Supplement MMC2 (Data S1):** 46 pages of images only, showing per-mouse histology and which mice were excluded. I looked at it only to identify it; no claim rests on it.
- **Code:** github.com/Tyelab/Mills-et-al-2026 at commit 1fee26d. It covers five electrophysiology analyses: the Fig. 3H decoding, the Fig. 3I to 3M model of spike counts (GLM), the Fig. 2Q population trajectories, the Fig. S8B example trial pairs and Fig. S9C. Its packaged results match the paper's GLM numbers (125 and 66 neurons, p = 0.029).

**Claims**
- 46 claims: 45 findings and 1 check that the dataset holds the paper's neuron counts per region and group.
- 45 have quotes. The count check has none, since the schema does not allow a quote or `inferred` note on that kind of claim.
- 38 have statistics (81 test entries in all), 12 have expected values and 39 have criteria.
- Two snRNA-seq claims are marked as data held elsewhere (GEO GSE211437).
- The optogenetics and RNAscope claims (about 13) are marked as the paper's own recordings. The dandiset description names neither, so they are probably not in it.

**Details the paper leaves open, with the readings named**
- **Bin size of the electrophysiology traces:** 10 ms (as in Fig. S6) or 100 ms (as in the code).
- **Inputs to the test that marks a neuron as responsive:** each trial's response window against its 20 s baseline, or against an equal-length window just before the cue.
- **Defensive behavior measure:** share of cue time spent freezing or darting, or summed seconds.
- **Fig. 2E and Fig. 5M clustering:** the linkage (average, Ward, or MATLAB's default single) and the span of the traces. Seven and nine clusters are taken from the figures.
- **Fig. 2P chi-square tables:** pairwise 2 x 3 tables with Holm correction, or one 3 x 3 table.
- **Fig. S8:** whether the Wilcoxon test runs on per-animal means against the mean of the two same-cue comparisons, against each separately, or on the pooled iterations.
- **Fig. S9 "1 s and 2 s timepoints":** the value in the bin at that time, or the mean from 0.1 s up to it.
- **Fig. S10 percentages:** ratio of the group means, or the median of each neuron's ratio. Linkage for splitting mice into high and low groups: average or Ward.
- **Fig. 3F-G bout-onset windows:** baseline of 20 s or 2 s before onset, response 0 to 1 s.
- **Fig. S14 reward consumption onset:** first port entry after delivery, or delivery itself.
- **Fig. S15 peak and spike estimation:** two readings named.
- **Fig. S8 PCA:** the Methods include both groups; the code is followed and the both-group version is a variant.

**Where the code settles or disagrees with the paper**
- **Unit filter:** the code keeps only units firing below 50 Hz. The Methods don't mention this, but it gives the paper's 193 ASt neurons, so I followed it.
- **Fig. 3H test:** the legend says Mann-Whitney U, the code runs a Wilcoxon signed-rank test. The legend is followed and the code's test is a variant.
- **Fig. 3M test:** the Methods say between-group tests are one-sided, the code runs it two-sided. Same approach.
- **Fig. S8 vectors:** the code uses 3-PC velocity vectors; the Methods' neuron-space vectors are followed and the code's are a variant.

**Missing from the paper that some claims needed**
- The MATLAB code for Fig. 2, Figs. S5 to S10, all calcium imaging and behavior scoring is not in the repository.
- The Fig. S8 statistics code is not there either.
- Fig. S10M analyses 191 neurons against 193 elsewhere, and the two dropped neurons are not identified.
- Three thresholds have no basis in the paper; I chose them and say so in the criteria: the "sustained cluster" rule in Fig. 2E, the plus or minus 0.5 z and "half" bounds in Fig. 3F-G, and the "over half ASt" rule in Fig. 1B.
