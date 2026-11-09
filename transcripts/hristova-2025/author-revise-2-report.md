I made the round-2 fixes. No outcome changed and none is proposed to change. The verifier agreed with all 34 outcomes and found every round-1 point resolved. The tally stays at 13 reproduced, 9 partially reproduced, 2 not reproduced and 10 blocked. The final `python tools/entry.py all` and `check` both passed with 0 errors.

**Text corrected (notebook, record notes, README, claims-file comment):**
- **disc-het-swd-minutes:** the 110.57 min came from the epochs that SWD events overlap, not from the scorer's flags. Cell 32 now prints both counts: 110.57 min from overlapped epochs and 60.2 min from flagged epochs. Cell 33 and the record now say the paper's 59.97 min fits both, and the "not the flags" conclusion is gone.
- **fig4c-wake-power:** the range now ends at +0.168, which I confirmed as 0.1683 in the cell 77 output.
- **fig3d-rem-hourly:** cell 48 and the record no longer say the result "holds only with all 16 rats". They now say it also holds with GRIN2B-132 counted as Het (p = 0.038, interaction p = 0.071), and does not hold without GRIN2B-228 or without GRIN2B-238.
- **Summary (cell 97):** added that without GRIN2B-228, fig5def-no-other-correlations would meet its criterion. Also added that without GRIN2B-238 the fig3d genotype by hour interaction has p = 0.0001.
- **Recording length:** the README, the fig6b note and the claims-file comment now say each file is a 73 to 99 h recording with two 24-h baseline windows.
- **Run time:** the README now says about four minutes. The final run printed 246 s.

**Recorded:** a round-2 entry under `verifications` with all 34 claims. For each it gives agreement, the verifier's outcome, its reason drawn from the report, and my response. Where the report says nothing specific about a claim, the reason quotes "I agree with all 34 stated outcomes."

**Not done:**
- The verifier's two standing concerns are already disclosed and need no new analysis:
  - The archive does not say which rats the paper analysed.
  - The wake results depend on how SWD epochs are removed.
- The verifier had already saved the paper text under `paper/`, so I downloaded nothing.
- Nothing is committed, as instructed.
