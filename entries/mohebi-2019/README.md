# Mohebi et al. (2019) from CRCNS vta-2

Tests the findings of [Mohebi et al. (2019)](https://doi.org/10.1038/s41586-019-1235-y) that can be
tested on CRCNS data set [vta-2](https://doi.org/10.6080/K0VQ30V9), which holds the spike times of
the 29 optogenetically identified VTA-l dopamine cells, with their bandit, Pavlovian, laser and
sleep segments. The paper's microdialysis, photometry, histology, in vitro imaging and untagged VTA
units are not in it, so the 20 claims on those data are blocked.

| Claim | Outcome |
|---|---|
| Latency scales inversely with reward rate | Reproduced |
| 27 tagged VTA-l dopamine cells plus 2 retrogradely tagged | Partially reproduced |
| Dopamine cell firing rates, mean 7.7 Hz, range 3.7 to 12.9 Hz | Reproduced |
| Pavlovian click responses fall as clicks become predictable | Partially reproduced |
| Pavlovian cue responses follow reward probability | Partially reproduced |
| Food-port entry is highest during the 75% cue | Reproduced |
| No cell changes tonic firing between high- and low-reward blocks | Partially reproduced |
| Burst rate does not change between blocks | Reproduced |
| Time spent inactive is very low and does not change | Reproduced |
| The retrogradely tagged cells resemble the others | Reproduced (assumed test) |
| Light-On, Go cue and reward responses in the great majority of cells | Partially reproduced |
| No firing ramp before Center-In or Food-Port-In | Reproduced |
| All 25 Light-On responsive cells are better aligned to Light-On | Not reproduced |
| Early-trial firing does not depend on reward rate | Not reproduced |
| Reward response is stronger at lower reward rate | Reproduced |
| Negative RPE coding is weak; pause coding in 2 of 29 cells | Partially reproduced |
| The same holds with other estimates of reward expectation | Partially reproduced |
| Microdialysis, photometry, in vitro, histology and untagged units (20 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/mohebi-2019-01.yaml`](../../attempts/mohebi-2019-01.yaml).

- `reproduce_mohebi_2019.ipynb`: the analysis. It takes about five minutes; it streams the 25 MB
  zip from the CRCNS bucket and reads the MATLAB file in memory.
- `vta.py`: loading the data set (MATLAB 7.3 read with h5py), the bandit trials, the leaky-integrator
  reward rate, spike density functions, the shuffle test for cue responses, bursts, block splits and
  SALT. Other notebooks on this data set can import it.
- `vta_measures.py`: the per-unit measures the claims use.
