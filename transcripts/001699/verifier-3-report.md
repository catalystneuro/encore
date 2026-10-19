# Round 3 verification: Moore et al. (2025) on DANDI:001699 0.260917.2322

The claims file has 27 claims and the attempt record has 27 outcomes. Only one outcome has a `proposed` entry: fig1g-juvenile-halves-correlation, which the author proposes to change from partially reproduced to not reproduced. I agree with the change.

| claim | proposed outcome | agree | my outcome if different | reason |
|---|---|---|---|---|
| fig1g-juvenile-halves-correlation | not_reproduced | yes | — | See below. |

**The numbers come from the data.**
- Cell 83 re-runs the analysis using the session definition from the claims file. Session 1 contains the same cells as before: 323 WT and 237 Fmr1-/y.
- The Pearson r of HD information between the first and second halves of session 1 is 0.7610 for WT (lower bound 0.81) and 0.8385 for Fmr1-/y (lower bound 0.855). Neither is within tolerance.
- These match my round-1 values of 0.761 and 0.840, which were computed under the same definition before the later fixes. The fix to spike counting and the full Isomap fit therefore do not affect this result.

**The session definition is implemented as written.** `hdfx.exploration_sessions(rule="claims")` at `hdfx.py:239` cuts a block to its first 1300 s only when the block is longer than 1800 s, and keeps other blocks whole. This is the claims file's definition. The session lengths printed in cell 83 agree: H3001 200201 is kept at 1662.8 s, and blocks over 30 min come out at 1300 s.

**The choice was not made to reach the result.** The proposal returns to the definition the claims file fixed before the analysis. It also moves the outcome against the author's interest. The 0.815 that put WT inside tolerance (cell 43) came only from the 20 min cut, which was adopted after round 1 and is not what the claims file says. That cut was the point I raised in round 2.

**The criterion and outcome rule are applied consistently.**
- The claims file's criterion for fig1g is the Pearson r over the cells of session 1, defined as the claims file defines the sessions.
- The claims file gives no outcome rule for correlation claims. The attempt treats a claim as not reproduced when neither value is within tolerance. Round 2 accepted that rule, and it is the rule behind fig3g and figs2j.

**Variants under the claims file's definition (cell 83) do not change the outcome.** With H3026 left out, the Fmr1-/y r is 0.869, which is within tolerance, but WT stays at 0.761. With the first day of each rat alone, WT falls to 0.650.

**Other claims under the claims file's definition (cell 84, checked against the table in cell 83).** No other claim crosses its criterion, so no other claim needed a proposal.
- figs1c active speed comes to p = 0.0504, just above 0.05, so it still counts as no difference.
- fig1ef HD information p = 0.031, fig1h p = 0.014, fig1j p = 0.069, fig2d p = 0.079, fig2h p = 0.045, fig3h p = 0.042 and fig3j p = 0.023 each stay on the same side of their criterion.
- The other correlation claims keep the same values within and outside tolerance.

I did not need the paper text this round, so nothing was added under `paper/`.
