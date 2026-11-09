# Round-2 verifier report: Nakagawa et al. 2026, DANDI:001968 v0.260914.1316

Counts are taken from the claims file and the attempt record. The claims file has 45 claims and the record has 45 outcomes, one for each claim: 2 reproduced, 6 partially_reproduced, 4 not_reproduced and 33 blocked (32 data_missing, 1 methods_underspecified).

## 1. Outcomes and assumptions

**I agree with these outcomes, unchanged from round 1:**
- link-unit-mice: partial.
- link-photometry-mice: partial.
- ed4a and ed4b: blocked.
- ed4c: reproduced.
- The 13 event-time claims and the 4 histology claims: blocked.
- fig1d-prelearned and the 12 other behaviour claims: blocked.
- figs6d: blocked, methods underspecified.
- fig1d-young: not reproduced.

**Changed or re-based since round 1:**
- **units-recorded (was not_reproduced, now partial).** The criterion only says when the claim is reproduced (both totals within tolerance). Only young APP-KI is within: 891 against 846±85. Young WT is 635 against 479±48 (cell 30). "Partial" is acceptable only by the reading the record uses for fig4b and figs7, that part of the criterion holds. The record does not say why the round-1 outcome was changed. I accept partial on that reading.
- **fig1e (was not_reproduced, now partial).** No single reading meets the criterion (cell 47). Under B1 both means are within tolerance but p=0.067. Under B2, p=0.046 but WT is 90.0%. Partial is acceptable on the same reading as above. Again the change is not explained.
- **fig4b: partial. I agree.** Under the adopted unit (mice, B1, 1–4 s) the T1 means are 1.17, 1.66 and 0.55, all within tolerance (cell 53).
  - With 5 mice, the signed-rank test's smallest possible p is 0.0625. So under the adopted unit the significance half of the criterion is ruled out by the design, not tested.
  - Under the sessions variant, Odor-1 at T5 fails (p=0.084). Partial holds either way.
- **fig4c: not reproduced. I agree.** It fails under both units (cell 57). Under mice, the Odor-1 and Odor-A conditions cannot pass because of the n=5 floor. Under sessions, Odor-1 is significant at T1 (B2) or T2 (B1), Odor-1 in error sessions is significant at T4, and Odor-A in error sessions is not significant at T1.
- **fig4d: not reproduced. I agree.** In the 1–4 s window (G1), mice give interaction p=0.16 and T1 Tukey p=0.059; sessions give 0.23 and 0.17 (cell 61).
- **fig4e: not reproduced. I agree** (cell 64).
- **fig4f: reproduced. I agree,** with the caveat the record states: 1 or 2 WT error sessions (cell 67).
- **figs7: partial. I agree.** Under mice, Odor-B against Odor-1 gives p=0.055. Under sessions, both comparisons pass (cell 70). The outcome depends on the unit, and the record says so.

**Assumptions (`assumed: true` on fig4b, fig4c, fig4d, fig4e, fig4f, figs7, fig1d-young, fig1e):** each is stated in the deviations and each is reasonable.
- **Timing (1 kHz, cue at sample 1000).** Each trial is z-scored to exactly samples 0–999. The noise peaks at 120/180/240 Hz. The pooled mean has its largest step at samples 1001–1002, and so does each odor code (cells 15, 21).
- **Odor and action codes.** The block tables give r≈0.97 on the diagonal (cell 17), and the action-by-odor cross-tabulation is consistent (cell 13).
- **Mouse mean as the unit.** It is derived correctly from F(4,80) (cell 50). Its cost should be stated plainly in the fig4b and fig4c outcomes: it makes the signed-rank parts impossible to pass.

## 2. Text against the printed outputs

**Numbers.** Every number in the "**Result:**" cells (25, 28, 32, 35, 39, 45, 49, 55, 59, 62, 65, 68, 71, 75), in the Summary (cell 76), in the README and in the record's notes matches the printed outputs. I checked each one. I found no sentence that the numbers contradict.

**Wording and editorial defects:**
- **Cell 76, Summary:** "Unit counts exceed the paper's in most groups." Cells 30 and 31 show all six groups exceed the paper's counts, including young APP-KI (891 against 846). It should say "in every group".
- **Cell 76, Summary table:** "(assumed)" is attached only to fig4b and figs7. The record has `assumed: true` on fig4c, fig4d, fig4e, fig4f, fig1d-young and fig1e as well.
- **Duplicated text in the attempt record.** These do not affect any outcome:
  - Duplicated passages:
    - the units-recorded notes ("No rule over sessions …" through "… the paper's 125.");
    - the figs6d notes ("Reading (b) takes the SD …");
    - the fig1d-young notes (the power sentence);
    - the `selection_undocumented` finding ("No rule over sessions …").
  - Duplicated deviations:
    - the 00266_20190405 deviation, in fig4b, fig4c, fig4e and fig1e;
    - the type III deviation, in fig4d, fig4e, fig4f and fig1d-young.

**Round-1 reasons.** The attempt record does **not** state my round-1 reasons, in my words or otherwise. It has no section recording the verifier's points or the author's responses. Its keys are schema_version, id, dataset, paper, date, entry, provenance, inputs, outcomes and findings. The responses appear only as changes to the analysis. The outcome changes for units-recorded and fig1e are not explained anywhere.

## 3. Round-1 points

**Resolved:**
1. **Unit of analysis.** Mice are now adopted and sessions are a variant, with the F(4,80) argument stated (cell 50). Some residue remains (below).
2. **Rank-sum against signed-rank.** The signed-rank test is adopted, with its reason stated, and the rank-sum test is shown as a variant (cells 50, 53, 55).
3. **Power on 10 of 27 mice.** Power is now stated: 0.69 for fig1d and 0.23 for fig1e, and both conclusions say a failure is weak evidence (cells 44, 48).
4. **ed4a two-class variant.** It is now reported: χ²=39.0, p=4.1e-10 (cell 34).
5. **00266_20190405.** Under B1 it is now neither correct nor error (cells 47, 51; `is_error`). The fig1e conclusion is based on 83.3% and p=0.067.
6. **Cue check.** There is now a check that does not depend on the z-scoring: the step at samples 1001–1002 (cells 21, 22). The sampling rate itself is still an assumption, and the notebook says so.
7. **figs6d reading (b).** The issue is now explained in the conclusion (cells 74, 75).
8. **Type III ANOVA.** `two_way` now uses type III with sum-to-zero contrasts. The interaction terms are unchanged, as expected.
9. **Unit surplus.** It is now documented per mouse and per odor set (cell 31), though not explained.

My round-1 "not checked" items are also covered now: the unit and photometry file contents (cell 5), hemisphere metadata (none exists, cell 6), and the cue trace (cell 21).

**Remaining issues that bear on a conclusion:**
- **fig4b and fig4c.** Under the adopted mouse unit (n=5), no signed-rank test can reach p<0.05. Those parts of the criteria are therefore settled by the choice of unit, not by the data. The outcomes stand because the sessions variant gives the same outcome (partial and not reproduced). Each outcome should say this explicitly rather than "cannot hold".
- **figs7.** The outcome depends on the unit: partial under mice, reproduced under sessions. Neither unit is the paper's hemisphere.
- **units-recorded and fig1e.** The outcomes were changed from not_reproduced to partially_reproduced. The criteria define no partial branch, and the record gives no reason for the change. The record should either state the reading that justifies "partial" or revert to not_reproduced.
- **Attempt record.** It does not record the round-1 points and the author's responses, so the requirement that it state my reasons cannot be met.

I found no place where the claims file misreads the paper.
