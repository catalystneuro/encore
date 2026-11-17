I've finished steps 1 to 6: the entry `entries/shi-2013/`, the record `attempts/shi-2013-01.yaml`, and the handover in `executed/shi-2013/handover/`. The data set holds monkey X only, and which trial code means Vision is not documented, so I inferred it from the data. Of the 28 claims, 7 are reproduced, 6 partially reproduced, 12 not reproduced and 3 blocked. Nothing is committed.

**(1) Outcomes** (monkey X only; 359 sessions, first unit of each; counts scaled to 343)

| Claim | Outcome | Key numbers |
|---|---|---|
| behavior-mean-position-sessions | not reproduced | 16.1% (paper 6.9 ± 1.5) |
| behavior-variability-sessions | not reproduced | 8.1 / 8.1 / 7.0% (only z within tolerance) |
| table1-endpoint-means | partially reproduced | 48 of 48 X means within; largest V–NV gap 0.150 cm, above the 0.121 bound |
| table1-endpoint-sd | not reproduced | 8.3% within; SDs about half the paper's |
| fig3-example-neuron | not reproduced | no matching neuron |
| movement-epoch-tuning | not reproduced (assumed) | 52.1% (paper 41%) |
| hold-position / vision / interaction | reproduced ×3 | 39.3 / 13.6 / 7.5% |
| hold-subepochs | not reproduced | 1 of 6 within |
| hold-overall-effects | partially reproduced | 40.4 / 18.7 / 13.1% |
| correlation-endpoint-datasets | reproduced (assumed) | r 0.924 / 0.915, P = 0.47 |
| fig4-indx1-negative, fig4-indx1-means | partially reproduced ×2 | |
| indx1-tuning-shift, indx2-means | not reproduced ×2 | |
| rate-variance-nv-higher | partially reproduced (assumed) | 46.4 vs 23.1 (paper 56 vs 30) |
| fig5-fano-factor | not reproduced (assumed) | 1.84 vs 3.19, P = 0.28 |
| cv2-larger-nv | reproduced (assumed) | P = 0.024 |
| fig6-decoding-vv / nvnv | not reproduced (assumed) | 77.4% / 63.7% |
| decoding-v-better-than-nv | reproduced (assumed) | P = 0.009 |
| fig6-decoding-cross | reproduced | 58.9 / 52.7% |
| decoding-subepochs, decoding-nonsignificant-cells | not reproduced ×2 | |
| eye-position-no-difference, aborted-trials-nv | blocked: `metadata_insufficient` | |
| longer-hold-no-difference | blocked: `data_missing` | |

**(2) What I found about the dataset**
- **Monkey B is missing.** Every session has monkey X's target layout; none has monkey B's.
- **More sessions than the paper used.** 359 monkey X sessions have the full design (485 sorted units), against the paper's 219 neurons. Which ones the paper used is not documented.
- **Undocumented formats.** The event codes don't match `EventCodes.txt`. Each trial ends with an unlabelled text record (target, a 4/7 condition code, one hand position per trial in Table 1's frame, task parameters). The analog channels are unnamed, so I found no arm or eye trace. Time units (ms for spikes, s for events) are not stated; I checked them against a `.plx` file.
- **No duplicate recordings.** The spike clock and the event clock agree.

**Assumptions:**
- Code 7 is No Vision: aborts after the reach are higher on code 7 trials (5,688 vs 4,423), while aborts before it are equal.
- Event 12 is the end of the hold and event 8 is movement onset, both read from their timing.
- I adopted one reading where the paper allows two, for the correlation pairs, the Fano factor outliers and CV2.

The questions for the paper's authors are recorded as a `methods_unavailable` finding. I asked no reader questions.

**(3) Where the protocol was unclear or missing something**
1. Data labels: step 1.6 covers methods the paper leaves open, not missing labels in the data (here, which code is Vision). I treated the mapping as an assumption, marked the outcomes that depend on it, and blocked aborted-trials-nv, because the mapping comes from the same aborts that claim tests.
2. Counts when the sample size differs: claims give counts out of 343, but only 359 monkey X cells exist. I compared percentages and recorded counts scaled to 343.
3. Partial deposits: when one animal is missing from a dataset, the protocol offers only `dataset_missing`, which applies to whole datasets. I recorded a `data_missing` finding and a deviation on each claim.
4. Table 1 has 96 expected values but only 48 can be measured, and the schema has no null. I left out `measured` there and put the numbers in the notes.
5. CRCNS streaming: a gzip tar can't be opened at random, so the notebook makes one 6–9 min pass. That fits the time limit but isn't covered in archives.md.

**(4) Runtime and failures**
- Final notebook run took 7 min; peak memory 0.48 GB.
- `lock`, `check` and `all` passed with 0 errors; `handover` ran.
- Nothing failed. One permission prompt to read a cached tool output was denied; I read the same numbers from the executed notebook instead.

The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts`, …) and two pre-existing edits under `tools/`.
