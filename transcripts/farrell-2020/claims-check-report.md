I checked the claims file for CRCNS:ear-1 against the paper and made 19 corrections. The file is ready for an attempt, though the gaps in the supplied text listed under "Still open" remain. Nothing was committed or pushed.

**Checker result** (before and after the edits): `claims/crcns-ear-1/10.1085-jgp.201912447.yaml: 48 claims, 42 quotes, 9 statistical values, 0 problems`

**Changes, by claim** (each is also recorded under `checks` in the file):
- **Opening comment:**
  - The signs in the rebuilt Eq. 7 were the wrong way round. The paper says the negative sign gives activation, and only that reproduces Table 3's barriers (2.68 forward, 0.125 reverse).
  - The argument for reading basal as turns 1 to 2 and apical as turns 3 to 4 was circular. It now rests on Fig. 1's 86 cells against the 84 cells in Table 1.
- **nlw-capacitance:** the form of Eq. 8c is now marked as rebuilt from the prose. The restriction to 144 mM chloride cells is not in the paper, so it is now an open choice between all 89 cells and those 86.
- **fig1-charge-not-linear:** added as an open reading whether the R² is taken on QTm² against CLW², or on QTm against CLW.
- **alpha-gradient-pigmented:** the criterion said these values times four equal Table 1 rows (b) and (c). That holds only for row (b); the albino values give 31.0 and 30.4 against the table's 31.3 and 30.5.
- **table1-xe991-no-effect-alpha:** added a one-way ANOVA on XE991 as a reading, since the paper does not give the model of its test.
- **fig2b-v05-vs-clw, xe991-voltage-clamp:** a slope test and a comparison of medians that the paper does not use are now marked as choices made by the claims file.
- **table2-xe991-v05-shift:** tolerance widened from 0.002 to 0.010 V. Table 2's own means give shifts of 19 to 29 mV, so the 10% default would have failed the paper's own numbers.
- **fig3a-eq3a-fit:** the paper states weights only for the Eq. 3a fits, so the unconstrained fit now runs both weighted and unweighted.
- **fig3a-high-density-deviation:** added the Fig. S4 bins as a reading, since the sentence describes binned data.
- **fig4a-vh-rises-vd-constant:** added a reading with the XE991 and non-XE991 bins pooled, as Fig. 4a plots them together.
- **fig4d-cleq-two-limits:** the split at -0.045 V was made up. It now uses the V0.5 ranges Table 3 gives for each pathway (up to -0.056 V, and from -0.043 V). Also noted that the paper's limits may include rat and mouse values.
- **fig4c-sensor-area:** noted that the paper's own numbers fit the text's exponent of -1.5, not the legend's -1.15.
- **table3-pathway-energies:** the barrier signs now follow the paper. The criterion now says Table 3 uses z = 0.859 for both pathways, which reproduces its 3.95 and 2.16 k_BT.
- **alternative-limit:** the text prints "[n/z]"; the criterion now notes that z/n is the reading consistent with Eq. 5 and with the paper's values.
- **fig4f-all-rodents:** source corrected from paragraph 4 to paragraph 3.
- **two-hyperpolarized-states:** source corrected; the Theoretical model is its own section, not part of Results.
- **v05-temperature-corrected:** the turn 3 tolerance is now the paper's stated "± 0.022", read as volts, in place of the 10% default.

**Still open:**
- All the displayed equations (Eqs. 1 to 9) are missing from the supplied text. The rebuilt forms do reproduce the paper's numbers.
- The contents of Tables S1, S3 and S4 are missing, so the values in tables3-by-region, recording-time and molecular-model cannot be compared until those tables are supplied.
- 16 pigmented XE991 cells had 144 mM chloride, but Table 1 row (a) holds 15. Which cell was left out cannot be settled from the paper.

Every main finding has a claim, and every claim comes from this paper.
