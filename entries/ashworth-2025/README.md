# ashworth-2025

Reproduction of Ashworth, Martenson, Shi, De Preter, Heinricher and Mancini, "Multi-timescale dynamics
organize descending pain modulation" (bioRxiv doi:10.64898/2025.12.15.693905), on DANDI:001708
version 0.260604.1023, the version the paper cites.

- `evoked.ipynb`: the dataset's composition, trial counts, and the piecewise Bayesian models (PyMC) of
  the evoked ON and OFF responses, their timing, and the withdrawal latency and heart rate.
- `ongoing.ipynb`: the ongoing segments, spike-train spectra, CV and ISI, the periodic GP period scan,
  and the coherence with heart rate.
- `gp.ipynb`: the generalized Poisson periodic Gaussian-process fits and their tests (Figure 5, Table 1,
  Figure S2), with the code's settings, compared cell by cell with the code's stored fits.
- `gp_methods.ipynb`: the same fits with the Methods' 200 inducing points and p_noise 0.001, a variant.
- `rvm.py`: loading (streamed with remfile and h5py), trial rules, models and measures, with the source
  of each parameter.

The claims are in `claims/001708/`, the outcomes in `attempts/ashworth-2025-01.yaml`.
A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

Run with `python tools/entry.py all entries/ashworth-2025` (about two hours on 4 cores: in the last
execution 31.8 min for evoked.ipynb, 27.1 for ongoing.ipynb, 36.7 for gp.ipynb and 25.6 for gp_methods.ipynb).
The PyMC fits repeat exactly on one machine at the fixed seeds, but their draws differ between machines, so the
model numbers can move in the third digit, and the convergence of a few fits can change, on another machine.
