The claims file for DANDI:001051 is ready for an attempt. I corrected eight claims from the paper and left three problems open.

**Checker result:** `45 claims, 45 quotes, 16 statistical values, 1 problems`. The one problem is figs6-replay's p = 1.8e-6. The value is right: the text prints it with a garbled minus sign ("1.8e�6"), and I confirmed it by reading.

**Changes, by claim:**
- **figs6-replay:** The statement now says "weakly but significantly correlated", as the paper does. I added a note to the criterion: r = 0.77 with p = 1.8e-6 fits about 28 points, which matches the S6F inset (7 sessions of four points each). A per-unit correlation over hundreds of units would give a much smaller p.
- **fig7f-mop-network:** The statement said "intermediate layers" of the superior colliculus. The paper says "deep layers of the superior colliculus (SCiw)", so I changed it.
- **fig6ef-optotagging-mrn:** The two readings of the tagging test described the same 10 ms window. I replaced them with a detail the Methods really leave open: which trials enter, since trials ran at several laser powers (all powers pooled, or each power separately).
- **fig4ef-rf-fraction-stable:** Added that Figure 4E prints p = 0.39 where the text says 0.38. Both are reported.
- **figs4ab-insertions-per-mouse:** The Figure S4A legend counts insertions "over all recording days", and 467 insertions over 25 mice give at most 18.7 per mouse, below the paper's 20. Which sessions count is now open, with two readings: the 87 QC-passing sessions, or all sessions.
- **fig7b-low-arousal:** The text gives the ~25% pupil change without naming the area, but the criterion tested VISp only. I added readings for VISp events, MOp events, or both pooled.
- **fig4g-visual-responses-similar:** The expected unit counts were labelled "units with significant RF", but the Figure 4G legend gives only unit and mouse counts. I relabelled them and noted that the RF selection comes from the code.

All changes are recorded under `checks` with their reasons, and the entry has `ready: true`.

**Still open (recorded in the file):**
- **fig3fh-mri-deformation:** The text does not say which pairs in Figure 3H carry the asterisk, and I could not open the figure here. The existing readings stand.
- **fig4d-qc-metrics-comparable:** Reading (a), the code's Mann-Whitney test, is significant in the code's own printed output, so the two readings will probably disagree and the claim end up `methods_underspecified`. Reading (b), medians within 10%, is a standard choice that does not come from the paper.
- **fig7e-lags-straddle-zero:** The paper names no test. The criterion uses the code's signed-rank test, which is significant for all seven pairs in its printed output, while the paper's "straddled zero" may describe the spread of lags. I left it as written because the code is the only source of a test.

I could not read the linked analysis code, so the claims' references to specific code cells are taken on trust. Each of the paper's main findings has a claim, and every claim comes from this paper. Nothing was committed or pushed.
