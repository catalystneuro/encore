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
| 809 neurons, 454 hippocampus, 209 entorhinal, 146 amygdala | Reproduced, resting on an assumption |
| Spike sorting quality (ISI, waveform SNR) | Not reproduced |
| Firing rates by period | Reproduced |
| Maintenance neurons in all three regions (Figure 2c) | Reproduced, resting on an assumption |
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

The behavior is within the tolerances of the claims for accuracy, capacity and the response-time F, but the
response-time slope is 69 to 76 against 118 ms/item. The total of units, the counts per participant
and the firing rates are within tolerance of the paper's. The claims that compare trials by their
labels (workload, set size, correct against incorrect) fail: in the files, the workload information
of the spikes is at chance in every session. Pooled over the sessions with all 192 trials, it peaks
when the spikes of each trial window are paired with the label of the trial three later, but
session by session only two sessions support that shift, and moving every session by three trials
recovers little, so a misalignment of the spikes and the trial table is possible but not
established. The units' regions as the paper assigned them are not in the files. Reading them from the atlas labels
of each electrode's contacts, nearest the tip first, gives region counts of 467, 196 and 146
against the paper's 454, 209 and 146, within 10%, and the maintenance neuron counts per region
then match too; by electrode name they do not. Those two outcomes rest on that choice, which was
made after seeing the counts. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000575-boran-2022-01.yaml`](../../attempts/000575-boran-2022-01.yaml).

- `reproduce_boran_2022.ipynb`: the analysis. It takes 16 to 27 minutes, depending on the machine, most of it in permutation
  nulls, dPCA runs and decoders.
- `mtl_wm.py`: loading the files, period spike counts, the permutation t-test of the paper's
  Methods, and the pseudo-population decoder. Other notebooks on this dandiset can import it.
