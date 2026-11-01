I've finished the round-1 revision. No outcome changed, and I recorded the one disagreement. I re-ran the entry with `tools/entry.py all`: it reports 0 errors and all three notebooks pass (the main one in 1,495 s, `elsewhere_001030` in 42 s, `elsewhere_001272` in 85 s). The conclusions match the new outputs.

**Outcomes**
- **Unchanged and agreed by the verifier:** the 6 Figure 4 claims, `figs1-di8-anepps-control` (not reproduced), and the 9 claims on other dandisets (blocked).
- **One disagreement:** `fig3c-sustained-firing-2s` stays `partially_reproduced`; the verifier gave `not_reproduced` "by the letter".
  - I revised the AP detector as the verifier asked. The trace is now smoothed over 1 ms, and a reading (a) peak must stand 5% above its surroundings. The first run's detector is kept as a variant.
  - With the revised detector, c7 meets the whole criterion under both readings. At its highest field (2.3 V) it has no APs after the ramp and a mean dF of 6.66%.
  - c5 and c8 stop firing at their highest field, but their dF stays below the 5% level (3.48% and 3.63%). c6 keeps firing.
  - So the criterion holds in 1 of 4 cells, and the firing part holds in all 4. With the old detector the firing part holds and the block part fails, which is also partial.
- **A weakness to note:** `fig4-no-pole-difference` stays reproduced, because the criterion's quantity (the fitted |dFmax|) shows no difference under any of its readings. But two new variants do find an amplitude difference in the full set of 22 experiments:
  - |dF| over the last 0.5 µs of the pulse is larger at the anodic pole (p = 0.014 and 0.011).
  - With poorly constrained fits dropped, |dFmax| differs at p = 0.046 in 2 of 8 readings.
  - Neither holds in the 40 V set, and the difference grows with pulse amplitude. The notes and the conclusion now say this.

**What I added or corrected**
- **`strobe.py`:**
  - The docstring said the fits use the onset estimated from the data; it now says they use frame 20, with the estimated onset as a variant.
  - Added a variant of ROI (a) clipped to the soma, and kept the full RATIO image and mask.
- **Main notebook:**
  - The full HDF5 contents of one file: no ROIs, labels or notes.
  - Pixel counts of the soma and every ROI.
  - A check that the nine cells of Figures 5 and 6 are not in this dandiset (no recording dates shared with 001274, and every file names the three-electrode array).
  - Trace and fit panels for all 22 experiments under both ROI readings.
  - Variants with the estimated onset, with fits dropped whose tau exceeds its fitting window, and with ROI (a) clipped to the soma. None changes an outcome.
  - A pole-position variant with neurite stumps trimmed from the soma mask: 12 of 14 pass.
  - Fixed the header table, which listed figs1 as untested.
- **`elsewhere_001272.ipynb`:**
  - Traces of every neuron at its highest field, with the bleaching drift and the first 5 ms marked.
  - Variants that drop first APs within 5 ms of onset, set the depolarization level to 5 SD of the pre-stimulus trace, or use the old detector. The outcome stays not reproduced under all of them.
- **`questions/001273.yaml`** (new): asks a reader whether the FluoVolt 5% level should apply to the Di-8-ANEPPS claim. The claim itself is unchanged.
- **Attempt record:** updated notes and deviations, and the round recorded under `verifications` with the verifier's reasons and my response for every claim. `README.md` now gives the runtime as about 25 minutes.

**Not done**
- **No debris ROI.** The paper chose it by eye, and the candidate spots in the images polarize too, so an automatic choice would be no better grounded than the whole-frame scaling already shown. The summary now explains this.
- **`blocked_by` for fig5, fig6 and threshold-depolarization-estimate** stays `too_large`, where the verifier wrote `other`. Both say blocked; the difference is recorded.

I did not touch the existing change to `tools/build_site.py`, and I committed nothing.
