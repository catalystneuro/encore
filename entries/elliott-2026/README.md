# Elliott, Andrews et al. (2026) on DANDI:001132

Tests the claims of Elliott, Andrews et al., "Microscale maps of bursting dynamics across human
hippocampal slices from patients with epilepsy" (J. Neurophysiol. 2026, doi:10.1152/jn.00217.2025)
on dandiset 001132 version 0.241130.1903, the raw recordings of Andrews et al. 2024. The curated
spike sortings the paper analysed are read from the paper's repository
(github.com/braingeneers/human_hippocampus at commit 0f83f70).

- `reproduce_elliott_2026.ipynb`: the link of the sortings to the raw files, and the claims that
  need spikes only.
- `lfp_elliott_2026.ipynb`: the claims on the raw voltage.
- `hippo.py`: loading (dandiset streaming, sortings from the repository) and the measures.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The outcomes are in `attempts/elliott-2026-01.yaml`.
