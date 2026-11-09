**A. Outcomes**

The claims file has 35 claims. The notebook tests 21 of them and treats 14 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| code-table-link | reproduced | All 288 files the table lists are in the dandiset. The table's presynaptic channel is the one that fires in 281/288 files (97.6%), and its postsynaptic channel holds a cell in 1385/1416 pairs (97.8%). Both are above the 90% threshold (cell 8). |
| fig5d-connectivity-totals | not_reproduced | There are 26 annotated connections (23 without "OK"), against 31 ± 3.1 (cell 11). Pair count 1416/1410 is within 1292 ± 129. Neuron count passes from the files (410) but fails from the table (295; 298 once the table is read correctly). Reading (a) does not exist, since the dataset has no labels. |
| fig5-pc-to-pc | not_reproduced | 18 of 743 (749 once the table is read correctly), 2.42%, against 24/503, 4.77%. All three values are outside tolerance under every reading (cell 14). |
| fig5-ven-outputs-absent | partially_reproduced | VEN-to-IN 0/54 holds and VEN-to-VEN has 0 connections. But VEN-to-VEN pairs are 59 (expected 110 ± 11), VEN-to-PC pairs are 146 (expected 200 ± 20), and there is one annotated VEN-to-PC connection where the criterion needs 0. That pair (190315s2, 4→6, "Excellent") shows a clear 1.01 mV averaged response, peak/s.d. 95.8 (cell 16). |
| fig5-pc-to-ven | partially_reproduced | 1 connection holds; 145 pairs is outside 200 ± 20 (cell 18). |
| fig5-pc-in | partially_reproduced | Connection counts 2 and 4 hold (with "OK" counted, as the criterion says). Pairs are 84 and 86, outside 65 ± 6.5 (cell 20). |
| fig5-in-to-ven-absent | reproduced | 0 of 54, against 0 of 55 ± 5.5 (cell 22). |
| fig5i-ven-sparse-local-connectivity | partially_reproduced | All four Fig. 5i rates are outside tolerance (2.42, 2.38, 0.69, 4.65% against 4.77, 3.08, 0.5, 6.15). Every VEN rate is below its paired PC rate (cell 24). The Fisher variants are all p ≥ 0.16. |
| fig5fg-example-slice | reproduced | Pair 2→6 (channel 2→8) is annotated "Ext", and no pair from cell 4 (channel 6) is annotated (cell 26). |
| fig5-pair-distances | blocked (data_missing) | The archive holds only the 301 NWB files, and their asset metadata have no positions (I checked the API). The code table has no position column. The NWB group check is not fully shown (problem 3). |
| fig5-pc-rate-comparable-primate | blocked (methods_underspecified) | Blocked by the criterion itself; the rate is printed (2.42%). |
| fig5b-psc-frequency | reproduced | The VEN median is lower for all four event types, p = 0.0068, 0.0093, 0.028 and 0.010. Group sizes match the legend, and I checked the column layout of the code's sheets (cell 35). |
| fig5c-psc-amplitude | reproduced | p = 0.11, 0.69, 0.57 and 0.14, all ≥ 0.05 (cell 35), on the code's per-cell values. The mean and median readings could not be run (problem 9). |
| fig4d-sodium-current | partially_reproduced | VEN is lower in every variant, but p < 0.05 in only 4 of 8 window/step variants the author chose (p = 0.008 to 0.096). Reading (b) cannot run. The code's own `max_Na_current` gives p = 0.001 (cell 37). |
| fig3e-phase-peak-index | reproduced | VEN median 0.116 is the lowest. Kruskal-Wallis p = 6.5e-8, and Dunn/Bonferroni p ≤ 0.001 against each PC type (cell 39). |
| fig4j-eepsp-amplitude | reproduced | VEN is higher. Cell-type p = 0.0056 (ordinary ANOVA) and 0.0065 (repeated measures), but on 23 pairs, not 26 (cell 32). |
| fig4j-eepsp-latency | blocked (data_missing) | The code table holds no latencies, and the paper names no dandiset for the raw recordings. |
| fig3c-ais-distance-length | blocked (metadata_insufficient) | The table has no slice or animal column, so the two-way ANOVA cannot run. The n also differ (120/500 against the paper's 108/430). |
| fig8a-metabolite-gradient | not_reproduced | AIC vs V1 gives 175 to 195 under all four variants, against 228 ± 23. AIC vs PrC is within tolerance only for log/ungated (98). The input table holds 558 of the 581 metabolites (problem 4). |
| fig8de-glycolytic-bias | partially_reproduced | Citrate (p = 0.0005) and L-glutamic acid (p = 0.0001) are higher in AIC. 2-Ketobutyrate is lower but not significant (p = 0.18 raw, 0.087 log) (cell 42). |
| patchseq-mapping | partially_reproduced | 273 excitatory neurons and 17 types (within 18 ± 1.8). The 33 or 35 non-excitatory neurons fall within 34 ± 3.4. The inhibitory-type count (17 of 33) is untestable from the saved tables. |
| ven-map-et-ct | reproduced | 14 L5 ET and 15 L5/6 CT of 29 VENs (cell 44). |
| fig6f-g-ven-subtype-mapping | partially_reproduced | VEN-L maps entirely to L5 ET and VEN-S to L5/6 CT. But the counts are 14 and 15 against 10 ± 1 and 11 ± 1.1. The COL24A1 POC5 subcluster part is untested, and the notebook never compares the counts (cell 44). |
| scrna-classes, scrna-78-types, fig3ab-ven-axon-from-basal-dendrite, fig4ac-ap-width-amplitude, fig4i-peak-index-ais-distance, fig4g-model-ais-distance-ap-shape, model-ven-fires-more, fig6-ven-subtype-morphology, fig6h-subtype-markers, ven-subtypes-similar-physiology, fig7c-tau-rna-distance | blocked (other) | Data elsewhere; not attempted in this run (cell 0). |
| ven-firing-rate-variability | blocked (methods_underspecified) | Blocked by its criterion, which needs Supplementary Tables 1 and 2. |

No claim here involves a selection with a stated chance level.

**B. Problems**

1. **[does not affect a conclusion] `multipatch.code_table`: fill-down puts 39 rows under the wrong file.** The function fills `filename` and `preSynChannel` down the table. Ten presynaptic blocks have a blank filename (190315s2 channel 7; 190315s6 channel 8; 190315s7 channels 3, 6, 7; 20240912venHS1 channels 1, 2, 4, 6; 20241014venHS2 channel 8), so their 39 rows get the previous block's file. I confirmed this by reading the table from GitHub. Consequences:
   - Cell 8's "6 duplicate pairs" and 2 of its 7 "cells given two types" (20240911HS4 channels 2 and 6) are artefacts. Read correctly, the table has 0 duplicates, 5 cells with two types, 55 slices and 298 cells, not 54 and 295. Unique pairs are 1416, not 1410.
   - Eight of the 13 "files the table does not list" are in fact these blank blocks. Their firing channels match the table's presynaptic channels: 190315s6 channel 8; 190315s7 channels 3, 6, 7; 20240912HS1 channels 1, 2, 4, 6.
   - For these rows, `post_base`, `peak_mv` and `snr` come from the wrong file.
   - None of these rows is an annotated connection, so no outcome changes.
2. **[affects a conclusion] Cell 37, fig4d.** The peak windows (0.2–3 to 0.3–10 ms) are the author's own, and the result splits on them. The notebook's peak correlates with the code's `max_Na_current` at only r = 0.40–0.90, and the VEN medians differ (−23.7 to −30.6 pA against −14.9 pA). The measure is not validated against the paper's. Also, reading (b) per area is a constant rescaling of (a) if every patch is about 5 µm², so it is not really a separate untestable reading.
3. **[affects a conclusion] Cell 28: "no positions" is asserted, not shown.** Cell 28 prints "none hold positions" as a fixed string. The code (`read_file`) reads only `general/intracellular_ephys`, `stimulus` and `acquisition`. It never lists other groups (`general/*`, `lab_meta_data`, icephys tables, `processing`) or prints the values of the electrode `location` and `description` fields. The data_missing block of fig5-pair-distances, and the claim that the dataset carries no connection or cell-type labels (reading a), both rest on this.
4. **[affects a conclusion] Cell 41, fig8a.** The test uses the code's table of 558 metabolites, not the MetaboLights deposit of 581. The 23 missing metabolites could bring AIC vs V1 (195) within tolerance (205 or more), so not_reproduced rests on an incomplete input.
5. **[does not affect a conclusion] `presynaptic_channel` adds a condition the criterion lacks.** It requires a pre-pulse mean below −30 mV, which the code-table-link criterion does not ask for. Five of the 7 mismatches are depolarised channels (−2 to −23 mV) whose sweeps do cross 0 mV.
6. **[does not affect a conclusion] `response_stats` picks up pulse-locked artefacts.** Its 1–15 ms window catches artefacts. Several peaks sit exactly at the 1.00 ms window edge: annotated pairs 368, 755 and 797, and in cell 26 cell 2→3 (peak/s.d. 10) and cell 4→5 (peak/s.d. 30.6). In my synthetic test, a decaying 5 mV artefact gave peak/s.d. ≈ 200. These numbers are descriptive only, but cell 26's cell 4→5 value could be misread as a response.
7. **[does not affect a conclusion] Cells 8 and 9: annotation oddities the notebook does not flag.**
   - Eight connections from PC presynaptic cells are labelled "Inh": 7 PC-to-PC and 1 PC-to-IN.
   - Two "Inh" IN-to-PC pairs (249, 293) have positive peaks with peak/s.d. below 2.3.
   - Most "Inh" postsynaptic cells sit near −70 mV, not the −60 mV the Methods use for uIPSPs.
   - Row 368's projection label "4→3" disagrees with its postsynaptic channel 1, whose response is weak (peak/s.d. 2.83). Channel 3's response is not shown.
8. **[does not affect a conclusion] Cell 44 does not state or compare its counts.** The fig6f-g counts (14/15 against 10/11) are never compared. The "35 (paper 34 inhibitory)" includes 1 VEN and 1 PC_L5; the inhibitory-named neurons number 33.
9. **[does not affect a conclusion] Cell 35, fig5c.** The criterion's mean and median readings of event amplitude were not run; the code's per-cell value was used. Two p values (0.11 and 0.14) are not far from 0.05.
10. **[does not affect a conclusion] Cell 32, fig4j-eepsp-amplitude.** There are 23 pairs, not 26, and whether the monosynaptic selection was applied cannot be checked.
11. **[does not affect a conclusion] Cell 26, fig5fg.** The cell 4 presynaptic file has 9 sweeps, below the legend's "more than 20". The NWB files have no test rounds, so all sweeps are averaged.
12. **[does not affect a conclusion] Cell 11: neuron-count readings disagree.** The table gives 295 (298 once read correctly), outside 377 ± 38; the files give 410, inside. The notebook does not say this, but the outcome is fixed by the connection count anyway.

Checked and found sound:
- The 25 kHz rate: the stated 1 Hz is contradicted by the 50-sample = 2 ms pulse and the ~1.5 ms spike latency.
- The fixed pulse onset at sample 5000.
- The column layouts of the sPSC and mEPSC sheets.
- The Dunn's test formula.
- The pairing of VEN rates with PC rates.

**C. What I could not check, and the output that would have let me**

- **NWB contents beyond the three groups read:** the full HDF5 group tree of one file and the values of the electrode `location`, `description` and `slice` fields (problems 1 and 3).
- **Cluster names (EXT_NAMES: leiden 16 = L5 ET, 8 = L5/6 CT):** a print of the code notebook cell they come from.
- **Layouts of `sumData_StimWM`, `PeakIdx` and `Metabolic_data`:** their header rows, and the paper's group sizes for Fig. 3e.
- **fig4d peak measure:** per-patch time of peak, and a scatter plot of the notebook's peak against `max_Na_current`.
- **Holding potential by connection sign:** the `post_base` of each annotated pair against its sign, and the alternative-channel response for rows 368 and 1309.
- **Supplementary Table 5:** `paper/` does contain the Supplementary Information (supp1.pdf, figure legends), which the claims file says was not read. But the supplementary tables have no extractable text, so I could not read Table 5's per-class pair counts.
- **The notebook's figures:** I did not view them.
