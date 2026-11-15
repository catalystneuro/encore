I checked `claims/kay-2008.yaml` against the paper and corrected it; the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/kay-2008.yaml: 23 claims, 22 quotes, 3 statistical values, 0 problems`. Before my edits it found 22 claims and 0 problems.

I rendered Figure 4 and Supplementary Figures 4, 5 and 8 from the PDF to check the numbers read off them. That needed a temporary PyMuPDF install under `$TMPDIR`.

**Changes, by claim**
- **Opening comment:**
  - Retinotopic mapping was one separate session per subject, and voxels outside V1 to V3 were discarded.
  - The data set's description says the ROI localizer scans are *not included*. The comment had said it "does not mention" them.
- **fig4a-noise-ceiling:**
  - The statement said the ceilings "show" the noise difference; the legend says "suggest".
  - From the figure, the markers sit at about 99 / 99 / 80 / 64, not 98 / 98 / 80 / 62. Values, tolerances and statement are corrected.
  - Some images have 14 trials, not 13, because the single-trial analysis keeps the 6 repeated trials.
- **fig4b-extrapolation:** the tolerance of 10% of the exponent now states its reason.
- **suppfig8-constrained-models:**
  - The voxel set comes from "the model that imposed no constraints". That could be model I or the final GWP model, so both are now named as readings.
  - The paper does not state `n` for the sign test, and the field now says so.
  - The percentages and p-values match the figure.
- **time-two-months, time-fourteen-months:** how the 500 voxels are chosen for the later sessions is not stated, so I added two readings.
- **supptable1-snr:** fixed garbled criterion wording.
- **methods-v4-poor:** noted that the paper discarded its V4 voxels, so V4 can only come from the data set's own labels. The comparison with V3 is marked as fixed here, not by the paper.
- **fig2-representative-voxel:** the bound used for "just below" the meridian is marked as fixed here.
- **suppfig7-roi-tuning:**
  - Added readings for which models give the averaged curves and for which subject is shown.
  - The thresholds for "nearly flat" and "band-pass" are marked as fixed here.
- **Added suppm7-selected-voxels-v1:** "Most of these voxels were located in area V1" is a stated result that had no claim.
- **Checked and unchanged:** the exponents in Figure 4b–c and Supplementary Figure 5, and the axis of Supplementary Figure 4.

**Still open**
- The 999-image library is not deposited, so four claims cannot be tested the way the paper did them: fig4b-set-size-1000, fig4b-extrapolation, fig4c-retinotopy-only-extrapolation and suppfig8-constrained-models.
- The data set's description does not list the later S1 sessions. It says the mapping scans are not included. So time-two-months, time-fourteen-months and suppfig10-retinotopy-validation depend on the author finding that data elsewhere.
- Supplementary Table 1's third column has no claim. I judged it a detail, not a main finding.

**Ready:** true, recorded under `checks` with 18 change lines.
