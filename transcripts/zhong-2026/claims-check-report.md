I checked `claims/zhong-2026.yaml` against the paper and made six fixes. The file is ready for an attempt.

**Checker result** (the same before and after my edits): `claims/zhong-2026.yaml: 12 claims, 12 quotes, 0 statistical values, 0 problems`

**Changes, by claim**
- **fig3b-individual-subjects**: I rewrote the criterion. As written, one result could count as both reproduced and partially reproduced: a majority of subjects showing the pattern, but one of the two named exceptions (P64CS without a ramp, TWH120 without a dip) failing. The statement includes those exceptions, so "reproduced" now requires them. "More than half of 14" is now stated as 8 or more.
- **fig2b-hierarchical-retrieval**: The criterion now notes that Methods C calls the 0.01 s clusters "k = 2, 3 level chunking clusters", while the Results put chunking clusters at k = 1, 2. It also gives the reason for the zero tolerances (they are counts).
- **fig4a-universal-slope**: The criterion now includes the natural-text curve, which the Fig. 4a legend includes.
- **fig4a, fig4b-plateau-near-eight, fig4b-three-languages**: The `where` fields now carry the DOIs from the paper's reference list for refs [42] and [46].
- **fig4b-three-languages**: The criterion now says when the claim counts as reproduced: every language must show the "similar trends", and the plateau must fall in the predicted region. It also explains why "at or below 8" is an allowed reading: the paper calls M* a limit beyond which perfect recall is impossible.

The other claims check out: statements match the paper, sources point at the right place, there are no statistics to record (the paper reports no tests), and every main finding has a claim (Fig. 1D, Eq. 1, Fig. 2B, Fig. S2, the subject exclusion, Fig. 3A–C, Fig. 4A–B).

**What remains open** (recorded under `checks`)
- The Hindi replication (ref. [47]) has no DOI or volume in the paper, so the author may not be able to pin it. That part of fig4b-three-languages could end up blocked.
- The Fig. 3 claims depend on details the paper doesn't give: bins, smoothing, the time window, the z-score reference, how a dip, ramp or peak is judged, and how boundary and onset neurons are selected. The criteria name these as open and fix readings, so the outcomes will rest on assumptions.
- The paper doesn't say whether "all trials" includes clips without a cut. The text supports cut clips only, which is the reading the criterion uses.

The edited file is not committed, as instructed.
