# Verification report: SHIELD (Bennett et al. 2024) on DANDI:001051 v0.260922.1827, round 2

**Summary of my review:** the claims file has 46 claims and the attempt record gives an outcome for all 46. The record's outcomes are 15 reproduced, 6 partially reproduced, 5 not reproduced and 20 blocked (11 data_missing, 4 metadata_insufficient, 5 methods_underspecified). Only `fig8d-response-latencies` is marked `assumed: true`.

I agree with 44 of the 46 outcomes. I disagree with two, fig7cd-mop-coupling and fig8d-response-latencies, and would block both as methods_underspecified. My outcomes are therefore 13 reproduced, 6 partially reproduced, 5 not reproduced and 22 blocked. Cell numbers below are 0-based indices in the re-executed notebook.

## 1. Outcomes and assumptions

**Agreed (44).** These include the two outcomes the author changed after round 1:
- **fig8d-cp-rf-larger-response**, now partially reproduced. With the Methods' QC filter the unit counts are 70, 162 and 218; the code's filter gives 79, 206 and 239.
- **link-code-tables**, still partially reproduced. The 33 of 79 sessions where more than 1% of units differ in RF significance are explained by two bootstraps disagreeing at the threshold: all 83 differing units have p of 0.003 to 0.020 in both computations (cell 14).

**Disagreed (2):**
- **fig7cd-mop-coupling: the record says reproduced; I would block it as methods_underspecified.**
  - The criterion's "reproduced" condition needs MOp–PO to be significant.
  - Cell 78 prints `coherence_part False` in all 8 E1 combinations, because PO is `absent` there. VISl is also untested in all L1 combinations and under L2 E1.
  - All four parts are tested only under L2 E2, which is 4 of the 16 combinations.
  - The claims file's rule is that every alpha claim is judged under each combination of readings, and the claim is methods_underspecified when they disagree. Here the E1 readings do not reproduce the claim, so they disagree with E2.
  - "No tested part contradicts" is true, but the criterion does not use that test. The record does state my disagreement.
- **fig8d-response-latencies: the record says reproduced on an assumption; I would block it as methods_underspecified.**
  - The assumption (half-peak latency) is stated, but it is weakly grounded.
  - The paper says only that the "response time course … lagged" and that CP-noRF had "slower responses". That wording does not pick an onset measure over a peak measure.
  - The claims file offers both readings without preferring either. The half-peak reading was adopted after it turned out to be the one that matches: peak lags are 34 and 9 ms, half-peak lags 16 and 20 ms (cell 99).

**Other window and reading choices.** The figs4i fit window is now stated as an assumption. The outcome does not rest on it: no window from 30 to 77 minutes brings tau into the 22.5 to 33 min range (cell 56). The figs4i, fig7a and fig7b readings are all applied as the claims file allows.

**Claims-file problems to report, not correct:**
- **fig7e.** The signed-rank test of the median lag reads the paper too strongly. This is now with a reader.
- **fig8d-cp-rf-larger-response.** The expected counts (80, 205, 239) are the code-filter numbers, but the criterion prescribes the Methods' QC units. The claim is internally inconsistent.

## 2. Sentences the printed numbers do not support

**Clock alignment, cell 66 and the fig7b note:** "The pupil and running clocks are checked … (alignment shown in all but 8 sessions)."
- Cell 10 lists 5 sessions with a weak running contrast and 3 with a weak pupil contrast.
- It also lists 2 sessions with no running contrast (1173189336, 1230732154) and 2 with no eye tracking.
- That makes 12 distinct sessions where at least one stream's alignment is not shown, not 8.
- The record's fig7b note and its finding both leave out the 2 sessions without a running contrast.

**KS p values, cell 69 and the fig7b-visp-offset-locked note:** "KS p 1.7e-233 or less". Cell 68's largest VISp KS p is 9.15e-233 (L1 E2 a). This does not change the conclusion.

**The 328 code units, cell 15, the link note, Summary finding (1) and the record's finding:** "328 units on probes the dandiset lacks / does not hold". Cell 13 shows only that 328 code units are not in the dandiset, by structure. No cell shows which probes they are on.

**Cell 15:** "(5.4 to 11.8, against 0 in the other 81 sessions)". Cell 13 prints only the median for the other 81 sessions (0.0000), not their maximum.

**fig4d-unit-drift deviation:** "202 more non-noise units … from the 40 probe recordings the paper's tables leave out." No output attributes the 202 units to those probes. The quality labels also differ for 14–38% of units in the 6 mismatched sessions, which would change the non-noise count as well.

**fig4ef deviation:** "r = 0.9989". Cell 14 prints 0.9990, which the link note also uses.

**Cell 91 and the fig7-hippocampus note:** "CA1, CA3, ProS, SUB or POST also under R2". ProS is significant under L1 E2 R1 and SUB under L2 E2 R1 (cell 90), so these regions are not significant only under R2.

**Cell 85 and the fig7f-visp note:** "significant … in 22 of 32 combinations". The 32 are 16 combinations × 2 subdivision modes, not 32 combinations. The 14 of 16 and 8 of 16 that follow are correct.

**Everything else matches.** I checked every other "**Result:**" sentence, the Summary and the README against the printed outputs, and the remaining record notes agree with them. The README counts (10 reproduced Figure 4 claims, 16 blocked claims) agree with the record.

**My round-1 reasons in the record.** The verification block states my round-1 reasons faithfully, mostly in my own words, with each problem attached to the right claim. Problems 5 (unsmoothed rate) and 11 (docstring) did not affect any conclusion and appear in no claim's reason. Both are fixed: problem 5 is now a stated deviation, and the shield.py docstring now describes the bootstrap. "43 of 46 agree" is right.

## 3. Round-1 points

**Resolved:**
- **Problem 1 (figs6 replay).** A run keeping only post-offset events gives r = 0.19 to 0.53, still not reproduced. Events after omitted flashes drop out.
- **Problem 2 (fig7a).** The zero-padded spectrum gives MOp 4.64 to 4.74 Hz, inside the range in all 8 combinations, so the outcome does not rest on the 0.5 Hz grid.
- **Problem 3 (figs4i).** The window is stated as an assumption, and fits over other windows are shown.
- **Problem 4 (link-code-tables).** RF agreement is now shown per session.
- **Problem 5 (unsmoothed rate).** It is stated as a deviation.
- **Problem 6 (BH family).** It now holds brain areas only. This changes 4 of 734 pair results and no outcome.
- **Problem 7 (absent areas, VISl/VISlm).** Absent areas are reported as untested, and the VISl/VISlm merge is stated.
- **Problem 8 (noise CP units).** No CP unit is now without an RF p value.
- **Problems 10 and 11.** The .5-median point is in the notes, and the docstring is fixed.
- **All the "could not check" items:**
  - The clock check is now there, at about 100 ms resolution, which is adequate for the 0–1 s pupil windows.
  - The area lists are printed.
  - The S4I windows are shown.
  - The post-offset replay run is done.
  - The `inserted` column shows all probes marked inserted, so it records no failed attempts.
  - The re-sort question is answered: the files' spikes match the files' metrics.

**Remaining, bearing on a conclusion:**
1. **fig7cd-mop-coupling** should be blocked (methods_underspecified), not reproduced (section 1).
2. **fig8d-response-latencies** should be blocked (methods_underspecified). The half-peak assumption is stated but not grounded in the paper (section 1).
3. **fig7e-lags-straddle-zero** is not reproduced under a criterion that likely misreads the paper. The question is open with a reader; until it is answered, the outcome rests on the claims file's reading.
4. **fig7b-low-arousal.** Clock alignment is not shown in 12 sessions, not 8. This does not change the outcome, since the direction holds and the size misses in every reading, but the text overstates the check.
