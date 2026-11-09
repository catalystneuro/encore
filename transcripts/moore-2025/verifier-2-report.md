## Round 2 verification: Moore et al. (2025) on DANDI:001699 0.260917.2322

The attempt record holds 27 outcomes, one per claim in the claims file: 14 reproduced, 8 partially reproduced, 4 not reproduced and 1 blocked. I agree with all 27. One sentence in the record is out of date (the first finding), and two other statements need care. Cell indices below are those of the re-executed notebook, which are numbered differently from round 1.

I could not get the paper text this round. bioRxiv refused the downloads with rate-limit errors (1015 and 429), so `paper/` holds only the bioRxiv list of versions (`paper/details.json`). The version-2 numbers quoted in the notes are therefore unchecked. These are, for example, unit-counts' "372 in 6 adult Fmr1-/y and 406 in 6 adult WT", fig1j's t(10) = 3.17, and the "Version 2 reports" r values.

### 1. Stated outcomes

I agree with each of the 27 outcomes. Notes where agreement is narrow or my earlier view changed:

- **fig1g, partially reproduced:** I agree under the rule now applied (one value within tolerance). The margin is 0.005: WT r = 0.8151 against a bound of 0.81 (cell 43). With the first day of each rat alone, WT r is 0.739.
- **fig2d, not reproduced:** I agree. The main test gives p = 0.0556 (cell 55), and every variant that keeps the rat is above 0.05.
- **fig2h, reproduced:** I agree under the criterion, with p = 0.0451 (cell 59). It is at the threshold. The first day alone gives 0.158, the archive's labels 0.253, H3026 left out 0.095 and rat means 0.079.
- **fig1j, not reproduced:** I agree, p = 0.0845 (cell 49).
- **fig3g and figs2j, not reproduced:** I agree; neither value is within tolerance (cells 65 and 74).
- **figs1d, blocked:** I agree. However, my round-1 reason was wrong in part. Cell 6 shows histology images in all 36 files, including the four whose names lack `+image`. Images exist for every rat; none of them marks the tract or PoSub.

### 2. Sentences the printed numbers do not support

- **Attempt record, `findings[0]`:** "With the archive's labels … the juvenile effects weaken (HD information p = 0.24, offsets p = 0.080)." These are my round-1 values. The re-executed notebook gives p = 0.2311 for HD information (cell 40) and p = 0.1690 for offsets (cell 46). They should read 0.23 and 0.17.
- **Cell 50 and the fig1j notes:** "H3001 200201 is decoded on 279 bins … as the rat moved faster than 2 cm/s in few bins of the second half." No output prints the speed behind this. It is hard to square with cell 34, where H3001 is inactive (below 1 cm/s) only 0.358 of the time and has a mean active speed of 4.8 cm/s. It also does not explain the change from 22 bins to 279. This does not bear on the outcome: dropping recordings under 300 bins gives the same p = 0.0854.
- **Summary (cell 82), "How the analysis differs from the paper's", and the verification `reviewed` text:** cutting every session to 20 min is presented as following the paper. It also departs from the claims file, which defines sessions as tracking blocks with only those over 30 min cut to 1300 s. The attempt records this as a deviation only under figs1j and figs2j. No variant under the claims file's own definition is shown, even though the change was made after round 1 and moved fig1g and fig2h.

Everything else checks against the outputs. That covers the other "**Result:**" cells (29 to 81), the Summary's statements about which juvenile results lose significance and under which variants, the entry README's outcome rows and tallies (including "1 reproduced, 5 partially reproduced, 2 not reproduced" for the correlation claims), and the attempt record's other notes. The record's `reason` fields reproduce my round-1 reasons word for word, and "24 of 27 agree" matches the `agrees` flags (false for fig1g, fig3g and figs2j).

### 3. Round-1 points

**Resolved**
- **Problem 4 (spike counting):** fixed. Cell 18 has a synthetic test with 0 wrong frames out of 16,746.
- **Problem 5 (session length):** made consistent at 20 min, but see the deviation from the claims file above.
- **Problem 6 (Isomap subsampling):** Isomap is now fitted on every bin, as the criterion says (`ISOMAP_FIT_MAX = None`), and the effect of the 3000-bin fit is measured in cell 56.
- **Problem 9 (ages):** the asset ages are printed in cell 4.
- **My unanswered questions:**
  - Spearman r, first-day r and scatter plots are now shown.
  - The y = 0 question is answered: one frame per file, an offset (cell 14).
  - The adult Isomap maximum no longer repeats across genotypes (2.639 and 2.417).
  - The REM-inside-exploration variants are shown.
- **Problem 7 (drift interpolation):** reported as fixed. I did not re-test it.
- **Problem 3 (short drift recording):** the recording now has 279 bins; the stated cause is not shown. It does not bear on a conclusion.

**Remaining, and bearing on a conclusion**
1. **H3026's relabelling (problem 1).** This is unchanged, since the files cannot settle it, but it is now quantified. fig1ef (HD information), fig1h and fig2h are all above 0.05 both with H3026 left out (0.072, 0.068, 0.095) and with the archive's labels (0.23, 0.17, 0.25). With H3026 left out, fig1g's Fmr1-/y r rises to 0.869, inside tolerance.
2. **Cells counted on every day (problem 2).** fig2h with the first day alone gives p = 0.158, and fig1g's WT r with the first day alone is 0.739, below its bound. Both outcomes depend on counting cells re-recorded on later days.
3. **Untuned cells in the offsets (problem 8).** This now bears on a conclusion. For fig1h, the variant restricted to cells with half-width below 120° gives p = 0.060, against 0.016 in round 1. The reproduced outcome no longer survives restriction to tuned cells.
4. **Analysis changes made after round 1.** The new session definition, spike counting and full Isomap fit together moved fig1g from not reproduced to partially reproduced (by a 0.005 margin) and fig2h from not reproduced to reproduced (p = 0.045). The full Isomap fit is what the criterion prescribes. The 20 min cut is not, and its effect on its own is not shown.
