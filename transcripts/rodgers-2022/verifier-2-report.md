**Verifier report, round 2: Rodgers 2022 (Sci Data 9, 620), DANDI:000231 v0.220904.1554**

The claims file has 39 claims (`grep -c "^- id:"`) and the attempt record has 39 outcomes, one for each claim. They are 23 reproduced, 0 partially reproduced, 6 not reproduced, 6 blocked (data_missing) and 4 blocked (methods_underspecified). The README table gives the same counts (23 / 6 / 2 + 6 + 2).

A correction to my round-1 report: its totals line ("24 reproduced, 7 not reproduced, 8 blocked") was miscounted. My own per-claim table gives 23 / 6 / 10, which is what the record holds. The record does not repeat my wrong totals.

### 1. Outcomes

I agree with all 39 stated outcomes. No outcome in the attempt record carries `assumed: true`, so there are no assumptions to judge.

- **neural-hours:** the main recordings give 33.770 h and the whole files 33.782 h. Both are within 0.05 h of 33.8 (cell 17), so the outcome no longer depends on how the test recordings are handled.
- **session-labeling-quality:** not_reproduced is now firm.
  - The stop frame is inclusive. `duration_frames` equals `frame_stop − frame_start + 1` on all 290,345 contacts (cell 92).
  - All four readings in the claims file fail (cell 92).
  - Pooling contacts over the whiskers of a session is not a reading in the claims file. It also exceeds 2%: 2.007% and 2.008%.
- **trials-table-structure:** not_reproduced is correct for the claims file as written. Problem 6 below could still change it.

### 2. Sentences the printed numbers do not support

- **Cell 44:** "the other 5 sessions begin at trial 61 or later". Cell 43 prints only the first *random* trial of those 5 sessions (61, 76, 88, 102, 124), not the first trial in each table. The output only shows that those tables start after trial 44. The attempt record says this correctly ("begin after trial 44; their first random trials are 61…").
- **Cell 111 (Summary), last sentence:** "Seven Open Ephys files begin with a short separate segment …, the test recordings the paper mentions."
  - Six of the seven are 14–15 records (0.48–0.51 s) with the same recording number (0) as the main segment (cell 17).
  - The paper describes test recordings as "a few seconds long". Nothing printed shows these segments are test recordings.
  - Leaving them out is a reasonable choice, but here it is stated as a finding. The neural-hours note and cell 18 ("left out as the test recordings") have the same problem.
  - This does not affect the outcome, since both totals fall within 0.05 h.
- **Cell 111 (Summary) and the record's `choice_time` finding:** "on 22% of other trials it falls 0 to 5 ms after the window opening". The 22% is the share of mismatched trials (7,185 of 32,085). Cell 34 does not print how many of *all* non-spoiled trials have `choice_time` 0–5 ms after the opening; matched trials can fall there too. It should read "on the 22% where it is not the first lick in the window, it falls…".
- **README:** "It takes about five minutes". Cell 110 prints a run time of 6.5 min.
- **Attempt record, behavior-clock-drift note:** "the dataset's other files are videos and Open Ephys and Kilosort files". Cell 66 lists 44 `.log`, 88 `.mat`, 88 `.m` and 44 `.py` files, and the notebook never identifies the `.log` files. My round-1 asset query found them to be sorting and acquisition logs. Since there are only 44 of them, in ecephys sourcedata only, they cannot be per-session behavioral logs for all 115 sessions. The statement is right, but the printed output does not back it.
- **Outside the scope of the check:** the cell 0 Method paragraph is out of date. It says Open Ephys sizes come from the asset list, but the notebook now also streams the CH1 record headers, the `.openephys` indexes and the Kilosort `.npy` files.

Every other Result, Summary, README and notes sentence matches the printed outputs. I checked each number: the frame and trial counts, the hours, the reward fractions, the per-session ranges, the unit counts and thresholds, the layer crosstab, the contact fractions, the C0 fractions, the conversions, the ages and the video sizes.

The `verifications` block states my round-1 reasons faithfully. They are close paraphrases of my table, with my problem points attached where they concern a claim. Nothing is misattributed and nothing is softened.

### 3. Round-1 points

| # | Status |
|---|---|
| 1 Contact stop inclusive / pooled reading | **Resolved.** Stops are inclusive (cell 92), and every reading plus the pooled variant exceeds 2%. |
| 2 Open Ephys test recordings | **Resolved for the outcome.** Record headers are read, and 33.770 h is within tolerance. The labelling of the 0.5 s segments is in §2. |
| 3 Right reward = right licks; verdict line | **Resolved.** The verdict line, the conclusion and a metadata_error finding now state it. |
| 4 Layer label disagreement | **Resolved.** It is a case difference only: 999 of 999 agree once case is ignored (cell 71). |
| 5 Keywords constant; reading not stated | **Resolved.** The reading is stated, with a crosstab, and `task_from_metadata` now uses the description first. |
| 6 trials-table-structure: "next trial" reading | **Open.** The question is with a reader (questions/000231.yaml), and the variant holds on all 32,230 consecutive-number pairs. If the reader adopts the next-trial-run reading, the outcome would become reproduced. |
| 7 Container frame count overwritten | **Resolved.** It is now printed: no video stream reports a frame count (0 of 115). |
| 8 Amplitude criteria | **Resolved.** Amplitude drift is reported outside the outcome (max 1.47%/min over 893 matched units). The rest are correctly stated as not runnable. |
| 9 KF134 2018-02-09 clock | **Resolved.** Leaving out its 16 units changes no count. |
| 10 Table 4 columns | **Resolved.** They are checked in all 44 files. |

**What still bears on a conclusion:**
- **Problem 6 (trials-table-structure):** the outcome depends on how the claims file reads "next trial", and the reader's answer is still pending.
- **A claims-file reading in session-labeling-quality (reported, not corrected):**
  - The claims file takes the 2% bound per whisker. The paper's "≤2% of the contact events" of a session reads more naturally as pooled over whiskers.
  - Under the pooled reading the outcome would still be not_reproduced. But it would rest on one contact in one session: 54 of 2,691 contacts is 2.007%, and 53 would be 1.97%. It also depends on the helper's rule that a frame absent from the processed series counts as missing.
  - The per-whisker reading fails clearly at 7.7%, so the outcome stands as tested.
