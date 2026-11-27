The claims file for yang-2025 is fit for an attempt (`ready: true`). I made six small corrections from the paper and left three open questions recorded in the file.

**Checker:** `claims/yang-2025.yaml: 19 claims, 17 quotes, 15 statistical values, 0 problems`, both before and after my edits.

I checked every claim against the text and against the PDF figures and supplement images. The figure readings match the paper: the Figure 3A bars, target boxes and 11 significant pairs; the stars in Figures 3B, 4B and 5B; the Figure 4A windows; the Figure 2 seizure counts (9, 9, 7, 9); the Figure S2 target table; and Table S1. All five key findings listed in the Discussion have a claim, and nothing comes from outside this paper.

**Changes, by claim**
- **fig2-r1-target-shifts:** removed the expected seizure count (34, tolerance 0). The claim does not rest on it, and its own criterion says a different count does not decide it.
- **fig3a-per-rat-site-differences:** the `about` of the Kruskal-Wallis entry now says the p bound comes from the pairwise marks in Figure 3A. The paper prints no overall Kruskal-Wallis p per rat.
- **fig3b-same-site-target-vs-nontarget:** fixed how the criterion quoted Methods G. Methods G lists Mann-Whitney with the paired t-test "for two paired samples", not for independent samples.
- **fig4b-psd-target-bands:** the criterion stated Dunn's follow-up test as the paper's method, but the paper names only Kruskal-Wallis. It is now marked open, with adjusted and unadjusted readings.
- **fig6e-ictal-ripples-no-difference and fig6f-ictal-fast-ripples-reduced:** the claims missed a conflict in the figure. The axis labels of Figure 6E-F call the red point "Non-target stim" and the yellow one "Target stim". That goes against the colours used in every other figure (red is target) and against the Results text. The criteria now say this and follow the colours, which the text supports.

**Still open** (named in the file, readings kept)
- **Which bands rise after target stimulation:** the Results text says alpha and beta; Figure 4B, the Abstract and the Discussion say theta and alpha.
- **The R7 mark in Table S1** ("0.71±0.41* **") could be one, two or three stars. This does not change the outcome, since the criterion only needs p < 0.05.
- **Details the paper never gives:** the normalization formula, the sign of cf_w, the Granger causality settings, the unit of analysis, and how the "paired" t-test in Figure 6 is paired.

Only `claims/yang-2025.yaml` was changed, and nothing was committed. To view the figures I installed PyMuPDF into `$TMPDIR`, because no PDF renderer was available.
