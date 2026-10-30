No outcome changed in this round. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passes), and every number the new text cites matches the new outputs. Nothing is committed.

**Outcomes**
- **fig6-sample-sizes:** now marked `assumed: true`, as the verifier asked. The median is in tolerance (19) only when one or both members of a near-duplicate pair are removed. Under the deposit and none readings it is 21. The outcome would still be partially reproduced under every reading, because the tails are missing; the notes and the conclusion now say so.
- **fig4bd-gaba-network and fig4e-extrasynaptic:** the notes now give the block as the verifier described it: the paper does not name the transmitter map or the connectome behind Figure 4. The sentence that made it sound like a choice is gone. Both stay `blocked_by: other`. I put `methods_underspecified` under `proposed`, because it fits this block more exactly, so a third round will review that change. The reasoning is in notebook cell 77 and the summary.

**Question for a reader**
- Added to `questions/000541.yaml` for fig6-nacl-unknown-interneurons. The claims file's criterion uses the mean dF/F0 and leaves out the paper's sentence "we used dNMF to normalize activity traces per neuron class". The claim itself is unchanged. The notes now say that the criterion as written gives 4 of 6.

**Text corrections**
- **Summary, normalisation bullet:** now names the two outcomes that change with normalisation (fig6-nacl-unknown-interneurons and fig6-asj-ric). fig6gi is no longer listed there, since Pearson correlations do not change.
- **Summary, selection bullet:** now lists the three results that change with the selection reading: fig6-asj-ric, fig6gi and the fig6-sample-sizes median. It also says that "one" matches Table S6 only on per-class counts. Agreement on p is about the same under all four readings (260, 261, 259 and 257 classes).
- **Missing deposit traces:** the summary and the `selection_undocumented` finding now say 126 named traces are missing from the deposit, 113 of them finite. 101 of these have an empty slot there.
- **Low pi0:** the summary and the fig6-asj-ric notes now give Storey's pi0 here (0.222) against 0.42 to 0.48 on the paper's own p values. That is what lets the ASJ response to 2,3-pentanedione pass under reading (a) (q = 0.040, p = 0.082); it does not change the outcome.
- **Smaller fixes:**
  - The fig6gi null window is now described as falling 20 to 50 s after each pulse ends, so it cannot rule out lingering stimulus effects.
  - The PCA description now says z-scored traces are the main run.
  - The stimulus set sizes are corrected to 16 to 55.
  - The README's "closest to Table S6" sentence is corrected.

Round 2 is recorded under `verifications`, with the verifier's reasons and my response for all 29 claims.

**Not done:** whether the median of 18 covers heads and tails together is still with a reader, as before.
