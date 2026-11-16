There were no questions to answer. `questions/okuno-2025.yaml` does not exist, and the answer run reported the same thing: the first author run asked a reader nothing, so the claims file was not amended. No claim needed re-running because of an answer.

## What I ran
- **Lock:** `entry.py lock` left the lock file unchanged.
- **Run:** `entry.py all` passed. The check gave 0 errors; `reproduce_okuno_2025.ipynb` took 1202 s and `connectome_okuno_2025.ipynb` 7 s. A second `check` after my edits also gave 0 errors.
- **Handover:** `entry.py handover` wrote `executed/okuno-2025/handover/`, with the conclusions removed.

## What changed anyway: the re-run gave different numbers
The code was unchanged, but the numbers moved. The registration is not repeatable between runs: the helper seeds ANTs but does not limit ITK's threads. In some variants the shift is well past the "second or third decimal" the record allowed for. fly-100's registration changed the most: 20 ROIs are now partly outside the field of view, with AL(L) 12% inside, against 65% in the first run.

The verifier gets this run's executed copy, so I updated the numbers in the notebook's conclusion cells, the summary, the attempt record's notes, `measured` values and two findings to match it. Each claim's notes say no question was asked, the claims file is unchanged, and what the first run gave. Statements, criteria and outcomes are untouched. I did not change the code.

| Claim | Before (first run) | Now (re-run) | Outcome |
|---|---|---|---|
| fig3d-flyem-vs-flywire | FlyEM 0.616, FlyWire 0.575 | 0.603, 0.563 | partially reproduced, unchanged |
| fig3e-flyem-higher-most-regions | 55 of 63 (swapped 49) | 56 of 63 (swapped 43) | reproduced, unchanged |
| fig3g-transmitter-correlation | ACh 0.013, GABA -0.157 | -0.024, -0.108 | not reproduced, unchanged |
| fig4e-unsegregated-higher | swapped-orientation synapse SC above the null (p = 0.0021) | swapped synapse SC not different from the null (p = 0.22) | reproduced, unchanged (main setting holds) |
| fig4f-segregated-lower | neuron 0.574, synapse 0.524 | 0.563, 0.517 | reproduced (reading a), unchanged |
| fig4i-reciprocal-higher | swapped synapse SC below the null at p = 0.0195 | below the null at p = 0.0021 | reproduced, unchanged |
| fig5b-walking-activation | reading (b) failed for FB (rank 26 of 63) | reading (b) holds for all four with the graded regressor and hemibrain atlas | reproduced, unchanged |
| fig5b-walking-suppression | lowest t -0.82 | lowest t -0.66 | not reproduced, unchanged |

The claims tested on the paper's own tables did not change: fig3a, fig3c, figs3-1a, fig3f and fig4b. Neither did any blocked claim.

The swapped-orientation and no-nuisance variants of the permutation tests, and fig5b's reading (b), depend on the run. CI will re-execute the notebook and can shift the numbers again. Making the registration deterministic, for example by fixing ITK's thread count, would need a code change and another full run, which I left for a later attempt.

Nothing is committed or pushed. The modified files are `attempts/okuno-2025-01.yaml` and `entries/okuno-2025/reproduce_okuno_2025.ipynb`.
