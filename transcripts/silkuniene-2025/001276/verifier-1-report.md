**Verifier report, round 1: Silkuniene et al. 2025 on DANDI:001276 (0.250701.1609)**

The claims file has 23 claims. The notebook tests 13 and treats 10 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig7be-center-linear-with-bursts | partially_reproduced | CHO slope 643.9 a.u. per burst, p = 2.2e-10 (individual experiments). The CT26 slope is positive but p = 0.0013 (individual) and 0.024 (group means), so it misses p < 0.001 under both readings (cell 18). |
| fig7b-ct26-saturation | partially_reproduced | The CT26 6-burst mean (4827) is below the fitted line (6272) but inside the 95% band (4234 to 8311) under both readings. The CHO 6-burst point is inside its band (cell 20). The criterion calls this partial. |
| fig7cf-fwhm-with-bursts | reproduced (fragile) | At 0.5 mm spacing, fit range 5 or 6 mm, individual experiments: CT26 slope p < 1e-4 and CHO p = 0.064 or 0.090 (cell 22). In 10 of the 12 readings the CHO slope is significant or the CT26 p is too large. The dataset has 23 CHO wells where the paper had 12. |
| fig7-sharpest-peak-one-burst | reproduced | At 0.5 mm spacing: FWHM 1.093 to 1.103 mm, 7.14 to 7.21% of the gap, area reading (b) 2.29 to 2.33%. All are within tolerance (cell 24). At 1 mm spacing the area test fails. |
| fig7-offtarget-40-50-fold | not_reproduced (not robust) | For 1 burst the ratios are 31.9, 34.8, 14.9 and 14.4. Reading B fails too (4 bursts gives 7.7) (cell 26). The 6 mm denominators (15 to 48 a.u.) are about as large as the spread between footprint backgrounds (problem 1). |
| fig7-cho-replicates-ct26 | reproduced | At 2, 4 and 6 bursts, center YP exceeds YP at 6 mm (18.2x, 23.1x, 18.9x) and at 7 mm (7.4x, 6.3x, 5.3x). The CHO linear part also holds (cell 28). |
| fig4b-40-fold-at-02mhz | not_reproduced (not robust) | Ratios 45.08, 52.10, 10.73 and 12.51; the window is 36 to 44 (cell 30). The 6 mm group-mean ratio misses by 1.1 and has the same background sensitivity as the fig7 ratio claim. |
| fig3a-cancan-center-enhanced | not_reproduced | The CANCAN ratios exceed 1 (3.43/1.67 at 1 Hz, 45.1/10.7 at 0.2 MHz). The control ratios are 1.10 and 1.11, where the criterion requires below 1, and the control center is the brightest point (cell 32). Only 2 of 4 CANCAN rates are present. |
| fig3bc-lorentzian-profile | reproduced (2 of 4 rates) | R is 0.93 to 0.99 with p < 0.001 for 1 Hz and 0.2 MHz in both directions and at both spacings (cell 34). The 1 Hz group has only 2 wells, and 1 kHz and 10 kHz are absent. |
| fig3bc-offtarget-deviation-falls-with-rate | reproduced | The deviation is 1.7 to 2.7% of a at 0.2 MHz and 24 to 30% at 1 Hz, in both directions and at both spacings (cell 36). |
| fig4b-center-no-rate-effect | reproduced (1 of 3 comparisons) | 0.2 MHz against 1 Hz: p = 0.257, or 0.770 with x3 correction (cell 38). With n = 2 against 5 and a 36% lower mean, the test has little power. |
| fig4b-near-electrode-rate-decline | reproduced (2 rates) | Exponents are -0.246 at 6 mm and -0.188 at 7 mm; t-test p = 3.2e-6 and 3.6e-4 (cell 40). With two rates the power fit is a two-point slope. |
| fig4c-fwhm-decreases-with-rate | partially_reproduced | 0.2 MHz FWHM is 2.00 or 1.88 mm (in tolerance) and the smallest value is 12 to 13% of the gap. The 1 Hz FWHM is 4.56 or 4.54 mm, outside 3.6 to 4.4 (n = 2). The required 1 kHz and 10 kHz tests are impossible (cell 42). |
| fig4c-log-dependence | blocked: data_missing | I checked all 108 asset descriptions through the API: the only packet rates are 0.2 MHz and 1 Hz. |
| fig5-raised-electrodes-weaker-center | blocked: data_missing | No asset description mentions elevation or raised electrodes. |
| fig5b-pr-gaussian-yp-lorentzian | blocked: data_missing (Pr part) | All 108 files are DAPI-pre or FITC-post, so there is no propidium. The YP half (Lorentzian against Gaussian R², CT26 0.2 MHz 2 bursts) could be tested on the wells present and was not. |
| fig5-yp-spot-slightly-larger-than-pr | blocked: data_missing | Needs propidium. |
| fig5c-irreversible-center | blocked, but for methods_underspecified, not data_missing | The YP part passes (cell 44: center 1985 a.u. is above every distance from 2 to 7 mm). Pre-exposure Hoechst exists for every well and the criterion does not ask for post-exposure Hoechst. Only the undefined Hoechst reference level (an open item in the claims file) blocks that part. |
| fig6b-900ns-peak-not-significant | blocked: data_missing | All 324 pulse-duration mentions in the descriptions are 600 ns. |
| fig6c-normalized-decline-similar | blocked: data_missing | Same reason. |
| fig6d-fwhm-sharper-longer-pulses | blocked: data_missing | Same reason. |
| fig2-heating-below-44c | blocked: data_missing | The files hold only well images; there are no thermochromic film images. |
| fig1e-field-simulation | blocked: data_missing | Simulation output; the model is not public and not in the dataset. |

The paper states no chance levels. I found no place where the claims file misreads the paper. I checked the Fig. 7 legend (p = 0.44, 6-burst exclusion), Fig. 4B (4 directions pooled) and Methods 2.5 (background) against the text.

### B. Problems

1. [affects a conclusion] **Background choice** (`cancan.background`, cell 14). Methods 2.5 says the background is "3 ROIs placed within a footprint of an electrode", meaning one footprint. The helper instead takes the median over all four footprints, an author choice presented as "standard". Cell 14 shows the spread between footprints has a median of 15% of background (about 25 to 80 a.u.). That is comparable to YP at 6 mm in CT26 0.2 MHz wells (13 to 48 a.u.). The 6 mm ratios behind the two not_reproduced ratio claims (fig7-offtarget-40-50-fold, fig4b-40-fold-at-02mhz) can therefore move by a large factor, and fig4b already misses by only 1.1. The four single-footprint readings were never run.
2. [affects a conclusion] **Well exclusion rule** (cell 9). The rule is the author's own: centers within 0.5 mm and free side within 4%. It drops CT26 well P1_20240627_B1 (0.2 MHz, 2 bursts) and two CHO 1-burst wells. These wells count toward fig7be (CT26 p = 0.0013, against a 0.001 threshold) and fig4b-40-fold (ratio 45.1, against a 44 limit). No manual or alternative placement was tried, and no sensitivity check was shown.
3. [affects a conclusion] **fig5c reason is wrong** (cell 0 table, cell 43). The claim is blocked as "no post-exposure Hoechst", but the criterion does not require that. Pre-exposure Hoechst (DAPI) images exist for all wells. The real block is the undefined reference level.
4. [does not affect a conclusion] **Pixel-size assumption** (`cancan.py` docstring, cell 8). Both say "The files give no pixel size". In fact the OME-XML in every image description gives PhysicalSizeX = 1.625 µm, plus acquisition dates and exposure times. The assumed value is correct. I also confirmed that FITC exposure is 200 ms in all 53 images that record one, so intensities are comparable across wells. The notebook never checked this.
5. [does not affect a conclusion] **Untested half of fig5b** (cell 0). The YP half of fig5b-pr-gaussian-yp-lorentzian could have been tested on the CT26 0.2 MHz 2-burst wells and was not.
6. [does not affect a conclusion] **Fragile fig7cf pass** (cell 22). The outcome depends on choosing 1 of 12 readings. The dataset's CHO n (8, 7, 8 wells) is about twice the paper's n = 4, which gives power to detect the 0.13 mm-per-burst CHO slope. The criterion allows the "one reading" rule, but the pass is fragile.
7. [does not affect a conclusion] **Sides profile runs past the array edge** (`cancan.profile` with kind="sides"). The side midpoint is 6.4 mm from the center, so the 6.5 and 7 mm ROIs lie outside the electrode square. These ROIs enter the deviation measure in cell 36, but the 1 Hz against 0.2 MHz difference is about 10-fold.
8. [does not affect a conclusion] **p of the fit correlation** (`fit_lorentz`). The p comes from Pearson with n - 2 degrees of freedom and ignores the two fitted parameters. For 1 Hz sides at 1 mm spacing (R = 0.927, 9 points), 5 degrees of freedom would give p ≈ 0.003. The 0.5 mm reading still passes.
9. [does not affect a conclusion] **Small center bias** (`square_fit`). On synthetic images with a known square, the center was off by 0.10 to 0.13 mm. That inflates FWHM by about 3% at 1 mm spacing. Other helpers checked on synthetic inputs behaved correctly: `fit_lorentz` recovered b = 1.10 from 1.1, `fit_band` matched a direct OLS confidence band, and `distances`, `roi_mean` and `profile` were correct.
10. [does not affect a conclusion] **Data provenance of the Fig. 3 and 4 tests** (cells 32 to 42). These claims are tested on wells that match the conditions but may come from the Fig. 7 series. The paper's Fig. 3 and 4 series had n = 3 per rate and n = 5 controls; here 1 Hz CANCAN has n = 2.

### C. Not checked, and the output that would settle it

- **Background sensitivity of the ratio claims:** the ratio tables in cells 26 and 30 recomputed with each single-footprint background, and the per-footprint values in `bgs`.
- **Excluded wells:** center YP, the 6 and 7 mm values, and FWHM for the 3 excluded wells under a manually checked square, plus the fig7be and fig4b numbers with them included.
- **Camera saturation:** the fraction of pixels at or near the maximum in each ROI. `bin_max` reaches 65435, and saturation could flatten the control profiles (fig3a) or create the CT26 6-burst "saturation".
- **Hoechst in the footprint:** mean Hoechst inside the footprint against the monolayer and against the camera offset (unimaged area or the empty plane), from the pre-exposure DAPI images.
- **YP half of fig5b:** Lorentzian and Gaussian R² on the CT26 0.2 MHz 2-burst group-mean profile, fitted from -5 to 5 mm.
- **Square fits:** I did not view the figures in cells 10 and 16, so whether the square sits correctly in each image rests on the numeric checks in cells 9 and 12.
