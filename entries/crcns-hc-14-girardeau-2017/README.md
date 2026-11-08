# Girardeau, Inema & Buzsaki (2017) from CRCNS hc-14

Tests the findings of [Girardeau et al. (2017)](https://doi.org/10.1038/nn.4637) on
[CRCNS hc-14](https://doi.org/10.6080/K0MS3QXD), which holds the sorted spikes, head positions and
events of the paper's 4 rats (61 sessions, with 4 more not in the paper) and a set of undocumented summary
tables computed by the authors. The hand-scored sleep states are not in it.

| Claim | Outcome |
|---|---|
| Units recorded per rat and structure | Reproduced |
| Danger zone speeds, two-way ANOVA and post hoc tests | Partially reproduced (assumption) |
| Speed ratio reversal, overall and per rat; slowing before the air puff | Reproduced (assumption) |
| Habituation | Reproduced |
| Air puff location does not bias danger zone speed | Not reproduced (assumption) |
| BLA firing rates in REM, NREM and wake (Figure 2c, three claims) | Reproduced (assumption on the REM column for two) |
| Hippocampus-BLA reactivation in NREM, absent in REM | Reproduced |
| Ripple modulation of BLA cells, pair groups, contributions, Figure 7 (ten claims) | Reproduced |
| Rates on safe and air puff laps do not differ | Reproduced |
| Reactivation decay over the first hour of NREM; decay and REM with all cells | Reproduced (decoded NREM) |
| Piriform reactivation and piriform weaker than BLA; no CeN reactivation | Reproduced (decoded NREM and REM) |
| Within-structure reactivation in NREM, absent in REM; ripple rate pre against post | Reproduced (decoded NREM and REM) |
| Reactivation strength around ripples (six claims) | Reproduced (decoded NREM) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Claims on hippocampus-BLA pairs, state firing rates and ripple modulation use the authors' summary
tables, after checking them against the raw spikes. Claims that need NREM or REM elsewhere use sleep
states decoded from the authors' per-state firing rates (StatesFR) in immobile epochs of the home cage
sleep, an assumption of this attempt checked against the authors' NREM and REM pair correlations.
Several of these outcomes sit near p = 0.05 and change with the decoder's settings. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-hc-14-girardeau-2017-01.yaml`](../../attempts/crcns-hc-14-girardeau-2017-01.yaml).

- `reproduce_girardeau_2017.ipynb`: the analysis. It takes about 30 minutes, 12 of them streaming the
  61 session archives (tar.gz, 1 to 2.5 GB each) from the CRCNS bucket.
- `hc14.py`: streaming the tar.gz archives, reading the summary tables and sessions, the danger zone and
  lap measures, EV and REV, the decoded sleep states and the reactivation strength. Other notebooks on this
  data set can import it.
