# Semenov, Kim, Silkuniene & Pakhomov (2025), Figure 4, from dandiset 001273

Tests the Figure 4 findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660)
on [DANDI:001273](https://dandiarchive.org/dandiset/001273/0.250805.1356), which holds the pulsed
laser strobe imaging of FluoVolt-loaded rat hippocampal neurons exposed to 2-us pulses: 181 files,
each one replicate of 160 images at 50-ns steps, forming 22 experiments of 7 or 8 replicates.

| Claim | Outcome |
|---|---|
| The poles of polarization lie along the field axis | Reproduced (13 of 14 experiments with a stated axis) |
| No difference between the cathodic and anodic poles | Reproduced |
| Pooled time constants 0.7, 0.91, 0.65 and 0.8 us | Not reproduced |
| Time constants double in elongated cells aligned with the field | Blocked: metadata insufficient |
| Discharging slower than charging, except elongated parallel cells | Blocked: metadata insufficient |
| Full charge within 3 us | Blocked: metadata insufficient |
| Sustained firing through a 2-s sine wave, then block (Figure 3C, dandiset 001030) | Partially reproduced |
| Di-8-ANEPPS control (Figure S1, dandiset 001272) | Not reproduced |
| Claims on the paper's other dandisets (9) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset holds the images only: no ROIs (including the debris ROI the paper used to scale out
laser-flash fluctuations), no cell shape or orientation groups, and the electrode axis for 14 of the
22 experiments. The notebook rebuilds the RATIO image and the polarized ROIs as the Methods describe.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001273-semenov-2025-01.yaml`](../../attempts/001273-semenov-2025-01.yaml).

- `reproduce_semenov_2025.ipynb`: the analysis. It takes about 25 minutes, nearly all of it
  streaming the 10 GB of images.
- `elsewhere_001030.ipynb`: the Figure 3C claim, on the 2-s sine wave sessions of dandiset 001030
  (about a minute).
- `elsewhere_001272.ipynb`: the Figure S1 claim, on the Di-8-ANEPPS sessions of dandiset 001272
  (about two minutes).
- `fastimg.py`: loading those sessions and the AP detection readings of the claims file.
- `strobe.py`: listing and grouping the files, loading an experiment in time order, the RATIO
  image, the ROIs, dF and the exponential fits. Other notebooks on this dandiset can import it.
