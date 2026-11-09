I checked the notebook and helper module against the claims file and the paper, and re-tested helper functions on synthetic data. None of the 21 claims is fully reproduced. Four are reproduced (the two behaviour/electrode counts pairs and the PLV peak), two are partially reproduced, and 15 are not reproduced. The biggest problem is that every PAC result depends on a unit selection that marks most pure-noise pairs as significant.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| behavior-proficient | reproduced | Cell 16, all 120 trials: lowest 0.792, highest 0.967, every subject between 0.711 and 1.0. |
| behavior-no-difficulty-difference | partially_reproduced | Accuracy shows no effect under either reading (numeric term F 0.16, p 0.70; F 0.44, p 0.51). Response time shows no effect only with the `summary_file.csv` values (F 2.41, p 0.13). With the per-trial tables it does differ (F 12.3, p 0.0015 all trials; F 11.5, p 0.002 kept trials), and the two sources disagree in 7 of 10 subjects (cell 13). |
| electrode-counts | reproduced | Cell 20: 36/116/102, and 9 and 7 subjects, all exact. |
| correct-trial-counts | reproduced | Cell 22: means 100.9, 32.9, 34.8, 33.2 and 10.2 are within tolerance; per-subject ranges equal the paper's exactly. |
| erp-no-condition-difference | not_reproduced | The criterion is no electrode below p 0.05. Cell 24 finds 1 of 254 electrodes with the subject-wide null and 13 with the per-electrode null. Both counts are at or below the expected false-positive count (25.4), so the data are consistent with no effect, but the rule as written fails. |
| power-theta-sustained | not_reproduced | Cell 26: theta is sustained in 0 of 10, 0 of 9 and 0 of 9 subjects (electrodes: 1/36, 1/116, 11/102). MTL alpha is desynchronised in 0 of 10 subjects. |
| power-condition-exclusions | not_reproduced | Cell 28: 12 electrodes (6 PFC, 5 OFC, 1 MTL) in 5 subjects with the subject-wide null, and 69 with the per-electrode null; expected 8 (5 PFC, 3 OFC) in 4. |
| plv-theta-peak | reproduced | Cell 30, imaginary PLV: a 3 to 7 Hz local maximum in MTL-MTL 7/9, MTL-PFC 8/9 and MTL-OFC 4/7 subjects. The one-subject rule is lenient: a noisy 11-bin spectrum often has a local maximum among the four theta bins. |
| psi-theta-shift | partially_reproduced | Cell 32. Single-window (Methods) PSI: the post-versus-pre test fails in both networks (p 0.27, 0.56). Sliding-window PSI on raw values: OFC passes (p 0.027), PFC fails (p 0.079), which is the criterion's partial case. The code's PSI form passes both networks on raw PSI (p < 1e-4), but its z part rests on a miscalibrated null (B3). |
| crossspectral-shift | not_reproduced | Cell 34: post greater than pre at p < 0.05 in 1 of 7 systems (single-window PSI) and 2 of 7 (code form); 4 are needed for partial. The claims file's sliding-window reading was not run (B4). |
| phase-directing-counts | not_reproduced | Cell 36: 0 units in every system with single-window PSI; with the code form only 1 of 7 counts is within 10% (OFC 38), and MTL→OFC is 200 against 93. |
| crossspectral-equal-strength | not_reproduced | Cell 38: frequency p 0.016 (MTL-PFC) and 7e-5 (MTL-OFC); frequency × direction p 1.6e-4. This is only on units picked by the miscalibrated code form (B3), so it is weak evidence. |
| theta-peak-bands | not_reproduced | Cell 40: overlap with the paper's counts is 4 of 10 (all electrodes) and 5 of 10 (code-selected electrodes); 7 are needed for partial. |
| pac-mtl-spatial | not_reproduced | Cell 42/43: condition p 0.00717 against a threshold of 0.00714 (borderline), condition × frequency p 0.20, peak at 38.5 Hz. Units are code-selected (B3). |
| pac-frontal-no-condition | not_reproduced | Condition effects fall below 0.05/7: PFC spatial condition × time 3.7e-6, PFC temporal three-way 2.9e-6, OFC spatial condition 1.8e-6. |
| pac-mtl-pfc-spatial | not_reproduced | Condition p 0.19 (a) and 0.17 (b); the spatial minus identity difference is negative. |
| pac-mtl-pfc-temporal | not_reproduced | Condition p 0.36 and 0.45; the difference is negative. |
| pac-pfc-mtl-no-condition | not_reproduced | Temporal model condition p 5.8e-6 (a) and 7.7e-7 (b), both below 0.05/7. |
| pac-mtl-ofc-spatial | not_reproduced | Condition p 0.015 (a) and 0.031 (b), above 0.05/7. The peak at 9.5 Hz does match. |
| pac-mtl-pfc-direction | not_reproduced | Condition × direction is significant but larger for PFC→MTL (the wrong direction). Direction p 0.32 and 0.96, with MTL→PFC higher. |
| pac-mtl-ofc-direction | not_reproduced | Spatial model: direction p 0.13, condition × direction p 0.17. The temporal model has effects below 0.05/15. |

The notebook treats no claim as blocked. I listed the archive (S3 `fcx-2/`); `live/` holds only the 10 subject tars, the docs and `analysis_scripts.tar.gz`, so nothing more is there to test.

**B. Problems**

1. [affects a conclusion] Time axis (cells 10–12, `WIN`). The code's windows are exact sign mirrors of the windows the descriptor implies:
   - Encoding: the code uses [0, 1.5] s of `encmain`; with stimulus onset at column H, the descriptor gives [−1.5, 0].
   - Postcue: the code uses [0.3, 1.2] s of `proc`; with `proc` starting 0.3 s before column I, the descriptor gives [−1.2, −0.3].
   - Baseline: the code uses [0.65, 0.85] s of `pre`; with `pre` starting about 0.1 s after column G, the descriptor gives about [−0.85, −0.65].

   A sign mirror like this suggests a sign-convention mismatch somewhere. The notebook's high-gamma and evoked-response check could not place the events, and the descriptor reading was never run. Every neural outcome (no sustained theta, no shift, and so on) rests on this unchecked choice.
2. [affects a conclusion] Response-time source (cell 18). The claim is judged on `summary_file.csv`, whose values are of unknown provenance: they do not equal the descriptor's "mean over all correct trials" of the trial tables. They were chosen because they match the paper. The per-trial data give a significant condition effect.
3. [affects a conclusion] `psi_code`. I tested it on independent pink noise (100 trials, 8 channels): z SD 27, with 46% of pairs above 1.96 and 39% below −1.96. The observed per-trial-mean PSI is z-scored against a null of a different statistic (shuffled trial-mean phasors), so the null is far too narrow. This selection supplies the units for crossspectral-equal-strength, theta-peak-bands (b), all 8 PAC claims, the code variant of crossspectral-shift and the z part of psi-theta-shift.
   - The sliding-window `psi_z` is also miscalibrated (noise z SD 2.09, 54% beyond ±1.96), which inflates the cell 32 sliding-window counts.
   - The single-window form is calibrated (SD 1.02) but weak: a strong 20 ms lag gave z 1.41.
4. [affects a conclusion] Cross-spectral PSI was computed only for the single window and the code form (`analyse_subject`: `if mode != "mtmfft": continue`). The claims file's M5 reading (sliding windows averaged) was never run for crossspectral-shift, phase-directing-counts or anything downstream.
5. [affects a conclusion] ERP baseline (`analyse_subject`). The baseline subtracted is the trial-averaged baseline, a per-channel constant that leaves the between-trial t and F tests unchanged. The claims file's "subtracting the temporal mean of the baseline" is normally done per trial in FieldTrip. Per-trial correction would change the test, and the deposited script was not shown.
6. [does not affect a conclusion] PSI is computed as one value over 3 to 7 Hz. The Methods describe "electrode pair and frequency-resolved" null PSI with 2 Hz bandwidth, and that reading was not run. The null pairs A(f) with B(perm f), a literal reading of "shuffled the frequencies in one signal"; shuffling the order of the coherency spectrum is another reading that was not run.
7. [does not affect a conclusion] `within_unit_anova` matches an OLS fit with unit intercepts exactly (my check), and its false-positive rate is about 5% on independent data. On autocorrelated PAC maps (19 × 16 bins, about 10^4 to 10^5 residual df) it will be anti-conservative. It follows the paper's model, but it biases the claims of absence (pac-frontal-no-condition, pac-pfc-mtl-no-condition) toward failing.
8. [does not affect a conclusion] Downstream analyses use the notebook's own 12 exclusions, not the paper's unknown 8. The resulting pair and unit counts (172, 302; 35/110/97) are within tolerance.
9. [does not affect a conclusion] Theta-peak maxima at the 1.5–4 and 6–10 Hz filters are remapped to 2–5 and 5–8 Hz for PAC. This is stated as an assumption and is reasonable.

**C. What I could not check**

- **Deposited scripts.** I did not open `analysis_scripts.tar.gz` (6.9 KB), since it is part of the dataset. So I could not confirm that `psianalysis.m` really uses the miscalibrated null of `psi_code`, the ERP baseline method, or the window latencies. Quoting the relevant script lines in the notebook would settle B1, B3 and B5.
- **Time axis.** Running power-theta-sustained, power-condition-exclusions and psi-theta-shift under the descriptor's placement would show whether B1 matters. So would a per-subject evoked or high-gamma plot for the electrodes with the largest responses, in place of the RMS pooled over all channels.
- **PSI calibration.** A z histogram for each PSI form under a trial-shuffled (between-trial) surrogate on the real data would show calibration directly.
- **Missing analyses.** Cross-spectral PSI under the sliding-window reading, and PAC models on all units without selection.
- **Response times.** The provenance of `summary_file.csv` response times, for example a check of medians or of kept-trial subsets per subject.
