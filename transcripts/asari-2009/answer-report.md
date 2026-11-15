There was one question to answer, and I amended the claims file for it.

`questions/asari-2009.yaml` isn't on this branch, but `main` has it with one unanswered question. I copied it into the working tree and added the answer there. Nothing is committed.

**`fig2-example-long-context`: claim amended.** The Figure 2 legend and the Results do identify the example cell and probe:
- **What the paper prints:** the legend gives the probe's reliability ("0.74 ± 0.08") and the cell's reliability across all its natural sounds ("0.61 ± 0.07"). The Results give 0.61 "for the seven natural sound fragments tested in this cell".
- **Matching rule:** the criterion left these numbers out, so it accepted any cell with the right number of fragments and contexts. It now also asks for a cell with mean reliability 0.61 (within 0.061) and a probe with reliability 0.74 (within 0.074). The tolerance is the protocol's default of 10%.
- **The 4 s boundary:** the paper says the responses "diverged again after about 4 s". As `fig7-example-frequency-context` already does, I set the bound at 3.6 s (4 s less 10%). The claim is now reproduced when the matched probe has significant periods before 2 s, none between 2 and 3.6 s, and one after 3.6 s.
- **Source:** now also cites Figure 2A and the legend.

I didn't name a recording in the claim, since readers work from the paper alone. Because of the new boundary, the strict 4 s cutoff no longer decides this claim. `tools/claims_check.py` reports 21 claims, 19 quotes and 0 problems.
