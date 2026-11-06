# Farrell, Skidmore, Rajasekharan & Brownell (2020) from CRCNS ear-1

Tests the findings of [Farrell et al. (2020)](https://doi.org/10.1085/jgp.201912447) that can be
tested on [CRCNS ear-1](https://doi.org/10.6080/K0571975), which holds the whole-cell voltage-clamp
recordings of 89 guinea pig outer hair cells, one HDF5 file each, with the per-cell values the
authors derived (linear capacitance, charge, V0.5 and voltage sensitivity).

| Claims | Outcome |
|---|---|
| Cohort, example cell, CLW by turn, colony and region differences of voltage sensitivity and V0.5 (Tables 1 and 2), the XE991 shift, sensor charge and Table 3 energies | Mostly reproduced (19 reproduced) |
| Steeper charge growth in small cells, counts of Table 1, Fig. 2b fit, voltage clamp with XE991, capacitance asymmetry, Vh and Vd, the overall conclusion | Partially reproduced (9) |
| CNLW of 4.82 pF, Eq. 3a fits (Fig. 3a, 3b, S4), mean slope of -0.48, the two C_Leq limits and sensor area, the alternative limit, length gradient, equal slopes of the two colonies, low chloride cells | Not reproduced (13) |
| Sequencing and protein model; values from other rodents and other papers | Blocked (7) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set does not store the lateral wall capacitance CLW. The claims file takes it as CL - 4.82
pF, while the paper's example cell implies 5.89 pF. Under the second value the Eq. 3a fit without
XE991 matches the paper, so several outcomes turn on this one quantity; it is asked of a reader in
[`questions/crcns-ear-1.yaml`](../../questions/crcns-ear-1.yaml). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/crcns-ear-1-farrell-2020-01.yaml`](../../attempts/crcns-ear-1-farrell-2020-01.yaml).

- `reproduce_farrell_2020.ipynb`: the analysis. It takes under a minute, most of it streaming the
  zip.
- `ear1.py`: streaming the zip, loading the 89 HDF5 files and the original MATLAB files, the
  derived per-cell quantities, and the fits. Other notebooks on this data set can import it.
