**Verifier report, round 1: Ocagli et al. 2024 (doi:10.1038/s41597-024-04294-w), Figshare 26877211 v1**

The claims file has nine claims. My outcomes: four reproduced, two partially reproduced, one not reproduced, one blocked, and one partially reproduced with its portal part blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| data-records-rows | reproduced | Cell 18: `jecfa.rds` has 6552 rows and all 17 Table 1 fields. `JECFA.csv` is the same table, with 0 differing cells (cell 5). |
| unique-pages | reproduced | Cell 20: readings D2 and D3 both give 6550, within 2 of 6549. Page 6316's chemical appears twice, at pages 6316 and 6319. Page 5883 is the TEST row (cell 15). |
| table1-availability | reproduced | Cell 22: 16 of 17 fields are within tolerance using the deposited `fas`, and 17 of 17 after the `add_metadata.R` step. The criterion needs 15. Only 12 of 17 match Table 1 when rounded to whole numbers; the five that differ are chemical names, synonyms, report, report sourcelink and FAS. |
| table2-evaluation-year | reproduced | Cell 24: the bin counts are 2357, 3099, 778 and 200, with 118 unknown. All match exactly, and the shares (36.63, 48.17, 12.09, 3.11%) are within tolerance. |
| table2-functional-class | reproduced | Cell 26: the counts are 4635, 1453, 77 and 277, with 110 unknown, all exact. All shares are within tolerance, and flavouring agents are the largest class. |
| unknowns-name-only | not_reproduced | Cell 28: only 86.4% (95 of 110) of unknown-class rows and 80.5% (95 of 118) of unknown-year rows are name-only. Both are below the criterion's 90%, and the criterion has no partial level. The statement holds exactly only for the 95 rows that are unknown on both class and year. |
| fas-codes | partially_reproduced | Cell 30: the named seven codes cover 46.34% of all rows (F1) under both FAS readings, and 53.42% of rows with a code (F2) after the `add_metadata.R` step. Both are within 5 points of 50%. The named seven are not the seven most frequent: 59 (or 60 after the `add_metadata.R` step) ranks above 52, which ranks 9th or 10th. |
| validation-failures | blocked (data_missing) | The claim needs the manual REDCap extraction of 700 pages. I queried the Figshare API: version 1 is the only version and holds only `jecfa.rds` and `JECFA.csv`. No part can be tested from the deposit. |
| portal-search-count | partially_reproduced; portal part blocked (data_missing) | Cell 33: 6552 rows have a JECFA name, within 655 of 6551. After cleaning (D2/D3) the count is 6550, which is 3 from 6547 and outside the claims file's margin of 2. The portal's 6547 is outside data and cannot be tested. |

### B. Problems

1. **[affects a conclusion]** Cell 30, fas-codes, "almost all 85". The 81 distinct codes under the deposited column include junk strings: `'617'`, five decimals such as `'24.65'`, and eight of the form `'77 JECFA 86'`. They also include `'86'`, which is above 85.
   - Counting only integer codes from 1 to 85, I get 66 using the deposited `fas` and 71 after the `add_metadata.R` step (73 distinct values there).
   - Both are below the ≥77 threshold, so the "almost all 85" part fails under any cleaned reading.
   - The outcome stays partial, but the notebook's "at least 77: True" should not be read as support for that part.
2. **[does not affect a conclusion]** Cell 22, table1-availability, FAS. Under reading E (empty strings count as absent), FAS is 81.38%, outside tolerance. The paper's 93% equals the share of non-NA `fas` values (92.86%), which is the same as Tox monograph presence. So the paper probably counted the 752 empty strings as present. The notebook prints this as a variant but draws no conclusion from it. The outcome is unchanged because 16 of 17 fields are still within tolerance.
3. **[does not affect a conclusion]** Cell 33, portal-search-count. The variant in cell 20 that drops both rows of page 6316's chemical gives 6549, which is within 2 of 6547. That reading is not D1–D3 in the claims file, so I did not use it.
   - The dataset has 6552 rows with a name, while the paper says 6551. The notebook does not explain the one-row gap (the TEST page carries the name "TEST").
4. **[does not affect a conclusion]** Cell 24 compares counts against `round(expected*0.1)` instead of the claims file's tolerances. These happen to be the same values, and all counts match exactly anyway.
5. **[does not affect a conclusion]** Claims-file reading, unknowns-name-only. The paper's sentence fits the 95 rows that have neither class nor year. The 90% threshold applied to each set separately was chosen by the claims file, and the claim fails because of that choice. I am reporting this, not correcting it.
6. **Helper functions: no problem found.** I tested `fas_process_df`, `fas_add_metadata`, `tox_abbr`, `year_bin`, `leading_class` and `present` on synthetic inputs. Each behaves as its docstring says, including bin edges, the `">` prefix, `See FAS 74`, cutting `77 JECFA 86` to `77`, and blank-string handling. Cell 11 also confirms that the deposited `fas` equals the `process_df.R` derivation in every row.

### C. What I could not check

- **The R code at commit 2d8a5340.** It was not available to me, so I could not confirm that `fas_add_metadata` and `tox_abbr` port it faithfully. A cell showing the R source lines next to the Python port would have allowed this.
- **Distinct FAS codes from 1 to 85.** The notebook does not print this count under either FAS reading. A cell with that count, and the list of codes that are missing, would have tested "almost all 85" directly.
- **The 15 unknown-class rows and 23 unknown-year rows that are not name-only.** The notebook does not print their page ids. I could not check whether they are clustered (for example, recent pages) or whether they are scraping artefacts.
