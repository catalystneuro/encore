# Kim et al. (2023) from dandiset 000633

Tests the findings of [Kim et al. (2023)](https://doi.org/10.3390/ijms241310921) that can be tested
on [DANDI:000633](https://dandiarchive.org/dandiset/000633/0.231013.2226), which holds the two
whole-dish YO-PRO-1 images of the paper's Figure 4: a BPAE monolayer after five single pulses on
one base electrode of a triangular array, and one after five paired pulses on the two base
electrodes in alternation. The data of Figures 2, 3 and 5 are not in it.

| Claim | Outcome |
|---|---|
| Under single pulses, uptake follows the field map (Figure 4A) | Reproduced, resting on an assumption |
| Under paired pulses, uptake is strong at the apex and weak at the base electrodes (Figure 4B,C) | Reproduced, resting on an assumption |
| The electroporated region is a comet pointing from the apex to the base (Figure 4B,C) | Reproduced, resting on an assumption |
| Figure 2: cancellation and facilitation by the angle of the field vector (four claims) | Blocked: data missing |
| Figure 3: co- and cross-directional pairs in a square array (three claims) | Blocked: data missing |
| Figure 5: membrane charging by strobe imaging (two claims) | Blocked: data missing |

The field map of the paper's simulation is not deposited; it is computed here from the geometry
the paper states and the electrode positions measured in the images. The single-pulse file's
description gives the settings of another exposure; the file is taken as Figure 4A from its name
and its image, and both of the first two outcomes rest on that. The file does not say which base
electrode was pulsed; it is taken as the lower-right one, which has the most uptake. For the
comet shape, the pixels on objects bright in the membrane stain (0.54% of the region, likely
debris) are left out before the maximum is taken; with them the region is empty. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000633-kim-2023-01.yaml`](../../attempts/000633-kim-2023-01.yaml).

- `reproduce_kim_2023.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  two 1 GB files.
- `swing.py`: streaming and binning the stitched images, finding the electrode footprints, the
  two-dimensional field model, and the ROI measures. Other notebooks on this dandiset can import it.
