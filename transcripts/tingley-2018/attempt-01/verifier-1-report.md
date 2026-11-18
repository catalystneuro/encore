**Verification report, round 1: Tingley & Buzsáki 2018 on dandiset 000213 (0.250624.0438)**

The claims file holds 25 claims. The notebook tests 18 and treats 7 as blocked. I did not see an attempt record, so the counts below come from the claims file and the notebook. The paper text is the PMC6605060 author manuscript, saved at `paper/PMC6605060.xml` and `paper/PMC6605060.txt`.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| ls-neuron-count | reproduced | Cell 16: 1,696 LS units against 1,647 (+3.0%, inside ±164.7), 62 sessions, 5 subjects. |
| hpc-unit-count | partially_reproduced | Cell 18: CA1 2,593 against 2,297 is outside ±229.7, and CA3 624 is inside ±65.4. The sum, 3,217, is +9.0%, inside 10%. |
| ls-active-neurons | reproduced | Cell 20: 793 against 840 (inside ±84). The condition count is lower: 3,694 against 4,393. |
| fig2-ls-phase-vs-shuffle | not_reproduced | Cell 22: 408 of 783 = 0.521 against 0.89 ± 0.089. Even at p < 0.05 it is only 0.660. |
| fig2-ls-phase-beats-rate | not_reproduced | Cell 24: neurons 0.845 (needs ≥ 0.872), conditions 0.481 (needs 0.624–0.762), sessions 58/58. "Partial" requires more than half of conditions; 0.481 falls short. With whole trials held out the values drop to 0.729 and 0.354. |
| fig2e-ls-phase-lower-mse | reproduced | Cell 26: conditions p = 2.5e-232 (N = 3,660), sessions p = 2.9e-23 (N = 58). Phase is lower in both. |
| fig2fg-mse-difference | partially_reproduced | Cell 30: LS conditions −1,045 (inside tolerance), LS sessions −1,132 (outside ±102.4), hippocampal values −167 and −221 (far from −33 and −25). The LS values are negative and larger in magnitude than the hippocampal ones at both levels. |
| fig1i-hpc-rate-phase-equivalent | reproduced (weak) | Cell 28: KS p = 0.115 over 315 fields and p = 0.874 over 35 sessions, so the criterion is met. But N is 1/6 of the paper's 1,820 because of problem 1. Phase − rate is negative in all four subjects, and over all 5,045 hippocampal conditions KS p = 7e-48. |
| ls-few-place-fields | not_reproduced | Cell 32: LS 0.058 (just inside tolerance), hippocampus 0.062 against 0.317. LS is not lower (χ² p = 0.41). |
| hpc-place-field-properties | partially_reproduced | Cell 34: fraction 0.146 against 0.499 and median peak 12.5 against 8.5 Hz are both outside tolerance. Width 40 against 38 bins is inside. |
| ls-place-fields-unstable | partially_reproduced (weak) | Cell 36: reading (b) gives LS 88.7% against 84.6%, p = 3e-4, with both medians far from 41.5 and 10. Under reading (a), the one makeFig2.m computes, LS is lower (7.0 against 10.5 Hz). |
| fig1e-phase-info-smaller-scale | partially_reproduced | Cell 38: medians 10 and 19 bins against 15 and 29. Phase is smaller at p = 4.9e-18, which passes p < 0.05 but not 1e-40. |
| fig1g-phase-more-info-fine-scale | partially_reproduced | Cell 40: fine scales pass 0 of 2 (the 2-bin smoothing is +0.015 at p = 5e-3, the 3-bin one is negative). Coarse scales pass 44 of 44. |
| fig4d-depth-gradient | partially_reproduced | Cell 42: the pooled within-animal correlation is r = −0.365, p = 0.005, but DT8 has r = +0.24. This rests on the untested assumption that the first depth in the session name is the LS depth. |
| fig4e-onset-depth | not_reproduced | Cell 44: DT5 r = 0.08, DT9 0.07, DT2 0.12, every p > 0.5. |
| fig6c-ca3-coherence-increases | not_reproduced | Cell 46: CA3 slope signed-rank p = 0.83; CA3 above CA1, Mann-Whitney p = 0.235. |
| fig6d-cfc-stronger-ca3 | reproduced (provisional) | Cell 48: as computed, CA3 > CA1 at p = 0.041, and the slopes are positive in both groups (p = 0.002 and 0.001). The CA1 group does not follow the criterion (problem 3), and the p = 0.041 is marginal. |
| figs7-ensemble-ls-phase-best | not_reproduced | Cell 50: LS phase MSE is higher than hippocampal phase at sizes 15 and 20 (4,738 against 4,597; 4,260 against 3,971). It is higher than hippocampal rate at every size (for example 4,738 against 3,119). The small p values printed are two-sided and come from differences in the wrong direction. |
| fig5-assemblies | blocked: too_large | "Not runnable" is not an allowed reason. The data (simultaneous LS and hippocampal spikes, position, LFP) are present and the GLM method is in the Methods, so a subsample of pairs could have been tested. |
| fig5g-assembly-neurons-stronger-phase | blocked: too_large | Depends on fig5-assemblies. |
| fig6e-assembly-position | blocked: too_large | Depends on fig5-assemblies. |
| speed-independent | blocked: methods_underspecified | Accepted: the Methods do not describe the speed and phase-precession test. Position, and so speed, is in every file. |
| ls-information-lower | blocked: methods_underspecified (weak) | `olypher_peak` already exists, and the scale is about 1.12 cm per bin outside DT2. The LS against hippocampus direction of the comparison could have been tested. |
| figs6-reference-frame | blocked: metadata_insufficient | I checked all 67 asset records from the API: none mentions rotation, and no session is marked as a rotation session. The loader skips `processing/behavior/allocentric_frame_tracking` without reporting what it holds. |
| fig7-dynamic-weighting-model | blocked: other | Accepted: this is a simulation and needs no data. |

### B. Problems

1. **[affects a conclusion]** `rate_map` (used by `place_fields` and for the stability values) smooths with a 5-bin box filter (`matlab_smooth`). In buzcode e615663, `bz_firingMap1D` builds `rateMaps` with FMAToolbox `Smooth`, a Gaussian whose SD is tau bins. Only `rateMaps_box` uses the box filter. On synthetic Poisson place cells (20 trials, a 10 or 20 Hz field), the box version found a field in 31–76% of cases and the Gaussian SD-5 version in 93–100%. The box version also gives a peak CV of about 0.9. This plausibly explains the 6% hippocampal field fraction (paper 31.7%) and the CVs near 85%. It affects ls-few-place-fields, hpc-place-field-properties, ls-place-fields-unstable, fig1i, fig1e, fig1g, and the hippocampal part of fig2fg. The tau the paper used is unknown; the module assumes 5.
2. **[affects a conclusion]** Cell 50 tests with two-sided t-tests and never checks the direction. A reader who looks only at the p values would see "p < 0.001" at size 15 although LS phase is worse.
3. **[affects a conclusion]** Cells 46 and 48 put every session without `ca3` units into CA1 (`group = "CA3" if has_ca3_units else "CA1"`). That brings in 19 sessions with no hippocampal units: the 17 DT8 sessions, DT7 20170317 (unlabelled units) and DT7 20170324 (no units). The criterion defines CA1 sessions as those with `hpc` units, which would give 36 sessions, not 55. DT8's median coupling (0.041) lowers the CA1 group, and fig6d's p = 0.041 may not survive the correct grouping. Separately, every CA3 session is from DT5 or DT9, so the comparison is confounded with animal: within DT9, CA3 coupling is below CA1 (0.049 against 0.057).
4. **[affects a conclusion]** `HPC_LABELS` includes `ca3`, so the theta reference can be a CA3 channel, while the paper uses the CA1 pyramidal layer. On the chosen channel the 6–9 Hz to 1–4 Hz power ratio is below 1 in 14 of 16 DT5 sessions (0.33 to 0.97, cell 11), and DT5 spike-theta locking is weak (mean resultant length 0.012 to 0.32). DT5 supplies 1,501 of the 3,660 decoded LS conditions, so a poor theta reference could weaken every phase claim. This was never checked.
5. **[affects a conclusion]** In `decode_cell`, samples are split at random across the trial-by-bin pool with 20-bin smoothing, so test samples share smoothed content with training neighbours in the same trial. The paper's code does the same, and the Methods' phrase "entire block of trials" is ambiguous. The whole-trial variant lowers phase-beats-rate to 0.729 of neurons and 0.354 of conditions (cell 24).
6. **[affects a conclusion]** fig4d and fig4e depend on reading the first depth in the session name as the LS depth. The only support is the ca3 pattern in DT9. DT2's first depths of 3,324–3,612 µm fit an LS probe, but DT8 and DT9 are ambiguous (for example `0um_0um`).
7. **[does not affect a conclusion]** The smoothing windows in `info_curves` differ between features at the same nominal w. For rate, `matlab_smooth` uses w, or w−1 when w is even, so w = 2 means no smoothing. For phase, `circ_smooth` uses 2·ceil(w/2)+1. I confirmed this on an impulse: w = 2 gives support 1 for rate and 3 for phase; w = 3 and w = 4 are identical for phase. The port matches circ_smoothTS. It shifts the fig1e medians by about 1–2 bins.
8. **[does not affect a conclusion]** The LFP clock check in cell 13 is weak. Theta has a period of about 125 ms, so shifting by ±200 ms reduces locking only modestly (median ratio 1.2). DT5 peaks sit consistently at −25 to −75 ms.
9. **[does not affect a conclusion]** In `place_fields`, `peak_hz` is the RMS-smoothed peak, which is at least the mean peak. It inflates the median peak rate slightly (12.5 Hz).
10. **[does not affect a conclusion]** The blocked-claim reasons in cell 0 ("not runnable") are not from the allowed list.

Checked and found correct: `circ_corrcl` (it detected a real dependence and gave p = 0.46 on null data), `decode_1d` and `_nearest_template` (a perfect feature gives MSE 0 and a permuted one gives the uniform level, about 6,640 against 6,666), the port of circ_smoothTS, the logic of bz_getPlaceFields1D apart from its input map, and the `/n_trials` scaling in fig1g (it matches makeFig1.m).

### C. What I could not check, and what output would have let me

- Place-field results with the input map built as in `bz_firingMap1D` `rateMaps` (Gaussian SD tau): field fractions, field counts and CVs for hippocampus and LS. This needs a rerun with that map.
- fig6c and fig6d with CA1 sessions limited to the 36 sessions that hold `hpc` units, plus a per-animal test within DT5 and DT9.
- The quality of the theta reference: power spectra of the chosen channel for each session, whether it is an `hpc` or `ca3` channel, and fig2 results restricted to sessions with a 6–9 Hz to 1–4 Hz ratio above 1.
- One-sided tests with the mean differences in cell 50.
- What `allocentric_frame_tracking` holds (keys, shapes, units) in a few files. This decides whether figs6 is blocked by missing metadata.
- A subsampled peer-prediction GLM, for example 500 pairs with a coarser window grid, to estimate the assembly fraction.
- I did not read the per-cell decoder in DavidTingley/scratch, so I cannot confirm whether it splits by samples or by trials.
