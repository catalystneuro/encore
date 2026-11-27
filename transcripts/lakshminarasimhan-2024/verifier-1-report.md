**A. Outcomes**

The claims file has 36 claims. 12 are about this dandiset; 24 use data generated elsewhere. The notebook tests 6 and blocks 30.

| Claim | Outcome | Reason |
|---|---|---|
| wm-sessions-link | partially_reproduced | Only one mouse, anm00264943, has both ALM and thalamic units, and its totals match exactly: 151 ALM and 72 thalamic (cell 12). It has 11 sessions, though: 5 ALM and 6 thalamic. The criterion expects 5 sessions with tolerance 0, and the notebook never checks the session count. The link itself is not in doubt. |
| fig6-wm-choice-r2 | not_reproduced | The largest test R2 over R1/R2 × T1/T2 at the claim seed is −0.247 (cell 17). Across five seeds the means run from −30.6 to 0.10 and the medians top out at 0.39, against a band of 0.873 to 1. Training R2 is 0.95 to 0.99, close to the paper's 0.97, but the criterion is test-set R2. |
| fig6c-wm-leading-pcs-drive-choice | partially_reproduced | Read literally, the criterion is met. Under R2 (pooled units), PC 1 or 2 is the argmax and PCs 1–3 beat 4–16 at every seed for T1 (cell 19). Under R1 (per session, which matches Figure 6C's n = 5) the argmax is PC 16 at every seed. Even under R2, the PC1 and PC2 alignments (0.077 and 0.110) are at or below the random-direction value of 0.110 for 53 units (cell 20). So the data do not show a "large influence" of the leading PCs (problem 3). |
| figs6d-wm-thalamic-r2 | not_reproduced | Mean test R2 runs from −5.47 to −1.98 over all seeds and readings, and no unit is positive under P1 (cell 24). Expected 0.70 ± 0.01. Training R2 is 0.74 (P1). |
| fig6d-wm-top5-pcs | not_reproduced | No combination of T, P and N falls within 0.59–0.67 at any seed (cell 26). The underlying test R2(k) is negative for every unit at k = 16, so the N1, N2 and N3 ratios are undefined, not merely off. |
| figs6f-ct-alignment-not-significant | not_reproduced | This is a claim of absence, and at the claim seed every 16-PC reading gives p < 0.05. The main reading gives p = 8.3e-6 (cell 28); only T2/P1 at seeds +2000 and +4000 reach p ≥ 0.05. The all-units variant gives p = 1.0, a large effect in the opposite direction (readout far above PC1), which does not fit "difference not significant" either. |
| fig6-motor-hand-r2, fig6c-motor-low-variance-pcs, figs6d-motor-thalamic-r2, fig6d-motor-top5-pcs, fig6e-motor-single-trial | blocked (data_missing) | I checked the archive. DANDI:000009 holds only ALM, SNr and thalamus extracellular files plus intracellular files, with no motor cortex and no hand tracking. A DANDI search for "Sauerbrei", "Hantman", "motor thalamus" and "reach-to-grasp" finds no Sauerbrei et al. 2020 deposit (000221 is a different study). No part can be tested. |
| fig6d-more-pcs-in-motor-task | blocked (data_missing) | The comparison needs the motor data. The working memory half is tested above and fails. |
| 24 simulation claims (fig1c … figs5j) | blocked (too_large); figs5cd is methods_underspecified | The data are not deposited. The timed RFLO run gives ≥ 14.5 h for fig1c alone (cell 30). The M = 1 time (22.7 ms) is inflated by first-call overhead, since M = 8 takes 9.6 ms, but the total still exceeds the limit. figs5cd follows its criterion. |

**B. Problems**

1. **[affects a conclusion]** Cell 12, wm-sessions-link. `ok` tests only the unit totals and ignores the criterion's "five sessions, tolerance 0". The mouse has 5 ALM and 6 thalamic sessions. Also, "sessions holding both: 0" is a hard-coded string, not computed. It happens to be true, since each file names one region (cell 6).

2. **[affects a conclusion]** fig6-wm-choice-r2, figs6d-wm-thalamic-r2 and fig6d-wm-top5-pcs (helpers `readout_fit`, `thalamic_regression`). The negative test R2 is not a code bug. I tested the helpers on synthetic spikes:
   - A stationary choice signal with 150 trials gives test R2 of 0.95–0.99.
   - A choice signal that ramps from zero gives test R2 near 0 even with 1200 trials, while training R2 is about 0.85.
   
   So the paper's procedure (OLS on 2 × 130 heavily smoothed bins, 10% test sets of about 5–8 trials per choice) is very fragile. The notebook's training values (0.97 for choice, 0.74 for thalamus) land near the paper's numbers. I cannot tell whether the paper reported in-sample values or used details it does not state. The not_reproduced outcomes stand under the claims file, but they say more about the method than about the data.

3. **[affects a conclusion]** Cells 19–20, fig6c. Criteria (a) and (b) only rank PCs 1–16 against each other. From the R2/T1 profile, the summed squared alignment over PCs 1–16 is about 0.075. A random direction in 53 dimensions would give 16/53 ≈ 0.30. The readout therefore lies mostly in PCs 17–53, which runs against "leading PCs have a large influence". The readout being analysed also has negative test R2.

4. **[affects a conclusion]** `thalamic_analysis` with `alignment`, figs6f (16-PC weights). `w_tc = U @ b` is confined to the top-16 PC span. That span contains PC1 fully but only about 27% of the readout's norm (problem 3), so a random vector in it would align about 0.20 with PC1 and about 0.055 with the readout. The observed values are 0.094 and 0.071: PC1 is below its chance level and the readout above its own. The significant "PC1 > readout" result is mostly this geometry. The test, as the criterion specifies it, does not compare like with like.

5. **[affects a conclusion]** Claims file, figs6f criterion. "Reproduced when the one-sided p ≥ 0.05" is satisfied trivially by a strong effect in the opposite direction, as the all-units variant shows (p = 1.0, d_z about −10). I am reporting this, not correcting it.

6. **[does not affect a conclusion]** figs6f all-units variant. The readout alignment of about 0.25 is inflated because both OLS weight vectors share the (HᵀH)⁻¹ factor, which pulls them toward the same low-variance directions.

7. **[does not affect a conclusion]** `thalamic_analysis`. `w_ro` is taken at the readout's best sigma, while `w_tc` and `U` come from each thalamic unit's best sigma, so the alignments mix smoothing widths.

8. **[does not affect a conclusion]** Cell 26. N1 and N2 are ratios of negative R2 values (e.g. N1 of −8.29 and 5.51). N3 min-max rescales curves that decrease with k, so its 0.84 at k = 5 only reflects that decline. These are printed as if they were explainable-variance fractions.

9. **[does not affect a conclusion]** The markdown and comments in cells 2 and 8 say 136 extracellular and 37 intracellular files; the output says 137 and 36.

10. **[does not affect a conclusion]** Checked and found sound:
    - delay onset is `pole_out_time` (cue − pole_out has median 1.30 s);
    - choice is the lick direction of correct trials, and T1 excludes stimulation;
    - the clock check shows choice information rising in the delay and after the go cue;
    - PCs come from training data only, sigma is chosen on validation, and the test set is held out, with no leakage;
    - ALM and thalamic splits are independent, which is correct because they come from separate sessions;
    - the helpers `split`, `average`, `pcs`, `readout_pc_alignment` and `r2` behaved correctly on synthetic inputs.

**C. Could not check, and outputs that would have helped**

- Whether 0.70 and 0.97 are reachable at all with 10% test sets. A noise ceiling would settle this: split-half reliability of the test-set trial averages for each thalamic unit and for the choice readout.
- How R2 depends on the number of test trials, for example 10% versus 50% test splits.
- The readout's alignment with all PCs (1 to d), with the chance level 1/d for squared alignment shown next to it.
- For figs6f, chance alignments of a random vector in the 16-PC span with PC1 and with the readout, computed per fit.
- A computed session count per region for wm-sessions-link.
- The R1 standard errors for fig6c, plotted in cell 20, are not printed numerically.
- The Figure 6C/6D and S6 images in the paper, to compare profile shapes. They could not be rendered here.
