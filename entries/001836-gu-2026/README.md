# Gu, Liu, Gillespie, Nevers, Denovellis, Coulter, Kay & Frank (2026) from dandiset 001836

Tests the findings of [Gu et al. (2026)](https://doi.org/10.64898/2026.05.26.727951) that can be
tested on [DANDI:001836](https://dandiarchive.org/dandiset/001836/0.261030.0428), which holds the
recordings of five rats learning a hidden four-arm sequence in a maze. The behavioral findings of
Figure 1 and Figure S1F are tested from the well pokes and pumps and the deposited linearized
position. The Figure 3 findings are tested on the paper's own triggered decode tables, which carry
no description and are identified by aligning their trigger times with the COM times and pokes. The
ripple finding of Figure S7B is tested by detecting ripples on the deposited LFP. The other findings
on hippocampal content need the decoder output over whole sessions, which the dandiset does not hold.

| Claim | Outcome |
|---|---|
| All rats learned the task (Figure 1C) | Reproduced |
| Trial and COM trial counts per rat (Figure 1E inset) | Not reproduced |
| Initial switch-side bias above 2 in every rat (Figure 1D) | Reproduced |
| The bias declines with days, to about 1.5 (Figure 1D) | Partially reproduced |
| Most COM trials have one COM event, several in every rat (Figure S1F) | Reproduced |
| COM final choices are rewarded more often than the initial ones (Figure 1G) | Reproduced |
| COM trials reach the reward rate of nearby trials (Figure 1G) | Reproduced |
| The final choice switches side less than the initial one (Figure 1H) | Not reproduced |
| The final-choice ratio does not differ from 1 (Figure 1H) | Reproduced |
| More extended decodes before stopping on COM trials (Figure 3B) | Partially reproduced |
| Decoded distance predicts a COM (Figure 3B) | Partially reproduced |
| More distant decodes after stopping than before (Figure 3C) | Partially reproduced |
| More distant decodes after stopping than on inbound runs (Figure 3D) | Not reproduced |
| Lower ripple rate during COM than at trial ends (Figure S7B) | Reproduced |
| Remote and local extended content, theta (15 claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds fewer trials than the paper reports for rats M, K and L, which is most of why the
counts are not reproduced. For Figure 1H the initial ratio exceeds the final in every rat, as a
direction (rat M has p = 0.42), but the paired t-test reaches p < 0.01 in two rats where the paper
reports four. Figure 3B: COM decodes reach further than run-through decodes at p < 0.01 in four of
five rats in the first random draw of arm ranges (all five in about half of further draws), and the
decoded distance predicts a COM with a fold change within tolerance but not at p < 1e-20. Figure 3C:
post-stopping decodes reach further than pre-stopping ones in four of five rats. Figure 3D: with the
decoder of the inbound tables identified and all the paper's COM tables, COM exceeds inbound at
p < 0.05 in only three rats, so the claim is not reproduced; the third verification round agreed
with this change from partially reproduced. The result is borderline and changes with the random
draw. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001836-gu-2026-01.yaml`](../../attempts/001836-gu-2026-01.yaml).

- `reproduce_gu_2026.ipynb`: the analysis. It took 11 to 14 minutes in the runs of the round-2
  revision, in separate processes: 2 to 5 minutes to stream the events and the linearized position
  of 197 run sessions, about 3 to 5 for the triggered tables, and under 3 for ripple detection on
  the LFP.
- `comtask.py`: loading, trials, change-of-mind detection, the side and sequence measures, the
  triggered tables and ripple detection. Other notebooks on this dandiset can import it.
