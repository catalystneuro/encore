The checker's result line is: `claims/001347/10.1126-science.adt3971.yaml: 56 claims, 55 quotes, 195 statistical values, 1 problems`. That one problem is not a real error. It is fig2i's p-value 1.8e-09, which Table S3 prints as "1.80e-09" (factor 1, pre against infusion), so the value is in the paper.

**Changes, by claim**
- **fig2i-ketamine-reduces-factors-1-2:** the claim said factors 0, 4 and 5 are not significantly changed. That is true only for the main test (infusion against the mean of pre and post). Table S3's post-hoc tests are significant for all three (factor 0 p = 0.036; factor 4 p = 2.99e-04 and 0.046; factor 5 p = 0.010). I limited the statement and criterion to the main test, and the post-hoc results are now reported too.
- **figs37b-fast-unchanged-across-bands:** added the seven post-against-ketamine tests from Table S3. The criterion judges each band on both tests, but only the pre-against-ketamine tests had been recorded.
- **fig6f-mouse-fast-activity-unchanged:** added Table S3's means (4.48, 4.59, 4.32) as expected values, with the reported s.e.m. as tolerance.
- **fig5e-mouse-emotion-dimension-late-reduced:** the criterion said the fast dimension was built from "puffs 5 to 8". The Methods say "last 4 trials" with 200 ms windows. I added the windows, named the reading of "last 4 trials" as open, and added the other reading as a variant.
- **fig1m-mouse-late-closure-accumulates-and-persists:** noted that Table S3 labels the 100 trials "Preinfusion".
- **figs2bc-mouse-ketamine-early-present-late-abolished:** noted that the fig. S2B and S2C legends say 18 trials per mouse where Table S3 says 15.
- **New claim fig4g-mouse-slow-clusters-altered:** ketamine changes the slow neuron clusters but not the fast ones (Fig. 4G and its Results sentence). This main finding had no claim. The paper gives no test, so the measure of change is named as a reading fixed here.
- **New claim fig5d-mouse-emotion-dimension-accumulates:** activity along the emotion-like dimension builds up over the eight puffs, lasts tens of seconds, and does not build up on ketamine (Fig. 5D). This had no claim. The comparison windows are named as a reading fixed here.

Everything else matched the paper: the other Table S3 values, the Methods details I spot-checked (cluster test, coding dimension, timescale, phase locking, oscillation detection, mouse epochs, coding dimensions and d′ thresholds), the legends, the sources and the quotes.

**Still open**
- The Fig. 5H and 5I variance-explained values (0.870 and 0.927) can't be assigned to ketamine and PCP from the text, so fig5g keeps both assignments.
- I could not read the code the criteria cite (Zenodo 14920570 and 14876694) in this run, so those details are taken as the first reader wrote them.
- I left three minor findings without claims: ketamine raising within-region correlations at rest (figs. S29 and S30), shorter persistence for the tone than for the eyepuff (fig. S34F), and regional over-representation of clusters (fig. S31B).

**Ready:** yes. The `checks` entry at the end of the file records all of the above with `ready: true`. Only the claims file was changed, and nothing was committed.
