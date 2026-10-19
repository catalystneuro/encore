# Davatolhagh et al. (2025) from dandiset 001712

Tests the findings of [Davatolhagh et al. (2025)](https://doi.org/10.1101/2025.09.12.675910) that can
be tested on [DANDI:001712](https://dandiarchive.org/dandiset/001712/draft), which holds one widefield
imaging and behaviour session of one mouse (FD-28) whose genotype is not stated. The dandiset has no
published version, so the draft is read. The paper's comparisons of Nrxn1a knockout and wild-type mice
cannot be tested.

| Claim | Outcome |
|---|---|
| Rightward choices rise with right contrast (Figure 1C) | Reproduced |
| Longer reaction times at lower contrast (Figure 1E) | Not reproduced |
| More rightward choices in right-likely blocks (Figure 2B, C) | Reproduced |
| Choices adapt toward the block side after a switch (Figure 2E, F) | Reproduced |
| Lateralized responses to visual stimuli (Figure 3B) | Not reproduced |
| The encoding model explains over half the variance (Figure 4C) | Partially reproduced |
| Movement predictors dominate the explained variance (Figure 4C, D) | Partially reproduced |
| Comparisons between genotypes (eleven claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001712-davatolhagh-2025-01.yaml`](../../attempts/001712-davatolhagh-2025-01.yaml).

- `reproduce_davatolhagh_2025.ipynb`: the analysis. It takes about seven minutes, a quarter of it
  streaming and decoding the body camera video.
- `encoding_all_cameras.ipynb`: a variant of the encoding model with the video components of the
  left and right cameras added, as in the paper. It takes about 20 minutes, most of it streaming
  and decoding the three videos. It does not decide an outcome.
- `wfprior.py`: loading the session, movement variables binned to imaging frames, the cameras'
  video components, psychometric and action-kernel fits, and the cross-validated ridge encoding model.
  Other notebooks on this dandiset can import it.
