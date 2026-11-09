**Verification report, round 1: Duszkiewicz et al. 2024 on DANDI:000939 (0.261016.2310)**

The claims file has 34 claims. The notebook tests 31 and treats 3 as blocked. My outcomes: 21 reproduced, 6 partially reproduced, 1 not reproduced, 3 blocked. The notebook uses the recomputed classes throughout: n = 1,661 excitatory, 430 FS and 1,512 HD cells, against the paper's 1,835, 427 and 1,602.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| cell-classes-counts | partially_reproduced | Five of six quantities are within tolerance (cell 6): excitatory 1661, at the edge of 1835±184; FS 430; HD 1512; fraction 0.91; vertical 931. Parallel units are 1760 against 1999±200, so outside. The shortfall of 239 is larger than the paper's largest recording (185 units), so one missing session does not explain it. |
| ed2b-excitatory-hd-information | reproduced | Signed-rank p=6e-273, median log10 information 0.10 against −1.53 (cell 10). The bimodal histogram is shown, with maxima at −1.67 and 0.19. |
| fig2a-fs-hd-information | reproduced | n=430, p=4e-72, real median above control (cell 12). |
| fig2b-decoding-from-fs | reproduced | Mean of the per-session median FS error is 36.0° against a chance level of 90.0°. Pearson r between FS cell count and error is −0.449, p=0.011, over 31 sessions (cell 18). |
| fig2c-geometry-independent | reproduced | FS n=273, p=1e-45; HD n=1118, p=4e-184; real above control at both 3° and 2° smoothing (cell 16). |
| ed2hi-within-epoch-stability | reproduced | FS p=5e-72 and HD p=1e-248 at both smoothings (cell 14). |
| fig2f-cue-rotation | reproduced | n=99 FS cells (the paper's n), p≈1e-17, real differences smaller, under all four exclusion readings (cell 20). |
| fig3c-adn-broader | reproduced | ADN median width 62° against 42°, z=11.58 (paper 11.4), p=4e-31 (cell 38). |
| fig3-ten-components-power | partially_reproduced | Squared-modulus reading is within tolerance: pooled 0.989, FS 0.969, HD 0.994. The rms reading has no population within tolerance (0.78–0.90), and the criterion needs one under each power reading (cell 24). |
| fig3e-fourier-signatures-differ | partially_reproduced | Direction readings (a) and (b) hold under both power readings. The main ANOVA reading (numeric covariate) with the code's squared-modulus power gives F(9,18333)=1.09, p=0.365. It is significant only with rms power (p=1e-16) or the categorical variant (cell 40). |
| fig3f-posub-hd-closer-to-fs | partially_reproduced | PoSub-HD is closer under all four readings with p<0.05, but p is not below 1e-9 in all of them. Squared-modulus with D_KL(cell‖FS) gives p=0.008, and squared-modulus with D_KL(FS‖cell) gives p=1e-7 (cell 42). |
| ed3k-robust-to-controls | reproduced | All 12 distance tests have p<0.05 with z<0. The multipeak test gives z=−4.18, p=3e-5 (cell 44). |
| fig3g-first-three-components | partially_reproduced | Interaction p<1e-160. With squared-modulus power exactly components 1–3 are higher than control. With rms power component 4 is also higher (p_bonf=0.005), which breaks "no other" (cell 26). |
| fig3h-dominant-component | not_reproduced | Counts are 237, 146 and 47. The third is outside 55±6. Reading (a) holds; reading (b) fails under both power readings (relative differences 0.42 and 0.55 for component 3). The criterion has no outcome for a count out of tolerance (cell 28). |
| ed3g-fs-spectra-heterogeneous | reproduced | FS distances are larger under all four readings, p×3 ≤ 6e-67 (cell 30). The ADN part (F≈184 against the paper's 169) is consistent (cell 46). |
| ed3l-fs-phases-independent | reproduced | PoSub-HD ρ=0.32 (p≈0) and 0.087 (p=1e-4). FS ρ=0.014 (p=0.77) and 0.005 (p=0.91) (cell 32). |
| ed4a-autocorrelogram-symmetries | reproduced | Twofold cells at 180°: p=2e-13. Threefold cells at 120°: p=0.004. Real values are higher, under both tests (cell 34). |
| ed4cd-isomap-posub-central | reproduced | PoSub-HD distances are smaller, z=−2.93, p=0.003 (paper z=4.26), using scikit-learn Isomap (cell 48). |
| fig4-random-connectivity-simulation | blocked (methods_underspecified) | Archive checked: 31 NWB files, no code. The simulation parameters and code are not available. |
| fig4f-synaptic-weights-dispersed | reproduced | strZ over 1,176 connections: CV 1.90, skewness 9.34 (cell 50). The strR variant has CV 0.71, below 1. |
| fig4h-model-fit | blocked (methods_underspecified) | The fit code and initial values are missing. The recorded FS and HD curves needed as inputs are available, so only the fit itself is blocked. |
| ed7-adn-disinhibition | reproduced | ADN-HD against non-HD: z=6.85, p=8e-12, ADN-HD median 1.54. Width test p=0.61 (cell 64). |
| fig5b-posub-rates-increase | reproduced | FS ArchT against control: p=6e-8. ArchT medians are 1.33 (FS) and 1.46 (HD), both above 1 and above control. Only 2 of the 5 ArchT mice are used (cell 54). |
| ed7gj-tuning-preserved | reproduced | HD width p=0.53 (signed-rank). FS correlation p=0.68. Both are claims of absence tested at n=62 and 33/43, against the paper's 83 and 47/38 (cell 56). |
| fig5e-hd-multiplicative-fs-additive | partially_reproduced | Every condition holds under exclusion readings (a) and (c). Under (b), HD additive against control gives p=0.015, so not every reading holds (cell 58). Reading (b) excludes 31 HD cells, which contradicts the Methods' "no cells from other populations" (problem 7). |
| ed8cd-multiplicative-detectable | partially_reproduced | With the code's noise (1.8×1.8), the additive simulation's multiplicative factors also differ (p=0.008), so it fails. With titrated noise (the Methods) and a simulated control it holds (p=0.022; 7.5e-5; 0.127), in 80% of 50 seeds. Against the recorded control, the additive simulation's multiplicative factors differ (p=0.0008) (cell 60). |
| ed8e-adn-mixed-gain | reproduced | Multiplicative p=0.47 and 0.62; additive p=7e-6 and 0.002 with ADN higher, under all readings (cell 66). |
| fig6c-coupling-preserved-wake-rem | reproduced | Pearson r is 0.716 (HD-HD), 0.400 (FS-FS) and 0.436 (HD-FS), all with p≪0.05, and FS-FS is below HD-HD (cell 68). This depends on the fit filter (problem 2). |
| ed9d-coupling-follows-tuning | reproduced | All four r values are positive (0.76, 0.35, 0.45, 0.14), all with p<1e-13 (cell 70). |
| fig7b-wake-isomap-tuning | reproduced | HD p=1e-248, FS p=4e-72 (cell 72). |
| ed10b-ring-topology | reproduced | Real against shuffled: p=1e-6 over 31 sessions, shuffled radius 0.44. REM against WAKE: p=0.43 over 27 sessions (cells 74, 76). |
| fig7d-rem-isomap-tuning | reproduced | Under both WAKE-curve readings, HD p≈1e-201 and FS p≈1e-31 (cell 76). |
| fig1ac-posub-border | reproduced (qualitative) | The running average rises from about 0.01 to about 1.19 bits per spike, with one half-range crossing at −1.68 mm. There is a small bump of 0.19 at −0.6 mm (cell 78). The judgement depends on the depth sign (section C). |
| ed6-trn-innervates-adn | blocked (data_missing) | Archive checked: 31 NWB files only, no images. |

No chance level for a selection is stated in the paper. The decoder's chance level is computed (90°) and used.

### B. Problems

1. **[affects a conclusion]** Cells 52 and 62 leave out data the claims file points to. Only 2 of the paper's 5 ArchT PoSub mice are used (A1813, A1815). Figshare Dataset_6, which the notebook opens, holds the other three (A1801, A1804, A1806); they are listed and dropped, and that choice is not stated as an assumption. The ArchT n falls to 62 HD and 33 FS (paper 83 and 47). This weakens the claims of absence in ed7gj and fig5e. It also probably explains the HD ArchT-against-control z of 7.8 against the paper's 1.69 (cell 54).
2. **[affects a conclusion]** In `poisson_glm_batch` (cell 68), the "ill-conditioned" filter is the helper's own approximation of glmfit's warnings: fitted-mean ratio below eps^(4/3). It removes 970 HD-HD pairs. Keeping them drops the HD-HD r from 0.716 to 0.102, below FS-FS (0.400), which reverses the fig6c ordering. The mapping to MATLAB's warning is not checked against the code.
3. **[affects a conclusion]** In cell 40 (fig3e), the main numeric-covariate ANOVA with the code's power is not significant (p=0.365, against the paper's 0.003). The notebook prints this but has no conclusion text. I tested `rm_interaction` against an independent split-plot and contrast computation and the F values match, so this is a data result, not a bug.
4. **[affects a conclusion]** Cell 6: the parallel-probe count shortfall (239 units) exceeds the paper's per-recording maximum (185). The criterion's "one session's cells" explanation does not cover it, and the notebook does not say so.
5. **[does not affect a conclusion]** In fig2b (cell 18), the chance-level error of the time-reversed decoder is measured against the reversed HD rather than the real HD. Both give about 90°.
6. **[does not affect a conclusion]** In `tuning_curves(reverse=True)`, only the speed-filtered samples are reversed, not the epoch's HD series before masking as the claims file states. `split_halves` splits used samples rather than epoch time (stated as an assumption). Viable units are cut at rate > 0.5 Hz rather than ≥ 0.5.
7. **[does not affect a conclusion]** This is a claims-file misreading, reported and not corrected. The Methods state that the exclusion "led to the exclusion of 1 of 47 PoSub-FS cells and no cells from other populations". That rules out exclusion reading (b), which removes 31 of 62 HD cells here, yet the fig5e criterion requires it. Reading (c) reproduces the paper's count exactly (0 HD, 1 FS).
8. **[does not affect a conclusion]** In fig3-ten, fig3e and fig3g, the claims file's "rms" power reading equals |c|/√2. After normalisation it is an amplitude spectrum, and the Methods' own Parseval check implies squared modulus. Requiring it under "each reading" is a strict reading of the Methods' words.
9. **[does not affect a conclusion]** Cell 50: the ±50 ms and ±25 ms outputs are identical. This is expected: the detection window (±2 ms) plus the kernel's half-width (about 12 ms) never reaches either edge, so the span variant is not informative.
10. **[does not affect a conclusion]** `signrank` reports scipy's z, which is negative when the first sample is larger (checked on synthetic data). The direction is judged from the medians, which is correct.
11. **[does not affect a conclusion]** In ed8cd (cell 60), the reported main result uses the code's noise level. The Methods specify titrated noise, which is run as the second block. The outcome differs between them.

Helpers I tested on synthetic data and found correct: `rm_interaction` (categorical and numeric), `fourier` (Parseval), `circ_xcorr_lag`, `xval_autocorr` (peaks at 120° and 240°), `peak_width` (about +3° bias on a von Mises curve), `hd_info`, `circ_corrcc`, `tuning_curves` (peak at the true angle).

### C. What I could not check

- **GLM filter (problem 2):** whether glmfit would flag the same 970 pairs. Adding the coefficient magnitudes and REM rates of the removed pairs, and the count under glmfit's exact rule, would settle it.
- **ArchT n (problem 1):** whether adding the three figshare ArchT mice brings n to 83 and 47 and changes ed7gj, fig5e or ed8cd. A rerun of cells 54–60 with them would answer this.
- **Parallel-unit shortfall (problem 4):** whether it comes from a missing session or from curation differences. A per-session comparison of dandiset subjects against the code's `dataset_All.list` would answer this.
- **Neuropixel depth sign (fig1ac):** whether larger CellDepth values mean shallower cells. A print of the probe tip or channel geometry would confirm the depth sign.
- **REM epochs:** the dandiset's 2026 update says it "fixed indexing of sleep scoring epochs", but cell 2 compares only unit, spike and HD counts between versions. A check that REM intervals fall inside the sleep epochs, and their durations in both versions, would cover the REM-based claims (fig6c, ed9d, fig7d, ed10b).
- **Light pulses:** the decoding in `light_pulses` is supported only indirectly, by the shifted-window control. A print of the pulse widths and intervals would let me check it directly.
- **Figshare files:** I could not open them, so the ADN, cue-rotation and Neuropixel loading is unverified beyond the matching counts (97 ADN-HD cells, 99 FS cells, 127 thalamic cells).
