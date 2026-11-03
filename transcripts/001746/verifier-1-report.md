**A. Outcomes** (33 claims in the claims file: 24 tested on this dandiset or blocked here, 9 with data elsewhere)

| Claim | My outcome | Reason |
|---|---|---|
| patchseq-cell-table-link | reproduced | All 462 rows find a file. Cell IDs agree 462/462 and subjects 461/462. Within 10% of the xlsx: half-width 89.5%, amplitude 90.2%, rate 98.9% (cell 12). The one subject mismatch is row 235 (n172, Mfa180730), which repeats row 110's file name; the one file no row names (s172, Mfa180730) is almost certainly the file it meant (cell 11). By the letter "labels disagree" fails on that row. |
| morph-table-link | reproduced | 166/166 rows match a file; clusters agree 163/165 = 98.8% (cell 56). |
| patchseq-sample | partially_reproduced | 462 neurons (457 distinct recordings), within tolerance. 10 subjects against 12 ± 1.2 fails; all male (cell 15). |
| patchseq-mapping | partially_reproduced | 278/307, 248/273, 17/18 and 17/17 are within tolerance. Inhibitory 30 against 34 ± 3.4 is not (cell 17). The 30% mapping-rate filter removes nothing (minimum 0.40). |
| fig2a-subclass-counts | partially_reproduced | 5 of the 6 judged counts are within tolerance (L6 IT and L6b judged together, 14/14). L5 IT FEZF2 is 125 against 143 ± 14.3 (cell 19). |
| ven-map-et-ct | reproduced | 14 VENs in DSG2 and 15 in COL24A1, none in other clusters (cell 21). |
| fig6f-ven-subtype-mapping | partially_reproduced | No VEN-L is in COL24A1 and no VEN-S in DSG2, and VEN-S is 10 (11 ± 1.1). VEN-L is 12 against 10 ± 1, outside tolerance (cell 23). |
| fig2d-l23it-small-tau | reproduced (marginal) | Methods tau median is lowest (32.7 ms). Against the pooled five, p = 0.0106: q = 0.023 in the 20-feature family, and between 0.0106 and 0.0514 in the deciding 39-feature family. The upper end is reached only if none of the 19 features not computed has p < 0.0106, while 7 of the 20 computed ones do. First-sweep tau gives q ≤ 0.005 (cell 27). |
| fig2f-l23it-narrow-ap | partially_reproduced | Significantly narrower than the pooled five (q ≤ 0.008), but the median ranks 2nd (IT RORB 1.92 ms against 2.00), and under reading (b) it is not significant against IT RORB, L5 ET or L6 PC (cell 29). The criterion's partial clause requires the lowest median, so this is a judgement the claims file anticipates. |
| supp11-rm-itrorb-l6pc | partially_reproduced | L6 PC is higher than the pooled five (q ≤ 0.006). IT RORB against the pooled five has q = 0.065 in the 20-feature family (between 0.023 and 0.147 in the 39-feature family), and both groups fail reading (b) (cell 31). |
| supp11-l5it-threshold-latency | reproduced | Reading (a): threshold −38.5 against −41.2 mV (q ≤ 0.045) and latency 204 against 149 ms (q ≤ 0.0012) (cell 33). |
| supp11-ven-broad-ap | not_reproduced | The highest median is L5 IT FEZF2 (2.92 ms) against VEN 2.90; VEN against the pooled five p = 0.17 (cell 35). |
| supp11-l5et-deep-sag | blocked (methods_underspecified) | Sag ratio is highest in L5 ET and significant. Sag value is lowest in L5 ET (19.6 mV) and significant the other way, so the measure readings disagree as the criterion foresees (cell 37). |
| ven-firing-rate-variability | not_reproduced | Firing rate is not lower under (a) (p = 0.09), (b) (ns against L5 IT FEZF2) or (c) (p = 0.38). No variability measure is significant under any reading (cell 39). |
| l5et-vs-l5it-sag-rm-rate | partially_reproduced | Firing rate higher (q ≤ 0.033) and sag ratio deeper (q ≤ 6e-5). Input resistance is lower, with q = 0.026 in the 20-feature family but up to 0.054 in the 39-feature family. Sag value goes the opposite way (cell 41). |
| fig3e-phase-peak-index | blocked (methods_underspecified) | VEN median is lowest only under the first-AP reading, not under the median-over-APs reading; Dunn separates VENs from only 2 of 5 groups (cell 43). The automatic index is also flawed (problem 1). The code's hand-read values would reproduce it (all Dunn p ≤ 0.001, cell 44), which is a deviation from the automatic reading. |
| fig3d-saddle-phase-plane | blocked (methods_underspecified) | Takes the outcome of fig3e. |
| fig4ac-ven-broader-smaller-ap | blocked (data_missing) | The archive holds 462 files, all rows of the Patch-seq table, with only 68 VENs and 138 L5 PCs. The Patch-seq variant is not significant (cell 47). |
| fig4i-peak-index-ais-distance-real | blocked (I'd give methods_underspecified, inherited from fig3e) | The notebook's reason, metadata_insufficient, is weak: the criterion already takes the 62 as the Patch-seq cells with a reconstructed axon origin, and morphFeatMatrix.xlsx has axonDist by cell ID for 166 matched cells. Not run (problem 4). |
| ext9cd-ven-subtypes-ap | blocked (data_missing) | The dataset has 18 VEN_Long and about 12 VEN_Short VENs, far fewer than 85 and 41. Variant: no difference (cell 51). |
| supp8-ven-subtypes-similar-features | blocked (data_missing) | As above. Part of the subtype-labelled VENs lack a transcriptomic type and may be non-RNA recordings; this was not separated (problem 5). |
| supp9-venl-more-distinct-from-ct | reproduced (weak) | 20-feature family: 1 feature against 0. 39-feature family: at least 4 against at least 0. Median q 0.46 against 0.83 (cell 54). The 1-against-0 margin is fragile. |
| morph-more-distinct-than-ephys | reproduced | Count 445 against 106, fraction 0.376 against 0.252 against the Methods' 20 features, the family this claim's criterion names (cell 58). The morphology family is 57 columns, not 40 (problem 7). |
| fig7c-tau-rna-distance | blocked (data elsewhere) | The archive's metadata lists only current-clamp series, so the RNA side is not on this dandiset. The notebook has no cell for this claim and no evidence for "too_large" (problem 6). |
| 9 claims with data elsewhere (scrna-classes, ext1d, fig3c, fig4d, model, fig4j, fig5, fig6 morphology/markers, fig8) | blocked (other) | This dandiset holds only current-clamp series (archive metadata). DANDI:001750, 001751 and 001752 exist separately. |

**B. Problems**

1. [affects a conclusion] `aic.phase_index`: when no AIS peak or shoulder is found, it returns 0. On synthetic APs a monophasic AP (no AIS phase) scores 0.0, while a clear biphasic AP scores 0.27 and a shoulder AP 0.42. So the APs least like a saddle get the index the paper assigns to the most saddle-like (lower = more saddle). The Methods' "point with the lowest derivative value" does not support 0. This rule produces the 0.0 medians of L2/3 IT and IT RORB under the median reading (cell 43), which is why that reading fails. It invalidates the automatic index for fig3e, fig3d and fig4i. Its agreement with the hand-read values is poor (Spearman 0.55 first AP, 0.09 median; cell 44).
2. [affects a conclusion] Cells 25–41, `compare`/`upper39`: the deciding 39-feature family cannot be computed for 19 features, so fig2d, supp11-rm (IT RORB) and l5et-vs-l5it (Rm) end "undecided". I confirmed `upper39` is a valid, attainable bound (brute force over random unknown p-values; `aic.bh` matches scipy). The xlsx's own values for the 19 features would have given exact q values.
3. [does not affect a conclusion] Cell 8 and cell 54: five pairs of byte-identical recordings carry different cell IDs, subjects and labels (for example s640 VEN and n5 PC_L5). n175 (cluster 8 PC, the same recording as B289, L5 ET) stays in the L5/6 CT group of supp9 (n = 11; the legend gives 10). The data-integrity question is noted but not carried into the link claim.
4. [affects a conclusion] Cell 49 (fig4i): blocked on the mat file's lack of IDs, although the criterion names a reading the dataset plus morphFeatMatrix axonDist allows. The regression was never run.
5. [affects a conclusion, possibly] Device: 253 files are labelled Axon, and the Methods put non-RNA recordings on MultiClamp/pClamp and Patch-seq on HEKA. Device is never crossed with typed/untyped status or with group. That leaves open (a) whether part of the dataset is the non-RNA recordings relevant to supp8/ext9cd/fig4ac, and (b) whether fs-dependent measures (5-sample smoothing in the phase index, half-width resolution) are confounded with group through the recording era (L2/3 IT cells come mostly from 2022 subjects, cell 25).
6. [does not affect a conclusion] fig7c: no notebook cell; the "too_large" reason is unstated and unsupported.
7. [does not affect a conclusion] Cell 58: the morphology family uses all 57 numeric columns, not the Methods' 40, an unstated choice. The fraction reading is barely affected.
8. [does not affect a conclusion] `cell_features`: sag and sag value are taken at the largest hyperpolarizing step, which is −80 to −120 pA in 28 grouped cells (cell 37), so step size is mixed into sag value and sag ratio. Plausibly harmless for the L5 ET direction, since its low Rm alone gives a small sag value.
9. [does not affect a conclusion] `tau_methods` averages every hyperpolarizing sweep's fit with no quality filter; outliers like 217 ms (cell 27) enter the mean. The median ratio to the code's tau is 1.26.
10. [does not affect a conclusion] Cells 23 and 51: table inconsistencies left unremarked. Some VEN-typed cells carry PC subtypes (PC_L5, L23_PC), and 5 VEN_Short labels sit on non-VEN rows.

**C. Not checked**

- Whether the NWB files hold cell-type annotations outside the fields `read_nwb` reads (icephys tables, lab_meta_data). The archive's description says the recordings are annotated with transcriptomic types; its asset metadata has none. A dump of each file's full HDF5 key tree would settle it.
- The GitHub tables (cluster lists, CSV/xlsx contents) were not available to me, so the group definitions are taken from the claims file.
- Outputs that would have helped:
  - a device × (typed/untyped) × group crosstab;
  - per group, the fraction of APs that fall into the phase index's "no shoulder → 0" branch;
  - BH q values over the 39 features using the xlsx values for the 19 uncomputed ones;
  - an axonDist (morphFeatMatrix) against phase-index regression;
  - per-cell `tau_n_fits` and the spread of tau across sweeps.
