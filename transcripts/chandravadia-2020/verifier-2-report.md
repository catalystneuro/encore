**Verifier report, round 2: Chandravadia et al. 2020 on DANDI:000004 (0.220126.1852)**

Cell indices below refer to the re-executed notebook. Its cells have been renumbered since round 1.

**1. Outcomes and assumptions**

The claims file has 25 claims and the attempt record has 25 outcomes: 10 reproduced, 10 partially_reproduced, 4 not_reproduced and 1 blocked. I agree with all 25. Each one matches the printed outputs and the criterion in the claims file. fig3-example-vs-neuron is now `blocked_by: data_missing`, which I agree with.

- **Assumption (fig5b-roc-asymmetric):** this is the only outcome marked `assumed: true`. It leaves out 5 sessions that have fewer than 2 distinct false alarm rates. The record states this, and it is reasonable. Two variants are run (cell 61): the slopes MATLAB's `regress` would return give p = 5.4e-10, and setting the five slopes to 1 gives p = 5.4e-09. Neither changes the outcome. I read `nomem.zroc_slope_regress`, which uses pivoted QR and a rank tolerance; it is a fair stand-in for `regress`.
- **Choices not marked as assumptions, none of which decides an outcome:**
  - The 6 units whose rates are all equal are counted as not VS. 332 is well inside 343 ± 34.3, so this does not matter.
  - The 50% threshold in new-old-label-coding is stated as this attempt's own. The strict count of 78/87 decides the claim.
  - The fig5d dynamic-split deviation (low-confidence hits counted as response 4 only) is stated. I did not verify it against helper.py. Reading (a) alone decides that claim.
- **Claims file:** one possible misreading.
  - fig4-example-vs-neuron reads the figure's "cell number" 4 as "electrode row 4". The paper says cell number. Only one unit sits on channel 177 in session 132 (cell 91), so the outcome does not change.
  - The fig3 discussion, though, reads cell number as a unit index counted from 1 (cells 95 and 104 of the record notes). For fig4, unit 4 matches only when counted from 0; counted from 1, cell 4 would be unit index 3, which is not on channel 177. So the statement that the T103 candidate "fits the figure's … cell number" uses the opposite convention to the one that matched fig4. This does not affect the blocked outcome, but that argument for the candidate is weaker than the text says.

**2. Sentences the numbers do not support**

- **Cell 42 and the units-table notes and finding:** "two isolation distances are above 1e27" / "two values above 1e27". The outputs show 2 values above 1e6 (cell 41) and a maximum of 8.08e32 (cell 7). Nothing shows that the second value is above 1e27.
- **units-table notes, "all infinite ones in H28_48", and the finding "infinite for 11 (session 48)":** no output shows which files hold the 11 infinite SNR values. Cell 41 prints only "in 33 files" for all non-finite values.
- **Cell 30 and the data_missing finding:** the missing old images are "in the encoding blocks of other files of the same variant". Cell 29 shows only "in the encoding block of some file". Nothing checks the variant.
- **Summary (cell 96):** "Seven sessions hold only 50 … and one holds 97, so 21 to 24 old images of those sessions were never shown in the file's encoding block". The 21 to 24 is true of the seven sessions only. Session 123 is missing 1 image (cell 29).
- **Cell 89 and the previous-release-additions notes:** "1863 − 1576 = 287 is the paper's number". The paper's number is 288. The sentence should say "within 1 of".
- **README:** "the paper's code uses 0.2 to 1.7 s and correct trials only, and gives the paper's numbers". This holds for MS (146). For dual cells the code gives 25 against the paper's 26; that is within tolerance but not equal. The summary states this correctly ("25 here").
- **Finding (metadata_error, session dates):** "timestamps_reference_time is set to the session's start date". That attribute is never printed. Cell 7 shows only that 38 files use Unix time.
- **Cell 8:** "Trial and spike times share one clock in each file (checked below)". Cell 14 says the check cannot establish this for 5 files. Cell 8 also says the median stimulus duration is "1 s in most files"; the output gives only the range (0.998 to 2.016 s), not how many files are near 1 s.
- **Cell 55:** "Duplicated recognition data: none" is a hard-coded string, the same pattern as round-1 problem 1. Cell 11 supports it for the three pairs of files that share spike trains ("same recognition trial times False"). No check across all sessions is printed.

All other conclusion sentences, the rest of the summary, the README table and the record notes agree with the outputs. These include every count, p-value, percentage and per-session list I checked: cells 16 to 92, and the notes for all 25 outcomes.

**My round-1 reasons in the record:** they are in my words, with the problem points and "Not checked" items merged into the relevant claims. Problem 2 is placed under session-dates, where it does not belong (it was about cell 7), but its content is right. Nothing is misstated.

**3. Round-1 points**

All 8 problems are resolved:

1. Column descriptions are now read from the files (nomem.py:133), and cell 41 prints `IsolationDist: 'IsolDist'` for 87 files.
2. The spike_times attributes and the events unit are now read (nomem.py:134–136, cell 7). spike_times states no unit.
3. The `auc` docstring now states the difference from the MATLAB.
4. The `zroc_slope` docstring is corrected, the exclusion is marked as an assumption, and variants are added.
5. The code-versus-Methods explanation is in cell 74, the summary, the README and the code_mismatch finding.
6. The low power of the Fisher tests is stated in cell 80.
7. The strict and threshold counts are both printed in cell 28.
8. The three findings are now in cells 4, 29/30 and 48.

From "Not checked":

- **Resolved:** `imp` is float64 and all NaN (cell 44). The Faraut et al. 2018 table is printed per row, with session 98 under H48, variant 2 (cell 85).
- **Listed but not checked:** per-unit p-values are now listed (cell 68). Comparing them unit by unit with the paper's code output would need that output, which I do not have.
- **Still unverified:** helper.dynamic_split. This does not bear on a conclusion.

Nothing that remains bears on an outcome. The section 2 items are wording fixes to the notes, findings, summary and README.
