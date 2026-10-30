# MICrONS Consortium (2025) from dandiset 000402

Tests the findings of [the MICrONS Consortium (2025)](https://doi.org/10.1038/s41586-025-08790-w)
that can be tested on [DANDI:000402](https://dandiarchive.org/dandiset/000402/0.230307.2132), which
holds the 19 two-photon scans of the MICrONS mouse: masks, fluorescence traces, stimulus tables and
video, treadmill and eye tracking. The paper describes 14 of these scans (its Extended Data Table 1).
Most of the paper's EM findings rest on CAVE tables that need an account token and are not tested.

| Claim | Outcome |
|---|---|
| 14 scans, P75 to P81 | Reproduced |
| Scan rates, fields and depths (11 / 2 / 1 scans) | Reproduced |
| 125,413 masks, 115,372 somatic | Reproduced |
| 75,909 unique neurons | Blocked: data missing |
| Half of the volume in VISp | Blocked: metadata insufficient |
| Z drift under 10 um | Blocked: data missing |
| Structural stack | Blocked: data missing |
| Stimulus composition of each scan | Reproduced |
| Stimuli conserved across scans | Partially reproduced |
| Oracle clips in the same order | Reproduced |
| Spontaneous periods before and after the stimulus | Partially reproduced |
| Monet2: 16 directions per 15 s block | Reproduced |
| Fig. 3f: oracle reliability | Reproduced |
| Fig. 3g: direction tuning | Reproduced |
| Treadmill and eye tracking throughout each scan | Partially reproduced |
| Photodiode code recovered for 89% of trials | Blocked: data missing |
| 144,120 nuclei in subvolume 65 | Reproduced |
| Neuron and cell type classification | Reproduced |
| Synapse counts | Partially reproduced (both counts within tolerance; precision, recall and partner accuracy not tested) |
| EM sections | Partially reproduced (share of subvolume 35 within tolerance; 19,952 sections with data against 19,974) |
| Co-registration and the other EM claims (16 claims) | Blocked: other (the CAVE tables they test, or that choose their neurons, need an account token) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset holds fluorescence traces only, so the trace analyses use fluorescence in place of the
deconvolved traces. The direction of each Monet2 period is not in the stimulus table and is measured
from the stimulus video by optical flow. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000402-microns-2025-01.yaml`](../../attempts/000402-microns-2025-01.yaml).

- `reproduce_microns_2025.ipynb`: the analysis of the dandiset and of the nucleus and cell type
  tables. It took 10 minutes in the last run, most of it reading the stimulus video and the traces
  of the oracle and Monet2 trials.
- `em_volume_counts.ipynb`: the EM sections, from the imagery on BossDB, and the synapse counts of
  the two subvolumes, from their tables on BossDB. It took 12 minutes in the last run, most of it
  streaming the two synapse tables (34 GB).
- `microns.py`: loading the files, the oracle score, the Monet2 directions from the video, the
  per-mask responses and the mask centroids, and reading the EM imagery and synapse tables on BossDB. Other notebooks on this dandiset can import it.
