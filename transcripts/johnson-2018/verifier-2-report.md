**Round 2 verification: Johnson et al. 2018 on CRCNS fcx-2 (attempt crcns-fcx-2-johnson-2018-01)**

Counts from the attempt record: 21 claims. 5 are reproduced, 7 not reproduced and 9 blocked, and 3 outcomes carry `assumed: true`. The summary (cell 60) and the README table agree with these counts.

**1. Outcomes**

| claim | record | agree? | comment |
|---|---|---|---|
| behavior-proficient | reproduced | yes | Cell 18. |
| behavior-no-difficulty-difference | reproduced, assumed | yes, with a reservation | In round 1 I said partially_reproduced, but this criterion has no partial outcome. On reading (c) the `summary_file.csv` response times give F 2.41, p 0.13; the trial tables give F 12.33, p 0.0015 (cell 21). The assumption is stated and can be defended, since that file's condition means and SDs are the paper's. It is weak, though: 21 of the 30 file values cannot be derived from the trial data (cell 15). |
| electrode-counts | reproduced | yes | |
| correct-trial-counts | reproduced | yes | |
| erp-no-condition-difference | not_reproduced, assumed | yes | One electrode with the subject-wide null; 0 with a per-trial baseline (cell 30). The assumption is stated and follows `erp_compute.m` lines 84–88, quoted in cell 13. Under the per-electrode null of M4 the result is not reproduced whatever the baseline (27 or 22 electrodes), so the outcome depends on the baseline only under the subject-wide null. One significant electrode is about what chance gives across 10 subjects × 2 tests. |
| power-theta-sustained | not_reproduced | yes | Both window placements fail. |
| power-condition-exclusions | not_reproduced | yes | 7 (1 PFC, 4 OFC, 2 MTL) in the table's windows; 12 in the code's windows. |
| plv-theta-peak | reproduced | yes | The one-subject rule is lenient, and the notes say so. |
| psi-theta-shift | not_reproduced, assumed | yes | With sliding windows (M5): table windows fail both parts; code windows give the partial pattern (MTL-OFC raw p 0.027). The outcome rests on the window placement, which is stated. The placement can be defended (see the window-placement section below). |
| crossspectral-shift | not_reproduced | yes | No reading reaches 4 of 7 systems (cell 45). |
| phase-directing-counts | not_reproduced | yes | |
| crossspectral-equal-strength, plus 8 PAC claims | blocked (methods_underspecified) | yes on blocking, label questionable | The trial-shuffle calibration shows the code's PSI form selects 57% of units on shuffled data and 56% on real data (cell 45), so its selection carries no information. Blocking is reasonable. But the Methods' PSI is fully specified, was run, and selects 0 to 3 units per system. The record's own findings call this a code_mismatch, and these claims `depends_on` phase-directing-counts, which is not reproduced. "methods_underspecified" describes the cause poorly. Also, the MTL-OFC network does have 5 sliding-selected pairs, and the model was not attempted on them. |
| theta-peak-bands | not_reproduced | yes | Overlap is 4 of 10 under reading (a). The code-window variant is no longer shown; in round 1 it gave 4 of 10. |

**Window placement.** This is the assumption that matters most. The delay-jitter test (cell 11) separates the two placements for `proc` and `encmain`:
- `proc`: ERPs differ between delay lengths from −0.25 s (p ≤ 0.05) and show nothing from 1.0 to 2.0 s (p 0.29 to 0.94).
- `encmain`: ERPs differ at 0.25 to 1.0 s (p 0.01 three times). The code's placement can explain neither result.
- Caveat: 28 of 108 window tests reach p ≤ 0.05, so isolated hits elsewhere carry little weight.

Two points the record does not address:
- **Edge effects.** The table placement puts the baseline 0.65 to 0.85 s after the segment's first sample and starts encoding at that sample. The low theta filters have FIR orders of about 1 to 2 s (`fir_order`), so baseline and early-encoding theta power sit inside the edge transient. Cell 12 mentions this for encoding only, and it is never measured. It bears on power-theta-sustained and on theta-peak-bands, where 4 subjects peak at the lowest filter (1.5–4 Hz). The outcomes are the same in both placements.
- **Which numbers the paper reports.** If the deposited scripts produced the paper's figures, the paper's numbers come from the code's windows. Running the table placement then tests the claims against the events the Methods describe, but it does not recompute what the paper did. The record should say this when it explains the choice for psi-theta-shift.

**2. Sentences the numbers do not support**

- **Cell 59:** "none of the eight patterns appears under either surrogate reading". This is wrong for pac-mtl-ofc-direction under reading (a). In cell 57 the spatial condition × direction p is 0.00018, below 0.05/15, and the difference is larger for MTL→OFC (0.0064 against −0.0192). That is one part of the criterion's condition (1), which the criterion calls partial. These results are not judged, so no outcome changes, but the sentence should be corrected.
- **Attempt record, psi-theta-shift notes:** "The code's single window gives part (2) for MTL-PFC on raw PSI only … which the criterion calls partial." The criterion allows readings of M1 and M7. M5 fixes sliding windows, so the single window is a variant the criterion does not judge. The numbers themselves are right (cell 42: p 0.014).
- **Attempt record, crossspectral-equal-strength notes:** "(also too few units under the claim's own rule)". No printed output says what this refers to.
- **`fcx2.py` docstring, lines 50–54:** it says the single window "is the main reading and sliding windows … are a variant". The notebook and the record judge on sliding windows, so the docstring is out of date.

Every other "**Result:" sentence, the Summary, the README and the record's notes match the printed outputs. I checked cells 12, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52 and 55, and every number in the record's notes.

The record states my round-1 reasons accurately. Several reasons fold in my B-points (B1, B2, B3, B4, B5, B7); these are fair summaries of what I wrote.

**3. Round-1 points**

Resolved:
- **B1 (time axis):** checked against the data and both placements run. What remains is listed below.
- **B3 (`psi_code` calibration):** confirmed on real data, and the selection dropped. The sliding-window z is too wide (SD 2.3 on shuffled data); this is stated as bearing on part (1).
- **B4:** sliding-window cross-spectral PSI now run.
- **B5:** script quoted, per-trial baseline run as a variant, outcome flagged as assumed.
- **C (deposited scripts):** quoted in cell 13.

Resolved as far as the data allow:
- **B2 (response-time provenance):** searched; 9 of 30 values matched, the rest unexplained, and the dependence is stated.

No longer relevant, because the PAC and equal-strength results are not judged:
- B7 (within-unit F tests are anti-conservative), B8 (own exclusions), B9 (theta band remap). PAC on all units without selection was declined; the record's reason, that it tests a different population, is acceptable.

Still open, not affecting a conclusion:
- B6: frequency-resolved PSI and the other null reading were not run.

**Remaining issues that bear on a conclusion**
1. The window placement decides psi-theta-shift (not reproduced in the table's windows, partial in the code's). Edge effects at the start of the segments under the table placement are not measured. The record does not say that the paper's own numbers would come from the code's windows if the deposited scripts produced them.
2. The behaviour outcome depends on `summary_file.csv`, whose response times for 7 of 10 subjects cannot be derived from the trial tables. With the trial tables the result would be not reproduced.
3. The 9 blocked claims are labelled methods_underspecified, but the cause is a fully specified Methods PSI that selects almost no units, together with a miscalibrated code form. The MTL-OFC equal-strength model was not attempted on the 5 sliding-selected pairs.
