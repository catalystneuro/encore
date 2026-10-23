The claims file for DANDI:001065 is ready for an attempt. I made eight corrections and added one claim; the changes are not committed.

**Checker result** (after my edits): `41 claims, 41 quotes, 22 statistical values, 0 problems` (it was 40 claims, 25 statistical values, 0 problems before).

I also downloaded the paper's code record (Zenodo 13749343). The values the criteria quote from it match what the code produced, with one exception: the count in `fig6a-area-variation`. That includes the area-ANOVA p values and means, the 4 nA test outputs, the morphology classifier scores, and the uncorrected interaction p values used for Figure S3D.

**Changes, by claim**
- **cohort-animals:** removed the comparison with "the 57 the archive lists". That number comes from the dataset's metadata, not the paper.
- **fig4h-patchseq-genes-et, fig1-snrna-genes-et, fig1-snrna-genes-area:** removed the `statistics` entries. The FDR p < 0.05 there is the cut-off used to count genes, which is a method, not a result. The criteria still use it.
- **fig6a-area-variation:** changed the count from 21 to 19. The paper's deposited table has corrected area p < 0.05 for 19 of its 40 features. I also noted that the notebook's current feature list adds three AHP features the table lacks, so the analysis uses the 40.
- **fig5-tap-root-dendrites:** "extended ~1.4 mm from the soma" can mean straight-line or path distance, so both are now listed as readings. The rule for the temporal cortex neurons is marked as the reader's own, since the paper gives no measure.
- **figs6d-equal-max-instantaneous:** the statement's first part (higher instantaneous rates in temporal cortex below 1 nA) had no criterion. It is now shown but does not decide the outcome, because the paper reports no test for it.
- **fig6-depolarization-block:** the "partially" outcome rested on a Fisher test the paper does not report. That test is now only a variant.
- **figs7g-modal-rates-long-isis:** the paper gives the temporal cortex value as an upper limit ("no TCx neurons … greater than ~8 Hz"). The criterion now requires at most 8.8 Hz instead of a value between 7.2 and 8.8 Hz.
- **patchseq-genes-area (new):** the paper's Patch-seq finding of 43 genes differing between motor and temporal cortex L5 ET neurons, 10 of them also found in the snRNA-seq data, had no claim.

**What remains open**
- Four claims judge vague words in the paper with measures the earlier reader chose, because the paper defines none: `fig3a-cs-with-l5et` ("exclusively distributed with"), `fig3-spc-classifier` ("similar"), `fig4-interaction-small` ("small") and `fig5-tap-root-dendrites` ("lacked").
- `figs7-cv-isi-higher-mcx` and `figs7-oscillations-with-blockers` don't know the ANOVA's second factor. The paper does not name it, so the criteria read it as bins of spike count, with bin edges the paper doesn't give.
- The Figure 7 oscillation claims rely on standard choices, because the paper's R analysis code was not deposited.
