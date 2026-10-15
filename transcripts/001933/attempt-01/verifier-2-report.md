**Round 2 verification: 001933-chen-2026-01**

I counted 18 claims in the claims file and 18 outcomes in the attempt record: 6 reproduced, 2 partially reproduced, 2 not reproduced and 8 blocked (data missing). Cell numbers below are the indices of the re-executed notebook. They have moved since round 1.

**1. Outcomes**

I agree with every stated outcome.

| Claim | Outcome | Basis (cell) |
|---|---|---|
| source-data-link | not_reproduced | Cell 12: match fractions 1.0, 0.609, 0.609 and 0. The transient-mean variant gives 0.481, also below 50%. |
| fig6e-anxa1-evoked-reduced | reproduced | Cell 21: 64 against 56 stimulations, p = 1.16e-22. |
| fig6e-anxa1-evoked-per-mouse | reproduced | Cell 24: 7 of 8 mice under all four readings; 3743 is the exception. |
| supp7c-anxa1-evoked-all-powers | reproduced | Cell 27: 4 of 4 powers; Methods window has 56 WT stimulations at every power. |
| fig6f-anxa1-spontaneous-reduced | reproduced | Cell 32: 1064 and 798 transients, 57 to 285 per mouse, p = 4.85e-72. |
| fig6f-anxa1-spontaneous-per-mouse | partially_reproduced | Cell 35: 5 of 8 mice under every reading. |
| supp8c-calb1-spontaneous-not-reduced | reproduced, marginal | Cell 38: p = 0.05088. Counts 896 and 635, both within tolerance. |
| supp8e-calb1-evoked-reduced | reproduced | Cell 41: 56 against 40 stimulations, 4 of 4 powers. |
| supp8e-calb1-few-mice-reduced | partially_reproduced | Cell 44: 7, 6, 4 and 4 mice; the closest reading gives 4. |
| cohens-d-anxa1-larger | not_reproduced | Cell 47: Calb1 d = 1.395 is outside tolerance, and the ratio is 1.58. |
| 8 claims from Figures 1 to 5 | blocked, data_missing | No change since round 1. |

**2. Text against printed outputs**

I checked every Result paragraph (cells 16, 22, 25, 28, 33, 36, 39, 42, 45, 48), the Summary (cell 50), the README and the attempt record's notes. Almost all of it matches the printed numbers. I recomputed the two values not printed directly, 131.9 and 302.9, from the per-mouse table in cell 32 and they agree. These sentences are not supported:

- **Cell 50 (Summary):** "the published traces equal the dandiset's dF/F to within 1e-12".
  - The only printed value is 5.7e-13, for Figure 6C (cell 12).
  - For Supplementary Figure 7B, matched traces are shown only to be below the 1e-6 threshold. The printed largest difference, 109.8, includes the one miss.
  - The record's source-data-link note has the same scope problem: "(largest difference 5.7e-13)" follows a clause that names both 6C and 7B. Cell 16 scopes it correctly.
- **README:** "It takes about three minutes". Cell 51 prints a total run time of 241 s, which is about four minutes.
- **Cell 10 (data check, outside the required scope, but it supports the power-label argument):** "In Anxa1 files where 1.5, 2 and 3 mW are given as 0.33 s trains, those responses fall below the 0.5 and 1 mW ones given as 0.51 s trains (for example mouse 4401)."
  - In cell 9 this holds for 4401, 3947, 4253, 4561, 4651, 4004 and 4007.
  - It fails for 3743, 3948, 4398, 4558, 4652 and 4005. For example, 4398 has 173.5 at 1.5 mW against 114.8 at 0.5 mW.
  - The sentence should say "in some files".
- **Minor, not checkable from outputs:** the fig1d note in the record gives "S-BIAD2070 to S-BIAD2074", but cell 49 lists 2070, 2071, 2072 and 2074, without 2073.
- **Minor, claims file:** the supp7c statement reads "p from 2.39e-16 to 1.10e-20". The paper's value at 0.1 mW, printed in cell 27, is 1.29e-15, which is outside that range. The outcome does not change.

**My round-1 reasons as the record states them:** they are accurate paraphrases. One error is mine, and the record copies it faithfully. My supp8c reason said that "under any of the alternative measures the outcome flips". That is wrong for the mouse-mean test, p = 0.402 (cell 38), which does not flip. Only the transient-mean measure (2.25e-09) and the code's exclusion window (1.81e-05) flip it. The record's reason should be corrected to say that.

**3. Round-1 points**

Resolved:

- **Problem 5 (dropped 4398 train):** `evoked_integrals` now checks only the samples each window uses. The synthetic test in cell 19 would fail under the old condition. Methods-window 4 mW now has 56 WT stimulations, p = 4.08e-18.
- **Problem 7 (no Calb1 evoked mouse-level test):** cell 41 adds it: p = 0.0424, 0.0413, 0.0726 and 0.0916 across the four powers.
- **Problem 8 (p printed as 0.0):** the summary dicts now print 3 to 4 significant figures.
- **Problem 6 and C2 (part-4 tolerance; which Anxa1 mice fail):** part 4 is now scored at both 1% and 1e-4 (cell 12). 4398 and 4007 fail by one sorted value each.
- **C1 (is the Calb1 mismatch a labelling error?):** cell 15 searches all 64 epochs and 8 powers of each mouse. No epoch is within 1e-6 of any of the 384 traces; the closest is 15.7 to 150.8 % dF/F away. This rules out epoch or power labels as the cause.
- **C3 (power labels for 3742 and 4885):** cell 9 adds the per-epoch tables. The response does not follow labelled power in either mouse, and the notes and findings now say so.

Still open, and bearing on a conclusion:

- **Problem 1 (Calb1 dF/F is not the paper's):** the attempt has characterised this as far as it can. It still decides cohens-d (not reproduced) and supp8e-few-mice (partial), and every Calb1 result is a result on the dandiset's processing, not the paper's.
- **Problem 3 (supp8c at the threshold):** the outcome rests on p = 0.0509 against 0.05. Two of the three variants flip it. Reproduced is correct under the criterion, but the result is fragile.
- **Problem 2 (spontaneous measure):** the published values are 0.005 times the mean dF/F of each transient, not its integral. This is why fig6f-per-mouse gets 5 mice where the paper's measure gives 6, and why source-data-link part 4 scores 0.
- **Problem 4 (two mice on different trains):** this does not change any outcome. Two of the seven significant Anxa1 per-mouse results (3742 and 4885) come from 0.33 s trains whose power labels the data cannot confirm.

Not done: C4, reading the Supplementary Figure 7 and 8 legends. My round-1 report says I saved the main text under `paper/`, but no `paper/` folder exists in this round's directory, and I did not download the paper again. The supplementary p-values and counts therefore still come from the claims file.
