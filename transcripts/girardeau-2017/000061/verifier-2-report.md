**Verifier report: Girardeau et al. 2017 (nn.4637) on DANDI 000061 @ 0.250624.0426, round 2**

Counts come from the claims file and the attempt record. There are 32 claims: 6 reproduced, 1 partially reproduced, 3 not reproduced and 22 blocked (17 metadata_insufficient, 5 too_large).

### 1. Stated outcomes

I agree with all 32 outcomes in the attempt record.

- **Tested claims.** `unit-counts`, `habituation-over-days`, `bla-pyr-sleep-firing-increase`, `bla-int-sleep-firing`, `reactivation-all-cell-pairs`, `cen-no-reactivation`, `ripple-modulated-cells-larger-reactivation`, `reactivation-peaks-at-ripples`, `direction-all-cell-pairs` and `ripple-rate-unchanged` each follow from the printed outputs (cells 30, 34, 38, 41, 46, 53, 64, 68, 70, 76) under the claims-file criteria as now worded.
- **`bla-rate-same-across-directions`.** I agree with "blocked", and with the new `blocked_by: too_large` in place of my "other". O7 reading (b) needs position, which only video tracking would give. That is the same reason the behaviour claims are too_large.
- **The 17 metadata_insufficient blocks** are correct. No file has 6 identified excitatory hippocampal units (cell 5: at most 4).

I found no place where the claims file misreads the paper.

### 2. Sentences the numbers do not support

**Not supported:**
- **README, line 44:** "about 216 hours to stream at the rate measured in the final run". Cell 13 prints "Streaming 20 frames … 7.0 s" and "about 186 hours".
- **Attempt record, `rats-learn-puff-location` notes:** "streaming 20 frames took 8.1 s in the final run, about 216 hours". Cell 13 prints 7.0 s and 186 h. The outcome does not change.
- **README, line 47:** "It takes about 10 minutes (10.0 in the final run), six of them streaming". Cell 77 prints "Notebook run time: 7.2 min", and cell 1 prints that loading took 302 s, about 5 min.
- **Cell 43:** "Its effect size r is 0.39 against the paper's 0.09, so these cells differ from the paper's in REM, not only in number." No test compares the two samples. A significant result here next to a non-significant one in the paper does not show the samples differ. Cell 42's bootstrap interval of the REM median (−0.015 to 0.109) includes zero.

**Minor:**
- **Summary, `ripple-rate-unchanged` row:** "excludes changes above about 11%". 11% is the change detected with 80% power (cell 77), not an exclusion bound. The bootstrap interval in cell 77 is −1.4% to 8.4%. Cell 78's "about a tenth of the rate" is closer.
- **Cells 31 and 48:** each "**Result:" paragraph ends with a stray `**`. This is formatting only.

Every other sentence in the "**Result:" cells (31, 32, 36, 39, 43, 44, 48, 51, 55, 59, 62, 65, 66, 69, 71, 74, 78), the Summary (cell 79), the rest of the README and the attempt-record notes and findings matches the printed outputs. That includes all counts, p values, per-rat splits, excluded units, lap tables and power or interval figures.

**My round-1 reasons in the record.** They are stated faithfully, in my own words. Points from my Problems and "could not check" sections are folded into the matching claims, and the remaining points are in `reviewed`. One small attribution: the record adds my platform-time point (Problem 3) to `habituation-over-days`. In round 1 I raised it about the air puff and safe templates (cells 51/52), not about habituation. It is harmless, because the lap counts are unaffected.

### 3. Status of round-1 points

**Resolved:**
1. **`bla-rate-same-across-directions` rule misread.** Fixed in cells 72 and 74, the Summary, the README and the notes.
2. **No power or effect-size context for the absence claims.** Fixed in cells 42, 54 and 77. The conclusions and notes now call the central nuclei result weak evidence.
3. **Platform time inside O1(c) laps not flagged.** Now flagged in cells 33, 67, 71 and 72 and in the deviations. A lap table and a variant without Rat08-20130708 were added; the variant gives the same result.
4. **Cell-type labels unverified beyond firing rate.** The new cross-correlogram check (cells 7 and 8) supports the reading: 99.3% of excitatory units excite another unit and 94.4% of inhibitory units inhibit one, at p < 1e-6.
5. **ElectricalSeries disagreement.** The group listing of every file (cell 15) shows the asset metadata is wrong, not the loader. It is recorded as a new finding.
6. **Rat mapping.** Recorded as an assumption.
7. **M3 rule not implemented.** The helper docstring now explains why it cannot change any bin used.
- **"Could not check" items.** All four are now shown: the file groups (cell 15), the cross-correlogram check (cell 7), the per-rat and left-out-unit tables (cell 68), and the BLA-only variant (cell 58).

**Remaining points that bear on a conclusion:**
- **`direction-all-cell-pairs`.** The templates still include platform time and stops. Early Rat08 air puff laps have median durations up to 998 s (Rat08-20130708; 660 s in Rat08-20130711), against a median lap of 22.6 s overall (cell 70). The robustness variant removes only Rat08-20130708, so it does not address the other long-lap sessions. The air puff result rests mostly on Rat08: 7 of 8 sessions, against 1 of 3 for Rat11.
- **`bla-rate-same-across-directions` commentary.** The runnable readings that "find a difference" (median 0.0036 and 0.0032 Hz, cell 73) use the same reward-to-reward laps. So that difference may come from platform time rather than the trajectory. The outcome stays blocked either way, but the README and notes present it as the direction of "not reproduced" without this caveat.
- **`bla-int-sleep-firing`.** The cell 43 sentence quoted above draws a conclusion the data do not test.
- **Absence claims.** `cen-no-reactivation` (9 and 8 sessions) and `ripple-rate-unchanged` (23 sessions) stay "reproduced" only on the paper's p threshold. The notebook now says so. The central nuclei NREM interval (−2.4 to 4.1%) includes the hippocampus–BLA median of 1.96%.
