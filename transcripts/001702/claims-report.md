I wrote `claims/001702/10.1002-alz.70813.yaml` with 50 claims. The quote checker reports 0 problems; nothing is committed.

**Text read:** the version of record from Europe PMC (PMC12541281): main text, Methods and the legends of Figures 1 to 5. There was no PDF, so I could not see which comparison carries which asterisk in the figures. Where a legend lists several p levels, I recorded the weakest bound it allows. The paper links no code. Its statistics were run in Prism, its image analysis in ImageJ, and its RNA-seq analysis in DESeq2 and GOplot.

**Missing from the paper text:**
- **The whole Supporting Information.** That is Figures S1 to S9 and Tables S1 to S4. Tables S2 and S3 hold every mean, SEM, test statistic and exact p; Table S4 holds the RNA-seq analysis. So no exact p-value or test statistic is available. I went ahead because the main findings are stated in the main text and legends, as earlier claims files here did. The 11 claims on supplementary figures quote the main text that cites them, but their tests, sample sizes and measures are unknown, and each criterion says so.
- **A published correction** (e71098), which was not in the text.
- **RNA-seq sample sizes**, which the main text does not give.

**Claims:**
- All 50 have quotes; none rests on `inferred`.
- 18 claims carry statistics (20 p bounds in all). Only two have expected values: the counts of differentially expressed genes (98 up and 133 down at 3 months, 314 up and 6 down at 7 months).
- Every claim has a criterion.
- All are `data: dataset`. The paper names no outside data. The dandiset's own description says the RNA-seq data are also in GEO (GSE317499); whether the dandiset holds the counts is left to the author.

**Details the paper leaves open, with the readings named:**
- **Social test:** the trial length is not stated; the reading is the whole trial as the dataset records it.
- **Social test ANOVA:** where a legend says only "two-way ANOVA" (Figures 3C, 3H, 3K, 5B, 5E), trial may or may not be a repeated measure. Tukey's test may compare the trials within each group, or all six cells. Every combination is run.
- **Difference score sign:** legends label the second score "Familiar − Novel 2", but the text calls impaired scores "lower". The criteria use the two-tailed test and judge direction by which group lies further from zero on the side of intact memory.
- **Image threshold:** Otsu or Triangle, both named in the Methods.
- **WFA intensity:** the mean inside the WFA mask, or the mean over the CA2 rectangle.
- **Figure 5I:** "PNN expression" could be area or intensity, and a mouse's value could be the mean over its slices or a single slice.
- **Units where the paper only shows images** (Figure 3B, 3G): slices or mice. These claims use the Methods' default test for two groups.
- **Distance moved (Figure 2K):** measured during habituation, familiarization or the test phase.
- **DESeq2:** a model per age or one model on all samples, each with or without log fold change shrinkage. The Results' thresholds contradict each other, so the Methods' absolute log2 fold change > 1 is used.
- **GO enrichment:** the tool, ontology and background are unstated. The readings are over-representation in Biological Process against the tested genes, or against all annotated genes.
- **Peak count (Figure 1B), PV-associated net region (Figure 1A), and the tests for Figures S2, S5 and S7:** readings are named in each criterion.

**Thresholds I set, not the paper:**
- "Many" GO terms is set as at least 3 of the top 10.
- "Vast majority" of nets eliminated is set as below half of the control mean.
