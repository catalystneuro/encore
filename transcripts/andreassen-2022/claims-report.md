I wrote `claims/andreassen-2022.yaml` with 28 claims. Every claim has a quote, none needed an `inferred` note, and nothing was committed.

The checker passes every quote and the schema but still exits non-zero on three p-values: 0.233 in Table S1, and 0.008 and 0.030 in Table S10. Those numbers exist only in table images, so the checker can't find them in the text. I read them on the rendered pages and say so in the file's opening comment, the way allen-2026 handles its one unfound value.

**Text read**
- **Main text:** the version of record (PMC9522358, Europe PMC JATS): Results, figure legends, Discussion and Methods.
- **Supplement:** the SI Appendix, with the legends of Figs. S1 to S4, the SI Statistical Analyses and the captions of Tables S1 to S10. The table bodies are images and are missing from the `.txt`. I rendered PDF pages 6 to 11 with PyMuPDF, installed in a temp folder, to read them.
- **Code:** not read. The R script is one of the files in the figshare item, and I was told not to open the dataset's files. The opening comment asks the author to read it.

**Counts:** 28 quotes; 19 claims with statistics (32 p-values); 28 criteria. Six of the criteria have no reported test behind them, and the criterion sets the measure.

**Details the paper leaves open, and the readings named**
- **Mixed-model p-values:** the paper doesn't say how lme4 models got p-values. Main reading is Satterthwaite tests via lmerTest; for Fig. 3D that equals a paired t-test with 6 df, which gives p ≈ 0.004. A normal approximation is shown as a variant.
- **Outlier removal (Fig. 5A, Table S3):** quartiles taken within each group or over all fish. The models with all fish are shown as variants. They matter: with all 76 fish neither oxygen effect on CTmax is significant, and with all 16 adults the adult CTmax differs from 5 dpf (p = 0.038).
- **Adult mean CTmax:** over 15 fish or 16.
- **Binning:** time bins (Fig. 2F) and temperature bins (Figs. S2A, 5D, 6C) are not given. 1 °C bins are used as a standard choice; deposited bins are used if present.
- **Peak values (3.6, 2.5, 3.3 peaks/min):** the peak of the group mean curve, or the mean of per-fish maxima.
- **Q10:** neither the formula nor the endpoints are given. Read as the standard formula on group means, with the endpoints the sentence names; per-fish Q10 is shown as a variant. The 0.02 in hypoxia is judged as below 0.1, with the reason stated.
- **Chi-squared test:** whether the continuity correction was used. The reported 15.6 matches R's default corrected statistic for the counts in Table S2; the uncorrected test is shown.
- **Wilcoxon effect size r:** read as |Z|/√N.
- **Swim speed (Fig. S1A):** Table S1 fits only a treatment main effect, while the legend speaks of the change over time. The model with a time × treatment interaction is shown as a variant.
- **"Stable before / during depolarization" (heart rate):** judged on the Table S6 contrast of the depolarization category against 37 °C.
- **Light-response threshold:** which SD the "2 SD above F0" uses. Read as the SD of the 2 s pre-flash signal.
- **Pooling:** percentages pooled over flashes or averaged per fish; mean temperature in Table S10 over all flashes or per treatment.
- **"Sharp" drop before depolarization (Fig. S3D):** window of 2 or 5 min. The threshold of half the group's maximum is set in the file, since the paper doesn't quantify "sharply".
- **Depolarization magnitude ratio and Fig. 2E spread timing:** no method is given. Readings are named in each claim.

**Missing from the paper:** nothing a claim needed. The text has four inconsistencies, listed in the opening comment:
- Fig. S1C's legend swaps the heat-ramp and control n.
- Fig. 2F's legend says 50 min before depolarization; the SI says 42.
- The Methods say "experiment 2" for the freely swimming imaging, which is experiment 3.
- Fig. S3D and Fig. 5D give different n.

The figshare item is CSVs plus an R script (about 0.1 MB), so derived values only. Claims that need imaging (the Fig. 2E spread timing, the depolarization magnitude ratio) are likely untestable.

The git status also shows untracked files I didn't create (dotfiles, `.idea`, `.vscode`, `scripts`); I left them alone.
