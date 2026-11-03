# Funamizu, Kuhn & Doya (2016) from dandiset 001605

Tests the findings of [Funamizu, Kuhn and Doya (2016)](https://doi.org/10.1038/nn.4390) that can
be tested on [DANDI:001605](https://dandiarchive.org/dandiset/001605/0.251007.0553), which holds
two-photon imaging of PPC and PM with the behaviour of 94 sessions in 8 mice during auditory
virtual navigation. The muscimol experiment and the sound-mapping trials are not in it.

| Claim | Outcome |
|---|---|
| Session and neuron counts (94 sessions, 41,031 neurons) | Reproduced |
| Time to reward and time per no-sound zone | Not reproduced |
| Start-to-lick distance correlates with goal distance in every session | Partially reproduced |
| Licking rises in no-sound zones (Fig. 1c); faster mice lick more steeply (Supp. Fig. 1) | Reproduced |
| Muscimol experiment (five claims) and sound-responsive neurons | Blocked: data missing |
| Counts of goal-distance and after-reaching neurons; task-relevant percentages | Not reproduced |
| PPC has more goal-distance neurons than PM | Reproduced |
| After- against before-reaching neurons; layer distance preference | Reproduced (assumption) |
| Distance or time in single-neuron regressions (Fig. 3b) | Blocked: too large |
| Distance fits better than Step or Sound (Supp. Fig. 6) | Partially reproduced |
| Tuning curves similar between PPC and PM | Blocked: methods underspecified |
| Ramping of after-reaching neurons with and without sound (Fig. 3c, Supp. Fig. 8a,b) | Reproduced (two with assumptions) |
| PPC steeper than PM without sound (Supp. Fig. 8c) | Partially reproduced (assumption) |
| PPC preserves distance preference more than PM (Supp. Fig. 9) | Reproduced (assumption) |
| Decoding above chance; PPC lower error, better MAP near the goal, lower uncertainty (Fig. 4) | Reproduced (assumptions) |
| Sound reduces decoding error (Supp. Fig. 11) | Reproduced |
| MAP follows distance in the continuous condition; falls in most intermittent zones | Reproduced; partially reproduced |
| MAP slopes lower and uncertainty falls less without sound (Fig. 5b-d) | Reproduced |
| PPC layer 3 steeper than layer 2; fast trials steeper (Supp. Fig. 13); log-normal decoder better | Not reproduced |
| SVM decoders and neural correlations | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes rest on one assumption: the baseline of the task-relevance t-test is zero (the
session mean of R). Under it, 91 of 94 sessions have goal-distance neurons, as the paper
reports. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001605-funamizu-2016-01.yaml`](../../attempts/001605-funamizu-2016-01.yaml).

- `reproduce_funamizu_2016.ipynb`: the analysis. It takes about 25 minutes, most of it streaming
  the files.
- `funamizu.py`: loading, the classification statistics, the decoder and the single-basis
  regressions. Other notebooks on this dandiset can import it.
