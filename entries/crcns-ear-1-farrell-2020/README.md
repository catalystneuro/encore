# Farrell, Skidmore, Rajasekharan & Brownell (2020) from CRCNS ear-1

Tests the findings of [Farrell et al. (2020)](https://doi.org/10.1085/jgp.201912447) that can be
tested on [CRCNS ear-1](https://doi.org/10.6080/K0571975), which holds the whole-cell voltage-clamp
recordings of 89 guinea pig outer hair cells, one HDF5 file each, with the per-cell values the
authors derived (linear capacitance, charge, V0.5 and voltage sensitivity).

| Claims | Outcome |
|---|---|
| Cohort, example cell, CNLW, CLW by turn, charge growth of Fig. 1, colony and region differences of voltage sensitivity and V0.5 (Tables 1 and 2), the XE991 shift, the Eq. 3a fit without XE991 and the deviation above 0.25 V, the two C_Leq limits, sensor charge | Mostly reproduced (22 reproduced) |
| Counts of Table 1, Fig. 2b fit, voltage clamp with XE991, Fig. S4 fits, capacitance asymmetry, Vh and Vd, Table 3 energies, the overall conclusion | Partially reproduced (10) |
| Eq. 3a fits with XE991 and of Fig. 3b, mean slope of -0.48, the band of Fig. 1, sensor area, the alternative limit, length gradient, equal slopes of the two colonies, low chloride cells | Not reproduced (9) |
| Sequencing and protein model; values from other rodents and other papers | Blocked (7) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set does not store the lateral wall capacitance CLW. After a reader answered the
question in [`questions/crcns-ear-1.yaml`](../../questions/crcns-ear-1.yaml), the claims file
takes CLW = CL - CNLW with CNLW = CSB + root per cell. The stereocilia capacitance CSB is computed
here by the rule of Corbitt et al. (2012), the paper the method cites, on the stored cell area; this
is an assumption, and every outcome on CLW, charge density or C_Leq rests on it. CL - 4.82 pF is
shown for comparison only. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/crcns-ear-1-farrell-2020-01.yaml`](../../attempts/crcns-ear-1-farrell-2020-01.yaml).

- `reproduce_farrell_2020.ipynb`: the analysis. It takes under a minute, most of it streaming the
  zip.
- `ear1.py`: streaming the zip, loading the 89 HDF5 files and the original MATLAB files, the
  derived per-cell quantities, and the fits. Other notebooks on this data set can import it.
