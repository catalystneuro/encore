# 001708-ashworth-2025

Reproduction of Ashworth, Martenson, Shi, De Preter, Heinricher and Mancini, "Multi-timescale dynamics
organize descending pain modulation" (bioRxiv doi:10.64898/2025.12.15.693905), on DANDI:001708
version 0.260604.1023, the version the paper cites.

- `evoked.ipynb`: the dataset's composition, trial counts, and the piecewise Bayesian models (PyMC) of
  the evoked ON and OFF responses, their timing, and the withdrawal latency and heart rate.
- `ongoing.ipynb`: the ongoing segments, spike-train spectra, CV and ISI, the periodic GP period scan,
  and the coherence with heart rate.
- `gp.ipynb`: the generalized Poisson periodic Gaussian-process fits and their tests (Figure 5, Table 1,
  Figure S2).
- `rvm.py`: loading (streamed with remfile and h5py), trial rules, models and measures, with the source
  of each parameter.

The claims are in `claims/001708/`, the outcomes in `attempts/001708-ashworth-2025-01.yaml`.
A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

Run with `python tools/entry.py all entries/001708-ashworth-2025` (about 65 minutes on 4 cores, most of
it in the Gaussian-process and period-scan cells).
