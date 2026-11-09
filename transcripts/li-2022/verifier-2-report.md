# Round 2 verifier report: Li et al. 2022 on DANDI:000689 (attempt 000689-li-2022-01)

## 1. Outcomes

The claims file has 39 claims, and the attempt record gives an outcome for all 39. Seven are tested, 13 are blocked as metadata_insufficient and 19 as data_missing.

| Claim | Record | Agree? | Assumption (`assumed: true`) stated and reasonable? |
|---|---|---|---|
| fig3k-nt-sensor-sucrose-increase | partially_reproduced | **No, should be not_reproduced.** The criterion says "Reproduced when the US comparison has p < 0.05 with late higher under every reading". It has one part, and only 2 of its 4 readings pass (cell 25). Those 2 are really one result, because AUC and mean give the same t and p. With the first 16 trials p = 0.093. The direction matches in all four readings, and the record can say so. | Stated. The per-trial z-score is reasonable. But the p = 0.0046 also depends on the trial-averaged regression. That fit has r = 0.25–0.75 in all four M-0 sessions and in M-1 late sucrose (cell 23). The pooled fit (r ≥ 0.94) gives p = 0.64 with all trials. The record reports this, but the conclusion depends on this one fit choice. |
| fig3l-nt-sensor-airpuff-decrease | not_reproduced | Yes | Stated and reasonable: all cues are treated as CS-US trials. |
| fig3-nt-sensor-early-dip | not_reproduced | Yes, judged on the criterion as written. | Stated and reasonable. |
| fig4-recording-count | partially_reproduced | Yes | None |
| fig4c-photoidentification | not_reproduced | **No.** Block 1, taken as the "fake" session, gets a short-latency response from 1353 of 1902 units, and 88% of block-2 responders also respond to block 1 (cell 42). So it does not behave like a session with the patch cord disconnected, or the responses are light artefacts on unsorted channels. The 91–256 "tagged" units are then units that cross the threshold in one block but not the other, on units the record itself calls unsorted. Cell 43 says "a count matching the paper was not expected". This does not test the claim, so it should be blocked (format_error, or the fake/real labels as metadata_insufficient). | "Block 1 is the fake one" is an assumption, but it is not flagged `assumed: true`. All the orders were run, so this does not matter for the result. |
| fig4d-seven-clusters | blocked (methods_underspecified) | Yes | — |
| fig5dh-behavior-clusters | partially_reproduced | **I agree with the outcome, but not the reason.** The criterion says "the defaults of scikit-learn" and does not mention feature scaling. Read that way (raw features, installed defaults), it gives 7 and 5 clusters for all 5 seeds (cell 47). The cluster counts therefore meet the criterion. "Partially" is still right, because "separate passive and active strategies" was not tested. The record's reason, "the shock count does not hold", depends on a reading that is not the criterion's. | Pose clock: stated and reasonable (20 of 21 factors are 0.9874–0.9885). It is only weakly checked where the head sits near the port most of the time: H08 is 29.0 vs 35.1 px, H10 27.7 vs 34.8, H24 38.4 vs 46.8 (cell 15). Z-scored features with the 2020 t-SNE defaults: stated, but it is a choice between equals, not the "best supported" reading. Even under the 2020 defaults the attempt does not use tsfresh 0.16.0. |
| 13 metadata_insufficient claims (fig2c, ed8d, ed8fg, fig4e, ed8i, both fig4fg, fig5a, fig5b, fig5c, ed8e, fig5fi, ed8os) | blocked | Yes. Cell 9 shows that no field holds a group or projection label. | — |
| 19 data_missing claims | blocked | Yes | — |

## 2. Text against the printed outputs

Sentences the numbers do not support:

- **Cell 48, and the record's fig5dh notes:** "4 to 6 and 3 to 6 (raw, 2020 defaults)". Shock under raw features with the 2020 defaults is [5, 5, 5, 6, 4], so the range is 4 to 6. It gives 5 in 3 of 5 seeds, so the shock count holds under that reading (cell 47, `both`).
- **Cell 17:** "the map leaves a lag of 1 to 15 s in some third". H11 has a residual of 19.2 s (cell 15).
- **Cell 17:** "durations equal to the pose series, except H07, H09 and H10". H11's video is 11373.3 s against 10947 s of pose, 426 s longer (cell 16).
- **The record's pose finding:** "800 to 1500 s longer". H09 is 1528 s longer.
- **README:** "rises after learning with p = 0.005 when all trials are used". This holds only under the per-trial z-score with the trial-averaged fit. With all trials, the session z-score gives p = 0.16 and the pooled fit p = 0.64 (cell 25).
- **Cell 27:** "partially reproduced … holds in 2 of its 4 readings". This contradicts the criterion's "under every reading", quoted in cell 24.
- **Cell 49, Summary:** "runs about 1.2% fast … by tens of seconds". A factor of 0.988 over about 11000 s is about 130 s, and the best lags reach about 190 s (cell 15).
- **The record's smoothing-window finding:** "goes from 12 to 6 as the window grows". It is not monotonic: 9 clusters at 20 ms, 12 at 60 ms, 8 at 2 s (cell 38).
- **The record's ed5f notes:** "The ecephys files of 29 mice hold confocal images of PVT slices (COFAImages)". No notebook output shows this. Cell 9 leaves out `acquisition/` and `processing/`.

The fig3k, fig3l, early-dip, fig4-recording-count, fig4c and fig4d numbers in the notes, the Summary table and the README's counts (13 metadata_insufficient, 19 data_missing, 7 tested) all match the outputs.

**My round-1 reasons are restated faithfully.** Two small gaps:
- The point that cell 19 described the regression the wrong way round appears in no reason, only in a response.
- My round-1 statement that there is "no … histology" is repeated in the data_missing reasons, but the record's ed5f note says images exist. If they do, I was wrong on that point, but the ed5f block still holds.

## 3. Round-1 points

**Resolved:**
- Problem 1: the fake-session test is now applied. It exposes the new fig4c problem above.
- Problem 2: a linear clock fit and the video headers were added.
- Problem 3: the share of one mouse in each cluster is shown.
- Problem 4: the regression coefficients are printed. This found the Mouse6 channel bug, which is fixed and checked in cells 18–19.
- Problems 5 and 6.
- Problem 7: all three text errors are corrected.
- Problem 8: clustering without the four sessions is run as a variant.
- Problem 9: a dip-minimum variant was added and the question sent to a reader.
- From "could not check": the group/projection labels (cell 9), the regression coefficients (cell 23), the fake/real tagging counts (cell 42) and the pose clock with video frame counts and durations (cells 15–16).

**Still open:**
- The smoothdata window for SmoothingFactor 0.85 (MATLAB was not available). This keeps fig4d blocked, which I accept.

**What remains that bears on a conclusion:**
1. fig3k should be not_reproduced under the criterion as written, and its significant reading depends on a low-correlation trial-averaged fit.
2. In fig4c the "fake" block evokes responses in most units, so the tagged count does not test the claim; it should be blocked rather than not_reproduced.
3. fig5dh: the counts meet the criterion under its own reading (raw features, installed defaults). The stated reason and the adopted reading need correcting, including the wrong "3 to 6" range.
4. The text errors listed in section 2.
