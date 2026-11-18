# Round 2 verifier report: payne-2020-01 (Payne et al. 2020, SPARC:206 v1)

Counts come from the claims file and the attempt record. There are 31 claims and 31 outcomes: 9 reproduced, 1 partially reproduced, 6 not reproduced and 15 blocked (14 `data_missing`, 1 `metadata_insufficient`). Seven outcomes carry `assumed: true`; these are the six anaesthetised-ECAP claims and awake-ecap-latencies.

My round-1 report said "13 tested and 18 blocked". That was my own arithmetic error: my own table lists 16 tested and 15 blocked. I still see no place where the claims file misreads the paper.

## 1. Outcomes

I agree with all 31 stated outcomes. The notes for each claim:

- **anes-ecap-recorded (reproduced, assumed):** I agree. Both assumptions are stated and reasonable: the lowest current stands in for 0 mA, and the peak rule is the record's own. This is the only ECAP outcome that changes with the peak rule. The `window` rule gives 2 of 5 rats (cell 34). The record's notes say so.
- **anes-ecap-latencies, anes-conduction-velocity (not reproduced, assumed):** I agree. 0 of 288 and 0 of 864 combinations meet the criterion under four peak rules. The assumption is stated.
- **anes-threshold-order (not reproduced, assumed):** I agree under the criterion's definition, 0 of 192 combinations. The outcome rests on two things, both stated:
  - It excludes the "sustained" reading. Under that reading, 12 of 384 combinations meet the criterion (`largest` and `window` rules; cell 43).
  - It applies a pass level that noise alone passes in 63–77% of current steps (cell 47).

  The not-reproduced outcome therefore says little about the paper.
- **fig2c-p3-above-p1 (reproduced, assumed):** I agree. It is narrow: unadjusted Dunn P = 0.034, n = 4, with a non-significant Friedman test (P = 0.105). All of this is stated.
- **fig2ab-one-rat-p2-below-p1 (not reproduced):** I agree.
- **awake-ecap-latencies (not reproduced, assumed):** I agree. The criterion needs three peaks in every rat. Only 5 of 7 recordings have them at best, and 12-057 has none under any rule (cell 56).
- **awake-threshold-increase (blocked, `metadata_insufficient`):** I agree. `pool_id` is empty for every subject (cell 3).
- **impedance-increase (partially reproduced):** I agree. The 8-week value is untestable, not out of tolerance.
- **electrode-failures (blocked):** I agree. The partial result on 32 electrodes is now stated.
- **colonic-pressure (not reproduced):** I agree. The outcome does not depend on the claims file's t-test rule for a responder. No rat's mean is within 2.6 ± 0.1 under any reading: the nearest are 2.17 and 2.88 (cells 66 and 68). So no `assumed` flag is needed.
- **Table 1, six claims (reproduced):** I agree; all are read from the derivative table.
  - **table1-hfpo-frequency should be marked `assumed: true`.** It is the only one with no independent support. Both readings recomputed from the traces fall below the CI (8.05 and 7.11 Hz, cell 91). Its n is 7, not 9. The outcome rests entirely on assuming that the derivative's HFPO frequency, whose method is unstated, matches one of the criterion's readings.
  - The other five each have at least one reading recomputed from the traces that falls inside the CI (cells 76–88).
- **table1-comparable-to-published (reproduced):** I agree.
- **Six stimulation claims (blocked):** I agree. The partial results on 4 rats are stated, and the cell 99 numbers support them.
- **Six histology, c-Fos and post-mortem claims (blocked):** I agree.

## 2. Text against outputs

Nearly every number in the "**Result:**" cells, the Summary, the README and the record's notes matches the printed outputs. The exceptions:

- **README:** "four are run; the outcomes are the same under each". This is false for anes-ecap-recorded, where the `window` rule gives 2 of 5 (cell 34). The Summary (cell 104) words it correctly: it lists only the latency, velocity, threshold-order, one-rat and awake outcomes as invariant.
- **Record, data_missing finding:** "Twelve of the claims cannot be tested". The record has 14 `data_missing` outcomes. The claims that this finding itself names come to 13.
- **Record, table1-minimum-pressure notes and the derivative finding:**
  - The notes say "The dataset's own R notebook output gives the same 11.741".
  - The finding says "the dataset's own R notebook output from it, do not give Table 1's means".
  - The R notebook (`cystometry-analysis.nb.html`) is never read or printed.
  - The same applies to "as the dataset's R code does" in cell 71 and in the table1-contraction-duration notes, because `cystometry-analysis.rmd` is not printed either.
- **Cell 104, Summary:** "while minimum and threshold pressure depend on how the minimum is taken". This holds only for threshold reading (a). Reading (b), threshold at the start of the HFPOs, is outside the CI under both ways of taking the minimum: 16.07 and 13.98 mmHg (cell 79).
- **Cell 57 and the awake-ecap-latencies notes:** "the velocities (1.59, 0.88 and 0.57 m/s) are not [within tolerance] … none both". This depends on averaging the velocity of each recording.
  - The claims file notes that the paper's printed velocities are 2.85 mm divided by the printed mean latencies.
  - Computed that way, the cell 56 means 2.142, 3.699 and 5.283 ms give 1.33, 0.77 and 0.54 m/s. All three are within tolerance, so all six values pass in that row.
  - The outcome does not change, because the three-peaks condition still fails. But the notes should say that the "none both" result depends on how velocity is averaged.

The record's verification section states my round-1 reasons faithfully and in my own words. Problems 1–10 and the section C items are attached to the right claims or summarised under `reviewed`.

## 3. Round-1 points

- **Resolved:**
  - 1: four peak rules are run, and the overlay figure is in cell 32.
  - 2: the noise simulation and the variant Friedman and Dunn tests are in the notebook.
  - 3: the narrow pass is now stated.
  - 4: the 0 mA assumption is now stated.
  - 5: stimulus-level reading (b) is fixed.
  - 6: the partial tests are run and the /Voids schema is printed.
  - 8: the between-train null is added.
  - 9: subjects.xlsx is printed in full.
  - 10: the n mismatch is commented on.
  - Section C: the time origin, gain and polarity are now printed or run as variants. The data cannot settle the first two.
- **Mostly resolved:** 7. Table 1 is now recomputed from the traces. What is left is table1-hfpo-frequency, which should be marked as assumed (section 1).

Still open and bearing on a conclusion:

1. Mark table1-hfpo-frequency `assumed: true`, or state that its pass rests only on a derivative value whose method is unstated, from 7 rats.
2. Correct the README sentence about the peak rules, since anes-ecap-recorded depends on the rule.
3. Fix the count of untestable claims in the record ("Twelve").
4. Print the R notebook output and code, or remove the statements that rest on them.
5. State in the awake-ecap-latencies notes that the velocity result depends on how velocity is averaged.
