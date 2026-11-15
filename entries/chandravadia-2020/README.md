# Chandravadia et al. (2020) from dandiset 000004

Tests the findings of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data
descriptor of human single-neuron recordings during a new/old recognition memory task, on
[DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852) (version 0.220126.1852). The
dandiset holds 87 sessions of 59 patients with 1864 units in the amygdala and hippocampus.

| Claim | Outcome |
|---|---|
| 1863 neurons from 59 subjects | Reproduced |
| 87 sessions, as in Online-only Table 1 | Reproduced |
| Age and sex of each subject as in Online-only Table 1 | Partially reproduced |
| 100 encoding and 100 recognition trials per session, 5 categories | Partially reproduced |
| new_old_labels_recog is 0 for old and 1 for new stimuli | Not reproduced |
| TTL event codes of Table 1 | Partially reproduced |
| Experiment ids of Table 2 | Partially reproduced |
| Session dates set to the first of the month | Partially reproduced |
| Units table columns and quality metrics | Partially reproduced |
| Electrodes table with location, coordinates, impedance, filter, channel | Not reproduced |
| Fewer than 3% of interspike intervals below 3 ms | Partially reproduced |
| All neurons in amygdala or hippocampus | Reproduced |
| Behavioural AUC 0.74 ± 0.10 | Reproduced |
| AUC 0.74 ± 0.09 (CS) and 0.69 ± 0.13 (TWH) | Reproduced |
| Asymmetric ROC | Reproduced |
| Higher accuracy with high confidence | Reproduced |
| 343 VS cells (18.4%) | Reproduced |
| 146 MS cells (7.8%) | Not reproduced |
| 26 dual VS and MS cells (1.4%) | Not reproduced |
| Comparable proportions at the two sites | Partially reproduced |
| 9 TWH sessions | Reproduced |
| Sessions of the 2018 release found in the dandiset (link check) | Partially reproduced |
| 23 sessions, 17 subjects and 288 neurons added since 2018 | Partially reproduced |
| Example neuron of Figure 4 selective for animals | Reproduced |
| Example neuron of Figure 3 selective for phones | Blocked: session 144 is not in the dandiset |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The MS and dual-cell counts follow the Methods (a 1 s window from 200 ms, all trials); the paper's code
uses 0.2 to 1.7 s and correct trials only, and gives the paper's 146 MS cells and 25 dual cells
(26 in the paper). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).

- `reproduce_chandravadia_2020.ipynb`: the analysis. It takes about three minutes, most of it streaming
  the files.
- `nomem.py`: loading the files (the stimulus images reduced to one hash per frame), the paper's
  tables from Europe PMC, and the behavioural and single-unit measures of the paper's code. Other
  notebooks on this dandiset can import it.
