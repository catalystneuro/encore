# Xia, Yang, Mu, Micovic, Poskanzer, Monaghan & Clark (2021) from SPARC:108 and SPARC:75

Tests the findings of [Xia et al. (2021)](https://doi.org/10.1073/pnas.2023807118), a DNA-based nanosensor
for acetylcholine imaged in the submandibular ganglion of living mice, on the two SPARC datasets that hold its
data: [SPARC:108](https://sparc.science/datasets/108) version 1 (doi:10.26275/w027-cisv), the deposit the
paper cites, and [SPARC:75](https://sparc.science/datasets/75) version 1 (doi:10.26275/prjd-jhoc), confocal
images of a ganglion stained with BTX or the nanosensor.

| Claim | Outcome |
|---|---|
| HPLC: nanosensors are 77% of the pHAb peak area (Fig. 2D) | Not reproduced |
| Native PAGE: several slower bands carrying pHAb and AF647 (Fig. 2E, S2C) | Reproduced |
| BTX staining is punctate across the ganglion (Fig. S5) | Reproduced |
| Nanosensor AF647 and pHAb puncta overlap on the somata (Fig. 3D) | Partially reproduced |
| Ex vivo Michaelis-Menten calibration, Km 49 uM (Fig. 4B) | Not reproduced |
| Lower limit of detection 228 nM (Fig. 4B) | Not reproduced |
| In vivo response of 3.7% at 3 V (Fig. 5B) | Not reproduced |
| Vesamicol cuts the response by 77% (Fig. 6) | Partially reproduced |
| The AF647 channel does not respond (Fig. S16) | Reproduced |
| Conjugation ratios, AFM size, retention, stability, response time, unit calibration, pH, controls, voltage and pulse series, reversibility, two-photon (14 claims) | Blocked: data missing or metadata insufficient |
| AQuA analyses (Fig. 7, S9, S12; 4 claims) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

SPARC:108 holds a part of the paper's data: one of three calibration mice, one of four vesamicol experiments,
the 3 V and 8 V recordings of the AQuA mouse and a 10 V recording, and none of the control nanosensor
recordings. Its recordings carry no channel labels, spatial scale or stimulation times. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/xia-2021-01.yaml`](../../attempts/xia-2021-01.yaml).

- `reproduce_xia_2021.ipynb`: the analysis. It takes about two minutes, most of it streaming the files.
- `xia2021.py`: reading the pinned versions from the SPARC bucket, the photobleaching correction, dF/F, initial
  rates, the Michaelis-Menten fit, gel lanes and puncta. Other notebooks on these datasets can import it.
