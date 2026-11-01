# Gao, Ramachandran, Yu & He (2025) from dandiset 001199

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
tested on [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250). The dandiset holds
sorted units (spike times only) and trial tables from 13 rats, recorded in S1, POm and auditory
cortex (AC) during transcranial focused ultrasound at 30 to 4,500 Hz PRF with 200 us pulses.

| Claim | Outcome |
|---|---|
| Rats with S1 and POm (16) and S1 and AC (12) recordings | Partially reproduced |
| AC neurons respond to 1,500 and 3,000 Hz during sonication, and to four PRFs after it | Not reproduced |
| Target determination artefact (Fig. 2) | Blocked: data missing |
| 20 claims on RSUs and FSUs (Fig. 4 to 6, 10A to 10C, 11C, 11D) | Blocked: data missing |
| 12 claims on the duty-cycle series (Fig. 7 to 9, 10D to 10F) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no spike waveforms and no RSU or FSU labels (a `celltype_label` column described as
RSU and FSU codes holds 0 or the area), so the paper's typing cannot be repeated. Only the 200 us
pulse-duration series is here. The 13 rats were recorded from August 2024 to July 2025, and only
one of them has a file in dandiset 000946, which the paper names as the repository of its data, so
this dandiset may not hold the paper's recordings. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001199-gao-2025-01.yaml`](../../attempts/001199-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  files.
- `tfus.py`: listing and reading the files, the condition of each file from its identifier and
  notes, window spike counts, the normalized rates and tests of the paper. Other notebooks on this
  dandiset can import it.
