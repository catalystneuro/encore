I made the round-2 corrections, re-ran the entry and recorded the round. None of the 38 outcomes changed and none are proposed for change, since the verifier agreed with all of them. The totals stay at 6 reproduced, 5 partially reproduced, 9 not reproduced and 18 blocked.

**Re-run.** `python tools/entry.py all entries/000011-li-2016` passed with 0 errors in about 19 minutes. The numbers the report quotes from cells 13, 75, 78, 93 and 96 come out the same, so no conclusion had to change because of new numbers.

**Corrected text.** These are the five sentences the verifier said the printed numbers do not support. I fixed them in the notebook and, where the same wording appeared, in the attempt record's notes.
- **Cell 14:** the event is logged up to about 1.6 s (1587 ms) after the light, not about 2 s.
- **Cell 76 and the fig3c-cd-predicts-movement notes:** the lick-left rho range is now -0.76 to -1.00.
- **Cell 79 and the fig3e notes:** "within 2 s.e.m. under every reading" now holds only for T1. I added that under the T2 variant (lick-early trials dropped, H1, g1) the ipsilateral difference of -0.353 is beyond its 2 s.e.m. of 0.294. The outcome is not reproduced either way.
- **Cell 94 (ed8):** bilateral separation is lower than ipsilateral only under K1 with H2 (0.616 against 0.672).
- **Cell 97 and the ed7 notes:** 750 ms is inside the tolerance of 210 to 770 ms. The ipsilateral time holds in 8 of 16 readings for the end-label combinations with lick-early trials dropped and D2 or D3, and those combinations fail on other parts.

**Added.**
- **Round 2 record:** it is under `verifications` in `attempts/000011-li-2016-01.yaml`, with all 38 claims marked `agrees: true`. Each has the verifier's reason taken from the report, including that it accepts ed7e and ed8 as partial and withdraws its round-1 point on E1, plus my `response`.
- **New question in `questions/000011.yaml`:** it asks a reader whether the claims file adopts the "at least half the parts" rule for partial outcomes. That rule covers five claims: unit-classification, fig2-recordings-recovery, ed7e, ed8 and fig6. The verifier asked for the claims file to settle it, and read strictly those five claims would be not reproduced.

**Not done, and why.**
- **K2 definition:** the question to a reader is still open, so the claims that depend on it stay as they are.
- **Population sizes:** the included populations are still 2 to 3 times the paper's. They stay recorded as selection_undocumented because no selection I tried gives the paper's counts.
- **cd-captures:** the captured fractions are in-sample, but there is no held-out test because the claims file names no held-out reading. The claim is blocked either way.
- **Data loading:** the verifier still cannot check how events and photostimulus records are assigned to trials without re-running the analysis, so it relies on the clock checks in cells 19 and 20. There is nothing for me to fix there.
- **Executed notebook:** a typo fix in cell 97 (D2 or D3) came after the run, so I applied it to the executed copy by hand as well. It touches markdown only, no outputs.
- **Commit:** nothing committed or pushed, as instructed.
