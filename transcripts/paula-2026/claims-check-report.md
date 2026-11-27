I checked `claims/paula-2026.yaml` against the paper and its supplement. The file is ready for an attempt (`ready: true`). I made six corrections, and four questions remain open.

**Checker result** (before and after my edits): `claims/paula-2026.yaml: 38 claims, 37 quotes, 7 statistical values, 0 problems`

**Changes, by claim**
- **fig2a-vis-cv-by-condition**: The rule for "partially reproduced" required blank-screen CV above natural-image CV. The paper's own medians contradict that: VISl is 0.46 in both, and VISal is 0.48 for natural images against 0.46 for blanks. The rule now keeps only the orderings the paper's numbers show.
- **fig3a-reference-systems**: The criterion misquoted the supplement. The supplement gives the tent map slope as (0, 2], not (1, 2]. It gives no range at all for the logistic map's r, for alpha or for k. Those three are now marked as open, each with a stated reading.
- **fig1c-cv-above-surrogate**: The paper's surrogate medians for visual cortex (0.21 to 0.24) were listed as expected values but never used in the criterion. They are now part of the test.
- **fig2b-visually-driven-js-cv-low**: The Fig. 2b legend states this finding as JS values (typically below 0.20), while the text gives percentages (below 4%). The legend's version is added as a second reading.
- **fig4c-dg-ca3-complexity**: The criterion now notes a conflict over CA1. The Fig. 4 legend and the Results III.D summary group it with DG and CA3, while the text's ranges group it with POST, ProS and SUB.
- **fig5-mb-flat**: The Fig. 5 legend gives a wider midbrain range for natural images (0.10 to 0.15) than the text (0.10 to 0.13). The criterion now notes this.

**Still open**
- I could not render the PDF either, so no figure images were read, including the Fig. 3a parameter values. Every claim rests on the text and the legends.
- One way of selecting units uses the Allen Institute's default quality filters. These do not come from the paper, and I did not confirm the exact defaults for this dataset. The paper's Table I neuron counts are meant to decide between this reading and using all units.
- Some criteria use cut-offs the file sets itself where the paper gives none, for example surrogate correlations below 0.2, and "most" taken as more than half. Each criterion says so.
- In several places the text and the legends disagree, and the paper does not say which is right. The claims test both versions.

I found no main finding without a claim, and every claim comes from this paper. Nothing was committed or pushed.
