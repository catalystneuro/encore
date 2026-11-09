# Wong-Campos et al. (2023) from dandiset 001791

Tests the findings of [Wong-Campos et al. (2023)](https://doi.org/10.1101/2023.05.25.542363),
"Voltage dynamics of dendritic integration and back-propagation in vivo" (bioRxiv preprint,
version 1), that can be tested on
[DANDI:001791](https://dandiarchive.org/dandiset/001791/0.260424.0313). The dandiset holds the
per-branch voltage traces and summary tables of the authors' pipeline, grouped by figure, and HiLo
z-stacks; it follows a later version of the paper than the preprint. The imaging movies, the
recordings of dendrite-targeted stimulation and the morphology reconstructions are not in it.

| Claim | Outcome |
|---|---|
| Light pulses of rising intensity evoke rising spike rates and dendritic bAPs (Fig. 1d) | Reproduced |
| Dendritic STAs peak after the somatic spike (Fig. 1f-g) | Partially reproduced |
| bAP amplitude halves at 242 μm from the soma, R2 0.49 (Fig. 2e) | Reproduced |
| bAP delays range from 1.5 to 4 ms over 50 to 280 μm (Fig. 2f) | Not reproduced |
| Conduction speed 0.09 m/s, R2 0.43 (Fig. 2f) | Reproduced |
| Dendrite pairs correlate 91% anesthetized and 73% awake (Fig. 3d) | Partially reproduced |
| Spontaneous doublets have ISIs of 18 ± 7 ms, 216 events (Fig. 4a) | Not reproduced |
| The first spike of a doublet fails to propagate, the second succeeds (Fig. 4b-c) | Partially reproduced |
| Accelerating trios amplify the third bAP, decelerating trios suppress it (Fig. 4d) | Partially reproduced |
| Air-puff bursts: first bAP fails, all dendritic spikes start as bAPs (Fig. 4i-k) | Partially reproduced |
| The sensory plateau lasts about 400 ms (Fig. 4l) | Not reproduced |
| Spontaneous bAP failures occur awake and anesthetized (Fig. S12) | Partially reproduced |
| Sustained optogenetic stimulation: first bAP attenuated, biphasic amplitude, larger distally (Figs. 4e-h, S13; three claims) | Blocked: no dendrite meets the paper's distal rule |
| Trial-to-trial bAP variation, shot-noise bound, dendrite coupling, dendritic spikes (Figs. 2c, S9, 3i, S11; four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes rest on a stated assumption: the site set of Fig. 2, the pair set of Fig. 3d, the
timing of peaks below one frame and the pulse times of Fig. 1. The paper does not settle these.
In the anesthetized recordings of Fig. S12 no column is shown to be a soma, so that half of the
claim is not tested. The attempt record, with the reasons and the differences from the
paper's method, is
[`attempts/wong-campos-2023-01.yaml`](../../attempts/wong-campos-2023-01.yaml).

- `reproduce_wong_campos_2023.ipynb`: the analysis. It takes about a minute, most of it streaming
  the files.
- `dendvolt.py`: loading every trace file of the dandiset, the list of its duplicate files, and the
  measures (spike detection, STA delays, bAP amplitudes, doublets and trios). Other notebooks on this
  dandiset can import it.
