# Chang, Finkel, Xu & O'Connor (2023) from dandiset 000232

Tests the findings of [Chang et al. (bioRxiv 2023, version 2)](https://doi.org/10.1101/2023.08.21.554194)
on [DANDI:000232](https://dandiarchive.org/dandiset/000232/0.240510.2038), which holds silicon-probe
recordings from S1, S2, MM, ALM and AMM of mice performing a cross-modal sensory selection task, and
the behaviour of optogenetic inhibition sessions in that task and in a tactile detection task.

| Claim | Outcome |
|---|---|
| Sessions, mice and units per area; optogenetic sessions per condition | Reproduced |
| Behavioural performance and outcome fractions (Figure 1D) | Reproduced |
| Neurons discriminating tactile hits from correct rejections (Figure 1H) | Partially reproduced |
| Neurons discriminating the rule before the stimulus (Figure 2C) | Partially reproduced |
| Neurons discriminating the stimulus before and after its onset (Figure 2D, 2E) | Reproduced |
| Pre-stimulus rule preference predicts touch-response modulation (Figure 2F) | Reproduced |
| Rule and stimulus decoding with LDA, SVM and random forests (Figure 3, S3) | Reproduced |
| Pre-stimulus distance predicts post-stimulus divergence (Figure 4C) | Partially reproduced |
| Subspace overlap of tCR with tHit (Figure 4E) | Partially reproduced |
| Pre- and post-stimulus overlaps correlate (Figure 4F) | Reproduced |
| Coding-dimension alignment (Figure S4E, S4F, S4H) | Partially reproduced |
| Block switches and first hits (Figure 5B) | Not reproduced |
| Motor but not sensory pre-stimulus states track rule switches (Figure 5D, 5E, S5) | Reproduced |
| Pre-stimulus inhibition of MM and ALM lowers tactile sensitivity (Figure 6C) | Partially reproduced |
| Hit rate, post-stimulus, visual, PPC and detection-task inhibition effects (Figure 6, S6, S7) | Reproduced |
| Lick probability unchanged on laser-only trials (Figure 6I, 6J) | Not reproduced |
| Probe locations (Figure 1E) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000232-chang-2023-01.yaml`](../../attempts/000232-chang-2023-01.yaml).

- `reproduce_chang_2023.ipynb`: the analysis. It takes about 9 minutes, close to 3 of them streaming the
  files.
- `xmodal.py`: loading the files, trial coding, binned and smoothed rates, the ideal-observer and
  decoding measures, transitions, coding dimensions and the optogenetic lick outcomes with the
  hierarchical bootstrap. Other notebooks on this dandiset can import it.
