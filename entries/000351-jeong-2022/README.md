# Jeong, Taylor, Floeder et al. (2022) from dandiset 000351

Tests the findings of [Jeong et al. (2022)](https://doi.org/10.1126/science.abq6740) that can be
tested on [DANDI:000351](https://dandiarchive.org/dandiset/000351/0.260828.1905), which holds the
photometry (dLight1.3b dF/F in the nucleus accumbens core) and event logs of Experiments 1 to 7
and the licking of the separate group of Fig S8L.

| Claim | Outcome |
|---|---|
| The code's session lists can be applied to the dandiset | Partially reproduced |
| Session counts per experiment (Methods) | Reproduced |
| Experiment 1: excluded rewards, Tests 1 and 2, Fig S8B, S8D, S8G, S8H, S8K, S8L | Reproduced |
| Fig S8E: lick bout onset responses | Blocked: methods underspecified (the windows give different outcomes) |
| Experiments 2 to 5: Tests 3, 4, 5, 6 and 9, Fig 4I, 4L, S10C | Reproduced |
| Fig 4P: faster decay of the cue response with background rewards (Test 7) | Not reproduced |
| Experiment 6: intermediate cue and reward responses (Test 8, Fig S11D-E) | Reproduced |
| Experiment 7: Fig 6D, 6G, 6I learning, last-session licking, Fig S12F | Reproduced |
| Experiment 7: lower CS1 response with inhibition in the last session | Not reproduced |
| Simulations (Figs 2, 3C and F, 5B, 6H, S5, S6, S13; seven claims) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most tests follow the paper's analysis code (github.com/namboodirilab/ANCCR at commit cff4414),
ported to Python; many of its printed statistics are recovered to the second decimal. The session
lists of the code (Day numbers) are applied to the dandiset's file names. Seven integer days
inside those lists have no session in the dandiset, one of them a listed start day, and the event times are in seconds though the files say
milliseconds. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000351-jeong-2022-01.yaml`](../../attempts/000351-jeong-2022-01.yaml).

- `reproduce_jeong_2022.ipynb`: the analysis. It takes about two minutes, most of it streaming the
  event logs and dF/F of 428 files.
- `jeong.py`: loading, the session lists of the paper's code, and the measures of its scripts.
  Other notebooks on this dandiset can import it.
