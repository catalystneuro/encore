# Asari & Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) on
[CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR), which holds the whole-cell recordings of the A1
neurons tested with natural and synthetic sound sequences, the cell-attached MGB recordings, and the
authors' MATLAB analysis scripts. The voltage-clamp recordings of Figures 5 and 6 are not in it.

| Claim | Outcome |
|---|---|
| Counts of cells and probes | Partially reproduced |
| A1 and MGB firing rates | Not reproduced (assumption: spike detectors) |
| Trial-to-trial reliability (Figure 2) | Reproduced |
| Example of an intermittent, 4-s context effect (Figure 2) | Reproduced |
| 204 of 305 probes significant, a quarter of events after 1 s (Figure 3A) | Partially reproduced |
| Two-exponential decay of the significance curve (Figure 3A) | Partially reproduced (assumption) |
| Normalized context-dependent power decays with 1.04 s (Figure 3B) | Reproduced (assumption) |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| Upper bound on model performance (Figure 4) | Partially reproduced |
| STRF model performance (Figure 4) | Blocked: not run in this attempt |
| Voltage-clamp conductances (Figures 5 and 6) | Blocked: data missing |
| Proportion significant by sound property (Figure 8A) | Partially reproduced (assumption) |
| Decay of normalized power by property (Figure 8B) | Partially reproduced (assumption) |
| Exponential fits of the significance curves by property (Figure 8A) | Not reproduced |
| Relative size of the effects by property (Figure 8C) | Partially reproduced (assumption) |
| Natural and synthetic probes alike | Reproduced (assumption: the test) |
| Fast decay in MGB (Figure 9D) | Reproduced |
| MGB example limited to the first bin (Figure 9B) | Reproduced |
| Example with DMR frequency contexts (Figure 7) | Blocked: data missing |
| Context effects soon after the silence, power fades within 1 s (Supplemental Figure S1) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Details the Methods leave open are taken from the authors' scripts shipped with the data
(`asari/Tools/CxtDep.m` and its helpers). In two cells the fragment lists of a cell's two files
are swapped; the notebook cuts each file's probes with the list that fits its triggers. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/asari-2009-02.yaml`](../../attempts/asari-2009-02.yaml).
