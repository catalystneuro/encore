I've verified all 28 claims in the claims file. 21 were tested, 2 neural claims are blocked for missing data, and 7 model-classifier claims are blocked as "too large". That last blocking isn't supported: the notebook's own estimate is 56–115 min, so the 7 claims were never run.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| fig1k-example-temporal-widths | reproduced (depends on one reading) | Cell 10: the `code_half` window with the channel-mean curve gives 10/11 within tolerance, and crowd and water are narrower than fire. The two window readings the claims file names give at most 8/11, which would be partially reproduced. `code_half` comes from NeuralExample.m, which I could not see. Its 60.9 ms snake period fits S1 Text, which puts the first-half rattle at about 16.5 Hz. |
| fig1-snr-noise-stronger | partially_reproduced | Cell 12: no reading gets both means and ≥3 of 4 bounds. Several readings have both means within the SD tolerance and SNR mostly below 0 dB (e.g. whole (a)(d)(e): −11.8 / −8.1 dB, 100% / 85% negative). |
| fig1-s5-model-predicts-neural | blocked (data_missing) | The data set has no tone-pip responses, so no best frequencies. Agreed (see B6). |
| fig2-noise-restricted | reproduced | Cell 14: noise width at 50% is narrower for 5/5 sounds in both domains, under every window. The SD across sounds is lower for noise (spectral 0.33 vs 0.68; temporal 3.63 vs 48.67). |
| fig3a-example-tonotopy-removal | partially_reproduced | Cell 18: no reading has both values in tolerance (without tonotopy: 45.1, 31.3, 60.0, 30.0 against 35 ± 3.5). The drop is ≥20 points under every reading (20.0 to 40.0). |
| fig3a-example-classifier-order | partially_reproduced | Cell 20: the order st ≥ spec ≥ temp holds under 1a2b a(a), 1b2a and 1b2b a(a). The noiseless rule fails under every reading; noiseless temporal is 15–20 points below single-trial, not similar. |
| fig3b-population-above-chance | reproduced | Cell 22: under every reading, all four classifiers are above 20% (p ≤ 2e-5), 1 s beats 62.5 ms, and the tonotopy drop is 25–32 points (paired p ≤ 4e-5). |
| figs6-per-sound-above-chance | reproduced | Cell 24 (1a2a): 18/18 other conditions are above chance, and snake temporal is not (30%, p = 0.095). Snake without tonotopy is significantly *below* chance (12%, p = 0.012), where the paper has p = 0.92 (B5). |
| figs9-mixing-coefficient | reproduced (fragile) | Cell 44: only 1 of 16 reading combinations passes (1b2a, a chosen on validation data, P3 (a)): pooled median 0.70, exactly at the tolerance edge, and P3 0.50. Its quartiles are 0.40/0.90 against the paper's 0.5/0.7, and medians range from 0.0 to 0.9 across readings. |
| figs10-amua-tmua | blocked (data_missing), partly testable | tMUA needs raw voltages, which are absent. The two aMUA split-half values (0.98, 0.83) could have been tested (B2). |
| fig4-example-original-vs-equalized | not_reproduced | Cell 28: spectral 0.93 ± 0.02 is in tolerance. Temporal is 0.88–0.90 against 0.72 ± 0.07, outside both the tolerance and 10%, under every reading. |
| fig4e-population-original-vs-equalized | not_reproduced | Cell 30: 0/4 values in tolerance under every reading. Same-sound beats across-sound, but the temporal values are >10% off (e.g. 0.917 vs 0.80), so the partial rule fails. |
| fig4f-example-equalized-classification | partially_reproduced | Cell 32: the one reading with 4/4 in tolerance (eq_3a 1a2a a(b)) has the 1/f spectrum classifier at 31%, not <30%. The pattern (correlation classifiers >40%, spectrum <30%) holds under eq_3a 1a2b and eq_3b 1a2a/1a2b. |
| fig4h-population-equalized-classification | partially_reproduced | Cell 34: at most 3/5 values in tolerance (1/f spectrum classifier 29–30% vs 27 ± 1). The t tests pass and the spectrum classifier is lowest on 1/f under every reading. |
| fig8b-example-pca-variance | reproduced | Cell 36, reading b_st1000: 96.3% and 85.3–85.5%; nearest-centroid accuracy 88.6% / 85.6% (>80%). |
| fig8e-example-categorization | reproduced | Cell 40: under every reading, all three correlation classifiers are ≥90% at 1 s, rise from 62.5 ms, and the spectrum classifier is 91–94%. |
| fig8f-population-categorization | reproduced | Cell 42: 4/4 in tolerance, p < 1e-11 against 33.3%, and every classifier rises with duration, under every reading. |
| fig5-speech-water-widths | reproduced | Model cell 9, readings (ii)(a)(iii)(a): speech 64.5 ms, water 4.0 ms; spectral breadth 0.464 (speech) vs 0.259 (water). |
| fig6-category-half-widths | reproduced | Model cell 11, readings (ii)(a)(iii)(a): 4/5 in tolerance (cat 160.9 vs 117.3 is out), and every vocalization is wider than water and wind. Single bird songs' spectral breadth (0.273) is below wind's (0.315); the criterion doesn't test this. |
| fig6c-category-diversity | reproduced | Model cell 13, reading (c), norms not squared: 5/6 in tolerance (bird songs 0.373 vs 0.29 is out). Speech is lowest of the 13 categories and white noise is lowest overall. |
| fig7i-stationarity | not_reproduced | Model cell 15: environmental 0.65–0.79 vs 0.49 ± 0.04 and vocalizations 0.36–0.62 vs 0.28 under every reading. Speech is lowest and white noise highest, but the criterion has no partial clause. |
| fig9a, fig9b-similar-maximum, fig9b-accumulation-rate, fig9c, fig9e, fig9-spectrum-classifier-lower, fig10 | blocked as too_large, which I reject | Model cell 17 itself estimates 56–115 min for the whole notebook. The 195 sounds are in the archive and were read in 3 s, so these claims are testable and were simply not run (B1). |

Chance levels match the paper: 20% for five sounds, 33.3% for three categories. The 7.69% model chance level was never used.

**B. Problems**

1. **[affects a conclusion]** Model cell 17: the "too large" blocking contradicts the notebook's own estimate of 56–115 min, and no time limit is cited. The estimate also overcounts. In leave-one-sound-out, only the held-out sound's category model changes per fold, so about 195×3×10 fits are needed, not 195×13×3×10. Seven claims are untested.
2. **[affects a conclusion]** figs10: the aMUA split-half reliabilities (spectral 0.98, temporal 0.83) need only the aMUA rasters, which the data set holds. They were not computed, so part of the claim was blocked without cause.
3. **[affects a conclusion]** `S.correlation_readings` / cell 10: the fig1k "reproduced" outcome rests on `code_half`, a reading the author took from NeuralExample.m. The code is not quoted or shown, so I can't confirm it. Under the claims file's own window readings the outcome would be partially reproduced (8/11).
4. **[does not affect a conclusion]** Cell 44: figs9 passes under one combination, at the tolerance boundary. Paradigm 2's a is taken only from reading (3)(a) (`eq_3a`); reading (3)(b) was not run for this claim.
5. **[does not affect a conclusion]** Cell 24: snake without tonotopy comes out significantly below chance (p = 0.012), against the paper's p = 0.92. The criterion only asks "not above", so the outcome stands, but the notebook doesn't flag the mismatch.
6. **[does not affect a conclusion]** Cell 32, within-site test reading (b): the z test treats 500–1000 heavily overlapping windows as independent, which overstates significance. The partial verdict doesn't use it.
7. **[does not affect a conclusion]** `S.classify`, a chosen on model data (reading a): for the noiseless classifier it uses in-sample log-likelihoods. This gives a spectro-temporal accuracy of 60% while spectral alone gets 89.6% (cell 20, 1a2b), a sign of a degenerate choice. The noiseless rule fails on the temporal classifier anyway.
8. **[does not affect a conclusion]** `model.py`: the Methods bandwidth formula is used. The paper's code formula (94 + 71 f^1.5) is noted but not run as a variant, so whether it would close the large SI gap in fig7i is untested. The time step of tau_W/4 is the author's own choice; it is stated and reasonable for time averages.
9. **[does not affect a conclusion]** Cell 5: P2_Site08 has 13 trials where the claims file and paper say 14. Site counts per animal match (P1 4 + 9, P2 and P3 3 + 8).

Synthetic tests of the helpers all passed:
- On a known signal-plus-noise raster, `site_correlations` recovers the stimulus-driven fraction (0.563 against an expected 0.569), stimulus plus noise equals 1 on the zero-lag diagonal, and the lag-1 value matches.
- `width_at` gives the correct full width at half maximum of a Gaussian.
- `_acc_1b` / `_acc_1a` and the `temp_shuf` channel permutation behave as intended.
- Train and validation windows cannot overlap: windows plus lags stay inside each half.

**C. What I could not check**

- **The MATLAB code** (NeuralExample.m, rastermuashuffledxcorrwinfast.m, xcorrst.m, cochleogram.m). Without it I can't confirm the ports, the `code_half` reading, or the code's time step and bandwidth. Printing the relevant lines from the tar would settle this.
- **Whether the tar holds tone-pip or raw-voltage data.** The archive API lists only data.tar.gz, docs and checksums. The data description lists only RAS, Fs and Param (AnimalNo, RecordDate, BlockNo), and FigureData has no S5 or S10 entries. A full tar member listing plus every Param field name would confirm the two data_missing blocks. For fig1-s5, a version using an assumed tonotopic channel-to-frequency mapping would need an assumption the paper doesn't make, so I agree it is blocked.
- **Why fig4/fig4e temporal r is high.** Per-sound temporal r restricted to non-zero lags or per channel would show whether lag 0 drives the 0.90.
- **figs9's spread.** Per-site a values would show how spread out the distribution is.
