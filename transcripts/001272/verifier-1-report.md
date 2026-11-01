## Verifier report, round 1: DANDI:001272 (Semenov et al. 2025)

**Materials mismatch, read this first.** The claims file I was given is the one for DANDI:001273. Its header says "on dandiset 001273", `dataset.id: "001273"`, and it has 17 claims. The notebooks cite a different file, `claims/001272/10.1016-j.xcrp.2025.102660.yaml`, with header items F1–F6 and O1–O6 and claim ids that are not in my file (figs1-eight-neurons, figs1-aps-as-emission-decrease, fig1-20khz-needs-twice-the-field, fig4-orientation-and-poles, and others). I had neither that file nor the attempt record. So:
- Table A1 gives outcomes for the 17 claims in the file I have. Only one of them, figs1-di8-anepps-control, is assigned to 001272.
- Table A2 gives outcomes for the notebook's own figs1 claims, judged against the criteria as the notebook quotes them. I could not check those criteria against their source.

### A1. Claims in the claims file provided

| Claim | My outcome | Reason |
|---|---|---|
| figs1-di8-anepps-control | not_reproduced | The archive holds 3 subjects and 65 files, not 8 neurons (API: `numberOfSubjects` 3). Every neuron fires, and latency falls with field (Spearman rho < 0 in 3 of 3 under 10 of 12 readings, cell 18). But no neuron's highest field ends in depolarization by the file's rule (no late APs, mean dF > 5%): late mean dF at the top fields is 1.0, 3.3 and 1.7% (cell 20). Two of the three neurons were only tested up to 234 V/cm. The file's "rise ≥ 5% within 5 ms" AP reading was not run, but failing under one reading is enough. |
| fig1-pure-sine-excites-all | not_reproduced | Under all 12 readings the median first-AP latency at threshold is 15–77 ms, below the 90–220 ms window. The median ceiling is outside 54–99 Hz in 8 of 12 readings, including all four whole-frame ones (fluovolt cell 10). |
| fig2d-modulated-thresholds-higher | not_reproduced | In every reading at least one 20/2-kHz ratio is outside 1.8–2.2; whole-frame ratios are 2.27–2.83 (fluovolt cell 12). No reading gives all three modulated-higher tests at p < 0.05 (cell 14). |
| fig2-modulated-locks-to-beats | partially_reproduced | Locking holds: 89% of APs fall 12.5–37.5 ms into the beat (whole/a/b, cell 16), and no session shows sustained depolarization. The cap of 10 APs fails: one session (001032:10_1, 8 V) has 13 APs under the whole-frame readings, and ROI (a) with the 5% height gives up to 17 APs. |
| fig2c-pure-more-aps | reproduced | Pure sine waves give more APs in 46–47 of 52 pairs against 0 under whole-frame readings, and in 22–41 against 2–12 under ROI readings. Paired p ≤ 0.022 everywhere (cell 18). |
| fig3b-low-conductivity-halves-threshold | blocked (data_missing) | Confirmed in the archive (see C). |
| fig3c-sustained-firing-2s | not_reproduced | Under the file's AP readings (peak value), no neuron's top-field session has no late APs together with elevated dF. The top sessions either have late APs (c7: 9) or a late mean ≤ 3.3% (cell 20). This holds under both bleaching corrections. |
| figs2-ttx-blocks-depolarization | partially_reproduced | Under whole-frame readings, APs are abolished in 6 of 6 TTX neurons and kept in 13 of 13 vehicle neurons (cell 23). The criterion also needs a late mean dF above 5% before TTX; the observed values are 0.12–3.28%, so the depolarization part fails. The notebook's pass is vacuous on that part (problem 2). |
| threshold-depolarization-estimate | not_reproduced (threshold part); rest untested | The FluoVolt 2-kHz mean 1-AP threshold is 140–178 V/cm with the files' scale, or 70–89 V/cm with it halved (di8 cell 26). Neither is within 57.7 ± 3.6 V/cm. The sensitivity terms need DANDI:001274, which was not loaded. Calibration caveat in problem 7. |
| fig6-sine-less-than-pulse | blocked (other: not attempted) | DANDI:001274 holds the data (see C). |
| fig5-sine-asymmetry | blocked (other: not attempted) | As for fig6. |
| fig4-orientation-time-constants | blocked (metadata_insufficient) | The 001273 files carry no shape labels (strobe cell 2). |
| fig4-polarized-poles-face-electrodes | blocked (other: not attempted) | Field direction is in the files for 118 of 181 files (14 of the 22 experiments), and the criterion falls back to "all experiments" when shape labels are missing. It is testable in part. |
| fig4-pooled-time-constants | blocked (methods_underspecified, likely) | Shape labels are not needed for this claim, and a missing debris ROI only makes the analysis "unscaled, as a deviation" (header F2). So the notebook's metadata_insufficient reason does not hold. The real obstacles are 22 experiments where the paper reports 19, and fits that vary widely across readings on the one experiment run (problem 8). |
| fig4-no-pole-difference | blocked (other: not run) | No labels needed; same fit problem as fig4-pooled-time-constants. |
| fig4-discharging-slower | blocked (partly metadata_insufficient) | The elongated-parallel part needs shape labels; reading (a) does not. Not run. |
| fig4-full-charge-within-3us | blocked | Depends on fig4-pooled-time-constants. |

### A2. The notebook's own claims for 001272 (criteria as quoted in the notebook, unverified)

| Claim | My outcome | Reason |
|---|---|---|
| figs1-eight-neurons | not_reproduced | 3 subjects; the archive confirms this. |
| figs1-aps-as-emission-decrease | reproduced | The test favours "inverted" by design, since the detector only looks for upward peaks. The independent check agrees: the largest brief deflection is negative in 57 of 65 sessions (cell 14). |
| figs1-near-threshold-delayed-aps | blocked (methods_underspecified) | The readings disagree: it passes under 19 of 48 combinations (cell 16). |
| figs1-stronger-field-shorter-delay-sustained-firing | partially_reproduced | The latency part holds in 3 of 3 neurons under most readings. The sustained-firing part rests on AP counts under height (b), which include noise (problem 4). |
| figs1-culminates-in-sustained-depolarization | not_reproduced | Passes under 0 of 24 combinations; the prominence variant reaches at most 1 of 3 neurons (cell 20). |
| figs1-noisier-than-fluovolt | not_reproduced | Pre-stimulus SD is lower for Di-8-ANEPPS (0.55 against 0.88 %, whole frame). SNR is lower in 10 of 12 readings, but the criterion needs both. |
| figs1-effects-same-as-fluovolt | not_reproduced | The pattern part already fails (culminates). The threshold comparison depends on the amplitude scale: no difference in 12 of 12 readings on the files' scale, a difference in 9 of 12 with FluoVolt halved. |

### B. Problems

1. **[affects a conclusion] Claims-file mismatch (all notebooks).** The file provided names only figs1-di8-anepps-control for 001272. Its AP readings are a 5% peak, a rise of ≥ 5% within 5 ms, and 5 SD; the notebook runs 5% and 5 SD only. Its depolarization level is 5%, while the notebook uses 5 SD or half the AP height. The notebook's claim ids, F/O labels and amended O3 (the 1-ms width) cannot be checked against the file I have.
2. **[affects a conclusion] fluovolt `ttx_eval` (cell 23).** The term `(~sd_before) | (~sd_after)` passes whenever there is no depolarization before TTX. That happens in 5 of 6 TTX neurons, so "abolished the sustained depolarization" is never actually tested. Under the provided criterion (late mean > 5% before), that part fails in 6 of 6.
3. **[affects a conclusion] `sinewave.detect_aps` with `height_ref="value"` counts noise on a raised baseline as APs.**
   - Synthetic tests: a 5.5% plateau with 0.5% noise gives 6 false APs (0 with prominence). Noise on a 3% drift gives 7 false APs under the 5 SD threshold.
   - Di-8-ANEPPS traces are inverted, so bleaching shows up as an upward drift: the late mean is about 1.4–1.6% at fields with no APs.
   - The di8 cell 10 figure (neuron 3) shows this: at fields of 144 V/cm and above, the red markers sit on small noise bumps on a raised plateau that follows one real AP.
   - Effects: the sustained-firing counts are inflated, and the sustained-depolarization test (which needs "no late APs") is suppressed. Prominence was run only as a variant for culminates and fig3c.
4. **[affects a conclusion] No null test for the detector on Di-8-ANEPPS data.** In FluoVolt sham sessions, ROI (a) with the 5% height gives 20 false APs (fluovolt cell 5). ROI (a) results are still weighted equally with the others in every count of readings.
5. **[does not affect a conclusion] O1 (b) is degenerate (`roi_masks`).** Erosion empties the mask in 65 of 65 Di-8-ANEPPS files and 264 FluoVolt files, so "12 readings" is effectively 8. ROI (a) is a membrane edge or a frame corner, not the soma (cell 5 image). The whole-frame reading is the author's own; it is stated as such and is reasonable.
6. **[does not affect a conclusion] Hard-coded text in di8 cell 4.** "16 x 16 pixels" and "of 256 pixels" are typed strings, not read from the data.
7. **[affects threshold-depolarization-estimate] Amplitude scale.** The 001272 file descriptions say "Actual amplitude measured on the oscilloscope may be smaller due to calibration factors". The scale check in cell 27 (p = 0.289) shows only that no difference was detected, not that the scales are equal.
8. **[affects the fig4 conclusions] `strobe.fit_tau` reports fits stuck at a bound as results.** Values of 20.000 µs (the upper bound) and 0.02–0.05 µs appear as taus (strobe cell 5). Unscaled charging tau ranges from 0.26 to 5.8 µs across readings on one experiment, with dF late in the pulse of 3–5% against a pre-pulse SD of about 3%. Fits are not checked for convergence.
9. **[affects fig5, fig6] Blocked without checking the archive.** DANDI:001274 holds pulse and sine recordings (see C).
10. **[does not affect a conclusion] fig3c window.** The notebook takes the last 250 ms with the O6 levels. The provided file says "after 250 ms", that is, from the end of the ramp to the end of the stimulus, at 5%. The per-neuron tables fail either way.
11. **[does not affect a conclusion] Truncated files and pooled latencies.** 38 FluoVolt files of 900 frames cover only 241 ms of the stimulus, and fig1 pools 2- and 20-kHz latencies into one median.

### C. What I checked in the archive, and what I could not check

- **fig3b.** No 250-ms sessions in sodium gluconate exist in 001030 or 001032–001035 (none mention gluconate), or in 001271. The only other gluconate data are in 001031, which holds 100-kHz bipolar pulses for 2 s and does not fit. The block is right.
- **fig5 and fig6.** 001274 (0.250805.1401) has 232 files from 20 subjects: 77 recordings with 2-µs pulses and 155 with 2-kHz sine waves modulated at 100 or 154 Hz. The data are present; the claims were simply not attempted.
- **Not checkable without data or files:**
  - Whether the criteria quoted in the notebook match `claims/001272`. I would need that file.
  - Whether the Di-8-ANEPPS AP counts under height (b) are mostly noise. A per-session count of APs in the 50 ms before onset, or in the post-stimulus window (300–388 ms), under each reading would have settled it.
  - How much of the late mean dF is bleaching. Late mean dF minus the same neuron's subthreshold late mean at each neuron's top field would have shown it, and would let figs1-di8-anepps-control be judged against a bleach-corrected level.
  - Whether the fig4 fits are stable across experiments. fit_tau over all 22 experiments, with a flag for fits that hit a bound, would have shown it.
