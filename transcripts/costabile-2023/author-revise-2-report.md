No outcome changed. The record still has 2 claims reproduced and 33 blocked, all as the round-2 verifier agreed, so nothing is under `proposed`. The entry was re-run with `python tools/entry.py all entries/costabile-2023`: both notebooks pass (main notebook 49 min, subsample 15 min) and the checks report 0 errors.

**Why the figures were stale.** The CNN fit times change from run to run by tens of percent: this run took 2.14 s per fit on one thread, where the run the verifier reviewed took 1.37 s. The conclusions in both notebooks and the README had copied the numbers from an earlier run. They now point to the printed figures, and cell 34 prints how many five-hour runs the fits would take (12.8, or 25.7 with the rotated controls). The record's notes give this run's numbers:
- **On one thread:** 2.14 s per fit, 257 h.
- **In four processes:** 4.37 s per fit, 1.17 s of wall time per fit, 141 h, and 283 h with the controls.
- **Backfill fish (fig6f):** 71 h.
- **Simulation and mouse claims:** 0.2 h (1.0 h for five seeds) for fig1f, 1.8 h and 9.2 h for fig2e, 0.2 h for fig3, 2.4 h for the mouse claims.

**Other corrections:**
- **data-zebrafish-coverage:** marked `assumed: true`. The deviation now says why the raw movie was used and how little the count depends on it.
- **figs6-mine-more-at-every-cutoff:** the "as the claim states" sentence is gone. The notebook and notes now say the subsample's point estimate fails the criterion at cutoff 0 (362,580 against 371,878), the interval of the difference there (−22,008 to 4,230) includes zero, and the 7 fits with no test correlation probably explain part of the gap.
- **Swim starts (cell 16):** "not before it" is replaced by the printed values. The correlation is 0.086 at −5 s and 0.108 at −1 s, and peaks 1.8 s after the bout.
- **Finding 5, the 128 s tail-timestamp jump:** cell 21 now shows which side is misplaced. Moving that side by the jump gives starts of −5.35 to −5.55 s and ends of 495.79 to 495.82 s, the range of the other planes. The statement is corrected, and the severity goes from `major` to `minor`, the verifier's rating, because the problem shows in the values and is easy to work around.
- **Linear-model count:** it moved from 26,326 to 26,328 between runs. The notes give both, and the notebook and README say "about 26,300".
- **README:** "well over 100 hours" is replaced by wording tied to the printed estimate.
- **Round 2 under `verifications`:** recorded for all 35 claims, each with the verifier's reason and my response.

**Not done:**
- **Round-2 `findings` list:** left out. No finding is rated `critical`, and the schema's list is only for critical ones. The severity change on finding 5 is recorded in the finding itself.
- **Questions file:** nothing added, because the verifier reported no place where the claims file misreads the paper.
- **`runtime_minutes` in entry.yaml:** still says 58 for the main notebook, which took 49 this time. Editing it would change the entry's hash and force another 65-minute run.
- **`tools/runner/chain.sh`:** it was already modified before this run, and I did not touch it.

Nothing is committed.
