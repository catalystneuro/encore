I checked `claims/saez-2016.yaml` against the paper and the file is ready for an attempt (`ready: true`). I fixed seven things, none of which changes a claim's id, statement or expected values. Nothing was committed or pushed.

**Checker result:** `claims/saez-2016.yaml: 16 claims, 16 quotes, 20 statistical values, 0 problems`, both before my edits and after them.

**Changes, by claim**
- **Opening comment:** "no difference" claims (claims of absence) are now judged under every reading of the post-pairing window, as the protocol requires. They count as reproduced only when no reading finds the effect. If the readings disagree, the outcome rests on the reading the author adopts, marked as an assumption. The file had judged them under any single reading, which makes them easier to pass.
- **fig1-control-no-net-plasticity:** I dropped the second t-test reading. Comparing normalized pre against post amplitudes is the same test as a one-sample test of the percent changes, so it added nothing.
- **fig1-vc-ic-same:** now judged under the new rule for claims of absence.
- **fig2a-bicuculline-outcomes:** the file said the paper's 63% was 16/26 rounded up. It is not (16/26 is 61.5%). It is now named as a mismatch, and the counts are used.
- **fig2-mean-unchanged-variance-increased:** the variance test is now recorded under the paper's own name, "Fisher's test". The criterion reads it as an F-test of the variance ratio. The equal-means part is now judged under the new rule.
- **fig3a-ks-scs-vs-ecs:** the "no difference" half (single-cell data against bicuculline) is now judged under the new rule. The file now notes that the paper does not state the 0.05 threshold used for it.
- **fig3b-segregation-near-complete:** the Methods do not say how the other two plasticity classes share the remaining probability as segregation rises. The file had presented its choice as the only reading; it now names two readings, in proportion to the single-cell counts or equally.

Everything else held up. The quotes, sources, statistics and tolerances are correct. The "±" values in the paper are standard deviations: the subgroup values pool to the stated totals, and the reported p = 0.28 and p = 0.97 follow from them. I kept the file's way of reconciling the paper's swapped labels for the control and bicuculline means. All main findings have a claim, and none comes from anything but this paper.

**Still open**
- The three Figure 3 claims need the single-cell stimulation data from the authors' earlier paper (their reference 17). That data is not in this data set, and the paper does not say where it is.
- The paper prints p > 0.8 for no net change in control cells, but its own mean and SD give about p = 0.08. The claim is judged at p < 0.05, so that printed value is not expected to be matched.
- The paper does not give the post-pairing window, the exact form of the per-cell t-test, or how the peak is measured. These stay as named readings or a stated standard choice.
