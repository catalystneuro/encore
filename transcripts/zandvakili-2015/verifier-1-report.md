**A. Outcomes** (26 claims in the claims file. The notebook tests 14 and marks 12 blocked.)

| claim | my outcome | reason |
|---|---|---|
| fig4c-broad-ccg-peaks | reproduced | Under both readings, 31 of 31 site-average shuffle-corrected CCGs have a broad peak, at sites with (16 of 16) and without (15 of 15) a narrow peak. The width above the flank mean is 68 ms (cell 10). |
| fig4c-narrow-peak-sites | not_reproduced | 16 of 31 sites, fraction 0.516, against 0.206 ± 0.021 (cell 8). It stays outside at 4, 5 and 6 SD (13 of 31 at 6 SD) and with the 25 ms jitter (0.710). The criterion notes that site sampling may differ. |
| fig4-narrow-peak-depth | blocked (data_missing) | The descriptor and the archive listing have no V2 depth and no layer 6/WM reference. |
| fig5a-rf-alignment | blocked (metadata_insufficient) | No pixel-to-degree scale exists in the paper or the data set. The scale-free part holds: probability falls steadily with offset in pixels, from 1.65% in the first bin to 0 beyond 100 px (cell 22). |
| fig5-narrow-pairs-rare | not_reproduced | 171 of 16,308 pairs, 0.0105, against ≤0.0039 under either target (cell 13). Still 0.0059 at 6 SD. Per session it ranges from 0.0028 to 0.018. |
| fig5b-v1v2-latency | not_reproduced | The offset is positive and significant: Wilcoxon p = 7e-20, sign test p = 2e-29. But the median is 2.0 ms (2.30 interpolated) against 2.8 ± 0.28. The width is 3.89 ms smoothed and 3.09 ms unsmoothed, both outside 3.71 ± 0.1 (cell 15). The criterion needs the median within tolerance. |
| fig5b-intra-areal-zero-lag | partially_reproduced | Both medians are 0.0 ms. V2-V2 shows no difference under either test (p = 0.86 and 0.70). V1-V1 differs under the Wilcoxon reading (p = 0.016) but not under the sign test (p = 0.076), so only reading (b) matches (cell 17). |
| figs3-efficacy | not_reproduced | Reading (a): median 0.324% against 0.39 ± 0.039, mean 0.496% against 0.69 ± 0.12. Reading (b) is far off: 6.5% raw, 0.82% shuffle-corrected. Using all significant pairs gives 0.334% and 0.494%, also out (cell 19). |
| fig6a-coordination-before-v2 | reproduced | Spike divergence is above control at 6 of 6 windows under every reading (main, e-b2, e-b3, s-b, r-b, d-b) and under both p-a and p-b (cell 24). |
| fig7a-threefold | not_reproduced | The ratios are 1.56 to 2.14. Geometric means are 1.79 to 2.00 and medians 1.80 to 2.01. Reading (c) puts at most 3 of 5 windows in range. Only e-b3 with the median summary (2.011) reaches the edge of the 2 to 4 range (cell 27). |
| fig7a-above-shuffle | reproduced | In all four shuffle and epoch readings, both lower bounds are above the shuffled value at 5 of 5 windows (cell 29). The margin is thin at 5 ms under (a, d): 2.013e-4 against 2.006e-4. |
| fig6b-not-after-v2 | not_reproduced | Every reading has a significant window after the spike. Under the main reading, 80 ms gives p-b = 0.004, and p-a = 0 at both 40 and 80 ms (cell 31). |
| fig6-slow-both-sides | reproduced | At 1280 ms, spike divergence is above control both before (ratio about 2.4) and after (about 2.0) the spike, p = 0 under all readings (cell 33). |
| fig7d-time-course | partially_reproduced | The peak is at 2.5 ms (reading a) or 3 ms (reading b) before the spike at every window. Under p-b, the 80 ms window still has Bonferroni-significant epochs after the spike and more than 8 ms before it. Under p-a, every window does (cell 35). |
| fig7b-nonmiddle-no-coordination | blocked (data_missing) | Confirmed: there is one site per V2 electrode per session and no depth or penetration order. |
| fig7e-nonmiddle-time-course | blocked (data_missing) | Same reason as fig7b. |
| fig7c-offset-rf-no-coordination | blocked (data_missing) | Confirmed: no depth and no degree scale. Also, no V1-V2 RF offset in the data exceeds 200 px (cell 22). |
| figs2a-v2-single-units | blocked (data_missing) | Confirmed: there are no waveforms or SNR. The descriptor says the units mix single units and multiunit activity. |
| figs2b-v1-single-units | blocked (data_missing) | Same reason as figs2a. |
| figs4-partner-not-needed | reproduced | Both subsets are above control at 5 of 5 windows under p-a, and at 5 and 4 of 5 under p-b. The ratio is larger with a V1 partner at 5 of 5 windows: 1.9 to 2.3 against 1.3 to 1.7 (cell 37). Only the main reading was run. |
| figs5-middle-layer-relay | blocked (data_missing) | Confirmed: it needs superficial and deep sites, and there is no depth. |
| fig1-ffn-propagation | blocked (other) | Not attempted. The data is a simulation, and the claims file gives a rerun criterion. |
| fig3-divergence-correlation | blocked (other) | Same as fig1. |
| figs1-higher-order | blocked (other) | Same as fig1. |
| fig8-architecture | blocked (other) | Same as fig1. |
| rf-sizes | blocked (metadata_insufficient) | RF fits are in pixels with no scale. The scale-free V2/V1 diameter ratio is 1.97 against the paper's 1.88 (cell 21). |

**B. Problems**

1. [affects a conclusion] Cells 0 and 38: the four simulation claims are blocked as "not_runnable", which is not an allowed reason. The claims file gives a rerun criterion for each and only "data: elsewhere", so nothing blocks them except that they were not attempted. They should be marked blocked (other: not attempted), not shown as untestable.
2. [affects a conclusion] Cells 31 and 35: the paired bootstrap (reading p-a) flags differences at offsets 10 to 15 ms from the spike, at every window. No null check shows whether it is calibrated, for example two independent control-epoch sets compared with each other. The fig6b outcome (p-b alone still fails at 80 ms) and fig7d (still partial under p-b) do not change, but the p-a results are not interpretable without that check.
3. [does not affect a conclusion] Cell 17: the V1-V1 Wilcoxon result depends on the claims file's pair order (unit-list order). The mean offset is 0.10 ms, so this is an ordering asymmetry, not a lead. Also, 141 of the 249 significant V2-V2 pairs share a tetrode. Excluding them makes V2-V2 significant under both tests (p = 0.030 and 0.033). The claims file says all pairs, but this sensitivity is worth reporting.
4. [does not affect a conclusion] `session_divergence` and `state_hist`: 1 ms spike times smear the 1.5 to 3.5 ms epoch to about 1 to 4 ms, and e-b has no 2.5 ms bin, so e-b2 and e-b3 stand in for it. This may dilute the spike-epoch divergence and lower the fig7a ratio. The data force it, but the notebook does not mention it for the divergence analyses.
5. [does not affect a conclusion] `gauss_smooth` with 1 ms bins: smoothing a single bin alone gives a FWHM of 3.54 ms (I tested this), so the fig5b width test has little room. The unsmoothed width is limited by the bin size. Likewise, "offset above 1 ms" in cell 19 means a lag of 2 ms or more.
6. [does not affect a conclusion] Cells 35 and 37: fig7d and figs4 are run only under the main reading, although the header asks for every reading. Cell 35 uses 2000 draws instead of 5000; Bonferroni at 0.05/30 can still be resolved with that many.
7. [does not affect a conclusion] Cell 35, `judge_tc`: centre −0.5 (bins −1 and 0) counts as "after", though bin 0 is simultaneous with the spike. Under p-b the 80 ms window fails on other offsets anyway.
8. [does not affect a conclusion] Cell 29: the bootstrap lower bound is compared with a single shuffle and jitter realization, whose own variability is not estimated. The 5 ms (a, d) margin is 0.3%.
9. [does not affect a conclusion] `jitter_events`: the jitter pool includes the spike's own trial, while the claims file says "other trials". The notebook states this choice, and its effect is about 1 in 400.
10. [does not affect a conclusion] Cells 21 and 22: the mapping from rfInfo row to electrode code minus 1 for V1 is assumed without a check, and two-eye sessions use eye 1 only. Both cells are for information only.
11. [does not affect a conclusion] Cells 8 and 13: the site and pair fractions are about 2.5 to 3.5 times the paper's. That fits a deposit drawn from sessions sampled more toward middle layers, but the notebook does not examine it.

Checks that passed:
- Helper functions on synthetic inputs: the CCG lag sign (V2 after V1 is positive), the jitter expectation (counts per window preserved), `jitter_events` (same window, same-stimulus pool, early spikes kept), `control_trials` (never its own trial, same stimulus), `js_bits`, `pop_counts`, `half_width`, both bootstrap p functions under the null, and the Equation 1 normalization.
- Every number in the outputs derives from the loaded data.
- The clock and orientation checks in cell 5 are sound.

**C. Not checked, and the output that would allow it**

- That the .mat files hold no fields beyond the descriptor's (depth, SNR, penetration). Printing `neuralData.dtype.names` and the distribution of unitCodes sort codes would show this; sort codes might also give a proxy for single units in figs2a and figs2b.
- Calibration of p-a and p-b. A divergence comparison of control against a second independent control set, per window, would show it.
- The V1 rfInfo channel mapping. A plot or printout of V1 RF centre against electrode code (a smooth layout across the grid) would confirm it.
- Spread of the shuffled-data divergence. Several shuffle realizations per window would give it.
- fig7d and figs4 under the s-b, r-b, d-b and e-b readings.
- I read only the text outputs, not the rendered figures.
