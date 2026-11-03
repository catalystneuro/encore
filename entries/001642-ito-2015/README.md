# Ito & Doya (2015) from dandiset 001642

Tests the findings of [Ito and Doya (2015)](https://doi.org/10.1523/jneurosci.1962-14.2015) on
[DANDI:001642](https://dandiarchive.org/dandiset/001642/0.260205.0153), which holds the behaviour
and the spike times of DLS, DMS and VS units of seven rats in a fixed- and free-choice task.

| Claim | Outcome |
|---|---|
| Trial counts; trials per block | Reproduced |
| Extinction tests differ between fixed tones and the choice tone; their time course | Reproduced |
| Decision trees: choice tone sensitive to experience, fixed tones biased | Reproduced |
| FQ learning with time-varying parameters predicts choices best | Not reproduced |
| Actor-critic near chance (0.508) | Reproduced |
| Counts of stable neurons and PANs | Not reproduced |
| VS activated in Phase 1, DMS in Phase 5, VS above DLS in Phase 7 | Reproduced (two on assumptions) |
| VS longest activation, DLS shortest | Partially reproduced |
| State information strongest in VS in Phase 1 | Partially reproduced |
| Action information rises in Phase 3 only in DLS | Not reproduced |
| Action information before cue offset higher in DLS | Reproduced (on an assumption) |
| Action information before centre exit and in Phase 5 highest in DMS | Reproduced |
| Reward information strongest in VS, then DMS | Blocked: methods underspecified |
| Event-coding proportions follow the MI; similar in fixed and free blocks | Partially reproduced |
| Event-coding proportions above chance | Reproduced |
| Action, reward and previous-trial coding in the regression | Partially reproduced |
| Action-value coding highest in DMS in Phase 5 | Reproduced (on assumptions) |
| QR coding in DMS above DLS | Not reproduced |
| State-value coding highest in VS | Partially reproduced |
| No policy coding | Reproduced |
| Action information rises DLS, then DMS, then VS in every block type | Not reproduced |
| DMS action command never above DLS | Reproduced (on an assumption) |
| DLS and DMS action information stronger in fixed than free blocks | Not reproduced |
| VS: no fixed against free difference | Blocked: methods underspecified |
| DLS action information stronger in stay than switch trials | Reproduced (on an assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's display equations are missing from its text and it links no code, so many method
details are open; where their readings disagree, the choice the paper best supports is adopted
and every reading is shown. The trial table's cue codes are described wrongly (2 is the left
tone, 3 the right, 1 the choice tone), and the units include more than the paper's stable
neurons, with a PANs flag that does not follow the Methods' rule alone. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001642-ito-2015-01.yaml`](../../attempts/001642-ito-2015-01.yaml).

- `reproduce_ito_2015.ipynb`: the analysis. It takes about 23 minutes, most of it the shuffles
  of the mutual information and the particle filters.
- `striatum.py`: loading the files, event-aligned spike counts and the mutual information.
- `models.py`: the choice models and the regression with BIC selection.
