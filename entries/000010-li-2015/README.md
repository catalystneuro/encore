# Li, Chen, Guo, Gerfen & Svoboda (2015) from dandiset 000010

Tests the findings of [Li et al. (2015)](https://doi.org/10.1038/nature14178) that can be tested on
[DANDI:000010](https://dandiarchive.org/dandiset/000010/0.220126.1905). The dandiset holds 99
extracellular sessions (19 mice) and 59 two-photon imaging planes (4 mice) from left ALM during the
object location discrimination task, with the antidromic tagging light of 75 sessions. It holds no
photoinhibition or photoactivation data and no histology.

| Claim | Outcome |
|---|---|
| Performance 78.4% correct, under 13% early responses | Reproduced |
| Unit counts by spike width (124 FS, 1,245 pyramidal, 39 intermediate) | Partially reproduced |
| 912 of 1,245 pyramidal neurons selective | Reproduced |
| Preparatory, peri-movement and both (219, 389, 304) | Not reproduced |
| Selectivity time course | Reproduced |
| Population dynamics and stable selectivity | Reproduced |
| Error trials predict the lick direction | Reproduced |
| No contralateral bias in spike counts | Reproduced |
| Fast-spiking neurons fire more and are less selective | Not reproduced |
| PT and IT tagging counts | Partially reproduced |
| Antidromic latencies and jitter | Partially reproduced |
| PT and IT neurons show both activity types | Reproduced |
| PT neurons mostly contra-preferring, IT not | Reproduced |
| Contralateral selectivity of PT neurons from 570 ms before the go cue | Not reproduced |
| Imaging counts of task-related and selective cells | Not reproduced |
| Contra- and ipsi-preferring cells spatially intermingled | Not reproduced |
| Imaged PT cells mostly contra-preferring, IT not | Blocked: metadata insufficient |
| Reaction time | Blocked: methods underspecified |
| Photoinhibition and photoactivation (eight claims) | Blocked: data missing |
| Anatomy | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every PT and IT unit is deposited twice (also as Pyr), and the tagging light was delivered during
behavioural trials that the trial tables do not flag. The paper does not say whether those trials
belong in the task analyses, and the claims file lets either reading decide; the notebook runs every
electrophysiology claim with and without them, and the PT contra-preference holds only with them. The light is balanced between
the two trial types, so this is not a bias from the light. The PT result reaches P < 0.05 only with
the light and no-light trials pooled (each alone gives P = 0.14 to 0.15); why is not tested here.
Seven questions to a reader, all answered, are in
[`questions/000010.yaml`](../../questions/000010.yaml); the paper settles none of them, and the
readings the answers name are run. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/000010-li-2015-01.yaml`](../../attempts/000010-li-2015-01.yaml).

- `reproduce_li_2015.ipynb`: the analysis. It takes about twenty minutes, most of it streaming the
  files (unit tables, trial tables, laser traces, fluorescence and the lick traces).
- `alm.py`: loading the files, matching trials to their events, the light pulses, unit widths and
  duplicates, spike counts, antidromic latencies, the lick trace, and the imaging measures. Other notebooks on this dandiset can import it.
