I wrote `claims/001887/10.1016-j.cub.2025.01.010.yaml`. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript in PubMed Central (PMC11916606): Results and Discussion, the legends of Figures 1 to 4, the STAR Methods and the key resources table. There was no PDF, so I saw no figure. I did not read the version of record.

**Supplement missing.** The text lacks the legends of Figures S1 to S4 and Tables S1 and S2. The main findings rest on Figures 1 to 4, which are in the text, so I went ahead, as earlier runs did for 001868 and 002020.
- Claims about findings shown only in the supplementary figures (S1H, S2, S3, S4) are written from the Results sentence that states them.
- Table S1 holds the F values, the post hoc p-values and the Pearson r and p for Figure 4. Because of that, most claims have no `statistics` and no expected r.
- If the supplement can be supplied, it would fill these gaps.

**Code read.** Zenodo doi:10.5281/zenodo.13351302 (published 2024-08-27, no version or commit). It does not contain:
- the auROC routine (it calls `run_caAnalyze`, from the lab's caAnalyze repository, which the paper does not link; I did not read it);
- the helpers `average_bin`, `Zscore_Sz` and `normalizeSZ`;
- the cumulative histograms and modulation scores, which were done in Prism.

The Rescorla-Wagner script, as deposited, reads a spreadsheet named for another experiment.

**Claims.**
- 40 claims, all with quotes, none inferred.
- 3 have statistics: the three chi-squares of Figure 1K and 1O.
- 5 have expected values: the cell and mouse counts, the 51% against 25% mixed-cell result, and the day 2 platform-exit cell counts.
- 38 have criteria.
- All use `data: dataset`. The paper's own "analysed datasets" on Zenodo (doi:10.5281/zenodo.13381210) are named in the opening comment but no claim uses them.

**Details left open, and the readings named:**
- **End-of-day periods:** tones 9 to 12 (Results and legend) or tones 10 to 12 (Methods). Which frames make up a period: two readings, F1 and F2.
- **Mixed-cell denominator:** responsive cells or all cells. A chi-square near 43 fits only the responsive cells, but both readings are run.
- **Decoding F1 positive class:** success (Methods) or failure (code).
- **F1 normalization:** min-max (Methods) or z-score (the code's `Zscore_Sz`, which is missing).
- **Pre-shock epoch:** 23 to 28 s (Methods); the code's 22 to 27 s is a variant. "Before the tone" uses the code's −5 to 0 s epoch.
- **Figure 3B and 3C:** "enhanced" compared with the all-cell decoder, or with the non-shocked group.
- **Rescorla-Wagner:**
  - the "avoid" learning rate is q, or a·q;
  - which trials are fitted: day 1 tones 4 to 12 plus all of day 2, or all 24;
  - the baseline seed: platform time during tones 1 to 3, or before the first tone;
  - the shock-only and avoid-only models are not in the code; the reading is q fixed at 0 or 1.
- **CILDS:**
  - tone-onset window: 0 to 5 s, 1 to 5 s, or −1 to 4 s;
  - day 2 trials: all 12, or 4 to 12;
  - the code's input signal is used, with ΔF/F as a variant.
- **Trajectory distance:** start-to-end distance on the trial (Methods). The code's mean distance between consecutive trials is a variant.
- **"Following the first successful trial"** (Figure S3E, F): the next trial, or that trial itself.
- **Mixed cells in Figure 1R:** two readings of which mixed cells count as excited.
- **Figure 2 ANOVA input:** per-cell values or per-mouse scores.
- **Sidak comparisons for behaviour:** two readings of which comparisons form the family.
- **Supplementary windows and measures:** the window for escape, jumping and rearing, and the behaviours in Figure S3G, H.

**Inconsistencies in the paper:**
- Non-shocked mice number 7 in the Methods but 9 in the Figure 1 behaviour legend.
- "3 measures" of distance are announced but only two are named.
- The Discussion says Figure 4E to H correlated, while the Results say 4F and 4H did not.
- The Discussion calls Figure 4J trend-level, while the Results report it as a correlation.
- The Methods say "stratified" leave-one-out and fit by maximum likelihood; the code does plain leave-one-out and minimizes squared error.
