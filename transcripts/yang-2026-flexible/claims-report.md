I wrote `claims/yang-2026-flexible.yaml` with 29 claims. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** I read the version of record (eNeuro, PMC13737997): main text, Methods, Results, Discussion, Tables 1 and 2 (rows a to y), and all figure and Extended Data legends. The Extended Data files themselves (TIF figures, DOCX Tables 1-1, 2-1, 3-1, 4-1, 4-3) are not in the text, and there was no PDF. No claim needed them: every expected value is printed in the main text or Table 2, and the feature lists of Table 1-1 come from the paper's code instead.

**Code read.** github.com/zy-neuro/protocol-response-geometry at commit 61a5a41: the analysis scripts, the curated gene list, and derived tables (PCA scores, retained features, and the table joining NWB files to t-type, Cre line and sample ID).

**Counts.**
- 29 claims, all 29 with quotes and none inferred.
- 8 claims carry statistics, 26 statistical values in all (permutation p floors 0.0099, 0.020 and 0.000999, plus three 95% intervals).
- All 29 have criteria and 23 have expected values.
- 8 claims use the dataset alone. 21 are `with_inputs`, because they need t-type, Cre and subclass labels or the gene counts from the NeMO Patch-seq release 20200611 (count matrix v2).

**Details the paper leaves open, and the readings named:**
- **Full-cell feature extraction.** The script that ran IPFX on all cells is not in the repo, so the IPFX version and call are open. The reading is the code's split-half feature packing with the current IPFX, with the Allen pipeline's version as a variant.
- **Which cells enter a regime, and the denominator of the 30% missing-value rule.** Either cells with any non-missing feature of that regime (as the code does), or all cells that passed extraction.
- **Cell-pair sampling.** The Methods say "unique" pairs; the code's draw can repeat pairs. The Methods reading is the main one and the code's is a variant.
- **Spearman ties in A_t.** The code ranks without averaging ties. On a binary label distance this shrinks the correlation well below an average-rank Spearman. I followed the code; average ranks are a variant.
- **Neighbor enrichment.** Ratio of means (the code, used) or mean of per-cell ratios (variant).
- **Cell set for Cre eta squared and the Cre-residualized A_t.** Cells with both labels (the code) or all cells with a Cre line.
- **Null for transcriptomic distance against phenotype.** Shuffle values across pairs one-sided, the same two-sided, or shuffle t-type labels and recompute (the Methods' wording). The 1,000-shuffle file the paper reports has no script.
- **Equal-N "well above nulls".** Either each 2.5th percentile is above the null's maximum, or each mean is above the null's 97.5th percentile.
- **"Proportions stable" under threshold changes.** The cutoff grid is fixed from the figure code. The two readings are a minority-selective test and a step size of at most 10 percentage points.
- **"Increased with k".** A rise at every step of the grid, or k = 600 above k = 15.
- **Subclass concordances 0.579 and 0.621.** Which brief-pulse pair each belongs to is open.
- **"Channel programs" for the Kv3 claim.** The seven channel modules, or all nine excitability modules.
- **Figure 2B.** The paper gives no test. I judge it with the paper's within-Cre A_t and eta squared; per-type PC1 medians are shown but not judged.
- **Residual t-type eta squared.** No value is printed; it is judged against the paper's 100-shuffle label null.

**Missing.** No claim lacked a text the paper rests on. Within the code deposit, two things are absent: the full-cell IPFX extraction script (and its feature table), and the script behind the 1,000-shuffle transcriptomic null.
