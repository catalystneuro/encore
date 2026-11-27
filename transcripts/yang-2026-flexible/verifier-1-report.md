**A. Outcomes**

The claims file lists 30 claims. The notebook tests 23 and treats 7 as blocked. There is no separate attempt record among my materials, so these counts come from the claims file and the notebook cells.

| Claim | My outcome | Reason |
|---|---|---|
| join-link | reproduced | Cell 11: all 4,430 join rows match a file. Session, subject and full genotype agree for 4,430/4,430. Cell 15: regime membership agrees 100% in all three regimes (0 only-paper, 0 only-here). |
| cohort-label-join | reproduced | Cells 13 and 15: 4430, 4266, 4183, 3988, 4266, all exact. |
| table1-phenotype-spaces | reproduced | Cell 15: 4344/42/11, 4139/20/3, 4422/21/5; overlaps 4054, 4336, 4134, 4049, all exact. The paper's rule gives the paper's feature lists under both denominators. |
| pc1-long-pulse-loadings | reproduced | Cell 17: the top four loadings are current features (|0.303|), then ri and input_resistance (0.263). Holds under readings (a) and (b). |
| fig1b-distance-correlation | reproduced | Cell 19: rho 0.4410, 0.3848, 0.3363, all within tolerance, each p = 0.0099, order holds. The code's pair draw and five seeds agree. |
| fig1-fixed-five-pcs-ordering | reproduced | Cell 21: 0.4335 > 0.3826 > 0.3392. |
| fig1c-knn-jaccard | reproduced | Cell 23: 0.0229, 0.0224, 0.0185, all within tolerance. Chance is 0.00199, 0.00187 and 0.00193, all within 0.0002 of the paper's chance level of ≈0.002. |
| knn-scale-sweep | reproduced | Cell 25: at k = 600, 0.1344, 0.1004, 0.1077, all within tolerance. Values rise at every step for every pair (reading a). |
| split-half-reliability | partially_reproduced | Cell 27: the within-regime value is 0.1071 and the adjusted value 0.1043, both in tolerance. Within exceeds all three same-pool values. But the ramp–brief same-pool value, 0.02219, is just outside [0.018, 0.022], and the long–ramp same-pool n of 2,946 is just below 2,948. 3,256 cells were split, against 3,598 in the paper; random splits were 16 against 358 (problem 1). Chance is 0.002856 against the paper's ≈0.0026, inside tolerance and consistent with the smaller pool. |
| fig2c-eta2-ttype-over-cre | reproduced | Cell 29, reading (a): 0.3269/0.2092, 0.3926/0.2672, 0.1492/0.1095, all six within tolerance. T-type exceeds Cre in every regime. |
| table2-alignment-ttype | partially_reproduced | Cell 31: A_t is 0.0336, 0.0276 and 0.0135 against 0.021, 0.025 and 0.021. All three are out of tolerance (ramp only just), and all have p = 0.0099. Across the five seeds, long-pulse ranges 0.0215–0.0336 and brief-pulse never reaches tolerance (problem 2). |
| ttype-beyond-cre | partially_reproduced | Cell 33: residual A_t is 0.0083, 0.0065 and 0.0103 against 0.011, 0.010 and 0.004, all out of tolerance, all p = 0.0099. Residual eta² is 0.110, 0.120 and 0.040, each above its shuffle null mean of about 0.015, so structure is detectable under both readings. |
| fig2d-knn-type-enrichment | reproduced | Cell 35: 6.608, 3.445, 2.643, all within tolerance, order holds. |
| fig2ab-ttype-structure-within-cre | reproduced | Cell 37: for Sst-IRES-Cre/Ai14 (n = 993), within-Cre A_t is 0.0314 with p = 0.0099, and eta² is 0.225 against a null mean of 0.031. The Sst/Ai167 row also passes. |
| fig3a-type-map-concordance | reproduced | Cell 39: 57 types; rho 0.6588, 0.6085, 0.4552; each p = 0.000999; order holds. |
| shared-map-model-call | reproduced | Cell 41: minimum 0.455, range 0.204. |
| subclass-map-concordance | reproduced | Cell 43, reading (a): 6 subclasses; 0.9357, 0.5786 (long–brief), 0.6214 (ramp–brief). |
| equal-n-centroid-robustness | reproduced | Cell 45: means 0.5529, 0.4573, 0.3226, all within tolerance and all below the full-sample values. Readings (a) and (b) both hold. |
| within-regime-type-map-reliability | reproduced | Cell 47: 0.8621, 0.8522, 0.7990, against a reference of 0.5742. All within tolerance and all above the reference. |
| fig3b-pair-tags | reproduced | Cell 49: 644/796/156 against 639/801/156. |
| pair-tag-threshold-sensitivity | reproduced | Cell 51: selective is below both other categories at every cutoff. This holds only under the criterion's ordering test (problem 5). |
| type-level-exceeds-cell-level | reproduced | Cell 53: the type-map rho exceeds the cell-cell rho in all three pairs. |
| mobility-distribution | reproduced | Cell 55: mean 0.5890, SD 0.1100, n = 4,049. |
| fig4ab-rna-tracks-shared-map | blocked (data_missing) | Needs the NeMO count matrix. Cell 57 got 502 three times, and my own request timed out. The DANDI asset list holds only 4,435 `_icephys.nwb` files (checked). |
| fig4-alternative-panels | blocked (data_missing) | Same as above. Even the curated-gene count (263) needs the matrix's gene list. |
| fig4c-joint-excitability-modules | blocked (data_missing) | Same. |
| fig4c-kv3-strongest | blocked (data_missing) | Same. |
| fig4c-no-module-tracks-rank-range | blocked (data_missing) | Same. |
| pvalb-marker-control | blocked (data_missing) | Same. |
| wgcna-mobility-within-type | blocked (data_missing) | The judged quantities need the counts. The two cell counts (3,906 and 3,902) could have been tested from the join's `transcriptomics_sample_id` and `t_type` columns on the 4,049 triple-shared cells, but were not (problem 3). |

**B. Problems**

1. **[affects a conclusion]** `patchseq._split_half` / `candidate_splits` (cell 27): the random split uses the crc32 claim seed. The criterion and the code (`rng = np.random.default_rng(SEED)` with SEED = 0, fetched from commit 61a5a41) use seed 0. Apart from the seed, `candidate_splits` is identical to the code's.
   - The odd/even (3,112) and sweep-number-interleaved (128) counts match the paper exactly. The whole shortfall is in the random category: 16 here against 358 in the paper.
   - Allen sweep protocols are standardized, so one fixed permutation per sweep count succeeds or fails for whole groups of cells. Seed 0 very likely restores the 342 missing cells.
   - That would move the two values that fall just outside tolerance (ramp–brief same-pool Jaccard, long–ramp same-pool n). A seed-0 variant was needed and is missing.
2. **[affects a conclusion]** `geometry.alignment` and `spearman` (cells 31 and 33): with ordinal ranks of a binary D_mol, the arbitrary order of tied ranks adds an offset that changes with the seed. The offset is shared by the observed value and its null.
   - My synthetic test (60 clustered types, n = 4,000, six seeds) gave an observed A_t of 0.003–0.016, with null means from −0.010 to +0.006 and a null spread of only about 0.001 within each seed.
   - The notebook shows the same pattern. Ramp seed 2000 has residual A_t −0.0018 and still p = 0.0099; long-pulse null mean is 0.0052.
   - So p-values are valid against the shared offset, but the A_t magnitude scatters by roughly ±0.005 between seeds, more than twice the 10% tolerance (±0.002).
   - The tolerance-based verdicts for table2-alignment-ttype and ttype-beyond-cre therefore cannot be met reliably even with the paper's own method. Seed 0 was not run either, and even seed 0 would need the paper's cell order and numpy sort implementation to match.
   - This is a weakness of the claims file's tolerance, not a misreading of the paper. I keep "partially reproduced" as the criterion requires.
3. **[does not affect a conclusion]** wgcna-mobility-within-type: the two cell counts it specifies (3,906 and 3,902) are derivable from the join without the matrix and were not computed. The claim stays blocked either way.
4. **[does not affect a conclusion]** Cells 3 and 15: the IPFX version is never printed, and the Allen-pipeline variant of reading 1 was not run. Moot here, because counts, feature lists and k80 all match exactly.
5. **[does not affect a conclusion]** pair-tag-threshold-sensitivity (cell 51): the fractions move a lot across the grid (stable 0.231–0.569, selective 0.038–0.235). "Reproduced" rests on the claims file's ordering reading, not on the paper's word "stable". That reading is explicitly noted in the checks, so it is not a misreading, but it is a lenient one.
6. **[does not affect a conclusion]** Cell 9: two files (sub-673135474_ses-680563483 and sub-673135516_ses-680897463) have identical voltage traces and features but different t-type and Cre labels in the join. Both are kept in every analysis, like the paper presumably does. The effect on any statistic is negligible.
7. **[does not affect a conclusion]** Cell 37: the join's `cre_line` includes the reporter, so "Sst-IRES-Cre" is split into Ai14 and Ai167 groups, and the notebook judges only the first. Both groups pass. The same 57-line definition reproduces the paper's Cre eta², so it matches the code.
8. **[does not affect a conclusion]** Seeds throughout are crc32 claim seeds, not the criterion's seed 0. Five-seed spreads were shown, and outside the A_t claims they are small against the tolerances.

Helper checks on synthetic inputs:
- The unique-pair index inversion is correct for n = 5, 7 and 100.
- The ordinal Spearman equals scipy's when there are no ties.
- kNN excludes self.
- Self-Jaccard is 1.
- eta² behaves sensibly.

**C. What I could not check**

- **Seed-0 split-half run.** I could not confirm problem 1 without re-running. A cell rerunning `_split_half` with seed 0 (rule counts and same-pool values) would settle it.
- **A_t with the paper's seed.** I could not get the paper's exact A_t. Outputs that would help: A_t at seed 0 with the code's cell order, and observed minus null mean for every seed. The latter is the quantity that is stable across seeds.
- **IPFX version.** Not printed; a `print(ipfx.__version__)` is missing.
- **Transcriptomic claims.** NeMO was unreachable for the author (502) and for me (timeout). Any cache or mirror of `20200513_Mouse_PatchSeq_Release_count.v2.csv`, or at least its gene header, would unblock the 263-gene count.
- **WGCNA cell counts.** The 3,906 and 3,902 counts from the join were not printed.
