I wrote `claims/yang-2026.yaml` and the quote checker passes it: 25 claims, 25 quotes, 0 problems. There are no em dashes, no "rather", and no colon-space in any plain scalar. Nothing was committed.

**Text read.** The Research Square preprint, version 1 (posted 2026-10-22), from `paper/10.21203-rs.3.rs-11447300-v1.txt`. That covers the main text, Methods, the legends of Figures 1 to 3, Table 1 and the Extended Data legends (Figures 1-1, 2-1, 3-1). There is no separate supplement and no PDF, and I read no figure. The paper reuses DANDI 000363, version 0.231012.2129, from Chen et al. 2024.

**Code.** The repository is private ("will be made publicly available upon publication"), so I read no code and no detail is settled by it.

**Counts.**
- **Claims:** 25, all with a quote, none inferred.
- **Statistics:** none. The paper reports no tests, only mouse-level means ± SEM, and says no test was added after the means were known.
- **Criteria:** all 25 have one.
- **Expected values:** 21 claims have them. Tolerances are the printed SEM where the paper gives one, otherwise 10%, and printed ranges are widened by 10% of each bound.

**Main findings covered.**
- The early joint, choice and action fractions (Table 1), and the cosine between the two axes.
- The ratio of the laser difference to a split of control trials, the fraction after removing that split, the trend with neuron count, and the fit without the video regression.
- The example session.
- Decoding, early against pre-lick and on the Go-aligned curve.
- The choice and action shares before the lick, the Go-aligned joint fraction, and the energy outside the subspace.
- The matched pairs and reaction times, the pre-lick residual and its ratio to the control distance, the early ALM residual, and the residual time courses.

**Details the paper leaves open, and the readings named.** These are shared methods M1 to M10 in the opening comment, plus a few within single claims.
- **Laser trials with an early lick** (the exclusion is stated for controls only): kept, or excluded.
- **Mapping brain areas to the five regions:** the region labels of Chen et al., or Allen CCF parent structures.
- **Lick direction:** the side of the first lick, or from instructed side and outcome. Reaction time is not defined; I used first lick after Go minus Go as a standard choice.
- **Placing laser-onset windows on control trials:** all trials aligned on Go at the median onset, or laser trials on their own onset.
- **The jaw, nose and tongue regression:** x and y coordinates with an intercept, with missing keypoints given the mean, or trials lacking keypoints dropped.
- **Which trials are decoded:** laser trials only, or laser and control together. The inner search for the penalty is a standard choice.
- **Matching:** the closest control or a random one within the 100 ms caliper; what happens to a pair with no second control; per-bin distances averaged, or the four bins concatenated; how pre-lick bins are z-scored.
- **Bin step on the 100 ms Go-aligned grid:** overlapping 50 ms steps, or non-overlapping bins.
- **Within single claims:**
  - Signed or absolute cosine.
  - How the 20 control splits are combined, and splits when there are too few controls.
  - Three readings of the "control-split projection" correction.
  - The session set for Figure 2D and 2E: its early means (0.035 to 0.046) differ from Table 1, so it is either the decoding sessions or the matched sessions.
  - What the 2,676 pairs count.
  - The order in which the residual ratio is formed.
  - The trials and source vector for the example-session principal component and plane.

**Missing from the paper.**
- **Values shown only in figures** (per-mouse points, curves) are not printed, so claims rest on the text and Table 1.
- **Trend claims without a test:** for "decreased with neuron count" and "distance scales with neurons" I fixed Spearman correlation as a standard choice and marked it as one.
