The claims file is ready for an attempt. I changed 13 claims, added one, and recorded the changes under `checks` with `ready: true`.

**Checker:** before my edits it reported `38 claims, 38 quotes, 1 statistical values, 0 problems`; after them, `39 claims, 39 quotes, 1 statistical values, 0 problems`.

**Changes, by claim**
- **Header:**
  - ROIs need at least 20 units, as the Fig. 4f and Extended Data Fig. 7i and 9d legends say; the file said "more than 20". I checked the paper's code at the pinned commit: most dataset KI scripts keep counts above 20 and the IBL scripts keep 20 or more, so "more than 20" is now a variant.
  - It now gives both preprint unit counts (23,386 and 23,667).
- **dataset-ki-counts:** added the PFC unit count from the Extended Data Fig. 1b legend (12,674) as an expected value.
- **fig1i-nw-higher-metrics:** added Tukey's correction for multiple comparisons, which the Methods and the legend state.
- **extfig1d-sleep-like-differ:**
  - The comparison now uses the legend's two separate samples: 19,186 ww units for active epochs and 11,599 for sleep-like epochs.
  - Added Tukey's correction.
  - The criterion now says the number of metrics required is the file's own rule.
- **extfig1-epoch-counts:** added 11,599 as an expected value and the legend to the source.
- **fig2e-category-stability:** stability is now computed per transition, as the Methods define it, and "around 57%" has two readings: the mean over transitions or the pooled value.
- **extfig3f-layer-enrichment:** removed a condition the paper doesn't state (L2/3 not enriched in categories 1 to 3).
- **fig2j-nw-ww-correspondence:** the "more than 20 nw units" threshold came from the code, not the legend, which says only "sufficient". It is now labelled as the code's.
- **fig4cd-dataroi-enrichment:** the "most ventral ORBl dataROI" part is marked untested, because the text doesn't give the flatmap's axes.
- **fig4g-gao-category1 and fig5h-choice-gao-hierarchy:** minimum set to at least 20 units. fig5h now states the Methods' 1,000 shuffles, with the code's 2,000 shuffles grouped by `task` as a variant.
- **fig5b-tone-categories:** which units train the tone SOM is now open, with two readings. The Results say deep-layer ww units (n = 15,352); the code uses all ww units in every layer.
- **fig5k-task-tuning-category4:** the main test followed the code's 2,000 shuffles over the Methods' 1,000. It now uses 1,000. Grouping, which the Methods don't give for this figure, has two readings, and disagreeing readings block the claim.
- **Added fig5g-tuning-maps:** the Fig. 5g maps of choice, feedback and visual tuning across 73 IBL ROIs, a Results finding that had no claim.

**Still open**
- Several criteria for findings shown only in figures rest on rules this file chose, because the paper gives no measure or test: fig2a, fig2b, fig2f part 2, fig4e, fig5b, fig5e, fig5j and fig5g-tuning-maps.
- The Supplementary Information was not available, nor the figures themselves. So the grouping by behavioral setting (G1), the test behind methods-settings-no-difference, and the E-score p-values (Supplementary Tables 1 to 7) are unread.
- Some minor findings have no claim: the GaoROI corroboration (Extended Data Fig. 7e–h), SOM occupancy by PFC subregion (Extended Data Fig. 2f), nw-unit category stability (Extended Data Fig. 5e,f) and Extended Data Fig. 3c.

Nothing was committed.
