**Verifier report, round 1: Liu et al. 2026, DANDI:001752 (0.260825.0222)**

I had no attempt record. The claim list comes from the claims file and from the two notebooks in the directory, `reproduce_liu_2026.ipynb` (the "main" notebook below) and `elsewhere_liu_2026.ipynb`. I checked the helper modules `psc.py` and `aic_tables.py`. I ran `psc.detect` on synthetic traces and queried the DANDI API. I did not download the dataset and did not re-run either notebook.

### A. Outcomes

**The dandiset's claims (main notebook)**

| claim | outcome | reason |
|---|---|---|
| psc-file-labels-link | partially_reproduced | All 85 table rows name a dandiset file, but several other parts fail (cells 12–14). File `fwphyw` is named by no row, and `1s3ysck` is named by two different cells (11a PC and 11b VEN), which the "counted twice" exception does not cover. mEPSC has 7 VENs where the legend has 8, and the sheet's cell type matches the table's for 0 of 15 mEPSC cells. The frequency correlation passes only for mIPSC (ρ 0.73); it fails for mEPSC (ρ 0.51, p 0.054), sEPSC (ρ 0.34) and sIPSC (ρ 0.19). |
| fig5b-sepsc-frequency | blocked (methods_underspecified) | At the 5 pA threshold, VENs are lower than PCs: 2.06 against 9.36 Hz, p 0.029 (11 PC entries), or p 0.027 (10 distinct cells) (cell 19). At the RMS threshold, VENs are higher: p 0.09 or 0.15. The readings disagree, so the criterion says blocked. Problems 1 and 2 weaken both readings. |
| fig5b-sipsc-frequency | not_reproduced | The VEN median is above the PC median under every reading and every 11a/11b assignment (cell 21). At 5 pA: 19.9 against 15.4 Hz, p 0.34–0.40. At RMS: p 0.0006–0.07, VENs higher. |
| fig5b-mepsc-frequency | not_reproduced | With the dataset's labels, VENs are higher at 5 pA (0.92 against 0.69 Hz, p 0.61) and at RMS (p 0.15) (cell 23). With the sheet's labels (the variant), the order flips but stays non-significant (p 0.61). |
| fig5b-mipsc-frequency | blocked (methods_underspecified) | At 5 pA, VENs are lower: 1.23 against 2.35 Hz, p 0.0074. At RMS the difference is not significant (p 0.235). The readings disagree (cell 25). The 3×RMS variant gives p 0.0005. |
| fig5c-sepsc-amplitude | reproduced (fragile) | The deciding reading (5 pA, whole recording, 11 PC entries) gives 8.20 against 8.51 pA, p 0.231 (cell 27). But the RMS (p 0.015), 30 s (p 0.035) and 3×RMS (p 0.019) variants are all significant. The amplitudes measured here do not track the sheet's (ρ 0.22). |
| fig5c-sipsc-amplitude | reproduced | Reading A gives p 0.082 (cell 29); readings B and C give p 0.072 and 0.094. |
| fig5c-mepsc-amplitude | reproduced | p 0.61 under both labellings (cell 31). |
| fig5c-mipsc-amplitude | reproduced | p 0.46 (cell 33). |

**Claims whose data are elsewhere (`elsewhere_liu_2026.ipynb`)**

| claim | outcome | reason |
|---|---|---|
| ven-map-et-ct | reproduced | The table the claim names gives 15 L5 ET and 14 L5/6 CT, inside the ±1.4/1.5 tolerance; it has 30 VENs, one of them in cluster 14. `results_Ext` gives exactly 14 and 15 (cell 4). |
| patchseq-mapping | reproduced | 273 excitatory neurons in 17 types, both inside tolerance. Inhibitory, reading (b): 33 neurons in 17 types. Reading (a) gives 19 types, outside tolerance, but it mixes excitatory cluster IDs into the count (cell 6). |
| fig3e-phase-peak-index | reproduced | The VEN median (0.117) is the lowest. Dunn's test with Bonferroni correction separates VENs from every PC type at p ≤ 0.001 (cell 8). This uses the code's per-cell indices, not a recomputation. |
| fig4j-eepsp-amplitude | reproduced | VENs are higher, and the cell-type effect is p 0.00339, matching the paper's 0.0034 (cell 10). |
| fig4d-sodium-current | reproduced | VEN median 23.0 against PC 34.6 pA, p 0.0023 (cell 16). Reading (b) is reading (a) divided by one constant patch area (Problem 13). |
| fig5-connectivity-total | partially_reproduced | Tested pairs: 1416 against 1292 (inside the ±129 tolerance). Connections: 26 against 31 (outside ±3.1) (cell 12). |
| fig5-connectivity-by-type | partially_reproduced | PC→PC is 18 (expected 24 ± 2.4), and VEN→PC is 1 where the claim requires exactly 0. The other six counts match. Tested-pair counts differ widely, e.g. 749 against 503 (cell 13). |
| fig8a-metabolite-gradient | not_reproduced | AIC against V1 gives 175–194, outside 228 ± 23 under every reading. AIC against PrC (84–98) is inside 108 ± 11 only under log10 with reading (a) (cell 18). |
| fig8de-glycolytic-bias | partially_reproduced | Citrate is higher (p 0.0005) and glutamate higher (p 0.0001). 2-ketobutyrate is lower but not significantly (p 0.18 raw, 0.086 log10) (cell 20). |
| fig2d-f-l23-it-tau-width | not_reproduced | L2/3 IT HPCAL1 has the lowest median tau, but no pairwise FDR-adjusted p is below 0.05. The lowest median half-width belongs to IT RORB (1.92 against 2.10 ms). Both readings fail (cell 23). |
| ven-subtypes-similar-physiology | partially_reproduced | Neither feature is significant (FDR 0.084 and 0.10), but the test has only 18 VEN-L and 16 VEN-S, against the 85 and 41 the criterion names. The raw half-width p is 0.042 (cell 25). |

### B. Problems

1. **[affects a conclusion] The RMS threshold, reading (b), counts noise.** (`psc.detect` with `threshold=None`; cell 9.) On synthetic white noise, a threshold of 1× the noise SD gives about 58 Hz whatever the SD. With real 1 Hz events added, it gives 57 Hz. In the data, reading (b) gives 17–43 Hz for mEPSC, where the sheet has 0.4–3 Hz. Reading (b) comes from the claims file, and I think it misreads the paper. The Methods say "the maximus root mean squared noise level (5 pA)", which gives the threshold's value (5 pA), not a per-recording threshold. That misreading is the only reason sEPSC and mIPSC frequency come out blocked. I report this rather than correct it.
2. **[affects a conclusion] At 5 pA, the threshold is at or below the noise in many spontaneous-current files, and nothing filters them or excludes noisy files.** (Cells 5, 14, 19.)
   - sIPSC: median noise is 6.1 pA, and 11 of 15 files exceed 5 pA.
   - sEPSC, subject Mfa201126: PC noise median 3.99 pA against 2.10 for VENs.
   - Synthetic pure noise at SD 2 pA gives 11 Hz of false events at 5 pA; at SD 4 pA it gives 51 Hz.
   - This fits the frequencies here being 3.2× (sEPSC) and 5.7× (sIPSC) the sheet's, with ρ only 0.34 and 0.19.
   - So the sEPSC 5 pA result (VEN < PC) is confounded by the PCs' higher noise, and the sIPSC frequencies and amplitudes largely measure noise.
3. **[does not affect a conclusion] mEPSC labels.** The sheet's own frequencies with the sheet's labels give VEN 1.40 against PC 1.97 Hz, p 0.032 (my calculation from the values printed in cell 23). The paper's result therefore follows from its labelling, and the dataset's labels reverse it. The notebook never runs this comparison.
4. **[does not affect a conclusion] Rank-sum test method.** The markdown in cell 16 says `mannwhitneyu` is exact as MATLAB's `ranksum` is. For 8 VENs against 11 PCs, MATLAB's default is exact while scipy's "auto" uses the asymptotic test. On a synthetic 8-against-11 case this gives p 0.0091 against 0.0103. No outcome sits near the 0.05 boundary.
5. **[does not affect a conclusion] Recording-quality conditions not applied.** The notebook never checks stability (shift beyond ±4 s.d.), the 5 min minimum or the 200-event minimum. 44 files are under 300 s and 18 have fewer than 200 events (cells 5, 9). The group sizes match the legend, so the paper evidently kept these files too.
6. **[does not affect a conclusion]** In sIPSC reading A, which decides the amplitude claim, one file (`1s3ysck`) sits in both groups. Readings B and C agree with A.
7. **[does not affect a conclusion]** Events above 500 pA are cut as artefacts, which is the author's own choice; it removes 19 events.
8. **[does not affect a conclusion]** The link claim's correlation step depends on the detector, so a low ρ may reflect detection, not the labels. That outcome is partial anyway because of the mEPSC labels.
9. **[affects a conclusion] fig2d-f feature extraction is unchecked.** (`aic_tables.first_ap`; cells 22–23.)
   - There are obvious extraction failures: threshold up to +53 mV, amplitude as low as 0.67 mV, half-width as low as 0.08 ms.
   - Group sizes differ from the legend: IT RORB 21/17, L5 IT 125/119, VEN 29/22, L5 ET 18/16, L6 PC 14/13 (here/legend).
   - The half-width verdict rests on 1.92 against 2.10 ms.
10. **[affects a conclusion] fig8a used a different table.** It used the code's `Metabolic_data.xlsx` (558 metabolites), not MetaboLights MTBLS13927, which the claim names; the paper reports 581 metabolites. The difference in metabolite count may explain the shortfall.
11. **[affects a conclusion] ven-subtypes-similar-physiology is underpowered.** It is a claim of absence tested on about 27% of the cells it is about (34 of 126).
12. **[affects a conclusion] fig5 connectivity used the code's annotations.** It counted from the code's `metadata_multiPatch.xlsx`, not from annotations in the deposit (DANDI:001751), which the criterion asks for. It did not check whether the deposit's NWB files carry annotations. The table has 1416 pairs where the paper has 1292, and its 6 subjects were not reconciled with the paper.
13. **[does not affect a conclusion]** fig4d reading (b) divides by one area (about 5 µm²) for every patch. This is reasonable given the Methods, but it means reading (b) was not tested on its own. The peaks found here are 1.26× the code's values.

**Blocked claims (step 4).** The archive lists exactly 84 NWB files from 5 subjects for 001752, all postsynaptic-current recordings. None of the blocked claims' data are in it. Some could still be tested in part:
- **fig6f-g:** the mapping table already loaded in cell 4 gives 14 VEN_Long in L5 ET and 15 VEN_Short in L5/6 CT, against an expected 10 ± 1 and 11 ± 1.1. It is testable now, and these counts would not reproduce.
- **fig4ac:** the DANDI:001746 features from cell 22 allow a VEN-against-L5 PC test on a small subset of the 281 and 306 cells.
- **fig3c and fig6-ven-subtype-morphology:** the code tables their criteria name (`AIScmp_PCvsVEN_Fig5c.xlsx`, `morphFeatTables_PC_VENL_VENS.xlsx`) look testable. I had no access to the repository, so I could not confirm.
- **The others:** the scRNA claims need GEO FASTQ or Zenodo (probably too_large), and ven-firing-rate-variability is methods_underspecified.

### C. What I could not check, and what would have let me

- **The code's tables.** I could not read them (metadata CSV, sheets, mapping and metabolite tables), so I took the notebook's parsing and the `×100` amplitude scaling on trust. Showing each sheet's header rows would settle this.
- **Detection validity.** These outputs would settle it:
  - noise against detected frequency, per file;
  - the group tests run on the sheet's own per-cell values under both labellings, for every experiment, to separate labelling from detection;
  - a positive control with synthetic events injected into real quiet traces;
  - results limited to files with noise below about 2 pA.
- **The figure.** I could not see the paper's Fig. 5b,c p-values, which were not in the text.
- **fig2d-f.** I could not check the per-cell feature distributions. Histograms of threshold, amplitude and half-width per subclass would show how far the outliers matter.
- **fig5 connectivity.** I could not reconcile the tested pairs with the paper's 1292. Pair counts per subject and session would.
- **The plots.** I did not view the images in cells 7 and 15.
