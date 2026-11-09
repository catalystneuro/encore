The claims file for DANDI:001187 is ready for an attempt. I made four corrections and left three points open. Nothing is committed.

**Checker result** (the same before and after my edits): `29 claims, 28 quotes, 43 statistical values, 0 problems`

I also cloned the linked code (SBCAT-NO-release-NWB, commit 6d07204) and checked every detail the file attributes to it. All of them match: the category-neuron test, the 5 s response-time cutoff, the confidence recoding, the outlier rule in the GLM code and the high-confidence definition. The neuron counts in Table S1 add up to the totals in the file's opening comment.

**Changes, by claim**
- **fig3h-encoding-no-effect:** the quote was a Methods sentence that describes the analysis but states no result. I replaced it with the Results sentences that cite Fig. 3h and give the result ("all p > 0.06").
- **fig3a-area-interactions:** the statement left out that the LTM accuracy × confidence interaction was also not significant. The quote and the criterion already include it, so I added it.
- **table-s1-counts:** the "partially reproduced" grade at 41 of 46 sessions (90%) had no source. It now applies when some sessions match and others don't, with the mismatched sessions listed.
- **fig4d-category-no-memory-signal:** the paper doesn't say whether the old-vs-new t-test uses only correct LTM trials, as the GLM before it does. I added this as an open detail (D3) with both readings.

**Still open** (recorded under `checks`)
- **fig3e and fig3f (cluster tests):** no source gives the threshold that forms the clusters. The file uses FieldTrip's default of 0.05, which could change how far the cluster extends.
- **behaviour-overall-accuracy and ltm-rt-confidence:** the tolerances are standard errors worked out from the paper's SD and session count, with a reason given. The protocol names the stated spread (the SD itself), which would be much looser.
- **fig3g-nonpreferred-no-effect:** the figure legend doesn't say whether brain area is a factor in that model. The file follows the Methods model, which includes area.

**Ready:** yes.
