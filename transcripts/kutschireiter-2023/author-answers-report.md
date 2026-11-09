There were no questions to apply, so nothing changed in the claims, the notebook, the conclusions or the attempt record.

**Questions:** none. `questions/000289.yaml` does not exist and never has in the repository's history. My earlier run asked no reader anything; its two open method questions went to the paper's authors as `methods_unavailable` findings. The claims file for 000289 has not changed since it was checked (commit `0e6f1c8d1`), so no claim was amended and none needed re-running.

**Outcomes:** all unchanged from the earlier run.

| Claim | Earlier outcome | Now |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | unchanged |
| fig2h-bump-tracks-circkf | reproduced | unchanged |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | unchanged |
| fig3b-bayesian-beats-conventional | reproduced | unchanged |
| fig3c-update-weights | reproduced | unchanged |
| fig3d-best-network-slow-decay | partially reproduced | unchanged |
| fig3f-noise-drop-below-70 | reproduced | unchanged |
| fig3f-retuning-reduces-drop | reproduced | unchanged |
| noise-effects-on-mu-and-kappa | partially reproduced | unchanged |
| fig4b-connectome-motifs | reproduced, resting on an assumption | unchanged |
| fig4gh-drosophila-network-matches | partially reproduced | unchanged |
| figs2-performance-independent-of-n | partially reproduced | unchanged |
| prediction-bump-amplitude-cue-reliability | blocked (`methods_underspecified`) | unchanged |

**Entry runs:**
- **Lock:** `python tools/entry.py lock` rewrote the lock file with the same contents.
- **Checks and run:** `python tools/entry.py all` gave 0 errors, and the notebook passed in 376 s.
- **Handover:** `python tools/entry.py handover` wrote the package to `executed/000289-kutschireiter-2023/handover`.

The working tree has no tracked changes. Nothing was committed or pushed, and I did not verify my own work.
