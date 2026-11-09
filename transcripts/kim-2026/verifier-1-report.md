A. Outcomes per claim (43 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig2a-threshold-decrease | reproduced | Cell 9, psignifit: early median 5.41 uA (tolerance 4.95–6.05), late 3.84 uA (3.78–4.62), p = 5.4e-6, late lower. The late median clears its bound by only 0.06 uA, and the MLE variant (mu and x50 both 3.68) falls outside it (problem 1). The late n of 89 is just over the expected 80 ± 8; the criterion does not judge on n. |
| fig2a-steepest-decline-early | reproduced | Cell 11, psignifit week medians: the week 0→1 fall is 1.77 uA, the largest later change 0.85. This depends on the fit: the MLE x50 medians give 1.16 for weeks 0→1 against 1.27 for weeks 1→2, which reverses it (problem 1). |
| figs1e-response-times-decrease | reproduced | Cell 13: the median over mice falls from 274.9 ms (week 0) to 193.9 ms (late), and 93% of that fall is between weeks 0 and 1. Variant MWU p = 7e-17. |
| figs5c-wheel-onset-decrease | reproduced | Cell 15, threshold per animal: Mouse 1 119 ms, all hits 133 ms, late 128 ms, all within tolerance; early against late p = 6e-32, late earlier. n = 1307/2897 against the paper's 1305/2922. |
| fig4-unit-counts | not_reproduced | Cell 19: 795 units, 584 pyramidal, 204 interneurons, 488 modulated (339 pyramidal, 146 interneurons). Only 2 of 6 counts are within tolerance (modulated, modulated pyramidal); the all-55-sessions variant gets 3 of 6. |
| figs3b-modulation-increase-all | reproduced | Cell 21: late higher at 4, 5 and 6 uA (p = 9.6e-5, 0.0066, 4.0e-4). n is close to the paper's (191/738, 284/498, 300/256). |
| figs3c-latency-all | not_reproduced | Cell 23: the 5 uA test holds (p = 0.0052), but 4 uA is also significant (p = 0.0465). The criterion requires P ≥ 0.05 there. |
| figs3d-modulation-stable-at-threshold | reproduced | Cell 25: reading (a) p = 0.24, reading (b) p = 0.61. The criterion picks (a) as "the reading whose n matches", but its n (42/87) does not match the paper's 21/34. |
| fig4g-modulated-count-mouse1 | reproduced | Cell 27: Mouse 1 one-sided p = 0.0443, n = 8/21, r = 0.42, matching the paper exactly. The group-level test is not significant (p = 0.073). |
| fig4ij-pyramidal-modulation-increase | reproduced | Cell 29: z rises at all three currents (p ≤ 9e-4). Time to maximum falls at 5 uA (p = 3e-4) and 6 uA (p = 0.025). |
| fig4ij-interneurons-little-change | reproduced | Cell 31: z gives p = 0.33, 0.88, 0.089. Latency is significant only at 6 uA (p = 0.034, r = 0.19; the paper has p = 0.010, r = 0.21). |
| fig5d-pulse-locking-stable-across-currents | reproduced | Cell 33: 0.842 of pairs keep their identity (> 0.80); 740 pairs against the expected 729 ± 73. |
| fig5e-pyramidal-fraction-pl | partially_reproduced | Cell 35, stored labels: PL 0.747 and NPL 0.536 are both within tolerance, Fisher p = 4.9e-5. Under the criterion's own cell-type rule (trough-to-peak, the variant), NPL is 0.582, outside 0.448–0.548 (problem 3). |
| figs4b-pl-latency-distance | not_reproduced | Cell 37: the latency slope is negative at 4 uA (p = 0.02) and flat at 5 and 6 uA under both readings, so no velocity can be computed. The result rests on a channel-to-position mapping that is unverified (problem 4). |
| fig5fg-pl-modulation-increase | partially_reproduced | Cell 39: modulation rises at all three currents (p ≤ 0.0017). Time to maximum falls at 5 uA (p = 0.0046) but not at 6 uA (p = 0.080). The criterion's partial clause does not cover this case; I judged it partial. |
| figs4de-npl-no-change | not_reproduced | Cell 41: NPL z at 4 uA gives p = 0.042, and any P < 0.05 is not reproduced. NPL n is about half the paper's (32/151 against 53/260), see problem 2. |
| fig5h-pl-spike-probability-increase | not_reproduced | Cell 43: 6 uA holds (p = 0.036), but 5 uA does not (p = 0.86). |
| figs5-restricted-window-consistent | reproduced | Cell 45, reading "keep": PL z rises at all three currents (p ≤ 0.0022) and NPL z is not significant at any (p = 0.069, 0.56, 0.59). PL time to maximum is significant at 4 and 5 uA but not 6 uA, as in the paper. |
| fig6c-kl-divergence | not_reproduced | Cell 47: median KL falls from early to late for PL (0.040→0.036) and NPL (0.36→0.33) under both k1 and k2. NPL > PL holds in both phases. |
| fig6d-npl-hit-miss-divergence | not_reproduced | Cell 49: PL has significant clusters in both phases under every reading. The early NPL onset is 95–615 ms against the paper's 65 ± 10. |
| fig6f-population-coupling | reproduced | Cell 51: PL rises (FDR p = 0.0016), NPL is stable (p = 0.49), and NPL > PL in both phases (p ≈ 3e-12). |
| figs9a-coupling-700ms | reproduced | Cell 53, reading (a): PL rises (p = 2e-5), NPL is stable (p = 0.48), NPL > PL in both phases. Reading (b) gives the same pattern. |
| figs9-coupling-window-and-control | partially_reproduced | Cell 55: in the 120 ms window NPL > PL in both phases (FDR p = 2e-7 and 1e-12). The control half is blocked (methods_underspecified): the control ephys exists, but the trains differ (problem 6). |
| fig2c-count-increase-fixed-current | blocked (metadata_insufficient) | The archive's variableMeasured has no image series, so there are no voxel volumes, no stimulation-site position and no activation calls. Only per-ROI dF/F and masks are stored. An ROI-level approximation would be the author's own method. |
| fig2b-example-counts | blocked (metadata_insufficient) | Same as fig2c. |
| figs2ab-density-peak-200um | blocked (metadata_insufficient) | Needs distances; same as fig2c. |
| fig2e-density-200um-increase | blocked (metadata_insufficient) | Same as figs2ab. |
| fig2e-radius-increase | blocked (metadata_insufficient) | Same as figs2ab. |
| figs2de-behaviour-increase-comparison | blocked (metadata_insufficient) | Same as fig2c. |
| fig2g-stable-at-threshold | blocked (metadata_insufficient) | Same as fig2c. |
| figs2de-control-stable | blocked for density only; the count half was testable | The control files store per-ROI binary activation per channel and current (cell 57), which are the paper's own calls. Only the density half needs positions and voxel size (problem 5). |
| fig3b-tracking-counts | blocked (metadata_insufficient) | No cross-session ROI identity is stored. The paper's matching aligns average prestimulus images with PatchWarp, and the archive lists no image data. |
| fig3df-stable-cells-amplitude-duration-onset | blocked (metadata_insufficient) | Same as fig3b. |
| fig3i-more-high-intensity-week4 | blocked (metadata_insufficient) | Same as fig3b. |
| fig3j-high-intensity-subgroup-increase | blocked (metadata_insufficient) | Same as fig3b. |
| fig3j-weekly-divergence | blocked (metadata_insufficient) | Same as fig3b. |
| fig3lm-deconvolved-spikes-subgroup | blocked (metadata_insufficient) | Same as fig3b. |
| fig3n-newly-recruited-weaker | blocked (metadata_insufficient) | Same as fig3b. |
| fig3n-enhanced-vs-week0 | blocked (metadata_insufficient) | Same as fig3b. |
| figs6-first-five-frames | blocked (metadata_insufficient) | Same as fig3b. |
| fig4d-waveform-separation | blocked (data_missing) | The files hold one single-channel mean waveform per unit (cell 7), with no waveforms in and out of stimulation. |
| figs7-control-no-change | blocked (methods_underspecified) | The control ephys is present, and its 4 animals and 15 ecephys files match the paper's n. But the trains are 3 bursts of 10 pulses at 50 Hz, while the paper says "similar stimulation parameters", so the 10 ms interpulse PL method is undefined. Modulation and time to maximum could still have been tested (problem 6). |
| figs8-tracked-units | blocked (data_missing) | No multi-channel templates and no tracked-unit labels. |

B. Problems

1. [affects a conclusion] Cell 9 and `fit_psignifit`: the coarse psignifit grid is called "a standard choice that cannot change an outcome". It can:
   - The late median sits 0.06 uA inside its tolerance.
   - The MLE fit, with either mu or x50, puts the late median outside it (3.68 against a bound of 3.78).
   - Under MLE x50 the fig2a-steepest result reverses (1.16 against 1.27).
   - The criterion's "current at 50% detection of the fitted function" is x50, which was not computed from the psignifit fit.
   - The default grid was not run.
2. [affects a conclusion] `pulse_locking`, PL/NPL split: the notebook finds 80% of responses PL (1806/2267), against about 66% in the paper; NPL n is about half the paper's (figs4de, figs5, fig6f). On synthetic data the PLI-versus-uniform-surrogate call:
   - has a 2.5–3% false-positive rate at 20–60 Hz, against a nominal 1%;
   - calls 99% of responses with a monotone rise across the interpulse interval and no locked peak "PL".
   
   Latencies reach 8.76 ms, close to the last unblanked bin, so some PL calls are of this ramp type. That would also flatten the figs4b latency-distance fit. The distribution of peak bins was never examined. Affects fig5fg, figs4de, fig5h, figs4b, fig6c/d/f and figs9a.
3. [affects a conclusion] Cells 19 and 35: cell type comes from the stored `cell_type`, not from the criterion's trough-to-peak rule (the two disagree for 72 of 795 units, cell 7). Under the rule, fig5e's NPL fraction (0.582) misses tolerance. fig4ij was not rerun under the rule.
4. [affects a conclusion] Cell 37 (figs4b): distance is the 1-D gap between `unit_y_um` and the `rel_y` of the electrode whose `channel_name` equals `stim_channel`. That the two use the same numbering is assumed and never shown. The notebook's own check (modulated fraction against distance) shows no fall-off near the contact, which does not support the mapping.
5. [affects a conclusion] Header and cell 57: figs2de-control-stable is blocked as a whole. The stored control activation calls allow the count test (early against late, 5 uA and pooled); only density needs the stimulation-site geometry.
6. [affects a conclusion] figs7 and the control half of figs9: modulation z and time to maximum over the 200 ms bursts could have been tested under a stated assumption. Separately, the mismatch between the control trains (50 Hz bursts) and the paper's "similar stimulation parameters" is worth reporting.
7. [does not affect a conclusion] `load_session`: the `accepted` unit flag is loaded but never used. If it marks rejected units, they enter every ephys analysis.
8. [does not affect a conclusion] Mouse 6 has no catch trials, so its fits lack the 0 uA point. Without Mouse 6, fig2a still holds (5.21 against 3.94, p = 7e-5).
9. [does not affect a conclusion] Cell 49: the label permutation swaps hit and miss rows within each response. This is a stated assumption, and on synthetic heterogeneous rows it was not anti-conservative (family-wise error rate 0 in 20 null runs). The bin-to-bin sign alternation of late PL clusters in 10 ms bins is unexplained.
10. [does not affect a conclusion] `channel_days` counts days over weeks 0–4 only; only two ICMS101 channels are dropped either way.
11. Checked and correct: `mwu` sign, `fdr_bh` (against a reference implementation), `time_to_max` (synthetic 300 ms peak gives 295 ms), week assignment, train selection. Weeks 0–4 give 46 sessions, matching the paper. No number in the notebook is hard-coded.

C. What I could not check, and the output that would have let me

- PL validity: a histogram of the peak bin (latency) of PL calls, and the PL fraction when peaks in the last two unblanked bins are excluded.
- figs4b mapping: the file descriptions of `stim_channel` and the electrodes' `channel_name`, plus modulation z against distance per stimulation channel.
- fig2a: psignifit at its default grid, and psignifit's x50 per channel and session.
- The `accepted` flag: its counts per session, and fig4 counts restricted to accepted units.
- Control counts: the early/late MWU on the stored activation sums per channel at 5 uA and pooled, with the per-file week assignment.
- Whether `PlaneSegmentation` in the behavioural files holds reference or mean images, which would make the planar tracking claims testable. The archive API lists no image types, but it does not show the file structure.
- Per-pulse stimulation timing, which would show whether the trains are exactly 10.000 ms apart, as `pulse_matrix` assumes.
