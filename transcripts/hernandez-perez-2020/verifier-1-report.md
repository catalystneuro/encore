**Verifier report, round 1: Hernández-Pérez, Cooper & Newman (2020) on CRCNS hc-27**

There are 24 claims in the claims file. My outcomes: 11 reproduced, 3 partially reproduced, 7 not reproduced, 3 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig2d-phase-shift-rate | reproduced | Cell 11, main reading: mean 27.32 deg/mm (target 26.36 ± 2.64). All six slopes are positive, T+ = 21, p = 0.031. All 12 runnable combinations pass. |
| fig2d-linear-fit | reproduced | Cell 14, reading (a) pooled: r² = 0.765 to 0.778, inside 0.7627 ± 0.0763. Readings (b) at 0.66 and (c) at 0.95 fall outside. |
| fig2a-all-rats | reproduced | Cell 16: 6 of 6 rats have a positive Hilbert slope, and the ventral-most cycle-triggered-average peak follows the dorsal one (18 to 40 ms). |
| fig2e-phase-locking-high | reproduced | Cell 18: counts, O3 c gives 0.946 (against dorsal) and 0.936 (all pairs), inside 0.85 to 0.95. Borderline: the main reading gives 0.963, which is outside, and `none` gives 0.79. |
| fig2e-phase-locking-decrease | reproduced | Cell 20: counts, O3 c gives a mean of −0.0675 (median −0.0619; −0.0705 without the dorsal point). All six slopes are negative, p = 0.031. Only O3 c passes; O3 a gives −0.039. |
| fig2c-coherence | reproduced | Cell 22: all pairs gives 0.677 to 0.690, inside 0.66 to 0.81. Against the dorsal-most electrode it is 0.61, which is outside. |
| fig2f-coherence-decrease | not_reproduced | Cell 24: the slopes are −0.21 to −0.22 per mm, about 3× the 0.067 ± 0.018 target. Direction and the test (p = 0.031) hold. 0 of 4 combinations pass. |
| fig2g-power-no-change | reproduced | Cell 26: relative power gives p > 0.0625 in 12 of 12 combinations (main p = 0.156). The median slope is −0.10/mm with CI [−0.22, 0.04], against the paper's +0.73 AU/mm. |
| fig3-along-not-across-layers | blocked (data_missing) | Confirmed against the archive (see problem 10). |
| fig4d-mua-phase-shift | blocked (data_missing) | Confirmed: the data are sampled at 500 Hz, so nothing above 250 Hz exists, and there are no layer II recordings. |
| fig4d-mua-matches-lfp | blocked (data_missing) | Needs the multi-unit slopes, and the dataset does not identify the three multi-unit rats. |
| fig5c-rise-decay-gradient | not_reproduced | Cell 28: dorsal −0.17 against −0.43 ± 0.14, ventral −0.05 against −0.11 ± 0.02. Direction and test hold (p = 0.031). 0 of 12 combinations pass. See problem 1. |
| fig5c-peak-trough-gradient | reproduced | Cell 30: dorsal 0.11 and ventral −0.04, both within the wide tolerances. Ventral is lower in all rats, p = 0.031. 12 of 12 combinations pass. |
| fig5-dorsal-sawtooth | reproduced | Cell 32: rise/decay T+ = 0, p = 0.031. Peak/trough p = 0.0625 exactly, because rat 1's value is exactly 0 and is dropped (n = 5). This passes, at the boundary. |
| fig5-ventral-rise-not-peak | reproduced | Cell 34: rise/decay T+ = 0, p = 0.031. Peak/trough p = 0.22, so no difference. The channel used is the ventral-most, at 2.26 or 2.83 mm. |
| fig6b-delay-by-phase | partially_reproduced | Cell 36: falling phase 5.86 and peak 11.82 ms/mm are both within tolerance, falling is the shortest, and p = 0.031. But the rising phase (12.53) is longer than the peak in every combination (4 of 6 rats in the main reading), so "peak longest" fails. |
| fig6c-delay-phase-slope | partially_reproduced | Cell 38: under counts, the slope is in range (pooled 0.0208, per-rat median 0.0194). R² = 0.67 to 0.69 is below 0.82 − 0.082. 0 of 8 combinations meet both parts. |
| fig6b-hilbert-between-limits | reproduced | Cell 40, counts: falling 16.9 and peak 34.1 deg/mm, both within tolerance, with the Hilbert value of 27.3 between them. Passes in 4 of 8 combinations; all four `none` combinations fail because the peak (26.0 to 27.0) is below the Hilbert value (27.7). |
| fig7-asymmetry-delay | not_reproduced | Cell 42: with theta epochs the values are 6.07 to 7.02 ms/mm, above the 5.89 upper bound. The main reading's p = 0.062 (one rat negative). It passes only under `none` (5.69), which drops the theta-epoch restriction the Methods require. |
| fig7-residual-delay | not_reproduced | Cell 44: 0 of 24 combinations pass. The total is within tolerance (9.4 to 11.8), but the residual is 2.0 to 5.2 against 9.61 ± 2.62. |
| fig8c-relative-delay-flat | not_reproduced | Cell 47: with the claims file's period (peak to next peak), the relative slope is significantly positive (+2.16 %/Hz, p = 0.031). Peak to previous peak gives a significant negative slope. Only the author's own `centred` variant gives no slope. |
| fig8d-absolute-delay-slope | not_reproduced | Cell 48: the main slope is +2.06 (wrong sign, p = 0.031). Only `none` + prev_period passes (−3.12), and that combination drops the theta epochs. With counts, prev_period gives −2.36, out of tolerance. |
| fig8-correlation-strength | not_reproduced | Cell 49: 0 of 48 combinations pass. The relative-delay \|r\| of about 0.16 to 0.37 is far above 0.02, and under the main reading relative > absolute. |
| fig8-coupled-oscillators | partially_reproduced | Cell 51: both slopes are significantly positive, so this is neither the coupled-oscillator nor the fixed-delay pattern. The criterion's "otherwise" gives partial, but neither of the paper's predictions holds. |

### B. Problems

1. **[affects a conclusion]** fig5c-rise-decay-gradient, a claims-file point to report, not correct. The Methods say log10, but the Figure 5A legend says only "log". Multiplying the notebook's main-reading medians by ln(10) = 2.303 matches the paper closely: rise/decay −0.39 and −0.11 (paper −0.43 and −0.11), peak/trough 0.25 and −0.09. The claims file did not list a natural-log reading. Under that reading the claim would pass.
2. **[affects a conclusion]** The `counts` unit reading (`mectw.Rat.scale`, cell 6). If the integer files are Intan ADC counts, as the notebook argues, a threshold of 400 counts is about 78 µV, not the paper's 400 µV. Rats 2 and 3 are rescaled by ×5.13 only because that makes the spreads match. This is stated as an assumption and is plausible, but the epoch definition changes outcomes: phase locking is 0.96 under `counts` and 0.79 under `none`, and fig7 and fig8d pass only under `none`. None of the paper's numbers was used to check the threshold. The paper's 3500 to 5000 cycles per rat is closest to O3 c (3200 to 6286, but rat 1 has 815).
3. **[affects a conclusion]** O2 reading (b) was declared impossible (cell 0, cell 6). The dataset's own docs (`docs/MEC-TW_authorProof.pdf`, supplementary figure 1) mark electrodes outside the MEC, and the descriptor points readers to it. The notebook did not consult it. Rat 1's dorsal-most channel has low theta (only 8% of time in epochs), so it may be outside the MEC. Excluding channels could change fig2e, fig2f and fig5c.
4. **[affects a conclusion]** fig8 (cells 46 to 49). The sign of every frequency relation flips between the next-peak and previous-peak periods. That points to a shared timing artefact between the per-cycle delay and the period, which the notebook acknowledges only by adding `centred`. The not_reproduced outcomes for fig8c, fig8d and fig8-correlation therefore rest on a definition the paper leaves open. They are not evidence against the paper's mechanism.
5. **[does not affect a conclusion]** In cell 36, fig6b checks "peak longest" only on the across-rat medians. A per-rat output would make the failure clearer: the rising phase exceeds the peak in 4 of 6 rats.
6. **[does not affect a conclusion]** Cell 39 says the two fig6b-hilbert readings coincide because the conversion is a constant factor. That holds for per-rat medians, but reading (b) is a median over pooled per-cycle values, which is a different statistic. Cell 40 also defines `hc` and never uses it; the Hilbert value always comes from O3 a.
7. **[does not affect a conclusion]** `mectw.signrank` drops zeros, so in fig5-dorsal-sawtooth n = 5 and p = 0.0625 is the smallest possible p. A zsplit or pratt zero treatment could push it above 0.0625. The outcome is fragile.
8. **[does not affect a conclusion]** `mectw.robustfit_slopes` keeps the previous iteration's beta for rows that have just converged. This is negligible. On synthetic data the slopes match statsmodels' Tukey RLM (8.834 with an outlier). `artefact_mask`, `theta_epochs` and `signrank` behaved correctly on synthetic input, and `extrema` (a) and (b) give the expected rise/decay index on a two-harmonic wave.
9. **[does not affect a conclusion]** Cell 4 holds dead "duplicates" code (`fp = {}` with a `pass` loop). The real duplicate check is in cell 5. The cycle-triggered average in cell 3 applies the artefact mask of channel 0 only.
10. **[does not affect a conclusion]** I checked the blocked claims against the archive. The S3 listing and `filelist.txt` show only `RawSignalTravelingWaveRats.zip`, holding six 5-to-6-channel, 500 Hz LFP files, plus two scripts and the docs. There is no broadband signal, no laminar site map and no geometry. fig3 and fig4d cannot be tested in any part. For fig4d-mua-matches-lfp, the per-rat LFP slopes exist, but the three multi-unit rats are not identified.

### C. What I could not check, and the output that would have let me

- **Whether ln explains fig5c (problem 1), and whether a half-delay explains fig7.** Delay_Asym as defined is a full duration difference. Peak displacement from asymmetry is about half of that, and half of 6.07 is about 3.0, which would match 3.56. The formula in the paper is explicit, so this is only a hint. A table of fig5c with natural log and fig7 with half the delay, shown as variants, would settle both.
- **Which channels lie outside the MEC.** A channel-by-channel reading of the author proof's supplementary figure 1, and a rerun of fig2 and fig5 without those channels.
- **Per-rat checks.** Theta amplitude in µV under each unit hypothesis, beside the 400 µV threshold. Per-rat phase-delay tables for fig6b. Per-rat sensitivity of the fig8 slopes to the reference-peak jitter, for example a delay measured from a trough-centred reference.
- **Figures.** No figure image was available to me, so I could not check per-rat values, the Figure 2G power measure, or which sites Figure 5C compares.
