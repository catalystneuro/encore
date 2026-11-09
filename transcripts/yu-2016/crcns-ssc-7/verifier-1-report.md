**A. Outcomes**

The claims file has 48 claims: 43 are tested in the notebook and 5 are treated as blocked. My tally is 17 reproduced, 15 partially reproduced, 11 not reproduced and 5 blocked. Cell 0 still holds an outcome table that should have been removed. I did not use it; the outcomes below are my own.

| Claim | Outcome | Reason |
|---|---|---|
| behavior-performance | partially_reproduced | Cell 9: cortical performance 0.706 is within tolerance. VPM performance 0.630 is just outside (bound 0.639), Go touches 7.56 are outside (5.7±0.57), and Nogo touches 1.06 and reaction time 328 ms are outside under every reading. Not all five values hold, which the criterion requires. |
| vpm-baseline-rate | partially_reproduced | Cell 11: the mean (4.3 to 4.8) is within 5.1±1.02 under all readings, but the median (2.0 to 2.2) is outside 3.3±0.33 under all readings. |
| vpm-touch-response | partially_reproduced | Cell 13: only the median spikes per touch (0.363) holds. The mean is 0.50 (tolerance 0.6±0.093), latency mean is 2.48 and median 1 ms (paper 3.2 and 2.5), and duration is 4.08 ms (paper 2.9). The response is clearly sharp and brief, with the population PSTH peaking 1 to 2 ms after touch. |
| vpm-whisking-count | reproduced | Cell 15, reading (b) per-trial rates: 24 increase, 4 no change, 1 decrease, all within tolerance. Reading (a) per-epoch gives 22/6/1, which fails. |
| vpm-whisking-rate | reproduced | Cell 17: 4.34 → 11.92 spikes/s, both within tolerance; signed-rank p = 5e-8. |
| vpm-phase-modulation | reproduced | Cell 19: r² > 0.25 in 27 of 29 units (8 bins) and 25 of 29 (16 bins). The notebook's shuffle gives 14 of 29, and my synthetic test gives 48%, so chance is about half; 27 of 29 is far above it. |
| vpm-rate-amplitude-trials | reproduced | Cell 21: no session has 310 trials, so the criterion's fallback applies. 24 of 29 units show a significant positive r. |
| l4e-example-e1 | reproduced | Cell 43: all seven values are within tolerance under readings (a) (whisking change 6.13 mV, rate increase 0.41 spikes/s), and the spike range is 0 to 7. |
| l4e-example-e24-e32 | reproduced | Cell 45, M-VM reading (a) with the 100 ms rise (M-EPOCH reading b): 1.07 and −1.75 mV, both within tolerance. The notebook printed these values but never checked them against tolerance (problem 6). |
| l4e-resting-vm | reproduced | Cell 47: all four values are within tolerance under both readings. |
| l4e-touch-psp | partially_reproduced | Cell 49: both medians are within tolerance (latency 5.0, amplitude 5.4); both means are outside (latency 6.03, amplitude 5.26 against a bound of 5.4). All amplitudes are positive. |
| l4e-whisking-vm | reproduced | Cell 51: wdep_a 1.02 / median 1.21 mV, both within tolerance. |
| l4e-distance-threshold | partially_reproduced | Cell 53: the test holds (p = 3e-11, touch larger), but the means (−0.87 and 7.55) are outside tolerance. The s.d. of 20.9 mV against the paper's 2.0 points to an implementation artifact (problem 1). |
| l4e-reversal-potential | partially_reproduced | Cell 55: touch reversal exceeds whisking reversal (p = 5e-5), and touch reversal is above rest in 34 of 35. The median whisking reversal sits 5.6 mV above rest, outside the 5 mV margin (5.9 mV pooled). |
| l4e-hf-fluctuations | reproduced | Cell 57: signed-rank p = 0.046 for band (a) and 0.03 for band (b). Marginal. |
| l4e-inhibition-window | blocked (data_missing) | Cell 98: no L4 E whole-cell trial has a median Vm above −42.8 mV, and the largest current is 0.2 nA. The check is incomplete (problem 3). |
| l4e-whisking-inhibition | blocked (data_missing) | Same recordings, same caveat. |
| fs-baseline-rate | reproduced | Cell 23: 9.43 / 6.3 spikes/s, within tolerance under all readings. |
| fs-touch-vm | reproduced | Cell 59: all four values are within tolerance (6.74 / 6.97 mV; 3.69 / 4.0 ms). |
| fs-touch-spikes | partially_reproduced | Cell 25: spikes per touch (1.83 / 1.95) and n = 25 hold; latency mean 5.92 and median 4.0 are just outside tolerance. |
| fs-whisking-count | reproduced | Cell 27: 21 to 22 increase and 3 decrease, within tolerance under all readings. |
| fs-whisking-vm | partially_reproduced | Cell 61: the means hold under (a) and (b) (2.0, 2.36), but the medians (1.53, 2.0) are outside 2.4±0.24. Reading (c) fails. |
| fs-whisking-rate | reproduced | Cell 29: all parts hold (21.7 / 14.2 spikes/s, ratio 2.30, p = 2e-5). |
| fs-phase-coupling | partially_reproduced | Cell 31: the single-sinusoid / second-harmonic split is 22/4 (8 bins) or 21/5 (16 bins) against 18±1.8 / 7±1, so both counts fail. Coupling itself holds (r² > 0.25 in 25 of 26). |
| fs-hf-fluctuations | reproduced | Cell 63: 5 or 6 of 7 neurons show the increase. The test is weak with 1 to 4 whisking segments per neuron. |
| l4e-spikes-touch-selective | not_reproduced | Cell 33: whisking against nonwhisking signed-rank p = 0.02 to 0.027, which the criterion counts as not reproduced. Spikes per touch are also outside tolerance (mean 0.2, median 0.04). |
| thalamus-inhibition-vpm | blocked (data_missing) | Confirmed from the archive: the file list holds only data.tar.gz, docs and code; the cell list has no thalamic multiunits; the 7 folders hold none. |
| thalamus-inhibition-l4e-vm | partially_reproduced | Cell 80: both tests hold (n = 13, p = 2e-4). The claims-file M-LAT rule gives 0 ms for both latencies because of the onset step. The author's smoothed variant, a stated assumption, gives 4.8 and 2.6 ms: thalamic is longer, but 4.8 is outside 4.2±0.42. |
| thalamus-inhibition-fs | partially_reproduced | Cell 76, M-LIGHT reading (a): all three tests hold. The percentages (12/27/47% or 9/24/47%) are all outside 4/13/32%. |
| thalamus-inhibition-dose | reproduced | Cell 78: 3 of 3 epochs show significant negative ρ. The design is weak (problem 9). |
| rabies-vpm-input | blocked (data_missing) | Confirmed: no histology in the archive or the cell list. |
| ion-cut-behavior | reproduced | Cell 35: 0.492 pooled and 0.510 per cell; chance is about 0.5 with balanced Go/Nogo, matching the paper's chance level. |
| ion-cut-l4e-touch | not_reproduced | Cell 65: amplitude 0.32 mV against zero, p = 0.0078, positive, which the criterion counts as not reproduced. The criterion itself is biased (problem 8): against random-time amplitudes, p = 0.15. |
| ion-cut-l4e-whisking | reproduced | Cell 67, wdep_a with controls (a), n = 17: 0.58 and 1.35 mV within tolerance (1.35 is at the edge), p = 0.033. |
| ion-cut-l4e-phase | reproduced | Cell 69, reading (a): 0.111 and 0.304 mV within tolerance (0.304 is at the edge), p = 0.03 / 0.02. |
| ion-cut-l4e-spectra | reproduced | Cell 71: p = 0.47, not significant, but only 7 of 9 neurons have whisking segments. |
| ion-cut-fs-touch | reproduced | Cell 37: p = 0.098 against zero; mean 0.06 against a control 1.83. |
| ion-cut-fs-whisking | reproduced | Cell 39: p = 0.63 to 0.85. |
| ion-cut-fs-phase | reproduced | Cell 41: ION-cut r² is lower (p = 0.013 / 0.004), and 9 (or 6) ION-cut neurons have r² > 0.25. |
| ion-cut-l5-fs | blocked (data_missing) | Confirmed: the cell list's ION-cut FS depths are 444 to 614 µm; no L5 neurons are in the archive. |
| enphr-kruskal-wallis | reproduced | Cell 82: four-group p = 4e-4 (n = 43, not 40). |
| enphr-l4e-rates | partially_reproduced | Cell 84, M-LIGHT (a): both tests hold and three means are within tolerance; control whisking 1.13 is outside 0.8±0.2. |
| enphr-whisking-driven | reproduced | Cell 86: p = 0.013 (a) and 0.0065 (b), whisking higher. Under (b) control trials also give p = 0.035, against the paper's figure value of 0.55. |
| enphr-spikes-per-touch | not_reproduced | Cell 88: the means hold, but the signed-rank test is significant (p = 0.009) and the Spearman correlation fails (p = 0.42). One of three parts holds. |
| enphr-auc | reproduced | Cell 90, M-ROC (b): ρ = −0.35, p = 0.036. Reading (a) gives p = 0.074. The test is biased (problem 9). |
| enphr-auc-groups | not_reproduced | Cell 92: groups are 18/18 or 22/15, most rates are outside tolerance, and the "increase" tests are not significant. |
| enphr-pv-latency | partially_reproduced | Cell 94: 3 of 4 PV neurons are strongly inhibited, but the PV latency is NaN under both readings because the 4-neuron grand PSTH is too noisy. |
| enphr-behavior | not_reproduced | Cell 96: 4 of 9 mice show a decrease, against 6±1 of 8, and the example session is not found. It is unverified that these recording sessions are the paper's Supplementary Fig. 14 sessions (problem 10). |

**B. Problems**

1. [affects a conclusion] `vm_summary` (M-DTT), cell 53. The per-trial threshold line from `np.polyfit` is extrapolated to trials far from any spike. This gives whisking-shift s.d. 20.9 mV (paper 2.0), and the notebook itself flags 6 shifts above 15 mV. No variant was run, such as clamping the line to the range of trials with spikes or using a per-neuron mean threshold. The means of l4e-distance-threshold, and fs-whisking-vm reading (c), rest on this.
2. [affects a conclusion] Principal-whisker choice, cell 5 and `pw_index`. "Series 1" rests only on FS touch responses. The L4 E rows of the PWT table are computed but never printed. The behaviour variant matches the paper better under "config" (Go touches 5.93, within tolerance). The L4 E claims (l4e-touch-psp, l4e-spikes-touch-selective, l4e-distance-threshold) were never run under the other reading.
3. [affects a conclusion] Blocked evidence for l4e-inhibition-window and l4e-whisking-inhibition, cell 98.
   - The FS whole-cell folder has a trial with median Vm −2.3 mV and a 1.99 nA current. That matches the Methods' depolarization protocol (about 0 mV, typically 1 nA) and was never examined.
   - JY1139 in that folder is labelled "Excitatory" in its own file.
   - The cell list names JY0978, which is in the dataset, as the Fig. 3 example.
   - `reduce_file` reads only `min(n_tr, n_e)` ephys trials, so ephys trials without whisker video are dropped silently; `n_ephys_trials` is never compared with `n_trials`.
   - Part of these two claims may therefore be testable.
   - The same depolarized FS trials may also be contaminating fs-touch-vm, fs-whisking-vm and fs-hf-fluctuations.
4. [affects a conclusion] thalamus-inhibition-fs, cell 76. M-LIGHT reading (d), the highest power only, was not run. The 15 mW rows of cell 78 (nonwhisking about 5% of control) suggest it would move the nonwhisking percentage, though the outcome likely stays partial.
5. [affects a conclusion] thalamus-inhibition-l4e-vm, `neg_latency_smooth`. The claims-file rule fails on the light artifact. The outcome rests on the author's own smoothing and 1 ms hold, which is stated, and is reasonable but untested against other window choices.
6. [does not affect a conclusion] Cell 45 prints the 100 ms-rise values (1.07 and −1.75) without applying the tolerance. Under them the claim is reproduced, not partial. That reading fails l4e-whisking-vm and fs-whisking-vm, so the reading choice is made claim by claim.
7. [does not affect a conclusion] `spike_latency` reports the left edge of the 1 ms bin. Using the bin centre would put the FS median at 4.5, but the FS mean (6.4) and the VPM values still fail. The VPM median latency of 1 ms against the paper's 2.5 is unexplained; it could be a touch-onset or clock offset, and the clock check only resolves to 1 ms.
8. [affects a conclusion; claims-file issue] ion-cut-l4e-touch tests a peak-minus-baseline amplitude against zero. That measure is positive by construction: random times give 0.21 mV, and touch against random gives p = 0.15. The not_reproduced outcome is an artifact of the criterion.
9. [affects a conclusion; claims-file issue] Two fixed tests cannot tell the effect from its null:
   - **enphr-auc:** correlating the control rate with (AUC_eNpHR − AUC_control) has a built-in negative regression-to-the-mean bias.
   - **thalamus-inhibition-dose:** with control coded as 0 and only one or two powers (4 neurons have one), the correlation mostly tests light against no light, not dose.
10. [affects a conclusion] enphr-behavior, cell 96, assumes the recording sessions are the paper's Supplementary Fig. 14 behaviour sessions. The data give 9 mice against the paper's 8, so this may deserve "blocked (metadata_insufficient)" rather than not_reproduced.
11. [does not affect a conclusion] The eNpHR set has 43 neurons against the paper's 40, and the extra 3 are not identified. This matches the cell list's Supplementary Table 2 (5 whole-cell + 38 cell-attached L4 E).
12. [does not affect a conclusion] `roc_cell` uses the first touch even in trials tagged passive, which `touch_table` excludes. `onset_vm_change` does not set to NaN data after a later touch (touches 250 to 300 ms after onset can enter the window), as M-EPOCH asks.
13. [does not affect a conclusion] `remove_spikes` uses a central-difference gradient, which puts the threshold about 0.1 ms early; the E No. 1 threshold s.d. is 8.9 mV against the paper's 3.7.
14. [does not affect a conclusion] fs-hf-fluctuations compares the whisking mean, from 1 to 4 segments in 4 of 7 neurons, against a narrow nonwhisking interval, so about half the frequencies can exceed it by chance.

Synthetic tests: `spike_latency`, `response_duration`, `spikes_per_touch`, `phase_fit`, `vm_latency`, `multitaper`, `touch_table`, `trial_epochs`, `onsets` and the phase convention all behave as specified.

**C. Not checked, and what would have let me**

- **Trial-type column order** (Hit/Miss/CR/FA is assumed in `behav` and cell 96). Print `trial_type_names` per folder, including VPM, whose matrix is transposed; the VPM performance of 0.63 is unexplained.
- **Depolarized trials** (problem 3). Print, per whole-cell neuron, `n_ephys_trials` against `n_trials`, the largest trial-median Vm and the largest current, especially for JY0978 and every FS whole-cell neuron.
- **Principal whisker** (problem 2). Print the L4 E rows of the PWT table, and l4e-touch-psp and l4e-spikes-touch-selective under the "config" reading.
- **Distance to threshold** (problem 1). Print the threshold-line slope and the range of trials with spikes for each neuron, and the shifts with the line clamped.
- **Pole times in M-ROC reading (a)** (pole_in/pole_out minus t0). Print their ranges, because the units on the cortical clock are not shown.
- **The 3 extra eNpHR neurons.** List the 43 against the cell list.
- **Blocked claims.** I could not list the tar members without downloading. The 7-folder content rests on cell 3's output, which matches the cell list.
