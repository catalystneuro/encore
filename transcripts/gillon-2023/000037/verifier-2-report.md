# Round 2 verifier report: 000037-gillon-2023-01

## 1. Outcomes

The claims file has 35 claims, and the attempt record gives an outcome for each of the 35.

**I agree with 33 of 35 outcomes.** These are the 33 that are not fig5-consistent-vs-inconsistent or fig7c-high-correlation-fraction. The numbers behind them have not changed since round 1. In cell 63, gabor-sequence-structure is still `partially_reproduced`: 46 of 50 sessions pass, with 13 of 340000 images out of range. The record now says that a strict two-way reading would give `not_reproduced`.

**I disagree with 2 of 35, as in round 1:**
- **fig5-consistent-vs-inconsistent** (record: `blocked`; my outcome: `partially_reproduced`). Cell 80 gives scaled 2/4 under (a) and 3/4 under (b), and unscaled 2/4 under each. Both readings give partial, so the readings agree. The only reason for the block is the claims file's `depends_on`.
- **fig7c-high-correlation-fraction** (record: `blocked`; my outcome: `not_reproduced`). Cell 92 gives (a) 0.0178% (134 of 752101 pairs), (b) 0.0176%, and (c) 0.0211, 0.0276 and 0.0043% by session. None is inside 0.005–0.015%, and none depends on how "similar" is read.

The author keeps both blocks under protocol author step 1.5. I cannot read `docs/protocol.md`. If the rule is as the author states it, the blocks follow procedure. The disagreement and the outcomes each claim's own test gives are recorded in the attempt record, the notebook (cells 81 and 93) and the README.

## 2. Statements the printed outputs do not support

Nearly every number I checked matches the printed output, with one figure that does not: the run time (item 3). The exceptions are below.

1. **The start times are called "evening" (cell 30; attempt record table2-sessions notes).**
   - Cell 30: "Their start times are evening Pacific times stated with a Pacific offset (for example 2018-10-19T00:18-07:00)".
   - Attempt record: "Their start times are evening Pacific clock values stated with a Pacific offset".
   - Cells 6 and 29 print 00:18, 01:51, 03:01 and 01:06 with offsets of -07:00 or -08:00. As stated, these are early-morning Pacific times. They become evening Pacific times only if the clock is read as UTC, which is the variant the text says it does not adopt. The sentence assumes the reading it then calls not decisive.
2. **Supplementary Table 1's notes are cited but never printed (cell 63, gabor notes, finding 7).**
   - Cell 63: "Supplementary Table 1 notes dropped stimulus frames for them".
   - Cell 13 and finding 7: "Supplementary Table 1 notes the laser was set to 800 nm" and "failed QC with the laser at 800 nm".
   - No cell prints that table's notes column. Cell 8 prints an excitation of 910 nm for every file, 838633305 included. These sentences may be true, but nothing in the outputs shows them.
3. **The run time (README and cell 0).** Both say "takes about seven minutes". Cell 2 prints 664 s, which is about 11 minutes.
4. **The clock check in finding 7.** The finding says the dF/F response in two sessions "does not exceed that at shifted times". Cell 12 shows that 777496949 exceeds 94.6% of the shifted contrasts (rank 0.054) and only fails the 99th-percentile test. Cell 13 states this correctly; the finding overstates it.
5. **Running speed (cell 9, data check, not a conclusion).** The cell describes "a median near a few cm/s". Cell 8 prints a median of 0.081 cm/s across the session medians.

Everything else I checked agrees with the outputs:
- every other `**Result:` sentence: cells 18–102;
- the Summary table and its findings: cell 103;
- the README table and text;
- the other notes in the attempt record.

The record's round-1 entry gives my reasons faithfully, folding problems 3, 4, 6, 7 and 9 and the section C items into the relevant claims. Most of it is close to verbatim. Nothing material is left out or changed.

## 3. Round-1 points

| # | Point | Status |
|---|---|---|
| 1 | fig5-consistent-vs-inconsistent blocked only by dependency | **Not resolved.** The block is kept by procedure. The planes where both readings hold at once are now printed: 1 of 4, L5 dendrites (cell 80). Bears on a conclusion. |
| 2 | fig7c-high-correlation-fraction blocked only by dependency | **Not resolved**, for the same reason. Bears on a conclusion. |
| 3 | The UTC variant and the truncated start string in table2-sessions | **Resolved.** Start times are printed in full (cells 6 and 29). All time and date fields of the four files are printed, and the UTC reading is labelled a variant that does not decide the outcome. The "evening" wording (item 2.1) is new. |
| 4 | SNR > 1 holds by how SNR is built | **Resolved.** Cells 86 and 87 print 0 ROIs with a negative median. |
| 5 | Over-long Gabor images | **Resolved** as far as wording goes (cell 63). The "dropped frames" source is not shown (item 2.2). |
| 6 | QC search too narrow | **Resolved.** Cell 32 searches all 23 fields in every file; there are no matches, and all fields of 759666166 are printed. |
| 7 | Alignment of 777496949 | **Resolved.** Cell 98 prints 4.07 SEM at onset and 6.77 at offset next to the clock check. |
| 8 | Supplementary Table 1 against Tables 1 and 2, not run | Unchanged. Does not bear on a conclusion. |
| 9 | No assert on dropped transitions | **Resolved.** `openscope_ca.py:447` asserts that `dropped == 0`. |
| C | Fig. 5 thresholds | **Resolved.** Printed in cell 77. The comparison with the repository's Fig. 5 source data was not added, so the ROI selection is still checked only on synthetic inputs. |

**Still open and bearing on a conclusion:**
- **Points 1 and 2.** These are the outcomes of fig5-consistent-vs-inconsistent (`partially_reproduced` by its own test) and fig7c-high-correlation-fraction (`not_reproduced` by its own test). They stay blocked under a protocol rule I cannot check.

**Still open, not changing an outcome:**
- **Item 2.1, the "evening" wording.** It sits in table2-sessions, whose outcome is `not_reproduced` either way.
