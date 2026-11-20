# Rozsa et al. (2023) on DANDI:000341

Tests the findings of Rozsa, Toth, Olah, Baka, Lakovics, Barzo and Tamas (2023), "Temporal
disparity of action potentials triggered in axon initial segments and distal axons in the
neocortex", Sci. Adv. 9, eade4511, on dandiset 000341 version 0.241220.1312.

- `reproduce_rozsa_2023_slices.ipynb`: ZD7288, soma and bleb, and active-slice recordings (about
  13 minutes).
- `reproduce_rozsa_2023_induction.ipynb`: the human and rat RAF induction recordings (about 56
  minutes; it streams 260 GB).
- `raf.py`: streaming, AP detection and the measures both notebooks use.

The in vivo recordings (259 files, 383 GB) were not analysed. The outcomes are in
`attempts/rozsa-2023-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
