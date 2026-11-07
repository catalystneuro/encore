I wrote `claims/crcns-ear-1/10.1085-jgp.201912447.yaml`, and the quote checker passes it with 0 problems.

**Text read:** the version of record (PMC7335013, Europe PMC XML flattened to text). It has the Introduction, the model, the Methods, Results, Discussion, the legends of Figs. 1 to 5 and S1 to S7, and Tables 1 to 3. There is no PDF. The paper links no code. The MATLAB scripts and the GitHub repository (gaviganet/OHC_curation) are named only by the data set's own description, so I did not read them.

**Missing from the text:**
- **All displayed equations (Eqs. 1 to 9).** The flattening dropped them. I rebuilt Eqs. 2c, 3a/3b, 5, 6a/6b, 7 and 8d from the surrounding prose, and checked each against the paper's own numbers; for example, Eq. 6a and Eq. 7 give back every energy in Table 3. Each is marked in the file as a reconstruction. Eqs. 8b and 8c, for the non-lateral-wall capacitance, can only be partly rebuilt.
- **The contents of Tables S1 to S4.** Only their captions are in the text. The claims `tables3-by-region` and `recording-time` cannot be compared to numbers, and Table S4's charges are absent.

The main findings rest on Figs. 1 to 4 and Tables 1 to 3, so I wrote the claims. Supplying the PDF and the supplementary tables would close both gaps.

**Counts:**

| | Number |
|---|---|
| Claims | 48 (1 `link` claim for the cohort, 47 findings) |
| With a quote | 42 |
| Marked `inferred` | 6 (rows of Tables 1 and 2 that no sentence states) |
| With statistics | 9 claims, 9 entries |
| With a criterion | all 48 |
| With expected values | 35 |
| Using outside data (`with_inputs`) | 6: rat and mouse values from other papers, engineered mice, the all-rodent fit, the protein model, the hearing-loss fit, the temperature correction |

The prestin sequencing claim cannot be tested on this data set.

**Details the paper leaves open, and the readings named:**
- **V0.5 and the peak:** taken at the largest measured capacitance, or from a smooth fit.
- **Pipette-drop correction:** uses either the DC conductance or the admittance conductance; per-cell stored values are preferred where they exist.
- **Basal and apical:** turns 1 and 2 against 3 and 4, or turn 1 against turn 4.
- **Which cells:** the 70 cells of Fig. 2, all cells, or the 86 cells with 144 mM chloride.
- **Fitting:** the Eq. 6b fit with or without an intercept. For the 5 pF bins of Fig. 3a, bin edges at multiples of 5 pF or starting at the smallest value. Adjusted R² computed with or without weights. Fig. S4 fits weighted or not, and whether the 0.4 V cut also applies to the XE991 fit.
- **Stereocilia bundle capacitance:** stored per cell, stored lateral-wall values used directly, or zero. The method comes from Corbitt et al. (2012) and is not given here.
- **XE991 effect test:** the two-way model over pigmented cells only, or over all three groups.
- **Cell surface area:** stored, 2πr(l−r), or 2πrl.
- **Grouping for C_L,eq, z and the sensor area:** the Fig. 3a bins, the Fig. S4 bins, or per cell.
- **Unnamed tests:** where the paper names no test (the αB–CLW trend, absence of correlation with voltage drop, "approximately constant" Vd, "cover the data range", the recording-time correlation), the criterion states the test chosen and marks the claim as resting on an assumption.
- **Inconsistencies in the paper:** Vd is 0.033 V in the text and 0.034 V in the legend; the power-law exponent is −1.15 in the legend and −1.5 in the text; λ is 3.95 κBT in the text and 3.97 in Table 3. Both readings are allowed in each case.
- **Temperature correction:** taken from Meltzer & Santos-Sacchi (2001); the paper gives no number for it.

Nothing is committed or pushed.
