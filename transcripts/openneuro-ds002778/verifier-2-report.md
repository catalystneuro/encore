**Verification report, round 2: Jackson et al. 2019 (eNeuro 0151-19.2019) on OpenNeuro ds002778 v1.0.5**

**Counts.** The claims file has 24 claims and the attempt record gives 24 outcomes: 9 reproduced, 9 partially reproduced, 6 not reproduced, none blocked. These are the outcomes I gave in round 1.

**How I checked this round.**
- I read every printed output of the re-executed notebook (cells 0–84).
- From the printed per-patient values, I recomputed the new variants without pd6 and pd16:
  - Beta sharpness: W 11, p 0.0159, d 0.811.
  - Beta steepness: W 5, p 0.0046, d 0.752.
  - Beta PAC (Methods filters): W 13, p 0.0231, d 0.732.
  - Spearman r on/off with and without the two patients.
  - All match to rounding.
- I recomputed the BH correction for Table 2 from the printed p-values (0.0531 for both steepness tests).
- I checked the Q4 counts in the paper's text (paragraph 90): C3 9, C4 8, both 8, so 9 with at least one. The claims file reads them correctly.

### 1. Outcomes and assumptions

I agree with all 24 outcomes.

- **Three outcomes changed after round 1.** offctrl-steepness, table1-alpha-pac-null and table2-alpha-offctrl are now not_reproduced. Each follows from its criterion:
  - Both non-failing outcomes of the two Table 2 claims need the average-reference result to survive FDR correction, and it gives 0.0531 under every reading. The correction-procedure table (cells 39 and 59) shows Holm, Bonferroni and BY are further from 0.05.
  - The alpha PAC readings disagree (a192 0.0609, b231 0.0783, c118 0.0356; cell 56). The criterion takes the outcome that all readings give.
- **Outcomes that rest on a judgement:**
  - fig2-pac-off-on applies the stricter reading of a criterion that contradicts itself. The record says so and puts the question to a reader.
  - pac-beta-larger-than-alpha is marked partially reproduced, but its criterion has no partial clause. Partial is a reasonable default (test holds, W 17–18 against 9.9–12.1), but the claims file does not define it.
- **Assumptions.** No outcome carries `assumed: true`; the earlier assumption of a 192-tap alpha filter was removed. The judgements the outcomes rest on are all stated, as notes or deviations:
  - no artifact rejection;
  - CSD computed with MNE on template positions;
  - "Total UPDRS" read as Part III;
  - the stricter fig2-pac reading.

  All are reasonable. The CSD one is the least tested (see section 3).

### 2. Sentences the numbers do not support

1. **Cell 84 (Summary), and the end of "What was found about the dataset":** "Without artifact rejection the main off against on results hold, with statistics close to the paper's."
   - Steepness W is 16 against the paper's 9 (cell 19), and sharpness d is 0.73 against 0.86 (cell 16).
   - Two of the three main claims have a value out of tolerance, so "close" overstates the match.
2. **Cell 84 (Summary):** "It holds the 15 patients … and 16 controls …, each recording once." Patients were recorded twice, off and on (cell 4). The sentence probably means no recording is duplicated (cell 10), but as written it is wrong.
3. **Cell 84 (Sensitivity):** "Without sub-pd6 and sub-pd16 … the off against on tests keep their direction and significance."
   - The exclusion is printed only for the three beta tests at C3/C4 (uncorrected) and for alpha PAC.
   - Alpha shape, bipolar and FDR-corrected values without the two patients are not shown.
   - Under reading c, alpha PAC is significant after correction (0.0356) but has uncorrected p 0.064 without the two patients (cell 56), so not every test keeps its significance.
   - "Dropping the filtered edges … changes no test" is likewise shown only for the beta off-against-on test at C3/C4 (cell 22).
4. **Cell 34 and the fig2c record notes:** "with the code's filters the smallest p is at Fz (0.020)". Cell 33 prints Fz and CP6 tied at 0.0199, and CP6 is in the sensorimotor set. The outcome does not change, since sharpness fails either way.
5. **Cell 74:** "points that decide membership (pd12, pd22, pd26, pd28, pd3 and pd9 on medication)".
   - pd9's C4 off point is in Q1 (0.027, 0.075), far from any axis. Its C3 points would have to cross both axes. So pd9's near-axis points do not decide its membership.
   - pd5 (C3 on, RDR −0.0023; C4 on, RDR 0.0070) and pd11 (C4 on) do decide membership and are not listed.
6. **Minor:**
   - Cell 23 and the record say edge-dropping "changes PAC by 5% at most". Cell 22 prints a ratio of 0.9487, which is 5.1%.
   - Cell 45 says CSD PAC is "higher off under every variant". The variant rows print p only, so the direction is shown for the main m = 3 CSD only.
   - Summary row for table3 says "two values above tolerance". That holds under log10 PAC with the Methods' filters. Under raw PAC, the all-patient PAC d (0.85, above 0.825) is a third.

The other "**Result:" cells, the README rows and the record notes match the printed outputs.

**Round-1 reasons in the record.** The record states my round-1 reasons in my words, and accurately. Problems 4, 6 and 7 and the Section C items are attached to the claims they concern. Problems 5 (pd6/pd16) and 8 (artifact rejection) are not quoted as reasons. Neither bore on an outcome, and the record answers both: problem 8 in the deviations and findings, problem 5 in the exclusion variants and the findings.

### 3. Round-1 points

**Resolved:**
- **2:** alpha PAC reading disagreement. The outcome was changed and the notebook now prints that the readings disagree.
- **3:** the Q4 subset is now stated as 13 patients against the paper's 9, with the patients listed.
- **4:** cell 12 now says 1 to 14.
- **5:** exclusion variants now cover PAC, the correlations, Q4 and Table 3. They show that the steepness–PAC on-medication miss rests on pd6 and pd16.
- **6:** edge-dropping changes PAC by at most 5.1% per recording and leaves W unchanged.
- **Section C, Table 2 FDR sensitivity:** the misses are not an artefact of BH.
- **Section C, Q4 per-patient values:** now printed.

**Still open and bearing on a conclusion:**
- **Problem 1, fig2-pac-off-on.** The criterion still contradicts itself. The outcome is partially reproduced or reproduced depending on which sentence governs, and it now waits on a reader.
- **Problem 7, offctrl-pac-csd.** The spline variants all miss (p 0.105–0.30), but MNE has not been compared with the CSD toolbox. CSD roughly doubles the ratio of 50–150 Hz power to beta power at C3/C4. That raises gamma, which the PAC amplitude uses, and the toolbox's output may behave differently.
- **Problem 8, artifact rejection.** It cannot be done with this dataset. It remains the likely cause of the out-of-tolerance W and d values and of the Q4 count gap: 16 of 60 points lie within 0.01 of an axis.
- **pac-beta-larger-than-alpha.** The criterion has no partial clause, so the claims file should define it.

**Still open, not bearing on a conclusion:** the summary and cell wording in section 2, items 1–6. Item 1 matters most, because the summary states a better match to the paper than the outputs show.
