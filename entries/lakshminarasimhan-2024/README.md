# Lakshminarasimhan et al. (2024) from dandiset 000009

Tests the findings of [Lakshminarasimhan et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114059)
that can be tested on [DANDI:000009](https://dandiarchive.org/dandiset/000009/0.220126.1903), which
holds the ALM and thalamus recordings of Guo et al. (2017) that the paper reanalysed for its working
memory task (Figure 6 and Figure S6). The motor control recordings of Sauerbrei et al. (2020) and
the model simulations of Figures 1 to 5 are not in it.

| Claim | Outcome |
|---|---|
| The dandiset holds the paper's mouse, 151 ALM and 72 thalamic units | Reproduced |
| ALM activity explains choice, R2 = 0.97 | Not reproduced |
| Leading ALM PCs drive the choice readout | Reproduced (pooled population only) |
| ALM activity explains 0.70 of thalamic variance | Not reproduced |
| Top 5 ALM PCs capture 0.63 of explainable thalamic variance | Not reproduced |
| Corticothalamic weights align equally with PC 1 and the readout | Not reproduced |
| Motor control task (six claims) | Blocked: data missing |
| Model simulations (24 claims) | Blocked: too large (23), methods underspecified (1) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The regressions follow the paper's STAR Methods, with R2 on held-out test trials. On test trials
they do not generalize; on the training trials they give values close to the paper's. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/lakshminarasimhan-2024-01.yaml`](../../attempts/lakshminarasimhan-2024-01.yaml).

- `reproduce_lakshminarasimhan_2024.ipynb`: the analysis. It takes about eight minutes.
- `tcloop.py`: streaming the files, delay-period trial averages, and the readout and thalamic
  regressions of the paper's Methods. Other notebooks on this dandiset can import it.
