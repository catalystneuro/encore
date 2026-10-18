# Scherrer, Lynch, Zhang & Fee (2023) from dandiset 000691

Tests the findings of [Scherrer et al. (2023)](https://doi.org/10.1038/s41592-023-01806-1) that can
be tested on [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), which holds
one session of one mouse imaged with the large-FOV head-mounted microscope while it explores a
looped maze: the raw imaging video, 2948 EXTRACT footprints with their traces, and a behaviour
video. The paper is not open access; the claims come from its abstract and its public Extended
Data legends.

| Claim | Outcome |
|---|---|
| Thousands of neurons imaged in a freely moving mouse | Reproduced |
| Quadrant and direction decoded from the activity | Reproduced |
| Octant decoded from the activity (Extended Data Fig. 9b) | Reproduced |
| Local decoders of 32 footprints significant in parts of the FOV (Extended Data Fig. 9c) | Reproduced |
| Footprints with activity localized in the maze (Extended Data Fig. 10) | Reproduced |
| Coactive populations spread across the FOV (Extended Data Fig. 8) | Reproduced |
| Flat illumination with axicon correction (Extended Data Fig. 2b, 2c; images in the paper's code repository) | Partially reproduced (both) |
| 2382 footprints after curation; field of view of about 4 mm | Blocked: metadata insufficient |
| Other mice, songbirds, weights, resolution targets, ADC | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no position of the mouse, so it is tracked from the behaviour video with the
rule in the paper's code. It does not mark which footprints the paper's curation kept, so all
2948 are used. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/000691-scherrer-2023-01.yaml`](../../attempts/000691-scherrer-2023-01.yaml).

- `reproduce_scherrer_2023.ipynb`: the analysis. It takes about 25 minutes on four cores, most of it fitting
  decoders.
- `kiloscope.py`: loading the session, tracking the mouse, the labels and decoders of the paper's
  code, and the radial illumination profiles. Other notebooks on this dandiset can import it.
