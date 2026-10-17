# Xu, Dong, Chen, Delgado, Hughes, Zhang & O'Connor (2022) from dandiset 000239

Tests the findings of [Xu et al. (2022)](https://doi.org/10.1038/s41586-022-04478-7) that can be
tested on [DANDI:000239](https://dandiarchive.org/dandiset/000239/0.230607.1752), which holds the
trial tables of 33 mice in a sequence licking task, tongue tracking from video, and sorted spikes
from 93 recording sessions in S1TJ, M1TJ, ALM, S1BF and other areas.

| Claim | Outcome |
|---|---|
| 1537 single and 303 multi-units from 57 sessions | Partially reproduced |
| Figure 3 session counts (8, 9, 13, 5) | Reproduced |
| 32 plus or minus 13 units per session | Reproduced |
| 2684 trials in Figure 3a | Reproduced |
| Decoding of L, L', theta, I and tau across S1TJ, M1TJ, ALM, S1BF (five claims) | Reproduced |
| The five behavioural variables are uncorrelated | Reproduced |
| Coding axes explain about half the variance of the top five PCs | Reproduced |
| Coding axes are largely orthogonal | Partially reproduced |
| Canonical correlation of coding and PC subspaces | Reproduced |
| ALM and M1TJ predict backtracking, S1TJ and S1BF do not | Partially reproduced |
| ALM encodes zigzag sequence context | Reproduced |
| ALM encodes the upcoming target position in the inter-trial interval | Reproduced |
| No region encodes time to the trial start | Reproduced |
| 324, 233 and 119 active neurons in ALM, M1TJ, S1TJ | Partially reproduced |
| More ALM neurons tuned to initiation | Partially reproduced |
| S1TJ and M1TJ more lick-rhythmic than ALM | Reproduced |
| ALM activity drops at water contact | Reproduced |
| Sequences completed in about a second | Reproduced |
| Learning curves of 15 mice | Reproduced |
| Proficiency after about 1500 trials | Not reproduced |
| 47 backtracking sessions with 7458 and 2695 trials | Not reproduced |
| 1 to 2 missed licks after backtracking | Reproduced |
| About 5 consummatory licks | Not reproduced |
| Sequences started from the correct side | Reproduced |
| Optogenetic inhibition and control experiments (nine claims) | Blocked: metadata insufficient |
| Inhibition efficiency by cell type | Blocked: data missing |
| NNMF clustering into 13 clusters | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not name the region inhibited in each opto session or the condition of each control
session, so Figure 2 and Extended Data Fig. 1i-k cannot be tested. The recorded area is given only
by the session description. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000239-xu-2022-01.yaml`](../../attempts/000239-xu-2022-01.yaml).

- `reproduce_xu_2022.ipynb`: the analysis. It takes about 20 to 25 minutes on four cores; about
  a quarter of it is the seed variants of the Figure 3 fits, and a few minutes streaming the files.
- `seqlick.py`: loading the files, trial types and selection, spike rates, the elastic net with
  the one-SE rule, the SVM over time, and the per-session analyses. Other notebooks on this
  dandiset can import it.
