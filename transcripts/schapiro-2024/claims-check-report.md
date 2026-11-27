I checked `claims/schapiro-2024.yaml` against the paper, fixed what the paper shows to be wrong, and think the file is ready for an attempt. Nothing is committed.

**Checker result** (after my edits): `claims/schapiro-2024.yaml: 25 claims, 25 quotes, 24 statistical values, 0 problems`. Before the edits it gave 27 statistical values; the drop is the three post hoc test entries I removed.

**Changes, by claim**
- **fig4c, fig4d, fig4e:** I removed the post hoc Tukey test entries recorded as "p < 0.05". The paper never prints a p-value for those comparisons, only that they were significant, so the bound was a threshold the file supplied, not a result. The criteria still use the Tukey tests.
- **fig4e:** The rule for "partially reproduced" described a case that cannot happen. It now reads: the condition effect and the two comparisons the legend names are significant, but saline against Cs+ + PTX is not.
- **Header O1 (how Q10 is computed):** The Figure 1C legend says "best fit Q 10 equations", which supports fitting the Q10 equation. That reading is now the main one and the other two are variants.
- **fig1e-two-saline-q10-same, fig1e-saline-q10-same-across-designs:** These are claims of absence, which the protocol judges on the paper's test alone. They had been judged under every Q10 reading, which could leave the outcome undecided. They are now judged under the main reading, marked as resting on it, with the others shown as variants. For the second claim I also noted that the paper gives no N for its two-sample test.
- **fig1-cs-lower-frequency-11c:** Noted that the sentence gives no N; the 21 comes from the design.
- **fig2c:** The statement generalised from one example preparation and left out the "inhibitory" phase the Results list. It now says it is an example and names that phase. The phase boundaries had been written as if they came from the paper. They are now named as open, with two readings: the three phases in the figure legend, and the four phases in the Results, using LP spikes. The 30 s windows now cite the Discussion. The source also cites the Figure 4G paragraph and the Discussion.
- **fig1d:** The source now points at the Figure 1D legend, where the quote and the statistic are.
- **fig1f, fig4c:** Which 11 degrees C hold is used now cites the open detail O2.
- **Header, phase constancy:** Noted that the Figure 6 legend says "paired t-test" where the Methods say one-sample t-test.

**What remains open** (recorded under `checks`)
- The paper doesn't say whether the Figure 6 p-values are the Bonferroni-adjusted ones; the file reads them as adjusted.
- F(5,85) in Figure 1D and r(21) in the matched-period correlation each fit about 18 experiments, not 21. The paper doesn't say which experiments entered.
- How periods were matched, and whether the PD offset advance is in ms or in phase, are not given.
- The time windows for measuring Ih, the smoothing alignment and span for the jag measure, and which cycles form a phase all remain open, with readings named. The scripts deposited in the dataset may settle them; I did not open the dataset.

Every main finding has a claim, and every claim comes from this paper. The last check entry has `ready: true`.
