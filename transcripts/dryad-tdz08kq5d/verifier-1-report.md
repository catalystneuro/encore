**Verifier report, round 1: doi:10.1093/evlett/qrad056, Dryad tdz08kq5d v263142**

The claims file has 32 claims. My outcomes: 25 reproduced, 4 partially reproduced, 1 not reproduced and 2 blocked. The notebook marks 30 as tested and 2 as blocked. Dryad's API lists two files for this version, `README.md` and `temperature_phage_data_allfigures2.xlsx`, which matches the notebook's SHA-256 check in cell 3.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-temperature-density | reproduced | Cell 19, days 2–12: temperature F(1,36)=73.989, p=3e-10, matching Table S1a in every printed SS and F. Mean OD600 is 0.563 at 35 °C and 0.255 at 25 °C (cell 20). |
| fig1b-phage-reduces-density | reproduced | Phage F=48.800, p=3e-8. With phage, mean OD600 is lower at both temperatures: 0.388→0.123 at 25 °C and 0.680→0.445 at 35 °C (cell 22). |
| fig1b-phage-effect-diminishes | reproduced | Three-way interaction F(5,180)=3.870, p=0.0024. The −P minus +P difference on the last day is below its earlier maximum at both temperatures: 0.322 vs 0.436 at 25 °C, −0.008 vs 0.505 at 35 °C (cell 24). The criterion is weak at 25 °C; see B6. |
| auc-phage-reduction-by-temperature | reproduced | All three readings fall within tolerance with the 25 °C reduction larger and p<0.05 (cell 26). Reading (b) gives the paper's numbers exactly: 66.8% and 37.18%, F 88.77 and 15.66. The df is (1,18), not the paper's (1,19), which the claims file allows. |
| fig1c-phage-density-temperature | reproduced | Temperature F(1,18)=32.75, time F(2,36)=86.96, both matching Table S1b. Density is higher at 25 °C (8.76 vs 7.38). At each temperature it peaks on day 4, well above the 10^4 PFU/ml inoculum, and then declines (cell 28). |
| fig1d-mucoid-lost-with-phage | reproduced | No 35 °C +P replicate has mucoid colonies, and exactly one 25 °C +P replicate does (replicate 2). The other three are 100% SCV. Reading (a1) gives 0.244%, within 0.24 ± 0.024 (cell 30). |
| fig1d-phage-raises-scv-frequency | partially_reproduced | The phage effect matches Table S2 (F(1,12)=7.016, p=0.021) and SCV share rises from 64.8% to 99.9%. 35 °C −P mucoid is 55.0% (mean reading). But 25 °C −P mucoid is 15.3% (mean) or 15.6% (pooled), outside 20 ± 2 under both readings (cell 32), so the criterion is not met. |
| fig2a-phage-exposed-more-resistant | reproduced | Unit means: phage F(1,15)=280.75 sequential (exactly Table S3a) and 30.50 type II, both p<1e-4. Mean R with phage exceeds R without at both temperatures (cell 36). |
| fig2a-temperature-resistance | reproduced | Unit means: p=0.023 (i) and 0.009 (ii). Mean R is higher at 35 °C on units (0.790 vs 0.731) and on clones (cell 38). See B9. |
| fig2a-no-temperature-phage-interaction | reproduced | p=0.168 (i) and 0.489 (ii). The clone variants are also not significant (cell 40). |
| fig2a-scv-more-resistant | reproduced | Colony type F≈443–445 and colony type × phage F=86.06, all p<1e-6 under both readings. SCVs have higher R than mucoid clones without phage (0.968 vs 0.273) and with phage (0.999 vs 0.906) (cell 42). |
| fig2a-mucoid-25p-replicate-resistant | reproduced | Reading (a): F(1,18)=174.50, p=1e-10, the paper's statistic exactly. Reading (b): F(1,38)=88.1, p=2e-11. These clones have higher R (0.906 vs 0.246/0.273) (cell 44). |
| fig2b-scv-higher-growth-rate | reproduced | Colony type p<1e-4 with SCVs higher; phage × type p=0.109; temperature × type p=0.967 (i) and 0.559 (ii) (cell 46). This is tested on the deposited fitted μ, whose sequential F matches Table S3b exactly. The logistic-vs-AIC fit readings cannot be done (B2). |
| fig2c-scv-lower-carrying-capacity | reproduced | Colony type F=87.97 (i) and 79.96 (ii), with SCVs lower (1.13 vs 1.36). Temperature × type p=0.093 / 0.273 and phage × type p=0.109 (cell 48). Same caveat as fig2b. |
| fig2d-scv-twitching-no-exposure-effect | reproduced | Temperature, phage and T×P have p≥0.05 under both sums of squares (smallest 0.058, type II T×P), under the by-name variant and on SCVs alone (cell 50). The deposited values do not reproduce Table S3d (B1). |
| fig2d-mucoid-25p-reduced-twitching | reproduced | Reading (a): F(1,6)=27.22, p=0.002, the paper's statistic exactly. Reading (b): F=14.66, p=0.009. Mean diameter is 6.24 mm against 9.56 and 8.56 (cell 52). |
| fig2e-mucoid-biofilm-increased | partially_reproduced | Colony type F=42.37 with mucoid higher, and the ancestor (0.489) is below the mucoid IQR. But the ancestor lies below the SCV minimum (0.576): all 16 SCVs are above it and their mean is 47% higher. Both readings agree that "SCVs within ancestral level" fails (cell 54). |
| fig2e-biofilm-no-exposure-effect | reproduced | Temperature, phage and T×P have p≥0.19 under (i) and p≥0.19 under (ii). Sequential F values match Table S3e (cell 56). |
| fig2f-phage-exposure-reduces-virulence | reproduced | Phage p=0.0002 (i) and 0.017 (ii), with +P incidence 0 vs 0.18. Temperature p=0.173 (i) and 0.508 (ii) (cell 58). |
| fig2f-scv-avirulent | reproduced | All 16 SCV clones have pooled incidence 0. Colony type F=33.4 (i) and 34.1 (ii), p<1e-5 (cell 60). |
| fig2f-mucoid-25p-avirulent | reproduced | Interaction F=9.992, p=0.0047. The 25 °C +P mucoid mean is 0, below 0.319, 0.403 and the ancestor's 0.722, and all four clones are 0 (cell 62). |
| sequencing-mutation-count | not_reproduced | Protein-changing variants per clone: 282/28 = 10.07, outside 8.5 ± 0.85. Variant counts give 2.36 and 16.96, and no reading gives 8.5. The morphology ANOVA cannot be formed from the group-aggregated table; group means are mucoid 10.17 and SCV 10.0 (cell 64). |
| table1-phcs-in-scvs | reproduced | SCV clones with phcS: 13 if variants sit in different clones, 12 if they overlap; both within 13 ± 1.3. Mucoid clones: 0 (cell 66). |
| table1-pild-in-25p-mucoid | reproduced | One pilD variant, carried by 2 clones of 25 °C +P mucoid and by no other group (cell 68). |
| table1-t2ss-in-35p-scv | blocked (metadata_insufficient) | gspE (2 clones) and gspF (1) occur only in 35 °C +P SCV, matching Table 1 per gene. Whether that makes 3 clones or 2 cannot be read from the group-aggregated table, and the tolerance is 0 (cell 70). |
| tables6-pil-mutants-resistant | blocked (data_missing) | Dryad lists only the README and the workbook, and no sheet, column or cell names pilB, pilM, OE1-1 or QL-Rs1115 (cell 72). Nothing is testable. |
| figs3-adsorption | reproduced | ANOVA F(12,26)=19.75. In Tukey tests both pilD mutants are below the ancestor (p<0.001), and no phcS, gspE or gspF mutant differs (all p_adj≥0.74) (cell 74). |
| rnaseq-differential-expression-count | reproduced | The deposited DESeq2 table gives 1477, 707 up and 770 down, exactly (cell 76). The pipeline from reads was not re-run. |
| rnaseq-kegg-enrichment | blocked (methods_underspecified) | Exactly the five named pathways have uncorrected p<0.05, but none has FDR<0.05 (minimum 0.196). The readings differ, so the criterion makes this blocked (cell 78; see B5). |
| rnaseq-mutated-genes-expression | partially_reproduced | phcR is up (log2FC 1.83) and pilD down (−1.35), and the other pilus and fimbrial genes are down. phcS is up but only by log2FC 0.41, below the threshold. Only 3 of the 11 listed Figure 4B genes meet both thresholds (at most 5 of 13) against the claimed 7 (cell 80). |
| rnaseq-defense-systems | reproduced | JetC is down (−4.21) and the MTase, REase, SMODS and effector genes are up (+2.30 to +2.64), all with padj<1e-25 (cell 82). |
| rnaseq-virulence-genes-down | partially_reproduced | rcpA, tadC and 6 hrp/hrc genes are down with |log2FC|>2. gspG, which the text names as downregulated, is up (+2.04, padj 0.0015), so "none upregulated" fails (cell 84). |

The paper states no chance levels, so there were none to compare.

### B. Problems

1. **[does not affect a conclusion]** The twitching sheet (`twitching`, cells 10, 11 and 50) is not the data behind Table S3d. Its total SS is 72.28, against 82.08 summed from S3d, and no relabelling changes a total SS. Temperature SS is 2.48 vs 3.857 and residual 28.32 vs 35.78, though P×C 27.040 and T×C 0.081 match exactly. The four 35_1 rows carry 35_0 strain names and are the likely mismatch. Separately, `type_design` (second 25_0 block = SCV) is the author's own inference and is not in the claims file. The exact F(1,6)=27.22 supports it. The notebook prints the S3d comparison but never says it fails. Outcomes hold under every labelling.
2. **[does not affect a conclusion]** fig2b/fig2c (cells 45–48): the criterion defines μ and A as a logistic grofit fit, with the AIC best-of-four as a variant. Neither can be computed, because the growth curves are not deposited. The exact match to S3b/S3c shows these are the paper's values, but the fit step itself is untested.
3. **[affects a conclusion, unverified]** In `clone_table` and `twitching`, the ancestor value is `anc.iloc[0]`, taken without checking how many "anc" rows exist. If the ancestor has several replicate rows, the dashed-line value is one replicate, not their mean. fig2e-mucoid-biofilm-increased turns on the ancestor (0.489) against the SCV minimum (0.576). The values 9.383 (the code's 9.38) and 0.7222 (13/18) suggest single aggregated rows, but no output shows it.
4. **[does not affect a conclusion]** The claims-file header gives the ancestor's twitching diameter as "9.38 cm". The data column is `twitching(mm)`, and a 9.38 cm colony would be implausible on a standard plate. This looks like a unit misreading in the claims file.
5. **[affects a conclusion]** In rnaseq-kegg-enrichment the claims file treats "corrected or not" as underspecified. The deposited KOBAS table shows that the five pathways the paper names are exactly those with uncorrected p<0.05, and no pathway passes FDR. That points to the paper using uncorrected p, but the criterion as written forces "blocked".
6. **[does not affect a conclusion]** The fig1b-phage-effect-diminishes criterion only compares the last day with the earlier maximum. At 25 °C the gap falls to 0.049 on day 8 and then rises to 0.322 on day 12 (cell 24), which is not a gradual decline. The claims file's operationalisation is looser than the paper's statement.
7. **[does not affect a conclusion]** sequencing-mutation-count (cell 64): the per-clone mean is exact from the aggregated table, since the paper says four clones per group, one per replicate. Every non-missing EFFECT row is protein-changing, so "nonsynonymous" is not ambiguous here. The mean misses under all three readings. The ANOVA half is untestable and the notebook says so.
8. **[does not affect a conclusion]** rnaseq-defense-systems (cell 82): the loci come from the authors' own Figure 4C labels, and "Effector_1TM_DUF1043" stands in for the Gros effector. The criterion asks for loci identified from the RS-N annotation, which was not done independently.
9. **[does not affect a conclusion]** fig2a-temperature-resistance (cell 38): the main effect comes from colony-type composition, since 35 °C +P is all SCV. Within mucoid clones R is higher at 25 °C (0.378 vs 0.295), and the sequential clone variant gives p=0.071.
10. **[does not affect a conclusion]** `rm_anova` reproduces Tables S1a and S1b to every printed digit. On synthetic balanced data its within-stratum residual (32.49) equals that of an OLS with a subject factor. `parse_strain`, `unit_means` (22 units, residual df 15) and the column mapping in `clone_table` behave as described.

### C. What I could not check

- **Ancestor rows.** I could not see how many "anc" rows each Figure 2 sheet holds, or their raw values. Printing the right-hand ancestor block of each sheet would settle B3.
- **README.** Its content is loaded in cell 1 but never printed. It might say what the twitching 35_1 rows are, or what units and replicates apply. Printing it would help B1 and B3.
- **Twitching sheet.** The raw columns 4–6 are not shown in full, and no labelling that reproduces S3d was searched for. A cell that tries to match S3d's SS would show which rows differ.
- **Figure 4B gene list.** I could not see the two missing genes (numbers 8 and 9). The list holds 11 genes, and nothing elsewhere in the workbook gives the 13-gene set.
- **Clone identity of the variants.** I could not check which clones carry which variants (t2ss, the per-clone ANOVA). PRJNA1028400 has 28 BioSamples and 14 assemblies but no SRA runs (cell 16). Testing per clone would need per-clone variant calls, which the dataset does not hold.
