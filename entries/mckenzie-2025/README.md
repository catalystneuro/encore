# McKenzie et al. (2025) from dandiset 000552

Tests the electrophysiology findings of [McKenzie et al. (2025)](https://doi.org/10.7554/elife.105183)
on [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.230630.2304), the Huszar et al. (2022)
recordings the paper reanalyses, at the version the paper cites (0.230630.2304). The fiber photometry of
norepinephrine (Figures 1 to 6) is not in the dandiset.

| Claim | Outcome |
|---|---|
| Ensemble of 253.8 neurons per session (191 to 363) | Reproduced (all units, not pyramidal cells only) |
| Faster decorrelation in the first minute in a novel environment (Figure S6B) | Not reproduced |
| No such change in the familiar environment (Figure S6D) | Reproduced |
| UMAP embedding maps position, early moments at its periphery (Figure 7A, B) | Partially reproduced |
| First-minute vectors less similar to same-place neighbours than at minute 10, novel (Figure 7E) | Reproduced |
| The same in the familiar environment (Figure 7F) | Reproduced |
| First minute more similar in the familiar than the novel environment (Figure 7G) | Reproduced |
| In-field firing rises and out-of-field firing falls (Figure S7A, B) | Partially reproduced |
| Movement differences of neighbours not related to time (Figure S7C, D) | Partially reproduced (familiar only) |
| Only time explains nearest-neighbour similarity (Figure S7E, F) | Not reproduced |
| The same without conditioning on location (Figure S7G, H) | Reproduced |
| Late moments more reactivated in post ripples (Figure 8B) | Not reproduced |
| No early against late difference in the familiar environment (Figure 8D) | Not reproduced |
| No reactivation in pre ripples (Figure 8A) | Not reproduced (above chance in the familiar run; in the novel run only through minute 1) |
| Photometry findings (13) and the NE and settling time-course comparison | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

The pinned version has no cell types; they are read from the later version 0.261113.1035, whose spike
times are the same. In session e16-3m2-211211 the linear-track tracking is filed in the open-field epoch,
in both versions. Time 0 is the start of the maze epoch, as the claims file reads "transfer"; tracking
starts 15 to 63 s later, and counted from the first tracked frame the late moments of the novel run are
reactivated more (Figure 8B), a variant shown and not judged. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/mckenzie-2025-01.yaml`](../../attempts/mckenzie-2025-01.yaml).

- `settling.ipynb`: the data check, the ensemble size, decorrelation, the UMAP embedding, nearest-neighbour
  settling, place field deviations and the movement controls. About 23 minutes.
- `reactivation.ipynb` and `reactivation_familiar.ipynb`: ripples detected on the LFP of the raw files (for
  e13-26m1-211119, which has no raw file in the pinned version, the LFP in the later version's file of the
  session), and reactivation of the moments of the novel and the familiar run in them. About 57 and 34
  minutes, most of it the 1000 shuffles per ripple set.
- `settle.py`: loading, population vectors, nearest neighbours, the speed filters, place fields, the
  model of Figure S7E, F, ripple detection and the reactivation test, with where each parameter comes from.
