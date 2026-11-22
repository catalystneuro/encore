**Round 2 verification: Gable et al. 2026 (attempt gable-2026-01)**

**1. Outcomes**

The claims file has 34 claims, and the attempt record has 34 outcomes: 31 blocked, 1 not_reproduced and 2 partially_reproduced.

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| figs4-session-selection | not_reproduced | Yes. No reading reaches 11 mice (cell 15). | None. |
| figs4-lowest-couplers-correlated | partially_reproduced, assumed | Yes | Stated. The stated basis (keep duplicated rows) is not reasonable; see the next row. The outcome holds without it, though. It is partial under 15 of 16 readings, and the one exception (bba, 0.0548) sits at the tolerance edge of 0.054. Bin 1 holds no duplicate pairs (cell 22). I would rest the outcome on that. |
| figs4-high-couplers-correlated | partially_reproduced, assumed | **No** | Stated, not reasonable. Explained below the table. |
| figs4-middle-couplers-not-correlated | blocked, methods_underspecified | Yes | None. With every row kept it turns on O2 (cell 33). With units counted once it turns on O3: baa gives reproduced, bab does not. It is blocked either way. |
| 30 imaging claims | blocked, data_missing | Yes | None. |

Why I disagree on figs4-high-couplers-correlated:
- **The record's own finding says the reading is wrong.** The adopted reading `baa-r` keeps every stored row, so each duplicated unit is analysed as two units. Finding 1, rated critical, states that an analysis treating each row as a unit counts the unit twice.
- **The notebook says the same.** Cell 18: "The duplicated rows are not distinct neurons."
- **Units counted once give not reproduced.** Seven of 8 readings give not reproduced, and the bin 5 Holm p is 0.074 to 0.53 (cell 29). The one exception, bab, has bins 5 and 6 at 0.012 and 0.019, both far outside tolerance.
- **Keeping the rows moves the duplicated units.** Counted once, 4 of 12 sit in bins 1 and 2. With the rows kept, they move to bins 5 to 7 (cell 22).
- **The basis is circular.** "Only then does a third Tlx mouse enter" picks the reading by matching the claim's expected count. That mouse enters only because two copied rows pad 16 units to 18.
- **What the outcome should be.** I would rate it not_reproduced. If the attempt treats the paper's handling of duplicates as open, which its methods_unavailable question implies, then its own rule makes the claim blocked. In neither case is it partial.
- **The paper may have kept the duplicates too.** The record does not say this. Under `baa-r` the bin 5 and bin 7 values (0.026 and 0.130) sit nearer the code's printed 0.0188 and 0.122 than under `baa` (0.008 and 0.067) (cell 25). If so, the paper's own high-coupler result may be inflated by these pairs. That is worth stating, but it does not justify adopting the reading.

**2. Sentences the outputs do not support**

1. **Cell 6:** "Units are counted once here." The notebook adopts every stored row (cells 10 and 18).
2. **Cell 13:** "In the sessions with a laser trace, every photostimulation onset has laser power." Cell 12 shows sub-219248 ses-20130919 with 122 onsets, of which 121 have power above 1. It also shows sub-219036 ses-20131120 with one powered trial that has no onset.
3. **Summary (cell 36):** "photostimulation onsets agree with the stored laser trace in the selected sessions that have one." Same exceptions as item 2.
4. **Summary (cell 36):** "puts these units … mostly in the top coupling bin." Only the 14 duplicated units in selected sessions were checked (cell 22), not all 72.
5. **Finding 8 (severity none):** "Photostimulation onsets agree with the stored laser power trace in the 13 selected sessions checked." Cell 12 lists 17 sessions, and 10 of them have a trace. The agreement is not exact (item 2).
6. **Finding 11:** "the other mice's files of the same strains hold all three." In cell 12, sub-210862 ses-20130626 and sub-210863 ses-20130626 and ses-20130628 (KJ18, not Ai32) have optogenetics metadata but no laser trace and no onsets.
7. **Finding 1:** "12 of the 14 duplicated units … fall in the top coupling bin, which changes whether the 57.14 to 71.43% bin is significant." Bin 5 holds only 1 duplicate pair (cell 22). What changes bin 5 is the shift in bin edges and membership, plus the added sub-218453 session. The causal link is not shown.
8. **Finding 5:** "in the 16 sessions analysed one photostimulation onset is NaN." Cell 3 prints NaN events per file without the event type, so the type is not shown. The count of 16 is `baa`, not the adopted 17 sessions of `baa-r`.

Everything else checks against the outputs: the Result cells 17, 27, 31 and 34, the README, and the outcome notes. The record's numbers match cells 15, 16, 22, 25, 29, 30 and 33. That includes 10/17/575/5,686, the range 0.032 to 0.055, the per-mouse 7/9, 9/9 and 7/7, the 8-to-8 split, and the maximum middle difference of 0.0084.

The attempt record states my round-1 reasons faithfully. For Problem 5 it leaves out two parts: the rejection rate is about 5% with session offsets, and the acceptance rule biases the mean toward large sessions (0.046 against 0.039). The record also reads my Problem 2 as support for adopting the duplicated rows. I raised the reading only because it had not been tested; I did not propose it as the analysis.

**3. Round-1 points**

- **Resolved:**
  - Problem 1: every reading is now shown, and the middle claim is blocked.
  - Problem 3: the per-mouse table is added (cell 16).
  - Problem 6: trial types are now printed.
  - The tests under "every stored row" and the location of the duplicates: cells 22 and 29.
- **Problem 2: resolved as asked, but the response adopts the defect.** This now decides the high-coupler outcome. It also contradicts the record's critical finding 1. This bears on a conclusion.
- **Problem 4: partly resolved.** The Ai32 sessions are confirmed to hold no laser data. The three non-Ai32 KJ18 sessions without a trace are not discussed (item 6 above).
- **Problem 5:** noted, in part (see section 2).
- **Remaining, bearing on a conclusion:**
  - The high-coupler outcome (section 1).
  - The stated basis for the lowest-coupler outcome should be the 15 of 16 readings, not the duplicated rows.

**4. Critical findings**

Finding 1 is the only one rated critical. It reads: 50 of 99 files repeat a unit id, and the repeated rows hold identical spike trains.
- **Shown by the outputs:** yes for the core statement. Cell 5 prints 50 of 99 files, 72 extra rows, all with identical spike trains, and the example ids 3, 4, 4, 5, 5. Cell 15 shows the selection effect: 9 against 10 mice, 15–16 against 17–18 sessions. Cell 22 shows 12 of 14 duplicated units in the top bin at r = 1. The causal clause about bin 5 is not shown (section 2, item 7).
- **Rating: critical is right.** One unit deposited as two rows is one of the rubric's examples. The repeated id is the only trace, it is easy to miss when the units table is read as stored, and an analysis that reads the table as stored comes out wrong. This attempt's adopted reading is an example.

No other finding is rated critical.
