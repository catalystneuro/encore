**Verifier report, round 2: Henry & Kohn 2022 on CRCNS v4-2**

The claims file has 32 claims and the attempt record has 32 outcomes, one per claim: 19 reproduced, 8 partially reproduced, 2 not reproduced and 3 blocked. Three of them are marked `assumed: true`: data-populations, fig5-terms-covary and fig5de-simulated-discriminability. A correction to my round-1 report: its opening sentence gave the counts as 17, 9, 3 and 3. That was wrong. My own round-1 table gives 19, 8, 2 and 3, the same as the record.

### 1. Outcomes and assumptions

I agree with all 32 outcomes. Each one follows from the claims-file criterion and the printed values.

The three assumptions are stated, and all three are reasonable:
- **data-populations:** It takes the blank epochs as the spontaneous condition, which are the only spontaneous data the files hold. The outcome is partial whichever way this goes, because the rule cannot regenerate 396 and 691 under either reading (cell 13).
- **fig5-terms-covary and fig5de-simulated-discriminability:** Both use the single even/odd split in stored order rather than the reliability averaged over 20 random splits (`REL_R`). That is the closer match to the paper's rule, which uses one split. Its counts also sit inside the range of single random splits (V1 143.8, range 126 to 163; V4 238.3, range 219 to 256; cell 38).
- The reason for each assumption is stated in the record and in the methods_unavailable finding.

Other outcomes rest on a reading the criterion allows; this is disclosed each time:
- fig2de uses V1 without the >0.5 restriction (cell 72).
- fig4b uses the t tests on log indices (cell 28).
- figs6 computes the driven fractions on 10 of 22 populations (cell 65).

### 2. Sentences the printed numbers do not support

- **Cell 77:** "The permutation nulls lie above 1 for the same reason ... so each estimate is tested against a null with the same bias." The no-crowding calibration has a mean of 1.17 in V1 and 1.09 in V4 (cell 76). The permutation null medians are 1.37 to 1.63 in V1 and 1.75 to 4.16 in V4 (cell 75). The null is shifted far more than the calibration, so "the same bias" is not shown. The fig2f-v1 sentence "near the medians of their permutation nulls" (cell 79, and the record notes) is accurate as stated, but it inherits this problem (see section 3).
- **Record, fig4a notes:** "each set with one value outside tolerance". Under within-orientation pooling at 2.6 degrees, both values are outside: 2.0 against 2.25 to 2.75, and 14.4 against 11.7 to 14.3 (cell 26). Cell 27 itself says "each far value misses by one neuron". Only the all-orientations pooling has one value out (1.8 out, 12.9 in).
- **Cell 66 and record, figs6:** "The fraction driven by targets (0.372 and 0.396, over the 22 populations) is in the range of Figure S6A, 0.3 to 0.5." Those means include the 12 populations in which no unit can be driven (cell 65: "Populations with no target-driven neuron: 12"). Over the 10 usable populations the same numbers give about 0.82 (V1) and 0.87 (V4), which is above S6A's range. So the agreement comes from averaging in 12 zeros.
- **Cell 66 and record, figs6:** "where any unit responds above the epochs labelled blank; in the other 12 no unit does". Cell 10 shows that 8% to 86% of V1 units and 23% to 75% of V4 units in those sessions do have a target-alone mean above their blank mean. What holds is that no unit exceeds the blank mean plus 1 SD.
- **Summary (cell 89):** "both are properties of the method as the paper describes it, not choices made here". This is said of both the decoders that keep no nonzero coefficient and the upward bias of the estimate. For the decoders it does not hold. The all-zero rate depends on the penalty grid's lower bound, C = 0.01, and the same paragraph lists that grid among the choices made here.
- **Record, methods_unavailable (5):** "5% to 18% of the decoders here have no nonzero coefficient". The printed fractions are of outer folds, not of decoders (cell 69).
- **Record, metadata_error finding:** "blank and distractor-only ... same mean counts as the target epochs (mean z against blank −0.18 to 0.16)". That range is for the target-alone z only. The distractor-only z in those sessions spans −0.29 to 0.37 (cell 9). This is minor.
- **README:** The table gives fig5-terms-covary and fig5de as "Reproduced", with no note that they rest on the even/odd selection. The notebook summary does carry that note.

Every other sentence I checked matches its output. That covers every "**Result:" cell, the Summary sections of both notebooks, the README, and the record notes. I recounted a sample by hand:
- fig7cd: 17 of 22 V1 and 16 of 22 V4 populations below the paper's means.
- fig5de: 3 of 4 spacings, and 1 of 4 with 1000 trials.
- fig4a: neuron counts 8 and 57, against 9 or 10 and 47 to 56 allowed.
- fig2f-v1: permutation p ranges.
- figs3: the closest pass, 0.52 against 0.63.

Round-1 reasons: the record gives my round-1 reasons nearly word for word, in my own words. Where a round-1 problem was merged into a reason, it is folded in accurately: B4 into fig4a, B2 into fig5bc, B1 into figs6, B10 into figs5, B3 into fig2de. "Agrees with all 32 outcomes" is correct.

### 3. Round-1 points

Resolved:
- **B1:** figs6 now says it covers 10 populations.
- **B3:** disclosed; the outcome still depends on that reading, which the criterion permits.
- **B4:** referred to `questions/henry-2022.yaml`.
- **B5, B6, B8, B9, B10, B11:** resolved. The wide grid shows the main run is not censored. The NaN null draws were 0% to 0.15% and changed no percentage. figs3 with 20 draws still passes 7 of 8 pairs. The point-slope check and the lower-first variant are in.
- **B2:** resolved as disclosure. The variant on random-split reliability was run for every tuning-model claim, and the two claims that change under it are marked assumed.
- **Section C:** every item was done. The contrast table is in cell 10. The `REL_R` fits are in cell 56. The null percentiles and the calibration are in cells 75 and 76. The decoder diagnostics are in cell 69. The fig7cd values per population are in cell 87. figs3 now uses 20 draws.

What remains that bears on a conclusion:
1. **fig2f-v1 (significance part) and fig2f-v4:** The permutation null is not calibrated. Its V1 medians (1.37 to 1.63) sit well above the no-crowding estimate (95th percentile 1.26 to 1.29). Judged against the calibration, V1 at 1.3 degrees (1.685) would count as significant. So the V1 significance pattern says little in either direction. The outcome stays not reproduced, because the values fail.
2. **fig2f, fig3c, figs3 and fig7cd values:** In 5% to 18% of folds the chosen decoder has no nonzero coefficient and predicts one class (cell 69). That pulls crowded performance toward chance and plausibly inflates k, for example V4 CA 10.9 and 18.5. The binomial calibration cannot capture it. Its effect on k and d′ was not measured, for instance by re-running with a grid that never leaves zero coefficients. This does not change any outcome: the values already fail, and the comparison in fig3c is internal. It bears on the "differs from the paper" reading.
3. **fig5-terms-covary and fig5de:** Only the decoder counts were shown across the 20 single random splits. V4 r and the fig5de comparison were not. Those two outcomes therefore rest on one particular split. Under `REL_R`, V4 r is −0.459 and V4 meets the fig5de comparison at 1 of 4 spacings, so both would fall below the criterion. Showing the distribution of r and of the fig5de count over single random splits would settle whether the stored-order split is typical.
4. **The section 2 wording errors:** the fig4a notes, the figs6 S6A comparison and its "no unit responds" wording, cell 77, and the Summary's "not choices made here". None of them changes an outcome, but each should be corrected.
