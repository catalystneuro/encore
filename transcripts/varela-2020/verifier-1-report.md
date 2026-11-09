**Verification report: Varela & Wilson 2020 (eLife 48881) on CRCNS hc-24, round 1**

The claims file has 46 claims. Below, "n=5" means the 5 thalamic units in the deposit (S1 1, S2 2, S3 2). Only S1 and S3 have CA1 recordings, so SWR-based analyses have 3 thalamic units.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1s3-spindles-not-theta | not_reproduced | The sleep mPFC peak is at 10–11 Hz only after the author's normalisation; raw S3 power peaks at 4–8 Hz. The criterion needs the waking CA1 peak to be lower than in sleep, and it is not: S1 13 vs 11–12 Hz, S3 9–10 vs 9 Hz (cell 17). |
| fig2-swr-phase-delta-spindle | reproduced | Across-session means are 0.00 to 0.10 rad for delta and −1.57 to −1.75 rad for spindle. These are inside the tolerance in every reading. Only 2 sessions (cell 19). |
| fig2c-swr-around-kc | not_reproduced | No reading has all five values within tolerance. The SWR minimum falls 37–45 ms before the KC, where the paper has 10 ms after (cell 21). |
| fig3a-thalamic-rate-wake-sleep | partially_reproduced | Sleep rate is lower in 5 of 5 units, but p=0.0625, the smallest p possible at n=5. Waking 10.30 is within tolerance. Sleep 4.58 is just outside the band, whose lower edge is 4.64 (cell 25). |
| fig3a-bursting-in-sleep | partially_reproduced | Burst percentage is higher in sleep in 5 of 5 units (p=0.0625). The sleep fraction (80%) and both means are within tolerance. The waking fraction is 0% against a band of 22.5–27.5% (cell 25). |
| fig3a-bursting-around-swrs | partially_reproduced | The SWR-window means (18.9 and 19.9%) are within tolerance and above sleep in 3 of 3 units. Kruskal-Wallis p=0.177 (cell 25). |
| swr-shift-control | partially_reproduced | Fewer spikes at SWRs in 2 of 3 units; burst % higher in 2 or 3 of 3. With 3 units the Wilcoxon p cannot go below 0.25 (cell 31). |
| fig3c-thalamic-decrease-at-swrs | not_reproduced | The direction fails. Pure increase is the largest class (2 of 3 units, both in S3) and decrease covers 1 of 3. The criterion needs decreasing units to be the largest group (cell 35). |
| fig3s1-ca1-mpfc-at-swrs | partially_reproduced | 100% of CA1 units increase (13/13) and mPFC has both increasing and decreasing units. The CA1 mean z (20.8) and the mPFC increase fraction (28.6%) are within tolerance. CA1 100% (band ends at 99.2%) and mPFC decreasing 71% are outside (cell 37). |
| glm-thalamus-anticorrelated-swrs | not_reproduced | 1 of 3 units has a significant negative coefficient; 1 is significantly positive. The change is 10.3% against 20.74 ± 2.07; the MUA variant gives 0.5–1.5% (cell 39). |
| glm-re-versus-other-nuclei | blocked (metadata_insufficient) | Confirmed. No file or the data description gives a nucleus per unit. |
| fig3e-thalamic-rebound-after-kc | partially_reproduced | Mean after-peak is above before-peak in all readings, but only 2 of 5 units have after > before. Three of four values are within tolerance; the before z of 1.42 is outside 1.28 ± 0.128 (cell 45). |
| kc-trough-timing | reproduced | Thalamus 42–54 ms and mPFC −6 to −47 ms are within the wide tolerances, and the thalamic minimum is later in every reading (cell 47). |
| kc-fraction-of-thalamic-peaks | partially_reproduced | The notebook marks this blocked, but under the methods KCs with disjoint groups: after only 40% (in band), both 20% (in band), before only 20% (out), and more units peak after than before. With the deposited KCs it is a 40/40 tie (cell 49). |
| kc-ca1-mpfc-symmetric | partially_reproduced | CA1 before and after are within tolerance in all readings. mPFC is outside in every reading except one before value, driven by the single S3 unit with after z 9.4 (cell 51). |
| kc-regions-compared | partially_reproduced | The after-KC absence holds (Kruskal-Wallis p 0.64–0.74). The thalamic median is lowest before KCs, but p is 0.18–0.25 where the criterion needs < 0.05 (cell 53). |
| fig3f-asymmetry-index | reproduced | Under index readings (a) and (b) all three means are within tolerance and the thalamic mean is positive (0.07–0.12). Three of the 5 thalamic indices are negative, and Wilcoxon p=0.81 (cell 55). |
| spindle-mua-modulation | not_reproduced | The notebook marks this blocked, but the order CA1 > mPFC > thalamus fails. All mPFC tetrodes pass, as do all CA1 tetrodes, and the strongest modulation is in mPFC (z 22–32). CA1 at 100% is out of band (cell 57). |
| fig4-units-not-rhythmic | not_reproduced (unreliable) | The outputs fail: Mann-Whitney p ≥ 0.69 and MUA in-band 14–19% against 63%. But the peak finder has a bug (problem 1) that pushes MUA lags to the second cycle, so this does not test the claim. |
| fig4b-thalamic-pairs-correlated | not_reproduced | Mean peak z is 4.56 or 7.24 against 2.40 ± 1.21, and both pairs exceed 3 sd. These are 2 deposited example pairs (cell 61). |
| xcorr-stronger-in-spindles | partially_reproduced | In-cycle z is above between-spindle z in 2 of 2 pairs, and the between value (2.98) is within tolerance. The in-cycle value (6.75) is outside, and the test cannot be run with 2 pairs. See problem 6 (cell 61). |
| fig5c-spindle-phase-locking | partially_reproduced | Circular mean 1.18 rad (reading a) is within tolerance, and all 5 units have a positive mean phase. The significant fraction is 60% against a band of 60.97–74.51% (cell 67). |
| fig5c-delta-phase-locking | partially_reproduced | Means of −0.32 and −0.08 rad are within tolerance. The significant fraction is 80% against 64.52 ± 6.45 (cell 67). |
| phase-robust-to-spike-count | reproduced (uninformative) | p is 0.31–1.0 in both bands, but with n=5 the smallest possible p is 0.0625, so the test cannot reject (cell 71). |
| rebound-delta-phase-trend | reproduced (by the letter) | Reading (i)(a) gives r=−0.011 (p=0.99) after and p=0.17 before, which meets the criterion. That r is about 0 and does not reproduce the paper's r=−0.32 trend (cell 73). |
| fig5d-phase-lags-consistent | blocked (other) | Confirmed: both pairs count as correlated, so there is no uncorrelated group. The correlated-pair sd (2.33–2.36) is within 2.15 ± 0.215 (cell 75). |
| spindle-cycles-by-ripple-power | partially_reproduced | High-power cycles are shorter in 1 of 2 sessions and larger in 2 of 2 with the deposited troughs. Durations of 99–101 ms are mostly below the tolerance band. Amplitudes are within tolerance. Across-session p cannot fall below 0.33 (cell 77). |
| fig6-modulation-with-ripple-power | partially_reproduced (unreliable) | Deposited reading: 2 of 3 units (66.7%) are in band; the methods and results readings give 33%. The 22.58% subset is never computed, and the modulation index is biased (problem 2). |
| modulation-amplitude-versus-ripple | blocked (other) | With n=3 the Wilcoxon p cannot go below 0.25, and the claim is a contrast of significance. The notebook computes no tests (cell 79). |
| fig6e-quartile-synergy | blocked (other) | Same as above. None of the claim's percentages or tests are computed. |
| fig6f-quartile-versus-median | blocked (other) | Same as above. None of the claim's percentages or tests are computed. |
| fig6g-spike-count-unchanged | reproduced (uninformative) | With n=3 neither test can reach significance. No test or median difference was printed, and with the deposited troughs spikes per cycle are higher in high-power cycles in 3 of 3 units (cell 79). |
| xcorr-pairs-ripple-modulation | blocked (other) | Cell 89 says one S3 pair can be tested, then computes nothing. |
| thalamus-at-spindle-nested-swrs | partially_reproduced | All four means are within the wide tolerances. The 1 s decrease appears in the deposited and results means but not in the methods reading. Tests are impossible at n=3 (cell 93). |
| mpfc-units-coupled-swrs | reproduced | Wilcoxon p is 0.30–0.81 with n=7, and the values are within tolerance (cell 95). |
| mua-coupled-swrs | partially_reproduced | Coupled > uncoupled for CA1 in 3 of 3 tetrodes and mPFC in 2–3 of 3; thalamus shows no consistent change. With 3 tetrodes p cannot go below 0.25 (cell 97). |
| maze-swr-kc-increase | blocked (data_missing) | Confirmed from the zip directory: there is no sleep before the maze. |
| maze-control-sessions | blocked (data_missing) | Confirmed: the control sessions are absent. |
| maze-ripple-power-in-spindles | blocked (data_missing) | Confirmed: there is no sleep before the maze. |
| fig7c-run-units-in-spindles | partially_reproduced | The ripple-power main effect is significant (p 0.001–0.017) and run units have higher means. The run effect is not significant: Mann-Whitney p ≥ 0.2, ANOVA run p ≥ 0.12 (cell 105). |
| maze-ca1-rates-similar | reproduced | Mann-Whitney p = 0.34 and 0.20 (cell 107). |
| fig7d-run-units-peri-swr | partially_reproduced | Both peak values are within tolerance and run > not-run, but Mann-Whitney p=0.057. Nested vs other SWRs gives p ≥ 0.125 (cell 109). |
| fig7b-run-units-spindle-phase | partially_reproduced | The run-coupled group has the highest Z in most readings, and the circular mean (−1.37 for spikes within ±50 ms of each SWR) is within tolerance. Neither ANOVA main effect is below 0.05 (cell 111). |
| fig8-thalamus-unchanged-by-maze | blocked (data_missing) | Confirmed. |
| fig8e-ca1-spindle-trend | blocked (data_missing) | Confirmed. |
| thalamus-not-selective-for-run-cells | blocked (other) | The co-modulated pairs need maze spikes, which are absent. The run vs not-run cycle comparison could be run with the 2 S3 thalamic units but was not. |

### B. Problems

1. **[affects a conclusion]** Autocorrelogram peak finder, `ac_peak` in cell 59. It takes the global minimum within 0–200 ms (`argmin`), where the criterion says the minimum that follows lag 0. On a synthetic 10 Hz process it returns a 200 ms peak, after a 150 ms minimum. The real MUA lags of 185–243 ms against the paper's 119 ms are consistent with this. The fig4 outcome is not valid until this is fixed.
2. **[affects a conclusion]** Modulation index, `mod_index` in cell 79. It smooths a ±100 ms histogram with `np.convolve(..., mode="same")`, so the edge bins are pulled toward zero. Flat Poisson firing gives an index of 0.39 where it should be about 0. The fig6, modulation-amplitude-versus-ripple, fig6e and fig6f indices are dominated by this artefact. The histogram should be smoothed over a wider range and then cropped.
3. **[affects a conclusion]** Status table in cell 0. It marks about 15 claims "Blocked: other" even though their outputs exist and the claims file's "Unit samples" paragraph says to compare values and judge direction on the subset. Some of these meet the criterion in part: kc-fraction (2 of 3 values in band) and fig6 (in band under the deposited reading). fig5c-spindle is blocked while fig5c-delta is tested, although both have the same 20% granularity. Cell 67 also says the delta band "holds 60%", but the observed fraction is 80%.
4. **[affects a conclusion]** Quantities the criteria need were never computed:
   - the fig6 22.58% subset;
   - all fig6e and fig6f quantities and tests;
   - xcorr-pairs-ripple-modulation for the one available pair;
   - the fig6g Wilcoxon tests and median differences;
   - the first part of thalamus-not-selective-for-run-cells.
5. **[affects a conclusion]** M-sleep readings (b) and (c), the author's own sleep detection, were not run; only the deposited sleep periods are used. fig3a's sleep rate of 4.58 sits 0.06 below the tolerance edge, so the sleep definition could change that outcome. M-KC and M-SWR reference reading (b) were not run either, though the module docstring describes it. That one probably does not matter, since the KC counts agree with the deposit.
6. **[affects a conclusion]** xcorr-stronger-in-spindles, cell 61. Both spike trains are restricted to the same roughly 100 ms cycles, which by construction puts extra pairs at short lags. Both z readings are inflated for in-cycle spikes. No control was run, for example cycle-shuffled trains.
7. **[does not affect a conclusion]** `circ_kappa` with the bin-spacing correction gives kappa ≈ 125 for sparse histograms (cell 111, methods reading). Kappa is not used in any criterion.
8. **[does not affect a conclusion]** Phase bins `-pi:0.2:pi` drop phases in (3.058, π], about 1.3% of the circle at the trough. The Rayleigh test uses left bin edges while the mean uses bin centres. This follows the deposited script, as the notebook states.
9. **[does not affect a conclusion]** In cell 39 the notebook writes "b1' = 0.25 b1"; the correct relation is 4·b1. The conclusion is still right: the claims file's readings (i) and (ii) are algebraically the same number. That is a flaw in the claims file, not a misreading of the paper.
10. **[does not affect a conclusion]** Weak criteria in the claims file. rebound-delta-phase-trend is met by r = −0.01 at n=5, because the criterion sets no minimum size for r. phase-robust-to-spike-count and fig6g are absence tests that cannot reject at n ≤ 5.
11. **[does not affect a conclusion]** S3 has no full deposited SWR list, so its "dep" SWRs are the k=3 detection and the dep and methods readings are not independent for S3. The notebook states this. fig1s3 "waking" is all time outside the non-REM periods, which includes REM. swr-shift-control uses one random shift per SWR.

### C. What I could not check

- **Deposited scripts.** I could not read the `.mlx` scripts without downloading the dataset. The S1 unit as MD, the S2 units as thalamic, and the binning and normalisation taken from `PhaseLockingCA1UnitsPFCSpindles.mlx` remain unverified. A cell quoting the relevant script lines would settle this.
- **fig4 on real data.** I confirmed the bug only on synthetic input. Needed: per-curve autocorrelograms with the first local minimum marked, and the lags recomputed with it.
- **Size of the modulation-index bias.** Needed: the indices recomputed from a ±1 s smoothed histogram cropped to ±100 ms, plus a flat-firing baseline.
- **Uncomputed claim quantities** (problem 4). Each needs its own output: the 22.58% subset, the fig6e/fig6f percentages and the Spearman correlation, the single pair's change in correlogram modulation, and the run vs not-run thalamic peri-spindle comparison.
- **Sleep-definition sensitivity.** Needed: fig3a rates under the author-detected sleep periods (1 s and 10 s windows).
- **The S3 mPFC epoch.** The S3 mPFC unit and MUA start at 11750 s, 1450 s before the LFP. Only mPFC streams cover that epoch, so it cannot serve the maze claims. Its identity is unknown, and a check against the descriptor's authors would settle it.
- **Figures.** I did not view the rendered figures, only their printed value ranges.
