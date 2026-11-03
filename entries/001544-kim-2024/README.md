# Kim, Ananth, Desai, Role & Talmage (2024) from dandiset 001544

Tests the findings of [Kim et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114009) that can be
tested on [DANDI:001544](https://dandiarchive.org/dandiset/001544/0.260827.1410), which holds the
current-clamp recordings of Figure 6F to 6H and Figure S12: 12 APP-odor-activated, 8
AV-odor-activated and 24 home-cage VP cholinergic neurons. The behaviour, histology, fiber
photometry and morphology of the paper are not in it.

| Claim | Outcome |
|---|---|
| APP and AV neurons have a higher maximum firing rate than home-cage neurons | Reproduced |
| APP and AV neurons have a larger sag than home-cage neurons | Partially reproduced |
| Most other features are shared (the ten Figure S12 names as similar) | Reproduced |
| APP neurons differ from home-cage neurons in input resistance, spike width, downstroke and f-I slope | Reproduced |
| AV neurons are more hyperpolarized than APP neurons | Not reproduced |
| AV neurons have a smaller AHP than APP neurons | Not reproduced |
| APP neurons are less excitable than AV neurons | Not reproduced |
| Behaviour, histology, photometry and morphology (24 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The membrane potential in the files is measured under the DC current that holds each cell near
-65 mV, so it cannot show differences in resting potential. The home-cage group holds 24 cells
from 11 mice, where the paper analysed 21 from 8; the sag outcome, and that of the four
APP-specific differences, depend on which cells are used. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001544-kim-2024-01.yaml`](../../attempts/001544-kim-2024-01.yaml).

- `reproduce_kim_2024.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  files.
- `vpchat.py`: loading the files, the eighteen features of the paper's Methods (with the paper's
  code where the Methods are silent), and the cell-level and nested tests. Other notebooks on this
  dandiset can import it.
