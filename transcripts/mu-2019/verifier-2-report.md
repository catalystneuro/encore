## 1. Outcomes

I took the counts from the claims file and the attempt record. There are 19 claims and the record gives 19 outcomes: 2 reproduced, 3 partially reproduced, 4 not reproduced and 10 blocked. I agree with all 19.

| Claim | Record | Agree | Note |
|---|---|---|---|
| fig1h-epoch-durations | partially_reproduced | yes | Cell 22: 2 of 3 values within tolerance under reading (a), and again 2 of 3 with edge epochs kept. |
| methods-isi | partially_reproduced | yes | Cell 25. |
| fig1j-open-loop-passivity | not_reproduced | yes, under the fixed criterion | Cell 28: p = 0.285. The variant that uses only closed loop before the first open loop gives p = 0.0137 and a median of 0.104, which meets the "partially" criterion. See section 3. |
| fig1c-vigor-open-loop-onset | reproduced | yes | Cell 31: p = 0.0195. It is fragile: the strict variant has 4 fish, p = 0.125. |
| fig1i-isi-before-passivity | not_reproduced | yes | Cell 34. The result depends on the minimum number of bouts per epoch. |
| fig2bc-neurons-lower-in-passivity | reproduced | yes | Cell 39. |
| fig2c-glia-rise-at-passivity | not_reproduced | yes | Cell 42: 2 of 4 fish in every variant. |
| figs2a-open-loop-higher | partially_reproduced | yes | Cell 45: the glial mean is higher in only 3 of 4 fish, so "reproduced" is out of reach whatever the SD measure. |
| fig2h-glia-weaker-closed-loop-pauses | not_reproduced | yes | Cell 48: 2 of 4 in every variant. |
| 10 blocked claims | as recorded | yes | For fig7-glia-accumulate I agree with the outcome but not the stated reason (section 3). |

## 2. Sentences the outputs do not support

- **Cell 43, and the fig2c notes in the record.** "In 20161109-2 the open loop alternates with stationary grating every 10 s, so its onsets mix the two."
  - Cell 11 shows that 3031 s of this fish's 3352 s of open loop is code 32. That code is prolonged open loop with velocities of 0.5 to 2, so the grating never stops.
  - The 10 s alternation applies only to the code 22/23 blocks. No output shows how many of the 26 onsets fall in those blocks.
- **Cell 43 and the record's "other" finding.** "consistent with a glial channel that carries little glial signal".
  - Cell 37 shows the neuronal trace of 20170203-1 also has a low SD: 0.00161, against 0.0069 to 0.018 in the other fish.
  - So in that file the low SD affects both channels, and the glial SD comparison does not single out the glial channel.
- **Cell 46, and the figs2a notes and response in the record.** "so drift between periods does not explain the larger open-loop fluctuations".
  - The per-period SD still compares periods of very different length. In 20170228-3 there are 10 closed-loop periods over 213 frames (about 12 s each) against 2 open-loop periods over 5477 frames. 20170228-4 has 22 against 3, and 20170127-1 has 65 against 2.
  - A long period holds slow fluctuations that a 12 s period cannot. Removing a linear trend does not remove them.
- **Cell 35, and the fig1i notes in the record.**
  - "the mean interval falls with distance from onset (Spearman rho = -0.536)": the means for k = 2 to 7 are 1.303, 1.357, 1.325, 1.327, 1.274 and 1.312, which is flat. Only k = 1 (1.506) is higher.
  - "Keeping the epochs that begin at a switch to open loop": the variant keeps epochs cut by either edge of a period (cell 20), not only those that begin at a switch.
- **Cell 50, Summary.** "a variant keeps them and changes no outcome": the edge variant was run for fig1h, fig1i, fig2c and fig2h only. It was not run for methods-isi, fig1j or fig2bc.
- **Cell 29.** "Passivity does not fall with the gain": of the 7 fish before the first open loop, 2 are tied at 0.000 (20170113-2 and 20170113-4), and one of the 2 "lower" fish differs by 0.006 (0.570 against 0.576). The sentence holds only loosely.
- **Record finding on raw images.** "Raw images are missing for part of 20170113-4 (3065 of 12050 volumes) and 20170228-4 (5776 of 7200)": the figures in brackets are the volumes that are present (cell 15). As written they read as the volumes missing.
- **Record notes for fig7-glia-accumulate.** "an analogue could be run in one fish only": cell 11 counts switches followed by 16 or more bouts as 7 in 20170203-1, 2 in 20170228-3 and 3 in 20170228-4. All 3 switches in 20170228-4 have 570 or more bouts. Three fish could support an analogue of Figure 7H.

Everything else in the conclusions, the Summary, the README and the record notes matches the printed outputs. That includes the fish, onset and dropped-onset counts, p-values, ranges, ROI fractions (8 to 15%), the code descriptions and the stationary share (26 to 54%).

The record states my round-1 reasons accurately and in my own words, and attributes the five changed block reasons correctly. One error in my own round-1 report: cell 31 shows 4 fish contributing a single switch, not 5.

I could not download the paper text this round. Cell.com returned 403 and the lab-site URL returned 404, so nothing is saved under `paper/`. I did not check the record's description of the Figure 7H protocol against the paper.

## 3. Round-1 points

**Resolved:**
- **Point 1, edge rule.** A variant now keeps the cut epochs, with a synthetic check and 0 to 8 dropped onsets per fish (cell 20). Outcomes are unchanged for fig1h, fig1i, fig2c and fig2h.
- **Point 5, switch window.** Fixed, with a synthetic check, and the numbers are unchanged.
- **Point 6, pause window.** A whole-window variant gives the same 2 of 4.
- **Point 7, passive epochs at period ends.** Covered by the edge variant: passive epochs average 20.87 s.
- **Point 8, weighting.** Declined, with a reason I accept.
- **Protocol codes.** Cells 11 and 12 describe every code. The block reasons for fig1k, fig1f, fig7-ne-mismatch and fig2dg now agree with mine.

**Remaining that bear on a conclusion:**
1. **fig1j.** Closed loop as defined pools the post-futility blocks: their passive fraction has a median of 0.825, against 0.183 before the first open loop. The selection closer to the paper's comparison (closed loop before the first open loop) meets the "partially" criterion: p = 0.0137, median 0.104. The record gives these numbers but does not say the variant would be partial, or that the main reading's closed-loop selection drives the "not reproduced".
2. **fig2c and fig2h.** Both outcomes depend on two fish (20161109-2 and 20170203-1) whose traces are questionable. The new outputs add one more inconsistency: in 20170203-1 the neurons rise after onset (cell 42, +0.28 SD, p = 0.0023), unlike the other three two-colour fish, and the file's neuronal SD is also low. The record already says the data cannot settle this, which is the right place to leave it. The sentence pointing to the glial channel should be weakened, and the 10 s alternation claim for 20161109-2 corrected or backed with an onset count by code.
3. **figs2a.** The SD measure is still confounded by period length (point 3 is only partly resolved). The outcome does not change, but the sentence saying drift does not explain the result should go, or rest on equal-length windows.
4. **fig7-glia-accumulate.** The "one fish only" reason conflicts with cell 11. The block on the Figure 7J/K part stands. The Figure 7H part could be tested in 20170203-1, 20170228-3 and 20170228-4, or the record should give a reason that follows from the outputs.
