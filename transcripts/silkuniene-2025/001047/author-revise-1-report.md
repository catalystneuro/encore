I've handled all 11 points in the round-1 report. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passes in 410 s), and every conclusion now matches the new numbers. Nothing is committed.

**Outcome changes**
- **fig3-tail-deviation-falls-with-rate:** partially reproduced → not reproduced, as the verifier said. At x1 every 0.2 MHz fit runs to the 100-mm width bound, so there is no fitted peak to deviate from. A deviation now counts only when both fits have a peak.
- **fig4b-centre-no-rate-effect:** reproduced → partially reproduced, as the verifier said. The paper's test finds no effect (p = 0.93), but neither rate stains the centre, and only one of the paper's comparisons can be made.
- **fig5-raised-electrodes-weaken-centre:** still blocked; the reason is now `metadata_insufficient`, as the verifier gave it.
- **fig7-sharpest-one-burst:** still blocked; the reason is now `metadata_insufficient` (the burst labels). The verifier's conditional "not reproduced" is recorded as a disagreement. Under the attempt's reading of the labels there is no 1-burst well. Under the other reading the result is far from the claim (FWHM 55 to 68 mm, ratio below zero), and the notes say so.
- All other outcomes are unchanged and agree with the verifier.

**Corrected or added**
- **Burst labels (B1):** the files say the protocol was "repeated 2, 3, or 5 times" upon completion. I now read the label as the number of repeats after the first burst. That makes x1 the paper's 2 bursts and x5 its 6 bursts, the largest number in Figure 7. This reading is adopted as an assumption and decides the outcomes. The other reading (the label is the total) is shown everywhere: 1 Hz x2 against 0.2 MHz x1 and x3, which bracket 2 bursts. x5 is now only a variant, and the "holds at one label = partial" rule is gone.
- **Error-bar rule, F8 (B4):** every table now shows three readings: the gap must exceed the longer s.e. bar, the mean of the two, or the shorter one. I adopted the longer bar as the literal reading. fig4b-near-electrode-decline rests on this choice: it would be reproduced at x1 under the shorter-bar reading, and the record says so.
- **Fig 7 CT26 half (B2):** now tested and reported. The slope of centre YP against bursts is not significant (p = 0.085 or 0.051, depending on the label reading), there is no saturation, and no FWHM slope is positive with p < 0.05 in any of 72 combinations of readings. Both claims stay blocked because the CHO series is missing.
- **Propidium claims (B3):** x1 now decides, with x3, x5 and the pooled wells shown. Each is also shown without the misplaced areas.
- **Area panels (B6):** all 77 areas are now shown. Four areas have centres that are visibly wrong, by my eye: the verifier's three plus one whole-well image. They are flagged and kept in the analysis.
- **Hoechst images (B7):** I printed the acquisition times. The Hoechst images were taken at 10:35, before the YP (12:49) and propidium (14:24) images, so they are pre-exposure. The helper now labels them as such.
- **Other text fixes (B5, B8 to B11):**
  - The 3.2-kV voltage in the files cannot be checked from the images; this is now in the notebook and the findings.
  - The CHO statement is corrected: the image extents do contain the electrode centres, though the footprints are clipped.
  - The 9% pixel-size mismatch in the whole-well images is stated, and a two-well-only variant is added.
  - The label check (11 of 18 images, binomial p = 0.48) is now called uninformative.
  - Subject 011C_x5 is explained as a control.
- **Output the verifier asked for:** the raw, unsubtracted profiles and backgrounds for the 0.2 MHz x1 wells.
- **Record:** the round is under `verifications`, with the verifier's reasons close to its own words and my changes under `response`. The README is updated to match.

**Not done**
- fig5c-nuclear-yp-centre keeps `data_missing`, and the verifier's `metadata_insufficient` is recorded as a disagreement. The claims file's own criterion says to block when full-resolution images are missing, and these images are at half the camera's resolution.
- The 9% pixel-size mismatch in the whole-well images is stated but not resolved.
- No question was added to `questions/001047.yaml`, because the report names no place where the claims file misreads the paper.
