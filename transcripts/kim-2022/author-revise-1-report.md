I've revised the entry for every point in the verifier's round-1 report. The entry re-ran cleanly with `python tools/entry.py all entries/000489-kim-2022`: 0 check errors, notebook passes in 10.7 min. I compared the printed numbers against a development run, and every number the conclusions cite matches. Nothing is committed.

**Outcome changes**
- **fig2b-exponential-same-slope:** blocked (`methods_underspecified`) → `not_reproduced`, marked assumed. The verifier was right: I had labelled one case "partially reproduced", a category the criterion doesn't define. Applied as written, all 12 readings fail: in 10 a slope differs, and in the other 2 the exponential beats a straight line for only 3 of 5 amplitudes. It is marked assumed because some data variants (top side only, scale set from the electrodes, right footprint only) have readings that pass.
- **fig2c-weaker-at-6-7:** `not_reproduced` → blocked (`other`). At 6.75 kV/cm the unipolar mean is −8.6 a.u. (s.e.m. 19.6), at background, so the percent of unipolar there measures nothing. The code now flags a unipolar mean that is not more than twice its s.e.m. above zero. With the bottom side alone or the left footprint alone it passes that check and gives reproduced, which the notes say. A blocked outcome can't carry `assumed` under the schema, so the notes say the block rests on the main reading.
- **The 15 claims on Figs. 3–7:** still blocked, but now `other` and no longer `data_missing`, since the data are public. The notebook lists 000548, 000549, 000550 and 000448, and each claim's notes name its dandiset and what it holds. They are not tested here: each is a separate registry target, and the claims file doesn't name them as a source for 000489.
- **Unchanged:** fig2a (partially reproduced), the vertical scales, fig2c-max and fig2c-flat (not reproduced), and fig1e (`data_missing`).

**Added or corrected**
- **Dish 0-03:** 000548's `sub-Fig3-Uni5-03` has the same MemBrite channel as 000489's 0-03 and a YP channel that registers with it (phase-correlation peak 0.301), so it holds the missing unipolar image. The other 5-pulse files of 000548 are 2640 bytes larger than the 000489 file for the same dish. This is now a finding.
- **fig2c-max:** prints a p-value table for every ROI and runs two more readings, at both named fields and at one ROI or more. Only the last passes: one of 36 tests, 50% against unipolar at 15.24 kV/cm, p 0.0018. The outcome now assumes the test applies over the whole field range, and says so.
- **Variants:**
  - Removed the "with sub-Fig2-0-03" variant, which the verifier showed was not valid.
  - Added a variant with the model field scaled to the paper's 15.1 kV/cm at the centre (the verifier's point about 15.1 kV/cm and the centre ROI).
  - Added tests of fig2a with the weakest ROI at 2.0 and 2.4 mm.
  - Added per-dish unipolar values around 6.7 kV/cm under every variant.
- **Fig. 7 data:** the notebook reads every 000448 session description: 5 unipolar and 4 bipolar cells, each recorded forward and reverse.
- **Assumptions stated:** why both sides of bb' are averaged, and how far the ROI extend (now in `bipolar.py`).
- **Record and text:** the round is recorded under `verifications`, with the verifier's reasons and my responses. Notes, findings, the README and the notebook summary match the new numbers.

**Not done**
- **Using the 000548 image of dish 0-03:** I didn't add it to the analysis or as a variant. It is outside this dandiset, and the automatic footprint finder takes a cell-free patch for the right electrode in it (3.81 mm apart, 0.71 mm across). A version that searched only near the nominal electrode distance shifted the verified footprints of six 000489 dishes and still missed this one, so I reverted it. Unipolar stays at 2 dishes.
- **Reader questions:** none added. The verifier reported no place where the claims file misreads the paper.
- **Image units:** nothing in the files says whether the images were rescaled, so the vertical-scales claim still rests on that assumption.
