# Lohani, Moberly et al. (2022) from dandiset 001172

Tests the findings of [Lohani, Moberly et al. (2022)](https://doi.org/10.1038/s41593-022-01202-6)
that can be tested on [DANDI:001172](https://dandiarchive.org/dandiset/001172/0.260129.0829), which
holds dual-colour mesoscopic imaging of ACh3.0 and jRCaMP1b with face video, pupil and wheel data
from 4 of the paper's 6 mice. The ECoG, pharmacology, control mice and cholinergic axon imaging are
not in it.

| Claim | Outcome |
|---|---|
| The paper code's Allen parcels line up with the dandiset's pixels | Partially reproduced |
| Behaviour explains ACh and calcium differently across areas | Reproduced |
| Inverted anterior-posterior gradients of explained variance | Reproduced |
| Face movement is the best predictor of ACh | Reproduced |
| Face movement is the best predictor of calcium | Partially reproduced |
| Transients at face movement onset | Partially reproduced |
| Transients at locomotion onset | Partially reproduced |
| ACh transients do not differ between onset types | Reproduced |
| Calcium transients are largest at locomotion onset | Partially reproduced |
| ACh, not calcium, transients have an anterior-posterior gradient | Reproduced |
| Sustained face movement raises ACh | Reproduced |
| Locomotion does not raise ACh further | Reproduced |
| Sustained face movement and locomotion raise calcium | Partially reproduced |
| Anterior-posterior gradients of sustained state differences | Partially reproduced |
| ACh is higher in frontal-motor than visual areas during face movement | Reproduced |
| State-dependent correlations between areas (four claims, Figure 4) | Reproduced |
| Face movement increases ACh-calcium coupling broadly | Partially reproduced |
| Locomotion reduces ACh-calcium coupling in frontal cortex | Not reproduced |
| ECoG, pharmacology, hemodynamic correction, sensor validation, axon imaging (five claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files' ΔF/F times are 49.9 s early and their FaceMap and pupil timestamps are wrong; the
notebook times frames by the synchronisation pulses, as the paper's code does. The cortical areas
come from the parcel masks in the paper's code. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001172-lohani-2022-01.yaml`](../../attempts/001172-lohani-2022-01.yaml).

- `reproduce_lohani_2022.ipynb`: the analysis. It streams about 110 GB and takes about 13 minutes.
- `meso.py`: streaming the ΔF/F movies as parcel means, the timing, the code's state and onset
  definitions, the correlation and permutation statistics, and the ridge regression. Other notebooks
  on this dandiset can import it.
