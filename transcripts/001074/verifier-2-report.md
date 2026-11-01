**Round 2 verifier report: 001074-kalugin-2026-01**

Counts come from the claims file and the attempt record. There are 47 claims and 47 outcomes: 4 reproduced, 1 partially reproduced, 7 not reproduced and 35 blocked (13 for missing data, 22 for insufficient metadata). Twelve outcomes are tested, and 10 of those are marked `assumed: true`.

## 1. Outcomes and assumptions

| Claim | Outcome | Agree? | Assumptions |
|---|---|---|---|
| link-revision-well-order | reproduced | Yes | Not flagged as assumed. The threshold was set by the author and is stated. |
| fig1c-cells-per-gel | reproduced | Yes | Stated and reasonable: reading (b) only, gel thickness taken as the imaged z range, contexts pooled. |
| fig1g-sensor-yield | partially_reproduced | Yes | Stated: the peak rule, the boxcar, and no hand corrections. No variant brings the cell counts into range (cell 22). |
| fig1g-all-ten-sensors-respond | not_reproduced | Yes, as the criterion is written | Stated. **Claims-file issue (reported, not corrected):** the Methods say Figure 1G's bottom panel is the derivative ("large values at the times when the signal was rising the fastest (Figures 1G, bottom…)"). The criterion instead asks whether peak-normalized dF/F0 is highest in each well, which carry-over defeats. The failure probably reflects how the criterion reads the figure, not missing responses. Referring this to a reader is right. |
| fig1h-crosstalk-pairs | not_reproduced | Yes | Stated. It fails under both labellings and both windows (cell 28). |
| table1-ec50-on-target / off-target | not_reproduced | Yes | Stated. Every normalization and labelling fails, including the Methods reading (iii/iii-b): at most 3 of 10 on-target and 0 of 4 off-target (cell 31). |
| table1-peak-dff-morse | not_reproduced | Yes | Stated (at most 5 of 14 within 10%). |
| fig1j-ec50-consistent-across-probes | not_reproduced | Yes | Stated. Neither reading holds in any variant, so the result is not a split. |
| figs3e-tau-on-under-one-minute | reproduced | Yes, but marginal | Stated, but the outcome rests on every main choice. The concentration count is exactly at the threshold (8 of 10). Each variant gives a split that the criterion would block as methods_underspecified: reading (a) labels (10 vs 7), the fitted EC50s (8 vs 7), and free x∞, which corrects the bias I raised in B7 (9 vs 6; 8 vs 6 with reading a). |
| figs3f-depth-delay | not_reproduced | Yes | Stated. The code's depth orientation is reasonable, and no variant reaches 9 of 10. |
| figs2f-cells-tracked | reproduced | Yes | Not flagged as assumed, yet it rests on reading `matched<k>` as one pair (taken from the code) and on the code's S2F sets. Both are stated in the deviations, and the all-probes variant (0.61) does not change the outcome. It should arguably carry `assumed: true`. |
| 13 blocked for missing data, 22 for insufficient metadata | blocked | Yes | fig3g is now partly shown (two of four probes). Keeping it blocked is right. |

**Second claims-file issue (reported, not corrected):** the SENSOR IDENTITY header gives the derivative window as 30 frames and credits it to the Methods. The Methods say 1 minute. The notebook uses 31 frames as the main window and 30 as a variant. This changes nothing material (559 vs 550 cells).

## 2. Sentences the outputs do not support

- **Cell 4, attempt record (fig1c deviation and finding):** "mask volumes have 15 to 26 planes". Cell 3 prints a minimum of 16, so it is 16 to 26. My round-1 B9 made the same error.
- **Cell 6:** "All dipping files but a few have frame counts that are multiples of 93". Cell 5 prints 254 of 384, so 130 files (34%) are not.
- **Attempt record, methods_unavailable finding (2):** "median log10 distance from Table 1 0.12 to 1.49 across readings". This is the round-1 figure. Cell 31 now prints 0.12 to 1.48 for reading (b) labels and 0.11 to 0.67 for reading (a).
- **Cell 50 and the attempt record's figs2f notes:** "In 70 of the 71 pairs with both files, the two hold the same count". Cell 49 counts every pair present in the dandiset. A pair whose moving recording has no file with that suffix counts as agreeing. No output shows how many of the 71 pairs actually have two files, so "with both files" is unsupported. The check may say nothing about pairs k≥1.
- **Cell 52:** "No file of any context holds … a region or a sensor label". This line is a fixed print statement. The table only shows acquisition and stimulus counts, the rates and the starts, so the region and label part is asserted, not shown.
- **README:** "the labels are made from the traces by the Methods' clustering". This leaves out the two assumptions the author added (the peak rule and the 1-minute boxcar), which are not in the Methods.

Everything else checks against the printed outputs. That covers every "**Result:**" cell (16, 20, 23, 26, 29, 33, 34, 37, 40, 43, 46, 50, 55), the Summary (including "only figs3e depends on the labelling reading"), the README table counts (13 and 22) and the outcome notes.

The verification block states my round-1 reasons faithfully and in my own terms, and "agreed with 44 of 47" is correct. One small difference: for the 22 metadata-insufficient claims it merges my separate slice and mouse reasons into one, and attaches B12 (which I marked as not affecting a conclusion) to each of them. That is acceptable.

## 3. Round-1 points

**Resolved:**
- **B1:** the peak rule and the boxcar are now stated, and variants are shown.
- **B2:** the reading (a) labels are carried into every section.
- **B4:** fits on the lower bound are flagged, and variant (iii-b) is added.
- **B6:** the per-probe EC50s are also judged against Table 1 (a').
- **B9:** depth is now checked on all ten probes using the matched dose-recording masks.
- **B10:** the difference from the paper's 506 cells is acknowledged.
- **B11:** the main result now uses the code's sets, and the code that writes `matched<k>` is quoted.
- **C (fig3g):** the mouse probes with post hoc dipping are listed, and the two 2025 probes are labelled.
- **B3:** partly resolved. The well increments show the failure is carry-over. The label check is circular, as the notebook says. The only independent check of the labels is still the dose-block test in cell 14, where DA scores 0.41.

**Not acted on, and not affecting a conclusion:** B8 (residual from the jump removal), and the 13/14 in vivo stability denominator.

**Still bearing on a conclusion:**
1. **figs3e:** "reproduced" holds only under the reading (b) labels, the Table 1 constants and the fixed x∞. Each alternative gives a split that the criterion would block. This should be stated as marginal.
2. **fig1g-all-ten-sensors-respond:** the outcome depends on a criterion that may misread Figure 1G. That question is still open with the reader.
3. **figs2f:** the 70-of-71 agreement check behind the `matched<k>` reading is not shown to compare two files per pair.
