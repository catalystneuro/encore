**Verifier report, round 2: Sabatini & Kaufman 2024 on DANDI:000070 (34 claims in the claims file; 34 outcomes in the attempt record: 13 reproduced, 11 partially reproduced, 10 not reproduced)**

Cell indices below count from 0 within each notebook: nb1 is `reproduce_sabatini_2024.ipynb`, nb2 is `reproduce_sabatini_2024_kinematics.ipynb`.

### 1. Outcomes and assumptions

- **Outcomes.** I agree with all 34 stated outcomes. None of the numeric mismatches in section 2 changes an outcome.
- **Outcome changed since round 1.** fig7f-decoder-beats-standard went from blocked to partially_reproduced. I agree.
  - All 14 non-GPFA decoders are now run per dataset (nb2 cell 41).
  - LDR is higher with p < 0.001 in 56/56 comparisons under both bases (nb2 cell 42).
  - The criterion's partial clause, "all but the GPFA decoders", applies.
- **Outcomes marked `assumed: true`.** Each assumption is stated and reasonable:
  - suppfig2, fig6e, fig7c-ldr-encoding, suppfig7a, fig7c-standard-encoding-worse, fig7f-ldr-decoding and trial-curvature-decoding: hand positions measured from each trial's start.
  - fig6e: the paper's kernel length scales. The sweep in nb2 cell 17 shows the outcome does not depend on them.
  - fig7f-decoder-beats-standard: the training subset of 4,000 or 12,000 samples, and velocity integrated from the true position at −260 ms. The integration, if anything, favours the standard decoders.
  - suppfig8: no EMG in the files, and the code's centring. The variant centring gives the same outcome.
- **The online-onset assumption.** Every claim's deviations state it as "Assumption". `assumed: true` is not set for the notebook-1 claims, though.
  - The offline-onset variant (nb1 cell 86) covers fig3g, tbf-variance-explained, the jPCA R² and variance, single-lds-variance, fig2c, fig3a, fig3i (reading b, truncate only) and rotation-orientation-dimensionality. Those outcomes do not rest on the assumption.
  - It does not cover fig3c, fig4b, fig4c, fig4d, fig4f, fig5a, suppfig6a/b/c, suppfig3, suppfig2, tbf-shuffle-control, fig3h or any notebook-2 claim. Strictly, those outcomes still rest on an untested assumption. This is minor: no recomputed claim moved.

### 2. Sentences the printed outputs do not support

None of these changes an outcome. Many of the conclusions quote numbers that differ slightly from this execution's printouts.

- **nb1 cell 43 (fig2c)**, also in the record's notes and response:
  - Text: "the single-condition LDSs explain 83.4%, 90.7%, 92.9% and 94.4% (91.0% for PMd-N at 5)".
  - Cell 42 prints 83.2, 90.5, 92.8 and 94.1 (90.9 at k = 5).
- **nb1 cell 60 (suppfig3)**, also in the record's notes:
  - Text: "in-sample single-condition LDS (83.4%, 90.7%, 92.9%, 94.4%)".
  - Cell 59 prints 83.2, 90.5, 92.8 and 94.1.
  - The record's held-out LDS "67.5%, 77.0%, 83.6%, 78.6%" (notes and response): cell 59 prints 67.5, 76.8, 83.5 and 78.4.
- **nb1 cell 48 (fig3a)**, also in the record:
  - Text: "0.63, 1.75 and 3.19 Hz (M1-N)". Cell 47 prints 1.74.
  - The response says "M1-N 1.75 Hz in the new run", which is not what was printed.
- **nb1 cell 52 (fig3c)**, also the record's `measured`:
  - Text: "0.717, 0.669, 0.660 and 0.580" (halves null). Cell 51 prints 0.716, 0.670, 0.660 and 0.581.
  - Text: "0.797, 0.729, 0.646 and 0.592" (Poisson null). Printed: 0.796, 0.731, 0.646 and 0.594.
  - Text: norm distance "0.577 to 0.787". Printed: 0.579–0.786.
  - Text: seeds "0.577 to 0.717". Cell 54 prints 0.579–0.716.
- **nb1 cell 57 (suppfig2)**, also the record's `measured` 0.243:
  - Text: "0.243 … (0.243 and 0.296 under the skew-normal basis)". Cell 56 prints 0.244 under both bases.
  - Text: "per dataset it is 0.149 to 0.476". Printed: 0.150–0.474.
  - Text: "each conjugate pair once gives 0.235 and 0.291". Printed: 0.237 and 0.291.
- **nb1 cell 24 (fig3i)**, also in the record:
  - Text: "The warped correlations move by at most 0.004 over the five seeds."
  - PMd-N under reading (a) runs from −0.304 to −0.299, a change of 0.005 (cell 23).
- **nb1 cell 36 (fig4f)**, also in the record:
  - Text: "rho 0.843 to 0.952 … for four of the six planes". Those four include M1-N plane 2 at 0.816, so the range is 0.816–0.952 (cell 35).
  - Text: "(0.826 to 0.947)" for the code's input. Printed: 0.824–0.947 (M1-N plane 2, 0.8235).
- **nb1 cell 87 (offline variant)**, also in the record's fig2c notes:
  - Text: "explains 79.6% to 89.8%". Cell 86 prints `lds_ve` of 0.792–0.897, i.e. 79.2–89.7%.
- **Record, fig3a notes** (no conclusion cell states this):
  - Text: "0.87 … 3.07 … (2 of 10)" on the offline onset.
  - Cell 86 prints 0.86 and 3.06. Its 3 of 10 are within 10%: 1.54, 1.53 and 2.74 (inside 2.25–2.75).
- **nb2 cell 11 (fig6b)**, also in the record:
  - Text: "against a null of 31.1% to 44.1%". Cell 10 prints 44.0, 35.7, 44.8 and 29.2, i.e. 29.2–44.8%.
  - The response says "(PMd-N 1.3e-11), as printed". Cell 10 prints 6.7e-12.
- **nb2 cell 33 (fig7f-ldr-decoding)**, also in the record's notes and its fig7f-decoder notes:
  - Text: "88.6% to 93.0% for skewnormal". Cell 32 prints 88.4–92.8.
  - Text: null "5.4% to 10.4%". Printed: 5.4–10.1 (svd) or 5.8–10.5 (skewnormal).
  - Text: seeds "86.8% to 94.5%". Printed: 87.2–94.5 (svd) or 86.7–93.9 (skewnormal).
  - The response says these "are corrected to the printed values"; they are not.
- **nb2 cell 39 (suppfig8)**, also in the record, which adds "under both bases":
  - Text: "p = 4.5e-10 to 8.6e-06". Cell 38 prints 4.53e-10 to 3.66e-06 (svd), or 2.45e-10 to 1.11e-05 over both bases.
  - Text: per-variable centring "p = 8.4e-11 to 4.1e-06". Printed: 8.43e-11 to 2.79e-06 (svd), 3.56e-06 (skewnormal).
- **Record, fig6e notes:** seeds "OU … 40.5% to 83.3%". Cell 17 prints up to 0.832 (svd) or 0.834 (skewnormal).
- **Record, `sanity` finding:** "Hand positions are in mm with a conversion of 0.001 to meters". No printed output shows the conversion.

Everything else checks out against the printed outputs: the other "Result" cells, both Summary sections, the README (13/11/10, matching the record) and the remaining notes.

**My round-1 reasons in the record.** They are stated faithfully and in my own words for all 34 claims, including problems 1, 3–12. Problem 2 (the alignment event) appears in no `reason` field; it is only addressed in the responses.

### 3. Round-1 points

**Resolved:**
- **1 (fig3i).** The per-trial reading is run, the span text is corrected, and the end+100 variant is added. The outcome is not reproduced under every reading.
- **2 (onset).** The offline variant covers the claims that depend most on the onset, and their outcomes hold. The rest is as in section 1.
- **4 (fig4d/f).** The basis is now re-extracted from normalised data as the main reading.
- **5 (length scales).** The scale of the reach parameters is printed and the length scales are swept.
- **6 (decoders).** The decoders are now run.
- **7 (units).** The notes now disclose it.
- **8, 9, 11 and 12.**

**Remaining, bearing on a conclusion:**
- **Problem 3, a claims-file misreading (suppfig3).** The legend calls the comparison cross-validated, but the main reading compares held-out TBF with in-sample LDS. Scored like for like on held-out data from −160 ms, TBF beats LDS and jPCA in 4/4 (nb1 cell 59). That would make the claim reproduced. The outcome correctly stays as the claims file decides, and the question has been put to a reader.
- **Problem 7 (unsorted threshold crossings).** This is a data limitation and cannot be fixed. It remains a plausible cause of the dimensionality failures: single-lds-variance, rotation-orientation-dimensionality and suppfig6b.

**Remaining, not bearing on a conclusion:**
- **Problem 10 (suppfig8).** The notebook's "code" centring subtracts each sample's mean over the four variables. That is consistent with `mean(kinParams, 2)` only if `kinParams` is samples × 4. The notebook centres neurons as N × samples, which suggests the per-variable variant is the code's actual operation. I still cannot check `removePotent.m`. Both centrings give p < 0.036 in every dataset, so the outcome stands.
- **Mismatched numbers.** The numbers in section 2 should be brought into line with the printouts.

### 4. Critical findings

No finding in the attempt record is rated `critical`.

Of the findings that do have a severity, both are rated reasonably:
- **Finding 1 (unsorted units, `major`).** nb1 cell 5 shows it: the units table description says "Threshold crossings on each electrode, not sorted", with 96 units per array. The file states this openly, so the data are not wrong. Because every population analysis changes, `major` is right.
- **Finding 2 (missing `maze_condition`, `minor`).** nb1 cell 4 shows `conds` NaN for Nitschke 2010-09-20 and 2010-09-22, but the finding names no cell.
