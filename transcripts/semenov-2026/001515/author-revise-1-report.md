No outcome changed. The verifier agreed with all 34: `fig5b-conductivity-calibration` stays partially reproduced, and the other 33 stay blocked as `data_missing`. The re-run with `python tools/entry.py all` passed with 0 errors in 337 s. The numbers came out the same: a 10-fold rise gives 1.33% and 1.20% (outside the 2 ± 0.2% tolerance), and a 100-fold rise gives 11.87% and 11.75% (inside 12 ± 1.2%).

**Added to the notebook (the outputs the verifier asked for):**
- **Session descriptions:** all are now printed. The 148 distinct texts reduce to 4 once the subject ID and amplitude are replaced by placeholders, with 73 files each. A term count shows that no session description mentions Di-8-ANEPPS, Gd3+, Fluo-4, calcium, a second pulse, a train, 0.3 µs, 900 ns, 1.6 mm or V/cm. "Sine" appears only in the image-series description, which every file shares.
- **Per-file table:** all 292 files, with `n_cells`, `peak`, `peak_frame` and the half-peak frames.
- **Mask figure:** one file's mean image with the mask overlaid. Two new helpers in `strobe.py`, `read_stack` and `membrane_mask`, now feed both the figure and the existing index.

**Corrected:** the figure shows the top-10% mask covers whole bright cells, interiors included, and two touching cells form one part. So `n_cells` counts connected parts of the mask, not cells. The notebook text and the matching finding in the attempt record now say this. It changes no conclusion, because the index is used only for the data check.

**Also updated:**
- The notebook's runtime in `entry.yaml` and the README went from 4 to 6 minutes, and the README's description of `strobe.py` now mentions the mask.
- Round 1 is recorded under `verifications` in the attempt record. For each claim it gives the verifier's agreement, its outcome, its reason in its own words, and my response.

**Not done:**
- No questions went to `questions/001515.yaml`: the verifier found no place where the claims file misreads the paper.
- I did not try other values for λi, λo or the intact λm, because the criterion fixes them.
- I did not look at the sister dandisets 001516 to 001518, as they are separate targets.
- Untracked dotfiles in the repository root (`.bashrc`, `.idea` and others) were not created by this work, and I left them alone. Nothing was committed, as instructed.
