# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/eneuro.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.261123.1703) (AJILE12), which holds the
ECoG, pose and wrist movement events of the paper's 12 subjects over 55 days. The ECoG around each
of 8088 events is streamed from the archive, and region power uses the paper's projection matrices
from [Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days are the paper's | Reproduced |
| The Figshare projection matrices match the electrodes | Reproduced |
| Cohort: sex, age, electrodes, hemispheres | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration and magnitude small, angles peak at +-90 | Partially reproduced |
| Bimanual features skewed toward unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations | Partially reproduced |
| Events even across days except S04, S05, S09; mostly waking | Partially reproduced |
| Group LFB decrease and HFB increase at onset | Reproduced |
| Largest changes in sensorimotor regions | Reproduced |
| LFB decreases more widespread than HFB increases | Blocked: methods underspecified |
| Precentral pattern per subject | Partially reproduced |
| Band power differs across subjects | Reproduced |
| Table 1 intervals | Partially reproduced |
| Recording-day effects per subject | Not reproduced |
| Baseline subtraction reduces day variability | Reproduced |
| Day-to-day changes are 1-2 dB | Reproduced |
| Best models over sensorimotor areas | Reproduced |
| R2 at most 0.25 | Reproduced |
| Reach angle and day most informative | Reproduced |
| Reach angle most often retained | Partially reproduced |
| Upward reaches enhance the pattern | Reproduced |
| Angle and day have the largest coefficients | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook runs for about 40 minutes. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/peterson-2021-02.yaml`](../../attempts/peterson-2021-02.yaml).
