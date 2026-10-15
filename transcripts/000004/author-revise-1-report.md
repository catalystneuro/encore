I've revised the attempt for every point in the round-1 report. The entry passes `check` and re-runs cleanly in 175 s, and every conclusion matches the new numbers. Nothing is committed.

**Changes to outcomes**
- **previous-release-additions** went from blocked to partially reproduced. Faraut et al. 2018 (doi:10.1038/sdata.2018.10), the paper describing the earlier release, lists that release's sessions by id in its Table 1, so the claim could be tested after all. The dandiset has 23 new sessions and 17 new subjects, as the paper says. Those sessions hold 325 units, not 288. The paper's 288 equals 1864 − 1576, so it looks like a difference of the two releases' totals, not a count of the new sessions.
- **previous-release-link** is a new claim, which the protocol requires when outside data is matched to sessions. It is partially reproduced: 64 of the 65 earlier sessions are in the dandiset under the same subject and task variant. Session 98 (subject H48) is missing.
- **fig3-example-vs-neuron** stays blocked, but the reason changed from data missing to metadata insufficient. The paper's code labels session 144 as a recording of subject T103, whose one session in the dandiset is 2009. In 2009 one unit on channel 140 in the right hippocampus is visually selective and fires most to phones (p = 1.3e-9). Its index does not match the label's cell number 3, and nothing maps 144 to 2009, so the neuron can't be confirmed.
- All other outcomes are unchanged; the verifier agreed with each of them.

**What I added or corrected**
- **Memory-selective counts:**
  - The main count (110) is not distinguishable from the shuffled-label null, now 10 shuffles per unit (5.4%, binomial p = 0.18).
  - A second bootstrap seed gives 118 for the main count, and 149 (against 147) for the paper code's choices.
  - Per-unit p-values are printed for the 288 units selected under any reading or seed.
- **Methods against code:** the conclusions for the memory-selective, dual and Figure 5f claims now say their outcomes come from the paper's Methods disagreeing with its code, not from the data.
- **Figure 5f:** 95% intervals for each site's percentages are printed, and the conclusion says the site comparison has little power with only 77 TWH units.
- **Event codes:** the check now confirms each response code matches its block (learning or recognition), and the result is still 78 of 87 files. Files without a start code and with an extra end code are listed.
- **Smaller fixes:**
  - The impedance column is shown to be stored as NaN.
  - The AUC under the paper's stated label coding is recomputed (0.247).
  - The two ROC p-values are printed to four digits, with a per-session table.
  - Units per session and per site are printed.
  - The diagnosis differences for C56, H51 and T90 are named.
  - The missing encoding trials in the 8 short sessions are described.
- **Records:** the helper module now holds a text copy of Faraut 2018 Table 1, and the claims file explains when the new criteria were written. The attempt record has the new input, three new findings and the round-1 verification record. The README and the notebook's header and summary are updated.

**Not done, and why**
- The extra unit (1864 against 1863) still can't be named. The paper gives no per-session counts in its text, and I did not read values off the figures.
- The verifier's point on the shared clock needed no change. The notebook already lists the 49 sessions where it could not be shown and says the clock is assumed there.

The Faraut 2018 article and tables, and this paper's text, are saved under `paper/`.
