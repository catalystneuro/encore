# Farrell, Skidmore, Rajasekharan & Brownell (2020) from CRCNS ear-1

Tests the findings of [Farrell et al. (2020)](https://doi.org/10.1085/jgp.201912447) that can be
tested on [CRCNS ear-1](https://doi.org/10.6080/K0571975), which holds the whole-cell voltage-clamp
recordings of 89 guinea pig outer hair cells, one HDF5 file each, with the per-cell values the
authors derived (linear capacitance, charge, V0.5 and voltage sensitivity).

| Claims | Outcome |
|---|---|
| Cohort, example cell, CNLW, CLW by turn, charge growth of Fig. 1, colony and region differences of voltage sensitivity and V0.5 (Tables 1 and 2), the XE991 shift, the Eq. 3a fits with and without XE991 and the deviation above 0.25 V, sensor charge, Table 3 energies | Mostly reproduced (23 reproduced) |
| Table 1 with XE991 (cell counts) and without XE991 (p = 0.0010, not < 0.0001), the XE991 effect of Table 1 (cell counts), Fig. 2b fit, Fig. S4 fits, low chloride cells, the overall conclusion | Partially reproduced (7) |
| Eq. 3a fit of Fig. 3b, mean slope of -0.48, the band of Fig. 1, voltage clamp with XE991, capacitance asymmetry, Vh and Vd, the two C_Leq limits, sensor area, the alternative limit, length gradient, equal slopes of the two colonies | Not reproduced (11) |
| Sequencing and protein model; values from other rodents and other papers | Blocked (7) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set does not store the lateral wall capacitance CLW. After a reader answered the
question in [`questions/crcns-ear-1.yaml`](../../questions/crcns-ear-1.yaml), the claims file
takes CLW = CL - CNLW with CNLW = CSB + root per cell. The stereocilia capacitance CSB is computed
here by the rule of Corbitt et al. (2012), the paper the method cites, on the stored cell area; this
is an assumption, and every outcome on CLW, charge density or C_Leq rests on it. CL - 4.82 pF is
shown for comparison only. Bins and groups whose mean charge density is outside (0, 0.4] V are left
out of the Eq. 3a fits and the groups built on them (an assumption taken from the Fig. S4 legend;
all bins are shown as a variant). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/farrell-2020-01.yaml`](../../attempts/farrell-2020-01.yaml).

- `reproduce_farrell_2020.ipynb`: the analysis. It takes under a minute, most of it streaming the
  zip.
- `ear1.py`: streaming the zip, loading the 89 HDF5 files and the original MATLAB files, the
  derived per-cell quantities, and the fits. Other notebooks on this data set can import it.
