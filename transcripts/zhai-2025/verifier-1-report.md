**A. Outcomes** (45 claims in the claims file: 5 links and 40 findings; the notebook treats 6 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| link-somatic-cells | partially_reproduced | All 12 groups have the paper's n. 90/123 cells (73.2%) match exactly, under the 80% bar, and 105/123 (85.4%) are within 3 spikes, under the 95% bar (cell 11). |
| link-dendritic-cells | reproduced (provisional) | 10/10 groups have the paper's n and the median relative difference is 0.027 (cell 32). This is provisional because of the background bug in problem 1. |
| link-sr-cells | partially_reproduced | All 33 cells match a paper identifier. Only 21/33 (64%) are within 25% on both amplitude and count, under the 75% bar (cell 47). |
| link-grab-rois | not_reproduced | Region counts equal the paper's (13/10/11), but only 16/34 regions match within 0.05 on every treatment (under half), and 11 paper regions are matched more than once (cell 58). Grouped by mouse (date), only 1 of 11 mice matches. |
| link-aim-mice | not_reproduced | Figure 8: 12 of 90 matched session totals are equal, 3 dandiset mice are not in the paper and 5 paper mice are missing. Figure 10: 103/105 equal (cell 71). The dandiset description says the Figure 8 sheets match the preprint, not the published figure. |
| fig1f-dspn-rheobase-on-lower | reproduced | P=8.9e-6, on-state median 140 against off-state 220 (cell 14). |
| fig1e-dspn-fi-on-higher | reproduced | P=8.8e-5, on-state higher (cell 16). |
| fig1f-dspn-sch-no-change | reproduced | P=1 (cell 18). |
| fig1i-dspn-dendritic-on-higher | reproduced | P=0.0091, on-state higher (cell 35). |
| fig1i-dspn-dendritic-sch-lower | not_reproduced | P=0.079 (cell 37). The cell of 2019-04-11 lacks the pair the paper used (dandiset description, item 3). Excluding it gives P=0.034, but that is not a reading the paper allows. The background bug could change this outcome. |
| fig1-dspn-lesion-and-off-somatic | reproduced | On the paper's table, P=0.0003 and 9.5e-5, both in the stated direction (cell 79). |
| fig1-dspn-lesion-dendritic-unchanged | reproduced | P=0.82 and 0.90 (cell 81). |
| fig2h-dspn-sr-amplitude-on-larger | reproduced | P=0.0062, on-state larger, robust across variants (cell 50). |
| fig2i-dspn-sr-frequency-unchanged | reproduced | P=0.0999, all variants ≥0.05 (cell 52). |
| fig2bc-dspn-spines | blocked (other) | Raw z-stacks only. Spine counting needs AutoQuant deconvolution and semi-manual NeuronStudio. |
| fig3d-ispn-rheobase-on-higher | reproduced | P=0.00083, on-state higher (cell 20). |
| fig3c-ispn-fi-on-lower | reproduced | P=7.2e-5, on-state lower (cell 22). |
| fig3d-ispn-sul-no-change | reproduced | P=0.143 (cell 24). |
| fig3f-ispn-dendritic-on-lower | reproduced | P=0.0058 (cell 39). |
| fig3f-ispn-dendritic-sul-no-change | reproduced (fragile) | P=0.05453, right at the threshold (cell 41). The background bug could flip it. |
| fig3-ispn-lesion-and-off-somatic | reproduced | P=0.0004 and 0.0006 on the paper's table (cell 83). |
| fig3-ispn-lesion-dendritic-up | reproduced | P=0.035 and 0.024, later group higher (cell 85). |
| fig4g-ispn-sr-amplitude-on-smaller | reproduced | P=0.0093, on-state smaller, robust across variants (cell 54). |
| fig4h-ispn-sr-frequency-unchanged | partially_reproduced | With all sweeps P=0.064. With the first 10 sweeps, the count the paper's frequencies imply, P=0.049 (cell 56). The outcome depends on a choice the paper leaves open. |
| fig4bc-ispn-spines | blocked (other) | Same as fig2bc. |
| fig4k-confocal-spines | blocked (data_missing) | No confocal files in the archive. They are in Zenodo 17260198, and counting used Imaris. |
| fig5f-ach-off-elevated | reproduced | P=5e-5, off-state higher, all variants agree (cell 61). |
| fig5f-ach-off-like-6ohda | reproduced | P=0.245; variants 0.22 to 0.79 (cell 63). |
| fig5f-ach-6ohda-elevated | reproduced | P=0.00022 (cell 65). |
| fig5f-ach-d2-control | reproduced | Wilcoxon: sulpiride raises 13/13 and quinpirole lowers 13/13 regions, P=0.00024 each (cell 67). |
| fig5f-ach-da-suppresses | reproduced | Dopamine P=0.002 and 0.00098, lowering every region; sulpiride after the lesion P=0.92 (cell 69). |
| fig6c-m1r-antag-somatic-unchanged | reproduced | P=0.68 (cell 26). |
| fig6d-m1r-antag-dendritic-lower | reproduced | P=0.016, antagonist lower (cell 43). |
| fig6f-m1r-antag-spines | blocked (other) | Same as fig2bc. |
| fig7c-cdgi-ko-somatic-oscillation | reproduced | P=0.001, on-state higher (cell 28). |
| fig7e-oxom-cdgi | reproduced | On the paper's table, wild type P=0.0098 with oxo-M higher, KO P=0.47 (the paper reports 0.91) (cell 87). |
| fig7f-cdgi-ko-dendritic-unchanged | reproduced | KO P=0.27 (cell 45). |
| fig7h-cdgi-ko-spines | blocked (other) | Same as fig2bc. |
| fig8a-cdgi-rotations | reproduced | P=0.012, KO higher (cell 89). |
| fig8bc-cdgi-aims | reproduced, with caveat | All four group effects P<0.05 with KO lower. Axial is much weaker than in the paper (F=6.87 against 19.91). These are the preprint score sheets, and link-aim-mice fails (cell 73). |
| fig9d-m1r-crispr-somatic-unchanged | reproduced | P=0.147 (cell 30). |
| fig9f-m1r-crispr-spines | blocked (other) | Same as fig2bc. |
| fig10a-m1r-rotations | reproduced | P=0.0078 (cell 91). |
| fig10b-m1r-aims | reproduced | F(1,19) = 28.7, 13.8, 41.4 and 44.6, all P<0.002. The last three equal the paper's (cell 75). |
| fig10ef-open-field | reproduced | All six tests in the stated direction (cell 93). |

**B. Problems**

1. **[affects a conclusion]** `zhai._site_trace` subtracts the wrong background from the red channel. It picks the background with `"Alexa" in col`, but `col` is always `"red"` or `"grn"`, so 161 is subtracted from red instead of 55. I confirmed this on a synthetic trace: a red value of 300 came out as 139, where 245 was expected. This changes R0, the index and the basal ratio for every dendritic cell. That touches link-dendritic-cells and the two outcomes near the threshold: fig1i-dspn-dendritic-sch-lower (P=0.079) and fig3f-ispn-dendritic-sul-no-change (P=0.0545).
2. **[affects a conclusion]** In cells 11, 14 and 20, the "last sweep of a repeated step" variant is a no-op. `per_cell_somatic` re-sorts by `start` in ascending order, so the descending input is undone. On a synthetic cell the "last sweep" result came out the same as the first-sweep one (120 both times), and the notebook's variant outputs are identical to the main ones. So the first-sweep assumption, which touches 14 of 123 cells, was never varied. That leaves the somatic link and the rheobase claims of absence (P of 0.14 to 0.15) untested against it.
3. **[affects a conclusion]** fig4h, cells 47 and 56: the main analysis uses all sweeps, although the paper's frequencies (and the dandiset description) imply 10 sweeps per cell. Only "first 10" was tried, not "last 10", and the outcome flips between readings.
4. **[affects a conclusion]** fig1i-dspn-dendritic-sch-lower, cells 33 and 37: the dandiset does not hold the 2019-04-11 pair behind the paper's value of 0.228 for that cell. The exclusion variant is informative but is not a reading the paper allows. The data as deposited give not_reproduced.
5. **[does not affect a conclusion]** `somatic_link`, cell 11: the code assumes row j of the rheobase sheet is the same cell as row j of the F-I sheet, and never checks this. Best matches are not one-to-one, and how many paper rows are reused is not reported.
6. **[does not affect a conclusion]** `grab_link`, cell 58: matching is done per region, not per mouse as the criterion says, and is not one-to-one (11 paper regions are reused). A one-to-one assignment could only lower agreement, so not_reproduced stands.
7. **[does not affect a conclusion]** `grab_areas` and cell 59: the dandiset description says 2024-04-02 Slice1Roi2 has no acetylcholine trial, but the notebook finds two (4.4 s and 1.2 s) and computes Fmax from them. This is not reconciled. Separately, trials within one condition with different frame intervals (0.047 to 0.1996 s overall) would be misaligned because a single median `dt` is used, and this is not checked per condition.
8. **[does not affect a conclusion]** fig8bc, cell 73: the test runs on 21 preprint-sheet mice, 3 of which are not in the paper. The helper itself is validated: run on the paper's table, `mixed_anova_group` reproduces the paper's F(1,21) values exactly, and my synthetic check matches a hand-computed split-plot F.
9. **[does not affect a conclusion]** fig7e, cell 87: pairing the paper's KO rows by `expt` gives P=0.47 where the paper reports 0.91. The pairing may differ from the authors'.
10. **[does not affect a conclusion]** `dendritic_link`: the Figure 6D letter is taken from the cell number, while the claims file defines it as the ordinal of the cell within the day. The two are the same only when cells are numbered without gaps.
11. **[does not affect a conclusion]** `detect_events` is a stand-in for TaroTools. Amplitudes run a median 11% above the paper's, and the smoothed-noise variant inflates event counts by 36%. The amplitude claims hold under both variants.
12. **Claims file, link-grab-rois:** the criterion speaks of "each mouse's vector", but the paper's unit is the ROI and each mouse holds several. This misreads the unit. The notebook departs from the wording and states that it does.
13. **[does not affect a conclusion]** Cell 9 calls the 93 spine files "raw image stacks only" from file names alone. No file was opened to rule out spine annotations.

**Blocked claims, checked against the archive.** The file list has 93 spine-image NWB files. iSPN: unlesioned 14, lesioned 10, off-state 15, on-state 9, CDGI KO off/on 6/3, M1R antagonist 5, M1R KO 3. dSPN: 6, 5, 8 and 9 across the same four main groups. Their asset metadata `variableMeasured` is empty. No file name mentions confocal, Imaris, spines or counts, and the dandiset description puts spine densities and confocal data on Zenodo. So spine counts from the dandiset need AutoQuant deconvolution plus semi-manual NeuronStudio counting: blocked (other). The only part that can be tested is re-running the paper's statistics on its own Zenodo spine tables, which is not a reproduction from the dandiset. fig4k is data_missing.

**C. What I could not check, and the output that would settle it**
- The dendritic results with a red background of 55. A rerun of cells 32 to 45 after fixing `_site_trace` would settle the link and the fig1i-sch and fig3f-sul outcomes.
- Rheobase and F-I results with the last sweep of a repeated step. A working variant, plus a per-cell list of first against last rheobase for the 14 cells, would settle it.
- fig4h with the last 10 sweeps for the two cells that have 11 and 12 sweeps.
- How many paper rows are best-matched more than once in the somatic link, and whether the rheobase sheet and F-I sheet rows line up.
- The frame interval per GRAB condition, and the trial labels for 2024-04-02 Slice1Roi2.
- Whether the spine NWB files hold any segmentation (an HDF5 group listing of one file).
- The Zenodo table labels, for example whether `"-M1R"` in 10E/F is the MCI-Park + M1R-deletion group. Printing the unique group values per sheet would answer this.
