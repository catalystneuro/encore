# Ito & Doya (2009) from dandiset 001641

Tests the findings of [Ito and Doya (2009)](https://doi.org/10.1523/jneurosci.6157-08.2009) on
[DANDI:001641](https://dandiarchive.org/dandiset/001641/0.260922.0719), which holds the behaviour of six rats
in 70 sessions of a probabilistic free-choice task and 214 single units of the nucleus accumbens (NAc) and
ventral pallidum (VP).

| Claims | Outcome |
|---|---|
| Trial and block counts, reaction times (3 claims) | Reproduced |
| Tone-discrimination error rates | Not reproduced |
| Choice history, Fig. 2 (6 claims) | 5 reproduced; the two-back test blocked (its readings disagree) |
| Least-squares model fits, Fig. 3 and Table 1 | Partially reproduced; not reproduced |
| Model prediction, Fig. 5: Markov and constant models | Blocked (readings disagree; the local matching law is undefined as specified) |
| Model prediction, Fig. 5: time-varying models, binary accuracy | Partially reproduced; reproduced |
| Fig. 5 paired tests (2 claims) | Blocked (readings disagree) |
| Table 2 parameters | Not reproduced |
| Table 3 | Blocked (readings disagree; asked of a reader) |
| Fig. 4, supplemental Data 1 | Reproduced |
| Neuron counts, firing rates, action and reward coding, chance levels | Reproduced |
| State coding | Blocked (readings disagree) |
| Action-value coding by block comparison and its region differences (3 claims) | 1 reproduced, 2 partially reproduced |
| Action-command coding; same event coding in NAc and VP | Not reproduced |
| Preferences of coding neurons (2 claims) | Reproduced; partially reproduced |
| Regression analyses, Fig. 8C and 8D (5 claims) | 2 reproduced, 1 partially, 2 not reproduced |
| Mutual information, Fig. 9 (5 claims) | 3 reproduced, 1 partially, 1 not reproduced (asked of a reader) |
| Core against shell | Blocked: the units are not assigned to core or shell |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code and its equations are missing from the text, so several methods were run under
every reading the claims file lists; as the claims file directs, a claim whose readings give different
outcomes is blocked, with every reading shown. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/ito-2009-01.yaml`](../../attempts/ito-2009-01.yaml).

- `reproduce_ito_2009.ipynb`: the analysis. It takes about 40 minutes, most of it fitting the time-varying
  models with the particle filter.
- `ito2009.py`: loading the files, the choice sequences, the Q-learning, Markov and particle-filter models,
  spike counts in the paper's time bins, and the mutual-information estimate. Other notebooks on this
  dandiset can import it.
