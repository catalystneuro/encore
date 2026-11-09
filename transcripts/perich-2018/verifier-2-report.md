**Verifier report, round 2: Perich, Gallego & Miller 2018 on DANDI:000688 (0.250122.1735)**

The claims file has 28 claims and the attempt record has 28 outcomes, one for each claim: 3 reproduced, 2 partially_reproduced and 23 blocked (data_missing).

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| methods-neuron-counts | partially_reproduced, assumed | Yes | Yes. The per-session ranges hold only if C 2016-09-29 (PMd 114) is not one of the paper's sessions, which is true for 715 of 2002 choices. The pooled >5 Hz counts fail under every choice. |
| fig3b-pmd-higher-dimensional | reproduced, assumed | Yes, but fragile | Partly. The noise scale (difference / √(2K)) is stated, along with the fact that it was chosen after the other scales gave 0. It is a reasonable assumption. The FWHM-kernel reading is stated. Not stated as something the outcome rests on: the 21-session set. Over 16-session choices the medians are within tolerance in only 910 of 2002 (cell 17); the rest would be partial. The record names the session set as an assumption for fig6c but not here. |
| figs4d-dimensionality-robust-to-size | reproduced, assumed | Yes | Yes. It rests on the same noise scale, but PMd > M1 holds under rule (b) at every size, under both kernels, both windows and both session sets (cell 21). |
| figs4c-null-potent-index-centered | reproduced, assumed | Yes | Yes. The adopted reading (absolute values) is the claims file's first reading. One of eight readings fails at 0.100085 (cell 25). Judged alone, Monkey M would fail (0.109). Both points are stated. |
| fig6c-null-leads-potent | partially_reproduced, assumed | Yes, as the criterion applies on 21 sessions. Weak. | Both assumptions are stated: all 21 sessions and the SD kernel. Under the main reading only 763 of 2002 (38%) 16-session choices are significant. With the FWHM kernel no reading is significant (p ≥ 0.18, cell 28), which would make it not reproduced. |
| 23 blocked claims | blocked, data_missing | Yes | Not applicable. No Force, Rotation or Washout trials (cells 3–8). |

**A point I missed in round 1, which bears on fig3b, fig6c and figs4c.** Lines 85–87 of the claims file say that when the readings of an open detail disagree, the claim is blocked as methods_underspecified. The fig3b and fig6c criteria instead say "under one reading". O4 (the kernel width) is named in neither criterion, and the claims file expected it "not to change an outcome".

- The record applies "one reading" to O4 without mentioning the header rule.
- No single kernel reading supports both outcomes:
  - FWHM: fig3b reproduced, fig6c not reproduced.
  - SD: fig3b partial, fig6c partial.
- The record picks the favourable kernel for each claim.

The record should say which rule governs O4 and state the inconsistency between the two claims. This is an internal inconsistency in the claims file, not a misreading of the paper.

### 2. Sentences the outputs do not support

- **Cell 4:** "plus four later Monkey M sessions (2014-09-29, 2014-12-03, 2015-05 and 2015-06) whose PMd counts (22 to 124) and reward counts (194 to 733) do not fit the paper's ranges."
  - Cell 3 lists 13 later dual-array CO sessions, not four.
  - Their rewards run from 174, not 194. The June 2015 sessions (174–196) fall inside the Baseline range.
  - M 2014-09-29 (PMd 124) and M 2015-05-12 (PMd 60, M1 30) are inside the widened Monkey M ranges. 2015-05-12 is excluded only by its 443 rewards, while C 2016-10-13 and 2016-10-21, which are also outside the reward range, are kept.
  - Little effect on the conclusions: the 7 February–March sessions match the paper's bounds exactly (66, 121 and 26 in cell 12).
- **Cell 0:** these sessions "have unit counts that match the paper's ranges". C 2016-09-29 does not (cell 12).
- **Cell 8:** "in every session the mean absolute deviation of the first eight reward trials is close to that of the last eight, except in C 2016-09-23 and C 2016-10-11".
  - M 2014-03-03 gives 14.0 against 6.4, with signed means of 10.2 and 3.3 and a significant trend (p = 0.019). M 2014-02-03 and 2014-02-18 give 9.1/5.6 and 8.8/4.8 (cell 7).
  - The cell does not mention that C 2016-10-11 has a significant decreasing absolute deviation (rho −0.21, p = 0.003).
  - This affects no conclusion.
- **Cell 23 and the figs4d notes in the record:** "both areas fall at small sizes (… M1 8.52 to 8.03)".
  - The M1 means at 60 and 70 neurons (8.53 and 8.65) equal or exceed the all-neuron mean.
  - The 40-neuron mean covers 17 sessions, against 21 for "all".
  - In window (b) with the FWHM kernel, M1 at 40 (6.74) exceeds "all" (6.52) (cell 21).
  - A fall in M1 is not shown. This is outside the criterion.
- **Record finding (metadata_error):** "the cursor never enters the square … Monkey M 2014-02-03 and 2014-02-18". Cell 7 gives 0.01 for both.
- **Record verification, figs4d reason:** "25 subsamples with 100 noise repetitions were used instead of 100". My point was 25 subsamples instead of 100, and 100 noise repetitions instead of 1000. The record's other restatements of my round-1 reasons are faithful, including the archive check appended to each blocked claim.

All other numbers in the conclusions of cells 14, 19, 23, 26 and 31, the Summary (cell 33), the README and the record's notes match the printed outputs.

### 3. Round-1 points

**Resolved:**
- 1: session dependence of fig6c is now tested and stated.
- 2: edge maxima are flagged; without them the mean is −20.5 ms, p = 0.034.
- 5: the figs4d justification is corrected.
- 8: the cut-off warning is read and recorded as a finding.
- 9: signed errors are now printed.
- 10: the pooled verdict is relabelled.
- 11: the Monkey M bias is stated.

From "could not check":
- The FWHM values per session and the medians over 16-session choices are printed.
- The unrounded figs4c mean is printed.
- The lag curves are plotted for all four window and resolution readings.
- The warning text is truncated in the source.
- The acquisition-time check is consistent: movement ends 0.09–0.15 s after the assumed acquisition time.

**Partly resolved, does not affect a conclusion:**
- 6: 100 subsamples are now used, but still 100 noise repetitions; this is stated.
- 7: the window (b) alignment is stated as a deviation but not changed.

**Remaining, bearing on a conclusion:**
1. **Kernel width (point 3):** now stated, but there is the cross-claim inconsistency and the unaddressed header rule from part 1. This affects fig3b and fig6c, and figs4c through its one failing reading.
2. **fig6c session set:** stated, but the result holds for only 38% of 16-session choices (51% for any of the 8 readings).
3. **fig3b session set:** reproduced in 910 of 2002 16-session choices. This should be named as part of what the outcome rests on.
4. **Noise scale (point 4):** stated and sent to the authors as a question. The synthetic check (cell 18) does not tell the scales apart, since raw and √2 also return 5 there. The choice rests on the other scales giving 0 on the real data.
5. **Whether the units are the paper's sort:** still open. It bears on methods-neuron-counts.
