I've checked the claims file for DANDI:001544, made 11 corrections, and marked it ready. Three problems remain open.

**Checker result:** `30 claims, 30 quotes, 43 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **fig1c-app-approach, fig1c-av-avoidance:** Added a third reading of the t-test: an unpaired comparison of odor-arm time against saline-arm time within the odor group. It is the only reading whose degrees of freedom match t(16), and it also matches t(14). The paired reading gives df 8 and 7. The `n` now names the APP group, and the outcome rule follows the protocol: the claim must hold under every reading, and is blocked when the readings disagree.
- **fig1f-cfos-total:** The equal ChAT counts in the statement had no quote, so I added that sentence. The criterion said df (2, 64) "fits slices". It does not: 67 observations fit neither 25 mice nor 100 to 150 slices, and the criterion now says so.
- **fig1k-app-calcium-auc:** The criterion now requires every APP delivery to exceed pre-odor, as the paper reports, not only the first.
- **fig2c-hm4di-app-reversal:** Added a second reading: saline arm against APP arm within the hM4Di mice. It also gives df 8, and it is the comparison the sentence states.
- **fig2e, fig5c, fig5e:** Parts of the statements (locomotion, saline in both arms, active avoidance) had no quote. I added the Results sentences that state them, and named tests for the parts of fig2e that come from Figure S3.
- **fig6f-max-firing-rate:** The Methods' rules for discarding recordings had been made a variant. They are the paper's own method, so they are now applied, including the rule on a change of more than 20%. I also added the rule for when the two test readings disagree, which the other electrophysiology claims inherit.
- **fig6-app-less-excitable:** The outcome rule did not cover the case where no reading is significant. That case is now "not reproduced".
- **fig7d-bla-projecting-av:** Added the quote for the equal activated counts. The percentage's denominator is open (BLA-projecting neurons, or odor-activated neurons), so both are now readings.
- **Code check:** I read the electrophysiology code at tag v1.0.0 (commit 4ee1125), cloned from GitHub. The spike detection, threshold, baseline window and max firing rate described in the file match it. The checks entry records this.

**Still open**
- **fig3-same-odor-reactivation:** The 90% threshold for "virtually all" comes from the earlier reader, not the paper. The claim says so.
- **figs11-intermingled:** The rule for "intermingled" (each section holds both groups) is not in the paper, which shows only a map.
- **Morphology (fig6j, fig6kl, fig6m):** The F values are recorded as a nested ANOVA because the Methods name one. Their degrees of freedom fit tests on individual cells instead, and fig6kl's df (1, 10) does not fit its 16 cells.

**Ready: true.** The first two open problems concern histology and mapping claims that this electrophysiology dataset almost certainly cannot test, so they do not block an attempt. Nothing was committed.
