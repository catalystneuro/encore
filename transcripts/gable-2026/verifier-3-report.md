**Round 3 verification: Gable et al. 2026 (attempt gable-2026-01)**

The claims file has 34 claims and the attempt record has 34 outcomes. Two outcomes carry a proposed change, and I agree with both.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs4-lowest-couplers-correlated | blocked (methods_underspecified) | Yes | — | Cell 25: bin 1 is positive with Holm p = 0.0007 under all 16 readings and all 5 seeds. The only open question is whether the difference is within 0.054 to 0.066. Under `bba` it is 0.0548, and it stays inside tolerance under every seed (0.0546 to 0.0548), so `bba` gives reproduced. `baa`, `bab` and `bbb` give partially reproduced (0.048, 0.044, 0.047). `baa` and `bba` differ only in O2. |
| figs4-high-couplers-correlated | blocked (methods_underspecified) | Yes | — | Cell 29: with units counted once and O1 (b), `baa`, `bba` and `bbb` give not reproduced, because bin 5 is not significant (Holm p 0.066 to 0.090, 0.53 to 0.55, 0.20 to 0.22 across seeds). `bab` has all three bins significant under every seed (bin 5 p 0.0007 to 0.0008) with only bin 7 within tolerance. The criterion's first partial clause gives partially reproduced for that. `baa` and `bab` differ only in O3. |

**Checks behind the lowest-coupler row**
- The numbers come from the data. The table in cell 25 matches the notes in the record and cell 27.
- The outcome code in cell 25 applies the criterion as written: tolerance is |md − 0.06| ≤ 0.006, and significance is Holm p < 0.05.
- The claims file says a claim's outcome is the one all readings give, and it lists both O2 readings as allowed. So the split means blocked.
- Blocked holds under several framings:
  - the four readings with units counted once and O1 (b), which the attempt adopts;
  - all 8 readings with units counted once;
  - all 16 readings.
- With every stored row kept, all eight readings give partially reproduced. That reading is the one I found unreasonable in round 2, so it does not decide the outcome.
- In round 2 I agreed with partially reproduced and would have rested it on 15 of 16 readings. That did not apply the claims file's rule as written, and I withdraw it.
- Nothing about the choice of reading pushes toward a better result: blocked is less favourable than either outcome in the split.

**Checks behind the high-coupler row**
- The outcome code in cell 29 applies both partial clauses as written.
- O3 (a) has some support, since TSA is defined on the four trial types. But the claims file lists (b) as an allowed reading. The claims file's rule therefore blocks the claim, the same way figs4-middle-couplers-not-correlated is blocked (cell 33).
- The blocked outcome does not depend on how duplicated rows are handled. With every stored row kept, the readings also split: seven give partially reproduced and `abb-r` gives not reproduced.
- In round 2 I said not reproduced, or blocked if the handling of duplicates is open. Bringing O3 in under units counted once shows that blocked follows even with that handling settled.
- Under `bab` the result is substantively weak. Bin 5 is 0.012 against 0.015 to 0.025, and bin 6 is 0.019 against 0.054 to 0.066. Bin 6 is below tolerance under all 16 readings (0.014 to 0.035). Even so, the criterion as written gives partial there.
- The basis no longer adopts the duplicated rows, so the circularity I raised in round 2 is gone.

**On the claims file:** I found no misreading of the paper. As written, its every-reading rule lets a value 0.0006 inside the tolerance edge (`bba`, lowest bin) block a claim whose effect is significant under every reading. Likewise, partially reproduced under `bab` is set by the significance of bin 5 alone. That is how the claims file was written, not an error in applying it.
