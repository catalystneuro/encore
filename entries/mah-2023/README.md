# Mah et al. (2023) on DANDI:001169

Tests the claims in `claims/mah-2023.yaml` for Mah, Schiereck, Bossio and Constantinople (2023), "Distinct
value computations support rapid sequential decisions", Nature Communications 14, 7573
(doi:10.1038/s41467-023-43250-x), on dandiset 001169, version 0.260825.1909.

- `reproduce_mah_2023.ipynb` streams every session of the dandiset (about ten minutes), checks the data
  against its description, and tests each claim.
- `mah2023.py` holds the loader and the measures, rewritten from the paper's MATLAB code
  (github.com/constantinoplelab/published, rat_behavior, commit b7b68ca8c107); each function says which script
  or passage it follows.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

The record of the attempt is `attempts/mah-2023-01.yaml`.
