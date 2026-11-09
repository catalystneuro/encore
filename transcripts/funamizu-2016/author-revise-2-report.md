No outcome changed and none is proposed. The counts are still 11 reproduced, 2 partially reproduced, 9 not reproduced and 18 blocked. I re-ran the entry twice after the code changes. Both runs passed (the last took 1,418 s), and `tools/entry.py check` reports 0 errors. Nothing is committed.

**svm-correlations: still blocked as too large, with a better estimate.** The verifier was right that the old estimate didn't show the block.
- The old estimate ignored the 4 worker processes.
- It had no estimate for reading (b).
- It was timed on a session with only 13 goal-distance neurons, so it understated the cost.

The notebook now times both readings on the session with the median neuron count (37 neurons). It divides by the 4 workers, counts the 4 classification readings that the decoder claims also use, and compares the total with the time the notebook has left. The result is about 173 min for the whole claim, or 43 min for one classification reading alone. The notebook had already used 23 min of its 60, so even one classification reading doesn't fit.

**fig3b: still blocked as too large.** It now also prints the estimate over 4 workers: 29.7 h.

**Text corrected to match the printed numbers:**
- **Timings:** cells 0 and 119, the record's fig3b and svm notes, and the timings quoted in the round-1 responses.
- **Cell 109:** it now says the fitted widths are refined by a bounded optimizer.
- **Cell 116 and the tuning-similar-ppc-pm note:** they now also say that b1 differs in layer 2 under O1 b (P = 0.014), which the earlier wording left out.
- **fig1d note:** it now says the paper's data page was checked outside the notebook and supplies no number.

**Outputs added:** the data check now reads `speaker_on_matrix` in all 94 files. Any of its 12 speakers is on in exactly 150 frames per file, all at a trial's first frame. The sentence the verifier quoted about it is now backed by a printed number.

**Questions:** I added the verifier's supp9 point to `questions/001605.yaml`. The group sizes fit equal quarters much better (summed share difference 0.63 against 3.09). The outcome doesn't depend on it, because the claim fails under equal quarters. The supp1 and fig4-above-chance questions were already there.

**Round 2 record:** written for all 40 claims, with the verifier's reasons and my responses. It records agreement on 38 and disagreement on fig3b and svm-correlations.

**Not done:**
- **fig4d "8 to 11":** I kept it. This run prints 8 to 11 of 16 bins: 8 under O1 a with shift 0.1, which the verifier's "9 to 11" misses.
- **Decoder range past the goal (fig5a-map-decreases-without-sound, fig5-layer3-steeper-than-layer2):** I didn't try one. The 67 to 0 cm range is the claims file's, taken from the Fig. 4b legend, and a wider range would need training frames past the goal, which the paper doesn't describe. It is a new analysis, so it waits for a new attempt. The notes now say the failure may depend on that range.
