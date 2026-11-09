**Verifier report, round 2: crcns-ret-1-lefebvre-2008-01**

**1. Outcomes**

The claims file and the attempt record list 26 claims: 15 histology claims, 4 blocked Figure 9 claims, and 7 claims tested here.

- **The 19 blocked for data_missing (15 histology, plus fig9a, fig9c, fig9-rod-cone and fig9b):** I agree. Cells 4–5 confirm that every recording is binary white noise.
- **fig9-cell-counts, not_reproduced:** I agree. Cell 24 shows 200 and 122 units, and no control count can reach 128.7.
- **fig9d-rf-size-similar, blocked (methods_underspecified):** I agree. This changed from not_reproduced in round 1. In cell 28, 17 of 18 combinations separate; the exception is reading B, svd, DKW. The criterion gives not_reproduced only when all combinations separate, and "blocked otherwise". The outcome now rests on that one combination, and it flips only because of the 20080702 frame correction. I accept the correction: cell 14's scan peaks at 16.671–16.672 ms in both recordings, which matches the other 22 bar recordings and half the checkerboard frame of the same two retinas.
- **s3-receptive-field-surrounds, reproduced:** I agree with the outcome under the criterion. But nulls meet the rule in 194–198 of 200 mutant and 119–121 of 122 control units (cell 33), so the result shows nothing about surrounds.
- **fig9e-slower-time-course, reproduced:** I agree. In cell 36, 36 of 36 combinations separate with the mutant curve later, none the other way, and DKW separates in every combination.
- **fig9f-lower-firing-rate, reproduced:** I agree. In cell 41, 9 of 9 combinations separate, DKW included.
- **fig9g-threshold-unaltered, not_reproduced:** I agree. In cell 45, 36 of 36 combinations separate with mutant thresholds higher.
- **fig9h-gain-reduced, blocked (methods_underspecified):** I agree. In cell 50 the printed form gives lower mutant gains in 18 of 18 combinations. The continuous form gives 9 overlapping, 4 lower and 5 the other way.

**2. Statements the outputs do not support**

- **README:** "the spike trains of four retinas hold a misplaced last minute". Cell 9 says the segments are "consistent with … but this is not proven". The README states as fact what the notebook calls a hypothesis.
- **README:** "It takes about eight minutes". Cell 53 prints "Run time of the notebook: 4.9 min". This is minor.
- **Cell 55 (Summary):** "The results hold with the 16.6 um recordings alone." This is false for fig9d. In cell 29, with 16.6 µm bars only, the svd DKW bands overlap, while in the main reading A they separate. Cell 31 says so itself.
- **Cell 55 (Summary):** "It changes the outcome of fig9d-rf-size-similar only." The same line appears in the record's response for fig9e: "With the 20080702 frame corrected no combination separates the other way". Neither can be checked in full. The frames-as-deposited variant is shown only under reading A, for two measures per claim (cells 29, 38, 42, 47, 53). Under readings B and C it is shown only for fig9d (cell 28). No outcome I can see changes, but the full 36- and 18-combination tables with the deposited frames are not printed.
- **Cell 54 and the fig9h notes:** "Each continuous-form separation rests on few cells". In cell 51 this holds under reading B and for reading A, frame fit, bootstrap (1 mutant against 6 control cells at 15.6). It does not hold for:
  - reading A, binned fit: at 41.46 the counts are 165/200 against 113/122, so 35 mutant and 9 control cells lie above, with bands of non-zero width;
  - reading C, frame fit: around 21.2 the counts are 16–19 mutant against 23–25 control cells.
  These are separations inside the distributions, not band-edge artefacts. The overall point (DKW overlaps in all 6 continuous-form combinations) still stands.
- **Cell 48 and the fig9g notes:** "stops at the top of its theta grid in 107 of 200 mutant and 39 of 122 control fits", "where only the highest bin of y lies above theta". Cell 46 counts fits at either end of the grid (`ret1.py:357`, `i == 0 or i == len(grid) - 1`); the top and bottom ends are never separated. For mutants the top is plausible (median 1.83, max 1.95). For controls (median −0.02) it is not shown, and the mechanism is not shown either.
- **Cell 26 and the fig9-cell-counts notes:** "No mutant count is inside its tolerance … so the counts miss under any reading". This is true only of the two thresholds shown. A threshold between 1.5 and 2 would put the mutant count, which runs from 138 down to 103, inside 103.5–126.5. The conclusion still holds because of the control count; the sentence should say so.

Everything else in the conclusions, the Summary and the record's notes matches the printed numbers. That includes cell 22's null rates (26–43%, 26–45%, 0 of 1600), cell 15's drift arithmetic, the medians and KS values, and the fig9h counts by reading (9/4/5).

**My round-1 reasons in the record:** They are stated faithfully, with my numbers and my B-labels. Two small issues:
- The record cites my B-numbers, but B1–B9 are not defined anywhere in the record.
- The fig9d reason absorbs my B4, which I had marked as not affecting a conclusion. That is accurate in content, but it attaches B4 to fig9d.

**3. Round-1 points**

Resolved:
- **B1:** the label-shuffle calibration was added (cell 21), and every conclusion now says whether it holds under DKW.
- **B3 for fig9d:** the outcome is now blocked.
- **B4:** the frame and onset search is executed (cells 14–16) and the correction is applied.
- **B5:** disclosed.
- **B6:** synthetic check in cell 52.
- **B7:** edge counts in cell 46.
- **B8:** disclosed.
- **B9:** unchanged; there was nothing to fix.
- **All the section C requests:** per-retina table (cell 25), edge counts, separating points (cells 37, 51), the alignment search, and example STAs (cell 30).

Remaining, bearing on a conclusion:
1. **Unit selection, my B2/B3 extended beyond fig9d.** With only units whose STA peak ratio is above 2 (103 mutant, 107 control, closest to the paper's counts), several outcomes would change:
   - fig9f: the DKW bands overlap (cell 42), so it would be blocked, not reproduced.
   - fig9g: frame/continuous DKW overlaps and binned/printed DKW overlaps (cell 47), so it would be blocked, not not_reproduced.
   - fig9h: both frame-fit forms overlap under all three bands (cell 53), so it would be not_reproduced if the binned fits agree; they are not shown.
   - fig9e alone is robust.
   So the fig9f, fig9g and fig9h outcomes depend on including the weak-STA units. The claims file does not settle which units to use outside fig9-cell-counts. The record's notes disclose the subset results but do not say the outcomes are conditional on this choice.
2. **Group definition (B2).** The data cannot settle it: the control labels differ from the paper's and there is no Pax6-Cre region. This is disclosed.
3. **fig9d's blocked outcome rests on one borderline combination** (reading B, svd, DKW) that depends on the frame correction. I accept the correction, but the record should present the outcome as that narrow.
4. **Two flaws in the claims file's criteria, not the analysis, both disclosed:**
   - "Overlap under every band" fails for about 35% of samples drawn from one distribution under the pointwise bands, a flaw that affects fig9d and fig9g.
   - The surround rule is met by noise (s3).

Not bearing on a conclusion: the binned/printed comparison without edge fits (cell 46) removes most of the high-θ mutant fits (107 of 200) by construction. Its overlap therefore says nothing about whether the threshold is unaltered, and it should not be cited as support.
