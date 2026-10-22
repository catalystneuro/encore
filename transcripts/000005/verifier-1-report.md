**Verifier report, round 1: Yu et al. 2016 (doi:10.1038/nn.4412) on DANDI 000005 @ 0.220126.1853**

The claims file has 33 claims. My outcomes: 6 reproduced, 9 partially reproduced, 4 not reproduced and 14 blocked. Cell numbers are 0-based notebook cell indices.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| behavior-touches | partially_reproduced | Both touch counts are within tolerance only under reading (b, principal whisker, every trial): 6.04 and 0.85, but over 9,794 and 8,223 trials against the paper's 4,147 and 4,173. Cortical performance 0.718 is within tolerance; VPM performance 0.585 is not (needs 0.71 ± 0.071) (cell 23). |
| vpm-touch | not_reproduced | Spikes per touch: mean 0.403 and median 0.268, both out of tolerance (0.6 ± 0.093, 0.4 ± 0.04). Latency: median 2.5 ms is within; mean 6.14 ms is out, inflated by one 71.5 ms unit. The best-whisker variant also fails (mean 0.485) (cell 25). |
| vpm-whisking | partially_reproduced | The signed-rank test gives p = 5e-8 with whisking higher. Nonwhisking mean 3.76 and median 1.71 are out of tolerance under every reading; the increase count (21–25) and whisking mean (11.0–11.5) are out under some readings (cell 27). |
| vpm-whisking-phase | reproduced | 25 of 29 (filtfilt) and 27 of 29 (lfilter) units have r2 > 0.25. They are clearly above the shifted-spike control (16 of 29; own > shifted, p = 0.0015) (cells 11, 29). |
| exc-vm-touch-whisking | partially_reproduced | All 48 measurable cells have a positive PSP and a latency. Latency mean 7.68 ms and amplitude 4.77 mV are out of tolerance; resting Vm and whisking change (b) are within. The no_flagged variant is still partial (amplitude 5.53 mV) (cell 31). |
| exc-threshold-touch-vs-whisking | partially_reproduced | Touch > whisking holds (p ≤ 1.9e-9). Touch shift 4.36–4.42 mV is out of tolerance (6.1 ± 0.61) under every reading (cell 33). |
| exc-effective-reversal | reproduced | Per neuron: touch median −50.0 mV > whisking −58.5 mV, in 39 of 48 neurons, and above rest (−63.9 mV). The pooled fit agrees (−31 against −55 mV) under both filters (cell 35). |
| exc-inhibition-timing | blocked: data_missing | Only one whole-cell file has trials near 0 mV, and it is the PV-ChR2 cell that the paper counts as FS (cells 5, 69). See B17. |
| exc-inhibition-whisking | blocked: data_missing | Same recordings as exc-inhibition-timing. |
| fs-touch-response | blocked: methods_underspecified | The FS readings disagree. With the waveform boundary, 2 of 3 values are within tolerance (partial); without it, 1 of 3 (not reproduced). Spikes per touch is 1.39–1.50 in every reading (needs 1.9 ± 0.2). Only 17 FS cells against the paper's 26 (cell 37). |
| fs-vm-touch-whisking | not_reproduced | Touch latency mean 1.88 ms is out of tolerance (4.0 ± 0.4); two of the five cells give 0.00 and 0.30 ms. Amplitude 5.56 mV and whisking change (a) 2.24–2.54 mV are within. 5 cells against the paper's 7 (cell 39). |
| fs-whisking-rate | partially_reproduced | Signed-rank p ≤ 0.0012 with whisking higher. 13 of 17 cells increase and 1–2 decrease, both out of tolerance. Whisking mean 19.0 is within (filtfilt); 17.8 is out (lfilter) (cell 41). |
| fs-whisking-phase | reproduced | 16 of 17 cells are coupled under both filters (14–15 of 15 in no_flagged). The shifted-spike control gives 9 of 17 (cell 43). |
| fs-touch-and-whisking | reproduced | 11–12 of 17 cells (0.65–0.71) multiplex under every reading (cell 45). |
| exc-mainly-touch | not_reproduced | The signed-rank test finds a difference (p = 9e-7 and 7e-6). Spikes per touch 0.319 is within tolerance; rates are 1.53 and 3.55 spikes/s against 0.4 and 0.6 (cell 47). |
| vpm-photoinhibition | blocked: data_missing | No VPM file has light, and every L4 file is in barrel cortex. The archive confirms this (step 4). |
| exc-thalamus-photoinhibition | partially_reproduced | Vm is lower with light in 12 of 13 cells and variance lower in 10 of 13. Both latencies come out at 0.10 ms by the criterion's rule (needs 4.2 and 2.8 ms), so the thalamic latency is not longer (cell 53). |
| thalamus-drives-fs | blocked: other (too few cells) | Only 5 FS cells, all from one mouse. The smallest possible two-sided exact p is 0.0625, so no test can reach 0.05. Fractions are out of tolerance in every reading except one: nonwhisking 0.040 under lfilter, O5 b, O7 b. The tag-only variant (9 cells, a reading of fs-touch-response only) gives p ≤ 0.012 with the fractions still out, so the best possible outcome is partial (cell 51). |
| rabies-vpm-input | blocked: data_missing | The archive holds no histology or images. |
| ion-cut-exc-no-touch, ion-cut-exc-whisking, ion-cut-exc-phase, ion-cut-fs-no-touch, sensory-input-drives-fs, ion-cut-fs-phase, ion-cut-behavior | blocked: metadata_insufficient | Neither the files, the DANDI metadata nor Supplementary Tables 1 and 2 identify the ION-cut mice. See step 4 below. |
| pv-enphr-suppression | partially_reproduced (count circular) | All 3 identified PV cells are strongly inhibited. The PV latency was not found (NaN). The E-cell rise comes at 48 ms against an expected 2 ms further delay (cell 55). See B7. |
| fs-suppress-movement-spiking | partially_reproduced | Both paired tests give p < 1e-4 with light higher. All four rates are out of tolerance: control 1.26 and 3.95, light 2.26 and 6.14 spikes/s, against 0.6, 0.8, 1.6 and 2.7 (cell 57). |
| fs-enhance-touch-selectivity | partially_reproduced | In light trials p = 2e-6 with whisking higher, but control trials also differ (p ≤ 1.3e-4; paper P = 0.55) (cell 59). |
| exc-touch-spikes-enphr | not_reproduced | The signed-rank test finds a change (p = 0.044 and 0.0091). The control mean 0.339 is just out of tolerance (0.27 ± 0.06) (cell 61). |
| auc-weak-strong | reproduced (fragile) | Neurons whose AUC rises have a lower control touch response under both readings: (a) 5.93 against 10.87, (b) 8.14 against 8.18 spikes/s. Reading (b) passes on a 0.04 spikes/s difference (rank-sum p = 1) (cell 63). |
| auc-groups | blocked: methods_underspecified | Reading (a) has all three tests holding but the means and group sizes out of tolerance (partial). Under reading (b) the reduced-AUC group's touch response changes (p = 0.021), so it is not reproduced (cell 65). |
| behavior-false-alarms | reproduced | Reading (b)(i) (per session, no correction) gives 6 mice. The other readings give 4–5 (partial). The paper has 8 mice; the data have 9 (cell 67). |

The paper states no chance level for any selection. The notebook's own shifted-spike controls, and my synthetic tests, show the r2 > 0.25 threshold is passed fairly often by chance (B6).

### B. Problems

1. **[affects a conclusion]** Cell 21, `group(sel="all")`: every "control" group includes the ION-cut cells. The claims specify control mice; the paper has 9 whole-cell E and 10 cell-attached FS ION-cut cells. The flagged variant shows the bias:
   - E touch latency moves from 7.68 to 4.97 ms (into tolerance).
   - FS spikes per touch moves from 1.50 to 1.69.
   - FS reading (a)(ii) goes from 1 to 3 values within tolerance.

   Because these groups cannot be cleaned (metadata), the outcomes of exc-vm-touch-whisking, fs-touch-response, exc-mainly-touch, exc-threshold-touch-vs-whisking and fs-vm-touch-whisking rest on groups the criterion does not define.
2. **[affects a conclusion]** `isolated_pulses` (gap 0.1 s on both sides) is the author's own rule and throws away the paper's 10 Hz tagging trains. On synthetic input, a 10 Hz train of 10 pulses keeps 1 and a 5 Hz train keeps all 5. The paper's rule is "driven within 5 ms" by 5 ms pulses at 5 or 10 Hz. As a result:
   - 29 of 67 VGAT cells are never tested and default to E, including cells with 11,087 and 16,350 spikes (cell 13).
   - Only 20 FS cells are found against the paper's 35.
   - The E groups may contain FS cells.
3. **[affects a conclusion]** `ca_waveform` is the author's own waveform measure, and it is combined with an approximate boundary. It drops 8 of 20 light-driven cells; driven cells have ratios up to 19 and durations up to 0.9 ms, which suggests the measure does not match the axes of Supplementary Fig. 6. This split is what makes fs-touch-response come out methods_underspecified.
4. **[affects a conclusion]** Spike detection (`detect_spikes_juxta` at 6 robust s.d.; whole-cell prominence of 20 mV) is never validated: no refractory-violation or signal-to-noise output. E rates are 2–6 times the paper's: nonwhisking 1.53 against 0.4; cell-attached E 2.45 and 6.19 spikes/s; AUC-group rates 10–16 against 3.4–7.3. This drives the value failures of exc-mainly-touch, fs-suppress-movement-spiking and auc-groups.
5. **[affects a conclusion]** The latency rule at the full sampling rate (`psp_measures`, `neg_onset_latency`) returns impossible values: 0.00 and 0.30 ms in FS cells, a minimum of 0.00 ms in E cells, and 0.10 ms for both laser averages. On a clean synthetic PSP with white noise the same rule recovers 4.8 ms (and a 4.2 ms hyperpolarization gives 4.4 ms), so something in the real averages at onset triggers it. The notebook does not investigate this. The 0.5 ms-step grand averages show onsets near 4.5–5 ms (thalamic) and 2.5–3 ms (cortical), which is qualitatively the paper's result. These latencies decide fs-vm-touch-whisking and the latency part of exc-thalamus-photoinhibition.
6. **[affects a conclusion]** The "more than half above r2 0.25" rule in the claims file (vpm-whisking-phase, fs-whisking-phase) is close to chance:
   - Spikes shifted to the next trial still pass for 16 of 29 VPM units and 9 of 17 FS cells (cells 29, 43).
   - Synthetic Poisson, phase-independent spikes give r2 > 0.25 in 26–30% of cells with a single sinusoid, and 65% with the FS double-fit rule.

   The outcomes still stand, on the own-against-shifted comparison and on counts well above these levels. This is a weakness of the claims file to report, not to correct.
7. **[affects a conclusion]** In pv-enphr-suppression, PV cells are identified by being inhibited (cell 13, `pv_inactivated`), so "3 of 3 inhibited" cannot fail. The paper's fourth, non-inhibited PV cell would be classed as E. The only independent parts, the latencies, fail.
8. **[affects a conclusion]** In the VPM files, the principal whisker is given once per file, and 11 of 20 units respond most to another whisker (cell 7). This metadata problem lowers vpm-touch's spikes per touch. The outcome holds even with the best-whisker variant.
9. **[affects a conclusion, weakly]** auc-weak-strong reading (b) passes on 8.14 against 8.18 spikes/s (Spearman 0.04). The AUC uses 5,000 random resamples with one seed, and reading (a) uses random windows with one seed. There is no seed-stability check, and the reading (b) result could flip.
10. **[does not affect a conclusion]** behavior-touches (cell 23):
    - The touch counts match only in a reading whose trial counts are more than twice the paper's.
    - Cortical performance uses the post-hoc flagged exclusion as "control", despite the notebook saying no_flagged never decides an outcome. Including the flagged mice gives 0.695, still within tolerance.
11. **[does not affect a conclusion]** Readings O10 and O11 are run only for exc-vm-touch-whisking. Every other whisking claim uses one mixed rule (O11 a-i epochs with the principal-whisker 250 ms rule; helper docstring), although the header says readings run wherever they apply. The effect on exc-vm was at most about 0.2 mV.
12. **[does not affect a conclusion]** The PV-ChR2 cell, which Supplementary Table 2 lists as FS, is classed E by FWHM (0.44 ms). It enters the E whole-cell group with a resting Vm of −34.9 mV (cell 13).
13. **[does not affect a conclusion]** The PSP amplitude (maximum 0–50 ms minus the pre-touch mean) is biased upward, so "every neuron depolarizes" is nearly guaranteed: amplitudes go down to 0.01 mV.
14. **[does not affect a conclusion]** thalamus-drives-fs: all 5 cells come from mouse anm260070; see the table.
15. **[does not affect a conclusion]** `resample` decimates 20 kHz averages with `[::2]` and no anti-alias filter (cell 53).
16. **[does not affect a conclusion]** Threshold readings O3 (a) and (b) give identical outputs (cell 33). That is plausible, since a trial's mean dVm/dt is close to 0, but it means the reading does no work.
17. **[probably does not affect a conclusion]** The "data_missing" verdict for the depolarized cells of Fig. 3 rests on per-trial median Vm > −20 mV, checked in whole-cell files only. A file held near 0 mV for the whole session would be classed cell-attached by the −20 mV mode rule, and the injected current per trial is never shown. The two cell-attached files with whole-cell-like slow components (1.09 and 1.3 mV) are PV-IRES-Cre. Supplementary Table 2 assigns Fig. 3 to the VGAT and PV-IRES-Cre × Ai32 lines, so the verdict is probably right.

**Step 4, blocked claims checked against the archive:**
- **Archive contents.** Version 0.220126.1853 has 148 NWB assets (121 icephys+ogen, 9 icephys, 18 ecephys). The measured variables listed are CurrentClamp(Stimulus)Series, OptogeneticSeries, ElectrodeGroup and Units, with no images.
- **ION-cut.** No ION, infraorbital, nerve, transection, cut, lesion or rabies term appears in the dandiset metadata or any of the 148 asset metadata records (I scanned them all). Supplementary Table 1 gives mouse ID, line, sex and dates only; Supplementary Table 2 gives counts only.
- **vpm-photoinhibition, rabies-vpm-input, exc-inhibition-timing, exc-inhibition-whisking.** These blocks hold.
- **Partly testable ION-cut claims.** ion-cut-exc-whisking, ion-cut-exc-phase, sensory-input-drives-fs and ion-cut-fs-phase could get an exploratory, non-deciding test on the flagged mice, because the flags were not chosen on those measures. The descriptive values (whisking change 0.39 mV, Vm coupling 0.11 mV) are close to the paper's ION-cut values. Mouse identity is unconfirmed (8 of 9 whole-cell and 7 of 10 cell-attached cells found), and the FS part has only 2 cells.
- **Circular ION-cut claims.** ion-cut-exc-no-touch, ion-cut-fs-no-touch and ion-cut-behavior would be circular on those flags, since the flags were chosen on touch response and performance.

### C. Not checked, and the output that would settle it

- **Spike detection quality.** Per-cell fraction of interspike intervals under 1.5 ms, spike signal-to-noise, and rates by mode set against the paper's.
- **Tagging coverage.** For each VGAT cell: the number of cortical pulses, the inter-pulse interval, and the tag result using the first pulse of each train.
- **Cause of the 0-ms latencies.** Full-rate touch- and laser-aligned averages from −2 to +2 ms, with dVm/dt and the 3 s.d. threshold drawn.
- **Fig. 3 recordings.** Per-file median injected current (CurrentClampStimulus) during trials, and trial-median Vm for the files classed cell-attached.
- **Pole times.** `pole_in_time − start` per L4 file. The first_touch_time scaling bug may also affect the pole times that AUC reading (a) uses; the notebook never checks this.
- **AUC stability.** AUC group sizes and auc-weak-strong / auc-groups outcomes over about 20 seeds.
- **ION-cut candidates.** A cross-tab of VGAT mice by presence of a VPM optical-fiber site against the flagged mice. Supplementary Table 2 suggests the ION-cut mice had no VPM fiber, which would narrow the candidates.
- **Exact −50.00 mV median.** The touch-reversal median is exactly −50.00 mV under both filters. I could not check it; the per-neuron touch reversals would settle it.
