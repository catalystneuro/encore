# Park, Wong-Campos et al. (2025) from dandiset 001266

Tests the findings of [Park, Wong-Campos et al. (2025)](https://doi.org/10.1038/s41467-025-55819-9),
"Dendritic excitations govern back-propagation via a spike-rate accelerometer", on
[DANDI:001266](https://dandiarchive.org/dandiset/001266/0.250710.0758). The dandiset holds the example
recordings of the paper's figures: raw voltage imaging movies of CA1 pyramidal neurons in slices,
with their optogenetic, EFS and patch clamp channels. The paper's Source Data file maps each file to
a figure panel. The pooled samples behind most of the paper's statistics are not in the dandiset.

| Claim | Outcome |
|---|---|
| The dandiset's files are the recordings the Source Data index names | Reproduced |
| Fig. 2: 8 of 54 trials with a dSpike, never on the first spike | Reproduced |
| Fig. 2b: unimodal somatic, bimodal distal amplitudes | Blocked: methods underspecified |
| Fig. 2e-f: dSpikes amplify the distal bAP | Not reproduced |
| Fig. 2h: length constant 255 µm | Not reproduced |
| Fig. 3: dSpikes never start in the dendrites | Not reproduced |
| Fig. 3: two motifs, independent of stimulus location | Not reproduced |
| Fig. 3e: soma stimulation, 6 of 54 third-bAP dSpikes | Not reproduced |
| Fig. 3d: distal stimulation, 35 of 54 first-bAP dSpikes | Reproduced, on an assumption |
| Fig. 3f: soma plus distal, third-bAP dSpike in 54 of 54 | Not reproduced |
| Fig. 3: dSpikes need 15 ms of distal depolarization | Not reproduced |
| Fig. S7b: first components hold 96% of the variance | Blocked: methods underspecified |
| Fig. 4a: step example, failure, dSpike, dSpike, failures | Reproduced |
| Fig. 4d: wide-field example alternates | Not reproduced |
| Fig. S15: stochastic dSpikes with regular somatic spiking | Not reproduced |
| Fig. S17e: 100 nM TTX removes dSpikes | Blocked: methods underspecified |
| Fig. S18g: Ba2+ adds putative Ca2+ spikes, Ni2+ removes them | Reproduced |
| Fig. 5a: plateau of about 120 ms with combined stimuli | Not reproduced |
| Fig. 5d: a single bAP with EFS gives no plateau | Blocked: methods underspecified |
| Fig. 5b: combined AUC 3.1 times the sum of the single ones | Blocked: data missing (10 of 28 cells shown) |
| Fig. S23: dendrite minus soma lasts about 300 ms | Not reproduced |
| Fig. S2: imaging fidelity (noise, sensitivity, spike detection) | Not reproduced |
| Fig. S2d: same sensitivity at 1 and 2 kHz | Reproduced |
| 28 other claims on pooled samples | Blocked: data missing |
| Model: soma step gives failure, success, success, failures | Not reproduced |
| Model: patch injection spikes in the dendrite, optogenetic stimulus at the soma | Reproduced |
| Model: motif robust over parameter sweeps | Not reproduced |
| Two-compartment Izhikevich model | Reproduced (Python port of the MATLAB script) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no regions, structural images, stimulus masks or pixel size, so the soma and a line
along the apical trunk are found on each movie's mean image, and distances use the Methods' 0.65 µm
per pixel. Spike and dSpike thresholds follow the claims file's rules where the paper set them by
hand, and several outcomes depend on them (see the notebook). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/001266-park-2025-01.yaml`](../../attempts/001266-park-2025-01.yaml).

- `reproduce_park_2025.ipynb`: the analysis. It takes about 17 minutes, most of it streaming 43
  movies (about 41 GB) from the archive.
- `simulations_park_2025.ipynb`: runs the paper's published NEURON model (Supplementary Software 1)
  for the model claims, its three phase diagrams (429 runs on 4 processes) and a Python port of
  the Izhikevich model (Supplementary Software 2), in about 37 minutes.
- `dendrite.py`: streaming the movies into soma and trunk traces, the trunk tracer, bAP and
  dSpike calls, and the AUC and duration measures. Other notebooks on this dandiset can import it.
