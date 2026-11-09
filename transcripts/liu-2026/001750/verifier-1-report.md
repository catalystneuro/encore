**Verifier report, round 1: Liu et al. 2026, DANDI:001750 v0.260825.0222**

The claims file holds 34 claims; 4 of them are on this dataset. The notebook tests those 4 plus fig8a, fig8de and fig4j-eepsp-amplitude, and treats fig3c and all other `elsewhere` claims as blocked. No attempt record was among my materials, so the counts below come from the claims file and the notebook.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| na-cell-table-link | partially_reproduced | All 35 files match the code table by file name, and all 35 cell IDs agree (cell 7). The files carry no cell type, so no type can disagree. But at most 2 of 35 cells are within 10% of the table under any reading (cell 7), against the 28 required. The post-hoc smoothing variant reaches 26, and the criterion does not let it decide. |
| fig4d-sodium-current-lower | blocked (methods_underspecified) | The counts are 14 VEN and 21 PC, within tolerance. The VEN median is lower under all 8 readings, but rank-sum p < 0.05 only under a1b1c1 (p = 0.045) and a1b1c2 (0.025). The other six give p = 0.077 to 0.29 (cell 10). Readings disagree, so the criterion gives blocked. Under the four a2 readings, the ones that remove the holding offset, p ≥ 0.077, so the measure as specified does not reproduce. The code table's own values give p = 0.001. |
| model-na-ratio | partially_reproduced | Only the four a1 readings give a ratio within 0.6875 ± 0.069 under some summary (0.68 to 0.75). All a2 readings fall outside (0.79 to 0.99), and so does the code table (0.58 mean, 0.51 median) (cell 12). The a1 ratios carry the holding-current offset (problem 2) and the parent claim is blocked, so this "partial" is weak. |
| na-patch-capacitance | blocked (data_missing) | The series hold only data, electrode, gain and starting_time (cell 13). I queried the metadata of all 35 assets and the dandiset: none mentions capacitance or resistance. Nothing of this claim can be tested from the archive's metadata. |
| fig8a-metabolite-gradient | not_reproduced | Welch's ANOVA then Games-Howell gives 175 metabolites for AIC vs V1 (tolerance 205 to 251) and 84 for AIC vs PrC (97 to 119). The log2 variant gives 190 and 95 (cell 14); both counts are outside tolerance either way. The deposit holds 558 of the paper's 581 metabolites, and I confirmed MetaboLights has only this one MAF file. The direction (more differences vs V1) holds. |
| fig8de-glycolytic-bias | partially_reproduced | Citrate is higher in AIC (ratio 1.37, Games-Howell p = 0.0005) and L-glutamic acid is higher (1.35, p = 1e-4). 2-Ketobutyrate is lower (ratio 0.37) but not significant (p = 0.18; log2 0.086) (cell 16). The criterion requires all three at P < 0.05 and defines no partial outcome; strictly read, the claim is not reproduced. |
| fig4j-eepsp-amplitude | reproduced | VEN amplitude is higher at every level. The cell-type effect is p = 0.0065 in the two-way ANOVA and p = 0.0068 in the repeated-measures ANOVA with 26 pairs (cell 17); the paper gives P = 0.0034. The monosynaptic selection cannot be re-applied to a summary table; it is taken as already done. |
| fig3c-ais-distance-length | blocked (metadata_insufficient) | The sheet has no slice or animal column, so neither two-way ANOVA can be run. Its counts (120 VEN, 500 PC) also differ from the legend (108, 430) (cell 19). As a description only, rank-sum is in the stated direction for distance and for length. |
| other `elsewhere` claims | blocked (as the notebook) | The notebook gives no reason per claim beyond "see the record", which I do not have. ven-subtypes-similar-physiology is partly testable (problem 7). For fig4j-eepsp-latency I confirmed that `sumData_StimWM.xlsx` has no latency column. |

### B. Problems

1. **[affects a conclusion]** `max_inward` takes the single most negative sample of unfiltered 100 kHz traces, and noise inflates it.
   - This follows the claims file's readings, so the gap is in the claims file: it names no filter, and the paper names none either.
   - Per-repetition noise SD is 3.5 to 57 pA (cell 3). Under a2b1c1 the computed value is a median 1.32× the table value.
   - Several maxima are not Na⁺ peaks. AS4c14, AS5c20, AS1c1, AS2c7 and AS3c10 peak at −60 or −65 mV, some 8 to 10 ms after the step onset. AS3c11 and HS1c12 peak 12.9 and 18.8 ms after it (cell 7).
   - On a synthetic trace, 7 pA of noise raised a true 64 pA peak to 80 pA. The helper otherwise behaves as specified: step levels and onset are read correctly, b1 keeps sweeps up to 0 mV, and a2 subtracts the mean from −2 to −1 ms before the step.
   - This affects na-cell-table-link, fig4d and model-na-ratio.
2. **[affects a conclusion]** The a1 readings keep the pre-step holding current, which is −29 to −131 pA, and +92 pA in HS1c18 (cell 3). So a1 values (about 4× the table) mostly measure that offset, not the Na⁺ current. a1 is a reading the claims file allows, but the only significant fig4d readings, and all of model-na-ratio's in-tolerance ratios, are a1.
3. **[does not affect a conclusion]** The smoothing variant (cells 9 and 10) was tuned to match the table (75 samples was the best fit), so its p = 0.0008 is not independent evidence. It is correctly labelled as non-deciding.
4. **[does not affect a conclusion]** Patches have 1 to 10 repetitions, so the noise bias differs by cell. Repetition count and noise are never shown by cell type, so a group-dependent bias was never checked.
5. **[does not affect a conclusion]** The effect is session-dependent: under a2b1c1, VEN > PC in session AS (40.7 vs 36.2 pA) and VEN < PC in session HS (15.9 vs 40.3 pA) (cell 10). This is reported but not discussed.
6. **[does not affect a conclusion]** In cell 17, the stimulation level is assigned by row order inside each block of the "copied data" columns, and 9 rows have no stimulation value. The same sheet's "re-orgnized data" block (columns G to J) gives an explicit level on every row and was not used as a cross-check.
7. **[affects a conclusion]** ven-subtypes-similar-physiology is left blocked although part of it can be tested. Column J of the same sheet types 24 of the 26 pairs as VENL or VENS (12 each at every stimulation level). That matches the Extended Data Fig. 9f design, so the VEN-L vs VEN-S eEPSP ANOVA (paper p = 0.9852) can be run.
8. **[does not affect a conclusion]** In fig8de, glutamate has two entries ("L-Glutamic acid" and "Glutamic acid glutamate"). The notebook picks neither explicitly, though both are printed. The second is not significant (p = 0.15).
9. **[does not affect a conclusion]** In the cell 14 log2 variant, the one zero value is clipped to 1e-9, which makes one extreme value. It is only a variant.

The statistics check out: the Games-Howell formula and the Welch gate in cell 14 are correct, and the rank-sum is two-sided as the criterion requires. No training/test split is involved. Units are pA, converted from amperes with the stored conversion factor. No chance level applies.

### C. Not checked

- **Patch capacitance inside the NWB files.** Only the series fields and asset metadata were inspected. If the notebook printed every field and attribute of `general/intracellular_ephys/IntracellularElectrode` (description, seal, resistance), plus any `lab_meta_data` and notes strings, I could confirm data_missing from the files themselves.
- **Whether the outlying maxima are noise or artefacts.** A plot or printout of the averaged trace at each cell's peak sweep, under a2b1c1, would show this. So would a per-cell I–V curve of the computed peaks.
- **Whether the noise bias differs between groups.** Repetition count and noise SD tabulated by cell type would let me check problem 4.
- **The other `elsewhere` claims.** Without the attempt record I cannot judge why each was blocked; the notebook should state a reason per claim.
