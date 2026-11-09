**Round-2 verification: CalMS21 (Sun et al. 2021) on dandiset 001878 (draft)**

**1. Outcomes**

The claims file has 22 claims. The attempt record gives 10 reproduced, 6 partially reproduced and 6 blocked, and I agree with all 22.

- **Reproduced (10):** resident-is-black, task1-vocab, task1-video, contact-during-social-behaviors, link-mouse071, table5-task1-counts, table5-task3-counts, fig4b-task2-label-fractions, table7-task3-label-fractions, dataset-size.
- **Partially reproduced (6):** format-keypoints, pose-errors-close-fast, pose-errors-close-fast-confidence, table5-task2-counts, table6-task1-label-fractions, table10-task3-difficulty.
- **Blocked (6):** table1 to table4, fig7 and fig11.
- **fig7 and fig11:** in round 1 I gave the reason as data_missing. The record keeps methods_underspecified and now names the missing predictions and the missing matrix as a second reason. I accept this: both depend on models that cannot be rebuilt, so the outcome is the same.

**2. Statements the printed outputs do not support**

- **Cell 32:** "Most flagged frames fall in mount (error fraction 0.105 against 0.009 in other frames)". Cells 7 and 31 give the label counts and error fractions. They imply about 304 of the 657 flagged frames are mount (2,894 × 0.105), which is 46%. That is the largest share, not a majority. Only within close frames is mount the majority (cell 38: 243 of 312). This does not change the outcome.
- **Cell 14, and the attempt record finding (kind: other):** "six Task 1 test recordings (mouse071 among them) are Task 3 training sequences". Cell 13 prints six Task 3 training *sequences*. They fall in only five keypoint groups (4 "task1/test + task3/train" plus 1 "task1/test + task3/test + task3/train"), so they come from five recordings. The four mount_attempt training sequences cannot all be distinct recordings. This does not change any outcome.
- **Cell 4:** "71,524 and 14,991 frames" for the other two NWB files. No cell prints these numbers. This does not change any outcome.

Everything else checks out against the outputs:

- All other "**Result:" cells (17 to 64).
- The Summary (cell 65).
- The README table and its run time: about 3 minutes stated, 2.6 minutes printed.
- The record's notes. For example: the 2.765009% attack value and its 0.00001 excess; the 3.2468% value with up to 4 more frames allowed; 5 of 7 outside 10% under reading (b); 62.2, 85.2 and 76.2 h; the variant intervals.

**Paper statements, checked in `paper/2104.02710v4.txt`:**
- The paper says each sequence is "to be treated as an independent observation".
- Its licence is CC-BY-NC-SA.
- Table 5 gives 139,112.
- Section 3.1 says the source videos are released, while the datasheet says the raw videos are not included.

**The eight-frame figure in cell 38:** I viewed it. In each frame at least one segment runs across the other mouse or into the background, as stated.

**My round-1 reasons in the record:** they are stated faithfully in my own words, including my wrong count of 4,521 for fig4b. The response corrects it from the printed output: the count is 4,517.

**3. Round-1 points**

All are resolved:

- **B1 (body-length proxy in close frames):** resolved. Flagged close frames have lower confidence than unflagged close frames (−0.082, CI −0.107 to −0.050), and the eight random frames all show tracking errors. The share of real postures is still unmeasured, but 8 of 8 supports "mostly".
- **B2:** resolved. Bootstrap blocks are now contiguous session time, with the new `include` argument.
- **B3:** resolved. The other order of the fast measure is shown as a variant; it gives the same direction, and at 20% its interval includes 0.
- **B4:** resolved. Patches are centred, and the smallest is a true 8 px patch.
- **B5:** resolved. Counts are now printed; my 4,521 was wrong.
- **B6:** unchanged, and adequate.
- **B7 to B9:** recorded as findings.
- **C items:**
  - Keypoints-versus-scores frame counts are now checked: they agree in all 574 sequences.
  - Integer label counts are now printed.
  - A per-sequence table for annotator 1 is added. It cannot locate the 10 frames because the paper gives no per-sequence counts.

Nothing open bears on a conclusion. The three statements above are worth correcting, but none of them affects an outcome.
