# Scherrer, Lynch, Zhang & Fee (2023) from dandiset 000691

Tests the findings of [Scherrer et al. (2023)](https://doi.org/10.1038/s41592-023-01806-1) on
[DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version 0.260827.1358,
which holds one session of one mouse imaged with the large-FOV head-mounted microscope (the
Kiloscope) while it explores a square loop maze: the raw imaging video, 2948 EXTRACT footprints
with their traces and masks, and a behaviour video. The claims file was written from the paper's
full text and its code; the optical measurements of five claims are read from the paper's code
repository, where the claims file places them.

| Claim | Outcome |
|---|---|
| Thousands of neurons imaged in a freely moving mouse | Reproduced |
| Field of view of 4.8 x 3.6 mm (with the code's pixel sizes) | Reproduced |
| Featherscope resolution about 4 um at the centre, 7 um at the edge | Reproduced |
| Kiloscope resolution about 4 um at the centre, 5 um at the edge | Partially reproduced |
| Flat illumination with the axicon correction (Featherscope, Kiloscope) | Reproduced (both) |
| Motion of the field of view of 0.13 pixels RMS | Not reproduced |
| Quadrant and direction, and octant, decoded above shuffled data; decoder size; local decoding maps | Blocked: not runnable within the time limit |
| Coactive footprints spread across the field of view; footprints with localized activity; field curvature; LMAN bursting (whose data are also missing) | Blocked: methods underspecified |
| 2,382 footprints after curation | Blocked: metadata insufficient |
| Other mice, songbirds, singing rate, weights, resolution targets, ADC | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no position of the mouse, so it is tracked from the behaviour video with the
rule in the paper's code. It does not mark which footprints the paper's curation kept, so all 2948
are used. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000691-scherrer-2023-02.yaml`](../../attempts/000691-scherrer-2023-02.yaml); the earlier,
deprecated attempt is [`attempts/000691-scherrer-2023-01.yaml`](../../attempts/000691-scherrer-2023-01.yaml).

- `reproduce_scherrer_2023.ipynb`: the data check and most claims (about 7 minutes).
- `decoding_quadrant_direction.ipynb` and `decoding_octant.ipynb`: the decoders under one reading
  of the paper's null, and the cost of the analyses that were not run (about 20 minutes each, on
  four cores).
- `motion_scherrer_2023.ipynb`: rigid registration of the whole imaging movie, streamed in blocks,
  with checks that the movie is the raw video and that the registration finds a known jitter
  (about 25 minutes on four cores).
- `decoding_null_n2_quadrant_direction.ipynb` and `decoding_null_n2_octant.ipynb`: eight more null
  decoders of the second reading (200 fits each) for each decoding claim (about 22 minutes each).
- `decoding_reduced.ipynb`: reduced runs of the decoder-size and map analyses, which decide no
  outcome (about 21 minutes).
- `kiloscope.py`: loading the session, its masks and movie, tracking the mouse, the labels and
  decoders of the paper's code, NMF, place maps, the motion registration, and the bead and
  illumination measurements. Other notebooks on this dandiset can import it.
