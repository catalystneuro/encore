**A. Outcomes (18 claims from the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| dataset-size | partially_reproduced | Mice 10, fields 49 and movies per field 4 all match (cell 8). Neurons are 2624 against 1054 ± 105, and P1 is presented 9 times, not 10, in all 188 complete stimulus files, which fails the zero tolerance. |
| stimulus-set | partially_reproduced | There are 3 shapes × 3 levels with ratios 4.99–5.00 and 2.996–2.999, and onsets 1.000 s apart (cell 10). The criterion also requires the order to differ between recordings, but 188 of 190 files share one order and the other two are truncated (52 and 87 deflections). |
| fig2ab-example-neuron | blocked (metadata_insufficient) | The neuron is not identified in the paper or the data. The criterion asks for a match of the Figure 2C mask against the field mean images, and cell 11 says this was not attempted. |
| responsive-fraction | not_reproduced | Reading (a) gives 44.7%, (b) BY gives 17.5% and the BH variant gives 33.9%. All are outside 45.2–55.2 (cell 13). (a) misses by 0.5 points, so the result is fragile to the ROI set (problem 1). |
| fig2de-tuned-fraction | reproduced | Main reading: 78.4% non-tuned pooled and 78.4% as the mean over fields, inside 64.6–79.0; 12 of 16 readings fall inside and all give a majority (cell 15). See problem 2: the per-mouse values conflict with the paper. |
| fig2e-all-categories | reproduced | All four classes are non-empty in all 16 readings (cell 17). |
| tuning-consistency | reproduced | With all neurons as the denominator: 99.5% and 86.5%, inside 85.5–104.5 and 72.9–89.1 (cell 19). With tuned neurons as the denominator, the all-three value is 43.8% or 11.3%. |
| shuffle-significance | reproduced (testable parts) | With FDR: 77.4% non-tuned, all classes present, SI p = 0.521. Without FDR: 57.0%, all classes, SI p = 0.629 (cells 21 and 34). The Figure 4 parts are untestable. |
| fig3b-example-correlation | blocked (metadata_insufficient) | The field is not identified. The Figure 3F inset or the n = 31 count was not tried as a match; I agree a match is unlikely with re-detected ROIs. |
| fig3c-correlation-above-shuffle | partially_reproduced | The Wilcoxon test gives p = 3.6e-15 with true above shuffled in 49/49 fields. Main reading: true 0.233 and shuffled 0.120, both out of tolerance. The dF/F variant gives 0.1097 (just above 0.1084) and 0.0133 (inside). No reading has both values inside. |
| neuropil-correlation | partially_reproduced | Neuropil is higher than neurons in 49/49 fields (p = 3.6e-15), but the mean is 0.61 against 0.179 ± 0.0097 (cell 26). |
| fig3d-example-correlation-distance | blocked (metadata_insufficient) | It depends on fig3b. |
| fig3e-correlation-falls-with-distance | partially_reproduced | Test holds in every reading. The true median of −0.287 (main) is inside tolerance; the shuffled median (−0.094, −0.024, −0.021) is outside −0.0202 to 0.0078 in every reading (cell 28). |
| correlation-gradient-beyond-200um | reproduced | This is an absence claim judged on the test: p = 0.459 (main), 0.76 and 0.41, all ≥ 0.05 (cell 30). 49 fields qualify, against 30 ± 3. |
| fig3f-example-si-distance | blocked (metadata_insufficient) | It depends on fig3b. |
| fig3g-si-no-spatial-organization | reproduced | This is an absence claim: p = 0.614 (main) and ≥ 0.23 in all 9 readings (cell 32). Neither the field count (35 against 23–29) nor the median slope (0 against −0.467) matches, under any SI scale. |
| fig4c-barrel-septum-tuned | blocked (metadata_insufficient), partly testable | The Fisher test needs neurons registered to the map, which was not done. The per-mouse neuron and tuned counts are already in the outputs and fail (problem 5). |
| fig4d-border-distance-by-feature | blocked (metadata_insufficient) | It depends on fig4c's registration. |

Totals: 6 reproduced, 5 partially reproduced, 1 not reproduced, 6 blocked. No claim states a chance level.

**B. Problems**

1. [affects a conclusion] `ssc6.detect_rois` (cell 3): 2624 ROIs, a median of 54 per field, against the paper's 1054 (about 21.5 per field), with only 2 ROIs dropped. In the one overlay shown (cell 5, mouse 1 field 1), several centroids sit in dim neuropil or on a bright non-somatic spot. The paper's ROIs were also "supervised and adjusted manually". No sensitivity run with a stricter detector, one that lands near 1054, was done. This drives the dataset-size failure, the 49 qualifying fields in the >200 µm claim (30 expected), the 35 SI fields (26 expected), and the borderline responsive and tuned fractions.
2. [affects a conclusion] Cell 15, per-mouse results for experiments 8 to 10. These are the only mice for which the paper gives per-mouse counts: 59/167, 39/102 and 47/117 tuned, about 35–40%. The notebook has about 6.3%, 11.4% and 6.7% tuned (22, 25 and 16 neurons of 349, 219 and 238). The pooled match of fig2de (78.4%) is therefore not supported mouse by mouse. It comes from a mix of very different mice (39% to 99.5% non-tuned). I keep the outcome as reproduced because the criterion is pooled, but it is weak.
3. [affects a conclusion] `process_field`, `corrected = (F-bg) - 0.7*(H-bg)`. The Methods subtract the scaled halo "from the background-subtracted mean fluorescence", which reads as F − bg − 0.7·H. The notebook's form leaves an extra 0.7·bg(t) term that is common to all ROIs. It is not stated as an assumption and the literal reading was not run. It changes F0 and the correlations of fig3c, neuropil-correlation and fig3e, which all miss their magnitudes under the corrected-signal reading.
4. [affects a conclusion] Cell 26 runs neuropil-correlation only on the corrected signal. The dF/F reading, which brought the neuronal mean to 0.11 (close to the paper's 0.10), was not run for neuropil, so the claim was not tested under every reading of fig3c that its criterion inherits.
5. [affects a conclusion] Cells 6 and 35, the fig4c/d blocking reason. The notebook says each histology figure has "one dashed square ... no coordinates of each field". But cell 5 prints the text of the exp8 PDF as `['6','5','4','2','7']`, which are exp8's field ids (fields 2 to 7, without 3). The rendered figure also shows several field overlays and barrel outlines. This suggests per-field positions are marked, at least for exp8, which was not examined at usable resolution. Separately, the fig4c count quantities (167/102/117 imaged, 59/39/47 tuned) can be read from cells 3 and 15 without registration, and they fail.
6. [affects a conclusion] Cells 11 and 22: the matching that the criteria for fig2ab and fig3b ask for (Figure 2C mask, Figure 3A/3F) was declared impossible or "not attempted" without being tried. The blocked outcomes therefore rest on a step that was skipped, not one that failed.
7. [affects a conclusion] Cell 10: the stimulus order is identical across recordings and fields. The notebook prints this but it fails the criterion's "order differs between recordings" condition, so stimulus-set cannot be fully reproduced.
8. [does not affect a conclusion] `parse_stim` / cell 8: P1 has 9 presentations in every complete file (89 deflections). Nothing shows whether a 90th deflection is outside the file or missed by the parser. One file's first deflection falls at frame phase 0.0 (cell 3), which is unexplained.
9. [does not affect a conclusion] Cell 4, clock check: 5 fields show no larger contrast at the true onsets, three of them in exp9. At mouse level, exp9's contrast is lower at the true onsets (+0.0014) than shifted (+0.0043). These fields are kept in every analysis without further check.
10. [does not affect a conclusion] Cell 32: the main-reading median SI slope is exactly 0, which implies many fields where SI is identically zero in both the true and shuffled data. `scipy.stats.wilcoxon` drops zero differences by default, so the effective n is below the 35 printed. All p values are far above 0.05, so the outcome stands.
11. [does not affect a conclusion] Cell 19: under the all-neurons denominator, the consistency mostly counts neurons that are non-tuned in both halves. Halves have half the trials and less power. The criterion allows this reading.

The helper functions I tested on synthetic inputs behave correctly: `fdr` matches statsmodels BH/BY, `regress_joint` and `regress_separate` match OLS and linregress, the `responses` windows are right, `shuffled_series` preserves values and the fixed frames, `spearman_upper` is correct, and `parse_stim` classifies P/V/A shapes and amplitudes correctly. Units (px→mm at 1.48 px/µm, dF/F as a fraction, normalized 1/3/5) are consistent. There is no train/test split, so leakage does not apply.

**C. What I could not check, and the output that would have let me**

- Whether the ROIs are somata across fields. Needed: ROI overlays for all 49 fields, and a rerun of the main claims with a stricter detection threshold that gives about 1054 ROIs.
- Whether the exp8 to exp10 histology figures place individual fields. Needed: full-resolution renders of the three PDFs, with the exp8 labels shown.
- The effect of the halo formula. Needed: fig3c, fig3e and neuropil rerun with F − bg − 0.7·H, and neuropil correlation on dF/F.
- The P1 count of 9. Needed: the command trace for the first and last 3 s of one file.
- The SI test's effective n. Needed: the number of fields with SI identically zero, and the n the Wilcoxon actually used.
- The fig2ab and fig3b matches. Needed: the 49 mean images with ROIs, set side by side with Figure 2C and Figure 3F.
- The per-mouse comparison for fig4c. Needed: the tuned counts for exp8 to exp10 printed next to the paper's 59, 39 and 47.

The archive check confirmed `filelist.txt` lists only `data.tar.gz`, the description docx/pdf and `checksums.md5`. There are no ROI or trace files elsewhere.
