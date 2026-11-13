I've written `claims/kay-2008.yaml`, and the quote checker passes it with no problems. Nothing is committed.

**Text read.** The version of record (Letter, Methods) with its full Supplementary Information: Supplementary Figures 1 to 11, Table 1, Discussion 1 to 3 and Methods 1 to 11. Nothing the claims needed was missing from the text. I rendered PDF pages only for Figure 4 and Supplementary Figures 4, 5 and 8, whose numbers the text garbles. The paper links no analysis code, so I read none. It names only Liu's m-sequence code and Ihler's kernel density estimation code.

**Claims.** There are 22 claims:
- 21 have quotes. The voxel counts of Supplementary Table 1 are marked `inferred`, as no sentence states them.
- 2 have statistics (3 values): the binomial tests of Supplementary Discussion 1, and the sign test of Supplementary Figure 8, recorded as p < 0.05.
- All 22 have criteria.

The claims cover:
- identification at set size 120: S1 92%, S2 72%; single trials 51% and 32%
- the noise ceilings
- set size up to 1,000 and the extrapolations to 10% performance
- the retinotopy-only model, at 120 images and extrapolated
- the nine constrained models
- the two later sessions (82% at two months, 100% at 14 months)
- errors falling on similar images
- the best voxel count (about 500)
- Supplementary Table 1: voxel counts, SNR, predictive power by area
- the poor fit in V4
- the example voxel of Figure 2
- the area-averaged tuning curves
- the check against retinotopic mapping
- receptive-field size against eccentricity
- the classification-extension control

**Details left open, with the readings named:**
- **O1, candidate voxels:** (a) V1 to V3 voxels whose first model is significant at p < 0.01, or (b) all V1 to V3 voxels.
- **O2, the significance bootstrap:** not described. Standard choice: resample the 120 images, 1,000 times.
- **O3, wavelet grid placement:** a standard convention.
- **O4, the goggles' luminance response:** not given. Pixel values are taken as linear in luminance.
- **O5, the final model's field of view:** (a) the ±2 SD square of the fitted Gaussian, or (b) the best first model's field of view.
- **O6, single trials:** models fitted to (a) the repeated-trial responses or (b) the single-trial responses.
- **Averaging across subjects (Fig. 4c):** (a) average the performance curves, or (b) average the exponents. (a) fits better, since averaging the per-subject exponents gives 9.3 and 5.4, not the printed 9.5 and 5.1.
- **Noise-ceiling sampling:** sampling with or without replacement.
- **SNR standard error:** least-squares or bootstrap.
- **Contrast in Supplementary Discussion 1:** RMS contrast as the SD, or the SD over the mean; and which voxels are used.
- **Which V1 voxels are averaged for the tuning curves:** two readings.
- **Image similarity for the errors claim:** pixel luminance or local contrast. Its test is set by me, and so are the bounds for "broadband", "nearly flat" and "about 500 voxels". Each criterion says so.

**Readings of garbled text.**
- **Formulas:** the stimulus resolution formula is read as min(500, round(2^(9 − x/8))), which reproduces both printed examples. The set-size formula is read as drawing images without replacement.
- **Figure values:** the noise ceilings and the Supplementary Figure 8 p-values were read from the figures. The p-values come from a low-resolution table and are only cited in the criterion.

**Missing data.** These are not missing from the paper, but some claims need data the paper never deposited:
- **The 999-image library:** the paper gives no source for it. Without it, the claims on set size, extrapolation, retinotopy-only extrapolation and constrained models cannot be tested as the paper did them (marked `with_inputs`).
- **S1's later sessions and the retinotopic mapping data:** the dataset's description does not list them.
- **Voxel 42205:** the paper does not say how its voxel numbers map onto the dataset's indexing.
