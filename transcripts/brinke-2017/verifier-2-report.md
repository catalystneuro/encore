**Round 2 verification: ten Brinke et al. (2017), attempt brinke-2017-01**

## 1. Outcomes and assumptions

The claims file has 56 claims, including the link claim `source-data-1-link`. The attempt record has 56 outcomes: 22 reproduced, 21 partially reproduced, 6 not reproduced and 7 blocked. Every claim has exactly one outcome.

**I agree with 55 outcomes as recorded.** All stated measured values match the notebook's printed output.

**fig2n-suppression-ds2: I now agree with partially_reproduced; in round 1 I said not_reproduced.** The full table in cell 77 shows:
- The magnitude is within tolerance under every reading (10.9 to 11.7 Hz).
- Class (a), 0-200 ms, rate (a), data set's CR amplitude: 7 significant negative cells, which is within 8 ± 1, with bootstrap p < 0.002. The slope is −0.603 (the fit with the computed CR amplitude, −0.592, is a clean fit).
- The cell count (14, against 14.4 to 17.6) and the slope (against −1.01 ± 0.2) are out.

So the effect is present, and some of its values are within tolerance. This is how fig6d is judged. The record's note "The verifier would give not_reproduced" is now out of date.

**Assumptions marked `assumed: true`:**
- **fig2d, fig2h, fig2l, fig2p.** The cross-covariance lag estimator is stated in a deviation and in the `ipn.xcorr_lag` docstring. It is a reasonable choice: it matches MATLAB `xcov` 'coeff', and the paper's statistics were done in MATLAB. No outcome rests on it: the re-cut variant gives the same four outcomes (cells 44, 59, 74, 83).
- **cs-pause-cells-have-us-pause.** The 50 ms rebound span is stated and is a plausible reading of "followed by". But it was chosen for this claim only. Under the same span, fig4b's own association fails: 2 of the 6 cells facilitate, Fisher p = 0.62 to 1, latency 98.7 ms (cell 93). So these 6 cells do not behave like the paper's CS-pause group.
  - The outcome needs the assumption only if the expected count of 6 ± 1 must be met.
  - The criterion's text requires only the Fisher test. That test holds under the claims file's own readings (4/4, p = 0.017; 3/3, p = 0.048; cell 148).
  - I accept reproduced, with this caveat.

## 2. Text against the printed outputs

These sentences are not supported by the numbers:

- **Cell 94:** "No reading gives 6 to 8 CS pause cells." Cell 93 shows that 125+50 mean/trough gives 6, and cell 94 itself says so two sentences later. (The record's note is correctly qualified.)
- **Cell 78:** "none of the claims file's readings gives 14 to 17". Class (a), 0-200 ms gives 14 (cell 77). The tolerance is 14.4 to 17.6, so the outcome stands, but the sentence should read "15 to 17".
- **Cell 32 and the record (fig1no):** the facilitation counts are "outside the tolerance of 30 and 30 under every reading". Under (a+), the count without behavior is 27, which is at the tolerance edge (cell 31). The outcome is unchanged.
- **Cell 186 (Summary):** the variants, including the 50 ms rebound, are "none of which decides an outcome alone". This contradicts cell 149 and the record's cs-pause-cells-have-us-pause note: "The outcome rests on the 50 ms rebound span".
- **Cell 186 (Summary):** the cross-covariance "puts no lag at the edge of the +/-100 ms range". Cell 74 shows 1 cell at the edge under class (b). The record's fig2l note ("at most one") is correct.
- **Cells 20 and 186, and the record's fig1ijk note and deviations:** "'Mean Facil Hz' equals reading (b)". Cell 13 shows a correlation (r = 0.9984, median difference −0.16 Hz), not equality. Reading (b) classes 88 cells as facilitating, against 84 from Source data 1's values at 5 Hz.
- **Minor:**
  - Cell 23 and the record give "r = -0.036 to -0.029" for "any reading", but (a+) gives −0.037 (cell 22).
  - Cell 97 and the record give "47 to 52" pause cells under the drop readings, but 130+50 drop/trough gives 56 (cell 96).

The README and the rest of the record's notes agree with the outputs. The summary counts (21/21/6/7 over 55, plus the link claim) match the record.

**My round-1 reasons in the record:** they are my round-1 table reasons, verbatim. Two problems:
- Their cell numbers refer to the round-1 notebook. They no longer point to the right cells (for example, fig1ijk is now cell 19, not 15).
- My own source-data-1-link reason, "Shifting by ±1 gives 0 agreements", was wrong: 9 of 371 cells still agree on trial count when shifted (cell 10). The record's note has this right.

## 3. Round-1 points

**Resolved:**
- **B1 (lag estimator):** the estimator is now an assumption, the round-1 estimator is shown as a variant, and edge and flat counts are printed.
- **B2 (CS-transient readings):** a fixed-reading table (cells 151–152) and a deviation now show that no single reading meets all eight tests.
- **B4 (0-212 ms window):** fig2n was run in full on 0-212 ms (cell 77).
- **B5 (0-200 ms window):** it now runs in every second-dataset claim. The 0-200 bootstrap for fig2f is not run, and this is stated.
- **B6 (docstring):** the `ipn.modulation` docstring is corrected.
- **B7 (mixed-model warnings):** warnings are now tied to each row of the tables.
- **B8 to B11:** all addressed.
- **Section C:** the CR flags, the per-cell values, the US-Cluster codes and the 26 ephysMean recordings are now compared or listed.

**B3 (a+) is partly resolved.** The measured values for fig2a and fig5cd now use the claims file's readings. us-peak-cooccurs-with-facilitation still reports 56, which is the (a+) value. Class (a) gives 72, which is out of 55 ± 5.5.

**What remains that bears on a conclusion:**
1. **cs-pause-cells-have-us-pause** reproduces with the expected count only under this attempt's 50 ms rebound. Under that reading fig4b's association fails. The Summary's statement that no variant decides an outcome contradicts this, and should be corrected.
2. **The CS transient results as a set:** fig4g, fig4s1, fig4h, fig5cd and fig5hi reproduce under drop/mean. cs-pause-cells-have-us-pause reproduces only under the mean readings, and fig4b and fig4c reproduce under no reading. The notebook now discloses this, but anyone reading the per-claim outcomes should take it into account.
3. **The classification criterion behind the paper's 60/23/187 is unknown.** Every count that depends on it (for example 42 against 30 base cells in fig2b) carries the gap. It is recorded as a finding and as a question for the authors.
4. **The CR rule gives 111 recordings with behavior; Source data 1's own flags give 103.** This shifts the behavior-dependent counts (fig1no, fig2b, fig6d, fig6h). With Source data 1's flags, fig6d's count would be 65, within tolerance. It is disclosed and was not re-run, which is right, since the claims file names no such reading.
5. **The claims file omits the 0-212 ms window.** The deposited per-trial facilitation for the second dataset uses that whole interval, but the claims file lists only 0-200 and 12-212 ms. This is reported, not corrected, and has been asked of a reader. With the full run it no longer changes an outcome.
