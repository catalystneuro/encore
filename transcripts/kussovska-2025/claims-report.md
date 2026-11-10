I've written `claims/kussovska-2025.yaml`: 45 claims, every one with a quote. The quote checker passes except for one p-value it can't parse: the paper prints "9.70 × 10−12" (fig3h, Dunn early vs late), which I confirmed by reading. Nothing is committed.

**Text read.** The bioRxiv full-text page of the preprint posted 1 November 2025 (doi:10.1101/2025.10.31.684900). Its header says "version of record", but the page offers a "current version", which I did not read. It holds the main text, the legends of Figs 1 to 6, and the full Methods. No PDF was supplied.

**Missing from the text.** The Extended Data Figs 1 to 5 and their legends, and the Source Data. The main findings are all stated in the main text, so I went ahead. The 9 claims on Extended Data panels rest on the main-text sentences that cite them and are marked "(not in the text read)". A few Methods equations were also lost in extraction (the GLM link, and the peak and prominence formulas for bursts).

**Code read.** github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last commit before the preprint. The later REVISIONS folders (2026) were not used. Three things in it bear on most claims:
- The matched trial sets (96 trials per participant matched on load, 75 matched on image) come only from xlsx files shipped in the repository. No code builds them.
- The autocorrelogram features are computed in MATLAB, but the spike input file is an empty placeholder. Only the output table `Cell_metrics.xlsx` is shipped.
- The README downloads dandiset version 0.240123.1806, while the paper cites 0.231213.2047.

**Counts.**

| Field | Claims |
|---|---|
| Quote | 45 |
| Statistics | 29 (74 values) |
| Expected values | 20 |
| Criterion | 45 |
| Inferred | 0 |

All claims use the dataset except `supp4-rodent-validation`, which is `data: elsewhere`: it uses the CellExplorer ground-truth rodent data, for which the paper gives no archive identifier.

**Details left open, with the readings named:**
- **GLM trials (Fig 1e,f; Fig 6e,f):** the 96 load-matched trials from the code's xlsx, or all trials.
- **GLM permutation:** within participant (Methods) or over the shared trial vector (code).
- **GLM RT predictor:** each trial's own RT, or the subject-1 RT vector the code uses for every neuron.
- **Concept-cell bootstrap:** the Methods version, or the code's (both groups resampled to the smaller size, a different p formula). The code sets no seed, so ten seeds per reading.
- **Behaviour:** RT summary (three readings); which p for Fig 1c (raw or Bonferroni); what is permuted in the two RT tests (no code exists for them).
- **Persistence:** what counts as single-cell and population persistence (two rules each).
- **Cross-temporal decoding:** one- or two-sided binomial; cluster-duration null (Methods) or the code's contours longer than 13 points; first image or last image as label for loads 2 and 3.
- **Maintenance decoding:** at least 3 (Methods) or more than 3 (code) concept cells per participant.
- **Bin-width decoding:** trial alignment, the code's xlsx or rebuilt from the dataset. The pairwise bin-width tests have no code, so two permutation schemes.
- **dPCA:** Kruskal-Wallis over 5 groups (code) or 3. H = 457 is only reachable with 5. The same or the code's trials for maintenance (the code selects them by the wrong id column). Smoothing sigma 120 ms (Methods and code) or 60 ms (Results). The early/late "protect time" setting.
- **Bursts:**
  - Peak rule: smoothed value above the 90th percentile (Methods) or prominence at that percentile (Results and code).
  - Surrogate threshold: the real data's or each surrogate's own.
  - Neuron groups: median split with at least 5 neurons (Methods) or the 6 lowest and 6 highest with at least 10 (code).
  - "All neurons": all 902 or the 294 fitted.
  - M1 to M3: 1 s windows in each trial (Methods) or thirds of the concatenated train (code).
  - The Fig 6a,b null: label-shuffled (Results) or Poisson (legend and code).
- **ACG and cell types:** which spikes enter the autocorrelogram; R2 > or ≥ 0.3; CV2 as Holt's local measure (Methods) or plain CV (code); whether the printed values are means or medians; load 1 or all loads for the CV2 and decay-constant tests.
- **Qualitative claims:** a measure is named for trajectory complexity and for the "minimal", "little effect" and "increased with load" statements in the Extended Data claims.

**Missing for specific claims:**
- **No code for these tests:** the RT tests and the pairwise bin-width tests. The per-trial-type decay constants exist only as a shipped xlsx, tested there with a t-test where the paper names a Wilcoxon test.
- **The trial-selection rule** behind the matched pseudo-population trials is in neither the paper nor the code.
- **No published rule** for the qualitative claims; the measures named above are readings, not the paper's.
