# Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019) from CRCNS pvc-12

Tests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)
on [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T), which holds, per V1 neuron and condition, the
spike rate map made by the authors and the stimulus image, for the Square and Edge, Star and Corners
stimuli. The files hold 53 neurons; 60 recordings carry the authors' aligned maps and are analysed
(22 Square and Edge, 12 Star, 26 Corners).

| Claim | Outcome |
|---|---|
| Counts of neurons per condition | Not reproduced |
| Spikes per condition | Blocked: data missing |
| Baselines do not differ across stimuli | Not reproduced (rests on an assumption) |
| Midpoint responses above baseline, growing with sharper corners (Fig 4A) | Reproduced (assumption) |
| Midpoint spike rate differences S40 > S52 > S90 > P180 (Fig 4B) | Partially reproduced (assumption) |
| Pairwise differences of Fig 4B | Reproduced |
| Average maps (Fig 5) | Reproduced (assumption) |
| Table 1, Edge, S90 and S40 | Reproduced (assumption) |
| Table 1, S52 | Partially reproduced (assumption) |
| Table 1, P180 | Not reproduced |
| Midpoint represents the whole fold (Fig 6) | Reproduced |
| RMS contrast along the Edge and its fit (Fig 7A) | Not reproduced |
| Folds equivalent to Edge contrasts (Fig 7C) | Not reproduced |
| Fold against Edge t-tests (Fig 7C) | Reproduced (assumption) |
| Non-linear relation with angle (Fig 7D) | Reproduced (assumption) |
| Similarity to the DOG model (Fig 7D) | Blocked: data missing |
| Peak response near 60 ms latency (S3 Fig) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The main assumptions are that the Corners response is taken at the bright of its two 40 degree
folds, as the Methods say only bright folds were analysed, and where the baseline squares lie,
which the text does not fix. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/martinez-conde-2019-01.yaml`](../../attempts/martinez-conde-2019-01.yaml).

- `reproduce_martinez_conde_2019.ipynb`: the analysis. It takes about five minutes, most of it
  streaming the zip and registering the maps.
- `vasarely.py`: reading the zip in place, the authors' aligned frame, the fold geometry from the
  stimulus polygons, and the midpoint, block and baseline measures. Other notebooks on this data
  set can import it.
