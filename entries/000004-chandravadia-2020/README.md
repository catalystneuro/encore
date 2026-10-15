# Chandravadia et al. (2020) from dandiset 000004

Tests the findings of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9) on
[DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852), which holds 87 sessions of
59 patients with 1864 single units from the amygdala and hippocampus during a new/old recognition
memory task. The paper is a data descriptor, so most claims check the files against its description
of the data; the others repeat the behavioural and single-unit results of Figure 5.

| Claim | Outcome |
|---|---|
| 1863 neurons from 59 subjects | Reproduced |
| The 87 sessions of Online-only Table 1 | Reproduced |
| Age and sex of every subject as in Online-only Table 1 | Partially reproduced |
| 100 encoding and 100 recognition trials, 5 categories per session | Partially reproduced |
| new_old_labels_recog is 0 for old and 1 for new stimuli | Not reproduced |
| Event codes of Table 1 | Partially reproduced |
| Experiment ids of Table 2 | Partially reproduced |
| Session dates set to the first of the month | Partially reproduced |
| Units table as described | Partially reproduced |
| Electrodes table as described (impedance, coordinates) | Not reproduced |
| Fewer than 3% of interspike intervals below 3 ms | Partially reproduced |
| All units in amygdala or hippocampus | Reproduced |
| Behavioural AUC 0.74 ± 0.10 | Reproduced |
| AUC by site, 0.74 ± 0.09 (CS) and 0.69 ± 0.13 (TWH) | Reproduced |
| Asymmetric ROC | Reproduced |
| Higher accuracy with high confidence | Reproduced |
| 343 visually selective cells (18.4%) | Reproduced |
| 146 memory selective cells (7.8%) | Not reproduced |
| 26 cells both visually and memory selective (1.4%) | Not reproduced |
| Comparable proportions at the two sites (Figure 5f) | Partially reproduced |
| 9 sessions from Toronto Western Hospital | Reproduced |
| Example neuron 132-177-4-RA of Figure 4 | Reproduced |
| The earlier release's sessions are in the dandiset (with outside input) | Partially reproduced |
| 23 sessions, 17 subjects and 288 neurons added to the earlier release (with outside input) | Partially reproduced |
| Example neuron 144-140-3-RH of Figure 3 | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The memory selective and dual counts follow the Methods (all trials, a 1 s window). The paper's code
selects on correct trials in a 1.5 s window, and with its choices the counts are 147 and 26,
against the paper's 146 and 26. The new/old label in the files is coded 1 = old, the reverse of the paper's text
and the files' column description. Two pairs of sessions hold identical spike trains. Against the
session list of the earlier release (Faraut et al. 2018, Table 1), the dandiset has the 23 new
sessions and 17 new subjects the paper states, but 325 units in them, not 288. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000004-chandravadia-2020-01.yaml`](../../attempts/000004-chandravadia-2020-01.yaml).

- `reproduce_chandravadia_2020.ipynb`: the analysis. It takes about three minutes, most of it
  streaming the files and the bootstrap tests.
- `recogmem.py`: loading the files, Online-only Table 1, Table 1 of Faraut et al. 2018, and the
  selectivity and behavioural measures of the paper's code. Other notebooks on this dandiset can import it.
