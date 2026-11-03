**Verifier report, round 2: Semenov et al. 2026 on DANDI:001521 (v0.261006.1845)**

The claims file has 27 claims and the attempt record gives 27 outcomes: 2 reproduced, 3 not reproduced, 1 partially reproduced and 21 blocked.

**1. Outcomes and assumptions**

| Claim | Record | Agree? | Basis |
|---|---|---|---|
| fig6a-ca-entry-1000-1200 | reproduced | Yes | Cell 22, M1 (1000 V/cm = 250 V, 1200 V/cm = 300 V). Three of four readings hold at both fields: end against sham, peak against zero and peak against sham. The means at both fields exceed those at 0 and 150 V (end −10.26 %, peak 0.55 %). M2 gives the same. The step at the pulse (cell 24) shows the 1000 V/cm entry is small: 0.35 ± 0.17 %, with p = 0.058 against zero. The record now says so. |
| fig6a-ca-sustained | not_reproduced | Yes | Cell 27: the end values are −5.44 and −3.83 % (M1), and +1.24 % with p = 0.53 at 350 V (M2). This still rests on the sham decline, which the paper's Fig. 6A does not show. Cells 12–13 now place the decline in the cells' own signal (raw −8.7 %, background −1.0 %). |
| fig6a-780-not-significant | reproduced | Formally only, as in round 1 | Cell 31: −7.42 %, one-sided p = 1. The record now says the test cannot detect an increase and that the outcome "carries little information". That is what I asked for. |
| fig6b-train-threshold | not_reproduced | Yes | Cells 34 and 43: the criterion is met in 0 of 36 combinations. The 780 V/cm fraction is 2.9–22.1 % (M1) and 44.7–78.7 % (M2). The higher-field minimum is at most 79.5 %. The comparison set (900/1000 V/cm only) and the count (256) are now the relevant ones. |
| fig6b-650-weak-but-significant | not_reproduced | Yes (changed from blocked, as I recommended) | Cell 38. M1: −9.17 ± 0.83 %, one-sided p = 1 for above zero, and p = 0.20 against 70 V. M2: p = 0.27 against zero. |
| fig5b-conductivity-calibration | partially_reproduced | Yes | Cell 46: 1.33 % (outside 2 ± 0.2) and 11.87 % (inside 12 ± 1.2). This matches my independent derivation. |
| 21 potentiometric claims | blocked: data_missing | Yes | Unchanged from round 1. |

On assumptions: no outcome carries `assumed: true`. The M1 conversion is called "an assumption" in the deviations prose, and every outcome is stated to hold under M2 too. Cells 22, 27, 31, 34, 38 and 43 confirm this, so no outcome rests on it, and leaving it unflagged is acceptable. Adopting M1 is reasonable on the group-size match in cell 19 (|Δn| summed: 32 under M1, 76 under M2).

**2. Statements the printed outputs do not support**

- **Cell 32:** "under the adopted conversion the one variant that separates 1000 and 1200 V/cm from the sham agrees with it."
  - It is not the only such variant. In cell 22, end-against-sham and peak-against-sham also separate both fields from the sham, and both find 780 V/cm significant (cell 31: p = 1e-6 and p = 0.021).
  - The step barely separates 1000 V/cm: p = 0.025 against the sham, and p = 0.058 against zero.
  - The two steps, 0.15 ± 0.16 % at 780 V/cm and 0.35 ± 0.17 % at 1000 V/cm, are not shown to differ.
  - Its "agreement" is therefore weak evidence. It should be described as the only variant not confounded by recording order, not as the only one that detects the higher fields.
- **README:** "Unpulsed cells lose 12 to 16% of their Fluo-4 signal over a recording (the raw cell signal, not the background)". In cell 12, 12–16 % is the background-corrected dF. The raw cell signal falls 8.7 % and 7.5 %.
- **Summary (cell 48):** "It slows with each recording of a field of view". This holds for the single-pulse session, but in the train session the pre-pulse slope goes −11.39, −5.12, −4.48, −2.04, −2.98, −2.75, −2.04, −5.40 % per min (cell 12). That is not a steady slowing. Cell 13 and the record's finding phrase this correctly ("2.0 to 5.4% per minute later").
- **Cells 29 and 25, and the record's notes for fig6a-ca-entry and fig6a-ca-sustained:** "p below 1e-8". The notebook prints these p-values only as 0.000000 (cells 22 and 27). From the printed n, mean and s.e. I get 4.9e-9 and 3.0e-11, so the statement is true but not shown.
- **Cell 36:** "Under no reading is the fraction at 780 V/cm within 25.2 to 30.8%". This holds for the criterion's 10-frame window. With a 5-frame window and region 0.5, cell 41 gives 27.9 %, which is within tolerance. The outcome is unaffected, because the ≥ 90 % condition fails there (76.6 %).
- **Record findings with no notebook output behind them:**
  - "age of P1D" and the species string.
  - "Six other dandisets … name this paper in their metadata".
  - Cell 47's guess that "~2%" "was probably read from its Fig. 5B graph", which is speculation.
- **Cell 5 and the record's metadata finding:** "42 of the 73 files are 60-pulse 6 Hz trains". 9 of those 42 are shams with 0 pulses (cell 4).

Everything else in the "**Result:**" cells (25, 29, 32, 36, 39, 47), cells 42 and 44, the Summary, the README table and the record's notes matches the printed numbers.

**My round-1 reasons in the record:** they are stated faithfully, and in substance in my own words, for all 27 claims. They are somewhat shortened (the p-values from my round-1 table are dropped), but no reason is changed. The fig6b-650 entry correctly gives `agrees: false` with my not_reproduced outcome.

**3. Round-1 points**

Resolved:
- **3 (conversion):** M1 was adopted from Fig. 6B, with M2 kept as a variant. The 1.00 mm against 1.6 mm gap is recorded as a metadata_error finding, which is an adequate reconciliation.
- **4 (comparison set and counts):** the higher fields are now 900/1000 V/cm only, and the count of 256 is reported. Measured was updated.
- **5 (rule b):** the literal reading was added.
- **6 (sign in the printout):** cell 38 now gives the sign and the one-sided p.
- **7 (repeated cells):** a test with fields of view as the unit was added (cell 24), and the recording-order confound is now exposed (cell 12).
- **8 (docstring counts):** corrected to 31 and 42.
- **"Could not check" items, all supplied:**
  - raw, background and whole-frame sham traces (cell 12);
  - region overlays (cell 14), which I viewed: regions sit on the cells;
  - the train end-dF table (cell 38);
  - the 14-cell combinations (cell 24).

Partly resolved: **1 (sham drift).** The decline is now shown to be in the cells' own fluorescence, not the background, and it is reported to the authors. It is still unexplained relative to Fig. 6, and it still decides fig6a-ca-sustained and colours every end-value reading. The overlays also show dim, unsegmented cells inside the "cell-free" region in several train fields of view (c2, c6, c7, c8). In the train session the background is 1.26 times the corrected cell signal (cell 12), so the train dF values depend strongly on the background estimate. This does not remove the raw decline, but it adds uncertainty to the train fractions.

Remaining, as it bears on a conclusion:
- **(a)** fig6a-ca-sustained being not reproduced depends on a decline the paper's figure does not show. It is correctly framed as a question for the authors.
- **(b)** fig6a-780-not-significant being reproduced comes from a test that cannot detect the effect. It is correctly passed to a reader as a claims-file question. The cell-32 sentence quoted in section 2 overstates the step variant's support and should be corrected.
- **(c)** Recording order is confounded with voltage in both sessions. This weakens every sham-referenced reading, including those behind fig6a-ca-entry. Only the step reading avoids it, and that reading is marginal at 1000 V/cm.
