# Dehaqani, Michelon et al. (2024) from dandiset 000931

Tests the findings of [Dehaqani, Michelon, Patella, Petrucco, Piasini & Iurilli (2024)](https://doi.org/10.1016/j.celrep.2024.114013)
on [DANDI:000931](https://dandiarchive.org/dandiset/000931/0.261011.1559). The dandiset holds one
NWB file: the spike times of 1013 sorted units from one of the paper's 22 mice, from the
concentration-series experiment. It has no breathing signal, inhalation times, odor trials,
artificial airflow pulses, unit waveforms or brain areas, and every claim needs some of these.

| Claim | Outcome |
|---|---|
| All 37 claims (inhalation sorting and decoding, odor responses and inhalation speed, encoding models, airflow tuning, bulbectomy, neurectomy, motor cortex, population decoding of concentration, simulation, waveform control) | Blocked: data missing |

The notebook lists what the dandiset holds, shows per claim which data it needs and which are
missing, and checks the unit table against its description and the paper's spike-sorting
criteria. The attempt record, with its findings about the dataset, is
[`attempts/000931-dehaqani-2024-01.yaml`](../../attempts/000931-dehaqani-2024-01.yaml).
