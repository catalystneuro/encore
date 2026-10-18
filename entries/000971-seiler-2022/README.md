# Seiler et al. (2022) from dandiset 000971

Tests the findings of [Seiler et al. (2022)](https://doi.org/10.1016/j.cub.2022.01.055) that can be
tested on [DANDI:000971](https://dandiarchive.org/dandiset/000971/0.261013.1707), which holds the operant
behavior of a fiber photometry cohort (RI60 and RR20 mice) and of three optogenetic cohorts, DMS and DLS
dopamine axon photometry during RI60 and RR20 training, and western blot images. Photometry during RI30
and the shock probes, fear conditioning, open field and histology are not in it.

| Claim | Outcome |
|---|---|
| RI60 mice accept more shocks than RR20 mice | Not reproduced |
| RI60 mice take longer on the omission probe than RR20 mice | Partially reproduced |
| Late shocks and omission time are not correlated | Reproduced |
| The phenotype rule gives 9 PR, 9 DPR and 18 PS mice | Partially reproduced |
| Only DPR mice accept more shocks on the late probe | Reproduced |
| PR and DPR mice nosepoke faster than PS mice | Reproduced |
| PR mice take longer on the omission probe than PS mice | Reproduced |
| PS mice wait longer after a reward | Partially reproduced |
| PS mice make fewer extra nosepokes than PR mice | Partially reproduced |
| PS mice have longer inter-reward intervals | Reproduced |
| PS mice earn fewer rewards per session | Partially reproduced |
| PR mice escalate nosepoking in RI30, DPR mice in RI60 | Partially reproduced |
| RI60 mice earn more rewards than RR20 mice | Reproduced |
| Males accept more shocks than females | Reproduced |
| DMS peak score differs by phenotype | Not reproduced |
| DMS peak score correlates with shocks (r = 0.53) | Partially reproduced |
| DMS peak score does not correlate with omission time | Reproduced |
| DLS peak score does not differ by phenotype | Reproduced |
| DLS peak score does not correlate with shocks | Not reproduced |
| DLS peak score does not correlate with omission time | Reproduced |
| DMS ChR2 mice escalate nosepoking faster | Not reproduced |
| DMS ChR2 mice accept more shocks on the first probe | Not reproduced |
| DMS ChR2 mice are mostly PR | Reproduced |
| All male and about 71% of female ChR2 mice are PR | Partially reproduced |
| DMS stimulation does not change omission time | Reproduced |
| NpHR mice accept fewer shocks on the second probe | Partially reproduced |
| NpHR mice are more often PS | Reproduced |
| DMS inhibition does not change omission time | Reproduced |
| DLS stimulation groups escalate alike | Not reproduced |
| DLS stimulation does not change shocks | Reproduced |
| DLS stimulation groups have similar phenotypes | Reproduced |
| DLS stimulation does not change omission time | Reproduced |
| DAT protein is not reduced in DAT-IRES-cre mice (Zenodo data) | Reproduced |
| NpHR mice drop out of initial learning (dropped mice not deposited) | Blocked: data missing |
| Peaks emerge during RI30; fear conditioning; open field; histology (four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The fiber photometry mice carry their phenotype in the dandiset; the optogenetic mice are classified
here with the rule in the paper's Methods. The attempt record, with the reasons and the differences
from the paper's method, is
[`attempts/000971-seiler-2022-01.yaml`](../../attempts/000971-seiler-2022-01.yaml).

- `reproduce_seiler_2022.ipynb`: the analysis. It takes 15 to 25 minutes, most of it streaming the
  events of about 2200 files and 62 photometry recordings.
- `seiler.py`: listing the sessions, reading events and photometry, the shock probe table and phenotype
  rule, the behavioral measures, and the photometry processing of the authors' code. Other notebooks on
  this dandiset can import it.
