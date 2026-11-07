# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds 55 days
of ECoG and pose from 12 people in clinical epilepsy monitoring, with their wrist movement events and
event features. Region power uses the paper's projection matrices from
[Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days match Table 2 (link) | Reproduced |
| The Figshare projection matrices match the dataset's electrodes (link) | Reproduced |
| Cohort and electrode counts | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration, magnitude and bimodal angle | Partially reproduced |
| Bimanual features skewed to unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations (Extended Data Figure 2-2) | Partially reproduced |
| Events by day and in waking hours | Partially reproduced |
| Group LFB decrease and HFB increase (Figure 3) | Reproduced |
| Largest changes in sensorimotor regions | Reproduced |
| LFB decreases more widespread than HFB increases | Blocked: methods underspecified |
| Per-subject precentral spectra (Figure 4) | Reproduced |
| Band power differs across subjects (Figure 5) | Reproduced |
| Per-subject band power in Table 1 intervals | Partially reproduced |
| Band power differs across days (Figure 5, Table 2) | Reproduced |
| Baseline subtraction reduces day variability | Reproduced |
| Day changes small next to absolute power | Reproduced |
| All regression R2 at most 0.25 | Reproduced |
| Best models over frontoparietal sensorimotor areas | Reproduced |
| Reach angle and day most informative (Delta R2) | Reproduced |
| Reach angle most often retained, then four features in order | Partially reproduced |
| Upward reaches enhance the movement pattern | Reproduced |
| Reach angle and day have the largest coefficients | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In three files the ECoG starts after midnight but is stored with a start time of 0; `ajile.py`
shifts it (`ecog_offset`). The files hold 8088 events with no false positives marked, more than the
paper analysed; all are kept, in the behavioural and in the ECoG analyses. The notebook reads about 8000 ECoG segments and takes 30 to 45 minutes; the regression models of
Figure 6 take a few minutes, as `ajile.huber_fit` solves many Huber fits at once. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).
