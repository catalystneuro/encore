I checked the claims file against the paper and the authors' code (repository at commit 4ee34f3). After my corrections and three added claims, I think it is fit for an attempt (`ready: true`). I did not commit anything.

**Checker result:** `22 claims, 22 quotes, 32 statistical values, 1 problems`. The one problem is the p-value 6.1e-05 for fig1g-dv-sequence-du. The text extraction printed it as "6.1 3 10�5", which is 6.1 × 10^-5, so the recorded value is right and I left it.

**Changes, by claim**
- **fig5d-isomap-pmr:** the code runs Isomap on PETHs cut to 0 to 155 ms, but the Methods and the Figure 5D legend say ±250 ms. The ±250 ms window is now the main result and the code's window a variant, since the Methods come first.
- **fig2f-gamma-travels:** the Figure 2D legend aligns gamma power to the delta peak, while the Methods align it to the DOWN-to-UP transition; both are now run. The paper doesn't say how power is taken from the filtered signal or how the UP-to-DOWN measure is defined for the LFP. These are now named as open, with readings, and a claim whose readings disagree is blocked.
- **figs2g-adn-synchronous:** the ADN detection code drops DOWN states shorter than 50 ms, but the Methods say 30 ms. The criterion didn't mention this. The Methods' 30 ms is now the main result and the code's 50 ms a variant.
- **figs1j-dorsal-ventral-same-hd:** the criterion summarized each session by the mean angular difference, which the paper doesn't specify. Now open, with the mean and the median both run.
- **figs2e-speed-similar:** noted that "mm/s" may be a garbled micro sign; the expected values are compared in mm/s.
- **Added three claims** for findings the Results cite that had none:
  - figs1i-du-more-stable: delays at UP onset are more stable across half-sessions than timing at the UP-to-DOWN transition (Figure S1I).
  - figs1kl-not-firing-rate: firing rate doesn't explain the sequence (Figures S1K and S1L).
  - figs2d-lfp-spike-agree: LFP and spikes give matching delay-depth correlations (Figure S2D).
- **Header:** notes the added claims.
- The other criteria match the scripts they cite: Figures 5C, 5E, 5F, 1G, 1H, S2G and the RSC DOWN-state detection.

**Still open**
- I couldn't render the PDF, so the S2E speed unit and any detail shown only in figures weren't checked against the figures.
- Figure S1J prints W = 38, p = 0.13, the same values as the Figure 1G UP-to-DOWN test. This may be a copy error in the paper; the claim keeps the printed values.
- **fig1j-down-resets-hd:** the paper doesn't fix which bin gives the angle at the end of the UP state, or the histogram bins, and has no code for this figure. The readings in the criterion are the file's own.
- Minor findings with no test in the paper are left without claims: the synchronous delta waves (S2B, S2C), the lack of clustering of preferred directions (S1G), the second Isomap dimension (S5), and the UP and DOWN duration statistics (S3A).

The changes are logged under `checks` at the end of `claims/000987/10.1016-j.cub.2024.05.048.yaml`.
