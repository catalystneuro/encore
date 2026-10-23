The file is ready for an attempt. I made 11 changes and left 3 points open. Nothing was committed.

**Checker result:** `claims/000678/10.1016-j.celrep.2024.113709.yaml: 29 claims, 29 quotes, 37 statistical values, 0 problems`. The first run, before my edits, also passed (28 claims, 28 quotes).

I read the full paper text, its supplement legends, and the paper's code from Zenodo (doi:10.5281/zenodo.10306018). The quotes, statistics, expected values and tolerances match the paper. The code checks I made mostly agree with the file: the Figure 2 and 4 stars, the transition windows, how the number of states is picked, the prediction-accuracy procedure, the optimal-pupil fit, the decoding script and the Figure S8 regressions.

**Changes, by claim**
- **Header:** the GitHub commit it cites lacks FigureS7.py and FigureS8.py; these exist only on Zenodo, and the header now says so. The note on the movement index now says it is z-scored over different sets of trials in different scripts.
- **distractor-response-rate:** added a reading pooled over all mice, since the paper does not say whether the 10% bound is per mouse.
- **fig2c-dwell-times:**
  - The source "Discussion, paragraph 3" cannot be located in the text, so it now names the paragraph by its first words.
  - The code counts each dwell as one trial longer than the run (one shorter for a session's last epoch). That count is now a reading next to the run length.
  - The indeterminate dwell also counts the gap from session start and direct transitions as zero; this is now stated.
- **fig4b-variability-at-transitions:** "optimal epochs of at least 10 trials" was wrong. The code's cut is a dwell above 9 in its own count, which is a run of at least 9 trials (at least 11 for a session's last epoch).
- **fig5c-state-classification:**
  - The "All measures" points in Figures 5 and S7 are the run with the movement index and its SD shuffled in training. This is added as a code variant.
  - The significance reading changed from z > 1.96 to z > 1.98, the dashed line Figure5.py draws.
- **figs7-pupil-best-raw-measure:** the file said the paper does not say which comparison gives the p-values. The Figure S7B legend does (p = 0.004 and 0.14). Both readings stay, because the Results print 0.106 where the legend prints 0.14.
- **fig5c-movement-index-best:** in the final Figure5.py, the "Movement index" label lands on a run that also keeps pupil. Added as a further variant.
- **figs1-iti-independence:** the evoked-response readings (4 s windows) were made up. FigureS1.py defines the measure: the larger signed change from the onset value within 2.5 s, as a per-mouse median per state. Its plot includes the indeterminate group. I rewrote the criterion from the code, defined the inter-trial interval as start-to-start, and marked the 0.1 and 0.2 cut-offs for "weak" as not from the paper.
- **New claim, fig3f-movement-index-u-disengaged:** the Figure 3F legend's U-shaped link between the movement index and the disengaged state had no claim.

**Open**
- Several claims judge shapes or words like "nearly all", "highly", "weak" and "consistently" with cut-offs and fits the paper does not give. They are named as readings, but a reader chose them: fig3c, fig3e, the new fig3f claim, figs5, figs8a and figs1.
- For Figure 2D, the Results name a signed-rank test and the legend a rank-sum test. Signed-rank is kept, because p = 2.4e-4 is the smallest exact signed-rank value possible for 13 mice.
- Neither the paper nor the code fixes the threshold for "stationary" trials, or which sessions feed the per-state means of the Results' paragraph 4.
