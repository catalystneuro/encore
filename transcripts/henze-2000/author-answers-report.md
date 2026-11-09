There were no questions to apply, so nothing in the attempt changed and no outcome moved.

**Questions:** none. `questions/henze-2000.yaml` doesn't exist. The reader's answer run (`transcripts/henze-2000/answer-report.md`) found that no questions had been filed, and I asked none in my first run. My one open point, which cells and trains make up the Fig. 4B and C analysis, is a question for the paper's authors. It is recorded in the attempt as a `methods_unavailable` finding, not as a reader question. `claims/henze-2000.yaml` is unchanged, so I didn't re-run any claim or edit the notebook, the conclusions, `attempts/henze-2000-01.yaml`, or any claim's notes.

**Outcomes, unchanged from the first run:**

| Claim | Earlier outcome | Now |
|---|---|---|
| sample-cells | not reproduced | same |
| fig1c-start-end-timing | not reproduced | same |
| ap-duration-match | reproduced (6 of 16 readings) | same |
| duration-correlation | partially reproduced | same |
| neg-peak-precedes-intra-peak | reproduced | same |
| fig1c-derivative-mismatch | reproduced | same |
| notch-and-ahp-landmarks | not reproduced | same |
| fig2-interneuron-narrow | blocked, metadata_insufficient | same |
| fig3a-example-pair | blocked, metadata_insufficient | same |
| fig3b-latency-vs-amplitude | reproduced | same |
| fig3c-backprop-velocity | not reproduced | same |
| fig4bc-burst-attenuation | reproduced, assumed | same |
| fig4d-amplitude-correlation | reproduced | same |
| fig5, theta-higher-rates, fig6, tetrode-cell-count-estimate, silent-cells-inference, fig8 | blocked, data_missing | same |
| fig7-vertical-spread | not reproduced | same |
| propagation-velocity-range | blocked, data_missing | same |

**Checks and run:**
- `python tools/entry.py all entries/henze-2000` gave 0 errors, and the notebook passed in 624 s.
- `handover` wrote `executed/henze-2000/handover`.

**Lock problem:** the working tree has uncommitted changes to `tools/entry.py` and other tools that I didn't make. With them, `lock` adds hashes to the lock file and a `python: "3.13"` field to `entry.yaml`, and the entry schema rejects that field, so `all` failed with 1 error. I restored the committed `entry.yaml` and lock, which pin the same package versions, and ran the checks on those. The entry files are back to their committed state. To use the new lock format, the entry schema needs the `python` field added.

I didn't verify my own work, commit or push. The run finished at 19:22 UTC.
