I've written `claims/martinez-conde-2019.yaml`. The quote checker reports 19 claims, 14 quotes, 2 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (PMC6438452, from the Europe PMC full-text XML). That covers the main text, Methods, figure legends, Table 1, and the legends of S1–S4 Fig and S1–S2 Table. The supplementary files themselves are not there, and the paper links no analysis code, so I read none.

**Counts:**
- 19 claims; 14 have quotes. The other 5 are the Table 1 rows, marked `inferred` because no sentence states those numbers.
- 3 claims record statistics, as 2 entries: the Wilcoxon rank sum test with Benjamini–Hochberg correction for Fig 4B (p < 0.05), and the Wilcoxon rank sum test for Fig 6 (α = 0.05, not significant).
- Every claim has a criterion, and 9 have expected values. Where Table 1 gives a SEM, the tolerance is that SEM; neuron counts get zero tolerance; and the R² of the Fig 7A fit gets 0.0017, since 10% of a value near 1 tests nothing.

**Details the paper leaves open, and the readings named:**
- **Corners (S40) midpoint:** (a) the average of the two S40 fold midpoints, or (b) the one fold at the centre of the region analysed. The text states averaging only for Square and Star.
- **S4 baseline test (no difference across stimuli):** the test is not named. Readings: (a) pairwise Wilcoxon rank sum with Benjamini–Hochberg, (b) Kruskal–Wallis, (c) one-way ANOVA. If they disagree, (a) is preferred as the paper's own test elsewhere.
- **Fig 4A mass centre:** (a) mean of the raw values, or (b) mean of the log values, since the axes are logarithmic.
- **Fig 4B correction family:** (a) all six pairs of folds, or (b) only the three pairs the text names.
- **Table 1 order of summary:** (a) per-neuron minimum, maximum, mean and median, then averaged over neurons, or (b) the same summaries of the population-average profile. For S90 and S52, the two symmetric halves of the fold are either (i) averaged block by block or (ii) treated separately.
- **RMS contrast (Fig 7A):** (a) luminance standard deviation divided by its mean, or (b) standard deviation of luminance normalised to 0–1.
- **Fig 7C percent scale:** (a) Edge luminance in percent, or (b) RMS contrast × 100. Under (b), 50% falls below the measured range of 0.61–0.943.
- **Fig 7C t-test correction:** Benjamini–Hochberg or Bonferroni, over 40 tests or 10 per fold, at α 0.05. "Less than 68%" is read as the levels 0.610 and 0.647.
- **Fig 7D:** the paper gives no test for non-linearity or for similarity to the model, so both criteria are assumptions I named:
  - Non-linearity: a straight-line fit, judged on whether any mean lies off it by more than its SEM.
  - Similarity to the difference-of-Gaussians (DOG) model: same rank order and Pearson r > 0.9.
- **Minor:** Fig 6 is taken as uncorrected (no correction is stated), and for the latency peak, "around 60 ms" is read as 30–150 ms.

**Missing from the paper that claims needed:**
- **S1 Table:** the exact p-values for Fig 4B.
- **S2 Table:** the Fig 7C t-tests, including their correction, confidence intervals and t-values.
- **The reference list:** so the DOG model output of reference [3], needed for the Fig 7D similarity claim (`fig7d-dog-similar`, marked `with_inputs`), can only be named by number.

The main text states every finding these tables support, so I judged that they did not block writing claims.

The S3 Fig latency claim needs spike times and eye positions. The criterion notes it cannot be tested if the dataset holds only maps computed at 60 ms.
