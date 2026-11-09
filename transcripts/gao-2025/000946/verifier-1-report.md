**Verifier report, round 1: Gao et al. 2025 (J Neurosci), DANDI:000946 v0.250829.1249**

The claims file has 33 claims. The notebook tests one of them (fig11b) and treats the other 32 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig4-unit-counts | **not_reproduced** | The notebook calls this blocked, but its own totals in cell 17 decide it. POm units at 3000 Hz are 352 against 233+17 = 250, and at 30 Hz 315 against 232. Both are far outside 10%, so neither the "reproduced" outcome (eight counts in tolerance) nor the "partial" one (area totals within 10%) can be reached under any RSU/FSU split. |
| fig4a-s1-rsu-time-locked-3000 | blocked (data_missing) | Cell 4: `celltype_label` is 0 in all 1516 files that have it and absent in the other 34. No file has waveforms, and no acquisition, analysis or processing group has content. The archive agrees: variableMeasured is Units and ElectrodeGroup only, and unit files are at most 12.6 MB. |
| fig4b-pom-rsu-time-locked-3000 | blocked (data_missing) | Same: needs RSU typing. |
| fig4-postsonication-3000 | blocked (data_missing) | Same. |
| fig4-30hz-responses | blocked (data_missing) | Same. |
| fig4-fsu-no-change | blocked (data_missing) | Same: needs FSU typing. |
| fig5a-sham-no-change | blocked (data_missing) | No cell types. Cell 8: no identifier, note or data_collection field names sham or no tFUS. |
| fig5b-cg1-control-no-change | blocked (data_missing) | No cell types, and no session is aimed at CG1. Targets in the data are only S1, M1 and POm (cell 8). |
| fig6-unit-counts | **not_reproduced** | Cell 17 again. S1 totals are 986, 1726 or 2414 depending on the S1 selection, against 1297 ±10% (1167 to 1427). POm is 1470 against 1019 ±10%. No split can rescue either. |
| fig6a-s1-rsu-time-locked-prf | blocked (data_missing) | Needs RSU typing. |
| fig6a-s1-rsu-delayed-prf | blocked (data_missing) | Same. |
| fig6b-s1-fsu-prf | blocked (data_missing) | Same. |
| fig6c-pom-rsu-prf | blocked (data_missing) | Same. |
| fig6d-pom-fsu-prf | blocked (data_missing) | Same. |
| fig7a-s1-rsu-dc-3000 | blocked (data_missing) | Same. |
| fig7b-s1-fsu-dc-3000 | blocked (data_missing) | Same. |
| fig7c-pom-rsu-dc-3000 | blocked (data_missing) | Same. |
| fig7d-pom-fsu-dc-3000 | blocked (data_missing) | Same. |
| fig8a-s1-rsu-dc-30 | blocked (data_missing) | Same. |
| fig8b-s1-fsu-dc-30 | blocked (data_missing) | Same. |
| fig9a-s1-rsu-prf-60dc | blocked (data_missing) | Same. |
| fig9b-s1-fsu-prf-60dc | blocked (data_missing) | Same. |
| fig10a-dsttc-3000 | blocked (data_missing) | dSTTC between typed S1 and POm units. The stored STTC arrays carry no unit types (cell 19). |
| fig10b-dsttc-30 | blocked (data_missing) | Same. |
| fig10c-sttc-constant-pd | blocked (data_missing) | Needs S1 RSU to POm RSU STTC. The stored STTC is untyped and its dt is not stated (cell 19: array shape (10 windows, 499 trials, 20, 9), with no dt axis). |
| fig10d-sttc-60dc | blocked (data_missing) | Same. |
| fig10e-sttc-dc-30 | blocked (data_missing) | Same. |
| fig10f-sttc-dc-3000 | blocked (data_missing) | Same. |
| pathway-follows-local-prf | blocked (data_missing) | Depends on fig6a and fig10c, both blocked. |
| fig11b-ac-responses | **blocked (methods_underspecified)** | Cell 24: the four method readings give different outcomes. N1/B1 is partial (during-sonication set {1500, 3000, 4500}, one PRF too many). N1/B2 is not reproduced (300 Hz also above baseline during sonication). N2/B1 and N2/B2 are not reproduced (Kruskal-Wallis in 0–67 ms p = 0.0213). The claims header says that when readings differ, the claim is blocked as methods_underspecified with every result shown. No reading reproduces the claim. The unit count is 633 against 453 ±45.3, outside tolerance. |
| fig11c-ac-to-s1-30hz | blocked (data_missing) | The target units must be S1 RSUs, which are untyped. |
| fig11d-ac-to-s1-3000 | blocked (data_missing) | Needs S1 RSUs and S1 FSUs. |
| auditory-confound-low-prf | blocked (data_missing) | Depends on fig11c and fig11d. |

For the cell-type claims, I checked the archive itself (API metadata and the full asset list). Its 1920 files are all NWB: 1550 unit files and 370 STTC files, with nothing else. File sizes, at most 12.6 MB for unit files, are consistent with spike times only. Nothing would let any RSU/FSU claim be tested in part. The paper does not state a chance level for any selection, so there was none to compare.

### B. Problems

1. **[affects a conclusion]** Cell 0 table and cell 17: fig4-unit-counts and fig6-unit-counts are marked blocked. The totals the notebook prints already rule out both the reproduced and the partial outcome, so the criterion gives "not reproduced". This is subject to item 6.
2. **[affects a conclusion]** fig11b, cells 24–25: the four readings disagree, so the claims header's rule makes the outcome blocked (methods_underspecified). The notebook's `judge` gives a verdict per reading but never combines them under that rule. Any single verdict taken from the N1/B1 row ("partially reproduced") would break the claims file.
3. **[does not affect a conclusion]** Claims file, reading N2: averaging per-trial ratios over trials with a nonzero baseline is biased low. The notebook shows this: 50–62% at onsets shifted by 1 s, where there is no stimulus (cell 27). My synthetic Poisson test (λ = 0.5 per window, no effect) gives N1 ≈ 86% versus N2 ≈ 45%. N2 is therefore not a reasonable reading of "normalized to the pre-stim period". This is a claims-file problem, which I report and do not correct. Dropping N2 would not change fig11b, because N1/B1 and N1/B2 still disagree.
4. **[does not affect a conclusion]** Claims file, reading B1 under N1: the "baseline sample" is exactly 100 for every unit, so the rank-sum test is effectively a one-sample location test. On synthetic null data, `vs_baseline` with B1 had a false-positive rate of 2.3% at α = 0.01. With B2 it was 0%. The fig11b p-values are far from the threshold, so no decision changes.
5. **[does not affect a conclusion]** fig11b pooling, cells 23 and 28: each PRF comes from only 3 or 4 of 6 rats, and the rats differ by PRF. Single rats dominate some means; for example BH538 at 3000 Hz, 201–268 ms, averages 654% against a pooled 310.5%. So the Kruskal-Wallis across PRFs confounds PRF with rat. The paper probably pooled the same way, so this is a caveat, not an error.
6. **[could affect the count outcomes]** Cells 10 and 17, session selection: PD 200 µs, tFUS at S1, area exactly "S1", "POM" or "AC". This keeps identifiers with suffixes (POM_POM, NEAR, back, front, contra, NEW, _2, dep05, cell 8), which may be repeat or off-target placements the paper left out. It also drops the AC_1, AC_2 and S1_1 files of a seventh AC rat. The count verdicts in item 1 assume every such session counts. The criterion's wording ("sessions of the S1 and POm rats") supports that, but it was not checked.
7. **[does not affect a conclusion]** Cells 12–15: trial `start_time` is assumed to be sonication onset. The 1 s-shift control and the PSTHs show it is stimulus-locked, but not that it has zero latency. The notebook says this itself.
8. **[does not affect a conclusion]** Helpers checked on synthetic inputs: `window_counts` uses half-open windows [a, b) correctly, `normalized_rates` (N1 and N2) and `vs_baseline` (Bonferroni factor 5, as in reading C1) behave as described, and `dedupe` is confirmed by spike-time hashes (734 of 734 identical). No train/test split exists, so leakage does not apply.
9. **[does not affect a conclusion]** Cell 9: the dataset has 20 rats, while the paper reports 16 S1/POm rats and 12 S1/AC rats. It also holds M1 recordings and tFUS aimed at M1 or POm, which the paper does not describe. Despite having fewer AC rats (7 vs 12), it has more AC units (633 vs 453). The paper's selection evidently differs, and the notebook does not investigate why.

### C. What I could not check, and the output that would settle it

- **Whether suffixed sessions belong in the paper's sets** (items 1 and 6). I need the unit totals per area and PRF from cell 17, broken down by identifier suffix and by rat. That would show whether excluding repeat or off-target sessions could bring POm to about 250 and 232 at 3000 and 30 Hz, and 1019 over the PRF series.
- **The seventh AC rat.** I need the PRF, PD and unit counts of its AC_1, AC_2 and S1_1 recordings.
- **Whether any M1- or POm-aimed session matches the CG1 control.** No metadata gives probe or target coordinates. Even if one did, the cell-type block would remain.
- **fig11b at the rat level.** Results with each rat left out, under N1/B1 and N1/B2, would show whether the during-sonication sets and the "lowest at 300 Hz" part depend on BH537 or BH538.
- **SEMs for fig11b.** They are computed but not printed in cell 25. I could only see means and p-values.
