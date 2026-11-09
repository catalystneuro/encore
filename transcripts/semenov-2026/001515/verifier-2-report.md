**Verifier report, round 2: 001515-semenov-2026-01**

**1. Outcomes**

The claims file has 34 claims (34 `- id:` entries). The attempt record has 34 outcomes (34 `- claim:` entries): 1 partially_reproduced and 33 blocked (`data_missing`). No outcome is marked `assumed: true`, so there are no assumptions to assess.

- **fig5b-conductivity-calibration, partially_reproduced.** I agree. Cell 19 gives 1.33% (reading a) and 1.20% (reading b) for the 10-fold rise, both outside 2 ± 0.2. It gives 11.87% (a) and 11.75% (b) for the 100-fold rise, both inside 12 ± 1.2. I computed Eq. (2) again myself and got the same values: f = 1.498, 1.4801, 1.322 and 0.6393 for the 1-, 10-, 100- and 1000-fold values. `strobe.f_factor` has not changed. The criterion (claims file, line 625) matches the paper's Results 3.5 ("~2% … 12%"). The claims file does not misread the paper here.
- **The other 33, blocked (`data_missing`).** I agree with all of them. Cell 5 shows every file is FluoVolt with 1-µs pulses and 1.00-mm electrode spacing, in 70-frame series at one amplitude per subject. Cell 6 now prints the full session-description texts: 4 templates of 73 files each. None contains Di-8, ANEPPS, Gd, Fluo-4, calcium, a second pulse, a train, 0.3, 900 ns, 1.6 mm or V/cm. The dependency notes for fig7b (on fig4b-di8-limits) and fig5c (on fig5b) match the claims file's `depends_on` fields.

**2. Sentences against the printed outputs**

Almost everything checks out. I rebuilt several results from the per-file table printed in cell 9, and the notebook's numbers come out exactly:
- the n_cells range of 2/5/12;
- the per-session and per-amplitude medians of |peak| in cell 17;
- the half-peak frames 16–34 and 35–53 in cell 13;
- the 9 files that disagree with their group, and the 35 of 37 subjects whose sign flips (cell 15);
- the two files per order and anode combination in each subject, with one each for CHO-20230925-c1.

The cell 11 figure supports cell 12: the mask covers whole cells, a dim cell at lower left is mostly outside it, and parts 1 and 6 are each two touching cells.

Wording that the numbers do not fully support:
- **Cell 16, "9 files have the sign of the other anode side of their subject".** The same wording is in the attempt record's anode finding. The count is actually files that differ from the majority sign of their own subject and anode side.
  - In CHO-20230925-c6 both sides have a negative majority, so its two positive files do not have "the other side's" sign.
  - The two negative "anode above" files of CHO-20230508-c5 do match the other side, but they are left out because that group's majority is a tie.

  The count of 9 is right for what the code tests; the sentence describes a different test.
- **Cell 14, "In most files frame 0 is about half as bright as the others", and Summary (cell 24), "Frame 0 is about half as bright as the rest in most files".** Cell 13 gives a median ratio of 0.587, with quartiles 0.516 and 0.715. "About 0.6 times" would be accurate; the finding's "median ratio 0.59" is correct.
- **Cell 22, "In the grid … no combination puts both values within tolerance".** The attempt record's fig5b notes say the same. Cell 21 checks only reading (a), and neither sentence says so. I checked reading (b) over the same grid and it also gives 0 combinations, so the conclusion holds.
- **README, "It takes about six minutes".** The printed timings cover only 76 s (cell 1) and 104 s (cell 9). Six minutes is not shown, though nothing contradicts it.

**My round-1 reasons in the record.** The reasons are in my own words, condensed faithfully; the fig5b reason also folds in my code check (round-1 B1). One cell reference is now wrong: the fig5b reason says "In cell 15", but the computation is now in cell 19, and cell 15 is the sign table. The "cell 5" references are still right.

**3. Round-1 points**

Resolved:
- **Per-file table of peak, peak_frame and n_cells (round-1 C).** Added in cell 9. The derived statistics in cells 13–17 now check out against it.
- **Figure of one file's mean image with the mask (round-1 C).** Added in cell 11. It led to the correction that n_cells counts connected parts of the mask, not cells; that change is made in cell 12 and in the finding.
- **Full set of session descriptions (round-1 C).** Printed in cell 6, with the term counts. The dye result no longer rests only on the regex fields.
- **Round-1 B1–B6.** All were "does not affect a conclusion" and all still stand. The grid stays labelled a variant (cells 20–21), and the 50-ns step is still stated as consistent with the data but not shown by it (cell 14).

Open, none bearing on a conclusion:
- I still cannot run the pixel-level helpers myself (no numpy or h5py here). I checked them only for internal consistency against the printed table.
- The sister dandisets 001516–001518 were not examined; the record says so in every blocked outcome's notes.
- Wording fixes:
  - the cell 16 "9 files" sentence and the matching finding;
  - "about half" for frame 0 in cells 14 and 24;
  - say "under reading (a)" for the grid in cell 22 and the fig5b notes;
  - the stale "cell 15" in the fig5b reason.

Nothing that remains bears on a conclusion.
