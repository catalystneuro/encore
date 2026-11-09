**Verifier report, round 2: Ocagli et al. 2024 (doi:10.1038/s41597-024-04294-w), Figshare 26877211 v1**

The claims file has nine claims, and the attempt record has nine outcomes: five reproduced, one not reproduced, two partially reproduced and one blocked (data_missing). Cell numbers below are those of the re-executed notebook. Three cells were added, so every cell from the old cell 13 onward is 3 higher than in my round-1 report.

### 1. Outcomes

| Claim | Agree | Note |
|---|---|---|
| data-records-rows | yes | Cell 20: 6552 rows, 17 of 17 fields, 0 differing cells. |
| unique-pages | yes | Cell 23: D2 and D3 give 6550. Page 6316's chemical has 2 rows, at pages 6316 and 6319. |
| table1-availability | yes | Cell 26: 16 of 17 fields within tolerance under A, 17 of 17 under B. |
| table2-evaluation-year | yes | Cell 29: all counts exact and all shares within tolerance. Counts are now tested against the claims file's tolerances. |
| table2-functional-class | yes | Cell 32: all counts exact, shares within tolerance, flavouring agents the largest class. |
| unknowns-name-only | yes | Cell 35: 86.4% and 80.5%, both below 90%. The criterion has no partial level. |
| fas-codes | yes | Cell 38: F1 is 46.34% under both readings. The named seven are not the seven most frequent. |
| validation-failures | yes | Blocked, data_missing. |
| portal-search-count | **no** (I changed my view since round 1, see below) | Cell 42: of the dataset's two conditions, 6552 against 6551 holds, but the cleaned count of 6550 is 3 from 6547, outside the margin of 2. |

- **portal-search-count.** The criterion says only when the dataset's part is reproduced. For unknowns-name-only the record reads that kind of criterion as "not reproduced when not met". Here it records "partially reproduced" for the same situation. The condition that holds (6552 within 655 of 6551) is the loose one; the condition that fails ("aligns", within 2) is what the claim says. Applied consistently, the dataset's part is not reproduced, with the portal part blocked. I accepted "partially reproduced" in round 1, and I now think that was wrong. The choice of a partial level here is an assumption that the record does not state.
- **Assumptions.** No outcome carries `assumed: true`. The only outcome that rests on an unstated choice is portal-search-count, as above. The record names the readings it uses for the other outcomes (A/B, D1–D3, F1/F2), and they are reasonable.

### 2. Sentences the printed outputs do not support

- **Cell 24, and the unique-pages notes in the record:** "The paper's 6549 is reached only by removing both rows of that chemical with the test page." Cell 23 tests only that one variant. "only" is not shown; "for example" is.
- **Cell 39, and the fas-codes notes in the record:** "FAS 59 (351 rows) is more frequent than FAS 52 (286)". This is true but leaves out FAS 54, which also ranks above 52 under both readings (287 rows, rank 8 in cell 38). The ranks the record gives (9 under A, 10 under B) are correct.
- **Cell 27:** "under it FAS is the one field outside tolerance". Under reading E this holds for reading A only; under B no field is outside (cell 26).
- **Record, finding "other":** "33 FEMA numbers have trailing spaces". Cell 9 prints 33 FEMA values that are not plain integers and shows only four examples, all with trailing spaces. It does not show that all 33 are trailing spaces.
- **Record, data-records-rows notes:** "in the order that function selects them". Cell 13 cuts `process_df` before its rename and select, so the outputs do not show this order. I did not count this as a numerical problem.

Everything else checks against the outputs:

- the conclusions in cells 21, 24, 27, 30, 33, 36, 39 and 43;
- the Summary (cell 44);
- the README;
- the record's notes and findings.

Examples of checked figures:

- the 355 empty-string rows that are FAS monographs (339 + 10 + 2 + 4) and the 277 "NOT PREPARED", in cell 11;
- the counts of 66 and 71 whole-number codes, the 15 malformed values under A and the 2 under B, and the list of the 14 codes missing under both readings, in cell 38;
- 13 of the 15 unknown-class rows on pages 6385 to 6450 and 11 of the 23 unknown-year rows on pages 6476 to 6533, in cell 35;
- 6551 rows with a JECFA name other than TEST, in cell 42;
- the shift of at most 0.05 points after cleaning, in cell 26.

**My round-1 reasons in the record.** They are in my own words and match my report, with points from Problems and from "What I could not check" merged into the reasons of the claims they concern. Two small omissions:

- table1-availability does not name the five fields that differ when rounded.
- My round-1 point about the R source (C1) is not attached to any claim's reason. The `reviewed` field cites the report, and cell 13 answers the point.

### 3. Round-1 points

- B1, "almost all 85": resolved (cells 38–39).
- B2, FAS under reading E: resolved (cell 27).
- B3, the one-row gap and the 6549 variant: resolved. Cell 43 says the data do not explain the gap.
- B4, tolerances: resolved (cells 29 and 32).
- B5, the claims file's reading of unknowns-name-only: resolved. The outcome is now not reproduced, and the reading is passed to a reader as a question.
- C1, the R source: resolved. Cell 13 prints the R next to the ports. I checked `fas_process_df`, `tox_abbr` and `fas_add_metadata` against it: same order of steps, same handling of NA, and the same `nchar > 3` cut. The one difference is R's `strsplit("")` returning `character(0)`, which the author already notes in cell 14. In R that value would become NA instead of "NOT A FAS", but `case_when` then falls through to the same FAS value, so the result does not change.
- C2, distinct codes from 1 to 85: resolved (cell 38).
- C3, the unknown rows that are not name-only: resolved (cell 35).

**Remaining point that bears on a conclusion:**

- **portal-search-count.** The outcome is not consistent with the rule the record applies to unknowns-name-only. Its dataset part fails the criterion's "aligns" condition (6550 against 6547, outside 2). It should be not reproduced, with the portal part blocked, or the partial level should be stated as an assumption. The README and the Summary carry the same outcome.
