# Sargolini et al. (2006) from dandiset 000582

Tests three conclusions of [Sargolini et al. (2006)](https://doi.org/10.1126/science.1125572)
on [DANDI:000582](https://dandiarchive.org/dandiset/000582/0.251111.2151).

| Claim | Outcome |
|---|---|
| Layer II was predominated by grid cells | Partially reproduced |
| Grid cells colocalized with head-direction and conjunctive cells in the deeper layers | Reproduced |
| All cell types were modulated by running speed | Reproduced |

The claims are from the paper's abstract; the paper is not open access and its full text and
methods were not used. The attempt record, with the reasons, is
[`attempts/000582-sargolini-2006-01.yaml`](../../attempts/000582-sargolini-2006-01.yaml).

- `reproduce_sargolini_2006.ipynb`: the analysis. It streams all 118 sessions and takes about
  six minutes.
- `sargolini.py`: loading the dandiset, and the rate-map, grid-score, head-direction and speed
  measures. Other notebooks on this dandiset can import it.

## Found about the dandiset

- Every file's description says the enclosure was 1 x 1 m, but in 23 of the 118 sessions the
  tracked positions span 1.5 to 2.5 m.
- No identifier links a cell across sessions, so the same cell may be counted more than once.
- The dandiset is described as a sample of the paper's cells; how they were selected is not
  stated.
- 47 sessions have one tracking LED, so head direction cannot be computed for them.
