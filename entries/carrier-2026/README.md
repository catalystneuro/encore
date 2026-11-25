# Carrier et al. (2026) from Zenodo records 17624449 and 17794764

Tests the findings of [Carrier et al. (2026)](https://doi.org/10.1152/jn.00294.2025) on the two
Zenodo records the authors deposited for the paper,
[17624449](https://zenodo.org/records/17624449) (Part I) and
[17794764](https://zenodo.org/records/17794764) (Part II). The isolated nervous system claims are
tested on the authors' per-preparation tables and Prism files, which hold the PD burst frequency
at every temperature step, the crash temperatures and the phases; the in vivo claim on the raw PPG
recordings.

| Claim | Outcome |
|---|---|
| Crab pyloric frequency unchanged in 0.75x and 1.25x saline (Fig. 1B, 1D) | Reproduced |
| Crab crash fractions across salinities (Fig. 1E) | Blocked: too large |
| Crab crash temperature unchanged in 0.75x, lower in 1.25x (Fig. 2B, 2E) | Reproduced |
| Crab Q10 unchanged by salinity, frequency rises in 1.25x (Fig. 2F to 2H) | Reproduced |
| Crab mixed-effects model (Fig. 2F legend) | Partially reproduced |
| Crab neuron crash counts (Fig. 2I to 2K) | Not reproduced |
| Crab neuron crash temperatures similar (Fig. 2I to 2K) | Reproduced |
| Lobster Q10 1.43, species frequency at 10 C, lobster phases (Fig. 3) | Reproduced |
| Lobster salinity series (Fig. 4, three claims) | Blocked: data missing |
| Lobster LP before PY, neuron crash by salinity (Fig. 5B, 6A, 6B) | Blocked: too large |
| Lobster mixed-effects model (Fig. 5C) | Partially reproduced |
| Lobster Q10 unchanged by salinity (Fig. 5D) | Not reproduced |
| Species Q10 at 0.75x, 1x and 1.25x (Fig. 7A to 7C) | Reproduced |
| Species crash temperature in 1x (Fig. 7E) | Not reproduced |
| Species crash temperature in 0.75x and 1.25x (Fig. 7D, 7F) | Reproduced |
| In vivo rhythm kept in every salinity (Fig. 8) | Reproduced, resting on an assumption |
| 15-h mortality (Fig. 9) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons, the differences from the paper's method and what was found
about the data, is [`attempts/carrier-2026-01.yaml`](../../attempts/carrier-2026-01.yaml).

- `reproduce_carrier_2026.ipynb`: the analysis. It takes about six minutes, most of it reading the
  in vivo recordings.
- `stns.py`: reading the records' files, the Prism files and the authors' tables, the semi-log Q10
  fits and their F tests, and the in vivo spectra. Other notebooks on these records can import it.
