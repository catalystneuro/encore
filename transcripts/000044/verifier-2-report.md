# Verification report, round 2: Grosmark & Buzsáki 2016 on dandiset 000044 (0.261005.2101)

I counted from the claims file and the attempt record. There are 20 claims. The record's outcomes are: 3 reproduced (sessions-and-tracks, fig1c-maze-gt-pre, fig4c-pre-fast-coactivation), 6 not_reproduced (place-cell-count, fig1c-post-gt-pre, fig4c-slow-coactivation-increase, fig4c-slow-replay, fig4d-slow-sequences, fig4e-gain-sequences), 3 partially_reproduced (fig2d-shuffle-high-dpcc, rate-split-medians, figs16-low-rate-info-gain) and 8 blocked as methods_underspecified. Cell indices below are positions in the notebook's cell list. I did not need the paper text for this round, so nothing new is under `paper/`.

## 1. Outcomes

I agree with all 20 outcomes.

- **sessions-and-tracks, reproduced.** Agree (cell 13).
- **place-cell-count, not_reproduced.** Agree: 417 at 1 Hz (cell 16). The notes now say 480 at 0.5 Hz falls within tolerance.
- **fig1c-post-gt-pre, not_reproduced.** Agree under the criterion's pooled test: 0.763 against 0.770, p = 0.412 (cell 19).
  - The same test run separately on each kind of track finds POST above PRE on both: linear p = 5.1e-07, circular p = 1.1e-05 (cell 25).
  - So the failure comes from pooling the sessions together. The record says this clearly.
- **fig1c-maze-gt-pre, reproduced.** Agree (cells 19, 23, 25).
- **fig2b-strong-contributors, blocked.** Agree.
  - The criterion's test has a false-positive rate of 0.561. The best-template variant still has 0.206 (cell 28).
  - The null is computed on every fourth event (`first_pass`, `sub = v[::4]`). A biased test gets more significant with more events, so these rates probably understate the real false-positive rate. That makes the case for the block stronger.
- **fig2-pre-post-overlap, blocked.** Agree.
- **fig2d-shuffle-high-dpcc, partially_reproduced.** Agree, going by the letter of the criterion.
  - The condition that holds (replay absent after shuffling the top 10 or 20%) tells us nothing, because the pooled baseline shows no replay either: p = 0.916 (cell 38).
  - The informative evidence is on the linear tracks. In sample it shows the paper's pattern, and random 10 and 20% shuffles leave replay intact. Out of sample (cross-validated), shuffling the top 10 or 20% lowers replay from +0.116 to +0.046 and +0.042 but does not remove it (cell 40). The notes say this.
- **fig2e-remove-plastic, figs2-track-distribution, fig3a-plastic-specificity, fig3b-plastic-improve, fig4a-rigid-faster, fig4a-plastic-ripple-burst-coactivation, blocked.** I now agree; in round 1 I disagreed. These claims depend on fig2b in the claims file, and the protocol blocks a claim whose dependency is blocked. The new outputs also show the rigid and plastic classes are drawn from a selection that lets through nearly every place cell on the linear tracks: all but 1 to 3 per session (cell 28). The analyses are still shown, which is enough.
- **The three fig4c claims (reproduced, not_reproduced, not_reproduced).** Agree (cell 61).
- **rate-split-medians, partially_reproduced.** Agree (cell 68).
- **figs16-low-rate-info-gain, partially_reproduced.** Agree (cell 71).
- **fig4d-slow-sequences, not_reproduced.** Agree under the pooled test (cell 74).
- **fig4e-gain-sequences, not_reproduced.** Agree under the pooled test (cell 77).

## 2. Text against printed outputs

Most best-template numbers in the text do not match the printed outputs; they look like they come from an earlier run. None of them changes an outcome, because every affected claim is blocked and none of the thresholds is crossed. But the sentences below are wrong as they stand. The same stale numbers appear in the attempt record's notes, in its responses for fig2b, fig2-overlap and fig2e, and in the notes for fig3a, fig3b, fig4a-rigid-faster and fig4a-plastic-ripple-burst-coactivation.

| Cell | Text | Printed |
|---|---|---|
| 29 | "finds 188 cells"; "0.132 in PRE" | 190; 0.129 (cell 28) |
| 32 | "72 of 102 (70.6%) ... chance level of 37.9%" | 71 of 104 (68.3%), chance 37.6% (cell 31); still within 73 ± 7.3 |
| 44 | "best-template classes ... -0.125 (p = 1.0) and +0.020 (p = 0.24)" | -0.121 and +0.016, p = 0.33 (cell 43) |
| 50 | "best-template classes p = 0.0035"; fields "p = 0.10" | 0.00633; 0.126 (cell 49) |
| 53 | "With the best-template classes plastic cells increase (p = 0.020)" | 0.0142 (cell 52) |
| 56 | "best-template classes p = 0.74" | 0.691 (cell 55) |
| 59 | "gain p = 0.15, bursting p = 0.11, coactivation p = 0.41" | 0.127, 0.158, 0.378 (cell 58) |

Other sentences that the outputs do not support:

- **Cell 0:** "their analyses are still shown, with a better calibrated variant of the contribution." The variant's false-positive rate is 0.206 (cell 28), and the record's response to my round-1 point says "the text no longer calls any of these calibrated".
- **Cell 47:** "All three are close to the threshold." The three p-values are 0.072, 0.079 and 0.119. The last one is not close.
- **Summary (cell 79):** "shuffling the top 10 to 20% of cells reduces replay out of sample without removing it". This holds on the linear tracks. Over all sessions, the cross-validated within-session variant has top20_cv at p_within = 0.0597, so there replay is removed (cell 40). The sentence needs "on the linear tracks".
- **Attempt record, fig4d:** "p below 0.0001 for each". high_rate prints p_within = 0.0001 (cell 74). Cell 75 says "p <= 0.0001", which is correct.
- **README:** "about eleven minutes on four cores". The timed steps alone add up to about 14 minutes: 201 s + 405 s + 250 s (cells 5, 11, 38).

Every other sentence I checked matches the outputs. That covers the Result cells for sessions, place cells, fig1c, fig2b (apart from the table above), fig2d, fig2e (pooled, linear and cross-validated), figs2, the fig4c claims, rate-split, figs16, fig4d and fig4e, plus the rest of the Summary, the README table, and the record's findings and its other notes.

The `verifications` block states my round-1 reasons accurately and in my own words, outcome for outcome. Where it adds "It asked for ...", that matches section C of my round-1 report.

## 3. Round-1 points

**Resolved:**

- **Problem 3 (circularity in fig2d and fig2e).** Random-shuffle and random-removal controls and a cross-validated even/odd control were added (cells 38, 40, 43). Their results are reported honestly, including that out of sample the top-dPCC shuffle reduces replay without removing it.
- **Problem 4 (fig2d wrongly blocked).** Now tested, and depends_on is corrected.
- **Problem 5 (place-cell threshold).** The text now says the count depends strongly on the threshold.
- **Problems 6 and 7 (50 shuffles in the variants; scipy's Tukey HSD).** Both are recorded as deviations.
- **Problem 1 (biased contribution measure).** Shifts are now drawn afresh for every event (`cell_contributions`, line 555). The template selection is identified as the main cause of the false positives. The best-template variant is reported, and the block is kept. Two things remain: the "better calibrated" wording in cell 0, and the null computed on a quarter of the events (see section 1).

**Partly resolved:**

- **Problem 2 (pooling across sessions).** It is disclosed, and per-track and within-session tables were added. The criterion is unchanged, as it has to be. So fig1c-post-gt-pre, fig4d, fig4e and the informative half of fig2d are still judged by a test whose unmanipulated baseline finds no replay (p = 0.916). These outcomes say little about the paper.

**Not addressed:**

- **Problem 8 (MAZE immobility from 2D speed, running from linearized speed).** Not recorded as a deviation. It does not affect a conclusion.

**What remains that bears on a conclusion:**

1. The stale best-template numbers in cells 29, 32, 44, 50, 53, 56 and 59 and in the attempt record need to be replaced with the printed values. No outcome changes.
2. The fig2d result depends on the pooled-test problem. Read with the controls, the evidence on the linear tracks is that top-dPCC cells are needed for part of the replay, not that shuffling them removes it.
3. Fixing the cell 0 wording and the cell 79 sentence about out-of-sample reduction.
4. Still impossible to check: the supplement (definitions of the PCC test, events and place cells), and comparing event counts with figs. S2 to S4. The per-session event counts are now printed (cell 25), but there is nothing to compare them against.
