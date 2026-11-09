The claims file for CRCNS:pfc-1 is ready for an attempt. I made four changes to existing claims and added two claims for findings nothing covered.

**Checker:** `34 claims, 34 quotes, 27 statistical values, 0 problems`. Before my changes it reported 32 claims with 0 problems.

I read the paper and its supplement in full. I also cloned the paper's code at the commit the file cites (cxrodgers/Rodgers2014, 390b608) to check the methods the criteria take from it. Spot-checked, they match: the error-trial stimulus categories, the hold windows, the multiple-comparison corrections and the disruption session test.

**Changes, by claim**
- **evoked-beyond-baseline-rare**
  - The expected tolerances (0.6 and 0.4 neurons) contradicted the criterion's own band of 5 to 7. I set both to 1 neuron, and the Rat 1 condition is now 3 to 5 units that are also a majority.
  - The statement says the effect is higher in pitch discrimination, but the criterion never tested direction. It now does, reading "these neurons" as the Rat 1 units.
  - The criterion now says the Benjamini-Hochberg correction comes from the code, since the Supplement names none. The uncorrected count is shown as a variant.
- **figs5hi-stimulus-pairs:** the statement now also says no stimulus pair's change differs from zero. The S5H legend states this, and the claim's statistics and criterion already tested it.
- **fig2d-block-switch (new):** rats switch rapidly at block changes, and performance dips during cue trials and recovers within a few trials (Results paragraph 2, Figure 2D). The method follows the code's script for Figure 2D. The paper gives no number for the dip or for "a few trials", so the thresholds are named as my choice.
- **figs2c-s3c-hold-by-trial-type (new):** hold activity does not differ among correct go, correct nogo and go-on-nogo trials, while interference trials differ from all of them (Figure S2C and S3C legends). The test is a paired Mann-Whitney with Bonferroni correction, as the legend and the code say. It has no statistics entry because the legends print no p-value.

**Still open (recorded in `checks`)**
- `fig3d-pfc-interference` and `figs2f-s3f-bidirectional-vs-spont` record p < 0.05 where the paper only says "significantly". I kept it because 0.05 is the level the paper uses throughout, but that bound is not printed where the claims cite.
- `fig2a-above-chance` reads "best rats' typical performance" as the median over a rat's sessions. The paper does not define it.

Only the claims file changed. Nothing is committed or pushed.
