**A. Outcomes** (26 claims, taken from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| cohort-prevalence | reproduced | Cell 11: the spreadsheet has 7 carriers, 2 with RP and 5 with VMD; 7/480 = 1.458%, 2/480 = 0.417% and 5/480 = 1.042%, all within tolerance. The denominator of 480 comes from the paper, which the criterion allows. |
| all-caucasian | blocked (data_missing) | There is no race or ancestry field in the spreadsheet headers (cell 13). I queried the archive: neither the dandiset metadata nor the asset metadata has any subject fields. |
| table1-genotypes | reproduced | Cell 15: 7 of 7 patients match on gene, cDNA, protein and zygosity. |
| table1-diagnosis-sex-age | reproduced | Cell 17: diagnoses match 7/7. Sex and age exist only in the "Sex & Age (Y)" label, and with no dates the two age readings can't be told apart (problem 8). |
| inheritance-by-disease | reproduced | Cell 19: the RP variants are all missense, D in IMPG1 and R with 2 variants in IMPG2; every VMD patient is heterozygous D for one variant, missense or nonsense. |
| table1-bcva | reproduced | Cell 21: 14 of 14 eyes match. There is one value per eye, so the two visit readings give the same result. |
| vmd-acuity-preserved | reproduced | Cell 23: under all four readings (better eye worse than 20/40; worse eye worse than 20/40, 20/50 or 20/70), M73 is the only reduced patient. |
| f32-sector-rp-phenotype | reproduced | Cell 26: all 4 features read as visible in both eyes. The reading was made on the published figure panels. |
| m83-rp-phenotype | partially_reproduced | Cell 27: 6 of 9 features visible; 360° bone spicules, pale discs and vessel attenuation not discernible. |
| m75-vmd-phenotype | partially_reproduced | Cell 31: 5 of 6 features visible. FA is not discernible because each eye has one angiogram frame, not early and late phases. The left-eye FAF matches the text's "hyper". |
| m82-vmd-phenotype | partially_reproduced | Cell 32: 2 of 4 visible; FF foveal hypopigmentation and the bilateral FA window defect not discernible. |
| m73-vmd-phenotype | partially_reproduced | Cell 33: 4 of 6 visible. Dot-blot haemorrhages not discernible; right-eye FAF not hyper-autofluorescent (p95 = 1.00). |
| f57-vmd-phenotype | partially_reproduced | Cell 34: 2 of 4 visible. FF hypopigmentation not seen. "More pronounced in the left eye" is contradicted: the OS/OD hypo-autofluorescent area ratio is 0.77. |
| m34-vmd-phenotype | partially_reproduced | Cell 35: 2 of 4 visible. FAF is hypo-autofluorescent, which matches the legend, not the text. Glaucomatous discs and macular hypopigmentation not discernible. |
| rp-superior-field-no-cme | reproduced | Cell 28: all 4 features visible. Only one B-scan per eye is available. |
| m73-f57-similar-lesions | partially_reproduced | Cell 36: the SD-OCT lesions and M73-only cobblestone degeneration hold. The FAF contrast holds in M73's left eye only. The criterion names no partial outcome; this depends on problem 2. |
| m73-eog-normal | blocked (data_missing) | Cell 38 finds no EOG or Arden term in any text. I listed the archive's assets: none of the 13 (xlsx, docx, py, figure images, desktop.ini) is an EOG. |
| other-gene-variants | blocked (data_missing) | Cell 38: none of the named genes appears anywhere. The spreadsheet has IMPG variants only; I confirmed this from the asset list. |
| variant-domains | partially_reproduced | Cell 40: 6 of 7 placements hold under each reading. UniProt fails IMPG1 L740 (IMPG1 has no EGF annotation); InterPro fails IMPG2 R1088 (no second EGF domain). See problem 5. |
| table2-pathogenicity | not_reproduced | Cell 42: no tool's own call matches the paper for IMPG1. SIFT calls L740F deleterious and D423E tolerated; PolyPhen-2 HumVar calls both benign, and HumDiv gives D423E 0.310. CADD matches at most 2 of 7 under any build and version (stop-gains score 36–45 against the paper's 11.2 and 13.4); FATHMM 0 of 5; MutationTaster 0 of 7. The IMPG2 SIFT and PolyPhen values match. |
| asp423glu-novel | not_reproduced | Cell 44: ClinVar VCV 1000102 (6:76002940 G>T, missense, Uncertain significance) is in all four November 2024 releases. On the minus strand that is c.1269C>A, GAC to GAA, p.Asp423Glu. rs758038128 is also colocated. |
| table3-destabilizing | blocked (data_missing: the I-TASSER models are not deposited) | iMutant and MuPRO run from sequence alone and could have tested 2 of the 5 tools (problem 6). |
| impg1-interactions-unchanged | blocked (data_missing) | Needs DynaMut on the undeposited I-TASSER models. The dandiset holds only the Figure 4 renderings. |
| impg2-interactions-changed | blocked (data_missing) | Same as the IMPG1 interaction claim. |
| table4-impg1-physicochemical | partially_reproduced | Cell 49, reading (a): 14 of 18 values match and every stated direction holds. The 4 misses are all in the p.Asp423Glu column, which matches an Asp→Phe change exactly (+32 Da, +7 atoms, pI 4.81, GRAVY −0.474). Reading (b) matches 0 of 18. |
| gnomad-frequencies | reproduced | Cell 51: gnomAD v4.1 joint with 1/(2·AF) gives 6 of 6 within 10% (98,335; 4,096; 3,031; 18,722; 58,997; 332). |

**B. Problems**

1. **Visual readings, cells 24–36** [does not affect a conclusion]. The dataset's figures are the paper's own annotated, published figure panels, not clinical images, and the dataset's spreadsheet is the authors' source file for Table 1. So "reproduced" for the dataset claims means the deposit agrees with the paper; it is not independent evidence. Every phenotype verdict is the notebook author's own reading. I checked the panel crops and arrow positions on the notebook's downsampled outputs (cells 25, 30, 33) and found nothing that contradicts them.
2. **`faf_measures` and the p95 > 1.1 threshold, cells 29, 30, 33, 36** [affects a conclusion]. The "bright focus" threshold is the author's own; neither the paper nor the claims file gives it. It decides that M73's right-eye FAF is not hyper-autofluorescent (p95 = 1.000), and with it the FAF condition of m73-f57-similar-lesions. Also, the 80–140 px reference ring includes the yellow arrow overlays (visible in cell 30 for M75 OS, M73 OD/OS and M34 OD/OS), the optic disc and vessels, which bias the surround median. No sensitivity check and no arrow masking were done. In the cell 30 crop, M73 OD shows a small bright central speck.
3. **`impg.dbnsfp`, cell 42** [does not affect a conclusion]. `first()` takes the first element of dbNSFP's per-transcript lists, not the MANE transcript. dbNSFP SIFT for L740F is 0.545 against VEP's 0.02, so the FATHMM and MutationTaster values may come from another transcript. MutationTaster2021 and the FATHMM web server were not run, so the paper's 0–100 MutationTaster scale is matched by no reading tried. The claims file asked for every output each tool gives. IMPG1 fails on VEP and CADD regardless.
4. **Table 2 inconsistencies, cell 42** [does not affect a conclusion]. The paper's two IMPG1 SIFT values are exactly swapped relative to VEP; exchanging them puts both within tolerance. The paper prints rs15048636 where VEP gives rs150486366, and rs267606975 where VEP and the Word document give rs267606875. These are reported here and not corrected.
5. **`domains("InterPro")`, cell 40** [affects a conclusion]. The InterPro reading keeps only integrated InterPro entries (`db == "interpro"`). The Pfam and SMART annotations, which the criterion names, were fetched but never used or shown. A member-database reading could place R1088 in a second EGF domain and L740 near or in an EGF domain, which would turn this into reproduced.
6. **Blocked claims, cells 45–46** [does not affect a conclusion]. The notebook's reason, "not runnable", is not one of the allowed reasons. iMutant and MuPRO need only the sequence, so the sign test and the ranking could have been run on 2 of the 5 tools. The deposited Word document also contradicts Table 3: p.Asp423Glu SDM is +0.58 (stabilizing) and mCSM is −0.58 against the paper's −0.653; MuPRO L249F is −1.2666, a duplicate of the C1019Y value, against −1.525; iMutant R131C is −1.22 against −1.13; there are no iMutant values for IMPG1. The notebook shows these but doesn't feed them into any conclusion.
7. **ProtParam, cell 49 and `impg.protparam`** [does not affect a conclusion]. I tested the mass and atom tables on ACDEFGHIKLMNPQRSTVWY: 2395.736 Da and C107H159N29O30S2 (327 atoms), which match ExPASy. Asp→Glu gives +14.03 Da and +3 atoms. The pI comes from Biopython, not ExPASy's own code; the small difference this could cause is not checked.
8. **Cell 17** [does not affect a conclusion]. `sex_paper` and `age_paper` are parsed from the same identifier string as `sex_data` and `age_data`, so those checks are true by construction.
9. **Cell 44** [does not affect a conclusion]. The ClinVar record's HGVS, condition (CLNDN) and first-submission date are not printed, so the "first association with VMD" half of the claim isn't addressed.
10. **Cell 3** [does not affect a conclusion]. The dandiset metadata says 1 subject and no species, but the files describe 7 patients.

**C. What I could not check**

- **Full-resolution panels.** I saw only the notebook's downsampled images, so I couldn't judge fine features myself (spicules, dot-blot haemorrhages, the nevus, the FA window defects). Full-resolution crops at each arrow for every feature would have let me.
- **Outside services.** I didn't query VEP, CADD, dbNSFP, gnomAD, ClinVar, UniSave or InterPro; I only queried the DANDI API. Printing the InterPro member-database rows (Pfam, SMART, PROSITE), the dbNSFP transcript lists alongside the MANE index, and ClinVar's CLNHGVS, CLNDN and date would have closed problems 3, 5 and 9.
- **FAF measures.** I couldn't run `faf_measures` (no numpy in this environment). A version with the arrow pixels masked, and a table of verdicts across p95 thresholds, would show whether problem 2 changes the outcome.
- **Word document images.** The 2 embedded images were not shown.
