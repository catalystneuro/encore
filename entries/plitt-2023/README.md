# Plitt, Kaganovsky et al. (2023) on dandiset 001710

Tests the claims of Plitt, Kaganovsky, Südhof & Giocomo, "Hippocampal place code plasticity in CA1
requires postsynaptic membrane fusion" (bioRxiv doi:10.1101/2023.11.20.567978), against DANDI:001710
version 0.260213.0329. The claims are in `claims/001710/`; the outcomes in
`attempts/plitt-2023-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

- `reproduce_plitt_2023.ipynb` streams every control and Cre session (about 40 minutes, four
  processes) and tests each claim.
- `stx3.py` loads the files, merges split days, and computes trial maps, shuffled place fields,
  HSEs, decoders and population vector measures.

Every imaging outcome rests on one assumption. The dandiset holds dF/F, not the deconvolved activity
rates the preprint describes, so dF/F is used, as the authors' code for these files does. Three
outcomes also rest on a reading adopted where the paper leaves a detail open: figs3c (the population
vector correlation per bin, as in the authors' code), fig4-block6-activity-increase-pattern (a 150 cm
stem) and fig6e (day 1 fields). The
across-day analyses use the authors' ROI matches from Figshare (doi:10.6084/m9.figshare.31286365.v5).

The claims on highly synchronous events (Fig 7 and S9) are blocked as methods_underspecified. The
HSE detector, read from the Methods, flags more than half as many trials in Cre mice when each
cell's activity is shifted in time to remove synchrony, so it does not pick out synchronous events
here, and the paper does not settle its null.
