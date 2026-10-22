I wrote `claims/001361/10.1038-s41593-025-01985-4.yaml` with 50 claims. Every quote passes the checker, but the checker still exits non-zero: it flags two p-values that I confirmed by reading (details under Statistics below).

**Text read.** The version of record is open access, from Europe PMC (PMC12229899). It has the main text, the figure legends, the legends of Extended Data Figs. 1–10 and the Methods. The only supplement file is the Reporting Summary. The Source Data files and the bioRxiv preprint were not read. Nothing the claims need is missing from the text.

**Code read.** GiocomoLab/Sosa_et_al_2024 at commit adf0f9e: the `reward_relative` package and one notebook per figure. The spatial information, its shuffle and the matching of cells across days run in an outside package, TwoPUtils, which the repository does not include. For those, the Methods alone set the method.

**Claims**
- **Quotes:** 48 of 50 claims have one. The other two (Extended Data Fig. 2p,q and Fig. 5d,i) use `inferred`, because their numbers appear only in legends.
- **Statistics:** 14 claims record them, 50 entries in all. Two p-values are printed exactly as I recorded them, but the checker reports them as not found: m12 in Fig. 6e, printed "4.40 × 10 −8", and Extended Data Fig. 3o, printed "8.0e-9". It doesn't recognise the trailing zero.
- **Criteria:** all 50 claims have one, and all use `data: dataset`.
- **Coverage:** behaviour, place-cell and remapping fractions, reward-relative remapping above chance and its growth, decoding, sequences, density and learning, the teleport period, cross-day recruitment, anatomy, rewarded versus omission trials, the GLM, remap timing (Fig. 8 and Extended Data Fig. 10), and the place-field analyses of Extended Data Fig. 3.
- **Tolerances:** a mean ± s.e.m. takes the s.e.m.; a confidence interval takes its half-width. A mean ± s.d. takes 10%, because there the s.d. is the spread across mice and days, not the uncertainty of the mean.

**Details left open, with the readings named**
- **Remapping categories:** the Methods remove reward-relative cells only from the appearing and disappearing groups; the code removes them from every category.
- **Non-reward-relative and unclassified percentages:** taken over all seven switch days, or over the six within-environment days.
- **Fig. 3c range:** either the outermost bins with z > 2, or the continuous run of such bins that contains the reward zone start.
- **Fig. 4m and related mixed models:** on the raw fraction or on its logit.
- **Fig. 4o speed window:** within 50 cm of the reward zone start or beyond it.
- **Licking variance (Fig. 4p):** the legend's wording, or the code's mean over trials of each trial's variance.
- **Extended Data Fig. 5d,i:** averaged over mouse-day rows or over per-mouse means.
- **Fig. 6 cell selection:** peaks between the zone start and the track end (Methods), or any positive offset after the zone start (code).
- **Fig. 8 "mean ± s.e.m.":** the mixed-model coefficients, which equal the printed values; the mean over sessions; or the mean over mice.
- **Behaviour, Fig. 1h:** the paper gives no test and doesn't say what "improved" is measured against. The readings are per switch day, or averaged per mouse.

**Where no source sets the method, so the criterion takes a standard reading and says so**
- "Nearly the entire track" in Fig. 2i: tested up to the 190 cm exclusion distance, the largest the code uses.
- The test for Extended Data Fig. 6a.
- The comparison of across-day with within-day drift.
- The "no reliable bias" rule in Extended Data Fig. 7.
- The one-bin tolerance on the region of over-representation in Fig. 4j.

**Where the Methods and the code disagree, so the code's choice is shown as a variant**
- Circular bins of 2π/44 in the code, against 2π/45 in the Methods.
- Shuffle offset ranges.
- The decoder: all post-switch trials in place of the last 30, and contiguous test folds.
- The diagonal band in Extended Data Fig. 2c.
- The session-acceptance Wilcoxon test in Fig. 8: one-sided in the code, two-sided in the Methods.
- The code applies none of the Bonferroni levels given in the legends of Fig. 6 and Extended Data Fig. 7; the criteria use the legends.

**Not in the code:** Extended Data Figs. 2e,f and 2n, the teleport statistics of Extended Data Fig. 5d,i, the Fig. 3c range, and the "2.1 ± 0.6" summary in Fig. 8. For these the Methods and legends alone set the method.

Nothing was committed, as instructed.
