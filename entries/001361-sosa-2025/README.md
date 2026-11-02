# Sosa, Plitt & Giocomo (2025) from dandiset 001361

Tests the findings of [Sosa, Plitt and Giocomo (2025)](https://doi.org/10.1038/s41593-025-01985-4) on
[DANDI:001361](https://dandiarchive.org/dandiset/001361/0.251124.0550). The dandiset holds two-photon imaging of dorsal CA1 in
the 11 switch mice over 14 days of a virtual-reality task with a hidden, moving reward zone.

Of 50 claims, 27 are reproduced, 11 partially reproduced and 5 not reproduced. 7 are blocked: the decoder and
the GLM (too large for the run), and the k-means remap-trial and teleport analyses (not attempted in the
run's time).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper cites version 0.250406.0045 of the dandiset, but in that version every file of a mouse carries the
behaviour of one session, so the entry reads 0.251124.0550, where this is fixed. dF/F and the deconvolved
activity are rebuilt from the files' fluorescence and neuropil, because the files' own deconvolved series is
not the paper's signal. Cells are matched across days by this entry, because the files hold no matching. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001361-sosa-2025-01.yaml`](../../attempts/001361-sosa-2025-01.yaml).

- `reproduce_sosa_2025.ipynb`: the analysis. It takes about 40 minutes, most of it streaming the 152 files.
- `sosa.py`: loading, dF/F, OASIS deconvolution, spatial information and its shuffle, cell classes and the
  RR cross-correlation, done for each session in parallel. Other notebooks on this dandiset can import it.
