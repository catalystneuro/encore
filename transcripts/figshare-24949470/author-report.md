## Report

The attempt is recorded and handed over. The entry is `entries/figshare-24949470-mintal-2024/`, the record is `attempts/figshare-24949470-mintal-2024-01.yaml`, and the verifier's package is in `executed/figshare-24949470-mintal-2024/handover/`. `entry.py lock`, `check` and `all` all passed with 0 errors, and the notebook runs in 449 s. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| user-responses-count | reproduced (134,699 rows) |
| collection-window | not reproduced (432 rows dated 1 to 9 Oct; 494 if the timestamps are read as UTC) |
| party-positions-structure | reproduced (39 statements, 429 positions) |
| eleven-parties | reproduced |
| party-self-placements | reproduced (4 parties) |
| coder-agreement-kappa | reproduced, rests on an assumption (0.842 with quadratic weights and "No opinion" left out; the other readings give 0.62 to 0.75) |
| uni-and-landscape-placements | partially reproduced (all 5 uni-dimensions and the cultural axis match Figs. 2 and 3 exactly; PS on the economic axis is 47.7 against about 54 in the figure) |
| party-clustering | reproduced (all 9 clusters of Fig. 7 at its heights) |
| table2-gender, table2-age, table2-education | reproduced (exact under the R code's cleaning) |
| age-education-inconsistencies | not reproduced (27 and 378 against 40 and 400) |
| s2-s3-wide-range, s4-s5-consensus | reproduced |
| efa-eleven-factors | reproduced (11 and 11 on the cleaned rows with "no opinion" as 50) |
| efa-loadings-consistent | reproduced, rests on the claims file's thresholds |
| selected-parties-top-vote | blocked, `other` (no pinned source of the 2023 results; ParlGov 2024 stops at 2020) |
| website-views | blocked, `other` (the platform's usage records are not public) |

### 2. What was found about the dataset

- **Statement numbers are wrong in the party workbook.** In `VAA_party_positions coded.xlsx`, "Statement no." disagrees with the wording in 99 rows. Statements 16 to 24 are numbered 22, 23, 24, 16 ... 21. The recoded CSV and Figs. 2 and 3 follow the wording, so I numbered statements by their wording.
- **Undocumented cleaning step.** The R code removes 330 responses that give the same answer to all 39 statements, which the paper does not mention. With that step Table 2 and the S4/S5 counts match exactly.
- **Rows after election day.** 432 rows are dated after the election, including Table 1's sample entry.
- **Description errors.** "No opinion" is the string `NA` in the file, not an empty string as the paper says. The README calls each row a unique respondent, but EMAIL_ID repeats. The "Self-placement source" column is empty in all rows. The data dictionary gives no categories for gender, age and education, and no time zone for TIME.STAMP.
- **Assumptions:**
  - Kappa uses quadratic weights with "No opinion" pairs left out.
  - The loading thresholds are the claims file's own.
- **Questions for the paper's authors:**
  - What weights and "No opinion" handling the kappa used.
  - Which rows and categories gave the 40 and 400 counts.
- **Questions to a reader:** none.

### 3. Where the protocol was unclear, wrong or missing something

1. **No reason fits an `elsewhere` claim whose data is not public anywhere** (website-views). `data_missing` is forbidden for `elsewhere` claims, but the protocol says unpublished data should be `data: dataset` with `data_missing`. I used `other` and explained in the notes.
2. **Public but unpinnable outside data** (official results with no DOI or versioned release) has no listed reason. I used `other`.
3. **The `with_labels` check demands outside inputs plus a `metadata_insufficient` finding**, but this claim's labels are in the dataset itself (Supplementary Table 1). I listed the paper's figures as the input; the check is met by a real `metadata_insufficient` finding I recorded anyway.
4. **No rule for expected values that must be read by eye from published figures.** I typed my readings into the notebook, marked them as such, and listed the paper under `inputs`.
5. **Unclear how to treat analysis code that disagrees with the Methods when the claims file has not read the code.** Here the code adds a cleaning step and the factor-analysis settings. I kept the paper's or criterion's reading as the main result and showed the code's as variants, following reader step 2's order.
6. **The clock-sharing check (author step 2) has no meaning for survey data.** I said so in the data check.
7. **The protocol assumes R-free environments implicitly.** psych cannot run in the locked Python environment, so I reimplemented fa.parallel, the polychoric correlations and the factor extraction, and recorded this as a deviation.

### 4. Runtime and failures

- **Runtime:** about 35 minutes of wall time; the notebook takes 7.5 minutes.
- **Failed or not completed:**
  - A first run failed because the synthetic test matrix was not positive definite; I fixed the test and guarded the ML fit.
  - `factor_analyzer` would not run with the current scikit-learn, so no cross-check against it was made.
  - 18 of 2,074 factor fits did not report convergence; the count is printed in the notebook.
  - The parallel-analysis count for reading (a) with Pearson moved from 12 to 11 when I tightened the optimiser tolerance (the looser run is not in the notebook). The record says so.
- **Untracked files not mine:** the repository root has dotfiles and a `scripts` device node from the sandbox. I left them alone; check them before committing.
