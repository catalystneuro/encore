The checker passes after my edits: `claims/000689/10.1038-s41586-022-04964-y.yaml: 39 claims, 39 quotes, 199 statistical values, 0 problems`. It also passed before them (38 claims, 185 values). I read the whole paper (PMC author manuscript, Methods, statistics section and all legends) against every claim. I marked the file ready.

**Changes, by claim**
- **fig1g-pvt-global-cko-reward**: the measure is now an open reading, z-score or raw percent. The Methods describe a z-score, but the effect size (20.52, CI 4.4 to 36.7) reads like a percentage.
- **fig1h-global-cko-no-shock-effect**: added the mouse counts from the legend, and noted that t(14) is printed for 8 and 9 PVT mice. The criterion now names the Methods' freezing rule.
- **ed2-glutamate-corelease**: noted that the vHPC t = 28.03 does not fit its P = 0.0188 or its effect size.
- **ed6-somatic-no-change**: added the two missing tone-airpuff tests (MGN, vHPC) and two missing CIs. The criterion judged six tests but only four were recorded.
- **fig4-recording-count**: the note on 684 neurons was wrong. The excluded BLA-CeA neuron is kept for basal firing, so it does not explain the gap to 685. I added that the Fig. 4e degrees of freedom sum to exactly 685.
- **fig5c-cross-group-decoding**: added the missing test (CRISPR-trained against shuffled, t(16) = 96.57) and the printed effect sizes. The statistics section's signed effect sizes (−0.3114; 0.4769 against 0.1662 over shuffled) run opposite to the direction the Results and legend state. The text's direction is judged, and the disagreement goes on record as a deviation.
- **ed8e-port-and-freezing**: noted that P = 0.012 for t(33) = 2.37 is half the two-tailed value. The baseline for z-scoring freezing was stated as fixed; it is now open, with two readings.
- **ed8os-active-trial-responses**: removed a BLA-NAc interaction test that the statement does not cover. I added the untagged-neuron state effects for both CSs. The criterion now says the paper's state effect supports larger active-trial responses only for the sucrose CS.
- **ed9-nt-acute-epsc**: each antagonist test is now paired with its population. The legend does not name the populations, so the sign of W is used to read which is which.
- **ed10-ntsr1-cko-reward**: added the ANOVA F(2,25) = 4.324 and the control against post-acquisition comparison (P = 0.99), which the statement's recall part rests on.
- **New claim ed8i-projector-cluster-proportions**: Extended Data Fig. 8i is cited in the Results and had no claim. The paper reports no test for it.

**Open, recorded in `checks`**
- **fig4e**: the significant clusters' effect sizes are mixed in sign, so the text cannot confirm that each shows a smaller CRISPR response. The 5-of-14 and 3-or-4 thresholds are a judging rule; the paper does not give them.
- **fig5a and fig5dh**: the rules over random subsamples and seeds (median of 20 subsamples, "most seeds") are also judging rules the paper does not give.
- **fig2d**: the paper scored this freezing by hand, so using the automated velocity rule is a substitution, recorded as a deviation.

Nothing is committed. The only file I changed is the claims file.
