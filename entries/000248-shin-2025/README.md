# Shin et al. (2025) from dandiset 000248

Tests the Neuropixels findings of [Shin et al. (2025)](https://doi.org/10.1038/s41593-025-02055-5)
on [DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), which holds 12
Neuropixels sessions (six probes, V1, LM, RL, AL, PM and AM) recorded while mice viewed illusory
contour images. The 2p imaging and holography data of the paper are not in it.

| Claims | Outcome |
|---|---|
| 18 Neuropixels claims and the decoder comparison | Blocked: too_large (the author's run reached its time limit before the notebook was executed; it ran afterwards as the entry check, in 20 minutes, and its outputs were not reviewed) |
| 21 claims on 2p imaging, mesoscope and holography | Blocked: data_missing |

The attempt record, with the reasons and the findings about the dataset, is
[`attempts/000248-shin-2025-01.yaml`](../../attempts/000248-shin-2025-01.yaml).

- `reproduce_shin_2025.ipynb`: the analysis, one section per claim. It streams the 12 session
  files (about 3 minutes) and runs the decoders in parallel; the whole took 20 minutes in the entry check.
- `illusion.py`: loading the session files, trial responses, the functional subsets of the
  paper's code (IC-encoders, segment responders, exclusive center units), the decoder and the
  cross-correlograms. Other notebooks on this dandiset can import it.
