I've written the claims file for DANDI:000017 at `claims/000017/10.1038-s41586-019-1787-x.yaml`. The quote checker passes with no problems, nothing was committed, and the dataset's data were not opened.

**Text read**
- The accepted author manuscript from Europe PMC (PMC6913580): main text, Methods, figure and Extended Data legends, and Extended Data Table 1.
- Both supplement Word files: the Supplementary Discussion, Supplementary Tables 1 and 2, and the legends of Supplementary Figs. 1 to 4.
- One value comes from the Word file itself: the "±" in the Supplementary Fig. 2 legend is lost in the text, and the Word file shows it (0.35 ± 0.04 and 0.10 ± 0.02).
- No PDF was opened. Supplementary Table 3 is only an image and was not read; no claim needs it.

**Code read**
- github.com/nsteinme/steinmetz-et-al-2019 at commit 9a0bea8. It holds the kernel regression, the trial movement classification, jPECC, the combined-conditions choice probability (ccCP) shuffle, and per-session arrays of included trials and units.
- It has no code for the passive-context, engagement-index, nested ANOVA, GLM, focality, Fisher-test or decoding analyses, so the Methods alone fix those.
- The code fixes several kernel details the Methods leave open: baseline subtraction, a basis shared by all sessions, a fixed penalty of 0.5, 5-fold cross-validation with up to 50 components for the full model, 75 components for the residual fit, 18 components and 10-fold cross-validation for the test kernel, and the scoring windows.

**Claims**: 40 in all. 38 have quotes; 2 are read from tables (Extended Data Table 1, Supplementary Tables 1 and 2). 9 carry statistics (11 values), 21 have expected values, and all 40 have criteria.

**Details the paper leaves open, with the readings named**
- **Trial selection:** the Methods rule against the code rule. The code drops NoGo trials with no movement before feedback, which the Methods do not; it is kept as a variant.
- **Neuron selection:** the code keeps about 1,000 neurons whose test returned NaN (its own comment calls this a bug); kept as a variant.
- **Which trials enter the behaviour figures:** all trials, or trials after dropping disengaged ones.
- **Reaction-time ANOVA:** its factors are not named. Readings: condition class with session, or with subject.
- **Wheel choice decoder:** not named. Readings: the sign of the velocity, or a cross-validated logistic regression.
- **Passive no-movement:** the window (−0.05 to 0.4 s or 0 to 0.4 s) and whether the value is a session mean or pooled.
- **"Consistently increased":** which responsiveness tests set the direction.
- **Supplementary Fig. 2:** what the d′ spread is taken over.
- **Significance z-score:** standard error or s.d. as the denominator.
- **Fig. 2 activity order:** which neurons count as responsive, and the latency measure (half-maximum or peak).
- **Focality bootstrap:** what is resampled (neurons within regions, or sessions) and how the difference is tested (its interval excludes 0, or the two intervals don't overlap).
- **Choice-timing decoding:** the time range (−0.25 to 0 s or −0.2 to 0.05 s), 5- or 10-fold, and the L1 strength.
- **jPECC:** the baseline window and which trials enter.
- **Contralateral preference and suppression:** model activity as the kernels at lag 0, or the full-model prediction.
- **ccCP:** the window around movement onset (−0.1 to 0.05 s or −0.05 to 0 s).
- **Nested ANOVA:** its factors (the Methods and the Extended Data Fig. 9a legend disagree) and which passive trials enter.
- **Pre-stimulus window:** −0.2 to 0 s or −0.25 to −0.05 s.
- **Engagement index:** which task trials and contrast conditions enter, z-scoring within session or pooled, pooling of the GLM, the inter-trial-interval split, the t-test form, and how each other variable's vector is defined.

**Problems in the paper itself**
- The Methods print p<0.05 for the area effect in the choice-timing ANOVA while calling it not significant; the Fig. 4c legend gives p>0.05.
- Extended Data Table 1's responsive column sums to 13,467, against 13,466 in the Results.

**What claims need that the paper lacks**
- **Fig. 5d:** the paper gives no test. I used a Pearson correlation across regions, the measure it reports for the matching Extended Data Fig. 7f comparison.
- **Vague wording:** where the paper says "widely", "frequently small" or "essentially no", the criterion sets the thresholds, and each says so.
- **Example neurons (Figs. 2 and 3):** the paper does not identify them beyond their region.
- **Repo's inclusion arrays:** the paper never says which selection they hold. They contain 18,248 of 48,661 units and 6,569 of 10,050 trials.
- **Histology:** the alignment-error claim needs DiI-spot and landmark data that may not be in the dataset.

Nothing the claims rest on is missing from the text.
