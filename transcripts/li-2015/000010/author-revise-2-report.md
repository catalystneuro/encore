I've worked through every point in the round-2 report and re-run the entry. The run passed, `tools/entry.py check` passes and the attempt record matches its schema. Nothing is committed.

**Outcomes:** none changed; they are still 8 reproduced, 4 partially reproduced, 4 not reproduced and 11 blocked.
- **imaging-selectivity-counts:** I agree with the verifier. The criterion has only a reproduced condition (all values within tolerance under one reading) and no reading meets it, 0 of 16. Round 2 may not change an outcome, so it stays `partially_reproduced`, and I wrote a proposed change to `not_reproduced` under `proposed`. A new notebook cell backs this with a count per reading: four of the five values are within tolerance in 12 readings. The selective count is within tolerance in only 4 readings, and in all 4 the task-related count is too high. The notebook's conclusion and summary, the README table and the notes all say a change is proposed, so a third verification round is needed.
- **fig2e-no-contra-bias-spikes:** still reproduced. The measured value is now 7.97 (it was 8.5). That comes from the only reading where both the absence test and the 8% value hold: selective neurons, delay window, light trials left out, P = 0.060. The conclusion and notes now say the claims file has no rule for judging a claim of absence across its readings, so the outcome depends on which reading is taken. They also report the paper's second P = 0.13 test.

**Outputs added and statements corrected:**
- **"66 extracellular trials":** the notebook now splits them by kind. All 66 are extracellular; the 28,508 they were counted against include the imaging trials. In 65 the go cue comes too soon and in one too late (2.68 s). Another 75 extracellular and 2 imaging trials have no go cue and are also dropped. The data check, the deviation and the finding are corrected.
- **Placeholder trials:** "most in the first or last tenth" is now "754 of 1,540 (49%)", and the notebook prints that share.
- **Spikes outside trial windows:** the notebook now prints where they fall. In 97 of 99 sessions at least 99% of spikes are inside a trial window. In two sessions (mice 214429 and 219031), 24% and 30% fall between trials, and none come before the first trial or after the last. The data check, the ed1 deviation and the finding now say this.
- **Light trials:** the notebook now prints 4,332 of 14,388 correct trials, and the finding uses that figure in place of the unsupported 18,385.
- **Imaging dips to 0:** my earlier "single frames" was wrong for about a third of the ROIs. Of the 3,403, the longest run at or below 0 is one frame in 2,034, two to seven frames in 1,199, and eight frames (0.5 s) or more in 170. The notebook and notes now say this.
- **README:** I removed the untested explanation for the PT result ("with the trials pooled there are more of them"). It now says the result reaches P < 0.05 only with light and no-light trials pooled, and that the reason was not tested.
- **Record of round 1:** I fixed the garbled fig2c reason ("273-326 to 377-408") and added the missing (b)(delay)(t2) result to the fig2e reason.
- **Record of round 2:** added under `verifications`, with all 27 claims. It includes the verifier's correction to its own round-1 text on reaction-time s.d. (the 29 to 51 ms range holds only for the (z) readings).

**Not done:**
- **Lick trace:** I added nothing on whether it is the photodiode signal. The files don't say, and the record already lists this as a deviation and a finding.
- **Figure-only values:** I didn't read them off the figures. The report names no claim whose outcome depends on them.
- **Imaging early licks:** these trials still can't be excluded, because the imaging files flag none.

The first run of the entry failed on a dropped connection to DANDI (connection reset) and the second run passed. After that run I edited only text cells, so the executed copy has the old wording in those cells but the same numbers.
