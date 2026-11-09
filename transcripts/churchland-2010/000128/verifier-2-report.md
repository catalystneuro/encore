**Verifier report: Churchland et al. 2010 on DANDI:000128 (round 2)**

**1. Outcomes**

The claims file has 22 claims and the attempt record has 22 outcomes:
- 11 reproduced
- 1 partially reproduced (recordings-jarray)
- 3 not reproduced (fig4d-mean-correlation-jarray, fig6-performance-vs-dimensionality, prep-dimensionality)
- 7 blocked: 5 for data_missing, 2 for metadata_insufficient

I agree with all 22. Each one matches the printed outputs and the claims file's criteria:
- **recordings-jarray (partially reproduced):** 182 units fails under every reading (cell 12).
- **fig4d (not reproduced):** p is 0.42 to 0.61, so even the "partially reproduced" rule fails (cell 15).
- **fig6-performance-vs-dimensionality (not reproduced):** best k is 14 and there is no decline (cell 44).
- **prep-dimensionality (not reproduced):** 15 and 18 components (cell 32).
- All the reproduced claims meet their criteria in cells 19, 22, 25, 29, 38, 41, 47, 50, 53, 58 and 61.

**2. Sentences the outputs or the paper do not support**

- **Cell 17 and the fig4d notes.** Cell 17: "The means are positive but less than half the paper's 0.13 and 0.11"; the notes: "The means are positive but below half the paper's."
  - This holds for Pearson (0.051 < 0.065).
  - It fails for Spearman: 0.072 is 65% of 0.11, above half (0.055) (cell 15).
  - The outcome is unaffected.
- **Cell 59 and the fig8-model-weak-correlation notes.** "a central 95% of about -0.43 to 0.43 under every reading" (the notes say the same).
  - Cell 58 prints lower bounds of −0.385 to −0.430 and upper bounds of 0.350 to 0.428.
  - −0.43 to 0.43 is the outer envelope, not each reading's interval. "About ±0.35 to ±0.43" would be accurate.
  - My own round-1 wording, "about −0.40 to 0.40", is also loose.
  - The outcome is unaffected, because 0.08 lies inside every interval.
- **Cell 33 and the prep-dimensionality notes.** Both say "This T-matrix" may mean a conditions × (neurons × times) matrix.
  - I raised this in round 1 and now withdraw it. Raw-stream text extraction of the supplement worked this time.
  - The sentence just before the quoted one defines the matrix: "T was c × n with each row containing the mean preparatory activity for every neuron" (Supplemental Experimental Procedures, "Estimating the upper limit of PD performance").
  - So the claims file's c × n matrix is the paper's. The 55 to 61 component variants test a reading the paper rules out.
  - The phrase "all neurons" there also points to reading N2 (18 components).
- **Summary (cell 64) and README.** "T2 (91% of trials kept …)": the 90.8% is of the 1967 trials with delay > 400 ms. It is 77.8% of all 2295 train trials (cell 10). The wording is ambiguous next to the paper's "~90% of all trials". This is minor.
- **Notes I cannot check.** Several notes quote values from the earlier record that the notebook no longer prints:
  - T1 for fig6-performance-vs-dimensionality: best at k = 5, 0.281, falling to −0.287.
  - T1 for fig4d: 0.025 and 0.054.
  - fig7b: 0.904 to 0.972, and 0.918 under T1.
  - S2 for prep-dimensionality: 4 components with 6 units.
  - T1 for prep-dimensionality: 18 and 20 components.

  These are history, not support for any current outcome.

Everything else checks against the printed outputs: every other "**Result:**" sentence, the Summary table and text, the README table (11, 1, 3 and 7 claims, consistent with the record) and the remaining notes and findings.

**My round-1 reasons in the attempt record.** The verification entries give my round-1 reasons faithfully and in substance in my words. The only place the record follows my wording rather than the output is my loose "about −0.40 to 0.40" for fig8 (above).

**3. Round-1 points**

Resolved:
- **1 (recordings-jarray table).** Each row is now labelled by reading. The held-in units and the delay > 400 ms count are marked as not readings, and reading (a) is shown both as 2869 and as 2295 (cell 12).
- **3 (n = 17).** Every selected neuron is now printed with its id digit, its two tunings, r and Spearman r (cell 15). The texts say the tests have little power, and that fig3 rests on unit 1581.
- **4 (edge k).** This is now stated in cells 39, 51 and 54 and in the notes.
- **5 (suppfig1).** "Positive by construction" is now stated in cell 30.
- **6 (lost comparison).** It is printed in cell 41: the 2-D initial-velocity space (0.238 against 0.223), with margins at k = 1 of 0.0024 to 0.0041.
- **7 and the array identity.** The electrode groups and the id digits are now printed (cell 4). Nothing maps a digit to an array, so both blocks remain correct.
- **Test-file trials.** The test file has its own clock and no delay or success column (cell 4). Reading (a) stays undecidable, but the outcome does not depend on it, because the unit count fails either way.
- **2, T-matrix part.** Resolved by the paper itself (see section 2).

What remains that bears on a conclusion:
- **prep-dimensionality.** The main text says "at least 7-10 dimensions". The supplement, which the claim quotes, says "7-10 dimensions were required" for the c × n matrix. I now judge the claims file's two-sided reading defensible, not a misreading.
  - The open question in `questions/000128.yaml` should be updated to drop the T-matrix part.
  - What still separates the result from the paper is the method: trial-averaged rates from 10 to 27 trials per condition (cell 10) carry noise that may add components. The claims file does not fix this.
- **fig4d and the correlation claims.** The dataset has 182 units, not 146, and nothing records which units or trials the paper used. Only 17 neurons pass the selection, so the not-reproduced outcome on the mean correlation may come from the selection rather than the data. The attempt states this as a deviation, and I agree it stays unresolved.
