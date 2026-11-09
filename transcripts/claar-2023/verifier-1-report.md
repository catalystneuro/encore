**A. Outcomes** (37 claims in the claims file; the two notebooks cover all 37)

| Claim | Outcome | Reason |
|---|---|---|
| stim-depths | blocked (metadata_insufficient) | The trial table gives only "superficial"/"deep" (cell 3), and the archive description lists no stimulating-electrode depth. I agree with the notebook. |
| eeg-good-electrodes | reproduced | `is_data_valid` gives 23.07 ± 4.01 good electrodes per subject, against the paper's 23 ± 4 (cell 13). |
| fig1d-two-erp-peaks | not_reproduced | Every deep site shows both peaks (18/18), but only 0 to 2 of 12 superficial sites lack a late peak, under every reading (cell 17). |
| fig1-supp1-example | reproduced | The example is 571619 MOs-deep, the only subject stimulated at both MOs depths. At high current, all awake trials: duration 1.085 s and magnitude 10.99 SD·s, both within tolerance (cell 15). |
| fig1e-erp-duration | reproduced | High current, awake, reading (a): 0.44 against 0.53 s, p = 0.51 (cell 19). The superficial SEM is 0.14, against 0.0 printed. |
| fig1f-erp-magnitude | reproduced (fragile) | Only one of 8 combinations passes: high current, quiet trials, reading (b), giving 2.90 against 5.33, p = 0.044. The deep mean is 0.03 inside its tolerance, and reading (b) rests on the author's own denominator (problem 5). |
| fig1-supp2-first-peak-flips | blocked (metadata_insufficient) | The stimulation coordinates are not in the files. EEG electrode x/y/z are read (`read_meta`) but never printed, so the "both signs occur" part may have been testable. |
| fig2c-superficial-quiescence | reproduced (fragile) | Only 2 sites. High current, all awake, 1 ms bins, reading (a): 84.0 ms against 94.2 ± 16.1 (the per-site values are 59 and 109 ms). With 5 ms bins it is 112.5, out of tolerance (cell 23). |
| fig2c-deep-triphasic-cortex | partially_reproduced | The triphasic pattern holds at 16/16 deep sites. No combination puts all three values in tolerance: the early peak is 20 to 65 Hz against 38.1 ± 4.2 (cell 24). |
| fig2f-thalamus-triphasic | partially_reproduced | The pattern holds at 12/14 deep sites and is mostly absent with superficial stimulation. No combination puts all three values in tolerance (cell 25). |
| fig3abc-decay-with-distance | blocked as run; partly testable | The archive holds raw LFP for every probe channel plus all sorted units with area and waveform duration. The spiking magnitudes (MO 30.9 against VIS 1.8 SD·s in 571619, which has 95 MO and 47 VIS RS units) need no layer labels. |
| fig3d-magnitudes | blocked as run; partly testable | Same as fig3abc: the 3 spiking medians and their tests could have been run. LFP magnitudes per area are possible, with the layer-1 exclusion as a stated deviation. |
| fig4-unit-counts | not_reproduced | RS counts are 290/1370/853/3162 against 870/4110/2559/9363 (cell 11). Each paper count is about 3× the dataset count, exactly 3× for three of the four (problem 2). |
| fig4ad-initial-excitation | not_reproduced | "Stimulated above non-stimulated in every session" fails under all 16 combinations. Means are 2.4 to 4.8% against 0.5% (non-stimulated) and 24 to 39% against 17.8% (stimulated) (cell 13). |
| fig4be-off-period | not_reproduced | Increased units: mean 0.7 to 1.4% (against 0.4), maximum 11 to 18% (against 2.8). 2 to 6 of 7 superficial sites show non-stimulated decreases, so the "deep only" pattern fails. 18/22 sites are reduced under one reading (cell 16). |
| fig4cf-rebound | partially_reproduced | Stimulated cortex holds at medium current: 16/16 deep against 1/6 superficial. Non-stimulated areas fail: 14/17 or 5/17 deep against 6/16, and never 0/7 superficial (cell 18). |
| fig4-supp1-fs-like-rs | partially_reproduced | Qualitatively FS behave like RS in every row (cell 20). FS counts are about a third of the legend's (cell 11). |
| fig5a-thalamus-modulated | reproduced | For example, high current, pooled FDR, reading (a): 1.9% against 42.7%, p = 0.002. The superficial n is 4 against the paper's 5 (cell 27). |
| fig5c-burst-probability-depth | partially_reproduced | Medium current, awake, reading (b): deep median 0.117 and U-test p = 0.018. The superficial median is 0.002 where the tolerance is exactly 0 (problem 9) (cell 29). |
| fig5e-early-latency | partially_reproduced | Cortex fires first (about 4.3 ms) and p < 0.05, but SM-TH is 8 to 9.6 ms and the difference is 3.8 to 4.9 ms against 6.9 (cell 32). |
| fig5f-rebound-latency | not_reproduced | SM-TH is earlier in direction only. In the rows shown, the difference is 2 to 19 ms against 36, and p < 0.05 in at most 1 row (cell 33). |
| fig6a-csd-sink | blocked (metadata_insufficient) | No layer labels in the files. Layers could only come from an outside CCF-atlas lookup of the electrode coordinates. |
| fig6-supp1-erp-deep-csd | blocked (metadata_insufficient) | Needs the same layer-resolved CSD as fig6a. |
| fig6b-bursts-cortical-rate | not_reproduced | Mean r is 0.13 to 0.24 against 0.4 ± 0.04, with 6 to 10 of 13 sites significant (cell 36). |
| fig6c-cortical-rate-late-erp | not_reproduced | Mean r is 0.21 to 0.32 against 0.5 ± 0.04 (cell 37). |
| fig6-supp2-late-erp-bursts | reproduced | High current, late GFP: 13/13 significant, r = 0.46. Against SM-TH rate, r is 0.06 with 4/13 significant (cell 38). |
| state-trial-counts | reproduced | Medium current, deep sites: 97 [86–104], 21 [16–27], 120 [120–120]. This matches the paper exactly, IQRs included (cell 23 of the EEG notebook). |
| fig7c-erp-duration-state | reproduced | High current, unmatched, deep, reading (a): 0.56/0.30/0.28 s, Friedman p = 5e-4. At medium current (the reading the trial counts point to), running and anesthetized are out of tolerance. |
| fig7d-erp-magnitude-state | reproduced (fragile) | Passes only under high current, unmatched, deep, reading (b): 5.45/1.89/1.37, p = 1e-4 (cell 26). |
| fig7e-baseline-rates | reproduced | Every row holds. Cortex F[2,30] with 16 animals and SM-TH Friedman with n = 13 match the paper's degrees of freedom (cell 40). |
| fig7f-early-latency-state | reproduced (weak) | State effect p = 0.09 to 0.85 and region effect p < 0.05, but with 6 to 8 animals against 13 (cell 41). |
| fig7g-rebound-latency-state | partially_reproduced | State effect and "running earlier" (corrected) hold in every row. No row has all six means in tolerance; SM-TH quiet is about 175 against 156 ms (cell 42). |
| fig7h-burst-probability-state | partially_reproduced | Friedman p < 0.001 and quiet is highest. Medians do not match: best is 0.15/0.03/0.006 against 0.1/0/0 (cell 43). |
| fig8b-pcist-awake-anesthesia | partially_reproduced | Awake exceeds anesthetized at 29 to 30 of 30 sites, p ≤ 3e-7. The anesthetized mean is 13.0 to 13.4 or 21.7 to 22.1, outside 16.5 ± 2.4 (cell 29). |
| fig8c-pcist-depth | reproduced | High current, all awake trials: 31.6 against 49.6, p = 0.006 (cell 31). |
| fig8d-pcist-three-states | partially_reproduced | Ordering, state effect and running > anesthesia hold. Quiet is 42 to 43 against 55.2 ± 10.3, and at high current the quiet-running pair is not significant (cell 33). |
| fig8e-pcist-recovery | reproduced (fragile) | Only 1 of 8 combinations passes: medium current, "first" trials, four-stage sample of 8 sites, with ANOVA p = 1.6e-4, 8/8 sites rising and q(rec1–rec2) = 0.32 (cell 35). |

**B. Problems**

1. **Artifact mask misses the artifact sample** [affects a conclusion] (`eeg_epochs`; cells 7–8). The clock check shows the artifact at window index 24 (656 µV), one sample before the onset index k. The mask copies samples k−5 to k−1 into k to k+4, so the artifact sample stays in and is also copied into k. Cell 8 misreads this as "begins at the sample of the trial onset."
   - On synthetic input, this residue after the zero-phase 0.1–100 Hz filter leaves about 68 µV of ringing from −20 to −2 ms and from 2 to 10 ms.
   - That window is inside the PCIst baseline and response windows, the early GFP peak, and the baseline SD.
   - Several superficial sites have their early peak at exactly 2 ms (the window edge).
   - Magnitudes and PCIst values that sit at tolerance edges (fig1f, fig7d, fig8b to fig8e) may move.
2. **Figure 4 unit counts point to an untested reading** [affects a conclusion] (cell 11; claims-file header, intensity readings). The paper's counts equal 3× the dataset counts: 290×3 = 870, 1370×3 = 4110, 853×3 = 2559, and 3162×3 = 9486 against 9363. Every FS difference is also a multiple of 3. So Figure 4 most likely pools the three intensities (unit × intensity). Neither the claims file nor the notebook runs an "all intensities" reading, yet it bears on fig4-unit-counts, fig4ad, fig4be, fig4cf and fig4-supp1. This is a gap in the claims file; I report it and have not corrected it.
3. **fig3abc and fig3d blocked too broadly** [affects a conclusion]. The spiking magnitudes need only units by area, and the archive holds raw LFP with electrode tables. Part of each claim was testable.
4. **Reading (b) of magnitude is close to a rescaling of (a)** [affects a conclusion] (`erp_metrics`). Dividing by the area under |z| in the baseline is a near-constant for any z-scored series (about 1.6 SD·s). fig1f passes only because this rescaling moves p from 0.053 to 0.044. The paper prints SD·s, the unit of reading (a). The choice is stated, but it is weak.
5. **fig7f is an absence claim tested on 6 to 8 animals against the paper's 13** [affects a conclusion] (`lat_state`). This low power favours "no state effect."
6. **Claims-file tolerance for fig5c** [affects a conclusion]. A tolerance of 0 on the superficial median is stricter than the paper's printing precision of 2 decimals; 0.002 would print as 0. Under printing precision, fig5c reproduces.
7. **"First" trial matching for awake is wrong** [does not affect a conclusion] (`eeg_site_summary`, `match_trials`). Awake is built as quiet followed by running, so "first" picks quiet trials first, not the first in time. fig8e's passing row also has its awake mean in tolerance under random matching.
8. **Unexplained PCIst outlier** [does not affect a conclusion] (cell 35). At high current with "first" matching, anesthetized PCIst is 48.2 ± 21.2, and 70.6 ± 32.6 on the four-stage sample. The notebook does not investigate it, and it suggests a problem in the early isoflurane trials or the EEG.
9. **Weak quiescence and triphasic tests** [does not affect a conclusion] (`quiescence`, `triphasic`). Quiescence is the first run of below-baseline bins, so with 1 ms bins a single noisy bin ends it (569073 SSp-deep: 2 ms). The "triphasic" flag needs only one bin below baseline.
10. **Small areas drive the fig4ad maxima** [does not affect a conclusion] (cell 13). Non-stimulated mean and maximum are computed per area only; the per-session pooled reading is not printed. The 50% maximum comes from 1 of 2 ACA units.
11. **fig8d analysed per site** [does not affect a conclusion] (cell 33). The RM ANOVA uses 10 to 13 sites, not 8 to 11 subjects, so it repeats subjects.
12. **Clock check on one session only** [does not affect a conclusion] (cell 8). The EEG clock is checked on 571619 alone; "every session by construction" is asserted, not shown.

**C. What I could not check, and the output that would settle it**

- **PCIst against the original code.** The PCIst package is not installed here, so I relied on cell 10's 4-site check, which agrees to 4 decimals. A check against the original code on more sites would settle it.
- **Size of the artifact residue (problem 1).** Needed: the per-site metrics, peaks and PCIst rerun with the mask covering k−1, and a plot of the ERP from −20 to +20 ms.
- **The pooled-intensity reading.** Needed: Figure 4 fractions and counts with all three intensities pooled.
- **fig1-supp2 and fig3/fig6 feasibility.** Needed: the EEG electrode x/y/z, and the column names of the LFP electrode table (vertical position, location).
- **Trial matching in fig8d.** Needed: the matched trial number per site, to compare with the paper's average of 51.
- **The fig8e outlier.** Needed: the per-site table for high current with "first" matching.
- **Truncated outputs.** The full fig5f summary line ("combinations where SM-TH fires first with p < 0.05") and the full per-area table in cell 13 were cut off in the outputs I read.
