**Round 2 verification: saez-2016-01**

**1. Outcomes and assumptions**

The claims file has 16 claims, and the attempt record gives 16 outcomes: 7 reproduced, 6 partially reproduced and 3 blocked. Eight of them rest on an assumption. I agree with all 16 outcomes.

- **dataset-size, reproduced.** I agree. This was my round-1 position. The fill of every Summary row is now printed (cell 29): included rows are green or unfilled, and every excluded row is red.
- **fig1c-control-outcomes, partially reproduced (assumed).** I agree, with the same reservation as in round 1. On the 20 measured cells, 5 to 7 are plastic (25 to 35%). The partial result needs the 7 missing cells to count as NC, based on their sheet changes being under 15%. Cell 32 shows that this bound fails for 5 of the 16 measured cells it can be checked on. Under (a,a), one extra plastic cell among the 7 would drop the result below partial. The record says all of this plainly.
- **fig1-control-no-net-plasticity, reproduced (assumed).** I agree. p = 0.27 to 0.44 (cell 35). The assumption (the last 120 baseline sweeps form the pre-pairing epoch) is stated and reasonable: the Methods' wording supports it, and so do the sheets' pre-pairing means (4.5% median difference against 24.3% for the first 120; 26 of 36 cells closer). With the first 120, the outcome reverses (p = 0.013 to 0.036). This is disclosed.
- **fig1-control-mean-change, partially reproduced (assumed).** I agree. Cell 38 shows the three means within tolerance under (a) and (c) and the SD outside, at 13.2.
- **fig1-vc-ic-same, reproduced (assumed).** I agree. The readings disagree: under (a), Shapiro-Wilk on IC gives p = 0.0497. The claims file's rule for claims of absence then lets the author adopt one reading. The choice of (P)(c) is stated, and its support is reasonable but thin. Both 120-sweep readings fit "Traces compared, 120", and the closeness argument rests on 34 against 30 of 46 cells.
- **fig1fh, fig1d, fig2cd, fig2f, reproduced.** I agree (cells 44, 47, 62, 65). The assumption behind fig1d is stated.
- **fig2a-bicuculline-outcomes, partially reproduced (assumed).** I agree (cell 50).
- **bicuculline-increases-plastic-fraction, partially reproduced (assumed).** I agree. The control count is never within 4 ± 0.4 (cell 53).
- **fig2-subgroup-changes, partially reproduced (assumed)** and **fig2-mean-unchanged-variance-increased, partially reproduced.** I agree, now that VCB17 is shown to be a real response (see section 3).
- **The three fig3 claims, blocked (data_missing).** I agree.

**2. Sentences the printed numbers do not support**

- **Cell 17:** "its per-sweep amplitudes (mean 100 pA) are twice the same measure before the stimulus (median 50 pA)". This sets a mean against a median. Median against median is 94.3 / 49.5 = 1.9, which is why cell 14 lists VCB17 as below 2. In the same cell, "so it does not depend on the baseline or on noise" goes too far: the 50 ms-baseline variant tests the baseline, not the noise floor. The conclusion that the response is real still stands on the median traces (93 and 473 pA) and on the sheet values less the holding current.
- **Attempt record, fig2-mean-unchanged response:** "without VCB17 the values are within under (b)". Cell 59 gives SD 30.75 under (b), and the tolerance is 34.3 ± 3.43, so the floor is 30.87. Without VCB17 the SD is outside tolerance in every reading. My round-1 figure of 31.56 no longer applies.
- **Cell 13 and the attempt record's fig2a response:** "342 are one sample (0.05 ms) away". Cell 12 prints 120 + 234 = 354.
- **Summary ("some sweeps of 12 files") and the record's fig1c deviation ("in some sweeps of 12 files"):** two of the 12 files, IC13 and VCB19, appear only because of their dropped sweeps with no stimulus (onset at 50 to 60 ms, cell 12). Those are not stimuli moved earlier, so the count should be 10. The record's findings entry (seven files, five cells) is correct.
- **Summary, last bullet:** "+62.9%, which enters the paper's … LTP mean". No output computes the sheet-based LTP mean. Only the sheets' bicuculline mean and SD are shown to match the paper (cell 59).
- **README:** "Outcomes marked 'assumed' rest on taking the last 120 baseline sweeps". fig1-vc-ic-same is marked assumed for the (P)(c) adoption instead, and its first-120 variant passes. The README's next sentence mentions the window adoption, but it does not link it to that row.

All other "**Result:" sentences, the Summary, the README and the record notes match the printed outputs. That covers cells 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66 and 69. In cell 63, "VCB7 under (P)(a)" understates the match: VCB7 is within tolerance in every reading, so the sentence is accurate but incomplete.

The verification section of the attempt record states my round-1 reasons faithfully and in my terms, with each problem point attached to the claim it bears on.

**3. Round-1 points**

Resolved:
- **Point 1 (VCB17).** It has a real stimulus-locked response: median traces of 93 and 473 pA, a steady holding current, and sheet values less the holding current giving +390% (cell 16). Keeping it is justified, and the new finding about the sheet is sound.
- **Point 4 (alignment).** Confirmed in the real data and fixed: sweeps are now aligned on the artifact onset, times are printed at 0.05 ms, and the old alignment is kept as a variant (cells 12 and 22).
- **Point 5 (inclusion by fill).** Resolved by the fill table (cell 29).
- **Point 6 (IC13).** Explained: four sweeps with no stimulus were being measured as responses. With them dropped, IC13 matches its sheet (r = 0.995) at −10.9% (cell 20).

What remains that bears on a conclusion:
- **Point 2.** The fig1c partial outcome, and the "out of 28" control counts in bicuculline-increases-plastic-fraction, still rest on classing the missing cells from their sheet changes. Cell 32 shows that bound is loose. This is disclosed, but the partial outcome is fragile.
- **Point 3.** The last-120 baseline assumption decides fig1-control-no-net-plasticity, fig1-control-mean-change, fig1d and fig2a. It is reasonable and disclosed, and it is now a question for the authors.
- **Point 7, now larger than I judged in round 1.** Cell 38 shows that if the paper exchanged its V-clamp and I-clamp labels, fig1-control-mean-change would become not reproduced. This waits on the reader question.
- **New: the fig1-vc-ic-same outcome depends on the (P)(c) adoption.** Under (a) it fails on one test, at p = 0.0497.
- **The record's fig2-mean response needs correcting.** Without VCB17 the SD is outside tolerance under (b) as well (section 2), so dropping VCB17 would not make that claim reproduced in any reading. The outcome stays partial either way.

I found no misreading of the paper in the claims file.
