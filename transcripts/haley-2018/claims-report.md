I wrote `claims/haley-2018.yaml` with 30 claims, and the quote checker passes with 0 problems. Nothing is committed.

**Text read.** I read the version of record from Europe PMC (PMC6328273, JATS converted to plain text). It has the main text, all figure legends, the legends of the figure supplements, the Methods and the data statement. No PDF was supplied. I also read the paper's code at github.com/jesshaley/haley_hampton_marder_2018, commit 83f5904.

**Counts.**
- All 30 claims have word-for-word quotes, so none needed an `inferred` note.
- 19 claims carry statistics, 32 entries in all. The checker found 22 of their p-values in the text.
- 30 criteria. Two claims also have expected values: the gastric-rhythm counts (10, 4, 5 and 7 of 15) and the Figure 8B counts (14, 6 and 3 of 15), each with a 10% tolerance.
- Every claim uses the dataset itself; none needs outside data.

**Details the paper leaves open, and the readings named:**
- **Two-way ANOVA (Figure 8).** `statistics.R` at this commit leaves out the ganglion term and could not have produced the paper's table. I took the model from the Methods. The open choice is how ganglion is coded in the Type III test: (a) sum-to-zero contrasts, (b) R's default treatment contrasts. The post hoc tests are Welch t-tests, as in the code.
- **Analysis window.** The code's "last 8 minutes" mixes seconds with sample counts, so it takes 480 s from the first burst of each file. The Methods' last 8 min are the main reading; the code's window is a variant.
- **PD burst frequency with picrotoxin.** The Methods measure it trough to trough; the code uses peak to peak. The code's version is a variant.
- **Words with no test behind them.** I named two readings each for:
  - "increased in acid" for the example preparations: extreme step against control, or the sign of a Spearman correlation across steps.
  - "rarely" and "usually" for state transitions: under 10% or 20%, and a plurality or a majority.
  - "similarly variable" at control: a range-based comparison, or Kruskal-Wallis across preparations.
  - "likely" for gastric rhythms co-occurring: a comparison of fractions, or a Fisher test.
  - "ceased firing", "reductions", "every pH condition" and "rhythmically bursting" in Figure 8B: two or three readings each.
  - which window counts for the gastric rhythm: whole step or last 8 min.
- **Baseline frequency correlations.** The data source (15 extracellular preparations, or the 9 picrotoxin preparations), the correlation (Pearson or Spearman), and "strong" (p < 0.05, or r of at least 0.7) are all open.
- **Figure 7C.** The text does not say whether the acid ANOVA was significant, so the claim holds under either reading.
- **Unnamed examples.** STG #2 and #3, CG #2, and the examples in Figures 4A and 5 are not identified, so those criteria look for any preparation that fits. The code does identify STG #1 (897_037) and CG #1 (877_149 CG2L).

**Missing from the paper:**
- The four statistics tables (Figures 3, 4, 7 and 8, supplement 1) are images with only their legends in the text. So no F, t or exact p values are recorded; the statistics hold only "p < 0.05" bounds.
- The source data files are not in the text read.
- The state annotations (`stateData_STG.xlsx`, `stateData_CG.xlsx`) are not in the code repository. If the dataset doesn't hold them, every state-based claim needs manual annotation from the paper's definitions.
- The paper gives no count of picrotoxin preparations; the code lists 9.
- The legend of Figure 3, supplement 2 says "CG" where it means STG; I followed the Results and the code.
