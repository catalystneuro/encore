# Ito & Doya (2009) from dandiset 001641

Tests the findings of [Ito and Doya (2009)](https://doi.org/10.1523/jneurosci.6157-08.2009) on
[DANDI:001641](https://dandiarchive.org/dandiset/001641/0.260922.0719), which holds the behaviour of six rats
in 70 sessions of a probabilistic free-choice task and 214 single units of the nucleus accumbens (NAc) and
ventral pallidum (VP).

| Claims | Outcome |
|---|---|
| Trial and block counts, reaction times (3 claims) | Reproduced |
| Tone-discrimination error rates | Not reproduced |
| Choice history, Fig. 2 (6 claims) | Reproduced (one resting on an assumption) |
| Least-squares model fits, Fig. 3 and Table 1 | Partially reproduced; not reproduced |
| Model prediction, Fig. 5: Markov, constant and time-varying models, binary accuracy | Reproduced (three resting on assumptions) |
| Fig. 5 paired tests (2 claims) | Not reproduced (resting on assumptions) |
| Table 2 parameters | Partially reproduced |
| Table 3, Fig. 4, supplemental Data 1 | Reproduced |
| Neuron counts, firing rates, state, action and reward coding, chance levels | Reproduced |
| Action-value coding by block comparison and its region differences (3 claims) | 1 reproduced, 2 partially reproduced |
| Action-command coding; same event coding in NAc and VP | Not reproduced |
| Preferences of coding neurons (2 claims) | Reproduced; partially reproduced |
| Regression analyses, Fig. 8C and 8D (5 claims) | 2 reproduced, 1 partially, 2 not reproduced |
| Mutual information, Fig. 9 (5 claims) | 4 reproduced, 1 partially |
| Core against shell | Blocked: the units are not assigned to core or shell |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code and its equations are missing from the text, so several methods were run under
every reading the claims file lists; outcomes that differ between readings follow the reading the paper best
supports and are marked as resting on an assumption. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001641-ito-2009-01.yaml`](../../attempts/001641-ito-2009-01.yaml).

- `reproduce_ito_2009.ipynb`: the analysis. It takes about 20 minutes, most of it fitting the time-varying
  models with the particle filter.
- `ito2009.py`: loading the files, the choice sequences, the Q-learning, Markov and particle-filter models,
  spike counts in the paper's time bins, and the mutual-information estimate. Other notebooks on this
  dandiset can import it.
