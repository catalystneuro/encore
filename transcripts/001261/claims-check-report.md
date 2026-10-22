I checked the claims file against the paper and the supplement images. It is ready for an attempt. Nothing was committed.

**Checker result:** before my changes, `28 claims, 28 quotes, 31 statistical values, 0 problems`. After them, `29 claims, 29 quotes, 28 statistical values, 0 problems`.

**Changes, by claim**
- **Opening comment:** corrected the macaque ages to 6.9 to 16.9 years (Methods 2.2).
- **fig2-mouse-c-nc-15-of-18, fig7-macaque-mouse-feature-count, fig9-macaque-morphology-feature-count:** removed the per-feature "p < 0.05" statistics. That is the threshold used to count features, not a result.
- **fig2-mouse-c-nc-15-of-18:**
  - The criterion now tests the second half of the statement: AP width, upstroke and downstroke must be among the features that do not differ (Fig. S2-2C).
  - The code's variant feature definitions are shown but no longer decide the outcome.
- **fig7-macaque-mouse-feature-count:** the statement said "the figures mark 17". Fig. 7D can't be read, so it now says the legends imply 17.
- **fig2c, fig4c, fig7c, fig9c and fig10 (the UMAP and LDA separation claims):** these were judged "under one reading" of open details (how missing values are handled, how the data are shuffled). The outcome must now hold under all readings; when the readings disagree the claim is `methods_underspecified`.
- **fig5a-mouse-lda-electrophysiology:** added the missing "not reproduced" and `methods_underspecified` outcomes.
- **fig10c-combined-lda-weights:** if the two readings of the weights disagree, the result was "partially reproduced". It is now `methods_underspecified`.
- **New claim, figs9-1a-macaque-mouse-sholl-similar:** Results 3.4 says many morphological features were similar between species, citing the Sholl panel (Fig. S9-1A), and no claim covered it.
- **Supplement figures:** the significance stars and directions recorded from Figs. S2-2, S4-1B, S7-1 and S9-1B match the images, so nothing changed there.

**Still open (noted under `checks`)**
- The paper gives no measure of UMAP separation. The file's measure (neurons misclassified by a straight-line boundary in the UMAP plane, compared against shuffled labels) is the file's own choice, and no other reading is offered.
- Figs. 2D, 4D, 7D and 9D can't be read because there is no PDF. So which 12 features Fig. 7D shows, and the input resistance and branch point values, are unknown.
- Means are given 10% tolerances instead of the paper's SDs. The file gives its reason (the SD is the spread of the same neurons), and I kept it.

**Ready:** yes.
