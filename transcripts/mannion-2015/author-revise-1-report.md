Round 1 is answered. The entry passes `python tools/entry.py all` (0 errors, 746 s), and every number in the conclusions, notes and record matches the new run. Nothing is committed.

**Outcome changes**
- **no-radial-bias-in-patches**: still blocked, but the reason is now `metadata_insufficient` instead of `data_missing`, as the verifier said. The test needs only the 120 screenshots, which are in the data set, plus the monitor calibration, which is not public. The finding about the calibration is now `metadata_insufficient` too.
- No other outcome changed: 1 reproduced (figs2-task-no-condition-difference), 15 blocked.

**Added or corrected**
- **Radial-bias variant** (new section). It runs the test the way the paper's `imstats.py` does, under two assumed calibrations (sRGB and Adobe RGB primaries) at 78.7 pixels per degree, plus sRGB at 78.2. None of the 12 tests reaches p < 0.05 in any of the three runs. Neither do the 4 luminance-only tests. The smallest p is 0.063.
  - The cell prints the lines of `imstats.py` and the experiment's `config.py` that it follows.
  - It shows crops of the patch locations and checks the patch geometry.
  - It checks colour inside the patches: R, G and B differ in more than half the pixels of 118 of 120 patches. This answers point 7, which had counted colour over the whole screen.
  - The Gabor filters, written in numpy, match OpenCV's to rounding. This needed matplotlib and opencv in the requirements, so I relocked.
  - No outcome rests on this variant.
- **Task claim** (points 2 to 4 and the unchecked parts):
  - The notebook now prints the lines of `task.py` at the pinned commit. They confirm the strict inequalities, the bin edges, the p1004 rule and that any key counts as a response.
  - New variant (d) keeps targets that fall exactly on an event onset. No effect gets below p = 0.49.
  - New variant (e) assigns each target to the event in progress. The interaction comes out at p = 0.053, still above 0.05.
  - Targets per participant and condition are printed for every reading (103 to 200).
  - The conclusion now says that under reading (a) the null depends somewhat on the window: 0.6 to 0.9 s gives p = 0.034.
- **Tar listing** (point 6). Every member of the archive is now listed by directory: 280 participant files, 120 stimulus files and one README.txt. So the absence of anatomical and area files now rests on the data, not only the descriptor.
- **Record**: I added the round under `verifications`, `inputs` for the paper's analysis and experiment code and the assumed calibrations, and updated the notes, README, entry description and runtime.

**Not done, and why**
- Point 5 (presses after 300 s piling into the last bin): no change, because variant (c) already covers it. Point 8 (the volume variant's limits): no change, because it is already labelled and no outcome rests on it.
- No question added to `questions/crcns-vim-3.yaml`, since the verifier found no place where the claims file misreads the paper.
- I did not mark any outcome `assumed: true`, because none rests on the assumed calibrations.
