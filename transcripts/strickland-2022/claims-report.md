I've written `claims/strickland-2022.yaml`. The quote checker reports 30 claims, 29 quotes, 6 statistical values and 0 problems. Nothing was committed.

**Text read**
- **Main text:** the version of record (PMC9582012, open access, Europe PMC full-text XML): Results, Discussion, figure legends and Methods.
- **Supplement:** Supplementary Information (MOESM1) as extracted text: Supplementary Methods, the legends of Supplementary Figs 1 to 7, and Supplementary Tables 1 and 2. Table 2's columns are garbled in the extraction, but its row and subject totals are intact.
- **Source Data workbook (MOESM4):** read with a small XML parser.
- **PDF:** could not be rendered because poppler is not installed, so no figure was read as an image.
- **Data descriptor:** read only to know what the data set holds.
- **Code:** not read. The paper puts its code at CRCNS, which means inside the data set's own files, so no commit is recorded.

**Claims**
- 30 claims: 29 findings plus 1 link claim.
- 29 have quotes. The link claim has none and none is inferred.
- 5 claims carry statistics (6 tests), 17 have expected values, and all 30 have a criterion.
- The link claim checks that the data set's units can be matched to the rows of the Source Data cluster sheets. That match recovers the paper's own cluster membership, and the four claims that name individual clusters depend on it (`data: with_labels`).

**Details the paper leaves open, and the readings named**
- **Baseline subtraction:** per trial, or per trial type.
- **Z-score window:** the 50 s stated in words (200 bins), or the "240 bins" also given (60 s).
- **Trials with no pokes:** a suppression ratio of 0, or left out.
- **K-means:** no options, replicates or seed. I used MATLAB's defaults and judge on the median over 20 seeds, with the best of 20 replicates as a variant.
- **Cluster labels:** the paper's own membership from Source Data (L1), or the author's own k-means matched to the paper's clusters (L2). The Source Data show that cue clusters are numbered by PC1 contribution.
- **What is shuffled in the lesion and contribution analyses:** each row on its own, or the whole block. The sign alignment of PCs across shuffles is also unstated.
- **Regression:** on the cluster-mean firing, or per unit and then averaged; with or without an intercept. Source Data Figs 3b and 5b hold the paper's own beta matrices, so whichever reading matches them decides.
- **Suppression ANOVA:** the stated degrees of freedom F(2,142) fit a cue × sex mixed design. A plain repeated-measures ANOVA on the paper's own Source Data gives F(2,144) = 116.2, so that reading is shown but is not the main one.
- **Bootstrap contrasts in Supplementary Fig. 2:** three readings of which quantity's interval must exclude zero.
- **Latency to PC1 contribution correlation:** contribution per unit or per cluster total. On the paper's Source Data these give R² = 0.51 and 0.39, against the reported 0.41. Which units carry no latency is also open: Source Data lists 1498 of the 1812.
- **Correlation matrix width:** 36 columns (Methods) or 42 (Source Data); r or r².
- **Bonferroni divisor for hubs:** 0.05/7 (Methods) or 0.05/8 (nine clusters give eight comparisons).
- **Network membership:** the Results give subnetwork k1–k9, phasic k1–k3 and tonic k6–k9. The Supplementary Methods say clusters 1–8, 1–5 and 7–10, and Source Data Fig. 5e's "phasic" row holds 679 units, the size of k1–k5. So the phasic network for Figs 5c and 5e is read both as k1–k3 and as k1–k5.
- **Thresholds I chose:** the shape claims ("sustained", "peaking mid cue", "intact") and the anatomy claims have no measure in the paper. Each such threshold is named in its criterion as a choice. The claim that anatomical biases were absent (Fig. 5e) has no test, so it is judged against the paper's own Source Data range.

**Inconsistencies in the paper**
- Supplementary Table 1 lists 75 sessions, against 73 in the Results and in Source Data Fig. 1c.
- The Methods say "21-cluster" for the outcome beta matrix, where there are 11 clusters.
- The Source Data sheets for Fig. 3a repeat the Fig. 2b firing values and contain no beta weights.

**Missing:** nothing the claims needed is missing from the paper, apart from the unread code inside the data set. Where those scripts settle one of the open details above, the author may follow them.
