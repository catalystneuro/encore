I finished steps 1 to 5 of the Author section and ran the handover. The entry passes `check`, and the notebook ran from a clean environment in 8.5 min. The handover package is in `executed/001025-pakhomov-2023/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig4-unipolar-strongest, fig4-bipolar-cancellation | blocked, data_missing |
| fig5a, fig5bc, fig6a, fig6b, fig8a, fig8b, fig9, fig9c | blocked, other (their data are in other dandisets) |
| fig7a-amplitude-scales-uptake | not reproduced (ratios 5.99 / 5.65 / 7.25 against 15.5 / 16.2 / 16.8; all 36 readings miss) |
| fig7b-targeting-independent-of-amplitude | not reproduced, assumed (1 of 20 voltage pairs at p = 0.0037; 22 of 72 readings find no pair) |
| fig7cd-holds-for-large-array | not reproduced, assumed (p = 0.0494 with a 2-dish group; 62 of 72 readings find no difference) |
| discussion-independent-of-array-size | not reproduced, assumed (depends on the two above) |

**(2) Dataset, assumptions and questions**
- **What it holds:** 21 stitched YO-PRO images from Fig. 7 only: 1Px4 on the small array at 2.4 to 5.6 kV, and 10Px4 on the large array at 4.8 kV (2 dishes) and 6.4 kV (3 dishes). Version 0.240605.1826 is the only published one.
- **Where the rest is:** Figs. 5, 6, 8 and 9 are in dandisets 000686, 000875, 001027 and 001028, which all cite the paper. The Fig. 4 single-cell data are on none of them.
- **What is missing:** there are no ROIs, electrode positions, pixel size or array label. The notebook fits the electrodes in each image and places the paper's ROIs from them. The array size inferred from electrode spacing matches the packet protocol in every file.
- **Metadata problems:**
  - Subject ids 15 and 25 each hold two different dishes.
  - 2.4 kV has 4 dishes where the paper says n = 3.
  - 7 files name no detector, objective or channel.
  - The images' dark floor varies from 33 to 81 a.u. between dishes and sessions.
- **Assumed main reading:** camera pixel size of 0.65 µm, 92/224 ROIs over both diagonals, both diagonals averaged, one ROI centred on the array centre, raw ROI values, normalisation to the mean of the end ROIs. Every other reading is shown.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Was a background subtracted? Subtracting the median inside the electrode footprints raises the fig7a ratios to 13.4 / 15.9 / 15.2, close to the paper's. The claims file fixes no subtraction, so this stays a variant.
  - How were the ROIs laid out, what is the pixel size, and how is the 8.4 mm diagonal measured?
- **Questions to a reader:** none.

**(3) Protocol gaps**
1. The paper's data are split over several dandisets in the same archive. `data: elsewhere` only covers another archive and is the reader's to set, and `data_missing` is defined as "not public anywhere". I blocked those claims as `other` and named the dandiset in each note.
2. Readings for absence claims: the protocol says absence is judged on the paper's test alone, but it does not say whether that overrides the readings of the ROI layout. I applied step 1.6 (adopt the best-supported reading as an assumption and show every reading).
3. The protocol has no guidance for image data with no annotations, where the author has to place ROIs. I treated the electrode detection and the pixel size as method choices, ran both pixel-size readings, and showed overlays of every fit.
4. The clock check in "Check the data" does not apply to single time-point images. The notebook says so.

**(4) Runtime and failures**
- About 67 min of the 5 h. Streaming all 21 images takes about 8 min.
- Two development errors were fixed: an argmin on an empty window in the electrode fit, and a wrong key when printing the imaging descriptions. No final step failed.
