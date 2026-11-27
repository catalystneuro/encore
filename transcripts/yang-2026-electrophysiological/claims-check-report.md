I made three corrections and added a check entry. The file is ready for an attempt (`ready: true`). The checker still reports one problem, which is not an error in the file.

**Checker:** `21 claims, 21 quotes, 2 statistical values, 1 problems`. The problem is `VALUE NOT FOUND (confirm by reading) fig5a-longpc2-ramppc1-centroids 0.002`. That p-value is printed inside Figure 5A, not in the text, so the checker can't find it. I confirmed it in the PDF: Spearman r = 0.883, p = 0.002, n = 9. No PDF renderer was installed, so I installed PyMuPDF into a temporary folder to read the figures and the supplement.

**Changes, by claim:**
- **fig4a-brief-response-variance:** reading (b) of the criterion was wrong. It said Figure 4C adds only one feature (lower-quartile peak response) to Supplementary Table 1. Figure 4C names 10 features, three of which are not in the table: maximum fast-response mean, lower-quartile peak response and mean peak response. Reading (b) now lists all 10.
- **fig2b-longpulse-continuous-biased** (fig3b and fig4b inherit it): the paper gives no test of the "biased occupancy" finding. The criterion borrowed the label-shuffle test from Methods 6 and set a 5% level, but read as if that were the paper's method. It now says both are the file's own choices.
- **fig3e-ramp-recruitment-current-order:** the criterion stated as fact that recruitment current is the command current at the first spike. The paper never defines it, so this is now marked as a reading.
- **No change needed:** every value read off a figure matched the plots: Figures 1C, 2A, 2C, 2E, 3A, 3E, 4A, 4E, 4F, and 5A to 5F. The loadings in Figures 2D, 3D and 4C also match.

**Coverage:** each main finding of the paper has a claim, and every claim comes from this paper.

**Still open (recorded in `checks`):**
- **Figure 1D and the other figures disagree:**
  - Figure 1D prints 7 driver lines shared by all three protocols, but the lines named in Figures 2 to 4 give 8.
  - Figure 1D labels a circle "Short pulse" where the ramp geometry is meant.
  - Figure 4B's legend lists 9 lines, while Figures 4D and 4F show 11.
- **Details the paper never gives:** feature-set membership, quality-control thresholds, spike detection, response windows, how many PCs are used for centroids, and all the balanced-resampling settings. No code is public, so the claims carry these as named readings.

Nothing was committed or pushed.
