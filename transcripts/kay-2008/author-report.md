The attempt on Kay et al. (2008) is finished: 12 claims tested, 11 blocked. The entry passes `check` and a clean `run` (39 minutes, peak memory 8.6 GB), and the handover package was built. No verification of my own was done.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig3-s1-repeated-120 | reproduced: 109/120 (90.8%), paper 110 |
| fig4a-s2-repeated-120 | reproduced: 87/120 (72.5%), paper 86 |
| suppm8-retinotopy-only-120 | reproduced: 53.3% and 43.8% (paper 55 and 42), both below the main model |
| errors-similar-images | reproduced with the local-contrast similarity (p = 0.00031); not with pixel luminance |
| supptable1-voxel-counts | reproduced: all six counts are exact |
| supptable1-predictive-power-by-area | reproduced: 6 of 6 within tolerance, V1 > V2 > V3 |
| methods-v4-poor | reproduced (the S1 margin is 0.7 points) |
| suppfig11-rf-size-eccentricity | reproduced, resting on an assumption |
| fig2-representative-voxel | partially reproduced, resting on an assumption |
| suppfig7-roi-tuning | not reproduced: the V1 spatial-frequency curve rises to the highest frequency in every variant, so it is not band-pass |
| suppdisc1-classification-extension | not reproduced: S2's contrast result is never above chance |
| suppm7-selected-voxels-v1 | not reproduced: 48% of selected voxels are in V1, not more than half |
| fig4a-single-trial, fig4a-noise-ceiling, suppfig4-500-voxels | blocked, `too_large`: refitting every voxel's time series is estimated at about 615 min |
| supptable1-snr | blocked, `too_large`: estimated about 164 min |
| fig4b-set-size-1000, fig4b-extrapolation, fig4c, suppfig8, time-two-months, time-fourteen-months, suppfig10 | blocked, `data_missing` |

**2. Dataset, assumptions, questions**

- **Choice of reading:** The identification results depend on the final model's field of view. With the ±2 SD square of the fitted Gaussian (O5 a), both subjects reproduce. With the best initial model's field of view (O5 b), the result is 75.8% and 46.7%.
- **Version:** CRCNS data sets are not versioned, so I recorded it as `unversioned` with doi:10.6080/K0QN64NG, and put the MD5 sums from the bucket in the notebook.
- **What the data set lacks:** single-trial responses, standard errors of the estimates, S1's later sessions, the 999-image library, and the retinotopic mapping scans.
- **Readme errors:** it calls `Stimuli.mat` and `mask.mat` MATLAB 7.3 files, but they are MATLAB 5. It gives `Stimuli_Trn_FullRes_15.mat` as 70×120×120, but it holds 70 images of 500×500.
- **Undocumented:** 345 (S1) and 214 (S2) V1 to V3 voxels have NaN responses; the readme does not say whether `voxIdx` is 0- or 1-based; the NIfTI headers give a TR of 0.
- **Assumptions:**
  - fig2: I adopted O5 (a), because its field of view puts the highest frequency at 2.94 cycles/deg, matching the 2.9 on Figure 2b's axis. Tuning curves are taken without the DC offset. I also assumed `voxIdx` 42205 is the paper's voxel 42205.
  - suppfig11: "within the stimulus bounds" is read as the 20° square.
  - A standard wavelet SD, stimulus values linear in luminance, a Gaussian fit with an offset, and area-averaging resampling.
- **Deviations:** one fit per model instead of the mean of 100 bootstrap fits (a 10-bootstrap variant changed results by at most 3 images), and one stopping set shared by the voxels fitted together.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the rule for the final model's field of view; how tuning curves are computed (DC offset, aperture, how voxels with different fields of view are combined); and square or circle for "stimulus bounds". There is also one `paper_inconsistency` finding: the stated 10.1°/5.2° fields of view and 41° orientation bandwidth do not follow from the paper's own resolution list and 1-octave bandwidth.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**

1. Running every reading versus time: the claims file asks for every O1×O5 combination. One combination roughly doubled the runtime (21 to 39 min), which is over the 10-minute aim but under the 60-minute limit. I ran it anyway.
2. A claim that depends on a blocked claim is blocked, even when part of it can be tested. suppfig4 holds in both repeated-trial conditions but is recorded as blocked, with those numbers in its notes.
3. `too_large` estimates need numbers, but numbers from analyses outside the notebook may not enter the record. I put small timing cells in the notebook so the estimates come from it.
4. A "standard choice" that should not change the outcome did change it: whether tuning curves include the DC offset decides fig2. I treated it as an assumption.
5. archives.md says to open zips with fsspec, but vim-1 has no zips: plain `.mat` files (mixed MATLAB 5 and 7.3) and gzipped NIfTI. I streamed each whole file into memory. The NIfTI files cannot be range-read, so each was read whole into memory and decompressed, never written to disk.
6. The data-check step's requirement that every stream shares the trial table's clock does not fit per-image estimates. I used predictive power with the image order shuffled as the contrast.

**4. Runtime and failures**

The run used about 2 h 40 min of the 5 h. The notebook took 39 min per full run, and the entry was executed three times. Nothing failed. `git status` shows untracked dotfiles (`.bashrc`, `.idea`, `.mcp.json` and others) and a `scripts/` folder that I did not create; they should be kept out of the commit.
