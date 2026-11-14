## Report

**Questions:** none. `questions/nishimoto-2011-reconstructing.yaml` does not exist, and no branch has ever had it. My earlier author run asked no reader any questions. The two open method details it raised went to the paper's authors as `methods_unavailable` findings, which a reader does not settle:
- how the L1 penalty was chosen;
- whether accuracy and identification used the mean of the ten test repeats or single repeats.

The reader's answer run found the same and left the claims file as it was.

**What changed:** nothing. No claim was amended, so I re-ran no claim and did not edit the notebook, the conclusions or the attempt record. Every outcome stands as before:

| Claim | Outcome (earlier = now) |
|---|---|
| fig2de-prediction-accuracy | reproduced (0.217, 0.375, 0.379) |
| fig2e-directional-gain-small | reproduced (ratio 0.026, bound 0.1) |
| figs1a-motion-better-every-area | reproduced |
| fig3ab-identification-s1 | reproduced (424 of 486; tolerance needs at least 418) |
| fig2fgh-retinotopic-receptive-fields | blocked, too_large |
| fig2j-speed-eccentricity | blocked, too_large (depends on fig2fgh) |
| discussion-color-no-gain | blocked, too_large |
| fig3c-identification-large-set | blocked, data_missing |
| fig4-reconstructions | blocked, data_missing |
| fig4d-reconstruction-accuracy | blocked, data_missing |

**Entry:**
- `lock` rewrote the lock file, and git shows no change to it.
- `all` passed its checks with 0 errors. It did not run the notebook again: it reused the executed copy from 13:38 UTC (1,547 s) because nothing the notebook reads has changed since.
- `handover` wrote `executed/nishimoto-2011-reconstructing/handover`.

Nothing was committed or pushed. This run's job was the answers, and there were none, so I did not use the remaining time on the three claims blocked as `too_large`.
