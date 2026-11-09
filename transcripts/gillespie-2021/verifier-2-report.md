**Verifier report, round 2: Gillespie et al. 2021 on DANDI:000115 (0.210914.1732)**

The claims file lists 33 claims. The attempt record has 33 outcomes: 2 reproduced (fig1d-sessions-blocks, fig1ef-reward-rate) and 31 blocked as too_large. There is no separate entry README among my materials, so I checked notebook cell 0, which acts as the entry text.

### 1. Outcomes

| claim | agree? | note |
|---|---|---|
| fig1d-sessions-blocks: reproduced | yes | Cell 20 matches round 1: 25/32/24/33 sessions and 88/85/109/166 blocks under reading (a); 26 of 26 candidates pass under (b) (jaq 88–93 blocks). The new variant leaves out one more jaq or despereaux epoch: 25/25 and 24/24 choices pass (jaq 82–87, despereaux 100–108 blocks). |
| fig1ef-reward-rate: reproduced | yes | Cell 23. The per-trial table is now printed and agrees with the summary columns. The plain reading of "rises" holds in all subjects. |
| fig6b-visits-decay: blocked, too_large | yes | The replay half is still not testable. The behavioural half (cell 27) holds in jaq, despereaux and montague (last significant trial +2 or +3) and fails in roquefort at +29 with the tie-corrected test. Without tie correction all four end at +2. |
| the other 30 claims: blocked, too_large | yes | Unchanged from round 1. |

The claims file reads the paper correctly on the points that bear on these results. I checked the Methods text on excluding "sessions 1 and 3 of subject 1", the trial-wise visit curves, and the eight-block limit.

### 2. Statements the printed outputs do not support

- **All 31 blocked notes in the attempt record:** "5 to 8.4 MB/s … (8.4 MB/s in the latest run)". Cell 12 of this run prints **9.5 MB/s** (77 MB in 8.1 s; 267 h for the dandiset; 73 min for one epoch). "Over an hour" and "hundreds of hours" still hold, so the reason stands, but the stated rate is wrong.
- **Cell 7 and the attempt record's finding:** "one more reward pump (arm 8) **226 s after the last logged reward**". No output prints this. Cell 15 prints the last logged trial at 2592 s and the extra pump at 2632 s, which is 40 s after the last trial. The 226 s may be right if measured from the last reward, but nothing printed shows it.
- **Cell 0:** "55 of its files were rewritten in January 2022". Only one file is compared (cell 10, montague day 4). Nothing printed shows 55.
- **Finding (metadata_error):** "110 of 116 run epochs **end with** 1 to 4 NaN position timestamps". Cell 10 prints the count of epochs with NaN timestamps, not where in the epoch they fall.
- **Cell 28 and the fig6b note:** "trial +1 (the closing trial)". `visit_traces` also takes the open last block of each session (any block with at least one reward). There, +1 is simply the next trial in the same block. The 0.84–0.90 figure covers both kinds of block.
- **fig1ef note:** "The closing-trial rule moves trial 15 for roquefort … and montague's Spearman rho …". This is true but incomplete. The rule also moves despereaux's rho (0.996 → 0.979) and its lowest 1F bound (0.420 → 0.429). It also moves jaq's trial 15 under reading (b) (0.696 → 0.681). No condition changes.

I checked every other sentence of the "**Result:" cells (21, 25, 28), cell 29, the Summary (cell 30), cells 4/7/9/11/13/16/18 and the record's notes against the outputs, and all of them hold. That includes 383/35/5 closing trials, 26/26 candidates, ratios within 5%/8%/4% and errors 11–24% over, 94/95/112/169 goal traces, 9 of 39 against 8 of 170 at p = 1.6e-4 / 0.074, and 0 of 116 logs with a multi-arm CURRENTGOAL line.

**My round-1 reasons in the attempt record:** they are faithful to my report and mostly close to my wording. "I confirmed" becomes "the verifier confirmed", and problems 1–4 and 6 are folded into the fig1d and fig1ef reasons accurately. No reason is misstated.

### 3. Round-1 points

**Resolved:**
- **1 (9- and 3-reward blocks):** explained in cells 15–16. Both follow a closing trial that was a rewarded visit to the new goal, and the outerreps printed are 10 and 4. The text was corrected.
- **2 (five logs without a header):** none has a multi-arm CURRENTGOAL line (cell 15).
- **3 (arms in jaq day 6 epoch 4):** the DIO beam breaks show arm 6 was never entered, including after the last logged trial. It is the only jaq session with fewer than eight arms.
- **5 (arms 1 and 8 not adjacent):** documented in the helper module's docstring. Only the error subtypes use it, and no test here does.
- **6 (E_rises stricter than the criterion):** acknowledged, and the plain reading was added and holds.
- **7 (behavioural half of fig6b):** computed in cell 27.
- **Section C requests:** all supplied (trial counts against the legends, per-session table, DIO arms, per-trial 1E/1F values, fig6b curves).

**Partly resolved:**
- **4 (the extra jaq and despereaux epochs):** these are still not identified. The leave-one-out variant shows the fig1d outcome does not depend on which one it is, so the conclusion is unaffected. The record notes that the paper's repository holds a saved filter output with per-animal epoch lists that might identify them; it was not used.

**Remaining points that bear on a conclusion:**
- **fig6b behavioural half:** the roquefort result depends on whether the rank-sum test corrects for ties, and that question is still open. To my knowledge, MATLAB's `ranksum` (the paper's code is MATLAB) corrects for ties in its normal approximation. If so, the tie-corrected form is the code's, and the behavioural half fails in roquefort under both bounds. The notebook did not look at why trial +29 is significant. The outcome stays blocked either way.
- **Error-trial labelling:** error trials are 11–24% above the Figure 5B counts (cell 17). No tested claim uses them, but any later analysis of correct against error trials would.
- **Corrections needed in the text, none changing an outcome:**
  - the streaming rate stated in all 31 blocked notes (9.5 MB/s, not 8.4);
  - the unprinted "226 s", "55 files" and "end with" statements;
  - the "+1 (the closing trial)" wording for fig6b.
