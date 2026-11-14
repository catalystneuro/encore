# Gao et al. (2018) from DANDI:000007 and CRCNS:alm-4

Tests the findings of [Gao et al. (2018)](https://doi.org/10.1038/s41586-018-0633-x) that can be
tested on its two deposits, [DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903)
and [CRCNS:alm-4](https://doi.org/10.6080/K0NS0S26). Both hold the same 54 sessions of ALM
recording in 13 mice: 34 during fastigial or dentate photo-activation and 20 during CN
photo-inhibition. The lesion experiments, behavior-only sessions, CN recordings, lick times,
VGAT-ChR2 experiments and anatomy are in neither, so 24 of the 46 claims are blocked.

| Claim | Outcome |
|---|---|
| Behavior in the recording sessions (Fig. 1g, 1h, 1k; Extended Data Fig. 10b), six claims | Reproduced |
| Most ALM pyramidal neurons are selective (Fig. 2) | Reproduced |
| Preparatory activity in 59% of ALM neurons | Reproduced (ALM only) |
| Peri-movement activity, ALM and CN | Partially reproduced (ALM only) |
| Selectivity emerges gradually (Fig. 2c, d) | Partially reproduced (ALM only) |
| CN photo-inhibition alters many ALM neurons, 7.1 ms latency | Partially reproduced |
| Mean ALM rate unchanged by CN photo-inhibition | Reproduced |
| Increase against decrease among modulated ALM neurons | Reproduced, on an assumption |
| CN photo-inhibition abolishes ALM selectivity | Partially reproduced |
| Fastigial photo-activation changes ALM within 4.5 ms | Partially reproduced |
| Fastigial photo-activation abolishes ALM selectivity | Reproduced |
| The fastigial effect persists for more than 1 s | Reproduced |
| Dentate effect recovers quickly | Partially reproduced |
| Control trajectories separate along the coding direction | Reproduced |
| Fastigial, not dentate, photo-activation collapses the trajectories | Partially reproduced |
| The coding direction captures 64.1% of selectivity and 27.0% of variance | Reproduced, on an assumption |
| After fastigial photo-activation the projection no longer predicts licking | Not reproduced |
| Lesions, CN recordings, licking, VGAT-ChR2 and anatomy (24 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The two deposits have identical spike times; the analysis reads the CRCNS copy, which keeps every
trial and the laser traces, and checks DANDI against it. Method details the paper leaves open are
taken from the analysis scripts deposited with CRCNS:alm-4. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/gao-2018-02.yaml`](../../attempts/gao-2018-02.yaml).

- `reproduce_gao_2018.ipynb`: the analysis. It takes about 25 minutes, most of it reading the two
  CRCNS archives (12.8 GB of gzip, read once each as a stream).
- `gao2018.py`: loading both deposits, the trial selection of the deposited scripts, and the
  measures (selectivity, photostimulation tests, latency, hierarchical bootstrap, coding
  direction).
