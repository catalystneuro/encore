There were no questions to answer, so no claim changed and no outcome changed.

**Questions.** `questions/001037.yaml` does not exist. In the first run I asked a reader nothing ("Questions to a reader: none"). The answer run also found nothing to answer and left `claims/001037/` as it was. That file's last commit (b97353078) is older than the author run, so every claim reads as it did when I first tested it.

**Effect on claims.** Nothing to re-run. I did not edit the notebooks, the conclusions, the claims' notes or the attempt record `attempts/001037-vinograd-2024-01.yaml`, because no answer called for a change. The outcomes stay as the first run recorded them, 54 claims in all:

| Outcome | Count | Claims |
|---|---|---|
| Reproduced | 8 | methods-subspace-angle, fig2d, ed7f, ed8a, fig2k, ed8jl, ed3c, ed8c |
| Reproduced, resting on an assumption | 4 | fig1m, ed8b, ed3g, ed3h |
| Partially reproduced | 5 | ed9d, ed3f, ed4hi, fig1f, x1-time-constant-range |
| Not reproduced | 10 | ed1n, ed1p, fig1e, ed3e, ed4c, ed4d, ed4g, fig2gh, fig2no, ed8gi |
| Blocked, `methods_underspecified` | 2 | methods-cvr2, fig4ce |
| Blocked, `data_missing` | 25 | the rest |

**Entry run.** This checkout had no executed copies, and the handover is built from them, so I ran the full sequence:
- **lock:** `requirements.lock.txt` came out identical to the committed one.
- **all:** 0 check errors, and all four notebooks pass from a clean environment: stored_weights_and_stimulation 125 s, rslds_fits 829 s, cross_validation 2623 s, network_model 117 s. That is 62 minutes in total, against 51 last time.
- **Spot-check:** the key numbers the record cites (p = 0.016, p = 0.15, 0.48 to 0.52, 0.58 z, −0.01 z) still show in the fresh outputs. I did not compare every value.
- **handover:** written to `executed/001037-vinograd-2024/handover/`.

No tracked file changed. I did not verify my own work, and nothing is committed or pushed.
