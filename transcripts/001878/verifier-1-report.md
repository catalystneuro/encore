**A. Outcomes** (22 claims in the claims file: 10 reproduced, 6 partially reproduced, 6 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| format-keypoints | partially_reproduced | Cell 16: 14 correctly named series, pixels, 30 Hz, all coordinates inside 1024 x 570. But all 333,340 confidence values are NaN, and the criterion's partial rule covers exactly that case. |
| resident-is-black | reproduced | Cell 18: with 746 frames ≥60 px apart and the 12 px patch, the resident is darker in 1.000 of frames (median grey 46 vs 251). This holds in every minute and every patch-size variant. |
| task1-vocab | reproduced | Cell 20: codes {attack 0, investigation 1, mount 2, other 3} and annotator "CalMS21 annotator 0". Cell 7: bouts tile 0 to 793.67 s with no gaps, so 0 unlabelled frames, and `frame_labels` raises on overlap. |
| task1-video | reproduced | Cells 9 and 22: 1024 x 570, 30 fps, 23,810 frames decoded, equal to the pose count. Motion energy peaks at lag 0. CaltechDATA also holds 89 Task 1 mp4s (70 + 19). |
| contact-during-social-behaviors | reproduced | Cell 24, nose-to-intruder minus other: investigation −354.6 px (CI −407 to −293), mount −361.0 px (CI −412 to −304). Attack has 0 frames in this session, so it is untested, as the criterion allows. |
| pose-errors-close-fast | partially_reproduced | Cell 26, factor 3 at 10%: errors are higher in close frames (+0.115, CI 0.064 to 0.179) but lower in fast frames (−0.020, CI −0.033 to −0.008). The same pattern holds in every variant. |
| link-mouse071 | reproduced | Cell 28: 23,810 frames in both, max coordinate difference 0 px, frame labels agree on 23,810 of 23,810. The CaltechDATA confidence scores (0.03 to 0.98) are absent from the dandiset. |
| pose-errors-close-fast-confidence | partially_reproduced | Cell 30: median confidence is lower in close frames (−0.091, CI −0.107 to −0.074) but higher in fast frames (+0.018, CI 0.012 to 0.025). The link it depends on is reproduced. |
| table5-task1-counts | reproduced | Cell 32: 507,738 frames / 70 sequences (train) and 262,107 / 19 (test), all exact. |
| table5-task2-counts | partially_reproduced | Cell 34: 19 of 20 counts are exact. Annotator 1 training frames are 139,122 against the paper's 139,112 (Table 5, confirmed in the arXiv v4 text), which is within 10% but the tolerance is 0. |
| table5-task3-counts | reproduced | Cell 36: 28 of 28 counts exact. |
| table6-task1-label-fractions | partially_reproduced | Cell 38, reading (a): attack is 14,039 / 507,738 = 2.76501%, which misses the 0.005 tolerance around 2.76 by 9e-6. The other three are within tolerance and all four are within 10%. Figure 4B's pie shows 2.8%, consistent with 2.765. |
| fig4b-task2-label-fractions | reproduced | Cell 40, reading (a) training split in Task 1 class order: 20 of 20 within 0.05. |
| table7-task3-label-fractions | reproduced | Cell 42, reading (a): all 7 within tolerance (largest gap 0.045, intromission). In v4 these percentages sit in the "% Frames" column of Table 7, the class-weight table. |
| dataset-size | reproduced | Cell 44: 282 unlabelled sequences with 5,952,058 frames. The over-1M-frames, >10 h and >70 h statements all hold under readings (b) and (c), and (c) counts duplicates once: 2.27 M frames, 21.1 h annotated, 76.2 h pose. |
| table10-task3-difficulty | partially_reproduced | Cell 46: the percent-of-frames correlation is significant (train rho 0.786, p 0.024; test 0.929, p 0.003), but mean bout length is positive and not significant (train 0.321, p 0.249; test 0.607, p 0.083). I recomputed these values exactly from the printed features, and the F1 constants match Table 10. |
| table1-architectures | blocked (methods_underspecified) | Model training is needed. The baseline repo (gitlab.aicrowd.com/.../mab-e-baselines) timed out from here too, and GitHub has no repository of that name. Neither the DANDI assets nor the CaltechDATA files hold predictions or weights. |
| table2-task-programming | blocked (methods_underspecified) | Same as table1. The task-programming features are deposited (`taskprog_features` JSONs in the task zips, per the CaltechDATA readme), so only a reimplemented baseline could be tried, not the paper's. The top-entry 0.864 cannot be tested (data_missing). |
| table3-task2-style-transfer | blocked (methods_underspecified) | Model outputs are needed and none are deposited. |
| table4-task3-new-behaviors | blocked (methods_underspecified) | Same. The "far below Tasks 1 and 2" comparison exists only between the paper's own reported numbers. |
| fig7-errors-at-transitions | blocked (data_missing) | Needs the baseline models' per-frame predictions, which are in neither archive. |
| fig11-annotator-similarity | blocked (data_missing) | Needs the top entry's learned annotator matrix. Its code is not linked and the matrix is not deposited. |

No claim states a chance level, so there is nothing to compare there.

**B. Problems**

1. [affects a conclusion] Cell 26, `error_flags`: the pose-error proxy flags body lengths outside the session's IQR bounds. During mount and close investigation, a hunched or occluded posture can produce real outliers, so the "close" excess may partly reflect behaviour and not pose error. Error fractions are 0.105 in mount and 0.045 in investigation, against 0.009 in other. This follows the pre-set criterion, so the outcome stands, but the close half of the partial result is weaker evidence than its confidence interval suggests. The confidence-based claim in cell 30 supports it independently.
2. [does not affect a conclusion] `block_bootstrap_diff` as called in cells 24 and 26 variants: in cell 24 it runs on `nose_d[base]`, a concatenation of non-contiguous frames, so some 300-frame blocks straddle removed stretches. The effect sizes are far from 0.
3. [does not affect a conclusion] Cell 26, `v_fast`: the criterion's order is ambiguous. The code takes the running median per mouse, then the maximum, not the maximum and then the median. The result is unlikely to change, since the fast effect is negative at every threshold.
4. [does not affect a conclusion] Cell 9, patch loop: with `half=3` and `STEP=2`, `h=1` gives a 2 x 2 downsampled patch, which is 4 full-resolution pixels, but it is labelled "6 px". The slices `yi-h:yi+h` are also off-centre by half a pixel. The main 12 px patch is correct.
5. [does not affect a conclusion] Cell 40: annotator 1 attack in reading (a) prints as 3.25. It is 4521/139122 = 3.2497%, 0.0497 from 3.2, so the 20/20 result depends on a single frame. The printout rounds to 2 decimals and hides this.
6. [does not affect a conclusion] Cell 20: the annotator check is a string test, `endswith(" 0")`, on free text. It is adequate here.
7. [does not affect a conclusion] Dandiset metadata, cells 5 and 8:
   - licence CC-BY-4.0, while the paper's datasheet says CC-BY-NC-SA (CaltechDATA also says CC-BY-4.0);
   - subject strain is C57BL/6 only, with the BALB/c intruder absent, sex U and age `P0D/`;
   - ethogram definitions are empty;
   - `centroid_speed` is the speed of the pair's midpoint, not of either animal;
   - confidence values are not carried over.
8. [does not affect a conclusion] Cell 13 (dataset finding, checked against the CaltechDATA readme): the readme says train and test are "split by animal identity". Yet four Task 2 recordings cross the train/test split between annotators 3 and 4, and mouse071 (Task 1 test) is also Task 3 groom training data. This matters for the blocked model claims, not the tested ones.
9. [does not affect a conclusion] task1-video, paper consistency: Section 3.1 says the Task 1 videos are released, but the datasheet (Appendix B) says the dataset "does not include the original raw videos". The dandiset mp4 (184 MB) is a re-encode of CaltechDATA's (964 MB).

Helper checks on synthetic inputs all passed:
- `frame_labels`: [start, stop) labelling, and it raises on overlap.
- `run_lengths` returns the correct lengths.
- `sequence_summary`: its "]]" frame count is right on indented JSON.
- `caltech_sequences` splits keys correctly across chunk boundaries.
- `nose_to_intruder` returns the expected distance.
- `block_bootstrap_diff` covers 0 under the null and recovers a shift of 1.

**C. What I could not check**

- The source of the 10-frame Task 2 gap (139,122 vs 139,112). A per-sequence frame table for annotator 1's training set would show whether one sequence accounts for it, which would point to a typo in the paper or a different deposit.
- Whether flagged "pose errors" are real tracking errors or real postures. A handful of video frames with keypoints overlaid, taken from flagged close frames, would settle problem 1.
- The unlabelled frame counts (`]]` in `scores`) were not cross-checked against `keypoints` length. The labelled sets validate the method, but printing keypoints-length totals for the unlabelled parts would confirm it.
- The exact label counts behind cells 38, 40 and 42. Raw integer counts per class, not only rounded percentages, would make the boundary cases (table6 attack, fig4b annotator 1 attack) auditable.
- The notebook's figures, which I did not view. All decisions above rest on printed numbers.
- I re-ran no data loading, as instructed. The dandiset asset list, blob ids and draft modification time match the notebook (6 assets, modified 2026-06-25T18:32:10Z). The paper text I used is saved at `paper/2104.02710v4.txt`.
