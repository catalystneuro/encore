The claims file is ready for an attempt. I made 10 corrections to individual claims and added the check entry under `checks`.

**Checker result:** `claims/wirtshafter-2020.yaml: 31 claims, 31 quotes, 44 statistical values, 2 problems`. Both problems are in `fig5s5-skew-frai`. The text extraction garbles two p-value bounds ("p<9 -13" and "p<9 -10"), so the checker can't find them. Reading them as 9e-13 and 9e-10 is correct, and I kept them. The count of statistical values dropped from 45 to 44 because I removed one entry (`fig4gh-firing-increases`, below).

**Changes, by claim:**
- **fig2b-poisson-control:** The criterion drew the 454 artificial units with replacement from the 378 included LS cells, a step the paper doesn't give. 454 is close to the 452 LS units recorded, so which units they come from is now named as open, with two readings. The note now says the t-test's df of 818 fits neither count.
- **fig3s1-speed-acceleration:** The expected count of 2 cells had tolerance 0, but the criterion accepted up to 3. I set the tolerance to 1 and gave the reason (10% of 2 is less than one cell). I removed a "partially reproduced" rule whose thresholds (median below 0.1, at most 5 cells) the paper doesn't give. I also clarified which bins are used and said the acceleration definition is a standard choice.
- **fig4gh-firing-increases:** Removed the statistics entry with p < 0.05. The legend prints no p-value or threshold, so the criterion now names p < 0.05 as a reading.
- **fig5e-reward-proximate-skew:** The statement's "LS fields ramp up firing on reward approach" comes from Discussion paragraph 8, not from the quoted sentence. I added that paragraph to the source.
- **fig5s2-skew-distance:** The r2 of 0.07 is an expected value with a tolerance, but the criterion said it was only reported. The criterion now requires it to be within tolerance.
- **fig6de-choice-side-bias:** The note said both arm-test dfs are close to twice the field totals. That holds for LS (334 = 2 × 168 − 2) but not for CA1: 364 matches no CA1 count (2 × 154 − 2 = 306). Corrected the note.
- **fig6g-ls-choice-by-direction:** The df of 254 doesn't match the 138 toward-reward LS fields (that would be 274). Corrected the note.
- **fig7s2-ls-rates-by-location:** The criterion judged on the LS fields of matched pairs, as "the sample the df suggests". The df implies 115 fields, which matches neither the 146 located LS fields nor the roughly 92 matched pairs. The sample is now named as open, both readings are run, and the protocol's rule applies when they disagree.
- **fig7s3-pair-distance-control:** Its statistics record a small but significant 3 cm difference in centre distance between choice and middle pairs, which the statement left out. Added it.
- **fig7c-thirds:** The analysis code (`CCpairs.m`, commit 5c6320a9, which I cloned and checked) uses the raw cross-correlation mean for the first third but subtracts the shuffle for the middle and last thirds. The Methods subtract the shuffle throughout; that is now the main reading, with the code's mix as a variant.

**Checked and left unchanged:** every count, percentage, df and field total I could recompute agrees with the paper. All the paper's main findings have a claim, and none comes from outside the paper. The code details I spot-checked also match: the FRAI formula, the 0.5 Hz rule, the 1950-bin coverage rule, the 15 and 20 cm lap windows and the 3 cm line that is commented out.

**Still open** (each is named as a reading in the file, not settled):
- The Methods say the field boundary is where firing is "equal to or less than" 1 SD above the mean; the Results and the code say at or above.
- Rate cut-off: 0.05 Hz in the Methods against 0.5 Hz in the code.
- What counts as full track coverage.
- The location chi-squared value: 6.03 in the Results against 12.7 in the legend.
- The CA1 arm test, printed as t(364) = 2.34 with p > 0.05, which that df doesn't allow.
- The 20 ms lag: the Results put it on the choice arm, the legend on the forced arm.

**Ready:** yes. Nothing was committed or pushed.
