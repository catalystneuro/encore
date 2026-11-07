**Verifier report, round 2: Grosmark & Buzsáki 2016 on CRCNS hc-11**

The claims file has 31 claims, and the attempt record gives 31 outcomes: 13 reproduced, 9 partially reproduced, 8 not reproduced, 1 blocked. Cell numbers below refer to the re-executed notebook, which has been renumbered since round 1.

## 1. Outcomes and assumptions

The claims file's opening comment sets the rule for every criterion: "the outcome is the one all its readings give". I apply it below.

| Claim | Agree? | Comment |
|---|---|---|
| place-cell-count | Yes | SD kernel assumption stated. Only the FWHM kernel matches the count. |
| fig1c-sequence-content | Yes | Holds in 12 of 12 combinations run. The L and S-b readings the criterion requires were not run; this is stated. |
| figs5b, figs5e, figs5f, figs9b, fig2b | Yes | Assumptions stated and reasonable. |
| fig2-pre-contributors-persist | Yes, as assumed | Matches only under D-a, where the fig2b counts miss. Under D-b it is 59.7 to 65.1%. Stated. |
| rigid-plastic-counts | Yes | Partially reproduced: 109/113/108 under D-b, 121 to 123 under D-a. |
| fig2d, figs12 | Yes | Now pooled under all six Y × D readings (cells 103, 108). The first step at or below zero is 10 or 15%, inside 9 to 22% everywhere. The ranking stays Y-a, D-a. Stated. |
| figs2, fig3a, fig3b, fig4a, both figs14, figs16ab, figs17d, figs18 | Yes | The D-b reruns (cell 76) leave each verdict unchanged. |
| figs13-outfield-rate-falls | Yes, with a reservation | With the D-b groups under Y-b, the plastic overall rate falls (two-sided p = 0.047, cell 76), which the criterion excludes. The groups that match the paper's 105 therefore fail under one Y reading. The record states the outcome rests on D-a, but cell 52 does not mention this. |
| fig2e-plastic-removal | Yes, as assumed | Not rerun with D-b groups. Under Y-b D-a and Y-c the upper bound is only 0.004 to 0.009 (cell 96). |
| low-high-rate-split, figs17, figs19c, figs16de, figs11 (blocked) | Yes | |
| **fig4c-coactivation-by-rate** | **No: partially reproduced at best** | The criterion names readings (a) and (b). Under (b) the low-half > high-half condition fails (p = 0.64, cell 85). By the all-readings rule this cannot be reproduced. The within-session argument is reasonable as a preference, but it does not override the rule. |
| **figs16c-low-rate-coding** | **No: not reproduced** (I said partially reproduced in round 1) | The claims file says "the reading(s) that match fix the split", and all six splits match. Under the (ii) splits the gain change reverses: (a, ii) p = 0.046, (c, ii) p = 0.037, (b, ii) p = 0.082 (cell 82). Under those splits the tests fail. The record does not mark this outcome as assumed, though it rests on split (a, i). |
| **fig4d-slow-cells-replay** | **No: not reproduced by the rule** | Under (b, i), (b, ii) and (c, i), high-rate increases exceed low-rate ones in 2 or 3 of 6 readings (cell 89). There even the partial pattern ("high also increases but less") fails. Partially reproduced holds only on split (a, i). |
| fig4e-high-gain-cells-replay | Yes | Reproduced under (b, ii) and under D-b; partial elsewhere. Partially reproduced is the weakest result across readings. |

I found no new places where the claims file misreads the paper. Two gaps, not misreadings:
- figs16c says "the reading that matched", singular, but all six splits match.
- rigid-plastic-counts has no partial clause and names no D reading.

## 2. Sentences the printed numbers do not support

- **Cell 15 and record fig1c: "largest p 7.0e-12".** The largest Tukey-Kramer p in cell 13 is 3.18e-10 (Y-c, D-b, 2D). 7.0e-12 is the Y-a, D-a, 2D row only.
- **Cell 15 and record fig1c: "POST exceeds PRE in all four (p 7.3e-08 to 0.020)".** Cicero has p = 1.61e-19 (cell 14), so the range starts at 1.6e-19.
- **Cell 27 and record figs9b: PRE median "inside only under Y-b, D-b".** Y-c, D-b gives 0.0086, also within −0.011 ± 0.02 (cell 26).
- **Cell 77 and record rigid-plastic-counts response: "no outcome of a group claim changes".** figs13 fails under D-b, Y-b (cell 76), as the same cell then says. fig2e was not rerun.
- **Cells 105 and 110, and record deviations for fig2d and figs12: "Only readings Y-a and D-a were run".** Cells 103 and 108 pool under all six readings. Only the ranking is Y-a, D-a.
- **Cell 112: "This run of the notebook took 71 minutes".** Cell 113 prints 38.2 min. The README and cell 0 say about 40 minutes.
- **Cell 65:** reading (c) "p = 0.035" is one-sided, and this is not said. Two-sided it is 0.07 (cell 76). The record uses two-sided p elsewhere (figs14).
- **Incomplete, not wrong:**
  - Cells 83 (figs16c) and 91 (fig4d) say nothing about the other splits, although cells 82 and 89 print them.
  - The figs16c record notes state the (ii) reversal twice.
  - The cell 112 summary table omits "(assumption)" for fig1c, figs9b and fig4d, which are `assumed: true` in the record.
  - Cell 7 compares a mean NREM interval (1.94 s) with the paper's medians.

All other conclusion, Summary, README and record-note numbers I checked match the outputs.

The record's verification section gives my round-1 reasons faithfully and in my wording. The "28 of 31 agree" count is correct.

## 3. Round-1 points

**Resolved:**
- 5 (fig2d and figs12 readings): outcome robust across Y × D.
- 6 (per-direction pseudo-replication): once-per-cell rerun, verdicts unchanged.
- 8 for figs14: two-sided p now decides.
- 9 (figs5f within-session test): 9 of 13 templates, p = 1e-16.
- 10 (Gatsby spikes past sessDuration): `hc11.py:318` and the rate.
- The sessInfo MD5 now matches (cell 1).
- Event-selection counts and events per NREM hour are printed (cell 6).

**Partly resolved:**
- 2 (D-a groups): D-b reruns are added, but D-a stays the main reading although only D-b matches 105. D-a groups under Y-b and Y-c were never used.
- 4 (rate splits): the splits are now run, but the outcomes still rest on (a, i).
- 11 (laps): the table is printed. Cicero_09102014 still has 2.3 laps per running minute against 5.0 to 7.5 in the other circular sessions, and this is unexplained.

**Remaining issues that bear on a conclusion:**
1. Events lack the LFP-ripple condition: 1,855 events per NREM hour, mean interval 1.94 s, against the paper's 3 s median. This affects every event-based claim, the fig1c L readings, and figs16de.
2. The downstream claims use the SD kernel (565 units), not the FWHM kernel that matches 491.
3. figs13 fails on D-b, Y-b groups. fig2e is not run on D-b groups.
4. Under the all-readings rule: fig4c should be at most partially reproduced, figs16c and fig4d not reproduced.
5. figs11: quality and stability are testable from `<session>.tar.gz` but were not done.
