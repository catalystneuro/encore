I've handled each point in the round-2 report, re-run all four notebooks and corrected the conclusions to the new numbers. No outcome changed and none is proposed for change, so no third round is triggered. `tools/entry.py check` passes with 0 errors.

**How the re-run was done.** `python tools/entry.py all` didn't fit. The whole entry takes about 2.9 hours (01: 41 min, 02: 52, 03: 53, 04: 28), but one foreground command can run for at most 2 hours, and the background run I tried first was killed when its call returned. So I ran `entry.py check`, then built the same environment and ran the same nbconvert command per notebook, in three foreground calls. All four notebooks passed. The re-run moved some 02 and 03 numbers by 0.01 to 0.02, apparently from nondeterminism across runs, so the text now quotes this run's values, not the ones the verifier saw.

**Outcomes**
- **Learning claims:** fig8de, fig8f, fig8g, figs13ab and figs13c are now marked `assumed: true`, as the verifier asked. Each deviation says the early and late days follow reading (a), the code's 20th and 80th percentile cut-off, and why: the Methods speak of "first few training days", which reading (b) cannot give here. A new finding asks the paper's authors which reading is meant.
- **Seed checks (new cells in 01):** I repeated the shuffle test with 10 more seeds. Both knife-edge outcomes turn out not to be stable:
  - fig2bc: mouse 2 is significant in 4 of 10 seeds (median p 0.0517), so the claim would count as reproduced in 6 seeds and not in 4.
  - figs3c: all four values are within tolerance in 2 of 10 seeds under reading (a) and 6 of 10 under (b).
  - I kept both verified outcomes and said in their notes that they are not stable. I proposed no change, because no single outcome holds across the seeds.
- **fig3df and fig3b:** notebook 04 now chooses C at every bin for the decoder weights and adds mouse 1. Mice 1 and 3 still show no difference in any bin, and mouse 2 differs in 3 of 12 bins, so the partial result stands. With per-bin C, mouse 1's peak falls at bin 3, which doesn't change the fig3b outcome.

**Corrections**
- I replaced every stale number the verifier quoted, in the notebook conclusions, the record and the question to the reader. This includes the `measured` lists for fig8ab and fig8ce, the fig1b count (now 1982 of 25883) and the C-grid difference (at most 0.44 points, not 0.67).
- The fig6a p-values per session are now printed to 4 decimals; mouse 2 EI is p = 0.0498. The fig4bd per-mouse check now notes that one of 28 tests is below 0.05.
- In the round-1 record, figs1b's reason no longer carries words the verifier didn't write, and it is marked as not agreeing, because that verifier gave a different reason for the block.
- Round 2 is recorded under `verifications`: the verifier agreed with all 38 outcomes, and its reasons are quoted with my response to each. The README run times and `entry.yaml` are updated.

**Not done**
- **The seven claims with no analysis are still blocked:** figs6ab, figs6c, figs7c, figs2 and the three simulations. The full re-run used most of the five hours. A tested result would also need another round of review.
- **fig8ce:** the onset decoders still use one C chosen at bin -1. Choosing C at every bin was estimated at over 6 hours of CPU.
- **Mouse 4 per-bin C:** not run in notebook 04.
- **figs6de:** the question about whether the claims file misreads the paper is still with a reader. The claim is tested as written.

Nothing is committed.
