# Andrews, Geng, Voitiuk et al. (2024) from dandiset 001132

Tests the findings of [Andrews, Geng, Voitiuk et al. (2024)](https://doi.org/10.1038/s41593-024-01782-5)
that can be tested on [DANDI:001132](https://dandiarchive.org/dandiset/001132/0.241130.1903), which holds
69 raw HD-MEA voltage recordings of 12 human hippocampal slices from 7 patients.

| Claim | Outcome |
|---|---|
| Cohort of 12 slices from 7 patients (Table 1) | Partially reproduced |
| Unit counts, light-ON firing and amplitude changes, Table 2 decreases, bursts, theta coherence and propagation, closed loop, intensity threshold, ChR2, waveform and opto-response clusters (23 claims) | Blocked: data missing (no sorted units) |
| Histology and patch clamp (3 claims) | Blocked: data missing |
| Transduction against response (1 claim) | Blocked: data missing (depends on Table 2 claims) |
| Network simulation | Reproduced (the published model, run with NEST 3.4 from conda-forge) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no sorted units, no light events and no labels for medium, drug, opsin or light
protocol. Light periods can be recovered from a voltage step in slices 3C, 4C and 7D, and in no
file of 5C, 8D, 10F or 11G. The attempt record,
with the reasons, is [`attempts/andrews-2024-01.yaml`](../../attempts/andrews-2024-01.yaml).

- `reproduce_andrews_2024.ipynb`: the survey of every recording, the cohort claim, a
  threshold-crossing variant around the 3C light trials, and the paper's network model, built
  with NEST 3.4 from conda-forge and run as published. It takes about 50 minutes, most of it
  streaming one 64-channel group of each file and every channel group of the 47 files of seven
  slices; the network model's runs, seed check included, take about 6 minutes of it.
- `hdmea.py`: streaming the files by HTTP range requests on their HDF5 chunks, the channel-mean
  trace of every channel group, light-step detection, threshold crossings and saturation. Other notebooks on this dandiset can import it.
