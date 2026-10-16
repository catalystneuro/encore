# Grosmark & Buzsáki (2016) from dandiset 000044

Tests the findings of [Grosmark and Buzsáki (2016)](https://doi.org/10.1126/science.aad1935) on
[DANDI:000044](https://dandiarchive.org/dandiset/000044/0.261005.2101), which holds eight sessions
of CA1 units, LFP, sleep states and track positions from four rats, each with sleep before (PRE)
and after (POST) a first exploration of a novel track (MAZE). The supplementary Methods could not
be read, so the definitions the main text leaves open are common choices fixed before the
analysis.

| Claim | Outcome |
|---|---|
| Four rats, eight sessions, two linear tracks and a circular one | Reproduced |
| 491 place cells | Not reproduced (417; 480 at a 0.5 Hz threshold) |
| Sequence scores higher in POST than in PRE | Not reproduced by the pooled test; higher within all 8 sessions |
| Sequence scores higher in MAZE than in PRE | Reproduced |
| PRE coactivation dominated by fast-firing cells | Reproduced |
| Slow-firing cells gain the most coactivation from PRE to POST | Not reproduced |
| Slow-firing cells show the most replay of coactivation | Not reproduced |
| Low and high-rate medians of 0.39 and 1.12 Hz | Partially reproduced |
| Low-rate cells more informative, with a larger ripple-gain increase | Partially reproduced |
| Slow but not fast cells increase sequence content | Not reproduced |
| Increase in sequence content limited to high ripple-gain cells | Not reproduced |
| Shuffling the 10 to 20% of cells with the highest dPCC removes replay | Partially reproduced |
| Eight claims on strongly contributing, rigid and plastic cells (PCC) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000044-grosmark-2016-01.yaml`](../../attempts/000044-grosmark-2016-01.yaml).

- `reproduce_grosmark_2016.ipynb`: the analysis. It takes about sixteen minutes on four cores, about three of
  them streaming one LFP channel per session.
- `grosmark.py`: loading the files, ripple detection on one channel, candidate events, rate maps,
  the Bayesian decoder with its weighted-correlation score, the per-cell contributions and the
  cell measures. Other notebooks on this dandiset can import it.
