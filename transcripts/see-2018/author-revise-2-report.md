I answered every point in the round-2 report. The entry now passes `tools/entry.py check` and a full re-run (47 min). Nothing is committed.

**Outcomes.** No outcome changed, since round 2 doesn't allow it. For fig10c I kept the verified `reproduced` and added `proposed: not_reproduced` to its record entry, with the reason. The re-run gives exactly the verifier's numbers:
- No reading meets p < 0.001 in the main draw: p = 0.0015, 0.0076, 0.049 and 0.19.
- The linear projection with every bin above threshold passes in only 2 of 5 subsampling draws.
- I had chosen the linear projection because it was the reading that passed. The paper says it follows Lopes-dos-Santos et al. 2013, whose projection is the quadratic one, and under that no reading passes in any draw.

The analysis is in the fig10c cell, which now also counts the main draw in the pass tally. A third round will review the proposal.

**Why the numbers changed between executions.** The verifier found that results changed from run to run even with fixed seeds. The cause was the float32 ICA: on a different CPU, the maths library's routines return weights and activity thresholds that differ by about 1e-7. That is enough to move an event across its threshold, which changes every random subsample drawn after it. I confirmed this by running the detection under two library settings outside the notebook.

In `cne.py`, arrays are now float64 and activity is rounded before it is compared with a threshold. Under both settings, three recordings' detection and STRF results and one recording's bin-size analysis then agree to 1e-15. Two full executions of the notebook gave identical numbers. To stay within the time limit, the ICA of the 100 shuffles and of the model runs stays float32; it only feeds averaged thresholds and mean sizes.

**Text corrected to the new run**
- **fig10b:** p-values replaced with the printed ones (8.0e-12, 3.8e-09, 5.6e-04, 2.4e-05).
- **fig10c:** conclusion cell, summary row, README row and the related finding rewritten.
- **fig5a:**
  - 0.075 against 0.072 to 0.073, and 2857 or 3358 distinct bins.
  - The notebook now prints the held-out MI as a fraction of the in-sample mean (0.086 to 0.209 under event reading a, 0.024 to 0.292 under b), and the text uses those ranges.
- **fig6c:** p is 4.1e-76. The notes now say that both sharpness measures are off the paper's scale.
- **fig11c:** the note no longer says the DG sample reproduces the covariances. Its covariance slopes run from 0.672 to 1.02, and at sites 1 and 16 it falls short by about a third.
- **Small shifts from the float64 change:** fig7b reading (b), fig5c, fig11c, fig11d, fig11ef and fig11s3b.

**Recorded.** The round-2 block covers all 31 claims, with the verifier's reasons and my responses. Agreed claims with no note in the report are marked as such.

**Not done.**
- No new reader questions: the report raised no new misreading, and the fig6j question was already filed.
- I did not delete or commit the files I didn't make: the edits to `tools/entry.py` and `tools/notify.py` and the untracked dotfiles at the repo root.
