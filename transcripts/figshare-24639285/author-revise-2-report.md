No outcome changed. All 17 stay as the verifier agreed in round 2, and nothing is under `proposed`. The re-run with `python tools/entry.py all` passes with 0 errors (notebook runs in 42 s).

**Supplementary Figure 1.** This was the verifier's main open point on table2-fit-statistics. I read the deposit's `SupplFig1 - other Thelliers March 2024.pdf` from its vector drawing, using a new `apollo.suppfig1_points` (adds `pymupdf` to the requirements), and compared the plotted points with each way of combining the repeated rows.
- For 12 of the 14 plotted specimens that are not synthetic sheets, the points match to within 0.1% (median). TRM gained comes from the mean vectors and NRM is the mean of the rows' moments. ss27 and ss34 match no way of combining the rows.
- 11 of the 12 plotted pTRM checks are measured against the field-off step before them, which is reference (i).
- The figure marks no fitted step range for ss9 or ss10, so the verifier's question about those two is not answered.
- The figure plots ss6's averaged 250 C step, so the authors' own fit used that averaged value. This answers the objection to counting ss6's R2.
- Rescored with the figure's NRM, 24 of 29 values match (83%) when any of the claims file's readings may count. With the pTRM reference the figure actually uses, it is 23 of 29 (79%), the same as before. I kept partially reproduced, because the 80% bar is crossed only by also counting a pTRM reference the same figure contradicts. This is a judgment call, written in the notes.
- New finding: the figure's points for the four synthetic sheets (g2, ss8, ss39, ss48) differ from every way of combining their deposited rows by 0.5% or more (median). So those rows are not the values that were plotted.

**Corrections and added outputs:**
- **MAD wording:** the overstated "to the printed digit" now reads "within 0.3 deg", in the result cell and in the deviation.
- **fig2-changing-field:** the no-changing-field rates now cover 3 vectors (ss41's range) as well as 4 and 5. The wrong "near ss41 and ss22" is replaced with the new numbers.
- **table2-no-fit:**
  - Each specimen's largest fall is now printed against its median standard error. Counting ss29's 0.6% fall as regular gives 10 of 11.
  - The text now says the trend out of the origin rests partly on ss39, a synthetic sheet.
- **no-alteration-recording-efficiency:**
  - Rewritten with the verifier's correction: the replicate scatter is below 8e-11 emu, and 14053g1's excess is 6 to 8 times its standard deviation.
  - The 590.0 moments are now said to be "1.3 to 7.5 times" the threshold, replacing "several times".
- **Table 1 M590 (problem 4):** added a paper_inconsistency finding and question (6) for the authors.
- **README:** removed "It runs in under a minute", since no output prints a run time.
- **Record:** round 2 is now under `verifications`.

**Not done:**
- The paper's Figures 1 to 3 are neither in `paper/` nor in the deposit, so the nominal paleointensities and the step ranges marked with arrows remain unchecked.
- No question for a reader was added; the verifier reported no new misreading of the paper in the claims file.
- Untracked dotfiles (`.bashrc`, `.profile` and others) appeared in the repo root during the session. I did not touch them, and they should not be committed.
