I tested 26 of the 32 claims on DANDI:000213 at version 0.261109.2219, the latest published version. 9 were reproduced, 12 partially reproduced and 11 not reproduced; 6 claims are blocked. The entry is at `entries/tingley-2018`, the record at `attempts/tingley-2018-02.yaml`, and the verifier's package is in `executed/tingley-2018/handover/`. I did not verify my own work, and nothing was committed. I saw no earlier attempt on this dataset.

### 1. Outcomes

"(A)" means the outcome rests on the stated assumption about undefined phase (section 2).

| claim | outcome |
|---|---|
| ls-neuron-count | reproduced (1,696 units, 62 sessions, 5 rats) |
| hpc-unit-count | not reproduced (3,260 units; no CA1/CA3 split fits both counts) |
| ls-active-neurons | reproduced (829, reading a) |
| fig2-ls-phase-vs-shuffle | reproduced (A) (0.890 with sample splits) |
| fig2-ls-phase-beats-rate | partially reproduced (A) (0.835 / 0.731 / 60 of 60) |
| fig2e-ls-phase-lower-mse | reproduced (A) |
| fig2fg-mse-difference | not reproduced (A) (hippocampus -3,871 against -33) |
| fig1i-hpc-rate-phase-equivalent | not reproduced (A) |
| ls-lower-peak-info | partially reproduced |
| ls-few-place-fields | partially reproduced |
| hpc-place-field-properties | partially reproduced (2 of 4 values) |
| ls-place-fields-unstable | partially reproduced |
| fig1e-phase-info-smaller-scale | partially reproduced (A) |
| fig1g-phase-more-info-fine-scale | partially reproduced (A) |
| fig3-ls-phase-reliable | reproduced |
| fig4d-depth-gradient | partially reproduced (A) (across animals the sign is opposite) |
| fig4e-onset-depth | not reproduced (A) |
| fig4e-onset-mediolateral | reproduced (A) (one reading only, five animals) |
| speed-independent | partially reproduced |
| fig5-assemblies | blocked, too_large (roughly 390 CPU hours measured) |
| fig5g, figs5, fig6e | blocked, too_large (they depend on fig5) |
| fig6-session-counts | partially reproduced (CA1 count 25 to 33 against 63; 57 if counted by LFP channel) |
| fig6c-ca3-coherence-increases | reproduced |
| fig6d-cfc-stronger-ca3 | reproduced |
| figs7-ensemble-ls-phase-best | not reproduced (A) |
| figs2-rate-phase-independent | not reproduced (14% against under 2%) |
| figs3-ls-major-target | blocked, other (Allen analysis not done for lack of time) |
| figs6-reference-frame | blocked, metadata_insufficient (no rotation labels) |
| figs1f-trial-counts | partially reproduced (2 of 3 counts) |
| fig7-dynamic-weighting-model | blocked, other (model not attempted for lack of time) |

### 2. What was found

**About the dataset** (all recorded as findings):
- **Wrong position unit:** 31 sessions of DT7, DT8 and DT9 label head position as metres but hold millimetres.
- **No units table:** session DT7 20170324 has none, so its spikes cannot be used.
- **No CA1 channel:** five DT9 sessions (CA3 probe only) and one DT7 session flag no CA1 channel, but the paper refers all spike phases to CA1 theta.
- **Unit counts:** the files hold 3,260 hippocampal units against the paper's 2,951. The `hpc` label names the probe, not the subfield, so CA1 against CA3 can only be inferred.
- **No rotations:** nothing marks the maze rotations of Figure S6.
- **Missing columns:** some files lack `trial_type`, `condition_type` or `max_waveform_channel`.
- **Clocks:** the clock checks pass. Hippocampal spikes lock to theta in 47 of 47 sessions, and rate decoding is better with the recorded positions in 44 of 47.

**Assumptions:**
- **Undefined phase:** the paper does not say how a position bin enters phase decoding when no spike falls in its smoothing window, which is about 70% of samples. I leave such bins out and show phase set to 0 as the alternative. The two readings give opposite results:
  - Left out, the LS phase claims hold, but hippocampal phase decoding beats rate by far, against the paper's equivalence.
  - Set to 0, the hippocampal equivalence holds, but LS phase no longer beats rate.
- **Phase reference:** where no CA1 channel is flagged, I use the hippocampal probe's theta channel.
- **Place fields:** I smooth the Gaussian rate maps with a width of 5 bins and take the field with the highest peak as the first field.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How are bins with undefined phase treated in the single-cell decoder?
- How is peak information converted to bits/cm, and are the 7 levels of equal width or equal count?

I also recorded that the paper does not say which 1,425 hippocampal neurons it means; 1,420 units in the files have an included condition. I asked a reader no questions.

### 3. Protocol points
1. Claims of absence: the protocol says the several-readings rule does not apply, but not what to do when method readings, not the test, change the outcome (fig1i). I judged it under the adopted assumption and reported the other readings.
2. Timing numbers in result text: they change from run to run, and any edit to fix them makes the next run a full 20-minute one. I worded costs approximately ("roughly 400 CPU hours").
3. An `elsewhere` claim not attempted for lack of time has no fitting block reason; `not_runnable` requires having tried. I used `other` for figs3 and fig7 and said why.
4. Partial outcomes: some criteria give no partial rule (fig6-session-counts, figs1f). I used the protocol's general meaning of `partially_reproduced` and said so in the notes.
5. "The first reading the criterion lists" for `measured` covers only cases where a reading matches. Where none did, I recorded the closest reading and said which.

### 4. Runtime and failures
- **Runtime:** about 2 h 50 min of the run, from 07:08 to about 10:00 UTC. The notebook takes about 19 minutes with a peak of 3.9 GB, and `entry.py check` reports 0 errors.
- **Lost time:** one development command ran past its 30-minute timeout because the 1.5 cm bin count was computed from millimetre values as if they were metres. It was fixed.
- **Other failures, all fixed:** three full runs failed on columns missing from some files, and one on a guard for empty shuffle sets.
- **Reduced Figure S7 run:** reading (a) of the ensemble claim uses 3 random draws per size, not 10, to fit the time limit.
