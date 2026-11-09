# Round 3 verification: 000579-tseng-2022-01 (Tseng et al. 2022, DANDI:000579)

The claims file has 43 claims and the attempt record has 43 outcomes: 9 reproduced, 5 partially reproduced, 1 not reproduced and 28 blocked. Only one outcome has a `proposed` change: **fig3q-cue-decoding**, from partially_reproduced to reproduced. The fig8cd result in the second notebook is recorded as a check of an assumption, not a proposed change, so I did not review it. Cell numbers are positions in the re-executed notebooks.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig3q-cue-decoding | reproduced | yes | — | See below. |

## Reason for fig3q-cue-decoding

**The criterion, as written:** under every reading (12 here), the area means of the decoders rank V1 highest and A lowest, and V1 is above A at two-tailed p < 0.05.

**The numbers come from the data.**
- **Second notebook, cell 5:** every pool session with a V1 or PM field was fitted: 41 sessions, 23,375 neurons, 0 failures. That gives 149 V1 and 71 PM decoders with k-means groups, and 142 and 80 with tiles. It uses the same pool (reading b, 142 sessions), the same helper, the same three grouping and fold settings, and the same stem bins (0–8) as the main notebook.
- **Second notebook, cell 6:**
  - V1 minus PM is 0.027 to 0.062, positive in 12 of 12 readings.
  - V1 ranges from −0.139 to −0.246 and PM from −0.187 to −0.282.
  - The difference is significant only for tiles over stem bins (p = 0.039 and 0.042); elsewhere p = 0.098 to 0.474.
  - These match the proposed reason exactly.
- **Main notebook, cell 58:** AM is the highest of the other four areas, at −0.276 to −0.382. I paired each reading's AM value with the V1 value for the same reading in second-notebook cell 6. The margins range from 0.118 to 0.157, as the reason states.
- **A against V1:** A is the lowest area in all 12 readings, with V1 minus A of 0.355 to 0.409 and p < 0.001 (main notebook, cell 58). The full-field V1 means are higher than the subsample's V1 means, so this result holds.

**The criterion is met as written.** V1 is now the highest area mean under every reading, and A is the lowest, below V1 at p < 0.001. The criterion ranks the area means without requiring V1 to be significantly above PM. The record says plainly that V1 against PM is not significant in 10 of 12 readings.

**The analysis choice was not made to reach the result.** Fitting every V1 and PM field session is the check I asked for in round 2 to settle the one open comparison. The scope (V1 and PM fields only) rests on the time limit; it was not chosen after seeing results. V1 is also above PM:
- in each of the 6 mice that have both areas, though mouse 3 is close (−0.166 against −0.178);
- within each field (cell 6).

## Caveats

None of these changes my outcome.

1. **The ranking mixes two decoder sets.** V1 and PM come from all V1- and PM-field sessions. AM, MM, RSC and A come from the 18-session subsample, with AM from 16–17 decoders in 3 mice. The bootstrap spread of AM is not printed. The 0.118 margin is large next to the subsample-to-full shift seen for V1 and PM (about 0.02–0.03), but the ranking of the other areas still rests on the subsample.
2. **Off-field PM decoders are missing.** Decoders labelled PM (by centroid) in sessions of other fields were not fitted. The cell 7 text states this. There are 71–80 PM decoders here against the paper's 106, while V1 is nearly complete (142–149 against 151).
   - The criterion assigns area by centroid, so roughly a quarter to a third of PM's decoders are absent.
   - In the subsample, off-field PM decoders do not average higher: mice 5, 7 and 8 give −0.036 (1 decoder), −0.332 (2) and −0.192 (2) (main notebook, cell 58).
   - So a flip is unlikely, but it has not been ruled out.
3. **Some checks rest on one reading.** The per-mouse and per-field comparisons are printed only for k-means groups, frame folds, minimum penalty and stem bins (cell 6). The reason states them without saying this.
4. **The record's timings again do not match the printed output.**
   - The record says "658 s on 4 processes" for the 41 sessions; cell 5 prints 930 s.
   - The record says "346 s … 77 CPU-s per session … 3.2 CPU hours, 48 minutes"; main notebook cell 56 prints 490 s, 109 CPU-s, 4.5 CPU-h and 68 min.
   - The README says the second notebook takes about 13 min; cell 12 prints 18.2 min.
   - None of this changes a conclusion, since every figure is over the 30-minute limit.

I found no place where the claims file misreads the paper for this claim.
