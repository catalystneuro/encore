**Round 2 verifier report: Najafi et al. 2020 on DANDI:000016 (attempt najafi-2020-01)**

**1. Outcomes**

The claims file has 38 claims and the attempt record has 38 outcomes. They are 7 reproduced, 3 partially reproduced, 14 not reproduced and 14 blocked: 4 data_missing, 3 methods_underspecified, 6 other and 1 too_large. The README's groups add up to the same counts.

- **Agreement:** I agree with all 38 outcomes as the claims file's criteria apply them to the printed outputs.
- **Blocked_by for figs1b:** the record keeps data_missing where I had metadata_insufficient, and records the disagreement. Either category is reasonable, because no session clock exists.
- **`assumed: true`:** no outcome carries it. The three assumptions from round 1 (fig2bd, fig6bc, fig7) were withdrawn, and those claims are now blocked as the claims file's rule requires.
- **Unflagged reliance on one reading:** five outcomes rest on reading (a) of early and late days alone, because reading (b) gives 0 or 1 days. They are fig8de, fig8f, fig8g, figs13ab and figs13c. The record states this in each deviation, and it is reasonable. But under the claims file's rule an untestable second reading means the outcome rests on one reading, so these five should be marked `assumed: true`.

**2. Sentences the printed numbers do not support**

None of these changes an outcome. Most look like text left over from an earlier run; the attempt record's notes repeat each one.

- **02 cell 6 (fig3bc):** "Mean accuracies are E 65.3, 64.3, 60.2, 67.3 and I 64.5, 66.0, 58.5, 69.6 percent (p = 0.63, 0.21, 0.57, 0.16)". Cell 5 prints E 67.2 for mouse 4; I 64.6, 66.1, 58.8; and p = 0.661 and 0.59.
- **02 cell 9 (fig3hi):** "differences -0.08 to +0.72 points, p 0.69 to 0.98". Cell 8 prints −0.05 to +0.70, p 0.678 to 0.989.
- **02 cell 15 (figs6de):**
  - "mouse 3 p 0.12 to 0.73": cell 14 prints 0.12, 0.25, 0.76.
  - "mouse 4 accuracy 44.0 to 47.6": the main set gives 44.0, 47.7, 46.3.
  - "(p 0.26 to 0.99)": the smallest printed p is 0.279.
- **02 cell 18 (fig4bd):**
  - "p 0.55 to 0.97": cell 17 prints 0.212 to 0.993.
  - "smallest p 0.056": the smallest per-mouse p is 0.098.
- **C-grid check, in every decoder deviation and in the Summary of 01 cell 53, 02 cell 26 and 03 cell 25:** "differs by 0 to 0.67 points" / "at most 0.67". 02 cell 25 prints differences of 0 to 0.44.
- **03 cell 12 (fig8ab):**
  - Mouse 1 inh "0.53": printed 0.51.
  - Mouse 2 "0.23, 0.20 (p = 0.13, 0.19)": printed 0.22, 0.19 (p = 0.15, 0.2).
  - Mouse 4 "0.56 (p 0.00042) … 0.068": printed 0.55 (p 0.00056), 0.069.
  - Reading (b) "0.06" and "0.11": printed 0.07 and 0.14.
  - The `measured` list in the record (0.23, 0.2, 0.56) is wrong in the same way.
- **03 cell 15 (fig8ce):**
  - "r = -0.49, -0.41; p = 0.0013, 0.014 … inhibitory (r = -0.07)": cell 14 prints exc −0.43 (p 0.0089) and inh −0.13.
  - "r -0.26 to 0.08, p >= 0.12": printed −0.24 to 0.02, p ≥ 0.15.
  - The `measured` list (−0.05, −0.26, −0.14, 0.08) does not match the printed −0.07, −0.24, −0.12, 0.02.
- **03 cell 18 (fig8de):**
  - "p 0.22 to 0.91": printed 0.23 to 0.89.
  - "p 0.0013 to 0.032": the maximum printed is 0.031.
  - "(p = 0.07, 0.26)": printed 0.086, 0.27.
  - "I 67.6 against E 60.5, p = 0.024": printed I 67.8, E 60.6, p = 0.019.
- **Attempt record, fig1b deviation:** "1983 of 26021". 01 cell 3 prints 1982 of 25883.
- **README:**
  - "03 … about 50 minutes" against 36.4 min printed.
  - "01 … about 30 minutes" against 36.5 min.
  - "04 … about 20 minutes" against 12.8 min.
- **Minor, 01 cell 41:** "(mouse 2 EI p = 0.05)" is counted as holding, but at the printed precision it is not shown to be below 0.05.

All other Result sentences, the Summary tables and the remaining README statements match the outputs.

**How the record states my round-1 reasons:** the reasons are mine. Text from my problems list has been attached to the matching claims; that is a fair paraphrase. Two exceptions:
- The figs1b reason adds "against data_missing in the record". I had no attempt record in round 1, so I made no such comparison.
- figs1b is marked `agrees: true` even though the blocked_by category differs.

**3. Round-1 points**

Resolved:
- **1 (trial exclusions):** the data check shows there is no column for helped trials or first trials, so these exclusions cannot be applied. This is now a deviation and a finding.
- **3 (16 Hz trials):** the per-rate table now groups on rounded rates, and the 138 trials at 16 Hz are excluded everywhere.
- **6 (per-bin weights):** these were added, and fig3df is now partially reproduced.
- **12 (`starting_time`):** a deviation of 0 s is printed.
- **figs3c precision:** printed to 3 decimals, 9.883 against a bound of 9.9.
- **Metadata items:** the trial columns, behaviour keys and imaging (Ophys) keys are all printed.
- **Exact fig2bc p-values:** printed.
- **fig3b:** rerun with C chosen at every bin for mice 2 and 3 (notebook 04). The outcome rests on mouse 3, which still peaks at bin 6 under both C rules.
- **9 (matched activity):** shown. The claims file's median rule keeps neurons whose median activity is zero, and a variant matched on mean activity was added.

Not affecting conclusions and unchanged: 5, 7, 8, 11.

Remaining points that bear on a conclusion:
- **Claims-file misreading (my problem 2, figs6de):** the criterion requires above-shuffle accuracy on incorrect trials in every mouse. The paper's S6D, S6E and S3E legends do not support that for mouse 4. This is still open; it was referred to a reader and the claim was tested as written.
- **Seed sensitivity (new):** two knife-edge outcomes rest on one draw of 50 shuffles, with no repetition across seeds.
  - figs3c: reading (b) gives 9.883 against the bound of 9.9. A value of 9.9 or more would make the readings disagree and the claim blocked.
  - fig2bc: mouse 2 p = 0.040; the empirical variant gives 0.10. Under the criterion's stated rule a non-significant mouse 2 could make the claim reproduced.

  fig2a used 20 repetitions for this reason; these two did not.
- **fig8ce:** C is still chosen once at bin −1, with 25 splits, for the onset decoders.
- **fig3df:** the per-bin weights also use C chosen at bin −1. Mouse 4's single significant bin (p = 0.012) does not change the band, but per-bin C in mice 1 or 3 is untested.
- **fig6bc, matched part:**
  - The criterion's median match does not equalise activity: the kept inhibitory neurons stay more active in mouse 2 (p = 0.016).
  - Under the mean-matched variant, reading (b) also fails in mouse 3 (II 0.0006 below EE 0.0048), and EI is not between them in mice 3 and 4.
  - The outcome is blocked either way, but the matched component is not robust.
- **Early and late days:** reading (b) cannot be tested, so the five learning outcomes in section 1 rest on reading (a) alone. They should be flagged as assumed.
- **Seven claims still have no analysis:** figs6ab, figs6c, figs7c and figs2 could be tested from the data; fig5a, fig5bc and figs9 are simulations.
- **Stale numbers:** the figures quoted in section 2, including the wrong `measured` lists for fig8ab and fig8ce, need correcting in the conclusions and the record.
