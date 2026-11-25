# Mah et al. (2023) on DANDI:001169

Tests the claims of Mah, Schiereck, Bossio and Constantinople (2023), "Distinct value computations
support rapid sequential decisions", Nature Communications 14, 7573
(doi:10.1038/s41467-023-43250-x), on dandiset 001169 at version 0.261120.1450.

- `reproduce_mah_2023.ipynb`: the data check and the behavioural claims (Figures 1, 2, 3c, 4, 5
  and the Supplementary Figures). Figure 4 reads the paper's Zenodo deposit
  (doi:10.5281/zenodo.10031483), which holds the sessions that fail the inclusion criterion.
- `models_mah_2023.ipynb`: the wait time models (Figure 3j, 3f, 3l, Supplementary Figures 8 and 9)
  and simulations of the initiation time models (Figure 3i).
- `mah2023.py`: loading (each NWB file is fetched into memory and read with h5py) and the shared
  measures and models.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
