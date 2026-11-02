No outcome changed and none is proposed. The counts are still 21 reproduced, 5 partially reproduced, 7 not reproduced and 19 blocked (`too_large`). I re-ran the entry with `python tools/entry.py all`: the notebook passes in 25 minutes, `check` reports 0 errors, and the test results match the previous run.

**Corrected text**
- **LSTM timing (fig4a and the 18 claims built on it):** epoch times change on every run. This run printed 9.9 h in one process and at best 2.5 h on 4 cores. The cell now prints whether the estimate is over the 60-minute limit, and the Result cell no longer quotes hours. The fig4a notes give this run's figures, and the 18 round-1 responses now say "about 10 h" and "about 2.5 h" and that the figures vary.
- **fig6e SVM timing:** the cell now prints on which side of the limit each part falls. This run: real labels alone 1.0 h, printed as within the limit; 1000 shuffles 41 days, over it. The text now says only the permutation test is too large in the CA1 half, and the claim stays blocked because the PFC half needs the LSTM.
- **"Four outcomes" is now "three"** in the Summary and the `methods_unavailable` finding. The text also says the round-1 grid changes one fig2g test but not its outcome.
- **Cell 111** now says p < 1e-8, with the largest value (9.25e-9).
- **Cell 10** now says only that the totals are consistent with the shortfall being the unlabelled units, and that how those 633 units divide between the regions is not known.

**Window averaging (new point):** no change needed, because the helper already does what the paper's code does. The code uses the 0.5 s bins only to pick which 0.2 s samples fall in the window, then takes a plain mean of those samples, so each sample has equal weight. The `window_mean` docstring now cites this. S7's wording invites the 3/2/3 reading, so I added a question for a reader in `questions/001371.yaml`; the claim is unchanged.

**Kenward-Roger (point 7):** R is not available here, so it was not run. As a stress test, every contrast now also prints its Tukey p on a deliberately small number of degrees of freedom (sessions minus levels). Three borderline results cross 0.05 on it:

| Claim | p now | p on small df |
|---|---|---|
| sfig3c-retrospective-unchanged | 0.036 | 0.050 |
| sfig12-delay-hpc-no-outcome-difference | 0.043 | 0.053 |
| sfig3ab new-arm front half | 0.044 | 0.063 |

The main tests of fig2g and sfig5e stay below 0.05. I put this in those claims' notes and in the Summary. I kept the outcomes and proposed no change, because the small value is not an estimate of what Kenward-Roger would give.

**Recorded:** round 2 is under `verifications`, with an entry for each of the 52 claims. The verifier's reasons are quoted or closely paraphrased, and the four fragile outcomes and the window and Kenward-Roger points are attached to the claims they bear on.

**Not done:**
- I kept the `too_large` label. The protocol names it for an estimate over the notebook limit, and the disagreement stays recorded.
- No subset of sessions was fitted with the LSTM.
- In the executed copy, cell 117 still says "(the cell prints which)", which reads awkwardly. Fixing it would mean another 25-minute run, so I left it.
- `tools/runner/chain.sh` was already modified before this run and I did not touch it. Nothing is committed.
