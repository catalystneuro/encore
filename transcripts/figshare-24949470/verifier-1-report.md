**A. Outcomes** (18 claims in the claims file; the notebook tests 16 and treats 2 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| user-responses-count | reproduced | Cell 9: the raw file has 134,699 rows and every Table 1 column. After removing incomplete rows, 133,473 remain. |
| collection-window | partially_reproduced | Cell 11: responses start 2023-09-05 and cover all 26 days of the window. But 432 rows under reading (a) and 494 under (b) fall between 1 and 9 October, so the criterion ("every timestamp" inside the window) fails under both readings. |
| party-positions-structure | reproduced | Cell 13: 429 rows, 39 statements, all three wordings for every statement. The expert, self-placement, final, snippet and link columns are present. |
| eleven-parties | reproduced | Cell 15: 11 parties, each placed on 39 distinct statements. |
| party-self-placements | reproduced | Cell 17: exactly 4 parties self-placed (SaS 39 statements, DEMOKRATI 38, PS 32 agree/disagree only, KDH 22). |
| coder-agreement-kappa | reproduced | Cell 19: quadratic weights with No opinion left out give κ = 0.842 on 266 pairs, inside 0.84 ± 0.084. The other three readings fail (0.620 to 0.745). I recomputed 0.842 (and 0.734 for linear) from the printed crosstab. |
| uni-and-landscape-placements | partially_reproduced | Cell 21: 18 and 16 statements are assigned, as claimed. Under reading (ii) all five uni-dimensions and the cultural axis match the figure order. On the economic axis PS scores 47.7 against 54 read from Fig. 3, which reverses its order against DEMOKRATI (52.3 vs 52). |
| party-clustering | reproduced | Cell 24: reading (a), the recoded CSV, finds all 9 of the 9 Fig. 7 clusters and no extra ones. |
| table2-gender | reproduced | Cells 26–27: readings (a) to (d) all fall within tolerance (largest count difference 2.96%). The R code's cleaning, a variant, matches exactly with a total of 107,965. |
| table2-age | reproduced | Same cells: 9 of 9 counts and both percentages fall within tolerance under every reading. |
| table2-education | reproduced | Same cells: 6 of 6 counts and the 64.41% fall within tolerance under every reading (largest difference 4.44%). |
| age-education-inconsistencies | partially_reproduced | Cell 29: the 18–20 count is 378 (cleaned) or 382 (raw) with university only, inside 400 ± 40. The under-18 count is 25 to 34 under every reading, never inside 40 ± 4. |
| s2-s3-wide-range | reproduced | Cell 31, reading (a): S2 mean 43.77, sd 33.82, median 25; S3 mean 42.09, sd 33.69, median 25. All six are within tolerance. |
| s4-s5-consensus | reproduced | Cell 31, reading (a): all six statistics are within tolerance. The 0-or-25 counts are 17,460 and 23,369, which satisfy both reading (i) and reading (ii). |
| efa-eleven-factors | reproduced | Cell 35, reading (a): 11 factors for Pearson and polychoric, under the default settings and the R-code settings, against both the mean and the 95th-percentile reference. The caveat is problem 3. |
| efa-loadings-consistent | partially_reproduced | Cell 37: on Pearson, readings (a) and (b), S1 and S3 load at 0.50 or more in both solutions and 35 of 39 statements match, so the claim holds under the 0.4 and 0.5 thresholds. On polychoric only 32 of 39 match (lowest congruence 0.36), so consistency fails. The criterion says "matrices", plural, and the thresholds are the claims file's own. |
| selected-parties-top-vote | blocked (data_missing) | The archive's 8 files hold no election results (I checked the Figshare API file list). The dataset side, the 11 party names, is available, so the claim is testable against the Statistical Office's official results. |
| website-views | blocked (data_missing) | The archive holds no platform usage logs (8 files: code, dictionary, README, Supplementary Table 1, responses, party workbook, recoded CSV, census). Responses per day cannot stand in for views. |

**B. Problems**

1. [affects a conclusion] Cells 21 and 24: the expected placements for uni-and-landscape-placements and party-clustering were typed in by the author from Figs. 2, 3 and 7, read by eye. They agree with the computed values far more tightly than the stated reading precision. Fig. 3 is said to be read to ±2 but matches within 0.5 everywhere except PS. Fig. 7 heights are said to be read to ±20 but match within 2.5. Both outcomes rest entirely on these readings, which I cannot verify, and the precision suggests the figures were not read blind to the computed values.
2. [affects a conclusion] Cells 3, 5, 7, 32 and 34: the R code is loaded but only its line count is printed. The notebook relies on it for several details: the straight-line row removal, the unique-email rows, `fm="ml"` with n.iter 1000/100, the moratorium cutoff, and recoded = final positions with No opinion as 50. None of the relevant lines are shown. The R code's `validate` rule for age and education, which is what age-education-inconsistencies depends on, is never examined.
3. [affects a conclusion, efa-eleven-factors] `vk.parallel_reference` and cell 35: the polychoric parallel analysis compares against eigenvalues from normal data with Pearson correlations. psych's `fa.parallel(cor="poly")` builds its reference from resampled data with polychoric correlations. Under reading (a) with default settings, the 12th polychoric value (0.0106) sits only 0.0011 below its reference (0.0117), so the count could move to 12. Separately, reading (b) Pearson with default settings already gives 12, so the claim holds under reading (a) only.
4. [does not affect a conclusion] `vk.FITS`, cell 35: 18 of 2,074 uniqueness fits did not converge, and the notebook does not say whether any of them were fits on the observed matrices.
5. [does not affect a conclusion] `discordant`, cell 21: a pair counts as discordant when one side is within the tie tolerance and the other is not. SMER-SD/HLAS-SD is flagged on the economic axis although both orders agree. This overstates the economic mismatch, but PS is still genuinely out of order.
6. [does not affect a conclusion] Cell 5: the workbook's "Statement no." column is wrong for 99 rows, with statements 16 to 24 rotated. Renumbering by English wording is justified, since the recoded CSV matches it 1.000 against 0.823. This is a defect in the dataset and should be reported as one.
7. [does not affect a conclusion] Cell 1: the MD5 values are printed from the API but never checked against the bytes that were streamed.
8. [does not affect a conclusion] Claims file, age-education-inconsistencies: the paper says these inconsistencies were found "upon initial review" and then "acknowledged during further data curation and refinement of the data collection tool". The 40 and 400 may therefore describe an earlier state of the data, and the criterion does not mention this possibility.
9. [does not affect a conclusion] Claims file, collection-window: the R code's moratorium cutoff (2023-09-30 22:42:30, as given) suggests TIME.STAMP is local time, which makes reading (b) unlikely. Under either reading, rows still fall after election day.

**C. What I could not check**

- The figure readings in cells 21 and 24, because Figs. 2, 3 and 7 are not available to me. Images of the published figures with the transcribed values overlaid, or a reading done before the scores were computed, would settle problem 1.
- What the R code actually fixes. Printing the relevant lines would settle problem 2: `same_response_rows`, the unique-email filter, the `fa.parallel` calls, the moratorium filter, the recoding, and above all the age/education `validate` rules.
- A cheap way to settle problem 3: a reference from resampled data with polychoric correlations (psych's method), or the counts from running psych's `fa.parallel` on the same matrix.
- Which of the 18 non-converged fits belong to observed matrices (problem 4).
- I did not download data or re-run anything. I tested `weighted_kappa` against sklearn (identical), `polychoric` on simulated ρ = 0.5 data (it returned 0.4998), and `parallel_count` and `dimension_assignments` on synthetic inputs; all behaved correctly. I also compared `varimax` and `promax` with R's code by reading, and they match.
