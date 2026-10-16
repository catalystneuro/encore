# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds the
long-term ECoG, upper-body pose and wrist movement events of 12 subjects during clinical epilepsy
monitoring.

| Claim | Outcome |
|---|---|
| 12 subjects, 3 to 5 days each, five implanted on the right | Reproduced |
| Sex and age of the subjects | Blocked: data missing |
| Surface and depth electrode counts | Partially reproduced |
| Electrodes removed as bad | Partially reproduced |
| 151 to 947 events per subject, median 640 | Partially reproduced |
| All ten features differ across subjects | Reproduced |
| Subjects 04, 05 and 09 have one dominant day | Reproduced |
| Most reaches last under 2 s and cover under 200 px | Reproduced |
| Reach angles bimodal at +/-90 degrees | Not reproduced |
| Correlations between features | Partially reproduced |
| Bimanual features skewed toward unimanual | Reproduced |
| The paper's projection matrices link to the electrodes | Reproduced |
| LFB decrease and HFB increase, largest in sensorimotor regions | Reproduced |
| Precentral power per subject (Table 1) | Reproduced |
| Precentral power differs across subjects | Reproduced |
| Recording-day effects per subject (Table 2) | Reproduced |
| Baseline subtraction reduces variability across days | Reproduced |
| Regression R2 at most 0.25 | Reproduced |
| Best regression models in sensorimotor areas | Reproduced |
| Reach angle and day are the most explanatory features | Reproduced |
| Upward reaches enhance the power pattern | Reproduced |
| Reach angle most often retained | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The regional analyses use the paper's projection matrices from Figshare
(doi:10.6084/m9.figshare.12114408.v1), which the dandiset does not hold. In three files the ECoG
and the event table are on different clocks; the notebook shows this and corrects the event times.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).

- `reproduce_peterson_2021.ipynb`: the analysis. It takes about ten minutes, most of it streaming
  ECoG windows around 8088 events.
- `ajile.py`: loading the files, the reach features, a direct reader of the ECoG chunk index with
  parallel range requests, Morlet power with the paper's parameters, the projection onto regions,
  and the regression of the paper's code. Other notebooks on this dandiset can import it.
