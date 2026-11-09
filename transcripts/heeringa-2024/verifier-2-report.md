**Round 2 verification: Heeringa (2024), DANDI:001262 v0.241205.0959**

**1. Outcomes**

The claims file has 23 claims and the attempt record has 23 outcomes. Tallied from the record, they are 14 reproduced, 1 partially_reproduced, 4 not_reproduced and 4 blocked. I agree with all 23.

- **table1-animals-units:** reproduced. Cell 13 shows all eleven counts matching.
- **table1-age-abr-weight:** reproduced. Cell 16 shows 9 of 9 means within tolerance. The SDs and ranges also match the quote in the claims file.
  - `assumed: true` is stated in the record (reading the ABR threshold as a character's code point) and is reasonable. All decoded values are multiples of 5 from 10 to 85 dB SPL (cell 6), and the means, SDs and ranges all match Table 1.
- **table1-bf-range:** reproduced. Cell 19 matches all three ranges exactly.
- **fig3-abr-age:** reproduced. Cell 22 shows the means rising with age and the old group having the largest SD.
  - `assumed: true` is the same ABR assumption. It is stated in the deviations and is reasonable.
- **females-fewer-in-old:** reproduced (cell 25).
- **oxygen-78:** reproduced (cell 28).
- **complex-stimuli-experiments:** reproduced (cell 31).
- **recording-type-counts:** partially_reproduced. In cell 34, 5 of 6 counts match under both readings. CLICK is 271 under reading 1 and 275 under reading 2.
- **fig7-sampling-by-age:** reproduced (cell 39).
- **isi-exclusion:** not_reproduced. In cell 42, 370, 391 and 148 units fail under readings (a), (b) and (c). The criterion gives not_reproduced when units fail under all readings.
- **no-prepotentials, rlf-monotonic, psth-primary-like:** blocked as methods_underspecified. The checks were visual and no rule can be fixed.
- **fig5b-example:** reproduced (cell 50).
- **fig6a-young-two-sensitive-regions:** reproduced under reading (b), which is enough for the criterion (cell 53).
- **fig6b-young-bf-gap:** not_reproduced (cell 56).
- **fig6c-sr-distributions:** reproduced (cell 59).
- **fig6d-max-phase-locking-bf:** reproduced. The highest young-adult BF is 4598 Hz (cell 62).
- **fig6d-highest-vs-low-bf-low-sr:** reproduced (cell 65).
- **fig7a-cf-matches-bf:** reproduced. Cell 68 gives r = 0.973 and a median CF/BF ratio of 1.0028. Both level sources give the same CF.
- **fig7b-click-latency-bf:** reproduced. Cell 71 gives correlations of −0.882 and −0.864 with the 7.75 ms delay, and −0.662 and −0.820 with 5 ms.
  - `assumed: true` (the 7.75 ms click delay) is stated and is reasonable. The outcome is the same under both delays.
- **fig7ab-representative-sampling:** not_reproduced. This follows the record's reading of "none does" in the criterion as "no reading holds for both CF and CLICK". That reading matches how the criterion phrases its "reproduced" case, and the record states the alternative.
- **old-success-rate:** blocked as data_missing. Cell 77 shows no animal without a unit file, and the description does not mention unsuccessful experiments.

No other outcome needs `assumed: true`. Recording-type-counts and fig7ab do not depend on the click delay: reading 2 of recording-type-counts uses no latency, and fig7ab fails on the CF subset.

**2. Sentences the printed outputs do not support**

- **Cell 75:** "The CF part fails every reading, so the outcome does not depend on the choice among them."
  - This conflicts with the record's fig7ab notes. Those notes say the claim would be blocked as methods_underspecified under the other reading of "none", because CLICK passes the KS test (cell 74).
  - The cell's sentence holds only for the choice among (i)/(ii) and (a)/(b). It does not hold for how the criterion's "none does" is parsed. The cell should state the reading it takes, as the record does.
- **Cell 17, and the record notes for table1-age-abr-weight:** "equal the paper's after rounding."
  - Cell 16 prints 5.55 (paper 5.5) and 83.35 (paper 83.4). At two decimals, these values could round either way, so the printed output cannot confirm the sentence. It does not affect the outcome.
- **Cell 72, and the record notes for fig7b:** "inside the 0 to 3.5 ms axis of Fig. 7b, which is consistent with the assumed delay."
  - The axis limits are not in the claims file or the printed outputs, and I cannot check them from the paper text.
  - A range of 0.42 to 2.78 ms is weak support for a delay of 7.75 ms in particular. Any delay from about 7.1 to about 8.2 ms would also fit.
  - The PSTH check in cell 36 only shows that the 10 ms and 20 ms trials share one delay. The record's methods_unavailable finding states this correctly ("do not fix it").
- **Cell 37:** "So the click comes at the same time in both trial lengths."
  - This rests on residuals computed under the assumed delay (−0.032 against −0.027 ms) and on 31 units from 9 animals. It supports "the same within about 0.05 ms", which is acceptable, but it is an inference rather than a measurement.
- **README:** "It takes about six minutes."
  - Cell 79 prints a run time of 2.9 min.
- **Summary, README and record findings:** the short-ISI pairs are called "double detections of one spike".
  - This rests on the dip-ratio rule (ratio above 0.5), which was checked only against reference pairs of 0.8 to 1.5 ms (cell 44, 0.00 of 300 pairs). Nothing checks the rule at 0.3 to 0.6 ms, where the 39% figure comes from.
  - For the pairs below 0.1 ms (ratio 1.00, median 0.95) the inference is sound. For the 0.3 to 0.6 ms pairs it is a plausible reading, not a demonstration.
- Every other sentence I checked matches the outputs, including:
  - the "about half" of short ISIs on one waveform: (1171 + 0.91×2541 + 0.39×10192) / 13904 ≈ 0.54;
  - the 176 and 179 units that still fail;
  - the histogram dip from 0.12 to 0.18 ms (41 to 70 per bin);
  - the 27 young PH units from 4718 to 12,359 Hz;
  - all the fig6a, fig6b and fig6c bin counts;
  - the fig7a statistics;
  - the 270 to 272 units with a latency across delays from 5 to 8.25 ms.

**Round-1 reasons in the record:** they are my reasons, faithfully condensed. Two small things are left out of the recording-type-counts and isi-exclusion reasons: that the maximum latency of 2.78 ms conflicts with 10 ms trials, and the paper's "only rarely". Neither changes the substance. The cell numbers in the reasons follow the round-1 notebook, not the re-executed one.

**3. Round-1 points**

- **B1 (click delay and CLICK count):** resolved for the outcome.
  - Reading 2 (275) uses no latency, and reading 1 stays at 270 to 272 across delays.
  - The 10 ms and 20 ms trials agree: the PSTH onset differs, but the latencies lie on one latency-BF line.
  - click_polarity is "COND" in every trial.
  - The halves of the 500-trial recordings agree about as well as odd and even trials.
  - What remains: why the paper counts 10 or 14 fewer CLICK units cannot be traced, and the absolute delay is not established. Neither changes an outcome.
- **B2 (CF level source):** resolved. The calibrated level column gives the same CF for all 119 units. The manual corrections remain unavailable, as the record states.
- **B3 (fig6a regions chosen around the answer):** resolved. The two lowest bin means overall are the regions used (cell 53).
- **B4 (short ISIs):** resolved. The histogram and the waveform check are added, and 176 units fail under (a) even counting only separate waveforms. The remaining caveat on the dip-ratio rule is in section 2; it does not bear on the outcome.
- **B5 (ABR code point):** resolved. It is stated as an assumption.
- **B6 (last bin counted as a mode):** resolved (cell 59).
- **B7 (N rule for the p-value):** resolved. The main reading now follows the Methods' N < 50. One level has exactly 50 spikes, and no unit's maximum changes.
- **B8 (fig7ab tests come from the claims file):** stands as a note, not a defect.
- **Section C requests:** the analysis-table columns, PSTH, polarity, trial counts, CF variant, ISI histogram and the fig6b counts by population are all now printed. I still could not compare the figures with the paper's.

**What remains that bears on a conclusion:**

- **fig7ab-representative-sampling:** the outcome depends on how the criterion's "none does" is parsed.
  - Under the record's reading (no reading holds for both CF and CLICK), it is not_reproduced. I agree with that reading.
  - If "none does" is checked per subset, CLICK passes the KS test, so the claim would be blocked as methods_underspecified.
  - Cell 75 currently says the outcome does not depend on the choice, which is incorrect. It should name the reading it takes.

Nothing else remaining changes an outcome. I found no place where the claims file misreads the paper.
