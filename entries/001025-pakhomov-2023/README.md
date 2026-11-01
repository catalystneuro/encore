# Pakhomov et al. (2023) on dandiset 001025

Tests the findings of "Next generation CANCAN focusing for remote stimulation by nanosecond
electric pulses" (Bioelectrochemistry 152, 108437, doi:10.1016/j.bioelechem.2023.108437) on
DANDI:001025 version 0.240605.1826.

The dandiset holds one stitched YO-PRO-1 image per dish for the experiments of Figure 7. The
notebook `reproduce_pakhomov_2023.ipynb` streams the images, finds the four electrodes in each,
places the paper's ROIs along the diagonals (helper `cancan.py`), and tests the Figure 7 claims
under every reading of the ROI layout the paper allows. The other figures' data are not in this
dandiset: Figures 5, 6, 8 and 9 are in dandisets 000686, 000875, 001027 and 001028, and the
single-cell data of Figure 4 were not found.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Outcomes are in `attempts/001025-pakhomov-2023-01.yaml`.
