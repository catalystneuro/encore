## Verifier report, round 2: Chandravadia et al. 2020 on dandiset 000004 (0.220126.1852)

The claims file has 25 claims and the attempt record has 25 outcomes: 10 reproduced, 10 partially reproduced, 4 not reproduced and 1 blocked. Since round 1 the author added `previous-release-link` and changed `previous-release-additions` from blocked to partially reproduced.

What I checked independently in this round (saved in `paper/`):
- I downloaded the paper and Faraut et al. 2018 (HTML and PDF).
- The helper's copy of Faraut 2018 Table 1 matches the PDF row for row: 42 subjects and 65 session ids, with no differences.
- The paper says "we added 17 subjects and 288 neurons" and "23 new sessions, including 9 sessions from … TWH". The Fig. 3 and Fig. 4 legends define the label as "session ID – channel number – cell number – brain area" and do not define "cell number".
- I ran the helper's `zroc_slope` on a session with responses only at 1 and 6.

### 1. Outcomes

I agree with all 25 stated outcomes. Three need comment:
- **fig5b-roc-asymmetric:** I agree it is reproduced, but some of the slopes it reports are not real values (see 2a).
- **fig3-example-vs-neuron:** I agree it stays blocked for now. A test that is not yet in the notebook could move it (see 3b).
- **previous-release-link:** The author added this claim, and it comes from Faraut 2018, not from the paper under test. I agree with partially reproduced: 64 of 65 sessions are found, which is above the criterion's 90%.

### 2. Sentences the outputs do not support

a. **Cell 55 and the attempt record's fig5b notes** say "below 1 in 70 of 87 sessions, with a mean of 0.726". The numbers are as printed, but several slopes are not real estimates.
- Sessions 60, 99, 119 and 2008 have negative slopes, and session 59 has −0.000 (cell 54).
- Cumulative hit and false-alarm rates rise together, so a properly fitted z-ROC slope cannot be negative. A negative slope only appears when all five z(FA) points are equal and `polyfit` has no unique fit.
- The helper reproduces this: a session with 36 of 50 old and 4 of 50 new answered 6, and every other trial answered 1, gives −0.2074. Session 99 prints −0.207, with hit rate 0.72 and false-alarm rate 0.08.
- Recomputed from the printed per-session table without 60, 99, 119 and 2008: 83 sessions, mean 0.778, 66 below 1, t-test p = 2.1e-9, Wilcoxon p = 1.3e-8. The outcome holds, but the stated mean, count and p-values include these values.

b. **Cell 19, and the attempt record's table1-demographics notes**, say "The diagnosis is coded more coarsely in the files for most subjects."
- Cell 18 shows the text differs for 19 of 59 subjects, not most.
- For H10, H16, H17, H19, C58 and T89 the files add "Lateral", which makes them more specific than the table, not coarser.

c. **Attempt record, table1-demographics notes and the matching finding:** "The files agree with the session list of the paper's code, defineNOsessions_release.ini (read, not shown in the notebook)". The same applies to the fig3 notes ("nor … in the session list of the paper's code", "its session list gives subject T103 the one session 2009"). No output shows the session list, so I cannot check these statements.

d. **README and the Summary (cell 87)** say "with its choices the counts are 147 and 26, the paper's numbers" and "343 VS, 147 MS and 26 dual cells, the paper's numbers". The paper gives 146, so 147 is within tolerance but not equal. Cell 66's "all matching the paper" is accurate.

e. **Cell 0's status table** gives fig3 as "blocked (data missing)". The attempt record, the README and cell 87 give metadata_insufficient.

f. **Cell 28** says "78 of 87 files meet every condition; nine hold codes …, seven files … have no start code 55, and session 2001 has three end codes 66". This reads as if the files without a 55 fail. Cell 27 shows that 6 of those 7 pass. The attempt record states this correctly.

**My round-1 reasons in the attempt record:** they are stated correctly and in substance in my own words. Problem 4 (the shared clock is shown in only 38 of 87 sessions) is not recorded under any claim. It was not tied to a claim, and cell 10 now states it.

### 3. Round-1 points

**Resolved:**
- Problem 1: cells 66, 69 and 72 and the notes say the MS, dual and fig5f outcomes come from the Methods disagreeing with the code.
- Problem 2: the null now uses 10 shuffles per unit, with a binomial test giving p = 0.18 against the null.
- Problem 3: a second seed gives 118 for the main count and 149 for the code's choices.
- Problems 5, 7, 8, 9 and 11.
- Problem 6: mostly resolved, apart from 2b.
- Problem 10: the two p-values now print as 1.586e-9 and 1.631e-9, and the per-session table is printed.
- Section C: the per-unit p-values are printed (288 units), the fig3 proxy is run, the earlier release is tested with a verified copy of its table, and `imp` is shown to be float64 NaN throughout.
- The extra unit (1864 against 1863) cannot be identified from the paper, and the notebook now says so.

**Acknowledged but unchanged:** Problem 4. For 49 sessions with 801 units the shared clock is still assumed.

**Remaining points that bear on a conclusion:**

a. **fig5b-roc-asymmetric:** the degenerate z-ROC fits (2a). Detect sessions whose interior z(FA) or z(H) points are all equal, and exclude or flag them before reporting the mean, the count and the tests. The outcome is unlikely to change.

b. **fig3-example-vs-neuron:** the cell-number convention is not tested.
- The notebook concludes from Fig. 4 that "cell number" is the electrode row, but cell 77 does not print the Fig. 4 unit's index.
- In session 2009 two units share electrode row 1, so the electrode row cannot tell neurons apart there. That argues against reading the cell number as the electrode row.
- The phone-selective candidate is 0-based unit index 2, which is the third unit, cell 3 if counted from 1.
- If the Fig. 4 unit is 0-based index 3 in session 132, then "cell number" is the 1-based unit index. The candidate would then match the label's channel (140), area (RH), cell number (3) and preferred category (phones, p = 1.3e-9), with only the session mapping 144 → 2009 coming from code read outside the notebook.
- One printed value would settle this, and it could move the claim from blocked to tested with outside input.

c. **ms-cells-proportion and dual-cells-proportion:** the correct-trials variant, which matches the paper's 147 and 26, has no shuffled null of its own. Some sessions have as few as 9 correct old trials. It is compared only with 5% (p = 7.1e-8). This does not change the not_reproduced outcomes, which are judged on the Methods test, but it leaves the matching variant's excess over chance unshown.
