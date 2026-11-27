**A. Outcomes**

The claims file has 45 claims. The notebook tests 39 and blocks 6.

| Claim | Outcome | Reason |
|---|---|---|
| link-somatic-cells | partially_reproduced | Cell 15: all 12 groups have the paper's n. 73.2% of cells match a paper row exactly (criterion needs 80%) and 85.4% match within 3 spikes (criterion needs 95%). Clears the 50% exact bar for partial. |
| link-dendritic-cells | reproduced | Cell 17: 8 of 10 groups have the paper's n (criterion needs 7). Median relative difference is 0.028 against a 0.10 limit. |
| link-sr-cells | partially_reproduced | Cell 19: all 33 cells match a paper identifier. Only 39% have both mean amplitude and event count within 25% (criterion needs 75%). The detector finds a median 1.33× the paper's event count. |
| link-grab-rois | not_reproduced | Cell 21: the dandiset holds every region, but only 16 of 34 regions match a paper region within 0.05 on every treatment. That fails both the reproduced and the partial bar. 10 paper regions are each picked by more than one dandiset region, so a one-to-one match would score lower still. |
| link-aim-mice | not_reproduced | Cell 23: Figure 8 session totals equal the paper's in only 6% and 16% of sessions, and 3 mice are not in the paper. Figure 10 agrees (98% of sessions). The dandiset description confirms the Figure 8 sheets differ from the published figure. |
| fig1f-dspn-rheobase-on-lower | reproduced | P = 8.9e-6; on-state median 140 pA against 220 pA off-state. |
| fig1e-dspn-fi-on-higher | reproduced | Spike sum P = 8.8e-5, on-state higher (median 88 against 36). |
| fig1f-dspn-sch-no-change | reproduced | P = 1.0. |
| fig1i-dspn-dendritic-on-higher | reproduced | P = 0.0091, on-state higher; P = 0.017 with every proximal site paired with every distal site. |
| fig1i-dspn-dendritic-sch-lower | not_reproduced | P = 0.066 (exact P 0.065), and 0.079 with every proximal site paired with every distal site. The SCH median is lower (0.419 against 0.476). The paper gives P = 0.0133. |
| fig1-dspn-lesion-and-off-somatic | reproduced | Paper's table: P = 0.0003 and 9.5e-5, both in the stated direction. |
| fig1-dspn-lesion-dendritic-unchanged | reproduced | P = 0.82 and 0.90. |
| fig2h-dspn-sr-amplitude-on-larger | reproduced | P = 0.0031 at 5 SD with mean amplitude, 0.0044 with median amplitude, on-state larger. Only the 3 SD median reading is above 0.05 (0.068). |
| fig2i-dspn-sr-frequency-unchanged | reproduced | P = 0.122 at 5 SD and at least 0.05 under every reading. The 4 SD reading is marginal (P = 0.0505). See problem 4. |
| fig2bc-dspn-spines | blocked (methods_underspecified) | Needs spine counts made with manual correction; see problem 2. |
| fig3d-ispn-rheobase-on-higher | reproduced | P = 0.00083, on-state higher. |
| fig3c-ispn-fi-on-lower | reproduced | P = 7.2e-5, on-state lower. |
| fig3d-ispn-sul-no-change | reproduced | P = 0.143. |
| fig3f-ispn-dendritic-on-lower | reproduced | P = 0.0128, on-state lower (n = 9 against 10). |
| fig3f-ispn-dendritic-sul-no-change | reproduced | P = 0.093 and 0.139. |
| fig3-ispn-lesion-and-off-somatic | reproduced | P = 0.0004 and 0.0006, both in the stated direction. |
| fig3-ispn-lesion-dendritic-up | reproduced | P = 0.035 and 0.024, later group higher in both. |
| fig4g-ispn-sr-amplitude-on-smaller | reproduced | P = 0.0093 at 5 SD; at most 0.04 under every reading. |
| fig4h-ispn-sr-frequency-unchanged | reproduced | P = 0.12 to 0.19 under every reading. |
| fig4bc-ispn-spines | blocked (methods_underspecified) | As fig2bc. |
| fig4k-confocal-spines | blocked (methods_underspecified) | Counts came from Imaris with manual correction. The notebook's stated reason is wrong; see problem 1. |
| fig5f-ach-off-elevated | reproduced | Per region P = 5e-5 under all three variants; P = 0.036 with one value per mouse. |
| fig5f-ach-off-like-6ohda | reproduced | P = 0.22, 0.79 and 0.22 across the three variants. |
| fig5f-ach-6ohda-elevated | reproduced | P = 0.0002 to 0.0003. |
| fig5f-ach-d2-control | reproduced | Wilcoxon: sulpiride higher in all 13 regions and quinpirole lower in all 13, P = 0.00024 each. |
| fig5f-ach-da-suppresses | reproduced | Dopamine P = 0.002 (6-OHDA) and 0.001 (off-state); sulpiride after the lesion P = 0.85 to 0.92. |
| fig6c-m1r-antag-somatic-unchanged | reproduced | P = 0.68. |
| fig6d-m1r-antag-dendritic-lower | reproduced | P = 0.023 (0.0079 with every proximal paired with every distal), antagonist lower. |
| fig6f-m1r-antag-spines | blocked (methods_underspecified) | As fig2bc. |
| fig7c-cdgi-ko-somatic-oscillation | reproduced | P = 0.001, on-state higher (210 against 140 pA). |
| fig7e-oxom-cdgi | reproduced | Wild type P = 0.0098 with oxo-M higher; KO P = 0.47. |
| fig7f-cdgi-ko-dendritic-unchanged | reproduced | P = 0.32 and 0.63. |
| fig7h-cdgi-ko-spines | blocked (methods_underspecified) | As fig2bc. |
| fig8a-cdgi-rotations | reproduced | P = 0.012, KO higher. |
| fig8bc-cdgi-aims | blocked (data_missing) | The deposited Figure 8 sheets are the preprint scores, and 5 of the paper's 23 mice are absent (dandiset description, items 7 and "Known limitations"). link-aim-mice fails for Figure 8. |
| fig9d-m1r-crispr-somatic-unchanged | reproduced | P = 0.147. |
| fig9f-m1r-crispr-spines | blocked (methods_underspecified) | As fig2bc. |
| fig10a-m1r-rotations | reproduced | P = 0.0078, deletion higher. |
| fig10b-m1r-aims | reproduced | Group F(1,19) = 13.80, 41.43 and 44.58 for axial, limb and orolingual, equal to the paper's; total 28.70 against 29.30. All P < 0.002 with CRISPR lower. |
| fig10ef-open-field | reproduced | Both measures, all three comparisons in the stated direction (P ≤ 0.0006 and P = 0.63 / 0.47). |

**B. Problems**

1. [does not affect a conclusion] Cell 0 says the Figure 4I to 4K confocal images are not in the dandiset. That is wrong for this draft. The archive holds 17 Adora2Cre "M####" files described as "High-resolution confocal z-stacks … the data of Figure 4, J and K" (for example asset c92df083…), plus a Figure 4I overview (c2141930…). fig4k stays blocked, but because counting needs Imaris with manual correction, not because data are missing.
2. [does not affect a conclusion] Cell 0 gives the spine blocks the reason "not runnable", which is not an allowed reason code. methods_underspecified fits. The archive has 76 two-photon spine Z-stack files with no counts, and the dandiset description says the paper's spine table rows "cannot be matched to the files". So no part of these claims can be tested from the dandiset itself.
3. [affects a conclusion] fig1i-dspn-dendritic-sch-lower (cells 17 and 47) never mentions a documented data gap. The dandiset description (item 3) says the first site pair of dSPN 2019-04-11 cell 1 (on-state with SCH) is not deposited. So the dandiset index for that SCH cell is computed from different data than the paper's. Only 78% of SCH cells agree within 10% (cell 17). With 10 against 9 cells, a shift in one or two values can move P from 0.013 to 0.066. The notebook does not show whether the not_reproduced outcome comes from this data gap or from the method.
4. [does not affect a conclusion] For fig2i and fig4h (cells 61 and 65), the frequency claims rest on `detect_events`. That detector matches the paper's per-cell event count within 25% for only 42% of cells, at a median 1.33× the paper's count (cell 19). fig2i at 4 SD sits at P = 0.0505. The outcomes hold under every reading, but the margin is thin.
5. [does not affect a conclusion] The criterion for link-sr-cells compares "per-cell mean amplitude", but cell 19 shows the paper's per-cell amplitude equals the median of its event list for 33 of 33 cells. The claims file misreads the paper's tables here. Under either reading, fewer than 75% of cells pass on both amplitude and count, so the outcome is partial either way.
6. [does not affect a conclusion] link-grab-rois (cell 21) matches regions to the paper's regions many-to-one, so 10 paper regions are reused. The criterion's unit was changed from mouse to region, and the notebook says so. The link is run only with Fmin = min(TTX, quinpirole). Normalised areas change by up to 1.7× under Fmin = TTX (6-OHDA median 0.315 against 0.539), and the notebook never checks which rule matches the paper's values.
7. [does not affect a conclusion] Cell 3 picks the Sr2+ files by a heuristic: date starts with "2023", modality icephys, not Adora2Cre. It works here, because the cell counts equal the legends, but nothing in the file metadata confirms the choice.
8. [does not affect a conclusion] The variant that keeps the last sweep of a repeated step is run only for the two rheobase claims (cells 25 and 31). It is not run for the spike-sum claims or for the absence claims fig3d-sul and fig9d, which have P = 0.14 to 0.15.
9. [does not affect a conclusion] Cell 23 merges AIM sessions on mouse and session but not on figure. That is safe only if mouse IDs never repeat across the two figures, which the notebook does not check.

Helper checks on synthetic inputs all behaved correctly: `count_spikes`, `cell_fi` (rheobase, first sweep kept for a repeated step), `detect_events` (10 of 10 events found, an event outside the window rejected, amplitudes correct) and `site_signal` (0.1366 against an expected 0.1375). The `mixed_anova` group F reproduces three of the paper's F values exactly. Exact and asymptotic Mann-Whitney P agree for every borderline test.

**C. Could not check**

- The paper's per-cell values themselves, since the Zenodo tables were not available to me. Two outputs would settle problem 3: the Mann-Whitney P on the paper's own Figure 1I table for on-state against SCH, and the per-cell comparison for the SCH group with 2019-04-11 cell 1 flagged.
- Whether the frequency claims depend on the detector. A Mann-Whitney test on the paper's own Figure 2I and 4H frequencies, shown next to the detector results, would show that.
- Which Fmin rule the paper's GRAB values used. link-grab-rois rerun with Fmin = TTX, one-to-one, would show it.
- That the file's `condition` column is the claims file's `condition_subfolder`. A printout of each file's condition values against its folder or session name would confirm it.
- The F of 29.30 for total AIMs. The ANOVA rerun on the lab's own "total" column would show whether that explains it.
