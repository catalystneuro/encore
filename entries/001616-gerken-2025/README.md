# Gerken, Darcher et al. (2025) from dandiset 001616

Tests the findings of [Gerken, Darcher et al. (2025)](https://doi.org/10.7554/eLife.106758.1), eLife
reviewed preprint 106758, on [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824)
(SUMMER), which holds 2286 units recorded in the medial temporal lobe of 29 patients while they
watched "500 Days of Summer", with 53 frame-wise annotations of the film.

| Claim | Outcome |
|---|---|
| 2286 units from 29 patients, with the paper's counts per region | Partially reproduced |
| Units responsive to feature onsets (Figure 2, Table S1; six claims) | Blocked: methods underspecified |
| Single units thresholded do not decode Summer | Reproduced |
| Logistic regression decodes characters and location (Summer 0.28, Indoor/Outdoor 0.31) | Reproduced |
| Logistic regression is weaker for scene and camera cuts | Reproduced |
| Without temporal gaps decoding is almost perfect | Reproduced |
| No single patient matches the pooled decoder | Reproduced |
| The patients the paper names decode above 0.2 | Reproduced |
| Decoding by region (amygdala for Summer, PHC for Indoor/Outdoor) | Partially reproduced |
| Responsive units drive decoding of cuts, not of Summer | Blocked: methods underspecified |
| 78 units shared by the top 500 of five rankings | Partially reproduced |
| LSTM results (Figures 3c, 3d, 5b, 7a; four claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The responsive-unit test of the Methods, as written, counts about 70% of units responsive even at
random event times on this data, so the claims that rest on it could not be judged. The paper's
LSTM is not published; its logistic regression is run instead where the paper uses it, and as a
stand-in in three claims. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001616-gerken-2025-01.yaml`](../../attempts/001616-gerken-2025-01.yaml).

- `reproduce_gerken_2025.ipynb`: the analysis. It takes about 22 minutes on four cores.
- `summer.py`: loading the files, the time base through the watchlogs, the responsive-unit and
  cluster tests, the fold layout of the dataset's code and the logistic regression. Other notebooks
  on this dandiset can import it.
