# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds the
ECoG, upper-body pose and wrist movement events of the paper's 12 subjects over 55 days.

| Claim | Outcome |
|---|---|
| The dataset's subjects and days are the paper's (link) | Reproduced |
| The Figshare false-positive flags and projection matrices match the dataset (two links) | Reproduced |
| Cohort: subjects, electrodes, hemispheres | Partially reproduced |
| 151 to 947 events per subject, median 640 | Reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration and magnitude; bimodal reach angle | Partially reproduced |
| Bimanual features skewed to unimanual | Blocked: methods underspecified |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Correlations between features | Reproduced |
| Days with most events; waking hours | Partially reproduced |
| Group LFB decrease and HFB increase at movement onset | Reproduced |
| Changes largest in sensorimotor regions | Reproduced |
| LFB decreases more widespread than HFB increases | Reproduced |
| Precentral spectra vary across subjects | Partially reproduced |
| Precentral band power differs across subjects | Reproduced |
| Per-subject band power in the Table 1 intervals | Partially reproduced |
| Recording-day effects on band power | Partially reproduced |
| Baseline subtraction reduces day-to-day variability | Reproduced |
| Day-to-day changes are 1-2 dB | Blocked: methods underspecified |
| Withheld R2 at most 0.25 | Reproduced |
| Best models at sensorimotor electrodes | Reproduced |
| Reach angle and day most informative | Reproduced |
| Reach angle most often retained by forward selection | Not reproduced |
| Upward reaches enhance the movement response | Reproduced |
| Reach angle and day have the largest coefficients | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset does not mark the 1157 events the paper treated as false positives; their flags are
read from the paper's Figshare epoch files, linked by timestamp. The regions use the paper's own
projection matrices from Figshare. In three files the ECoG starts at the session start while the
events count from midnight, which the files do not say; the notebook shows it and reads those
files on the shifted clock. How the paper rejected segments on their power spectral density is
not specified; three readings are run and a question is open. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).

- `reproduce_peterson_2021.ipynb`: the data check, the link claims, the behaviour claims and the
  spectral claims. About 17 minutes, most of it streaming about 170 GB of ECoG around the events.
- `reproduce_peterson_2021_regression.ipynb`: the regression claims of Figure 6. About 27
  minutes: it streams the ECoG again and fits 2368 models of 200 splits each.
- `ajile.py`: loading the files and the Figshare inputs, the spectral measures, the segment
  rejection, the region projection and the regression. Other notebooks on this dandiset can
  import it.
