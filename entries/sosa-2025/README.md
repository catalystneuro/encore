# Sosa, Plitt & Giocomo (2025) from dandiset 001361

Tests the findings of [Sosa, Plitt and Giocomo (2025)](https://doi.org/10.1038/s41593-025-01985-4) on
[DANDI:001361](https://dandiarchive.org/dandiset/001361/0.251124.0550). The dandiset holds two-photon imaging of dorsal CA1 in
the 11 switch mice over 14 days of a virtual-reality task with a hidden, moving reward zone.

Of 50 claims, 35 are reproduced and 8 not reproduced. 7 are blocked: the decoder and
the GLM (too large for the run), and the k-means remap-trial and teleport analyses (not attempted in the
run's time). After the first round of verification, place cells come from the spatial-information test as
the paper's code runs it, which gives the paper's fraction of place cells (48.7% against 48.5%). That match rests mostly on the code's 0.001 offset in the SI. After the second round no outcome changed. The third round agreed with the one proposed change: ed4l-disappearing-decrease is not reproduced, since the disappearing fraction falls significantly near reward but not far from it, and the criterion needs both.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper cites version 0.250406.0045 of the dandiset, but in that version every file of a mouse carries the
behaviour of one session, so the entry reads 0.251124.0550, where this is fixed. dF/F and the deconvolved
activity are rebuilt from the files' fluorescence and neuropil, because the files' own deconvolved series is
not the paper's signal. Cells are matched across days by this entry, because the files hold no matching. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/sosa-2025-01.yaml`](../../attempts/sosa-2025-01.yaml).

- `reproduce_sosa_2025.ipynb`: the analysis. It takes 41 to 48 minutes (the notebook prints its run time before the summary), most of it streaming the 152 files.
- `sosa.py`: loading, dF/F, OASIS deconvolution, spatial information and its shuffle, the RR
  cross-correlation and individual place fields, done for each session in parallel. Other notebooks on this dandiset can import it.
