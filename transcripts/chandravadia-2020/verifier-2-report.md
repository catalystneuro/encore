**Verifier report, round 2: Chandravadia et al. 2020 on DANDI:000004 v0.220126.1852**

The claims file has 25 claims, and the attempt record gives 25 outcomes: 10 reproduced, 10 partially reproduced, 4 not reproduced and 1 blocked (data_missing).

## 1. Outcomes and assumptions

I agree with all 25 outcomes. They match my round-1 outcomes, and the re-executed outputs still support each one (cells 15 to 90).

No outcome in the record is marked `assumed: true`. The choices that outcomes depend on are listed as deviations instead:
- IsolationDist is read as IsolDist (units-table).
- Trials are cut at TTL-1 (ttl-codes).
- Sessions without a z-ROC slope are left out (fig5b).
- Experiment ids are read at TTL-1 (experiment-ids).
- The task variant is read from the image folder (previous-release-link).
- The bootstrap seed and its mode (ms-cells).

All of these are reasonable and stated. Two are close to assumptions and could be flagged as such:
- units-table: without the IsolationDist reading, the column test fails.
- ttl-codes: the record says cutting trials at the trials' start and end times "gives more failures", but that result is not in the notebook. So it is not shown that "most files" still holds under that cut.

Neither changes my agreement.

## 2. Sentences the printed outputs do not support

- **Attempt record, fig5f-site-proportions notes:** "equal to the figure's values to the second decimal". Cell 75 prints CS 18.35, 7.78, 1.40 and TWH 19.48, 10.39, 1.30. The figure's values, as given in the claims file, are 18.4, 7.7, 1.4, 19.4, 10.4, 1.3. 7.78 against 7.7 and 19.48 against 19.4 differ even at the first decimal, and no rounding rule makes all six equal. "All 6 within tolerance" is supported; "equal to the second decimal" is not.
- **Cell 32, the ttl-codes notes and the TTL finding:** "in T88_2001, T88_2002 and T90_2003 a second 3 comes before the 2". Cell 31 prints one failing example per file. Only T88_2001's shows this ([1, 3, 2, 3, 21, 6]). The examples printed for T88_2002 and T90_2003 are [1, 2, 3, 21, 23, 6], which is an extra code 23, not a 3 before the 2. Code 23 occurs only 6 times in all files, so most of the 10 and 7 failing trials in those files must have some other defect. What that defect is, is not printed.
- **README:** "it takes about 6 minutes". Cell 93 prints 8.3 min. Cell 3 (97 s) and cell 28 (323 s) alone take 7 min.
- **Cell 38 (minor):** "before the Huntington recordings that surround it in the session numbering (2006 to 2016)". The nearest H sessions to 68 are H43_56 (2013) and H47_92 (2014), and its direct neighbours are CS sessions. 2006 to 2016 is the span of all H files. The conclusion that the year is likely a default still holds.

Every other sentence I checked is supported by the printed numbers. That covers all "**Result:**" cells, the Summary (cell 94), the rest of the README, and the record's outcome notes and findings. I also confirmed three statements against `paper/`:
- H48 is listed as 54 M and C48 as 32 F.
- The Methods give "89 sessions".
- The text says "the existing and new dataset".

The record restates my round-1 reasons faithfully and in my own words. Problems 1 to 3 and 5 to 9 are attached to their claims, problem 4 is in `reviewed`, and the items from section C are attached to electrodes-table, task-structure, previous-release-link and previous-release-additions.

## 3. Round-1 points

Resolved:
- **Problem 1 (bootstrap mode):** The notebook and helper now cite a three-argument call (NWB_singleCellAnalysis_release.m line 102), so mode 1 without variance correction applies. A studentized variant was run and gives 92 under the main reading and 126 under the code's choices. The helper's studentized form matches its description. I cannot see the code, so the line-102 citation is unverified. Neither form reaches 131.4, so this does not bear on the outcome.
- **Problem 2:** the spread of the correct-trials variant (132 to 147) is now stated.
- **Problem 3:** the main count's distance from the null (1.55 points) is now stated.
- **Problem 4:** the cell 6 text now matches cell 5.
- **Problem 5:** the strict count (78) and the missing encoding trials are now stated, and the pixel hashes confirm the file names in 87 of 87 files.
- **Problem 6:** CS24_59 is shown as a variant (p = 6.6e-9).
- **Problem 7:** no change was needed.
- **Problem 8:** the variant was removed.
- **Section C:** the stored form of `imp` (float64, fill value 0, only NaN), the H48 unit count, the area breakdown of the 37-neuron gap, and image identity by pixels are all resolved.

Remaining points that bear on a conclusion:
- **fig5f-site-proportions, possible misreading in the claims file (problem 9).** The record has filed this as a reader question and shows the text's grouping as a variant (p = 0.87, 0.52, 0.70). The claims file gives no per-group expected values for that grouping, so the outcome under the paper's text is undefined until the question is answered.
- **fig5f-site-proportions notes:** the "second decimal" sentence above should be corrected. The outcome does not change.
- **ttl-codes:** the description of the sequence failures in T88_2002 and T90_2003 is not supported by the printed outputs. The partial outcome does not change.
