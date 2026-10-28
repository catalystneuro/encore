# Round 2 verification: Churchland et al. (2010) on DANDI:000139, version 0.220113.0408

Counts below come from the claims file and the attempt record: 23 claims, 23 outcomes. Cell numbers refer to the current notebook, which is renumbered since round 1.

## 1. Outcomes

| Claim | Outcome in the record | Agree? | Notes on the assumption |
|---|---|---|---|
| j-array-recordings | partially_reproduced | Yes, with a caveat | The criterion's "partial" needs the 27 conditions to be a subset of the paper's 108. The notes say this "cannot be shown", yet the outcome is not marked `assumed: true`. It should be. |
| fig4d-mean-correlation-j-array | partially_reproduced (assumed) | Yes | The tuning measure (range) and the proto-trial (condition mean, profiles concatenated) are stated and reasonable. The main reading passes on the t-test only (p = 0.042), and 3 of 8 selection readings fail (cell 18). |
| fig4abc-mean-correlation-other-datasets | blocked, data_missing | Yes | |
| fig4-broad-unimodal | reproduced (assumed) | Yes | Low power is stated. |
| fig4e-correlation-time-course | reproduced (assumed) | Yes, borderline | The splice assumption is stated, but its consequence is understated (§3). |
| suppfig1-population-psth-weak-movement-tuning | reproduced (assumed) | Yes, nominally | Criterion reading (a) holds in 16 of 16 rows. The cross-validated ranking breaks it for the claim's 17 neurons (ratio 1.115, cell 27). The record says so plainly. |
| fig6d-perimovement-best-j-array | reproduced (assumed) | Yes | Holds under all 8 combinations of the S, kinematic-window and replication readings. It is clearer on the 43 units whose tuning passes a permutation test (cell 36). |
| fig6-perimovement-best-each-dimensionality | reproduced (assumed) | Yes | 0.909 to 0.955 (cell 39). |
| fig6-dimensionality-peak | reproduced (assumed, S fixed) | **Yes. I am changing my round-1 position.** | The new chance curves show the recomputed-S reading cannot produce a decline: noise falls only 0.094 from k = 6 to 14, against 2.292 with S fixed (cell 42). The recomputed reading is therefore uninformative for this claim. S fixed is grounded in the Methods' wording, and with S fixed the best k is 2 to 6 in all 8 selection readings. |
| fig6-maze-task-spaces | reproduced (assumed, segments equal in time) | Yes, marginal | Segment directions score 0.008. That is above zero in only 2 of 8 selection readings (cell 45). The fragility is stated. |
| fig6abc-perimovement-best-other-datasets | blocked, data_missing | Yes | |
| fig6e-summary-rank | blocked, data_missing | Yes | |
| fig6-preparatory-dimensionality | not_reproduced | Yes | Under the criterion's plain count, 12 to 19 PCs. The cross-validated count of 7 (cell 54) points to noise as the cause, and the notes say so. |
| fig7a-shuffled-space-poor | reproduced (assumed) | Yes | |
| fig7b-window-start-slide | reproduced (assumed) | Yes | |
| ap-location-no-effect-j-array | reproduced (assumed) | Yes | The p-value does not depend on which array is labelled PMd. |
| ap-location-no-effect-other-datasets | blocked, data_missing | Yes | |
| fig7c-anterior-posterior-performance | not_reproduced (assumed) | Yes | Now run with the paper's upper limit. See the claims-file note under §3. |
| prep-activity-more-anterior | blocked, metadata_insufficient | Yes | |
| fig7d-pd-consistency | reproduced (assumed) | Yes | |
| some-neurons-better-elsewhere | reproduced (assumed) | Yes | |
| high-dimensional-task-spaces-underperform | reproduced (assumed) | Yes | |
| fig8-linear-dynamics-simulation | reproduced (assumed, full cycle) | Yes | The check is weak. |

## 2. Sentences the printed numbers do not support

- **Cell 37:** "Only 59 of 152 units pass the 5 spikes/s range with labels shuffled against 75 observed".
  - "Only" inverts the finding. The noise median of 59 is about 79% of the 75 observed (cell 11), so most of the passing count is matched by noise. The Summary and the record state the same numbers neutrally.
- **Cell 37:** "Every space is above its chance level at every dimensionality". The record's fig6d notes say the same.
  - Chance was computed only for the peri-movement space, kinematic window a with replication a, and the task spaces (cell 36). It was not computed for kinematic window b, replication b, or the upper limits.
- **Cell 72:** "The variant without the fitted neuron … gives upper limits at or below zero and ratios from -0.740 to 2.111". The record's fig7c notes say the same.
  - Only 2 of the 8 printed upper limits without the fitted neuron are at or below zero: −0.107 and −0.043. The others are 0.055 to 0.170 (cell 71). The ratio range is correct.
- **Cell 16:** "250 labelled trials per unit (350 with the unlabelled test segments)". The record's j-array notes say the same.
  - The test file holds only the 114 held-in units (cell 3). The 38 held-out units have 250 trials, not 350.
- **j-array-recordings notes** say the MC_Maze dandiset 000128 is a 2009-09-25 session with 182 units. Nothing in the notebook prints this. It is marked "not used for the outcome", which is acceptable, but no output supports it.
- **README** lists "Performance peaks at middle dimensionality", "Population PSTHs show weak movement tuning by onset" and the Figure 8 simulation as plain "Reproduced".
  - It drops what the Summary table keeps: "resting on S fixed", "reading (a) only; not under cross-validated ranking", and "full-cycle reading".
  - The README's list of open readings does not mention the Figure 8 gray interval.
- **Summary**, "best about 0.1 to 0.2": a small understatement. The recomputed-S best is 0.226 (cell 32).

Every other number in the conclusions, the Summary and the record notes matches the printed outputs. That includes the fig4d failing-reading p values (0.052, 0.056, 0.080), the 7 of 8 and 22 of 32 counts for fig4e, the threshold-table ranges, the fig7c values and SD, and the chance-curve falls.

**My round-1 reasons in the record.** They are faithful and in my words. My problems 1, 5, 8, 9, 10 and 11 have been folded into the per-claim reasons. Problem 5 is attached to both fig6d and the dimensionality peak, which is reasonable.

## 3. Round-1 points

**Resolved:**
1. The threshold noise. It is quantified (59 vs 75 units pass; 43 of the 76 units fitted in the PD analyses pass a permutation test), and a variant on the 43 tuned units was added.
2. The Figure 7C normalizer. The paper's upper limit is now the main reading.
3. The array labels, as far as the files allow. The metadata are printed, and every outcome is now either independent of the labels or blocked.
4. fig6-maze-task-spaces. It was changed from blocked to reproduced.
5. Chance levels. They were added; only the "every space" wording above remains.
6. The Supplemental Figure 1 ranking bias. A cross-validated variant was run and disclosed.
7. The wrong recording. It is disclosed and referred to a reader. Only the missing `assumed` flag remains.
8. The Wilcoxon p-value. It is disclosed.

**Not resolved, no effect on a conclusion:**
- Velocity is unsmoothed in the kinematic space. This was not run, but the gap to the peri-movement space is large.
- The SD tuning measure leaves no neurons, so that reading is degenerate. This is disclosed.

**Still bearing on a conclusion:**
- **fig4e: the splice sets the decline time.** This sharpens my round-1 problem 8.
  - The go-locked part of the spliced trace covers go −200 to +100 ms. That is exactly the preparatory window (`maze.PREP`), mapped to −554 to −254 ms.
  - So the reference value "400 ms before onset" (0.703) is taken inside the window the preparatory rate is averaged over. The decline at −263 ms is the end of that window shifted by the median RT.
  - In the main selection, this spliced combination is the only one that passes (cell 24). The movement-locked trace alone gives −307 ms, and the all-preparatory-neuron set is not near zero at onset.
  - The outcome still holds in other selection readings through the movement-locked trace with all preparatory neurons (6 of 8). But the main-reading conclusion should not rest on the splice.
- **suppfig1: the result for the claim's 17 neurons does not survive cross-validation.** The outcome is correct under the criterion, but the README should carry the caveat.
- **j-array-recordings: the outcome rests on an unprovable subset relation.** It should carry `assumed: true`.
- **fig7c: the criterion's band is narrower than random variation (claims-file issue).** This is reported, not corrected.
  - "Within 10% of random halves" is a band of ±0.046 around 0.455, but random halves themselves have SD 0.153 and range 0.067 to 0.869 (cell 71). A random half would usually fail it.
  - The outcome still stands, because array 2 lies 3 to 5.6 SD below the random halves under both S readings.
