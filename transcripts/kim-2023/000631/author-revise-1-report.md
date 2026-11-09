No outcome changed. I fixed or answered every point in the report, and the verifier agreed with all 12 outcomes. The entry re-ran cleanly with `python tools/entry.py all entries/000631-kim-2023` (0 check errors, notebook passes in 278 s), and the notebook text and attempt record match the new numbers. Round 1 is recorded under `verifications` with the verifier's reasons and my response for each claim.

**What I added, by point in the report:**
- **Background (problem 1).**
  - Inside the footprints the YP intensity is flat out to about 0.55 mm. The needle's lumen and the wall ring around it read within 8 counts of each other in 11 of 14 dishes.
  - The exception is the three 833 kHz controls, where the lumen holds bright material.
  - I kept the 0.5 mm disk as the background and now run the lumen alone, the wall ring alone and a 0.6 mm disk as checks on every Figure 2 measure.
  - Every outcome is the same under all four, except fig2-60-fold-co-counter: it is not met with the lumen alone (33 to 219-fold, scattered).
- **ROI layout (problem 2).**
  - The notebook and record now say the layout is a deviation from the claims file, and the notebook states the rule: L2 decides and L1 is a variant.
  - A new scan along the bisector backs this up. The 180° point lies 0.84 to 1.03 mm beyond the base midpoint, which is where L2's first ROI sits. At the midpoint, where L1 starts, the angle is only 168 to 170°.
  - I also corrected L1's ROI overlap from 20% to 15%.
- **Bias of the lowest-ROI reading (problem 3).** I measured it three ways:
  - The lowest ROI and its two neighbours give 16.4 to 18.8-fold at 833 kHz.
  - All ROIs above 160° give 13.1 to 13.9-fold.
  - A bootstrap over dishes, with the bias removed, gives 16.2 to 20.1-fold.
  - With the bias removed, the 60-fold ratio is still 56.9 under normalisation (ii), which is in tolerance.
  - A per-dish table of ROIs 0 to 7 shows no single dish sets the 833 kHz value.
- **1 Hz crossover (problem 4).** It rests on one ROI. Leaving out ROI 11 gives 131.4 to 143.3°, and averaging over three neighbouring ROIs gives 132.8 to 135.6°; both are below the 144° lower bound. The criterion as written is still met, so it stays reproduced, marked low confidence at 1 Hz.
- **Plateau test P2 (problem 5).** It is now reported as untestable under angle model C, which has no ROI below 10°, and model B decides it.
- **Single-ROI plateau level (problem 6).** The notebook now prints how many ROIs the 90 to 100° level uses, and the text says it is one ROI on L2.
- **Things the verifier could not check.**
  - Saturation is negligible: at most 0.03% of pixels in any ROI, and none at 833 kHz.
  - Comparing days: YP in the footprints is similar on every day, but MemBrite (the stain for all cells) differs. It reads about 431 counts in the 833 kHz controls against 295 in the paired dishes they are compared with. The files give no exposure or gain, so whether their YP values compare cannot be checked. I added this to the findings.

**Other changes:** I updated the notes and deviations in `attempts/000631-kim-2023-01.yaml`, the result text and summary in the notebook, and the README, which now names the three fragile values. The helper `swing.py` now records saturated pixels when loading and accepts a ring-shaped footprint region. The notebook's runtime in `entry.yaml` is now 5 minutes.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/000631.yaml`.
- I did not change fig2-60-fold-co-counter even though it fails with a lumen-only background. The lumen mean in the three 833 kHz controls is raised by bright material, and the claims file asks for the mean over the footprints. The record notes the dependence instead.

Nothing is committed or pushed.
