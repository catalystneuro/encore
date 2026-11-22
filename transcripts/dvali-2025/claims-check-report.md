Checker result after my edits: `claims/dvali-2025.yaml: 38 claims, 36 quotes, 8 statistical values, 0 problems`. It also passed before them, with 34 claims and 11 statistical values. I also read the paper's code at the commit the file names (35e87ca) to check the criteria that cite it.

**Changes, by claim**
- **seven-enriched-pairings, fig3b-signaling-cell-type-enrichment:** removed the statistics entries. The FDR p < 0.05 there is a threshold for counting which pairs or communities are enriched, not a result.
- **fig4c-broadcaster-integrator:**
  - Removed the statistics entry: the text gives no p-value, and the figure's significance stars can't be read without a PDF.
  - Added the condition that pharyngeal out-edges exceed in-edges. The statement says this but the criterion did not check it.
  - Described the null as `broadcaster_integrator.py` builds it.
- **bilateral-anatomy-stronger:** fixed which values are compared. The Methods compare 78 with 2 and 38 with 2.43; the file had compared 78 with 2.43.
- **forced-same-number-ars:** said what each adjusted Rand score compares, following the Extended Data Fig. 4 legend, and added the recomputed original score as a comparison.
- **triad-distribution:** named the 13 connected triad types that `motifs.py` counts (networkx returns 16).
- **signaling-clustering-small-world:** the mean path length counts the source neuron at length 0, as networkx does.
- **anatomy-twenty-communities:** added the smallest community (1 neuron), which was in the quote but not in the expected values.
- **more-communities-anatomy-controls:** added the 16 communities of the 1.25-synapse anatomy network (Extended Data Fig. 12 legend).
- **ed6-signaling-not-feedforward:** added the rewiring counts from the code. `SIM.py` tests the inter-to-motor value against the sensory-to-motor null, apparently a slip; the criterion uses the correct value.
- **fig5a-signaling-rich-club, ed9e-degree-observations:** the one-SD rules and the window around the maxima are now marked as this file's choices, since the paper names no test.
- **fig5b-degree-correlation:** added a criterion for the "tended to" half of the statement.
- **rich-club-controls:** added a second threshold reading, each control network's own rich club maximum, plus the 9-of-15 overlap from the Extended Data Fig. 12a legend. The only reading before, the original degree thresholds, could leave the sparser networks with no rich club.
- **New claims** for findings that had none: anatomy-community-motif-fractions, community-vi-most-self-connected, pharynx-less-isolated-signaling, ave-most-connected-both.

No claim ids were changed, and every claim comes from this paper.

**Still open**
- **No PDF:** values shown only in figure panels can't be read. The section heading "signaling is ambiguous" suggests the paper's own feed-forward figure may show a significant leg, and the strict criterion for ed6-signaling-not-feedforward would count that against the claim.
- **q-values:** the paper doesn't say whether they are recomputed or taken from the atlas of its reference 27, or which strains are included.
- **fig4-community-motif-fractions:** the 30% core-periphery figure can only be reached under reading (a) of the between-community density.

**Ready:** yes. The checks entry is recorded with `ready: true`. Nothing was committed.
