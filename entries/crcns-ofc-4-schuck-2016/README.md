# Schuck, Cai, Wilson & Niv (2016) from CRCNS ofc-4

Tests the findings of [Schuck et al. (2016)](https://doi.org/10.1016/j.neuron.2016.08.019) that can be
tested on [CRCNS ofc-4](https://doi.org/10.6080/K0FN14CH), which holds the OFC fMRI time series, design
matrices and event files of 24 of the paper's 27 participants. The whole-brain searchlight, the other
regions of interest, the training session, the response side and the synthetic-data controls are not
testable on it.

| Claim | Outcome |
|---|---|
| Mean error rate 2.3% | Blocked: metadata insufficient |
| Error rates differ by trial class (3.4, 2.3, 1.4%) | Partially reproduced (assumption) |
| Error rates stable over runs | Reproduced (assumption) |
| Error rates not affected by age or category | Reproduced (assumption) |
| Training against scanner errors and RTs (two claims) | Blocked: data missing |
| RTs stable over runs | Reproduced |
| Faces faster than houses (944 against 1028 ms) | Reproduced |
| RTs faster on Internal trials | Reproduced |
| 16-way decoding in OFC (12.2%) | Partially reproduced |
| Two-back state space decodes worse (8.1%) | Partially reproduced |
| Hidden components decoded above chance | Partially reproduced |
| Current age not decoded | Reproduced |
| Two-back components not decoded | Reproduced |
| 8-way decoding (16.7%) and its components | Reproduced (assumption) |
| Permutation control | Partially reproduced |
| Synthetic-data controls (two claims) | Blocked: metadata insufficient |
| Enter and non-Enter states cluster | Reproduced |
| Hidden components decoded within Enter and non-Enter trials | Not reproduced |
| Searchlight conjunction in medial OFC | Blocked: data missing |
| Other regions of interest | Blocked: data missing |
| Decoding correlates with error rate (r = -0.58) | Partially reproduced (assumption) |
| Trial-wise decoding drops on error trials | Not reproduced |
| Decoding declines before errors | Not reproduced |
| Error trials decode worse than matched trials | Not reproduced (assumption) |
| Pattern correlation predicts transition errors | Not reproduced |
| Euclidean distance predicts transition errors | Reproduced (assumption) |
| Motor response not decoded in OFC | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no voxel coordinates, so no beta map or volume is smoothed, and the paper's smoothing
is the main difference from its method. The error events are blocks that merge each error with its
repetitions and often the trials after it, so the number of errors and the state of most error trials
cannot be read from them; the notebook reconstructs the state of Enter errors from the neighbouring
trials. Only Enter errors can be given a state, and with beta maps z-scored by voxel Enter trials decode
worse than other trials on single volumes, so the error-trial comparisons are made against Enter trials as well. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ofc-4-schuck-2016-01.yaml`](../../attempts/crcns-ofc-4-schuck-2016-01.yaml).

- `reproduce_schuck_2016.ipynb`: the analysis. It takes about five minutes, most of it streaming the
  zip and fitting the classifiers.
- `ofc4.py`: streaming the zip, reading the run files and event files, the reconstruction of error
  trials, the GLM, the classifiers and the trial-wise test data. Other notebooks on this data set can
  import it.
