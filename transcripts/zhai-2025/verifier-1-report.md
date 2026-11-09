I made my own call on all 45 claims in the claims file: 24 reproduced, 2 partially reproduced, 4 not reproduced and 15 blocked. Two of the notebook's dendritic tests come out against the paper, and in both cases the index computation may be the cause rather than the data.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| link-somatic-cells | partially_reproduced | All 12 groups have the paper's n, but only 73.2% of cells match exactly (80% needed) and 85.4% match within 3 spikes (95% needed). Cell 19. |
| link-dendritic-cells | reproduced | Cell counts equal the paper's n in 7 of 10 groups, and the median relative difference is 0.040 (Spearman 0.91). Two cells are far off (1.559 in dSPN on+SCH, 1.014 in iSPN off). Cell 21. |
| link-sr-cells | partially_reproduced | All 14 cells match a paper identifier, but only 2 of 14 are within 25% on both event count and amplitude. Cell 23. |
| link-grab-rois | not_reproduced | The dandiset holds part of the regions (3/13, 3/10, 5/11). Only 5 of 11 mice match within 0.05 on every treatment, short of half. Cell 25. |
| link-aim-mice | not_reproduced | 7 of 9 mice are in the paper, but only 15 of 35 matched session totals are equal. All five Fig. 8 mice differ; the two Fig. 10 mice agree exactly. Cell 27. |
| fig1f-dspn-rheobase-on-lower | reproduced | P = 8.9e-6; medians 140 (on) vs 220 (off). Cell 30. |
| fig1e-dspn-fi-on-higher | reproduced | P = 8.8e-5, on-state higher (88 vs 36); same with complete cells only. Cell 32. |
| fig1f-dspn-sch-no-change | reproduced | P = 1.0; the paired Wilcoxon (n = 5) also gives P = 1.0. Cell 34. |
| fig1i-dspn-dendritic-on-higher | reproduced | P = 0.0091, on-state higher; holds in all variants. Cell 36. |
| fig1i-dspn-dendritic-sch-lower | not_reproduced | P = 0.066 (paper 0.0133). The SCH median is 0.419 against the paper's 0.338; one SCH cell differs 2.6-fold from the paper and may drive this (B1). Cell 38. |
| fig3d-ispn-rheobase-on-higher | reproduced | P = 0.00083; medians 160 vs 120. Cell 41. |
| fig3c-ispn-fi-on-lower | reproduced | P = 7.2e-5, on-state lower. Cell 43. |
| fig3d-ispn-sul-no-change | reproduced | P = 0.143. Weak: medians 160 vs 120, only 2 paired cells. Cell 45. |
| fig3f-ispn-dendritic-on-lower | reproduced | P = 0.0128, on-state lower. Fragile: the 0.8–1.25 basal-ratio variant gives P = 0.077. Cell 47. |
| fig3f-ispn-dendritic-sul-no-change | not_reproduced | P = 0.0164 (paper 0.0545), sulpiride higher (0.506 vs 0.340). n is 9 and 7, against the paper's 10 and 8. Cell 49. |
| fig5f-ach-off-elevated | reproduced | P = 0.0357, the smallest P possible for 3 against 5, with off-state higher. The unnormalised dF/F0 variant gives P = 0.25. Cell 52. |
| fig5f-ach-off-like-6ohda | reproduced | P = 0.143; little power with 3 against 5. Cell 54. |
| fig6c-m1r-antag-somatic-unchanged | reproduced | P = 0.681 (sum of spikes, P = 0.45). Cell 57. |
| fig6d-m1r-antag-dendritic-lower | reproduced | P = 0.0229, antagonist lower. Cell 59. |
| fig7c-cdgi-ko-somatic-oscillation | reproduced | P = 0.00104, on-state higher (210 vs 140). Cell 61. |
| fig7f-cdgi-ko-dendritic-unchanged | reproduced | P = 0.315. KO off has n = 10 against the paper's 11. Cell 63. |
| fig9d-m1r-crispr-somatic-unchanged | reproduced | P = 0.147; the control group is 6 cells from 2 mice. Cell 65. |
| fig1-dspn-lesion-and-off-somatic | reproduced | Paper's table: P = 0.0003 (lower after lesion) and 9.5e-5 (higher in off-state). Cell 68. |
| fig1-dspn-lesion-dendritic-unchanged | reproduced | P = 0.82 and 0.90 (paper 0.824 and 0.905). Cell 70. |
| fig3-ispn-lesion-and-off-somatic | reproduced | P = 0.0004 and 0.0006, both in the stated direction (paper gives 0.002). Cell 72. |
| fig3-ispn-lesion-dendritic-up | reproduced | P = 0.035 and 0.024, later group higher. Cell 74. |
| fig7e-oxom-cdgi | reproduced | WT P = 0.0098, oxo-M higher; KO P = 0.47. The paper reports 0.910 for KO (B13). Cell 76. |
| fig8a-cdgi-rotations | reproduced | P = 0.012, KO higher (paper 0.0092). Cell 78. |
| fig10a-m1r-rotations | reproduced | P = 0.0078, deletion higher. Cell 80. |
| fig10ef-open-field | reproduced | Distance and time mobile both meet the criterion: control vs MCI-Park P = 1e-5 / 7e-6; levodopa vs levodopa with deletion P = 0.0003 / 0.0006; MCI-Park vs deletion alone P = 0.63 / 0.47. Cell 82. |
| fig2h-dspn-sr-amplitude-on-larger | blocked (other) | Archive has 3 off and 4 on cells, so the smallest P is 0.057. Both the detector and the paper's per-cell values put on above off at that floor. |
| fig2i-dspn-sr-frequency-unchanged | blocked (other) | Same 3 against 4; P = 0.229 says nothing for an absence claim. |
| fig4g-ispn-sr-amplitude-on-smaller | blocked (other) | 3 against 4. The paper's per-cell values put off above on (P = 0.057), but the detector does not (P = 0.229). |
| fig4h-ispn-sr-frequency-unchanged | blocked (other) | 3 against 4; P = 0.114. |
| fig2bc-dspn-spines | blocked (methods_underspecified) | Raw 2PLSM stacks only. Counting needs AutoQuant deconvolution and semi-automated NeuronStudio counting. |
| fig4bc-ispn-spines | blocked (data_missing, methods_underspecified) | No 2PLSM stacks from control or 6-OHDA mice; only off/on and manipulation sessions. Counting method as above. |
| fig4k-confocal-spines | blocked (methods_underspecified) | Confocal stacks only (CTRL 3+1, PD 3, OFF 3, ON 2 files). Counting used Imaris with supervised learning and manual correction. |
| fig6f-m1r-antag-spines | blocked (methods_underspecified) | Raw stacks only. |
| fig7h-cdgi-ko-spines | blocked (methods_underspecified) | Raw stacks only. |
| fig9f-m1r-crispr-spines | blocked (methods_underspecified) | Raw stacks only. |
| fig5f-ach-6ohda-elevated | blocked (other) | 3 against 3, smallest P 0.10. All 3 lesioned values (0.18–0.27) are above all 3 controls (0.09–0.11). |
| fig5f-ach-d2-control | blocked (other) | 3 pairs, smallest P 0.25. Direction holds in 3 of 3 for both drugs. |
| fig5f-ach-da-suppresses | blocked (other) | 3 lesioned pairs and 5 off-state pairs (smallest P 0.0625). Dopamine is lower than no drug in 8 of 8. |
| fig8bc-cdgi-aims | blocked (other) | Only 1 wild-type mouse by the paper's labels (2587). Dandiset genotype labels contradict each other, and the link fails. |
| fig10b-m1r-aims | blocked (other) | One mouse per group. |

The paper states no chance level for any selection, and the notebook has none.

**B. Problems**

1. [affects a conclusion] `cell_index` / `lid.dendritic_index`, cells 21 and 38: one dSPN on+SCH cell's index differs 2.6-fold from the paper's value, but the notebook prints only the group maximum, not which cell.
   - I replaced each SCH value in turn with value/2.559 (the paper's value implied by that difference, if ours is the high one). For any of the top five SCH values, P falls to 0.014–0.041.
   - So fig1i-dspn-dendritic-sch-lower may fail because of one computed index, not because of the data.
2. [affects a conclusion] `lid.dendritic_index`, cell 21: the main basal-ratio rule (0.5–2) drops 0 of 162 pairs, so the paper's rule of keeping only pairs with similar G0/R0 is never applied. The stricter 0.8–1.25 variant changes the results:
   - fig3f-ispn-dendritic-on-lower goes to P = 0.077;
   - fig1i SCH goes to P = 0.52;
   - fig3f sulpiride goes to P = 0.066.
3. [affects a conclusion] `lid.dendritic_index`: proximal and distal sites are paired only by number. Three cells get no index (iSPN on, iSPN on+sul and KO off are each one short of the paper's n). That bears on fig3f-ispn-dendritic-sul-no-change, where P is 0.016 here against 0.0545 in the paper.
4. [does not affect a conclusion] Cell 21: matching dendritic cells to the paper's rows by order is assumed, and the notebook never checks that the somatic best-match rows follow date order. The two large differences (1.559, 1.014) could be misaligned rows.
5. [does not affect a conclusion] Cells 19 and 25: best matches are not one-to-one.
   - Somatic: dSPN off row 23 is used twice, dSPN on row 39 three times and row 44 twice.
   - GRAB: off-state ROI 29 is used twice.
   - This can only inflate the match counts, and the outcomes are already partial or not reproduced.
6. [does not affect a conclusion] `fi_sum`, cell 32, and `lid.rheobase`: 18 cells are missing a step.
   - In the spike sum a missing step adds nothing, which lowers that cell's total.
   - Rheobase skips missing steps and can come out 20 pA high, e.g. dSPN off 20161116 cell 3 (no 80 pA step) and the Fig. 6 vehicle cells missing 100 or 120 pA.
   - The complete-cell variants agree, and the margins are large.
7. [does not affect a conclusion] `lid.load_patch` keeps the first of a repeated step (14 cells). Nothing checks this against the paper's script.
8. [does not affect a conclusion] Cells 34 and 45: the on-state and on+drug groups share cells (5 dSPNs, 2 iSPNs), so the unpaired Mann-Whitney samples are not independent. The criterion follows the paper here. The absence claims (fig3d sulpiride, fig5f off-like-6-OHDA, fig9d) pass with little power.
9. [does not affect a conclusion] `mw`: scipy's asymptotic test is used for n > 8, while Prism is exact. I recomputed exact P on the printed values; no outcome changes (fig1i SCH 0.065, fig3f off/on 0.010).
10. [does not affect a conclusion] `lid.detect_events`, cell 23: the detector works on synthetic events (5 of 5 and 3 of 3 found, amplitudes right), but on real cells it finds far fewer events than the paper (20230405b: 2 against 73).
    - The 25% criterion compares against the mean of the paper's histogram events, not the paper's per-cell amplitude. These differ (11.13 vs 12.37).
    - This affects only link-sr-cells, since the Sr claims are blocked.
11. [does not affect a conclusion] Cells 11–12, GRAB:
    - six files put the stimulus at 3 s, against the Methods' "10-s baseline";
    - the background reference images have a mean above the signal itself, so they cannot be PMT background.
    - The normalised area does not depend on a constant background (confirmed on a synthetic case). The Fmin rule (TTX or quinpirole baseline, whichever is smaller) matches the Methods.
12. [does not affect a conclusion] Cell 13: the AIM genotype labels contradict each other within an animal and across files. The notebook reports this correctly.
13. [does not affect a conclusion] Cell 76: the KO Wilcoxon on the paper's own table gives P = 0.47, but the paper reports 0.910. The pivot on `expt` may pair the wrong rows. The criterion is met either way.

**C. What I could not check, and the output that would have let me**

- **Zenodo tables:** I did not have the paper's per-cell tables, so I could not recompute any link match or "elsewhere" P value. For the dendritic link, a per-cell table with dandiset date and cell, our index, the paper's value and the per-pair basal ratios for every group would settle B1–B4 and show which SCH cell is off.
- **Somatic order:** the best-match row number next to the date and cell order for every group would test the order assumption behind the dendritic link.
- **One-to-one links:** the somatic and GRAB link counts recomputed with a one-to-one assignment.
- **AIM mismatches:** a per-time-point comparison with the paper for the five mismatched Fig. 8 mice, to tell a scoring difference (for example the 120-min point) from different data.
- **fig7e:** the KO pairing table from cell 76.
- **Sr2+ detector:** traces with detected events marked for 20230405b, and for one cell where we agree with the paper.
- **Spine stacks:** I checked them only through the asset metadata. All 86 stack files have empty `variableMeasured`, which points to no stored annotations. A listing of each spine file's processing modules would confirm that no counts are stored.
