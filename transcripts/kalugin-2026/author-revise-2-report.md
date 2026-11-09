I've answered every point in the round-2 report. No outcome changed and no change is proposed, so a third round isn't needed. The final `python tools/entry.py all entries/001074-kalugin-2026` run passed with 0 check errors in about 19 minutes. Every number quoted below matches its output, and nothing is committed.

**Outcomes:** all 47 stay as verified: 4 reproduced, 1 partially reproduced, 7 not reproduced, 35 blocked. The verifier agreed with all 47.
- **figs3e (tau-on under 1 minute):** still reproduced, but the notes, the result cell, the summary and the README now call it marginal. The concentration count is exactly at the threshold (8 of 10), and each alternative choice splits the criterion's two readings. I didn't propose blocking it. The fixed xinf and the Table 1 constants are the method the criterion itself gives, and the reading (b) labels are the main labelling for every claim.
- **figs2f (cells tracked):** still reproduced, now marked `assumed: true`. The reading of the `matched<k>` files is stated as an assumption.

**Corrected or added:**
- **figs2f pair check:** the check now counts the files in each pair. Of the 71 pairs with a matched file, 70 have both files (20230922-PL28 pair 3 has only one). In 69 of those 70 the two files hold the same count, including all 29 dipping pairs with k of 1 or more. This replaces the unsupported "70 of 71".
- **Regions and sensor labels:** the file survey in `morse.py` now reads each file's descriptive fields (imaging plane location and description, session description, mask-table columns, subject fields, analysis group). The blocked-claims cell prints their values by type of recording (dipping, slice, in vivo) in place of the fixed sentence. Every field holds the same placeholder (location "brain"), and there is no label column.
- **Text fixes:**
  - Mask volumes have 16 to 26 planes, not 15 to 26; fixed in cell 4, the fig1c deviation and the finding.
  - The cell 6 sentence on dipping files now gives the counts: 254 of 384 are multiples of 93, and 130 (34%) are not.
  - The question to the authors about the dose-response normalization now gives the median distance from Table 1 as 0.12 to 1.48 with the reading (b) labels and 0.11 to 0.67 with reading (a).
  - The README now names my two labelling assumptions, the 1-minute boxcar and the peak rule.
- **New reader question** in `questions/001074.yaml`: the claims file's header gives the derivative window as 30 frames, but the Methods say 1 minute. Cell 12 and the fig1g-sensor-yield notes say it is asked. The claim itself is unchanged, and it makes no material difference (559 against 550 labelled cells).
- **Round 2 recorded** under `verifications`, with the verifier's reasons for each claim and my responses.

**Not done, and why:**
- **The derivative-shape question on fig1g-all-ten-sensors-respond:** it was already with a reader, so I left it open.
- **Round-1 point B8, the jump-removal residual:** left as is, because the jump is measured the way the paper's code measures it (morse_figs3_rev cell 23).
- **The 13 of 14 in vivo stability count:** it can't be tested, because the files have no stability flag and hold only processed recordings.

The verifier said neither point affects a conclusion. The change to `tools/build_site.py` was there before this run, and I didn't touch it.
