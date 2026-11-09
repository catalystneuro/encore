fig6d-decode-p10 is now **not reproduced**. Round 3 is recorded, and the entry's checks pass.

**Outcome changed**
- fig6d-decode-p10 went from partially reproduced to not reproduced, because the verifier agreed with the proposal. Preparation 4, bout 1 fails under all four readings of width and count, with histories up to 100 ms, and with the code's windowing. That leaves 8 of 9 responses, and the criterion requires all nine. The `proposed` block is removed and no `blocked_by` was needed.

**Proposals still standing:** none. No other outcome changed.

**Numbers that didn't match the outputs**
The verifier found that the prose numbers for fig6d came from a different execution than the notebook it reviewed. My first re-run gave yet another set of numbers, so the decoding is not the same from one machine or environment to the next. On this machine two consecutive runs printed identical outputs apart from timings.
- **Which numbers changed:**
  - mean R of the failing response: own/le80 −0.120 here against −0.127 in the reviewed copy, pooled/min80 −0.080 against −0.060;
  - diverging windows over all histories: 462 to 627 here against 796 to 1107;
  - fig6s2's Wilcoxon p-values.
- **What stayed the same:** 8 of 9 passing under every reading, in every execution so far.
- **What I changed:**
  - **Notebook, fig6d conclusion (cell 82):** rewritten from this run's printed outputs. It now says the decoding varies between executions and gives the reviewed copy's values for the failing response.
  - **Notebook, fig6s2 conclusion (cell 85):** rests on the same decoding, so I updated it to this run's numbers (own/le80 MAE p = 0.91, 5 of 9 lower; own/min80 R-squared p = 0.13; pooled/le80 p = 0.65). Its outcome, reproduced, is unchanged.
  - **Rest of the notebook:** the summary table now shows not reproduced for fig6d, and the header has a "Revision after verification round 3" paragraph.
  - **README:** the fig6d row now says "Not reproduced (8 of 9)".
  - **Attempt record:** the fig6d and fig6s2 notes are updated to match. Round 3 is recorded under `verifications`, with the verifier's agreement, outcome and reason, and my response.

I did not commit or push.
