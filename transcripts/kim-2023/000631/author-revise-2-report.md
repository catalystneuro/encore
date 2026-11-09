No outcome changed. The round-2 verifier agreed with all 12, and nothing turned up that calls for a `proposed` change. I re-ran the entry with `python tools/entry.py all entries/000631-kim-2023`: 0 check errors, the notebook passes, and the printed numbers are the same as before.

**What I added or corrected:**
- **60-fold ratio (verifier's open point 1):** The notebook (cell 42) now prints the plateau level divided by less selected 180-degree values, on layout L2 with background (b):
  - over the lowest ROI and its two neighbours: 45.7 to 52.6-fold;
  - over the mean of the ROIs above 160 degrees: 36.0 to 39.1-fold.

  Both are outside 60 ± 6, so the criterion is met only at the single lowest ROI. The result cell, the Summary, the README and the notes now say this. They also say the bootstrap correction (0.4 to 0.8 percentage points, giving 56.9) underestimates the bias of a minimum over 32 ROIs and does not settle it. The outcome stays reproduced, with low confidence.
- **Plateau claim (point 2a):** The 833 kHz half of fig2-facilitation-plateau holds only with the 0.5 mm and 0.6 mm footprint disks:
  - lumen alone: levels 3.39 to 13.31-fold, none within 2.7 to 3.3;
  - wall ring alone: the one level in tolerance, 2.79, is reached at 80.2 degrees, outside 81 to 110.

  This is now stated in the plateau result (cell 36), in the Summary (which no longer says the footprint region changes only the 60-fold outcome), in the README and in the claim notes. The label stays partially reproduced under the 0.5 mm disk, which decides.
- **Summary table (point 2b):** fig2-crossover-angle and fig2-frequency-dependence now list only the pixel size as an assumption, since both ROI layouts give the same outcome for them.
- **Stale cell number (point 2c):** I annotated the round-1 reason with the current cell, 25, and left the verifier's original wording in place.
- **Attempt record:** Round 2 is recorded under `verifications`, with the verifier's reasons in its own words and my response for each claim.

**What I did not do:**
- The open point that the 833 kHz paired dishes and controls were imaged on different days is still open. The files hold no exposure or gain settings, so they can't settle it. It was already stated in the notes, the Summary and the findings.
- The verifier found no place where the claims file misreads the paper, so nothing was added to `questions/000631.yaml`.
- I made no commit or push, as instructed.
