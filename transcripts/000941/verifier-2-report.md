**Round-2 verifier report: Rouse & Schieber 2015 (doi:10.1152/jn.00686.2015) on DANDI:000941 0.241029.1405**

The claims file has 26 claims. The attempt record has 26 outcomes, one per claim, and all are blocked: 25 as data_missing and one (table2-movement-time) as metadata_insufficient. Its verifications block has 26 entries covering the same 26 claim ids.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| table2-trial-counts | blocked, data_missing | **Yes.** Cell 17: the session file has 412 trials, all R, none failed, numbered 201–673 over 53.3 of 86.2 min. Monkeys X and Y are absent. |
| table2-movement-time | blocked, metadata_insufficient | **Yes.** Cell 23: the file's per-session medians are 52–58 ms below jn.00008.2016 Table 2 in all four sessions. I checked the reference values against `paper/`: 238, 255, 232 and 253 ms, and J Neurosci 2016 I–M minimum 243 ms. Cue-to-onset is 57–77 ms above 243 ms, and cue-to-contact is 4–25 ms above 243 ms plus Table 2. The 200 ms result is shown but not compared, which is correct. The note that X and Y are data_missing is right. |
| fig2-trial-count-coax-45 | blocked, data_missing | **Yes.** Cell 28: 19 trials (16 under the approximation), from 412 of 717 trials. 28 × 0.57 = 16.1. |
| The 23 joint-angle and marker claims | blocked, data_missing | **Yes.** Cells 3 and 31: the only series are `eval_mask` and `preprocessed_emg`. |

No outcome carries `assumed: true`. None needs it: the movement-time outcome rests on the dataset leaving its onset undefined, not on an assumption.

The claims file's rule "if the dataset gives onset times, those are used" takes for granted that a dataset's onset is the paper's M. The attempt handles this correctly: it uses the times and then checks them. This is not a misreading of the paper, and I found no other place where the claims file misreads it.

### 2. Sentences the outputs do not support

- **Cell 0, the claims table:** "fig4-armps-time-course, the eleven Fig. 5 to Fig. 7 claims". There are 14: nine for Fig. 5, two for Fig. 6 and three for Fig. 7. Cell 30 lists all 14 correctly. My round-1 report made the same miscount ("11 … fig5 ×8"), and this sentence probably came from it.
- **README:** "including the first 53 minutes of the paper's session L20120928". Cells 5 and 17 show that the file starts at trial 201, with trials 1–200 absent. So it is a 53-minute stretch of the session, not the first 53 minutes. The attempt record's "spanning 53.3 of the session's 86.2 minutes" is correct.
- **Cell 32 (Summary), "the onset is shown above to be a later event … so it is not the paper's marker-speed onset", and the record's notes for table2-movement-time, "the notebook shows it is not the paper's onset M":** cell 25's own conclusion is "very likely a later event". The evidence is session medians on a 20 ms grid compared with another paper's medians from a different set of trials (676 against 412). "Very likely" or "indicates" is what the outputs support. The outcome does not change.
- **Cell 25, the record's notes and the metadata_insufficient finding, "such as the release of the center object":** both 2016 papers (`paper/`) say M "was identified from motion-capture data as the monkey released the center object". As written, the explanation names the paper's own definition of M as the "later event". The hypothesis that fits the outputs is the task software's center-release event marker (2015 Methods, Behavioral Task), not the release as seen in motion capture. This wording does not change the outcome.
- **Attempt-record finding (data_missing, monkeys X and Y):** "[dandiset 001209] holds monkey X (with session 20121219 in its held-out-calib split)". No notebook output shows this; cell 4 names only 001209 and monkey X. No outcome depends on it.
- **Cell 8 (data check, not a conclusion):** "all intervals positive". In cell 7, reward minus contact has a minimum of 0.000, so the intervals are non-negative, not all positive.

Everything else checks against the outputs:
- the "**Result:**" cells 18, 26 and 29;
- the rest of the Summary;
- the README's outcome table and its onset paragraph;
- all outcome notes and findings in the record. This includes the trial numbers 201–673 with 61 absent, the 473 and 387 counts, the runs of 118, 159 and 135 trials, decoding at 0.99 against 0.42, the minival scale factors of 0.955–1.016, the misplaced trial number 127, and the EMG statements (DLTa, BCPs and TCPlat at 50% of peak at −40 ms, 8 of 16 muscles before onset, DLTa and BCPs peaking 0–20 ms after it).

**Round-1 reasons in the record:** they match my round-1 report and are in my wording. The movement-time reason keeps my "about 40 to 55 ms". The cosmetic point and the `prev_present` point are attached to the right claims. My round-1 point 6 (cells 11–15) is not recorded, which is correct because it feeds no claim.

### 3. Round-1 points

| Round-1 point | Status |
|---|---|
| 1. Onset never checked; movement-time outcome | **Resolved.** All three outputs I asked for were added (cell 23), and the outcome changed to blocked, metadata_insufficient. |
| 2. `prev_present` approximation | **Resolved.** Its limits are stated in cell 19 and in the record. |
| 3. Floating-point residue | **Resolved.** Medians now print as whole milliseconds. |
| 4. Object naming | No action was needed. |
| 5. Archive check | No action was needed. |
| 6. Cells 11–15 | No action was needed. |

**What remains that bears on a conclusion:** nothing changes an outcome. Two wording points touch the movement-time conclusion:
- the Summary and the record notes say "shown" or "shows" where the evidence supports "very likely";
- "release of the center object" names, as the later event, what the authors' own papers give as the definition of M.

The other points need text changes only: the README's "first 53 minutes", cell 0's "eleven", and the 001209 statement that no output supports.
