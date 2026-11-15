**Round 2 verification: martinez-conde-2019-02**

**1. Outcomes**

The claims file and the attempt record both list 19 claims, and the README and Summary tables match the record. I agree with all 19 outcomes.

- **neuron-counts** (not reproduced), **spikes-per-condition** (blocked), **fig4a** (reproduced), **fig4b-spike-rate-difference** (partially reproduced), **fig4b-pairwise** (reproduced), **fig5** (reproduced), **table1-p180** (partially reproduced), **table1-s40** (reproduced), **fig6** (reproduced), **fig7c-fold-edge-equivalence** (not reproduced), **fig7d-nonlinear** (reproduced), **fig7d-dog-similar** (blocked) and **s3-latency-peak** (blocked): agree. Each of these holds under every baseline placement the notebook prints (cells 23, 26, 37, 46, 49, 55, 61).
- **s4-baseline-no-difference**, reproduced, assumed: agree, because it follows the claims file's rule for readings that disagree. Reading (a) gives smallest BH p = 0.071, while Kruskal-Wallis gives 0.042 and ANOVA 0.007 (cell 17). The outcome rests on three things: the mixed placement, the tie rule, and a p-value close to 0.05. Both single placements find a difference under all three readings. The stored `BaseActivity` finds none under any reading, which supports the outcome. The assumption is stated, and the notes call the result fragile.
- **table1-edge** (partially reproduced, 3/5) and **table1-s90** (partially reproduced, 3/5), both assumed: agree. These are the values I derived in round 1. The Square and Edge squares are centred on the corners.
- **table1-s52**, reproduced, assumed: agree. It needs the Star squares inside the corners and the best of four readings. Centred squares give at most 3/5 and the stored baseline at most 2/5 (cell 43). The notes say both.
- **fig7a-rms-contrast-fit**, blocked (methods_underspecified): agree. On the image gray levels the background equals the 0% level (cell 8; `_gray` maps polygon count 1 and the background both to 0). Adding a black level never gives a rise from 0.61 to 0.943, and the best case is 2 of 6 values (cell 52). The paper's curve needs a luminance calibration or an RMS definition that neither the text nor the files give. My round-1 synthetic background assumed a background below the 0% level, which the image does not show.
- **fig7c-fold-edge-significance**, reproduced: agree. It passes under BH over 40, BH over 10 and Bonferroni over 10, and fails under Bonferroni over 40 (cell 58). The notes say so.

On the assumptions (`assumed: true`): every one is stated in a deviation, and each is reasonable.
- Choosing a placement by how close it comes to the stored `BaseActivity` is fixed before looking at outcomes. The choice for Square and Edge rests on n = 9 and for Star on n = 10.
- The adopted placement differs between the two stimuli, though the paper describes both with the same words. The record says this openly.

**2. Text against outputs**

Every figure I checked in the conclusions, the Summary, the README and the record notes matches the printed outputs. That includes all within-tolerance counts, the differences (2.09, 3.61, 1.51, 1.68, 2.12), the p-values, the ranges and the variant counts. The points below are unsupported or imprecise; none affects an outcome.
- Cell 53: "the window at the 100% end holds a quarter of bright rectangle". Nothing printed shows this.
- Cell 53 and the fig7a notes say RMS is "computed on the gray levels of the stimulus image". `rms_profile` uses the rasterised polygons (`stimulus_luminance`), which match the image in at least 93% of pixels exactly and 99% within one level (cell 8). The image pixels themselves are not used.
- Cell 63, "no data in … any public archive found", and the cell 0 table, "the DOG output of reference 3 is not public". The record only says the dataset's files and description were searched.
- Cell 18 and the s4 notes: "the gap … comes mostly from the smaller sample." This is shown only for the adopted placement on the subset (Kruskal-Wallis 0.081 against 0.114). It is a fair reading, but not a full separation of sample size from placement.

The record states my round-1 reasons faithfully. Problems 2, 4, 5, 6 and 8 are attached to the relevant claims, problem 1 to fig7a and fig7c, and problems 3, 7 and 9 are summarised under `reviewed`. Most of the wording is mine nearly verbatim.

**3. Round-1 points**

Resolved:
- **1 (RMS input):** the image gray levels are printed and checked against the polygons. The outcome changed to blocked, which I accept.
- **2 (placement):** every Table 1 claim now prints both placements and the stored baseline.
- **3 (Star registration):** the polygon fit error (2.3e-13 DU) and a correlation registration are now printed. The best shift sits at the 64 DU search limit in 8 of 12 files, so that test is weak. Dropping the 15 files rests more securely on the aligned diagonal not being stored.
- **4:** the adopted placement is now also run on the subset with a stored baseline.
- **5:** the gray level inside every baseline square is printed (all 0), and the 2 Corners files are fixed.
- **7 and 8:** fixed. For 7 I checked the record's account only, not the code.
- **C items:** the gray levels, the rasterisation agreement, the 0% squares, the variant tables and the Star fit error are all now printed.

Partly resolved: **6**. Reading (ii) was not added, which cannot change the result.

Unchanged: **9**. This is a point about the claims file; its checks still list the Corners two-fold question as open.

What remains that bears on a conclusion:
- **Table 1 placement and subset (table1-edge, table1-s90, table1-s52).** The stored `BaseActivity` gives Edge 0/5, S90 at most 2/5 and S52 at most 2/5 on 9 to 10 neurons. The adopted placement was not run on those same subsets for Table 1, so it is unclear whether these low scores come from the subset or from the placement. This is the Table 1 version of problem 4, and it affects how much these three outcomes can be relied on.
- **s4.** The outcome depends on the tie rule and on BH p = 0.071, as stated above.
- **Claims file, fig7c-fold-edge-significance.** The criterion tests only the levels 0.610, 0.647 and 0.943, but the paper's wording sets limits that the criterion does not check:
  - "An Edge of less than 68% contrast" implies S40 is not significant at 0.684 and above. Under the passing readings, S40 is also significant at 0.684 to 0.795 (BH) or 0.684 to 0.721 (Bonferroni over 10).
  - "A 94% contrast Edge" may mean P180 is lower only near 0.943. Under BH it is lower at all ten levels.

  The notebook reports these levels. I note this as a place where the criterion is looser than the paper's statement, not as a correction.
- **Not checkable here:** S1 and S2 Table are missing, as in round 1.
