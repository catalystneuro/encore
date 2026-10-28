# Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018) from OpenNeuro ds000228

Tests the findings of [Richardson et al. (2018)](https://doi.org/10.1038/s41467-018-03399-2) on
[OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot 1.1.1,
which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults, with the paper's own
preprocessed images, artifact and CompCor regressors, group ROIs and behavioural scores.

| Claims | Outcome |
|---|---|
| Sample, behaviour and motion (11 claims) | Reproduced |
| Inter-region correlations (15 claims) | 7 partially reproduced, 8 not reproduced |
| Reverse correlation (8 claims) | 1 reproduced, 4 partially reproduced, 3 not reproduced |
| Functional maturity (4 claims) | 3 reproduced, 1 partially reproduced |
| Face regions (2 claims) | 1 reproduced, 1 not reproduced |
| Replication sample and hand-coded events (2 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every behavioural number of the paper is recovered from participants.tsv. With the deposited
preprocessed data and the pipeline of the Methods, the inter-region correlations are higher within
networks and less negative across them than the paper reports, and several event-level and
false-belief results do not come out as reported. Five outcomes rest on readings of a method the
paper leaves open. The attempt record, with the reasons and the differences from the paper's
method, is
[`attempts/openneuro-ds000228-richardson-2018-01.yaml`](../../attempts/openneuro-ds000228-richardson-2018-01.yaml).

- `reproduce_richardson_2018.ipynb`: the analysis. It takes about three minutes, most of it
  streaming the 155 preprocessed images (14 GB).
- `social_brain.py`: loading from the pinned snapshot, ROI extraction, the timecourse cleaning
  of the Methods, inter-region correlation, reverse correlation and the statistics. Other
  notebooks on this dataset can import it.
