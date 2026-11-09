The claims file for DANDI:001048 now passes the checker and is ready for an attempt (`ready: true`).

**Checker:** `20 claims, 20 quotes, 7 statistical values, 0 problems` (before my changes it was 19 claims, 19 quotes, 8 values, 0 problems).

The dataset itself does not hold this paper's data, as the file's header already says. The paper lists ten other dandisets (001030 to 001035 and 001271 to 001274), so every claim is marked as data held elsewhere.

**Changes, by claim:**
- **fig1-pure-sine-excites-all:** The Spearman test and "most neurons" for the shortening delay are not in the paper, so I labelled them standard choices. The statement says the maximum firing rate rose linearly, but nothing tested that. The paper gives no measure for it, so a straight-line fit is now reported but does not decide the claim.
- **fig1-excitation-block:** The statement says the depolarization reversed when the stimulus stopped, but the quote did not contain that. I added the sentence that says it, from the Tetrodotoxin section.
- **fig2d-modulated-thresholds-higher:** The file fixed 57.7 V/cm as the 1-AP threshold, which the paper never says. Both 1-AP and 5-AP are now listed as readings, and the value holds under either.
- **fig2-modulated-locks-to-beats:** The timing of the beat peaks was taken from the Methods for a different stimulus (the single-beat waves of Figure 5). The Results' description of two waves added in phase would put the peaks elsewhere. Both are now readings, used when the dataset has no record of the envelope.
- **fig3-extrapolated-threshold:** The three extrapolation readings give 7.0, about 5.8 and about 16.6 V/cm from the paper's own numbers, so the claim would always be blocked. Only "threshold proportional to conductivity" (57.7 × 2/16.4) gives the paper's ~7, so that is now the method and the other two are variants.
- **figs1-di8-same-as-fluovolt:** One condition ("APs at their lowest field with APs") could never fail. It now asks for one to three APs, matching the paper's "one or a few".
- **fig5-sine-asymmetry:** In the Figure S3 cell, the statement said the depolarized region was the smaller one. The paper says ROI 1, the hyperpolarized region by the paper's convention, was 20% smaller; I corrected it. The pulse asymmetry now has two readings, the peak (as the Results describe Figure 5B) or the mean from 1 to 2 µs (Figure 6B).
- **fig6-sine-less-than-pulse:** The "p < 0.01% for both ROIs in eight cells" counts cells that pass a threshold, which the protocol treats as a method, not a result. I removed it from `statistics`, made it an expected count of 8 cells, and the criterion now asks for eight of nine.
- **threshold-depolarization-estimate:** Now uses both readings of 57.7 V/cm.
- **New claim, fig5-whole-cell-depolarization:** The two regions oscillate in opposite phase on top of a gradual depolarization of the whole cell (Figures 5C, 5D, S3). This is a Results finding that had no claim. The paper gives no measure, so its tests are labelled standard choices.

**Still open (recorded under `checks`):**
- The dataset versions in each `where` field, and which figure belongs to which dandiset, come from DANDI titles. I did not check them, since I could not look at the dataset, and the paper does not say which figure is in which dandiset.
- **fig3-not-heating:** The paper's 2.5 °C cannot be reproduced from its own stated conductivity and fields: using the peak field gives about 3.9 °C and the RMS field about 1.95 °C. The criterion already blocks this claim unless the ratios between the three temperatures hold, and the paper gives nothing more to settle it.

Nothing was committed or pushed.
