I wrote `claims/001545/10.26508-lsa.202403169.yaml`, with 52 claims. The quote checker reports 0 problems.

**Text read.** The version of record as Europe PMC serves it (PMC12032840): main text, Methods, and all figure legends including Figs S1 to S10. One supplement was not under `paper/`: the Key Resources Table (Supplemental Data 1, a docx). It holds the GEO accession and the code links, so I took it from the Europe PMC supplementary bundle. I also looked at the Fig 2 and Fig S2 images from that bundle. Tables S1 to S6 are gene lists and no criterion needed them.

**Sources beyond the paper text:**
- **Ephys code:** `nsdesai/patch_clamp_analysis`, commit 5d756c2 (MATLAB). It only extracts features; the paper says the statistics were run in Prism and the regression and LDA in R.
- **Sequencing code:** `RajNINDS/V321L-snMultiome`, commit c124726 (R).
- **Kim et al 2024 (Cell Rep):** the Methods take their feature definitions from this paper, so I read it too.

**Claims:**
- 52 claims, all with quotes and criteria; 33 have statistics.
- 16 claims use the sequencing data, which is in GEO (GSE280167), not the dandiset. Their `data` is marked `elsewhere`.
- The ones the dandiset can test are Figs 1J to L, S1, 2I to K, 2M, S2D to G and the multiple regression. The morphology and soma-position claims also need those data, if the dandiset holds them.

**Details left open, with the readings named:**
- **Which 20 features:** Kim et al and Fig S2C list 18, and the code outputs 21. The paper also uses an upstroke/downstroke ratio that neither defines. Readings: the 18, or the code's 21.
- **Kim et al against the code:**
  - Spike threshold is 20 mV/ms in Kim et al and 10 mV/ms in the code.
  - Input resistance uses the −20 pA step in Kim et al; the code fits steps from −50 to 0 pA.
  - For downstroke, the code's window runs to the end of the 500 ms step, so it can include later spikes; Kim et al take only the first spike.
  
  Kim et al's definitions are the main reading and the code's are variants.
- **Mann–Whitney tails:** not stated, so one- and two-tailed tests are both run.
- **LDA (Fig 2G and 2M):** the classes are not stated; I read four (genotype by cell type), because the figures show an LD2 axis. Whether PCA comes before the Fig 2M LDA is also open.
- **Classifier (Fig S2G):**
  - V321L data scaled with their own mean and SD, or with WT's.
  - "78%" as the mean over folds, or pooled out-of-fold.
  - The fold seed is not given.
- **Regression:** how cell type is coded (which type is 1), which flips the sign of β1.
- **k-means (Figs S2B, S2D):** the scaling, number of PCs and seed are not given.
- **PCA ellipses (Fig S2E):** a 95% ellipse of the data, or of the group mean.

**Mismatches inside the paper (recorded in the claims):**
- **Prox1+ count (Fig S3B):** the Results give Mann–Whitney P = 0.69, the legend Welch's t P = 0.5. Both tests are run.
- **Classifier accuracy (Fig S2G):** the confusion matrices give 16/21 (76%) and 11/23 (48%, kappa about −0.09). The text says 78% (kappa 0.57) and 52% (kappa 0.08).
- **p-values that differ between text and legend:** Fig 6a′ (0.0032 against 0.002) and Fig 6b′ (0.0012 against 0.001).
- **Fig S1B:** P = 0.0543 is counted as significant, so the criterion accepts a p up to 1.1 times the reported value.

**Thresholds I set myself:** several criteria for claims the paper only describes in words use cutoffs it does not give: 90% separation on LD1, top decile or thirds of pseudotime, a 40 to 60% share for "uniformly", and "8 of 10 clusters" for "nearly all". Each is marked in its criterion as not from the paper. The second reader should look at these first.

**Missing from the paper:** nothing a claim needed, once the Key Resources Table was fetched.
