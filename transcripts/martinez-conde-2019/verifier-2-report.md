**Verifier report: Martinez-Conde et al. 2019 on CRCNS pvc-12, round 2**

The claims file has 19 claims, and the attempt record has 19 outcomes, one per claim. The record gives 8 reproduced, 1 partially reproduced, 7 not reproduced and 3 blocked. Only one outcome is marked `assumed: true`, fig7c-fold-edge-equivalence.

### 1. Outcomes

I agree with all 19 outcomes, and none changed from round 1.

- **Unchanged claims.** These still rest on the same printed numbers as in round 1:
  - neuron-counts, cell 7.
  - s4, cell 11: Kruskal-Wallis p = 0.005, ANOVA p = 0.001, BH p = 0.009 and 0.036.
  - fig4a, cell 14.
  - fig4b, cell 17: S90 is 8.09, below the lower bound of 8.75.
  - pairwise tests, cell 20.
  - fig5, cell 23.
  - Table 1, cells 27–35: Edge 1/5, P180 2/5, S90 at most 1/5, S52 5/5 under (a ii) only, S40 5/5.
  - fig6, cell 38: 0 of 10 significant.
  - fig7a, cell 41.
  - fig7c significance, cell 47.
  - fig7d, cell 50.
  - The three blocked claims.
- **fig7c-fold-edge-equivalence (assumed).** The assumption is stated in a deviation, in cell 45 and in the Summary, and I think it is reasonable:
  - Under reading (b) the ladder step is 0.037, so "within one step of 90%" taken literally means |level − 90| ≤ 3.7. That is the criterion's own wording.
  - The other way of reading it is also run and printed (cell 44: "within one level: True").
  - The deviation mentions the paper's "94%"/"68%" labels, which point the other way.
  - Under (a) the claim fails whichever way the margin is read: the level nearest P180 is 0%.
  - The outcome is still borderline. I cannot confirm the reader question was filed, because `questions/martinez-conde-2019.yaml` is not among my materials.

### 2. Sentences the numbers do not support

Almost everything checks against the printouts. The exceptions:

- **Cell 53 (Summary): "Pixels of the ROI that fall off the display are left out; keeping them changes no outcome."**
  - The unmasked variant (`df_um`) is run for s4, fig4b, the pairwise tests, Table 1 and fig6 only.
  - It is not run for fig4a, either fig7c claim or fig7d. `edge_responses` is never called with `rate_unmasked`.
  - Likely true, but not shown.
- **Cell 53: "for Square and Edge they match a single 16 DU square beside the rectangle, and using it changes no outcome."**
  - `df_fit` is run only for s4, fig4b and Table 1.
  - It is not run for fig4a, the pairwise tests, fig6, fig7c (where the Edge responses take the baseline through `base_kind`) or fig7d.
- **Cell 4, cell 53 and the attempt record's `metadata_error` finding: "`smoothed_image_norm` is normalised to its maximum after subtracting `BaseActivity`."**
  - No cell prints a check of this, so the notebook's outputs do not support it. The `image`-is-a-rate part of the same finding is supported (cell 3).
- **Cell 48: "with BH, up to 0.832."**
  - This is true for BH over 40 tests.
  - BH per fold also makes S40 significant at 0.906 (p = 0.040, cell 47).
  - The attempt record says "BH over 40" and is correct.
- **Attempt record, fig6 notes: "the smallest p is 0.415 (S40 median) … and the same with the unsmoothed and the unmasked map."**
  - If "the same" refers to the smallest p, it is wrong: the unsmoothed map gives 0.174 and the unmasked map 0.481 (cell 38).
  - What holds is that none of the ten is significant in any of the three runs. The wording should say so.
- **Attempt record, Star finding: "A check made while preparing, not run in the notebook, found no rotation and shift…"**
  - This has no output behind it. It is labelled as such, so it is disclosed rather than wrong.

Everything else checks against the printed outputs, including the README, the s4, fig4b and fig7a–d notes, the 11 of 188 squares off the display, and the 83 recordings (25 + 30 + 28) in the Summary.

**My round-1 reasons in the attempt record.** Each claim's reason restates my round-1 report faithfully, in my words. The problems I raised are attached to the right claims: problem 1 to fig7c, 2 to s4, fig4b and table1-p180/s90, 3 to table1-s52, 6 to fig7a and 7 to fig5. Two small points:

- The fig7c reason drops my "borderline" label. The verification summary keeps it.
- The s4 reason does not carry my caveat that "the main analysis follows the paper's text, so my outcomes stand".

### 3. Round-1 points

**Resolved:**

- **1, fig7c margin.** Both ways of reading it are run and printed. The outcome is marked as resting on an assumption, and the question is passed to a reader.
- **2, Square and Edge baseline.**
  - The best-fitting square is now located at (15, 129), on grey level 0.
  - Applied to all 22 recordings, it still gives a difference (cell 11: Kruskal-Wallis p = 0.009).
  - The paper's four squares on only the recordings that store BaseActivity also still find one (p = 0.025).
  - So the non-significant result comes from the stored values themselves. The four-square method and the smaller subset don't explain it.
  - In Table 1, that square gives 1/5 for Edge, 2/5 for P180 and 1/5 for S90. In fig4b it gives S90 = 8.21, still out of tolerance.
- **3, Star sample.** The 12 recordings used are compared with the 16 readable ones left out. They do not differ (p = 0.98 and 0.09), and the notes call this a coarse check.
- **4, slice wrap-around.** `window` now clips both ends of every slice; I read the code.
- **5, stimulus offset.** It is now tested: with offset 1 the error is 0.5–1.0 DU.
- **6, fig7a RMS contrast.** The synthetic check is printed (1.0), and the physical-luminance explanation is given as untested.
- **7, fig5 `left_out`.** It is now computed: 1 for Corners.
- **8, Square and Edge registration.** It is now discussed as "consistent with, not shown by" the data.
- **9, Corners baseline squares.** The darkest grey level in the ROI (1.01) is printed and recorded as a finding.
- **10, claims file inconsistency.** It is passed to a reader. It is not a misreading of the paper.
- **"Could not check" items.** All were added: fold lengths (150, 150, 70.7, 150 and 100 DU), the square positions, the block luminance profiles, the zip listing and the Star comparison.

**What remains that bears on a conclusion:**

- **fig7c-fold-edge-equivalence.** It goes from not reproduced to reproduced depending on the reader's answer about the margin. Even a pass under (b) would just pick the two ends of the ladder: S40 is 6.66 spikes/s above every Edge level and P180 is 4.50 below every one.
- **s4.** The paper's squares find a difference and the stored BaseActivity does not. How the stored Star and Corners values were computed is still unknown: no placement fits within 12.4% and 18.6%. The Corners squares sit on grey level 1.01 rather than 0%, and their placement is assumed from Fig 2C.
- **Square and Edge outcomes** (table1-edge, -p180 and -s90, and fig4b's S90). They rest on a registration that is only weakly supported (p = 0.13).
- **table1-s52.** It is reproduced only under reading (a ii), with n = 12 against the paper's 30.
- **Summary wording.** The two "changes no outcome" sentences in cell 53 go beyond the variants actually run, as listed in section 2.
