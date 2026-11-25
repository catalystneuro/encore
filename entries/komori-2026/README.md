# Komori, Mizusaki, Tomita, Yoneda, Matoba & Morita (2026) from DANDI:001425

Tests the resting-state findings of [Komori et al. (2026)](https://doi.org/10.64898/2026.05.27.726399)
on [DANDI:001425](https://dandiarchive.org/dandiset/001425/0.250705.0947), the cued-lever-pull
dataset of Kondo et al. (2025), whose resting-state recordings the paper reuses. The paper's own
recordings with somatosensory and visual stimulation are not deposited.

| Claim | Outcome |
|---|---|
| A GRU on 0.1 Hz ICs decodes spontaneous pupil dilation above null models | Partially reproduced (one sample reading, one seed) |
| The decoder has lower loss and higher accuracy than null | Not reproduced |
| Decoding needs a 0.1 Hz filter; 2 Hz does not decode | Not reproduced |
| 10 ICs and a 1.5 s window give the highest median AUC | Partially reproduced (10 ICs yes, 1.5 s no) |
| Maximum VIF 9.0 with 10 ICs; 7 ICs lower, 13 and 15 not different | Not reproduced |
| SHAP of a medial anterior IC rises before RSP and MOs | Not reproduced |
| 18 claims on the paper's stimulation recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every tested outcome rests on choices the paper leaves open: which three mice and sessions, which
ICs (kept "by visual inspection" in the paper), and how samples and labels are formed around each
dilation peak. The notebooks run the main reading and one change at a time. The pipeline is
rebuilt from the paper's Methods, as its published code does not cover the resting data.

- `reproduce_komori_2026_decoding.ipynb`: data check and the three decoding claims.
- `reproduce_komori_2026_features.ipynb`: IC count and window, VIF, SHAP, and the costly
  every-frame variant of the decoding claim.
- `pupilwf.py`: streaming, hemodynamic correction, SVD and JADE ICA, labels, the GRU and its
  cross-validation.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/komori-2026-01.yaml`](../../attempts/komori-2026-01.yaml).
