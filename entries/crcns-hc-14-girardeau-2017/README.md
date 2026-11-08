# Girardeau, Inema & Buzsaki (2017) from CRCNS hc-14

Tests the findings of [Girardeau et al. (2017)](https://doi.org/10.1038/nn.4637) on
[CRCNS hc-14](https://doi.org/10.6080/K0MS3QXD), which holds the sorted spikes, head positions and
events of the paper's 4 rats (61 sessions, with 4 more not in the paper) and a set of undocumented summary
tables computed by the authors. The hand-scored sleep states are not in it.

| Claim | Outcome |
|---|---|
| Units recorded per rat and structure | Partially reproduced |
| Danger zone speeds, two-way ANOVA and post hoc tests | Partially reproduced (assumption) |
| Speed ratio reversal, overall and per rat; slowing before the air puff; habituation | Reproduced |
| Air puff location does not bias danger zone speed | Not reproduced (assumption) |
| BLA firing rates in REM, NREM and wake (Figure 2c, three claims) | Reproduced (assumption on the REM column for two) |
| Hippocampus-BLA reactivation in NREM, absent in REM | Reproduced |
| Ripple modulation of BLA cells, pair groups, contributions, Figure 7 (ten claims) | Reproduced |
| Rates on safe and air puff laps do not differ | Reproduced (assumption) |
| Reactivation decay over the first hour of NREM | Not reproduced (substitute NREM) |
| Decay and REM with all cells | Partially reproduced (substitute NREM) |
| Piriform weaker than BLA | Not reproduced (substitute NREM) |
| Within-structure NREM reactivation; ripple rate pre against post | Reproduced (substitute NREM) |
| Reactivation strength around ripples (six claims) | 4 reproduced, 2 not reproduced (substitute NREM) |
| Piriform and CeN reactivation with REM; within-structure REM (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Claims on hippocampus-BLA pairs, state firing rates and ripple modulation use the authors' summary
tables, after checking them against the raw spikes. Claims that need NREM elsewhere use a substitute
NREM made from head immobility in the home cage, an assumption of this attempt. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-hc-14-girardeau-2017-01.yaml`](../../attempts/crcns-hc-14-girardeau-2017-01.yaml).

- `reproduce_girardeau_2017.ipynb`: the analysis. It takes about 18 minutes, 11 of them streaming the
  61 session archives (tar.gz, 1 to 2.5 GB each) from the CRCNS bucket.
- `hc14.py`: streaming the tar.gz archives, reading the summary tables and sessions, the danger zone and
  lap measures, EV and REV, the substitute NREM and the reactivation strength. Other notebooks on this
  data set can import it.
