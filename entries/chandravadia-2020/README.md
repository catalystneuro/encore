# Chandravadia, Liang, Schjetnan et al. (2020) from dandiset 000004

Tests the claims of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data
descriptor, on [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852), which holds 87
sessions of single neurons recorded in the human amygdala and hippocampus during a new/old recognition
memory task.

| Claim | Outcome |
|---|---|
| 1863 neurons from 59 subjects | Reproduced |
| 87 sessions, as listed in Online-only Table 1 | Reproduced |
| Age and sex of each subject as in Online-only Table 1 | Partially reproduced |
| 100 encoding and 100 recognition trials (50 new, 50 old), 5 categories per session | Partially reproduced |
| new_old_labels_recog is 0 for old and 1 for new | Not reproduced |
| TTL event codes and their order | Partially reproduced |
| Experiment ids of the learning and recognition blocks | Partially reproduced |
| session_start_time set to the first of the month | Partially reproduced |
| Units table columns and quality metrics | Partially reproduced |
| Electrodes table: location, coordinates, impedance, filter, channel | Not reproduced |
| Fewer than 3% of interspike intervals below 3 ms | Partially reproduced |
| All neurons in the amygdala or hippocampus | Reproduced |
| Mean behavioural AUC 0.74 ± 0.10 | Reproduced |
| AUC by site, CS 0.74 ± 0.09 and TWH 0.69 ± 0.13 | Reproduced |
| Asymmetric ROC | Reproduced |
| Higher accuracy at high confidence | Reproduced |
| 343 VS cells (18.4%) | Reproduced |
| 146 MS cells (7.8%) | Not reproduced |
| 26 cells both VS and MS (1.4%) | Not reproduced |
| Comparable proportions at the two sites | Partially reproduced |
| 9 sessions from Toronto Western Hospital | Reproduced |
| Sessions of the earlier release (Faraut et al. 2018) are in the dandiset | Partially reproduced |
| 23 sessions, 17 subjects and 288 neurons added to the earlier release | Partially reproduced |
| Example VS neuron 132-177-4-RA prefers animals | Reproduced |
| Example VS neuron 144-140-3-RH prefers phones | Reproduced (assumed: session 144 is session 2009) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The MS and dual counts are judged on the Methods' description (a 1 s window, all trials); the paper's
code (a 1.5 s window, correct trials only) gives the paper's numbers, shown as a variant. The new/old
labels in the files are the reverse of the stated coding. The Figure 3 neuron's session (144) is not
under that id in the dandiset; the paper's Figure 3 scripts name it as the session of subject TWH103,
session 2009 here, and the neuron is tested there as an assumption. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).
