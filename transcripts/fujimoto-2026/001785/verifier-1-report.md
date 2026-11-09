**Verifier report, round 1: Fujimoto et al. 2026 on DANDI:001785 (0.260615.1835)**

The claims file has 35 claims. The notebook tests 28 and treats 7 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| link-fc-voxels | reproduced | Cell 15: all 5087 voxels land on grid centres in all 6 maps (offset 0, inside 1.0), and 100% agree to within 1e-4 (largest difference 5e-7). |
| link-fa-voxels | reproduced | Cell 42: 6332 of 6332 values found, every sheet at 100%, 17 ambiguous (but see B5). |
| link-if-counts | partially_reproduced | Cell 58: the link holds under at least one reading in MCC-CB N/T (isodata or otsu, min 10), dACC-CB (min 10) and MCC-CB D (min 50). It fails in UF-FM: at min 10 CC1 r is 0.692–0.694, below 0.7; at min 50 the CC1 median ratio is 0.755, below 0.8. So 3 of 4 regions. |
| ed1-behavior-increase | reproduced | Cell 71: movement F(1,236)=34.61, p=1.37e-08; foraging F(1,236)=17.35, p=4.37e-05. Both animals' post proportions are above pre. |
| ed1-sham-no-behavior-change | not_reproduced | Cell 73: foraging fell from 0.183 to 0.050, F(1,118)=5.32, p=0.0228, below 0.05. Movement p=0.175. |
| fig2a-cb-fa-increase | reproduced | Cell 45: PrePost×side F(1,3187)=4.64, p=0.0312. Stimulated CB Tukey p=0.0223 with post higher. All six voxel counts equal the expected values. |
| fig2a-no-other-tract-change | reproduced | Cell 47: none of the 5 comparisons has p<0.05; the smallest is 0.863. |
| ed2-cb-both-monkeys | reproduced | Cell 49: post minus pre is +0.019 in N and +0.079 in T. |
| fig2b-mcc-cb-increase | reproduced | Cell 51: F(1,1357)=5.42, p=0.020. Stimulated MCC-CB p=0.00177 with post higher; no other comparison increases significantly; both monkeys rise (+0.081, +0.205). Counts 55/271/361 match. |
| fig3c-cc1-dapi-ratio-mcc | reproduced | Cell 61: the side effect on the ratio has p from 0.00025 to 0.0026 under all 4 readings, stimulated side higher in N and T. 56 fields per hemisphere. |
| ed5-cc1-count-dapi | reproduced | Cell 63: CC1 p from 0.003 to 0.017 (stimulated higher) and DAPI p from 0.39 to 0.97 under all 4 readings. |
| ed6a-dacc-cb-no-change | not_reproduced | Cell 65: the ratio side effect is significant under all 4 readings (p from 0.0058 to 0.013, stimulated side lower). The paper's own counts give p=0.0899. The link holds in this region (r about 0.98). |
| ed6b-uf-fm-no-change | reproduced | Cell 67 variant, which keeps the paper's design of 40 fields per hemisphere (df 76): ratio, CC1 and DAPI all have p≥0.05 under every reading (smallest 0.0685). The notebook's main run includes an extra field (B2). Counts in this region failed the link. |
| fig3f-gratio-decrease | blocked (other) | Cells 12–13: the dandiset holds only the EM images. The per-axon measurements were made by hand on axons the raters chose, and they exist only in 001773. Any automatic segmentation would be the agent's own method. |
| fig4a-cortical-decrease-subcortical-increase | blocked (data_missing) | Archive check: MRI/FC holds 12 single-volume seed maps and no EPI or residual time series, so no ROI-by-ROI matrix can be computed. |
| fig4b-dbs-widespread-roi-changes | blocked (data_missing) | As fig4a. |
| fig4c-cortical-network-reduction | blocked (data_missing) | As fig4a. |
| fig4-control-no-systematic-pattern | blocked (data_missing) | As fig4a. |
| ed10c-sham-subcortical-decrease | blocked (data_missing) | As fig4a. |
| fig5a-pre-scc-connectivity | reproduced | Cell 18: all 9 signs hold under both readings. |
| fig5b-scc-decreases | reproduced | Cells 16 and 20: F(1,20279)=186.48, p=2.87e-42. All 7 ROIs fall with p<0.05 (largest 4.9e-4). All 17 ROI counts equal Supplementary Table 8, which I checked against the paper. |
| fig5b-scc-increases | reproduced | Cell 22: insula p=6.8e-08 and sensory cortex p≈1.4e-11, both increases. |
| ed7-decreases-both-monkeys | reproduced | Cell 24: all 7 ROIs are below 0 in both N and T (AMY in N only just, −0.0006). |
| fig5-bilateral-changes | reproduced | Cell 26: all 4 hubs are significant on the control side (insula p=0.029). The 11 of 17 significant ROIs are the same set as Supplementary Table 9. |
| fig5a-control-group-no-reduction | blocked (data_missing, partly testable) | Reading (a) needs runs, which the dandiset lacks. Reading (b) could be computed from the B, W and H maps (see B9). |
| fig5c-network-decreases | reproduced | Cell 28: F(1,21967)=51.09, p=9.1e-13. Stimulated-side DMN, CEN and LIM all decrease with p≈1.7e-11. Counts 857/821/1102 match. |
| fig5c-smn-increase | reproduced | Cell 30: stimulated-side SMN increases by 0.0196, p≈1.7e-11. |
| disc-no-motor-roi-change | reproduced | Cell 32: motor cortex p=0.99992, SMA p=1.0. |
| fig5c-vis-no-change | reproduced | Cell 34: VIS p=1.0, V1 p=1.0, MT p=0.9989 on the stimulated side. |
| fig5bc-san-no-net-change | reproduced | Cell 36: SAN p=1.0; insula up (p=6.8e-08); dACC down (p=4.9e-4). |
| fig6a-sham-cb-fa-decrease | reproduced | Cell 53: sham-side CB falls by 0.117, p=8.4e-09. The other 5 have p≥0.088. Counts 162/148 match. Three-way F(2,1238)=6.02, p=0.0025. |
| fig6b-sham-dacc-cb-decrease | reproduced | Cell 55: F(1,492)=24.55, p=9.97e-07. dACC-CB falls, p=3.6e-08. MCC-CB shows no significant increase. |
| fig6c-sham-cc1-no-change | blocked (methods_underspecified) | Cell 69: min-area 10 gives p≈0.31 and min-area 50 gives p≈0.044, so the two readings give opposite outcomes. In monkey D the link holds only at min 50, which would make this not reproduced. |
| fig6d-sham-scc-little-change | reproduced | Cell 38: sham-side PCC p≈1.0 and dACC p=1.0. Exactly 2 of the 8 hub comparisons are significant (sham vmFC, control insula). F(1,10106)=4.58, p=0.0323. |
| fig6e-sham-no-network-reduction | reproduced | Cell 40: no significant decrease in sham-side DMN, LIM or CEN (p≥0.73). Counts 453/404 match. |

Totals: 24 reproduced, 1 partially reproduced, 2 not reproduced, 8 blocked.

### B. Problems

1. **[affects a conclusion] Cell 69, fig6c.** The smallest object size is the notebook's own assumption (`count_cells`), and here it decides the outcome (p 0.31 against 0.044). The notebook prints both results but does not say the readings disagree. Under the protocol this is methods_underspecified, not a pass.
2. **[affects a conclusion] Cell 67, ed6b.** The main run includes image N122 RW6, a sixth field outside the 5-field design. It has no row in the paper's sheet, and it raises the error df to 77 against the paper's 76. With it included, the otsu/min-50 reading gives ratio p=0.04997, so the readings disagree. Only the variant that leaves it out matches the claims file's n of 40 fields per hemisphere.
3. **[affects a conclusion] Cells 57–65, `count_cells` and `section_threshold`.** The counting pipeline is the author's approximation of the paper's FIJI counts: one global threshold, 8-connected objects, no background subtraction, no watershed, and size filters the paper does not give. No single procedure links all regions. MCC-CB N/T passes only at min 10, D only at min 50, and UF-FM never passes. The criterion was also set after the counts were computed (claims file). The not_reproduced result for ed6a (ratio significant under every reading, where the paper's counts give p=0.09) may therefore come from the method rather than the data. It stands under the stated method.
4. **[does not affect a conclusion] FA and FC claims, cells 8 and 16.** The dandiset's values equal the paper's spreadsheet values by construction; FA voxels are even located by matching the values. Every voxel selection (tracts, lead-track exclusion, CB subregions, ROIs) is the paper's. So the open readings of [FA], [CB-PARTS] and [SEED] are moot, as the notebook argues, and these results re-run the paper's statistics on its own data rather than derive them independently. The claims file allows this (with_labels/with_inputs), but the outcomes should be read that way.
5. **[does not affect a conclusion] Cell 8, nearest-value fallback.** When a value matches within 1e-6 rather than exactly, `nmatch` is set to 1 without checking for other voxels inside the window. The largest difference is about 5e-7 in every group, so most matches probably took this path, and "ambiguous: 17" undercounts. Separately, cell 9 shows the paper's lists repeat the same voxel within a group (99, 44, 40 and 18 times in the four tables). The notebook never explains this; the paper's analysis carries the same repeats, so the statistics are unaffected.
6. **[does not affect a conclusion] `tukey_kramer`.** scipy's studentized range stops at about 1.4e-11, and the variant in cell 28 prints p=0.0 with an IntegrationWarning. Some small p differ from the paper (sham CB 8.4e-09 against 5.07e-09; dACC-CB 3.6e-08 against 1.3e-08; PCC 4.5e-11 against 8.22e-12; insula 6.8e-08 against 4.42e-08). All are far below 0.05. On synthetic unbalanced data the function matched statsmodels' Tukey HSD (p 0.8168 against 0.8168), and the `anovan` F values equal the paper's exactly.
7. **[does not affect a conclusion] fig6d.** The criterion asks for the local increase at the lead site, read from the thresholded map, to be reported. The notebook does not do this; only the area-25 ROI change is visible (+0.18, cell 38).
8. **[does not affect a conclusion] fig4 claims and ed10c.** DANDI:001773 holds `source_data/Source Data FC matrix.xlsx` and `FC_ROI_label.xlsx`, which the notebook never mentions. Under the claims file they cannot stand in for the dataset's measurements, and 001785 has nothing to link them to, so data_missing stands.
9. **[does not affect a conclusion] fig5a-control-group-no-reduction.** The notebook's reason ("one map per session; no runs") covers reading (a) only. Reading (b), a one-sample t-test of the per-animal change, could be run on the deposited B, W and H maps (n=3), with D99 PCC/vmFC masks and cluster correction from smoothness estimated on the maps. The claim stays blocked because reading (a) cannot be run.
10. **[does not affect a conclusion] Cell 71.** The behaviour columns are assigned by position and the headers are never printed. The exact F match for N and T supports the assignment.
11. **[does not affect a conclusion] Paper misprint.** For ed6b, the paper prints DAPI p=0.9611, but its own counts give F=0.0038, p=0.9511 (cell 67), and its stated partial eta squared of 4.97e-05 fits F=0.0038.
12. **[does not affect a conclusion] fig3f.** The notebook's blocked table gives no reason category.

### C. What I could not check

- **The counting pipeline.** I did not see the IF images themselves. Printing per-field scatter plots of image counts against sheet counts, and the CC1/DAPI channel assignment checked on one field against the sheet, would let me judge B3.
- **The EM sheet.** I don't know whether `dbs_EMgratio_MCC_CB_data_a.xlsx` gives axon positions as well as image names; that would make fig3f partly testable. Printing the sheet's header rows would settle it.
- **Which match path each FA value took.** Exact against nearest is not output. Counts per path, plus the number of voxels within 1e-6 on the nearest path, would settle B5.
- **Reading (b) of fig5a-control-group-no-reduction.** It was not run, so I cannot say whether it would agree with the claim.
- **The lead-site increase for fig6d.** Not output (B7).
