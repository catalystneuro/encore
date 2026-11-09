**A. Outcomes (26 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| fig1-pure-sine-excites-all | not_reproduced | 2 kHz passes (27/28 or 28/28), but 20 kHz is 15/17 = 88% under all four readings (cell 20). The criterion needs at least 90% at each frequency and has no partial outcome. The two neurons that never fired were tested up to 288 and 324 V/cm, above the mean 20-kHz threshold of 171 V/cm. |
| fig1-onset-delay | not_reproduced | Latency falls with field in 38/38 pairs, but the median near-threshold latency is 54–67 ms under every reading (cell 22). The variant that keeps only bracketed thresholds gives 67 ms. Both are outside 90–220 ms, and the criterion needs both parts. |
| fig1-max-rate-ceiling | blocked (methods_underspecified) | On the adopted whole-frame trace the two AP readings disagree: 59.9 Hz under (a) is inside 54–99 Hz, 42.9 Hz under (b) is outside (cell 25). The fig1 criterion that this claim inherits blocks when readings disagree. The notebook's "reproduced" ignores reading (b). |
| fig1-excitation-block | not_reproduced | Block in 3 of 42 neuron-carrier pairs under every reading. The second-half variant also gives 3 (cell 27). |
| fig2d-20khz-twofold-threshold | not_reproduced | p < 0.0001 holds pooled and nearly always per group. The 20/2 kHz ratios are 2.27–2.82, outside 1.8–2.2, except two groups under bright/b (cell 29). The criterion needs every ratio within tolerance. The outcome also depends on frequency-dependent generator calibration (problem 3). |
| fig2d-modulated-thresholds-higher | partially_reproduced | The modulated mean is higher in all three pairs. p < 0.05 holds in only one or two of the three under every reading: whole/a 20k-1AP only (p = 0.021); whole/b 20k-1AP and 20k-5AP (cell 31). |
| threshold-2khz-unmodulated | not_reproduced | 75.6 ± 6.2 V/cm (half reading) or 151 V/cm (full reading), both outside 57.7 ± 3.6, and the AP readings agree (cell 33). The dataset itself says its volts overstate the true amplitude (problem 3), so this miss may come from calibration. |
| fig2-modulated-locks-to-beats | not_reproduced | (ii) passes: 0.83–0.98 of APs fall in the peak window. (iii) fails under every reading: one session has 5.9% in the last 100 ms. (i) fails under whole/a, bright/a and bright/b, with up to 13 APs in a session (cell 35). |
| fig2c-pure-more-aps | reproduced | Unmodulated beats modulated in 43–46 of 52 pairs, against 1–2 the other way. Paired t test p ≈ 1e-9 under all four readings (cell 37). |
| fig3b-low-conductivity-halves-threshold | blocked (metadata_insufficient / data_missing) | I checked the archive: none of the 1,177 assets of 001032/34/35, 001033, 001271 and 001272 mentions gluconate, and all list the NaCl solution. Only 001030 (2-s ramps, sodium gluconate only) does, so there is no NaCl against sodium gluconate pair to test. |
| fig3c-sustained-firing-2s | not_reproduced | (i) and (ii) pass for c7. (iii) fails under both readings at 82.8 V/cm: reading (a) finds 131 APs after 250 ms, reading (b) finds one (at 1.682 s); rest dF is 6.7% (cell 39). Reading (a)'s count is probably noise on the plateau (problem 2), and reading (b) misses by one AP. |
| figs1-di8-anepps-control | not_reproduced | Only 3 of the paper's 8 neurons are deposited. I confirmed three separate voltage series by session times. The block test gives 0/3 under every reading, and the readings disagree on excitation (cell 41). The 3 deposited neurons fail it. Whether all 8 would pass cannot be decided, so blocked (data_missing) is also defensible. |
| figs2-ttx-blocks-depolarization | not_reproduced | APs are abolished in 6/6 neurons under (a) and 5/6 under (b). Only 1 of 6 neurons has last-100-ms dF above 5% before TTX, so the depolarization part fails (cell 43). The vehicle neuron was not identified. |
| fig4-orientation-time-constants | blocked (metadata_insufficient) | 001273 has no ROIs and no elongated or random labels; the archive metadata has no variableMeasured, and the descriptions give field direction for 118 of 181 files only. |
| fig4-no-pole-difference | blocked (metadata_insufficient) | No ROIs (O1). A rebuilt-ROI variant was possible but not run. |
| fig4-discharging-slower | blocked (metadata_insufficient) | No ROIs and no groups. |
| fig4-pooled-time-constants | blocked (metadata_insufficient) | No ROIs (O1). |
| fig5-carrier-antiphasic | blocked (metadata_insufficient) | No ROIs (O1), and C7 cannot be matched (O4): at most 5 sessions at 100 Hz per subject, where C7 had 12 (cell 8). |
| fig5-whole-cell-depolarization | blocked (metadata_insufficient) | Same as above (O1, O4). |
| fig5-sine-asymmetry-c7 | blocked (metadata_insufficient) | Same as above (O1, O4). |
| figs3-sine-asymmetry-c8 | blocked (metadata_insufficient) | Same as above (O1, O4). |
| fig5fg-no-migration | blocked (metadata_insufficient) | The 16 ROIs and their 5F/5G split are not in the dataset. |
| fig6b-pulse-sensitivity | blocked (metadata_insufficient) | No ROIs. The rebuilt-ROI variant (20.6 ± 2.7) decides nothing. |
| fig6c-sine-sensitivity | blocked (metadata_insufficient) | No ROIs, and no waveform or field in the files. |
| fig6d-sine-less-than-pulse | blocked (metadata_insufficient) | Depends on fig6b and fig6c. |
| threshold-depolarization-estimate | blocked (metadata_insufficient) | Depends on fig6d. The threshold half is not reproduced anyway. |

**B. Problems**

1. **[affects a conclusion]** `ti_sine.detect_aps`, reading (a), counts noise on a depolarized plateau as APs. I tested it on a synthetic trace with no APs: a 6% plateau with 0.8% SD noise, which is the data's median pre-stimulus SD. It found about 18 "APs" per 250 ms, with a first-two-AP rate of about 79 Hz. That rate falls inside the paper's 60–90 Hz ceiling. Reading (b) has the opposite fault: on an 80-Hz train of APs riding on a plateau it reports 51 Hz. These errors bear on fig3c (iii) (131 APs under (a)), fig2 locks-to-beats (i) (12 APs under (a) against 6 under (b) in the same session) and fig1-max-rate-ceiling. The 2.5% prominence is the author's own addition and does not prevent it. No output shows detections overlaid on high-field traces.
2. **[affects a conclusion]** Calibration. Every fast-recording description says the generator voltage overstates the real amplitude, with frequency-dependent factors "reported separately", and those factors are not deposited. The 001273 descriptions show the measured amplitude for pulses at 0.62–0.78 of nominal. A factor of about 0.76 would turn 75.6 V/cm into 57.7. A larger loss at 20 kHz than at 2 kHz would pull the 2.27 ratio towards 2. Within 001035 alone, the threshold is 58.3 V/cm (cell 33). The notebook mentions this caveat (cell 18) but never estimates its effect. It bears on threshold-2khz-unmodulated, fig2d-20khz-twofold-threshold and threshold-depolarization-estimate.
3. **[affects a conclusion]** The summary cell 50 does not apply the claims' criteria:
   - fig1-pure-sine-excites-all, fig1-onset-delay, fig2d-20khz-twofold-threshold, fig2-modulated-locks-to-beats, fig3c-sustained-firing-2s and figs2-ttx-blocks-depolarization are scored "partially reproduced". Their criteria have no partial outcome, and each fails a required part.
   - fig1-max-rate-ceiling is scored "reproduced" even though reading (b) is out of range.
4. **[does not affect a conclusion]** Cell 35 tests (iii) as last-100-ms dF > 5% only. It leaves out the "exceeds the near-threshold session" part of the fig1-excitation-block test. The failing session at 5.9% would very probably fail the full test too.
5. **[does not affect a conclusion]** Cell 10 shows only 116 of 178 asset names shared between 001032 and 001034. I matched all 178 by session start time and size through the API, so leaving 001034 out is correct.
6. **[does not affect a conclusion]** Cell 43 never identifies the paper's vehicle-control neuron; "neurons never in TTX" stands in for it. The "about 5 min after TTX" pairing ranges from 3.6 to 11 min apart.
7. **[does not affect a conclusion, variants only]** Cells 46 and 48:
   - The 15-V pulse of sub-4-20240522 is divided by 0.257 kV/cm, as if it were 10 V.
   - The rebuilt ROIs are placed at the extremes of the same RATIO image they are then measured on, which biases the result upward.
   - The carrier phase is fitted on ROI 1 before ROI 1 is regressed, which forces a positive sign and inflates its p.
   - `frame_times_pulse` assumes forward recording, but 4 pulse files in 001274 and many in 001273 are described as "backward". I checked that the nine pulses actually used are all forward.
8. **[does not affect a conclusion]** In cell 20 the "neurons with an AP in any session" variant is identical to the main count, so it adds nothing. The "never on-off" part of the statement is not tested, and the criterion does not require it.
9. **[does not affect a conclusion]** Cell 39 uses c7's 36-V/cm trace as the bleaching reference for neurons c5, c6 and c8 as well. Only c7 is judged.
10. **[does not affect a conclusion]** Fast traces are not bleaching-corrected for the window-mean tests (fig1-excitation-block, TTX). The near-threshold last-100-ms median of −0.2% suggests the drift is small.

**C. What I could not check, and the output that would settle it**

- Whether the AP detections are real APs. Example traces with detected APs marked would settle it, for:
  - the highest-field session of each neuron;
  - c7 at 82.8 V/cm (001030);
  - the sessions that give each neuron's rate ceiling, with their baseline dF;
  - the two modulated sessions with more than 10 APs.
- Whether the shortest near-threshold latencies (minimum 3 ms) are stimulus-onset artifacts. A histogram of first-AP latencies below 20 ms, with the traces, would settle it. If they are artifacts, the 64-ms median of fig1-onset-delay is biased low.
- The 1.75 V ↔ 63 V/cm cross-check (cell 18) that supports the half-field reading. No output shows it.
- The raw traces of the two 20-kHz neurons that never fired, to rule out a dim cell or a misplaced soma ROI.
- Whether any 001032–001035 neuron was recorded in sodium gluconate despite its NaCl description. A per-neuron threshold time course across sessions, showing a reversible two-fold drop, would settle it.
- The strobe frame timing. A plot of whole-frame mean intensity against frame index for one pulse file would show the pulse onset at frame 20, as `frame_times_pulse` assumes.
