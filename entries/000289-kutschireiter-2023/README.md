# Kutschireiter, Basnak, Wilson & Drugowitsch (2023) with dandiset 000289

Tests the findings of [Kutschireiter et al. (2023)](https://doi.org/10.1073/pnas.2210622120),
"Bayesian inference in ring attractor networks", a theory paper. The dandiset it is linked to,
[DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), holds two-photon imaging of
EPG neurons from a separate study of the same lab (Basnak et al.), which this paper does not analyse.

- Twelve claims are simulation or connectome results. They are tested on the paper's released code
  and processed outputs ([Zenodo 7615975](https://doi.org/10.5281/zenodo.7615975)) and on the public
  hemibrain v1.2 connectome export, not on the dandiset.
- One claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is
  tested on the dandiset's cue-contrast experiment (15 flies, visual cue at zero, low and high
  contrast).

| Claim | Outcome |
|---|---|
| A conflicting HD observation lowers the circKF's certainty, a confirming one raises it | Reproduced |
| An 80-neuron Bayesian ring attractor tracks the circKF, and its amplitude decays in darkness | Reproduced |
| The attractor matches the circKF's accuracy for reliable cues, not for unreliable ones | Reproduced |
| The Bayesian attractor beats the optimized conventional one at every reliability | Reproduced |
| The attractor's update weights are close to the circKF's | Reproduced |
| The best network decays slowly; performance falls with decay speed | Partially reproduced |
| Neural noise drops accuracy below 70% without retuning | Reproduced |
| Retuning reduces the drop by about 35% | Reproduced |
| Neural noise: unbiased position diffusion, upward amplitude drift, 1/sqrt(N) scaling | Partially reproduced |
| Connectome motifs: shifted PEN1 projections, broad Delta7 inhibition | Reproduced (assumed) |
| The Drosophila-like network matches the Bayesian attractor | Partially reproduced |
| Accuracy depends little on the number of neurons | Partially reproduced |
| Prediction: higher bump amplitude with a reliable cue (dandiset) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000289-kutschireiter-2023-01.yaml`](../../attempts/000289-kutschireiter-2023-01.yaml).

- `reproduce_kutschireiter_2023.ipynb`: the analysis. It takes about nine minutes, most of it
  streaming 10% of the raw imaging of 15 sessions.
- `bra.py`: loading the paper's Zenodo deposit in memory (with the two patches its code needs), the
  hemibrain export, and the dandiset's sessions; the bump decoder; a batched copy of the paper's
  single-population network.
