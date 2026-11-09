I answered both questions and changed the claims file for each. I didn't commit or push.

1. **figs12-trials-per-session: changed.** The paper counts trials with a choice, not every go cue. The code that draws Figure S12a counts only trials where the mouse licked left or right, in the longest stretch without manual or extra water (`F_behavior_w_FP.ipynb` cell 19, `makeSessionDF`; `beh_mertics.py` calls this the "Total number of completed choice trials"). The criterion now defines a trial that way. Its first reading is now the session set that code uses: the 259 behaviour sessions that pass `beh_only.json`. The 106 sessions of the recorded neurons and all sessions stay as further readings. The all-go-cue count and the count without the cut are kept as variants.

2. **fig5h-switch-on-anatomy-axes: changed** (in the criterion of fig5d-ignore-on-anatomy-axes, which fig5h uses). The file had the two axes the wrong way round, and the code confirms it. In `F_spatial-axis-comparison.ipynb`, the retrograde (LDA) axis is b_z = [0.024, 0.332, 0.943] and the MERFISH (CCA) axis is b_y = [-0.248, 0.499, 0.830]. Since the legend reads "axonal projections and gene expression (left, r = 0.32; right, r = 0.30)", r = 0.32 goes with b_z and r = 0.30 with b_y. The criterion now names each vector with its data and its side of the legend.

**Wider problem for the claims file:** `paper/10.1038-s41586-026-11026-0.txt` now holds the full version of record. The claims file's opening comment says that text had only the abstract, so every expected value was taken from the preprint, and they don't all agree:

| Item | Preprint (used now) | Version of record |
|---|---|---|
| Trials per session, range | 94 to 558 | 94 to 800 |
| Fig. 5h, r (left, right) | 0.32, 0.30 | 0.37, 0.35 |
| Fig. 5d, r (left, right) | 0.23, 0.23 | 0.36, 0.36 |

Changing all the expected values is beyond these two answers, so I left them as they are and noted the differences in both answers. A new claims run against the version of record is needed to settle which values apply.

`python tools/claims_check.py` against the preprint text exits 0 and finds every quote. It flags two p-values it can't locate (fig5g-switch-dorsal and fig6a-outcome-space, both 0.0003), in claims I didn't touch; they need confirming by reading. Only `claims/001950/` and `questions/001950.yaml` are modified.
