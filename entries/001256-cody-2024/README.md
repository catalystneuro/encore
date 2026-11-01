# Cody, Kumar & Tzounopoulos (2024) from dandiset 001256

Tests the findings of [Cody et al. (2024)](https://doi.org/10.1523/JNEUROSCI.0939-23.2024) on
[DANDI:001256](https://dandiarchive.org/dandiset/001256/0.241120.2150), which holds two-photon imaging of
right auditory cortex and video pupillometry in 30 mice (C57BL6/J, ZnT3-WT and ZnT3-KO) during low- and
high-contrast dynamic random chords, before and after ZX1 or ACSF. The widefield experiments of Figure 5
are not in it.

| Claim | Outcome |
|---|---|
| Pure-tone responses peak at intermediate baseline PD (Fig. 1f) | Reproduced |
| Response reliability peaks at intermediate baseline PD (Fig. 1g) | Reproduced |
| Contrast scaling factor largest at intermediate baseline PD (Fig. 1h) | Reproduced |
| Contrast scaling factor above 1 in every baseline PD bin (Fig. 1h) | Not reproduced |
| Baseline PD effect and contrast interaction on pure-tone responses (Fig. 1i) | Reproduced |
| Contrast effect only in the 43-54% bin (Fig. 1i) | Not reproduced |
| Evoked PD over 0-8 s larger in high contrast (Fig. 2b) | Not reproduced |
| Evoked PD over 1-2 s larger in high contrast (Fig. 2c) | Blocked: methods underspecified |
| DRC cell responses do not differ by contrast (Fig. 2e) | Not reproduced |
| LME: baseline PD predicts responses, evoked PD does not (Fig. 3b) | Reproduced |
| LME: full model no better than null (Fig. 3c) | Not reproduced |
| ZnT3-WT: contrast and ZX1 effects and their interaction (Fig. 4c) | Partially reproduced |
| ZnT3-WT: post hoc contrast and ZX1 effects (Fig. 4c) | Not reproduced |
| ZnT3-KO: no contrast or ZX1 effect on the intercept (Fig. 4f) | Blocked: methods underspecified |
| ZnT3-KO: ZX1 still reduces the slope, less than in WT (Fig. 4f) | Not reproduced |
| Figure 5 (three claims, widefield imaging) | Blocked: data missing |
| Baseline PD drifts up in ZX1 and ACSF experiments alike (Fig. 6a) | Partially reproduced |
| Contrast effect on intercept and slope after ACSF (Fig. 6b) | Partially reproduced |
| No baseline-evoked PD correlation below 50% (Fig. 6c) | Blocked: methods underspecified |
| Negative baseline-evoked correlation overall, none below 50% (Methods) | Blocked: methods underspecified |
| ZnT3-KO slope below ZnT3-WT in high contrast (Fig. 6d) | Reproduced |
| High-contrast peaks near 110% after ZX1 in WT and in KO (Discussion) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry labels that name the paper's analyses, which identify most of the paper's groups. The
pupil traces hold tracking failures that the Methods' cleaning does not remove, so the cleaning was
extended (an assumption, with the paper's single pass and the first round's cleaning shown as variants).
Several of the Figure 1, 4 and 6 outcomes change with the cleaning (the Fig. 1i interaction, the Fig. 4
effects and post hoc tests, Fig. 6c and Fig. 6d), and the Fig. 2b and 3b outcomes rest on keeping the
ZnT3-WT mouse that the files put in group A; the notebook's last section shows by how much. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/001256-cody-2024-01.yaml`](../../attempts/001256-cody-2024-01.yaml).

- `reproduce_cody_2024.ipynb`: the analysis. It takes about three minutes, most of it streaming the files.
- `zinc_pupil.py`: loading the trials, pupil cleaning and measures, dF/F and pure-tone responses, cell
  inclusion and the growth curve polynomials. Other notebooks on this dandiset can import it.
