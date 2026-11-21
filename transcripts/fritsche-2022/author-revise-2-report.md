Round 2 is finished. No outcome changed and none is proposed for change: the verifier agreed with all 31, so the counts are still 26 reproduced, 3 partially reproduced and 2 not reproduced. I re-ran the entry twice with `python tools/entry.py all entries/fritsche-2022`, once after adding the new output and once after the text fixes. Both runs passed with 0 errors, and every recorded `measured` value still appears in the new outputs.

**Output added**
- **fig3b with `noise` units kept:** the verifier said the effect of keeping these units had not been shown for the one reading that passes. I added that variant, for all 12 readings, to the end of cell 66 so the cell numbers do not shift.
- **Result:** with `noise` units kept, no reading meets fig3b's criterion or its partial rule. Under the reading that passes (pooled ratio, blanks held, pairs across blocks), RL stops at 5-back, below the threshold of 6. This confirms the outcome rests on the `noise` filter, as the record already said. The verifier found the filter reasonable and it is not changed, so the outcome stays reproduced (assumed). The result is now in the fig3b result cell (cell 68), the notes and the deviation.

**Sentences corrected, in the notebook and the record notes**
- **fig3a-v1-long-term:** "Eight of 12 readings give 8" now says seven of 12.
- **decay-cortex-double-better:** the p-value range using every unit's values is now 4.5e-09 to 0.0021.
- **fig8:** "contains the ground truth in every run" now covers only the six named runs, and adds that over the 200 extra seeds the true value falls inside the interval in 192 (drifting) and 189 (static).
- **Summary:**
  - It now says the main reading matches the paper's 1-back values to within 0.01 only for drifting gratings and static gratings in cortex. For static gratings in the thalamus it gives LGN 0.957 against 0.93 and LP 0.900 against 0.85.
  - It now states the two assumptions separately. Leaving out `noise` units affects both decay-thalamus-single and fig3b. Counting only ratios below 1 as significant adaptation affects fig3b alone.

**Recorded**
- **Round-2 entry:** added under `verifications`, with 31 results, each with `agrees: true`, the verifier's outcome, its reason in its own words, and my response. This includes the verifier withdrawing its round-1 remark that results are "unchanged without" the `noise` filter.
- **Critical findings:** the round's `findings` list is empty, because no finding in the record is rated critical and the verifier saw no reason to rate any that way.

**Not done, and why**
- **fig8:** still not reproduced. The verifier thinks the claims file misreads the paper here, but the claim stays as tested on the claims file, and the question for a reader is already in `questions/fritsche-2022.yaml`.
- **fig7a and fig7b-static-areas:** no change. The verifier described the FDR family of 1 to 20 as the claims file's reading, reported, and bearing only weakly on the conclusion. It did not call it a misreading, so I added no question.
- **Run-to-run differences:** two near-zero fast time constants (AL and PM, in cell 76) came out slightly different from the verifier's run. Neither value is quoted or used in any conclusion.

Nothing has been committed.
