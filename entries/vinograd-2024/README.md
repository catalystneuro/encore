# Vinograd, Nair et al. (2024) on dandiset 001037

Tests the findings of "Causal evidence of a line attractor encoding an affective state" (Nature 634,
910-918, doi:10.1038/s41586-024-07915-x) on DANDI:001037 version 0.260609.1402.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `stored_weights_and_stimulation.ipynb`: the claims that use the stored two-photon factor weights and
  the group photostimulation sessions, the data check of the two-photon files, and the table of all
  claims.
- `rslds_fits.ipynb`: rSLDS fits (ssm, the authors' sample-code settings) to the miniscope and
  two-photon sessions, and the claims that rest on them.
- `cross_validation.ipynb`: fivefold cross-validation, for the paper's cvR2 and the number of states.
- `network_model.ipynb`: the network time constants of the excitatory model of Figure 4.
- `linattr.py`: loading, projections, measures and fitting; each parameter says where it comes from.

The rSLDS library ssm cannot be built in an isolated build environment, so the notebooks install it
at a pinned commit (`linattr.ensure_ssm`) against the locked numpy and Cython. The cross-validation
notebook runs 255 fits and takes about 40 minutes on four cores.
