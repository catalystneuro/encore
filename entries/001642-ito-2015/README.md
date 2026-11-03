# Ito & Doya (2015) from dandiset 001642

Tests the findings of [Ito and Doya (2015)](https://doi.org/10.1523/jneurosci.1962-14.2015) on
[DANDI:001642](https://dandiarchive.org/dandiset/001642/0.260205.0153), which holds the behaviour
and the spike times of DLS, DMS and VS units of seven rats in a fixed- and free-choice task.

| Claim | Outcome |
|---|---|
| Trial counts; trials per block | Reproduced |
| Extinction tests differ between fixed tones and the choice tone; their time course | Reproduced |
| Decision trees: choice tone sensitive to experience, fixed tones biased | Reproduced |
| FQ learning with time-varying parameters predicts choices best | Not reproduced (on assumed model forms) |
| Actor-critic near chance (0.508) | Reproduced |
| Counts of stable neurons and PANs | Blocked: data missing |
| More than 60% of VS PANs activated in Phase 1 | Blocked: data missing |
| DMS activated in Phase 5; VS above DLS in Phase 7 | Blocked: methods underspecified |
| VS longest activation, DLS shortest | Blocked: methods underspecified |
| State information strongest in VS in Phase 1 | Blocked: methods underspecified |
| Action information rises in Phase 3 only in DLS | Blocked: data missing |
| Action information before cue offset higher in DLS | Blocked: data missing |
| Action information before centre exit and in Phase 5 highest in DMS | Blocked: data missing |
| Reward information rises after L/R entry, strongest in VS, then DMS | Blocked: data missing |
| Event-coding proportions follow the MI; similar in fixed and free blocks | Blocked: methods underspecified |
| Event-coding proportions above chance | Blocked: data missing |
| Action, reward and previous-trial coding in the regression | Blocked: methods underspecified |
| Action-value coding highest in DMS in Phase 5; QR coding in DMS above DLS | Blocked: methods underspecified |
| State-value coding highest in VS | Blocked: data missing |
| No policy coding | Blocked: data missing |
| Action information rises DLS, then DMS, then VS in every block type | Blocked: data missing |
| DMS action command never above DLS | Blocked: methods underspecified |
| DLS and DMS action information stronger in fixed than free blocks | Blocked: data missing |
| VS: no fixed against free difference | Blocked: methods underspecified |
| DLS action information stronger in stay than switch trials | Blocked: methods underspecified |

No count computable from the dandiset limits the paper's neuron counts, since the waveform and
histology exclusions cannot be applied, so the counts are blocked (data missing). By the
protocol's rule for dependent claims, the neural claims that depend on them and were not already
blocked are blocked for the same reason; three of these also depend on a claim blocked because
its readings disagree. The verifier agreed with these thirteen changes in a third round. The
notebook still gives each one's result as tested. In all, 6 claims are reproduced, 1 is not
reproduced and 25 are blocked.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's display equations are missing from its text and it links no code, so many method
details are open; every reading the claims file names is run, and a claim whose readings
disagree is blocked. The trial table's cue codes are described wrongly (2 is the left
tone, 3 the right, 1 the choice tone), and the units include more than the paper's stable
neurons, with a PANs flag that does not follow the Methods' rule alone. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001642-ito-2015-01.yaml`](../../attempts/001642-ito-2015-01.yaml).

- `reproduce_ito_2015.ipynb`: the analysis. It takes about 35 minutes, most of it the shuffles
  of the mutual information and the particle filters.
- `striatum.py`: loading the files, event-aligned spike counts and the mutual information.
- `models.py`: the choice models and the regression with BIC selection.
