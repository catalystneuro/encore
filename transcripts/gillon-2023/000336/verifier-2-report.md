**Round 2 verification: Gillon, Lecoq et al. (2023), DANDI:000336 → 000037**

**1. Outcomes**

The claims file has 18 claims and the attempt record has 18 outcomes. I agree with all 18.

- **dataset-holds-paper-sessions, not_reproduced: agree.** Cell 18 now opens a file from all 16 subjects, and none of their IDs is in Table 2.
- **table1-subjects, table2-sessions, roi-counts-per-session, fig8-example-matches, stimulus-durations, fig6-behaviour, fig7b-signal-stable: reproduced, agree.** The printed counts match exactly (cells 21, 24, 33, 39, 43, 54, 63).
- **session-schedule and tracked-rois-per-plane, reproduced: agree.** Each holds under readings the claims file names: (a)/(ii) for the schedule, (a) for the theoretical maximum.
- **imaging-planes, partially_reproduced: agree.** Rate and image size hold. Depth matches in 47 of 50 sessions, and the raw strings show 60 µm is the deposited value (cell 30). The criterion has no partial rule, so "partial" is a judgement, but a reasonable one.
- **fig8-ordering-variation, reproduced, `assumed: true`: agree.**
  - The assumption (overlap read as IoU of registered masks, applied to every pair in a three-session match) is stated and reasonable. Somatic variation is below dendritic in every row of the summary (nb2 cell 4), including the linked-pairs and no-threshold variants.
  - One deviation is not recorded. The claims file asks for "each tracked mouse", which is 13 mice: 411400 and 412933 are tracked in sessions 4 to 6. The notebook uses the 11 analysed mice. Both left-out mice are dendritic, so this is unlikely to change the outcome.
- **inconsistent-event-fraction, reproduced: agree, but the outcome rests on two choices that are not marked `assumed: true`.**
  - The criterion asks that "every consistent and inconsistent duration lies in the stated ranges". On raw row times, 49 consistent, 377 Gabor and 347 flow runs fail. All pass only after rounding to the Methods' 1.5 s / 1 s grid.
  - The block count is judged on the session mean. Per session, 2 Gabor and 11 flow sessions of 33 fall outside 27 to 33 (cell 46).
  - Both choices are stated (one as a deviation, one in the notes) and both are defensible. Because the outcome depends on them, it should carry `assumed: true`.
- **fig5-stimulus-responses, reproduced: agree.** All reading pairs hold (cell 49), and the outcome survives the b_u variant.
- **fig7a-snr-high-stable, reproduced: agree.** It follows the criterion. The notes now say that noise alone gives SNR ≈ 2.06.
- **fig7c-correlations-similar, blocked (methods_underspecified): agree.** Reading (i) holds in 5 of 6 comparisons and (ii) in 6 of 6.
- **high-correlation-pairs, not_reproduced: agree.** Readings (a), (b) and (c) are all above 0.015%.
- **fig9-onset-offset-transients, reproduced: agree.** It holds in 12 of 12 groups under both readings (cell 73).

**2. Text against printed outputs**

*roi_matching_orderings.ipynb, cell 9 (Result), against cells 4 and 6:*
- "with the 10% overlap threshold the range over mean is 0.036 to 0.26": the printed range is 0.0356 to 0.3088 (433448).
- "with 20% 0.053 to 0.41 (mean 0.161)": the printed values are 0.0533 to 0.4000, mean 0.1595.
- "range over mean 0.029 to 0.40, mean 0.113 at 10% and 0.172 at 20%": the printed range is 0.0299 to 0.4078, with means 0.1368 and 0.1836.
- "range over mean 0.040 against 0.004": the printed value is 0.0381.
- "(34 and 44 for 433414 and 433448)": cell 6 prints 33.7 and 43.2.
- "…against 118 and 112), Xfiles'.": this is a corrupted fragment in the text.

*Attempt record, fig8-ordering-variation notes.* They repeat the cell 9 numbers above (0.26, 0.41, 0.161, 0.113, 0.172, 0.040, "44 against 112"). They also contain three more that do not match cell 4:
- "mean 0.136": the printed value is 0.137.
- "SD over mean mean 0.055": the printed value is 0.057.
- "and 0.079": the printed value is 0.076.
- "The dendritic counts of this run differ slightly from those of the first run … (433414 18 to 22 at 10%, against 18 to 21)": this run prints 18 to 21 for 433414 (nb2 cell 3). The summary means (0.137/0.057 and 0.160/0.076) equal the values I read in round 1, so the outputs do not support a difference between runs. The stale numbers seem to come from some other run.

None of these errors changes the fig8 outcome.

*Attempt record, fig9 notes.* "On that variant the claim would not be reproduced" is wrong. On Gabor-only offsets both readings agree that some groups lack a transient (7 and 9 of 12). The criterion calls that "partially reproduced". My round-1 point B6, which said "blocked", was also wrong on this.

*Cell 61 and the fig7a notes.* "correlations equal those of the paper's code" goes further than cell 60 shows. Cell 60 compares `np.corrcoef` applied to the paper's `rolling_mean`; it does not run the paper's own correlation step (`get_correlation`). The SNR and rolling-mean equality is supported.

*Cell 76.* "with a brief peak after the offset in the mean traces" is backed only by the figure. The printed min/max per trace do not show when the peak occurs.

*Summary (cell 77) and the dataset-holds notes.* "mesoscope imaging" and "V1, LM, PM and AM" are not shown by any output. Cell 4 shows one file with planes in VISl at about 10 Hz. The claims file says this description came from the archive and was not checked against the data.

*README.* "takes about ten minutes": cell 78 prints 13.7 min. The orderings notebook "about fifteen to twenty minutes": nb2 cell 8 prints 21.2 min, and cell 41 of the main notebook says "about twelve minutes".

Every other "Result:" sentence, the Summary table, the README outcome table and the remaining notes match the printed outputs.

*My round-1 reasons in the record.* The `verifications` block restates them accurately and in my own words. The fig8 entry merges B2, B3 and the related items from section C, and the fig7a entry merges B1 with the code-equivalence item; both keep the substance.

**3. Round-1 points**

Resolved:
- B1: noise-floor control added (cell 59).
- B3: reconstruction equals the package's own `NwayMatching.run` in 12 of 12 orderings (nb2 cell 8).
- B4: b_u selection variant and per-session selection counts and thresholds added (cells 49 and 50).
- B5: per-session block counts and the runs furthest from the grid are printed.
- B7: fractions by mouse and with each mouse left out (cell 70).
- B8: all 16 subjects opened.
- Section C: 433414 depth strings, the `mouse_df.csv` content, the Fig. 5 selection counts, and the SNR and rolling-mean equivalence with the paper's code.

Partly resolved:
- B2: the effect of the IoU rule is now quantified and shown as a variant. The dendritic counts still do not approximate the paper's matching, so the outcome rests on the stated assumption.
- B3, max projection: the max projection still stands in for the average projection (stated).
- Correlation step: not checked against the paper's own function.

What remains that bears on a conclusion:
1. **fig8-ordering-variation.** The text and notes misstate several summary numbers and claim a run-to-run difference the outputs do not show. The outcome holds on the printed table. The 13-versus-11-mouse deviation is unrecorded.
2. **fig9.** The record says the Gabor-only variant would be "not reproduced"; under the criterion it would be partially reproduced. This matters if the reader question in `questions/000336.yaml` is answered "Gabor only".
3. **inconsistent-event-fraction.** The outcome rests on grid rounding and on judging the block count by its mean. Both are stated but not marked `assumed: true`.
4. **fig7c and high-correlation-pairs.** The correlation step is not checked against the paper's own correlation function. Both outcomes rest on these correlations.
