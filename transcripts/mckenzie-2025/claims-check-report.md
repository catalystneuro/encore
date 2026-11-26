The claims file is fit for an attempt, and its last check says `ready: true`. I made nine corrections; nothing was committed or pushed.

**Checker:** `claims/mckenzie-2025.yaml: 28 claims, 28 quotes, 25 statistical values, 0 problems`. I got the same result after my edits.

**Changes, by claim:**
- **figs1a-desipramine:** the source named the wrong subsection. The sentence is in the opening paragraph of the Results, before the first subsection heading.
- **fig5d-decay-hastens-with-days:** the statement said only that the decay rate "changes"; it now gives the direction. The Figure 5D legend says the decay "hastens over days of exposure".
- **fig6-recent-history:** the statement called the decay constant that matches arena days 3 to 4 "the track's". In the paper it is the decay after moving onto the track, not after the return to the home cage, so I reworded it.
- **fig7g-familiar-more-similar-early:** the quote comes from the Figure 7G legend, so the source now names the legend first. The paper says settling is faster in the familiar environment but gives no test or measure for it, so that part is now shown and not judged.
- **fig7ab-umap-embedding:** added that the paper's one example session is on a linear track.
- **figs7ab-in-field-out-field:** the paper does not say whether the 5 cm/s speed filter used for the place maps also applies to the 100 ms deviations. Both readings are now named.
- **figs7cd-movement-not-time-locked:** the paper gives no window for this test, and the criterion's 10-minute window is not from the paper. I said so and added the 1000 s window the paper uses for z-scoring as a variant.
- **figs7gh-unconditioned-similarity:** added a second reading of the measure, the mean correlation with all other vectors in the run. The Figure S7G legend allows it alongside the three-nearest-neighbour search.
- **Header E10:** the file had fixed which ripples the reactivation shuffle draws from. The Methods do not fix it and it can change the result, so both readings are now named: within the pre or post set, or both sets pooled.

**Open:**
- Two printed p-values do not follow from their t values under a two-sided test. Figure 2C gives t(7) = 7.20 with p = 0.0008, where the t value gives 0.0002. Figure 6C gives t(5) = 3.74 with p = 0.005, where the t value gives 0.013. Both are recorded as printed, and both claims use the photometry data, which cannot be tested on DANDI:000552. All electrophysiology p-values match two-sided paired t-tests over 8 sessions.
- The paper lists 7 novel environments for its 8 sessions, so which sessions it used is left to the author.
- The paper links no analysis code, so the method details named as readings cannot be settled from code.

All of the paper's main findings have a claim, and every claim comes from this paper.
