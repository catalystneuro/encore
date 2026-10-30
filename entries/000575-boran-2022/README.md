# Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022) from dandiset 000575

Tests the findings of [Boran et al. (2022)](https://doi.org/10.1016/j.neuroimage.2022.119123) on
[DANDI:000575](https://dandiarchive.org/dandiset/000575/0.231010.1811), which holds the trials,
answers and sorted units of 16 sessions from 13 epilepsy patients doing a visual change detection
task with 1, 2, 4 or 6 colored squares.

| Claim | Outcome |
|---|---|
| Accuracy by set size (98, 99, 88, 73%) | Reproduced |
| Memory capacity, Pashler's and Cowan's K | Reproduced |
| Table 1, capacity and neurons per participant | Reproduced |
| Response time rises with set size, 118 ms/item | Partially reproduced |
| 809 neurons, 454 hippocampus, 209 entorhinal, 146 amygdala | Partially reproduced |
| Spike sorting quality (ISI, waveform SNR) | Not reproduced |
| Firing rates by period | Reproduced |
| Maintenance neurons in all three regions (Figure 2c) | Partially reproduced |
| Maintenance neurons modulated by workload (Figure 2d) | Not reproduced |
| More hippocampal maintenance neurons on correct trials | Not reproduced |
| Test neurons (Figure 3b) | Partially reproduced |
| dPCA separates set sizes (Figure 4a) | Not reproduced |
| Speed lowest in maintenance (Figure 4b) | Reproduced |
| Distance between set sizes largest in maintenance (Figure 4c) | Partially reproduced |
| Workload decoded from all neurons, 87.5% (Figure 4d) | Not reproduced |
| Workload decoded from hippocampus and entorhinal cortex | Not reproduced |
| Performance not decodable | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The behavior matches the paper exactly, and so do the counts of units and the firing rates. The
claims that compare trials by their labels (workload, set size, correct against incorrect) fail:
in the files, the workload information of the spikes is at chance and peaks when the spikes of each
trial window are paired with the label of the trial three later, which points to a misalignment of
the spikes and the trial table in part of the sessions. The units' regions as the paper assigned
them are not in the files. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000575-boran-2022-01.yaml`](../../attempts/000575-boran-2022-01.yaml).

- `reproduce_boran_2022.ipynb`: the analysis. It takes about 18 minutes, most of it in permutation
  nulls, dPCA runs and decoders.
- `mtl_wm.py`: loading the files, period spike counts, the permutation t-test of the paper's
  Methods, and the pseudo-population decoder. Other notebooks on this dandiset can import it.
