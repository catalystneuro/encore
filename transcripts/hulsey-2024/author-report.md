I did steps 1 to 5 of the Author protocol and ran the handover. The entry is `entries/000678-hulsey-2024/`, the record is `attempts/000678-hulsey-2024-01.yaml`, and the handover package is in `executed/000678-hulsey-2024/handover/`. `tools/entry.py all` passed with 0 errors, and the notebook ran in 13 to 14 minutes. Nothing is committed.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| cohort-inclusion | partially reproduced: 13 mice (8 auditory, 5 visual) match; 376 sessions pass the criteria, not 381 |
| training-duration | blocked, `data_missing` (only stage 5 and 6 sessions are in the dataset) |
| distractor-response-rate | reproduced: 5.2% overall; one mouse, BW053, at 16% |
| figs2-n-states | reproduced: 3 to 5 states per mouse under both readings |
| fig1g-example-mouse-prediction | reproduced: BW046 has 4 states; 70.2% against 78.3% |
| fig2a-state-types | reproduced, resting on one assumption (`assumed: true`) |
| fig2b-optimal-occupancy | partially reproduced: all tests pass; indeterminate share 14.8%, just outside 13.1 ± 1.6 |
| fig2c-dwell-times | partially reproduced: tests pass and the optimal dwell (39.5) matches; indeterminate 3.0 and disengaged 11.9 are outside tolerance |
| fig2d-prediction-accuracy | reproduced: 76.0%, a gain of 10.9 points |
| fig3c-inverted-u-pupil, fig3d-optimal-pupil-modality, fig3e-u-disengaged-pupil | reproduced |
| figs4-r2-individual-movement | partially reproduced: pupil r2 is 0.65; face and locomotion are lower on average but mostly not significantly |
| fig3f-movement-index-inverted-u | partially reproduced: shape holds and p = 0.34 as in the paper; r2 is 0.567 against 0.63 ± 0.06 |
| fig3f-movement-index-u-disengaged, figs5-movement-index-correlations | reproduced |
| fig3-distance-from-optimal-pupil | partially reproduced: the order and tests hold, but the values are larger than the paper's |
| fig3-raw-face-energy-trend, fig3-raw-locomotion-no-difference | reproduced |
| fig4a-lower-variability | partially reproduced: 5 of 6 tests pass |
| fig4b-variability-at-transitions | partially reproduced: all signs hold; 2 of the 4 marked tests pass |
| fig4d-pupil-movement-decoupling, figs6-individual-measure-decoupling | reproduced |
| fig5c-state-classification | reproduced: 88.5% and 77.2% |
| figs7-pupil-best-raw-measure | reproduced |
| fig5c-movement-index-best | not reproduced under the claim's main reading; the paper code's conditions 5 and 1 reproduce it |
| figs8a-regression-weights, figs8b-pupil-movement-interaction, figs1-iti-independence | reproduced |

**2. What was found about the dataset**
- I pinned version 0.231004.2146 because the paper cites it. The later 0.261020.0029 has identical assets and differs only in archive metadata; the notebook header says this.
- The dataset holds 391 sessions from stages 5 and 6, against 381 in the paper. Nothing marks which sessions the paper used.
- The excluded mice, the other stage 5 and 6 sessions, and all training before stage 5 are absent. That is why training-duration is blocked.
- `running_speed` is labelled cm/s but the values are m/s.
- 38 sessions have a post hoc pupil series that is entirely missing values.
- Rig names are spelled several ways ("Box 1", "Box1", "Boox1").
- No recording is deposited twice. A response against no-response contrast is consistent with the measures sharing the trial clock.

**Assumption:** one state of mouse BW059 has no trials confidently in that state (posterior ≥ 0.8) in the sessions where the optimal state occurs. The paper's state-typing code (Figure2.py) would score such a state as matching every template, so I typed it on all of the mouse's sessions. The question to the paper's authors (how such states were handled, and which 381 sessions were analysed) is recorded as a `methods_unavailable` finding.

I asked no reader questions.

**3. Where the protocol was unclear or did not fit**
1. The paper's method cannot run in full within the 30-minute notebook limit: 10 initialisations per fold for choosing the number of states, and 1000 shuffle runs for the decoders. I reduced these to 3 initialisations, and to 3 runs per shuffled condition plus 20 null runs. I recorded this as a deviation, not as `too_large`, because blocking it would have blocked almost every claim that depends on the state fits.
2. The paper's model library (its fork of ssm) is not a locked dependency, so I reimplemented the model in `hulsey.py` with the same EM, priors and stopping rule. The protocol says nothing about reimplementing a method versus installing the original; I recorded it as a deviation.
3. The protocol does not say what to do when the paper's own code has a latent bug that the data trigger (the empty-state typing above). I treated my fix as an assumption and asked the authors.
4. The protocol has no rule for a session set that the dataset cannot reconstruct (381 reported, 376 passing the criteria). I used the paper's criteria and recorded a `selection_undocumented` finding.

**4. Runtime and failures**
The run started at 09:19 and finished at 11:00 UTC. The notebook takes about 13.5 minutes on 4 cores: about 3 to stream the files, 4 for the cross-validation fits and 6 for the decoders. The last three full runs gave identical numbers. During development a first version of the model fitting diverged; I fixed it with damped Newton steps before any reported fit. Nothing failed in the final runs.
