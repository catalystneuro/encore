There were no questions, so no claim, notebook or record changed. `questions/000678.yaml` does not exist on this branch, and the claims file (`claims/000678/`) has not changed since the first author run. That run asked no reader questions. Its one open question, about how `Figure2.py` types a state with no confident trials and which 381 sessions were analysed, is for the paper's authors. It is recorded as a `methods_unavailable` finding in the attempt record. The answer run before this one also found nothing to answer and changed nothing.

I didn't edit the notebook, `hulsey.py`, the README or `attempts/000678-hulsey-2024-01.yaml`, because nothing was answered to update them for.

What I ran:
- **Lock:** `python tools/entry.py lock entries/000678-hulsey-2024` rewrote the lock file with no change.
- **Check and run:** `python tools/entry.py all entries/000678-hulsey-2024` gave 0 errors, and the notebook passed in 581 s (about 10 minutes).
- **Handover:** `python tools/entry.py handover entries/000678-hulsey-2024` wrote `executed/000678-hulsey-2024/handover/`.

The working tree under `entries/`, `attempts/`, `claims/` and `questions/` is clean. Nothing is committed or pushed, and I did not verify my own work.

**Per question:** none, so no claim was affected. In the executed notebook, every claim's result line matches the first run. Each claim's earlier and current outcome:

| Claim | Earlier | Now |
|---|---|---|
| cohort-inclusion | partially reproduced (376 sessions, not 381) | same |
| training-duration | blocked, `data_missing` | same |
| distractor-response-rate | reproduced | same |
| figs2-n-states | reproduced | same |
| fig1g-example-mouse-prediction | reproduced | same |
| fig2a-state-types | reproduced, resting on an assumption | same |
| fig2b-optimal-occupancy | partially reproduced | same |
| fig2c-dwell-times | partially reproduced | same |
| fig2d-prediction-accuracy | reproduced | same |
| fig3c-inverted-u-pupil | reproduced | same |
| fig3d-optimal-pupil-modality | reproduced | same |
| fig3e-u-disengaged-pupil | reproduced | same |
| figs4-r2-individual-movement | partially reproduced | same |
| fig3f-movement-index-inverted-u | partially reproduced | same |
| fig3f-movement-index-u-disengaged | reproduced | same |
| figs5-movement-index-correlations | reproduced | same |
| fig3-distance-from-optimal-pupil | partially reproduced | same |
| fig3-raw-face-energy-trend | reproduced | same |
| fig3-raw-locomotion-no-difference | reproduced | same |
| fig4a-lower-variability | partially reproduced | same |
| fig4b-variability-at-transitions | partially reproduced | same |
| fig4d-pupil-movement-decoupling | reproduced | same |
| figs6-individual-measure-decoupling | reproduced | same |
| fig5c-state-classification | reproduced | same |
| figs7-pupil-best-raw-measure | reproduced | same |
| fig5c-movement-index-best | not reproduced | same |
| figs8a-regression-weights | reproduced | same |
| figs8b-pupil-movement-interaction | reproduced | same |
| figs1-iti-independence | reproduced | same |

If reader questions were meant to be part of this round, they were never committed. Once `questions/000678.yaml` exists and a reader has answered it, the answer run and then this run need to be done again.
