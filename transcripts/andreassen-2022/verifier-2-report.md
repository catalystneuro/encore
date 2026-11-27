**Verifier report, round 2: Andreassen et al. 2022 (attempt andreassen-2022-01)**

**1. Outcomes**

The claims file has 28 claims. The attempt record has 28 outcomes with matching ids: 17 reproduced, 2 partially reproduced, 9 blocked (data_missing). I agree with all 28.

- **figs1e (blocked).** The block is now established. Cell 15 prints the Readme entry for `Response` ("0 = never lost equilibrium, 1 = lost equilibrium"). It also prints the crosstab (control 5/9, heat ramp 0/12) and shows `Response equals (LOE > 0): True`.
- **figs3d (the only `assumed: true`).** The deviations state every assumption:
  - bins are converted to time with the 0.3 °C/min ramp;
  - window means are weighted by overlap;
  - the onset-bin frequency is read as a rate over the part of the bin recorded before onset;
  - the 0.5 threshold is the claims file's.

  These are reasonable, but the onset-bin reading decides the outcome. Cell 60's rescaled variant gives a normoxic 2-min ratio of 0.691, which fails. The evidence for the reading is indirect: Spearman rho = 0.23, p = 0.22, n = 30, and mean onset-bin frequency 0.839 against 0.922 by fraction of the bin. That is consistent with a rate over the recorded part, though not proof. "Reproduced, fragile, assumed" is the right label.
- **No misreadings of the paper** by the claims file found. As in round 1, fig6c's decline rule is fragile, not a misreading.

**2. Text against outputs**

Almost every number in the Result conclusions, Summary, README and record notes matches the printed outputs. Exceptions:

- **Cell 11:** "Fish33 … the hypoxia counts of Table S8 (14) and Fig. 5D (12) both hold without it." Only Table S8's count holds without Fish33. In cell 60, hypoxia has 11 fish once Fish33 is dropped. Cell 63's hypoxic count of 12 at 28 °C includes Fish33, so Fig. 5D's 12 needs it.
- **Cell 61:** "The onset frames support 0.3 °C/min as the rate from the start of the recording." This overstates cell 60:
  - across fish the slope is 0.225 (r = 0.98, experiment 2) and 0.222 (experiment 1 without three fish);
  - the start temperatures implied by 0.3 °C/min range from 19.72 to 28.95 °C.

  The outputs only show that 0.3 °C/min gives start temperatures consistent with the first medulla bins. The cell's own later sentence ("does not equal a constant 0.3 °C/min ramp … cannot say which part … differs") is accurate.
- **Record, figs3d notes:** "The drop below half lies in the partial bin that holds the onset; the last complete bin before it is 0.58, 0.40 and 0.72." In hyperoxia the last complete bin (0.401, cell 60) is already below half. Cell 61 correctly limits this to normoxia and hypoxia; the notes do not.
- **Summary (cell 77):** "every model reproduces the estimates of Tables S1 and S3 to S10." The notebook only checks the terms that the claims file quotes. It does not print a full comparison table for each model (for example Table S7's Model 1 and 2.1 against the paper), so "every" is not shown.
- **Round-1 reasons in the record** (`verifications.results`) are faithful paraphrases of my reasons, and problems 8 and 9 are covered under `reviewed`. One correction to my own round-1 reason for fig5a: "The overall-quartile variant also passes" is wrong. Cell 48 gives a hypoxic mean of 38.972 °C over 25 fish, outside 39.1 ± 0.1. The author's notes and cell 49 state this correctly. The outcome is unaffected because the R script uses within-treatment outliers (cell 19, line 433 context).

**3. Round-1 points**

- **Resolved:**
  - 1 (`Response` column, cell 15)
  - 2 (chi-squared shown, cell 17)
  - 4 (27 °C bin shown; no line of the script mentions a Q10, cell 19; alternative readings in cell 69, none gives 0.8)
  - 7 (median and range added)
  - 8 (Readme printed and columns checked, cell 6; a new finding on the `Recovery` unit, cell 7)
  - 9 (version taken by number, cell 3)
  - "Could not check" items: the script lines are printed, and the 27 °C bin and the onset bins are shown.
- **Accepted as is:** 5 (rule applied as written), 6 (Kenward-Roger not available; no p-value is near a threshold).
- **Partly resolved:** 3. The period-1 slope is explained by three fish with late onsets, and the last-complete-bin and rescaled variants are added. The normalisation of the onset bin remains unknown.
- **Remaining that bears on a conclusion:**
  - figs3d depends on the onset-bin normalisation (the rescaled variant fails) and on the bin-to-time conversion. It is recorded as assumed and put to the authors in finding 4. No change needed.
  - The fig5d-hypoxia gap (0.883 against 0.8) cannot be settled from the item. It is put to the authors in finding 6.

**4. Critical findings**

None of the 6 findings is rated `critical`. Findings 4 and 6 are author questions without a severity. On the others:

- **Finding 3 (minor):** its cell, `finding-fish-ids` (cell 12), shows only the Fish03/Fish35 medulla endings and Fish33. The Fish27/Fish29 light endings are shown in cell 10, and the 90-row / 14-missing CTmax counts in cells 4 and 8. The cell reference should be widened.
- **Fish33 (findings 2 and 3, minor):** this is a hypoxic fish with medulla and light data but no depolarization row. Its series ends at 37 to 38 °C, which matches none of the three hypoxic depolarization rows that lack medulla data (onsets 39.0 to 39.4 °C). Nothing shows it is misfiled, so minor is right.
- **Versions:** cell 3 shows version 3 has the same file names and MD5s as version 4, which supports `versions: ['3','4']` for findings 1, 2, 3 and 5. No finding gives `fixed_in`.
- **Ratings:** I agree with major for finding 1 and minor for findings 2, 3 and 5.
