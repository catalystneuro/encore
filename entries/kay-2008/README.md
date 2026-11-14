# Kay, Naselaris, Prenger & Gallant (2008) from CRCNS vim-1

Tests the findings of [Kay et al. (2008)](https://doi.org/10.1038/nature06713) that can be tested on
CRCNS [vim-1](http://crcns.org/data-sets/vc/vim-1) (doi:10.6080/K0QN64NG), which holds the estimated
fMRI responses of two subjects to 1,750 model estimation images and 120 identification images, ROI
labels, the stimuli and the raw time series. The 999-image library of the set-size analyses, the
later sessions of subject S1 and the retinotopic mapping scans are not in it.

| Claim | Outcome |
|---|---|
| S1 identifies 92% of 120 images (Figure 3) | Reproduced (90.8%) |
| S2 identifies 72% of 120 images (Figure 4a) | Reproduced (72.5%) |
| Retinotopy-only model, 55% and 42% at 120 images | Reproduced |
| Errors fall on visually similar images | Reproduced (local contrast reading) |
| Voxel counts per area (Supplementary Table 1) | Reproduced |
| Predictive power falls from V1 to V2 to V3 | Reproduced (assumed) |
| The model does poorly in V4 | Reproduced |
| RF size grows with eccentricity and from V1 to V3 | Partially reproduced (assumed) |
| Representative voxel 42205 (Figure 2) | Partially reproduced (assumed) |
| V1-averaged tuning curves (Supplementary Figure 7) | Not reproduced |
| Classification extension (Supplementary Discussion 1) | Not reproduced |
| Most selected voxels lie in V1 | Not reproduced |
| Performance is best at about 500 voxels (Supplementary Figure 4) | Partially reproduced (repeated trials only) |
| Single-trial identification, noise ceiling, SNR | Blocked: too large |
| Set sizes up to 1,000 and beyond, retinotopy-only extrapolation, constrained models | Blocked: data missing |
| Later sessions (two and fourteen months), retinotopic validation | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The identification results hold only when the final receptive-field model covers the square of
+/-2 SD of the fitted Gaussian; over the best initial model's field of view they are much lower. The
paper does not say which it used. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/kay-2008-01.yaml`](../../attempts/kay-2008-01.yaml).

- `reproduce_kay_2008.ipynb`: the analysis. It took 39 minutes in one run and 106 in another, on a
  slower machine, most of it fitting one final model per voxel.
- `vim1.py`: loading the files, the Gabor wavelet pyramid, the gradient descent fits, identification
  and the retinotopy-only model. Other notebooks on this data set can import it.
