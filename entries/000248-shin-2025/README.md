# Shin et al. (2025) from dandiset 000248

Tests the Neuropixels findings of [Shin et al. (2025)](https://doi.org/10.1038/s41593-025-02055-5)
on [DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), which holds 12
Neuropixels sessions (six probes, V1, LM, RL, AL, PM and AM) recorded while mice viewed illusory
contour images. The 2p imaging and holography data of the paper are not in it.

| Claims | Outcome |
|---|---|
| 14 Neuropixels claims (unit counts, functional subsets, fixed gaze, eye, decoding, population responses) | Reproduced (ed6b, ed2b and fig3d rest on an assumption; fig3d meets the criterion with two of three seeds under the adopted decoder reading and with every seed under the other) |
| fig2d-npx-ccg-hva-input | Blocked: methods_underspecified (7 of 8 combinations of the criterion meet it; in the eighth the medians are equal; the effect is present in all 8) |
| fig1e, fig1f, fig1g (exclusively center-responsive V1 units) | Not reproduced (44 or 52 units against 18) |
| supp3-decoder-types | Blocked: too_large (the network); the quadratic and RBF SVMs agree with the linear SVM |
| 21 claims on 2p imaging, mesoscope and holography | Blocked: data_missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the findings about the dataset, is
[`attempts/000248-shin-2025-01.yaml`](../../attempts/000248-shin-2025-01.yaml).

- `reproduce_shin_2025.ipynb`: data check and the non-decoding claims, one section per claim. It
  streams the 12 session files (about 4 to 5 minutes).
- `decoding_shin_2025.ipynb`: the decoding claims (Figs. 3a, 3c, 3d, Extended Data Fig. 7) under
  both decoder readings.
- `decoding_checks_shin_2025.ipynb`: decoder reading (a) over two further cross-validation seeds,
  the bound of the C search and the coding of reading (b) in V1, PM and AM, and the quadratic and
  RBF SVMs of supp3-decoder-types.
- `decoding_seed1_shin_2025.ipynb`, `decoding_seed2_shin_2025.ipynb`: decoder reading (b) on every
  area with each of the two further seeds, one seed per notebook to stay within the notebook limit.
- `illusion.py`: loading the session files, trial responses, the functional subsets of the
  paper's code (IC-encoders, segment responders, exclusive center units), the decoder and the
  cross-correlograms. Other notebooks on this dandiset can import it.
