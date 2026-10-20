I checked the claims file and corrected it. It is ready for an attempt.

**Checker result** after my edits: `33 claims, 33 quotes, 0 statistical values, 0 problems`. Before them it gave 32 claims with 0 problems. I also read the paper's code (berenslab/mini-atlas, at the commit the file names) to check every place a criterion says it follows the code.

**Changes, by claim**
- **Opening comment and ttype-qc-counts:** they said the 7 cells with an exclusion reason are excluded. Two of those 7 had already failed quality control, so the excluded cells with a t-type are the Methods' 5. The arithmetic now reads 1,232 minus 5 gives 1,227.
- **cohort-ages:** I removed the "over cells" reading. The Methods give the ages over the 266 mice, so the paper doesn't allow it.
- **stimulus-protocol:** the 1 ms and 0.05 s timing margins and the 95% and 80% shares of cells are not in the paper. They are now labelled as standard choices.
- **fig2-family-features:** reading (b) said Fig. 2 shows four interneuron families. It actually separates five groups (the four plus the excitatory class), so (b) now uses those. I dropped the Mann-Whitney p < 0.05 requirement, because the paper reports no such test; the test is still reported, for information only.
- **fig3d-families-ephys:** the criterion was wrong about the code. The code keeps the 5 excluded cells under their RNA family, both as rows and as neighbour labels. Now both the Methods' handling and the code's are run, and the claim is blocked if they disagree. I also corrected the tie-break: it is numpy's sort order, where "low quality" comes last, not alphabetical order.
- **l45-it1-boundary:** added a second reading of "on the boundary" (the t-type's interquartile depth range contains 0.29), with the rule for when the readings disagree.
- **ed7-within-families:** the "many features" test pooled pairs across families, which neither the paper nor the code does. It is replaced by a count within each family, as the code computes, and labelled as the reader's own reading.
- **fig3d-morph-combined:** the Methods call the electrophysiology block "16-dimensional", but they build 17 components and the code uses all 17. Both versions are now run. The code's handling of excluded cells is named as a variant.
- **fig5a and fig5b:** named as a variant that the code keeps the excluded cells in their t-types.
- **ed8-leiden-entropy:** filled in from the code the resolution (2), the seeds, the graph and the entropy base. The Spearman comparison is now labelled as the reader's reading, since the paper gives no measure.
- **rnaseq-depth:** added a criterion using the Methods' definition of a detected gene.
- **New claim, ed6-physiological-temperature:** covers the 34 °C follow-up findings for completeness. Its data are in dandiset 000035, so it is not tested here.

**Still open**
- Several criteria turn vague words the paper never measures ("agreed well", "many", "grouped", "often the same") into thresholds chosen by the reader. They are labelled as readings, but the thresholds are not the paper's.
- A few minor qualitative findings have no claim: deep neurogliaform cells of two origins, chandelier cells, and L5 Pvalb and Martinotti morphological types matching t-types. They rest on morphology or on Extended Data Tables that are not in the text, and none is a main finding.
- For ed6-it-et-room-features, the paper doesn't say how cells with a missing feature value are handled in the Mann-Whitney ranking.

All of these are recorded under `checks` with `ready: true`. Nothing was committed or pushed.
