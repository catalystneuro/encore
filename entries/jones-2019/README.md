# Jones, Gillespie, Yoon, Frank & Huang (2019) from CRCNS hc-26

Tests the findings of [Jones et al. (2019)](https://doi.org/10.1016/j.celrep.2019.10.056) on
[CRCNS hc-26](https://doi.org/10.6080/K0D798NB): home-cage LFP of female apoE3-KI and apoE4-KI mice
(a screen cohort at 12-18 months, a replication cohort at 5-8, 9-11 and 13-17 months) and their
water maze, active place avoidance and control behavior. Sharp-wave ripples and their slow gamma
power are computed from the 108 GB of LFP with the paper's filters and rules.

The genotype differences reproduce: fewer SWRs and lower SWR-associated slow gamma power in aged
apoE4-KI mice, the water maze and place avoidance deficits, the decrease of the SWR-band baseline
with age. The correlations between SWR measures and later behavior reproduce in part in the screen
cohort (weaker than printed) and not in the replication cohort, where the deposited site labels
give fewer mice with CA3 sites than the paper and three young apoE4-KI mice are missing.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with every outcome, the differences from the paper's method and what was found
about the data set, is [`attempts/jones-2019-01.yaml`](../../attempts/jones-2019-01.yaml).

- `reproduce_jones_2019.ipynb`: the analysis. It takes about 45 minutes, most of it streaming and
  reducing the nine LFP archives (four at a time).
- `swr.py`: streaming the LFP archives and reducing each session to SWR events, slow gamma power
  and MUA counts, with the source of every parameter.
- `behavior.py`: the behavior spreadsheets and APA tracking, and the link between behavior IDs and
  recorded mice.
- `stats.py`: the paper's tests (Pearson as F, Holm-Sidak, aligned rank transform ANOVA,
  performance scores, predicted scores, leave-one-out).
- `analysis.py`: per-mouse tables and the behavior metrics.
