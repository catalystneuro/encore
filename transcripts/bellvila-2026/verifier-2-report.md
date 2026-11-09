**Round 2 verifier report: DANDI:001678, Bell Vila et al. (2026)**

**1. Outcomes**

The claims file has 45 claims and the attempt record has 45 outcomes, one per claim. One claim is reproduced and 44 are blocked.

- **efield-20min-median, reproduced (`assumed: true`): I agree.** Cell 21 prints these values per 2×2 cell under the row-by-row layout: (a) 1.834 and (b) 1.525. Both are within 1.44–1.86. Reading (b) passes under all three pairings and both layouts. Reading (ii) gives 3.698 and is outside the range.
  - The assumption is stated in the first deviation. It is the 4×4 channel layout, row by row.
  - The assumption is reasonable. In cell 20, the share of random layouts as smooth as row-by-row is between 0 and 0.0135 per rat. Serpentine, a transpose or a mirror of the layout would all give the same outcome.
  - One addition: the "smoothest 5%" of random layouts still have a roughness score of at least 22.4, against 13 for row-by-row and 13.8 for serpentine. Their 29% and 65% figures therefore describe layouts much rougher than any row-structured one, and understate the support for the outcome.
- **efield-1min-medians, units-1min, the 25 dependent 1-minute claims, and the two sham claims (blocked, data_missing): I agree.** Cells 3 and 5 support this: the only channel in the 1-minute files is "S1r 1", and it is the stimulation command.
- **The three fem claims (blocked, data_missing): I agree that they are blocked.** The record keeps data_missing, citing the protocol's rule for an outside input that is not public, and records my label of "other". I accept that. The corrected reason for fem-depth-falloff is right.
- **units-20min, the three 20-minute percentage and magnitude claims, and the eight power and PAC claims (blocked, too_large): I agree with the outcome, but not with the reason as written.**
  - Cell 15 prints an estimate of **68 min** against the 60-minute limit, and the notebook had already run 11 min before that cell.
  - The block therefore still holds on the printed numbers. The margin is small, and the machine-to-machine spread the author reports (52 to 126 min) is larger than that margin.
  - The author's argument that the count is pooled over 13 rats, so one rat or a subset cannot test it, is reasonable.

**2. Statements the printed outputs do not support**

Cell 15 of the re-executed notebook prints:
- "streamed, filtered and cleaned in 72 s"
- "27 units in 243 s"
- "Time per minute of recording: 6.4 s"
- "Estimated time … 13 rats: 68 min"
- "27 of 27" units passing the 0.25 Hz rule

The following text contradicts those numbers:

- **Cell 16:** "took 65 s to stream, filter and clean and 391 s to sort, 9.2 s per minute … take 98 minutes", "The sorter finds 26 units … all 26 pass". The output shows 72 s, 243 s, 6.4 s, 68 min and 27 units.
- **Summary (cell 25):** "sorting the 13 rats takes about 98 min at the speed measured on one full rat". The output shows 68 min.
- **README:** "loading and sorting the 13 rats takes about 98 minutes at the speed measured on one full rat". The output shows 68 min.
- **Attempt record, units-20min notes:** "65 s and SpyKING CIRCUS 2 … 391 s, 9.2 s per minute", "about 98 minutes", "Two runs made while preparing gave 98 and 100 minutes", "gives 26 units". The output shows 72 s, 243 s, 6.4 s, 68 min and 27 units. The record states the preparing runs as if they were the result, while the notebook it cites shows 68.
- **Attempt record, notes on baseline-fr, baseline-ppc, 20min-during-percentages, 20min-post-percentages and 20min-magnitudes:** "about 98 minutes". The output shows 68 min.
- **Attempt record, data_missing finding:** "about 7.5 minutes per rat here, about 98 minutes for the 13". The output works out to about 5.2 min per rat and 68 min in total.
- **Attempt record, round-1 responses for units-20min and the three 20-minute claims:** "65 s to load and 391 s to sort, 9.2 s per minute, about 98 minutes". Same contradiction.
- **Cell 9, a minor point outside the requested sections:** "the 60 Hz line stands 10 to several hundred times above its neighbours". Cell 8 prints ratios from 1.000 to 1099, and five rats are below 10 (1.000, 1.041, 2.945, 5.81, 9.61). The attempt record's finding that the stream is "not notch-filtered at 60 Hz" is therefore unsupported for at least sub-2023-05-04 and sub-2023-05-05.

The following could not be checked against any printed output: the spikeinterface version (0.103.0), the SpyKING CIRCUS 1/MPI statement, and the "52 to 126 minutes" history.

Everything else matches the outputs of cells 20–23:
- the Result cell (cell 24)
- the efield-20min-median rows of the Summary
- the efield notes and deviations in the attempt record
- the methods_unavailable finding

That includes 1.834, 1.525, 1.890, 1.648, 1.748, 1.650, 3.698, 1.848 and 1.589; 18%, 43%, 29% and 65%; "10 of 13"; "at most 1.35%"; 1.310–1.777 with half-width 0.234; 0.313 and 0.522; 0.810–3.052 with SD 0.730; 14 of 208 channels in 4 rats, the first row in two rats; 1.834 and 1.695; 310, 2406 and 810; and a band effect under 1%.

The README's claim counts (1, 1+3, 26, 4, 8, 2) add up to 45 and match the record.

The attempt record's `verifications` reasons give my round-1 points accurately and in substance. The efield reason leaves out my synthetic checks of `fields` and `grubbs` and the unit handling, but those points did not bear on the outcome.

**3. Round-1 points**

Resolved:
- **Point 2 (layout):** the maker's map was searched for and is not published, and the random-layout results are now reported. The outcome remains conditional on the layout, as stated.
- **Point 3:** the 20-minute parts of baseline-fr and baseline-ppc are now filed with units-20min.
- **Point 4:** the conflict is forwarded to a reader. The claim and the claims file are unchanged, which is correct.
- **Point 5:** a per-electrode variant using all 16 electrodes was added.
- **Point 6:** the fem-depth-falloff reason is corrected.
- **Point 7:** the subject and trial discrepancies are recorded as findings.
- **Point 8:** the unstable channels are named, and the sensitivity of the field without them (1.695) is shown.
- **Section C:** the bootstrap intervals, the per-minute artifact and the onset checks are now printed.

Partly resolved: **point 1 (the too_large reason).** The extrapolation was replaced by a timed sort of one full rat, as I asked. What remains, bearing on the reason given for the 13 blocked 20-minute claims:
- Every prose statement of the timing (cell 16, the Summary, the README, and the attempt record's notes, findings and responses) gives 98 min, 9.2 s/min, 65 s + 391 s and 26 units. The re-executed notebook prints 68 min, 6.4 s/min, 72 s + 243 s and 27 units. These must be brought into line with the outputs.
- With 68 min the block still holds (68 > 60, plus the 11 min already run). The reason should say it is narrow and depends on the machine.
