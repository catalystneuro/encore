I did steps 1 to 5 of the Author section and ran the handover (step 6). Lock, check and the clean run all passed. The notebook ran in 13.8 minutes (828 s), most of it streaming 19.4 GB of YO-PRO-1 (YP) images. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig7be-center-linear-with-bursts | partially reproduced (CHO slope p = 2e-10; CT26 slope p = 0.0013, needs < 0.001) |
| fig7b-ct26-saturation | partially reproduced (CT26 6-burst point below the fitted line but inside the 95% band) |
| fig7cf-fwhm-with-bursts | reproduced (both parts hold in 2 of the 12 readings the criterion names) |
| fig7-sharpest-peak-one-burst | reproduced, resting on an assumption (0.5 mm ROI spacing: FWHM 1.09 mm, 7.1%, 2.29%) |
| fig7-offtarget-40-50-fold | not reproduced (ratio 31.9 to 34.8 at 6 mm) |
| fig7-cho-replicates-ct26 | reproduced |
| fig4b-40-fold-at-02mhz | not reproduced (45.1, just above the 36 to 44 tolerance) |
| fig3a-cancan-center-enhanced | partially reproduced (control ratio 1.10, should be below 1) |
| fig3bc-lorentzian-profile | reproduced |
| fig3bc-offtarget-deviation-falls-with-rate | reproduced |
| fig4b-center-no-rate-effect | reproduced (p = 0.26, but only two 1 Hz wells) |
| fig4b-near-electrode-rate-decline | reproduced |
| fig4c-fwhm-decreases-with-rate | partially reproduced (1 Hz FWHM is 4.56 mm, tolerance 3.6 to 4.4) |
| fig4c-log-dependence, fig5 (4 claims), fig6 (3 claims) | blocked, `other`: the data are in other dandisets |
| fig2-heating-below-44c, fig1e-field-simulation | blocked, `data_missing` |

**2. What was found about the dataset**
- **Version:** I pinned 0.250701.1609, the only published version; the paper cites none.
- **What it holds:** 54 wells. The Fig. 7 burst series at 0.2 MHz, plus 1 Hz CANCAN and 1 Hz control wells. Each file is one stitched 19190 x 19190 image.
- **Other dandisets:** 001047, 001277 and 001284 also cite this paper and appear to hold the 1 Hz vs 0.2 MHz series, the pulse-duration series and the raised-electrode series. Dandiset 001276 does not point to them.
- **Findings recorded in the attempt:**
  - No pixel size and no electrode positions in the files.
  - Protocol and condition appear only in free text.
  - `session_start_time` is the conversion date, and subject age is "P1D" for culture wells.
  - More wells than the paper's n, with no record of which it used.
  - Two Hoechst files carry an undocumented second plane; one well has a duplicated Hoechst fragment and another has no Hoechst file.
  - Three wells where the electrode footprints cannot be found.
- **How the array was located:** pixel size 1.625 um, taken from the camera and objective in Methods 2.4. It agrees with the fitted electrode spacing (median 12.83 mm against the paper's 12.8 mm). The center comes from a square fitted to the footprints. I left out three wells by a rule I set, since the paper places ROIs by hand; this is recorded as a deviation.
- **Assumption:** 0.5 mm ROI spacing for fig7-sharpest-peak-one-burst. At 1 mm spacing that claim would be partially reproduced.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which ROI spacing, fit range and background footprint were used for Fig. 7, and which wells form each group.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**
1. There is no rule for a paper whose data are split across several dandisets in the same archive. `data_missing` excludes data that are public elsewhere, and `elsewhere` needs the claims file to name the source, which a reader cannot know. I blocked those claims as `other` and named the dandisets.
2. The clock check in step 2 does not fit single-time-point images. I replaced it with a spatial check: the YP peak sits about 0.3 mm from the fitted center in CANCAN wells, while control wells show no centered peak.
3. "Break down by animal" does not fit culture wells. I broke results down by experiment date.
4. The protocol does not cover an author having to place ROIs that the paper placed by hand, or the exclusion rule this needs. I set an objective rule, showed every fit in a figure, and recorded it as a deviation.
5. It is unclear whether a calibration taken from the paper's equipment (pixel size) counts as an assumption. I treated it as a detail taken from the paper, checked it against the electrode geometry, and did not set `assumed`.
6. Step 1.6 says the outcome is the one all readings give. The fig7cf criterion instead says "under one reading". I followed the criterion there, and used step 1.6 for fit range and spacing in fig7-sharpest-peak-one-burst.
7. There is no rule for a claim that can only be tested on part of its conditions (2 of 4 packet rates). I judged the result on the rates present and recorded the missing rates as deviations.
8. The protocol is silent on caching during development. I kept binned arrays in `$TMPDIR` while developing; the notebook streams everything.
9. The example record writes the harness as "Claude Code (GitHub Actions)", while the prompt says "Claude Code". I used the prompt's value.

**4. Runtime and failures**
- About 65 minutes in all (19:35 to 20:41 UTC). Two clean runs of the notebook took 13.7 and 13.9 minutes.
- One `sed` on a tool-output file was denied for want of approval; I read the file another way.
- I could not read the file-level metadata of 001277 and 001284 (their image path differs from this dandiset's). So whether 001047 holds 1 kHz and 10 kHz wells is not established, and fig4c-log-dependence's notes say so.

Files are in `entries/001276-silkuniene-2025/`:
- reproduce_silkuniene_2025.ipynb
- cancan.py
- README.md
- entry.yaml

The attempt record is `attempts/001276-silkuniene-2025-01.yaml`.
