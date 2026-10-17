# Mu, Bennett, Rubinov et al. (2019) from dandiset 000350

Tests the findings of [Mu et al. (2019)](https://doi.org/10.1016/j.cell.2019.05.050) that can be
tested on [DANDI:000350](https://dandiarchive.org/dandiset/000350/0.240822.1759), which holds 12
light-sheet sessions of paralysed larval zebrafish swimming fictively in virtual reality: swim and
stimulus signals for all 12, and segmented cell traces for 8 (4 of neurons and radial astrocytes,
4 of neurons only). The perturbation and noradrenergic imaging experiments of Figures 4 to 6 are
not in it, and its undescribed protocol codes and stimulus signals do not allow the replay, probe
and feedback protocols of Figures 1F, 1K and 7 to be identified.

| Claim | Outcome |
|---|---|
| Passive and active epochs in open loop last 24.4 and 36.1 s, with 29 bouts per active epoch | Partially reproduced |
| Inter-swim interval 1.2 s in closed loop and 1.19 s in active epochs | Partially reproduced |
| Fish are passive more in open loop than in closed loop | Not reproduced |
| Swim vigor rises after the switch to open loop | Reproduced |
| Intervals and vigor rise before passivity | Not reproduced |
| Whole-brain neuronal activity is lower during passivity | Reproduced |
| Whole-brain glial calcium rises before and peaks after passivity onset | Not reproduced |
| Neuronal and glial calcium are higher and fluctuate more in open loop | Partially reproduced |
| Glial calcium is weaker at closed-loop pauses than at futility-induced passivity | Not reproduced |
| NMF components consistent across fish (Figure 2D to 2G) | Blocked: methods underspecified |
| L-MO astrocytes most consistent (Figure 2K, 2L) | Blocked: metadata insufficient |
| Neuronal ramp overlapping NE-MO (Figure 6A) | Blocked: metadata insufficient |
| Replay, probe stimuli, NE mismatch and glial accumulation (Figures 1F, 1K, 7) | Blocked: metadata insufficient |
| Figures 4, 5 and 6B to 6N (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000350-mu-2019-01.yaml`](../../attempts/000350-mu-2019-01.yaml).

- `reproduce_mu_2019.ipynb`: the analysis. It takes about fifteen minutes, most of it reading cell
  traces from a subset of ROIs.
- `fictive.py`: loading the files, the closed- and open-loop conditions, passive and active epochs
  by the Methods' rule, and the whole-brain signal. Other notebooks on this dandiset can import it.
