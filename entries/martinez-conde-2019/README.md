# Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019) from CRCNS pvc-12

Tests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)
on [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T), which holds, for 53 V1 neurons of two
monkeys, the spike rate maps the authors made at their 60 ms latency and the stimuli (Square and
Edge, Star, Corners). The analysis uses the maps the authors registered to the stimulus, which
exist for 22 Square and Edge, 12 Star and 26 Corners neurons.

| Claim | Outcome |
|---|---|
| Neuron counts (58 analysed; 25, 30 and 28 per condition) | Not reproduced |
| Spikes per condition | Blocked: data missing |
| No difference in baseline across stimuli (S4 Fig) | Not reproduced |
| Midpoint responses above baseline, ordered by fold angle (Fig 4A) | Reproduced |
| Midpoint spike rate differences S40 > S52 > S90 > P180 (Fig 4B) | Reproduced |
| Pairwise tests of Fig 4B | Reproduced |
| Average maps (Fig 5) | Reproduced |
| Table 1, S40 | Reproduced |
| Table 1, Edge, P180, S90 and S52 | Partially reproduced |
| Midpoint represents the whole fold (Fig 6) | Reproduced |
| RMS contrast along the Edge and its fit (Fig 7A) | Not reproduced |
| P180 like a 50% Edge, S40 like a 90% Edge (Fig 7C) | Not reproduced |
| Tests of folds against the Edge (S2 Table) | Reproduced |
| Non-linear relation with fold angle (Fig 7D) | Reproduced |
| Similarity to the DOG model (Fig 7D) | Blocked: data missing |
| Latency peak near 60 ms (S3 Fig) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most outcomes rest on an assumption about where the baseline squares sit, which the paper shows
only in its Fig 2. For each stimulus, the placement used is the one closest to the baselines the
authors stored in the files. The notebook shows every placement. The data set holds fewer neurons
than the paper analysed. Its maps are rates, not the raw spike counts its descriptor states. Two
files in its Star folder hold Corners recordings. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/martinez-conde-2019-02.yaml`](../../attempts/martinez-conde-2019-02.yaml).

- `reproduce_martinez_conde_2019.ipynb`: the analysis. It takes about a minute, most of it
  streaming the zip.
- `pvc12.py`: loading the files, the registration check, the fold geometry in the authors'
  ROI frames, and the measures (baselines, midpoints, blocks, Edge responses).
