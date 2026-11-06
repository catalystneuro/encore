**Verifier report, round 2: doi:10.7554/elife.112525 on DANDI:002034 (0.261019.2146)**

The claims file holds 17 claims, and the attempt record gives an outcome for each: 14 reproduced, 1 partially reproduced (figs1-raw-baselines-similar) and 2 not reproduced (range-baseline-lc-evoked-pupil, figs2-llr-cross-epoch). My round-1 header said "13 reproduce, 2 partially". That was a counting error on my part. My own round-1 table lists exactly the 14 / 1 / 2 above.

### 1. Outcomes and assumptions

I agree with all 17 stated outcomes. The re-executed outputs support each one under the claims file's criteria:
- Cell 13: 26 of 26 values match the code's printed output.
- Cell 16: 42/32 and 63/51.
- Cell 19: rows 1–6 under M-E1 and M-E2.
- Cell 28: the cross-epoch rule holds under every reading.
- Cells 31 and 33: the range correlations. Oz row 5 gives −0.04 and −0.13, both non-significant.
- Cell 36: 11 of 12 under M-E1 and M-E2.
- Cells 39, 41 and 43: the LLR counts. M-E1 gives 6/32 and 7/51 for pupil, and 3/42 and 4/63 for LC. For the cross-epoch fits, Oz is 5/42 (0.119) and 6/42, both above a tenth of the units.
- Cells 46 and 49: 8 of 8 within-epoch cells, and 0 of 84 cross-epoch cells.

**No outcome is marked `assumed: true`, yet two assumptions underlie outcomes.** Both are stated only as deviations:
- **Trial start taken as fixation onset.** Every outcome rests on this, and it sets every baseline window in the deciding readings. It is reasonable, because the files hold no fixation marker and the code uses the same anchor. But cell 7 makes it less certain: 39% of spikes are stored before the trial start. It should be flagged.
- **Stored pupil taken as already z-scored per session.** Both fig3 claims rest on this. It is reasonable, and cell 50 shows that z-scoring again changes the coefficients by at most 0.008, which I recomputed from the printed tables.

### 2. Sentences the numbers do not support

- **Cell 52 (Summary):** "The three claims that do not reproduce in full all turn on the evoked pupil: measured from the beep to 20 ms before the end of fixation (Methods) in place of 0 to 800 ms after the beep (code)." The printed outputs contradict this:
  - For figs1, the cell that fails is row 6 in Ci (evoked LC against baseline pupil). It does not use the evoked pupil at all. Cell 36 shows it still fails with "Methods trials + code pupil" (p = 0.136) and with "code trials + E1" (p = 0.131). It passes only under the full code reading (p = 0.023). The difference therefore comes from the trial set, not the pupil window.
  - For range-baseline-lc-evoked-pupil (cell 33) and figs2-llr-cross-epoch (cell 43), neither mixture of the two methods reproduces the paper. Cell 34 says this correctly: the result needs both the code's trial rule and its evoked pupil. The README's wording ("evoked pupil … and which beep trials are kept") is accurate.
- **Cell 14, the attempt record's include-list-link notes, and its second code_mismatch finding:** these say the code's printed Figure 3 values are matched "only when" firing rates are z-scored by within-session unit index. No cell compares against the code's printed Figure 3 values. Cell 13 prints only this attempt's own values under the code's grouping. Nothing in the outputs supports either the match or the "only".
- **Cell 0:** "The draft holds the same 83 assets with the same total size." This is not printed anywhere. It is minor.
- **Attempt record, data-units-sessions notes:** "(7 to 109 beep trials per unit)" is said to hold under both rules. Cell 16 shows a maximum of 111 under the code's rule. It is minor.

I checked every other "**Result:**" sentence (cells 14, 17, 21–26, 29, 32, 34, 37, 40, 42, 44, 48, 51), the README and the record's notes against the outputs, and they are supported. That includes the new numbers for the "200 ms after beep" variant: 0.0085 and 0.011, 0.0022 and 0.0041, 3.7e-7 and 1.9e-11, 0.029 and 0.046, 3/32 and 9/51, 6/42 and 5/63, and 8/42 and 7/63.

**Round-1 reasons in the record:** they state my round-1 reasons faithfully. Each B-point is merged into the relevant claim, mostly in my own words. Two gaps:
- The reasons cite round-1 cell numbers ("Cell 10", "Cell 12", "Cell 14", …), which no longer match the re-executed notebook. Those are now cells 13, 16 and 19, for example.
- The record does not carry my round-1 notes that the synthetic tests found no errors and that I found no misreading in the claims file. These are not claim-level points, so this does not matter much.

### 3. Round-1 points

**Resolved:**
- B2: the pupil z-scored-again variant was added (cell 50).
- B3: cell 7 shows that spikes are mostly not stored past the trial end and counts the affected trials (75 Oz, 96 Ci). A variant without those trials runs through every analysis, and no outcome changes.
- B4: cell 50 shows neither removed unit is in a row 1 group, and the groups formed after the removal give 0 cells.
- B5: medians are now compared unrounded (−0.0375 against −0.037).
- B6: cell 26 and the notes now say the row 6 Ci result is fragile.
- B7: recorded as a code_mismatch finding.
- C2 and C3: done in cells 50 and 43.

**Partly resolved:** B1 and C1. The spike check was added and the deviation is reworded, but what the trial start marks is still unknown.

**Remaining, bearing on a conclusion:**
1. **Wrong attribution in the Summary.** The cell 52 sentence (section 2) gives the wrong reason for figs1, the partially reproduced outcome. It should say the difference comes from the trial set, not the evoked pupil.
2. **Undisclosed reason the code reproduces figs1.** Cells 7, 10 and 36 together imply something the notebook never says. Under the code reading, row 6 in Ci and figs1 depend on the 85 rows (unit × trial) that the code's rule keeps and the Methods' window drops. In those trials the beep falls within about 70 ms of the trial end or after it; 41 Oz and 39 Ci beep trials fall after the end. On those trials the 0–200 ms evoked rate is counted largely over a period with no stored spikes (cells 7–8). So the code's 12 of 12 for figs1, and its Ci row 6 p of 0.0105, may rest on evoked rates that are biased low. This should be stated with the figs1 outcome and the code_mismatch finding.
3. **The unsupported Figure 3 z-scoring claim** (cell 14, record notes, second code_mismatch finding). It should either be shown against the code's printed values or withdrawn.
4. **Assumptions not flagged.** The trial-start and pupil-preprocessing assumptions should be marked `assumed: true` on the outcomes that rest on them.
5. **Unknowable from the archive:** which units and sessions the paper actually used (its 51 Ci sessions against the code's 50, and 63 units against 61). The row 6 Ci outcome is fragile on exactly this point.

I found no misreading of the paper in the claims file.
