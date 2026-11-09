**Round 2 verification: Mintal et al. (2024), Figshare 24949470 v1**

**1. Outcomes**

The claims file has 18 claims, and the attempt record gives an outcome for each of the 18: 12 reproduced, 4 partially reproduced and 2 blocked. I agree with all 18.

| Claim | Record | Agree | Note |
|---|---|---|---|
| user-responses-count | reproduced | yes | Cells 3 and 11. |
| collection-window | partially_reproduced | yes | Cell 14: 432 rows under reading (a) and 494 under (b) fall after the window. |
| party-positions-structure | reproduced | yes | Cell 17. |
| eleven-parties | reproduced | yes | Cell 20. |
| party-self-placements | reproduced | yes | Cell 23. |
| coder-agreement-kappa | reproduced, assumed | yes | The assumption (quadratic weights, "No opinion" pairs left out) is stated. It is reasonable, but it was chosen because it is the one reading of four that gives 0.84, and the record says so. It is also put to the authors as a finding. |
| uni-and-landscape-placements | partially_reproduced | yes | Cell 29: under reading (ii) 6 of 7 axes match. PS on the economic axis is 47.7 against 54.5. |
| party-clustering | reproduced | yes | Cell 33: 9 of 9 clusters, no extra ones. |
| table2-gender, -age, -education | reproduced | yes | Cells 36 and 37. |
| age-education-inconsistencies | partially_reproduced | yes | Cell 42: the 18–20 count (378) is within tolerance; the under-18 count (25 to 34) never is. |
| s2-s3-wide-range | reproduced | yes | Cell 45, reading (a). |
| s4-s5-consensus | reproduced | yes | Cell 45, reading (a). |
| efa-eleven-factors | reproduced | yes | Cells 51 and 53. Under psych's defaults it holds under reading (a) only, which the record states. |
| efa-loadings-consistent | partially_reproduced, assumed | yes | Cell 56: 35 of 39 match on Pearson, 32 of 39 on polychoric. The assumption (the claims file's thresholds) is stated and reasonable. |
| selected-parties-top-vote | blocked (other) | yes | |
| website-views | blocked (other) | yes | |

For the two blocked claims, the author answers my round-1 `data_missing` by saying the protocol does not allow `data_missing` for claims whose data is held elsewhere. docs/protocol.md is not among my materials, so I accept that explanation without having checked it.

No other outcome rests on an unstated assumption. The figure readings are recorded under `inputs`, not as an assumption, which is appropriate.

**2. Sentences the outputs do not support**

- **Cell 15, and the collection-window notes:** "The first row of the file, the sample of Table 1, is one of the late rows." No output shows the row order. Cell 3 prints only the earliest and latest timestamps.
- **Cell 15:** "Under both readings the timestamps … cover all 26 days." Cell 14 prints the 26-day count only for timestamps as given.
- **Cell 15, the collection-window notes, and the third finding:** "The R code's optional filter … would drop 461 rows." The 461 is counted on the raw rows. The printed R code (cell 7, line 375) applies the filter to `data_cleaned_corrected`, and no count on those rows is printed.
- **Cell 15 and the collection-window notes:** "so the code reads TIME.STAMP as local time (reading a)". Cell 7 shows the code parses TIME.STAMP with `tz = "UTC"` (lines 377, 380 and 381), and the comment gives "22:45" with no time zone. This is an inference, which I made too in round 1, and the printed code partly cuts against it. It does not change the outcome, since the claim fails under both readings.
- **Record, efa-eleven-factors notes:** "While preparing, a looser optimiser tolerance gave 12 for reading (a) Pearson with the defaults (not run here), so the 12th value is close to its reference under minres." This is not in the notebook. It also conflicts with cell 51, where the 12th value under reading (a), Pearson, defaults is 0.0042 against a reference of 0.0117, so not close. If an optimiser setting can change this count, that bears on the outcome and should be shown. Otherwise the sentence should go.
- **Record, age-education-inconsistencies notes:** "The paper says the discrepancies were found 'upon initial review'". The paper (Structural validation, paragraph 3) says that "upon initial review" the team broadened the acceptable age range for a university degree to include 21–24, and then reports the 40 and 400. I made the same misreading in round 1 (problem 8). The rest of that note ("acknowledged during further data curation and refinement of the data collection tool") is accurate.
- **Record, uni-and-landscape-placements notes:** "No reading of the economic statements tried while preparing (leaving out statement 10 or 21) explains it". This is not in the notebook. The record says so, but the sentence is still unsupported by any output.
- **README:** "Reproduced (assumed quadratic weights)" leaves out the second part of the assumption, "No opinion" left out, which the Summary (cell 58) and the record both state.

Every other sentence in the Result conclusions (cells 12 to 57), the Summary (cell 58), the README and the record's notes and findings matches the printed numbers.

The record states my round-1 reasons accurately and in substance in my words. Each numbered problem is attached to the claim it bears on: 1 and 5 to the placements, 1 to the clustering, 2 to the age–education and factor claims, 3 and 4 to efa-eleven-factors, 6 to the party positions, 7 to the response count, and 8 and 9 to the age–education and window claims. The "18 of 2,074" in the problem 4 reason is my own round-1 figure; cell 51 now gives 18 of 2,040 reference fits.

**3. Round-1 points**

Resolved:
- **2 (R code not shown):** cell 7 prints the relevant lines. The `validator` rules check only that each field takes a valid category, and no rule relates age to education.
- **3 (polychoric reference):** cell 53 adds a reference built from resampled data. It gives 11 again (0.0103 against 0.0143, s.d. 0.0009).
- **4 (convergence):** cell 51 shows 0 of 12 fits on observed matrices failed, and cell 53 shows 0 of 40 on resampled data. All 18 failures are on simulated reference matrices.
- **5 (discordant pairs):** fixed in cell 29. Reading (ii) now flags only DEMOKRATI/PS.
- **6 (workbook numbering):** recorded as a metadata_error finding.
- **7 (MD5):** cell 3 now checks all 8 files against the archive, and all match.

Partly resolved: **1 (figure readings).** The readings were redone blind, by pixel position, with the axis calibration printed. The explanation that Fig. 2 places parties at whole percentages fits the output: every one of the 55 Fig. 2 values equals the computed score cut to an integer. The Fig. 7 heights match within 1, which is under one pixel (4.18 per pixel), consistent with the stated ±3. I still cannot check the readings against the images, and the registry refuses an overlay.

Still open and bearing on a conclusion:
- **uni-and-landscape-placements and party-clustering:** both outcomes still rest entirely on figure readings that cannot be checked from the materials.
- **efa-eleven-factors:** the unshown statement that an optimiser tolerance gives 12 under reading (a), Pearson, defaults (section 2) needs to be shown or withdrawn.
- **age-education-inconsistencies:** point 8, that the 40 and 400 may describe an earlier state of the data, is now a question for a reader. The claim is unchanged, so the partial outcome may reflect this and not the deposited data. The misquotation in the notes (section 2) should be corrected.
- **coder-agreement-kappa:** the outcome depends on a reading chosen because it gives the reported value. It is stated and put to the authors, but it is unresolved until they answer.
- **collection-window (point 9):** carried into the conclusion, but see the `tz = "UTC"` point above. It does not change the outcome.

No new misreadings of the paper by the claims file found in this round.
