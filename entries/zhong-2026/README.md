# Zhong, Katkov & Tsodyks (2026) on dandiset 000207

Tests the findings of [Zhong et al. (2026)](https://doi.org/10.7554/elife.109538) that can be tested
on [DANDI:000207](https://dandiarchive.org/dandiset/000207/0.220216.0323), the human medial temporal
lobe single-neuron recordings of Zheng et al. (2022) that the paper reanalyses for its Figure 3 and
Figure S3. Most of the paper is model simulation, a derivation, and a reanalysis of published recall
tables, none of which use these data.

| Claim | Outcome |
|---|---|
| The dandiset's subjects are those of Supplementary Table 2 of Zheng et al. (link) | Reproduced |
| Four of eighteen subjects are left out, leaving 14 | Partially reproduced |
| Non-boundary neurons dip about 130 ms after the boundary-neuron peak, then ramp up | Blocked: methods underspecified |
| The dip and ramp are seen in most individual subjects | Blocked: methods underspecified |
| Aligned to clip onset, the other neurons show no dip and ramp | Blocked: methods underspecified |
| Simulations of the model and the derivation of M* = 2^(C-1) (five claims) | Blocked: other |
| Lc from the Miller and Selfridge recall data and its replications (three claims) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper takes its boundary and onset neurons from Zheng et al. (2022). The dandiset does not say
which units they are, and Zheng et al. give only counts per subject. Re-selecting them by the Methods
of Zheng et al. finds 8 to 10 boundary and event cells where they count 76, so the Figure 3
analysis is run under every reading but does not decide the claims. Along the way the attempt found
that the spike times of one subject (TWH138) are not on the clock of its trial tables, and that in 11
of the other 18 sessions the population shows no clear response at clip onsets. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/zhong-2026-01.yaml`](../../attempts/zhong-2026-01.yaml).

- `reproduce_zhong_2026.ipynb`: the analysis. It takes about six minutes, mostly streaming the files
  and running permutation tests.
- `chunking.py`: loading the files, the cut times, the cell selection of Zheng et al. with its
  permutation tests, the pooled and z-scored traces, and the dip and ramp measures. Other notebooks on
  this dandiset can import it.
