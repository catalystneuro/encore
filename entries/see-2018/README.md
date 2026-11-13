# See, Atencio, Sohal & Schreiner (2018) from CRCNS ac-3

Tests the findings of [See et al. (2018)](https://doi.org/10.7554/eLife.35587) that can be tested
on [CRCNS ac-3](https://doi.org/10.6080/K09021X1). The data set holds the 16 columnar recordings
(655 units) made in rat primary auditory cortex with the 10-min dynamic moving ripple and ripple
noise, and the stimuli. It does not hold the 5-s repeats (Figure 9), the 15 repeats of the 10-min
ripple noise (Figure 11A, B) or the 64-channel recordings (Figure 8).

| Claim | Outcome |
|---|---|
| 16 penetrations, 655 neurons, 104 cNEs, 6.5 per penetration | Reproduced |
| Example recording: 9 cNEs of 2 to 6 neurons | Reproduced |
| Number of cNEs grows with the number of neurons (R2 0.74, about 15%) | Reproduced |
| Mean cNE size 7.4 neurons, R2 0.33 against neurons | Not reproduced |
| 9 cNEs with a negative-weight member | Not reproduced |
| 68% of neurons in one cNE, 9% in none, 23% in several | Not reproduced |
| 82% of cNE pairs within 200 um | Reproduced |
| No depth bias of cNE members | Reproduced (on an assumed test) |
| 70% of cNEs span 200 um or less | Not reproduced |
| PWC sharpness and delay explain about 50% of the variance of the correlation | Not reproduced |
| Distance explains 10 to 30% of the variance of the synchrony measures | Not reproduced |
| cNE pairs have sharper PWCs in every penetration | Partially reproduced |
| Member PWC sharpness about 2 ms, delay 0.76 ms | Not reproduced |
| Spike PWCs narrower than STRF PWCs for cNE pairs | Reproduced (on an assumption) |
| cNEs of interleaved halves match (96%) | Reproduced |
| Training cNEs predict test activity (102 cNEs, 83%) | Not reproduced |
| STRF MI peaks at 10 to 15 ms bins | Not reproduced |
| Fewer and larger cNEs with larger bins | Reproduced |
| cNE STRFs have a higher peak-trough difference than members' | Reproduced |
| cNE STRFs have a higher MI than members' | Not reproduced |
| cNE members' STRFs beat random groups | Reproduced |
| Shuffled and PR models give fewer cNEs, DG more | Reproduced |
| All models give smaller cNEs | Not reproduced |
| Coincidence ratios below the real data | Partially reproduced (models only) |
| PR model keeps STRFs (similarity 0.74) | Reproduced (on an assumption) |
| Figures 8, 9 and 11A, B (five claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The number of cNEs matches the paper closely, but they are smaller, which bears on the membership
claims. The paper does not give its STRF parameters or the lag range of its pairwise correlation
functions, and several outcomes rest on the choices made here. For the MI of cNE STRFs, no
reading meets the criterion in the printed run, and the outcome was changed to not reproduced
after a third verification round. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/see-2018-01.yaml`](../../attempts/see-2018-01.yaml).

- `reproduce_see_2018.ipynb`: the analysis. It takes about 47 minutes on four processes, most of
  it the detection at eight bin sizes, the random groups and the model runs.
- `cne.py`: loading from the bucket, the cNE detection, pairwise correlation functions, STRFs and
  their mutual information, and the shuffled, PR and DG models. Other notebooks on this data set
  can import it.
