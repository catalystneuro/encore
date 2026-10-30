**Verifier report, round 2: doi:10.1038/s41586-025-08790-w on DANDI:000402 (0.230307.2132)**

The claims file has 36 claims: 16 on the dataset, 3 `with_inputs` and 17 `elsewhere`. The attempt record gives an outcome for each of the 36:

- 10 reproduced and 3 partially reproduced;
- 23 blocked: 16 by `other`, 4 by `data_missing`, 2 by `too_large` and 1 by `metadata_insufficient`.

It also holds a round-1 verification result for each of the 36.

### 1. Outcomes

No outcome in the attempt record is marked `assumed: true`; the word does not occur in the file. Two outcomes rest on choices that are stated as deviations, and both are reasonable:
- The 14-scan list was read from the image of Extended Data Table 1. The exact mask totals in cell 14 support it.
- The Monet2 directions were measured from the stimulus video.

**I agree with these outcomes:**
- **Reproduced:** scans-14-p75-p81, scan-configurations, masks-125413-somatic-115372, stimulus-composition, oracle-same-order, nuclei-144120 and cell-classification.
- **Reproduced, though the criterion tests little; the record says so:** fig3f-oracle-reliability and fig3g-direction-tuning.
- **Partially reproduced:** stimulus-conserved-across-scans, spontaneous-periods and behaviour-recorded.
- **Blocked:**
  - unique-neurons-75909, z-drift-under-10um, structural-stack and photodiode-89pct, all `data_missing`;
  - area-split-half-visp, `metadata_insufficient`; I said `data_missing` in round 1, and either fits;
  - the 3 `with_inputs` claims and the 13 `other` claims among the `elsewhere` ones.

**monet2-directions, reproduced:** I now agree. Cell 33 measures the directions by optical flow:
- All 560 trials have 16 distinct directions under both measures, the largest deviation from the grid is 7.9°, and both showings of each seed give the same directions in 280 of 280 pairs. That agreement checks the method independently.
- The method was changed after the first one failed. This is disclosed, and it is justified by the bias of the phase correlation towards whole-pixel shifts.

**I do not fully agree with these two:**
- **synapse-detection, blocked `too_large`.** The record says a count of the same 20 GB file took 10 minutes in an earlier run, and that the entry's run stalled. That is a failed run, not a file too large to process. The count for subvolume 65 should be retried, or the reason recorded as `other`. The subvolume 35 count and the precision and recall would stay untested either way.
- **em-sections, blocked `too_large`.** The record's metadata bounds (7,904; 14,816; 27,903) already decide the second expected quantity, the share of sections in subvolume 35: (14,816 − 7,904) / 20,000 = 34.6%, against 35 ± 3.5. Only the exact section count needs whole sections. The patch read that put the first section at 7,931 was run outside the notebook and has no printed output.

### 2. Statements against the printed outputs

Almost every sentence in the "Result:" conclusions, the Summary, the README and the record's notes matches the outputs. The exceptions:

**Cell 35 and the monet2 notes: "for the two seeds it flagged".**
- The phase correlation flagged 4 trials by the 10° rule and 6 on the grid (cell 33). Only one trial each of seeds 7637 and 6154 is printed.
- In round 1, seed 6154 was not among the grid failures. So at least two of the 6 grid-flagged trials belong to seeds that are not printed.
- The outcome does not depend on this, since the optical flow gives 16 directions in all 560 trials.

**Cell 43 and the fig3f notes: "The score on fluorescence carries a shared, stimulus-locked signal … does not separate neural reliability from that shared signal".**
- Cell 41 shows that removing each mask's fit on its field's mean trace barely changes the scores: somatic 0.200, 0.380 and 0.665 against 0.208, 0.396 and 0.702.
- That is evidence against a field-wide shared signal driving the scores. The high artifact-mask scores (0.235, 0.402 and 0.650) stay unexplained; a local neuropil signal or real neurites could account for them.
- "Cannot separate" is fair. "Carries a shared signal" is not shown for the unit scores.

**Cell 47 and the fig3g notes: the 80 units shown respond more at their preferred direction "in 91.2% of cases (median … 2.87)".**
- The 80 units are chosen by a preference index computed over all 40 trials, which include the second-half trials used to test them (cell 46). So 91.2% and 2.87 are inflated by selection.
- The unbiased number is 0.629 over all somatic masks. The fig3f caveat about shared stimulus-locked signals also applies to it and is not discussed.

**Cell 30 and the behaviour notes: "Of the 5 files outside the paper's 14, the eye tracking also stops early in 4-10, 5-3 and 8-7".**
- By the notebook's own 1 s rule (cell 29), 4-9 (3.9 s early, starting 1.77 s late) and 8-9 (6.2 s early) also fail. So all 5 fail.
- These files are not among the 14, so no conclusion changes.

**Summary (cell 61), wording:**
- "13 other … the CAVE tables that choose their neurons need an account token" does not fit fiducial-automatch, vessel-automatch, hybrid-automatch, fiducial-transform-residual or fig7d. For those, the CAVE tables are the data themselves, or no table is named.
- The `with_inputs` row says "variants on the dataset's own EM identifiers above" for fig6k-target-responses too, but no variant was run for it.

**Statements without printed output.** Several notes rest on nothing printed in the notebook:
- the em-sections bounds and patch read;
- the earlier 10-minute synapse count;
- the BossDB stack path and the export sizes (about 20 GB each).

**README.** Each row agrees with the record. I could not check the "about 12 minutes" run time; the printed cell times add up to about 8 minutes, and some cells print none.

**My round-1 reasons in the record.** They are in my own words and faithful, with two gaps:
- **em-sections:** the record keeps my round-1 "Blocked (other)" and answers "No change of outcome", but the outcome is now `too_large`. The response should say the outcome changed.
- **Problem 7:** per-unit delay and shared time stamps. It appears in no reason. It does not affect a conclusion, and the record's deviations now state it.

### 3. Round-1 points

**Resolved:**
- 1, spontaneous-periods: the bounds are now compared and the outcome is partially reproduced.
- 2, behaviour-recorded: the series in file 4-7 are listed.
- 3, stimulus-conserved-across-scans: the repeated Trippy seed is recorded.
- 4, monet2-directions: the outcome is now settled by the optical flow.
- 6, fig3g: the count is given a reference.
- 9, ed4: the variant is run on reading (b) only and decides nothing.
- 10, cell-classification: the 82,247 sum is stated.
- 11, oracle-same-order: the check now counts trials inside a repeat.
- 12, scan-configurations: the fields-by-depth table shows exactly two per depth in all 19 files.
- 13, cell 0: the group listing is printed and the unsourced statement is removed.
- C, NWB group listing, scan 4-7 eye series and fields per depth: all now printed.

**Addressed, with a new over-reach:** 5, fig3f artifact masks. The artifact-only distribution and the field-mean regression are now computed, but the interpretation goes beyond the numbers (section 2).

**Disclosed and unchanged:** 7. It does not affect an outcome.

**Partly addressed:** 8, BossDB. The notes now list the public exports and why they do not suffice.

**Still open, bearing on a conclusion:**
1. synapse-detection: `too_large` is not supported, since the same count ran in 10 minutes before. The count for subvolume 65 should be retried, or the reason changed.
2. em-sections: the subvolume 35 share can be tested from metadata, so the claim is at least partly testable. The patch read should be put in the notebook or removed from the notes.
3. fig3g: the 91.2% figure is inflated by selection. The conclusion should rest on the 62.9%, and the shared-signal caveat should be stated.
4. fig3f: the sentence on the shared signal should match the regression result.

**Still unverifiable by me:**
- The cells of Extended Data Table 1. They are now cited but cannot be printed from the data.
- The phase-correlation results for the unprinted grid-flagged trials. They are moot for the outcome.
