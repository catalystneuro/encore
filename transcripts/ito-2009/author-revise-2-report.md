No outcome changed in round 2. All 46 are as the verifier agreed: 23 reproduced, 7 partially reproduced, 8 not reproduced and 8 blocked. I re-ran the entry twice with `python tools/entry.py all`, and both runs pass (2386 s for the last one). The numbers are the same as before, and `entry.py check` reports 0 errors. Nothing needed a `proposed` change.

**Added or corrected, by verifier point:**
- **tone-discrimination-errors:**
  - The notes, cell 20 and the `result`-code finding now say the outcome rests on the tone-B rate, which is 0.97 to 1.11% under every count against 0.73 ± 0.073.
  - They also say the tone-A rate is not settled by these data (0.27 to 0.81% depending on the count), since filtering for tones of at least 1 s gives only an upper bound.
  - I fixed the wrong sentence "0.39% and 0.73% lie between these".
  - I added the output the verifier found missing: cell 19 now prints the time from tone offset to center exit. In the 96 short-tone trials the exit falls within 10 ms of the tone offset.
  - The summary and the cue-tone finding now say the tone "probably" stops when the rat leaves early, and that cue duration only marks exits before 1 s.
- **Partial rule:** fig5-variable-models-best and fig9-action-value-information-low now carry `assumed: true`, with a deviation stating how the partial rule was read. Cells 64 and 150 and the summary say the same.
- **Initial value Qi(1) = 0.5:** the notes of fig5-constant-models say the measured 0.5064 comes from this assumed value (0.5000 under Qi(1) = 0). The notes of table2-ml-parameters and cell 75 say the main reading has 7 of 16 matching values under Qi(1) = 0.
- **fig5-variable-models-best:** corrected to say DF-Q leads in 8 of the 12 readings with O1 (b) and O5 (b), those on splits (a) and (b); F-Q leads on split (c).
- **table2-ml-parameters:**
  - The "within 0.0005" statement now applies only to O5 (a); under O5 (b) F-Q is 0.0008 below and DF-Q 0.0002 below.
  - The round-1 response now says the 5000-particle sigmas differ from the 1000-particle ones in 5 of 6 cases.
- **Q-update finding:** it no longer says Table 2 is reproduced.
- **Sigma-search finding:**
  - It now gives the range over the whole grid: at most 0.0074, and at most 0.0035 for sigma_alpha up to 0.04.
  - It names the collapsed grid point and says F-Q's best sigma_alpha under O5 (b) is 0.08, the top of the grid.
  - It also fixes the old "under 0.003", which was wrong for DF-Q as well.
- **fig9-reward-information:** "6 to 7% of the peak" is now "5.6 to 6.7%" in cell 147, the notes and the round-1 response.
- **Round 2 record:** added under `verifications`, with all 46 claims marked as agreed, the verifier's reasons and my responses.

**Not done:**
- I did not widen the sigma grid past 0.08 for F-Q under O5 (b). The verifier found the outcome does not change either way.
- No new questions for a reader were needed. The two that bear on outcomes, fig9-reward-information and table3-parameter-averages, are already in `questions/001641.yaml`.
- Problem 8, slow drift affecting the MI threshold, is left as it is because the threshold follows the paper's method.
- Nothing is committed.
