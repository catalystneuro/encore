I wrote `claims/001828/10.1101-2024.12.22.629963.yaml` with 38 claims. The quote checker reports 0 problems (37 quotes, 56 statistical values found in the text).

**Text read.** I read the bioRxiv preprint, version 1 (posted 22 December 2024): main text, Results, the legends of Figures 1 to 6, Discussion and Methods. There was no PDF, so I saw no figures.

**Missing from the paper:**
- **Supplement.** Figures S1 to S6, their legends and Supplementary Videos 1 to 3 are not under `paper/`. I went ahead anyway, as the 001544 reader did under the same protocol, because the main findings rest on the main figures and the Methods. Seven claims cite only a supplementary figure; they rest on the Results sentence that cites it, and their tests, n and windows are named open.
- **Code.** The paper's only code link is the Key Resource Table at Zenodo (10.5281/zenodo.14138011). That DOI returns 404 at doi.org and at the Zenodo API, so I read no code. The dandiset links the conversion code (catalystneuro/meletis-lab-to-nwb), which is not the analysis code, and I did not read it.

**Claims:**
- 38 claims, all with a criterion.
- 37 have a quote. Figure 3F-G uses `inferred`, read from the legend's list of significant tests.
- 21 claims carry statistics and 6 have expected values (the ~99% and ~40% overlaps, ~50% Th loss, 37 motifs, R = 0.70 and −0.52, R = 0.83, R = −0.762).
- RNA-seq is `data: elsewhere`, at GEO GSE282753.

**Details left open, and the readings named:**
- **Photometry z-scoring and processing parameters:** whole session or a pre-event baseline.
- **Linear speed:** from the tail base or the mean of the six pose points. The smoothing and the immobility threshold are open.
- **VAME motif labels:** a refit cannot reproduce them, so motif claims need the paper's labels to be in the dataset. Category membership is drawn only in Figure 4C. The text says seven categories, the Figure 4C legend six, Figure 5G five.
- **Reward-window edges (Figure 3D-G):** 1 s windows (−2 to −1, −1 to 0, 0 to 1 s) or 2 s windows. It is also open whether the printed one-sample p are Bonferroni-corrected.
- **Self-stimulation preference:** active over total pokes, or active minus inactive. It is also open which group the Figure 3K-L ANOVA and Friedman test belong to; I read F(4,32) as DAT mice over five days, with six days as the other reading.
- **Speed correlation shuffle (Figure 4B):** random permutation or circular shift. The printed paired t-test p equal exact Wilcoxon p (2/512, 2/256, 2/128), so Wilcoxon is a variant.
- **Motif AUC averaging (Figure 4F-H):** pooled onsets or per recording, with or without a −1 to 0 s baseline subtraction.
- **PCA (Figure 5G-I):** standardized or centred usage. The PC sign is arbitrary, so magnitudes are judged.
- **"All the PD models" (Figure 5J):** with or without Anxa1-TeTx.
- **Maze efficiency:** lateral rewards only, or all drops.
- **Reaching accuracy threshold:** < 0.2 cm in the Results, < 0.1 cm in the Figure 6J legend; both are run.
- **Paper text inconsistencies:** the legends' "Day 1 vs. Day 2" is read as day 1 against day 4, the days plotted. Figure 5M gives n = 3 mice against n = 14 elsewhere for Anxa1-TeTx.
- **Missing test or n:**
  - The test for FR5/PR and iPSC is not given; I used the Methods' unpaired t-test.
  - The VTA tests are not given; I used the ANOVAs of the matching SNc panels.
  - The intensities and windows of the Figure S2 evoked release are not given.
  - For the RNA-seq pipeline I named DESeq2 as the standard reading.

**Thresholds I set myself, where the paper gives none:**
- The 10% bound for "near-complete" axon loss (Figure 2N).
- The similarity rule for Figure 5E.
- Spearman within action categories for Figure 4E.

The reviewing reader should check these first.

Nothing is committed.
