**A. Outcomes (29 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| sessions-and-neurons | reproduced | Cell 12: 46 sessions, 950 isolated units, 351 hippocampal and 532 amygdala units after the filter (67 removed, 7.1%). Table S1 sums to 973. |
| table-s1-counts | partially_reproduced | Cell 14: 42 of 46 sessions match before the filter, 21 after. P1809jh, P61cs_2, P68cs and P82cs differ, and together they account for the 23-unit gap (973 vs 950). |
| behaviour-overall-accuracy | reproduced | Cell 18: WM 93.33%, LTM 70.32%, d' 1.189, all within tolerance; both accuracies beat 50% at the smallest p 10,000 permutations allow (9.999e-5). |
| fig1c-wm-accuracy-load | reproduced | Cell 20: t(45) = 4.91 (paper 4.89), p below 0.0001. |
| fig1d-wm-rt-load | partially_reproduced | Cell 22, main reading (RT > 5 s set to missing): t(45) = -4.28 (paper -4.29), but perm p = 0.0003, which misses the < 0.0001 bar. With all RTs, t = 0.20. |
| fig1e-ltm-confidence-accuracy | reproduced | Cell 24: t(44) = 8.51 pooled and 7.34 averaged, both p below 0.0001. |
| ltm-rt-confidence | reproduced | Cell 26: with RTs over 5 s missing, high 1.838 s and low 2.618 / 2.659 s, all within tolerance; t = -11.37 / -11.22, p below 0.0001. |
| fig1f-ltm-load | reproduced | Cell 28: t(45) = 2.65, p = 0.0097. |
| fig1g-ltm-probe | reproduced | Cell 30: t(45) = 6.80, p below 0.0001. |
| category-neuron-counts | reproduced | Cell 36: 102 hippocampal (104 ± 10.4) and 222 amygdala (220 ± 22). |
| fig2b-hippocampus-persistent | partially_reproduced | Cell 40, O-G, all four readings: both effects positive at p < 0.01, but every reading has a beta out of tolerance (intercept 20.2 to 25.4 against 17.86 ± 1.79). |
| fig2c-hippocampus-correct-load | blocked (methods_underspecified) | Cell 42. Reading (a), main effects, is partial: B1 acc 18.48, p = 0.0499 and l1 18.64, both out of tolerance; B2 acc p = 0.060. Reading (b), with the interaction, is not reproduced (l1 = -14.2, p = 0.56). The claims file blocks a claim whose readings disagree. |
| fig2e-amygdala-persistent | blocked (methods_underspecified) | Cell 44, O-G. One row per trial reproduces (B1 10.50 / 6.88, B2 10.06 / 6.55, all within tolerance). The code's rows are partial (13.06 / 5.62 and 11.26 / 5.61). |
| fig2f-amygdala-load-not-accuracy | blocked (methods_underspecified) | Cell 46. Accuracy is not significant in every reading (p ≥ 0.15). The load effect is reproduced under (a) B1 (11.55, p = 2e-5), has its beta out of tolerance under (a) B2 (9.51), and is not significant under (b) (p ≥ 0.70). |
| fig3a-area-interactions | partially_reproduced | Cell 50, O-G: all three area interactions are significant with the paper's signs, and the main effects are not (p ≥ 0.24). All three betas are out of tolerance (70.57, 19.12, -32.52). The O-C variant with the all-sure session, which is the code's own procedure, gives 59.96, 17.84 and -29.16, all within tolerance. |
| fig3b-hippocampus-predicts-ltm | reproduced | Cell 52, O-G under (a) and (b): LTMacc 67.37, conf3 21.25, interaction -30.69, all p ≤ 0.0045 and within tolerance. |
| fig3b-amygdala-no-prediction | reproduced | Cell 54: no effect has p < 0.05 under any reading or outlier rule. |
| fig3c-hippocampus-high-confidence | not_reproduced | Cell 57: the high-confidence difference is not significant (normalized t(68) = 1.17, p = 0.255; Hz t(70) = 1.79, p = 0.078; with the all-sure session p = 0.33 / 0.054). Only the low-confidence absence holds, and the criterion has no partial grade for that case. |
| fig3d-amygdala-no-difference | reproduced | Cell 58: all p ≥ 0.30. |
| fig3e-early-delay-cluster | partially_reproduced | Cell 61: the only significant clusters with remembered above forgotten lie at 0.875 to 1.05 s (p 0.0001 to 0.0196). Nothing significant falls in 0 to 650 ms; the closest is 0 to 0.125 s at p = 0.061. This meets the criterion's partial grade, but it does not support "early". |
| fig3f-amygdala-no-cluster | reproduced | Cell 62: smallest cluster p is 0.40. |
| fig3g-nonpreferred-no-effect | reproduced | Cell 64: smallest non-intercept p is 0.067 (O-C) and 0.089 (O-G). |
| fig3h-encoding-no-effect | reproduced | Cell 66: smallest non-intercept p is 0.074. |
| ms-neuron-counts | reproduced | Cell 68: 53 memory-selective, 26 familiarity-selective (25 ± 2.5). |
| fig4b-ms-confidence-auc | reproduced | Cell 70: (a) 49 neurons, t = 3.87, p = 0.0005; (b) 40 neurons, t = 3.55, p = 0.0009. The paper has 41 neurons. |
| fig4c-overlap-chance | reproduced | Cell 72: overlap 19 (20 ± 2), p = 0.179 (paper 0.11), null mean 15.6. The paper states no numeric chance level. |
| fig4d-category-no-memory-signal | blocked (metadata_insufficient) | The notebook calls it blocked as data missing. The archive's file names (`*_ecephys+image.nwb`) and the notebook confirm the stimulus images are in the files, so only the category labels of the 200 new pictures are missing. With categories inferred from ID blocks, cell 77 finds no p < 0.05 (GLM smallest 0.079 with O-M; t-tests p ≥ 0.22). |
| fig4e-fs-strong-maintenance | not_reproduced | Cell 80: strong is below weak in all 16 GLM readings and all 8 t-test readings, and none has p < 0.05. Pair counts are close to the paper (197 pairs, 84 familiarity-selective). |
| fig4f-ns-no-effect | blocked (methods_underspecified) | Cell 81: no GLM reading reaches p < 0.05. One of 8 t-test readings does (answered old, without self-pairs, Hz: t(81) = 2.04, p = 0.0395), so the absence holds under some readings and not others. |

**B. Problems**

1. [affects a conclusion] fig4d, cells 73 to 77: the category labels of the new pictures are missing, but the images are in the files. Labelling the 200 new images (IDs 1001 to 1200) by viewing them would test the claim on real labels instead of inferring them. The ID-block inference agrees with the preferred category in 58% of neurons, against 60.5% for the true labels on old pictures, which is good support for it. Under it, every reading reproduces the claim.
2. [affects a conclusion] Reading (b) of fig2c and fig2f, in the claims file, not the notebook: in `acc * l1` with 0/1 reference coding, the `acc` and `l1` terms are simple effects at the reference level (for example, load in incorrect trials, where only 59 rows have load 1). They are not the main effects the paper reports. This reading alone turns both claims into blocked. Reported here, not corrected.
3. [affects a conclusion] fig1d, cell 22: t matches the paper (-4.28 vs -4.29). With 10,000 permutations, p < 0.0001 is reachable only when no permutation exceeds the observed t. At |t| ≈ 4.3 that happens about a third of the time, so the grade between reproduced and partial depends on the seed.
4. [affects a conclusion] fig3c and fig3d, `remembered_forgotten` (cell 56): hippocampus keeps 69 and 71 neurons where the paper keeps 83 (amygdala 146 vs 159). Only 80 hippocampal neurons have both conditions before any removal, fewer than the paper keeps after removal. So the row set probably differs from the paper's, and the Hz p of 0.078 is close enough to 0.05 that this could change the outcome.
5. [does not affect a conclusion] `fig3_select` (cell 48): the all-sure session (P69CS) is dropped from the main Figure 3 analyses. Claims file S defines confidence sessions by NaN confidence, which would keep it. The paper's text supports dropping it, and the variants that keep it give the same outcomes.
6. [does not affect a conclusion] Cell 60, binning (a): windows centred at 0 take in 100 ms of the last encoding picture. Cluster bounds near 0 should be read with that in mind.
7. [does not affect a conclusion] fig4f, `pair_tests`: 24 uncorrected tests per claim, so a single p of 0.0395 is about what chance predicts. The claims file's rule still decides the outcome.
8. [does not affect a conclusion] `mixedlm`: statsmodels printed "invalid value in sqrt" warnings during the Figure 4 fits, and `fig3_fit` does not record convergence. No NaN SE or p appears in the outputs.

Checked and correct: the helpers on synthetic data (paired and pooled t and one-way F match scipy, the AUC equals the Mann-Whitney U/(n·m), `binned_counts` and `count` window edges, `s1_label`, and the cluster test, which finds a planted effect with a null rate of about 5%); the rate filter; selections C and M; both confidence recodings; the nesting of the random effects; the residual degrees of freedom.

**C. Not checked, and the output that would allow it**

- The shared clock for the 12 sessions where the WM alignment check shows no advantage (cell 34). A per-session peri-onset PSTH of all units, true against shifted onsets, would settle it.
- Why fig3c has fewer neurons: a table of neurons lost at each step (no rows, missing condition, zero spikes, outlier) and the number of rows per neuron and condition.
- Whether an early effect in fig3e is just below threshold: the time-resolved t curves (`t` from `time_resolved`) were computed but not printed or plotted.
- fig4e: the per-pair distribution of strong minus weak, and a variant with the median split pooled across loads, to see whether the opposite sign is robust.
- fig4d: per-image category labels for the new pictures, or a contact sheet of a few images per ID block, to confirm the inferred blocks.
