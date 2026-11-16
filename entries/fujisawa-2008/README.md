# Fujisawa, Amarasingham, Harrison & Buzsaki (2008) from DANDI:000067 and CRCNS pfc-2

Tests the findings of [Fujisawa et al. (2008)](https://doi.org/10.1038/nn.2134) on both of the paper's datasets:
[DANDI:000067](https://dandiarchive.org/dandiset/000067/0.261106.2004) (NWB files with the sorted units, the
wideband signal and the head LEDs of three rats) and [CRCNS pfc-2](https://doi.org/10.6080/K01V5BWK) (the lab's
per-session summaries: correct trials, linearised position, cell lists, and for the paper's Figure 2a session its
list of connections). Spike times are read from the NWB files and matched to the lab's cells by shank and cluster;
trials, positions and cell lists come from CRCNS.

| Claim | Outcome |
|---|---|
| The DANDI channels follow the CRCNS channel map | Not reproduced (no nose-poke sensor on channels 97 and 98 in rat GG) |
| 633 units in four rats, 222 in layer 5 | Partially reproduced (627 in three rats, no rat with 222) |
| Task performance 91.9% | Blocked: data missing (correct trials only) |
| Population fires uniformly over the maze | Not reproduced |
| 10% and 20% of neurons active per 100 ms | Partially reproduced |
| Firing width 0.27 +/- 0.17 | Reproduced |
| Population vector widths 0.18 and 0.27 | Partially reproduced (rests on an assumption) |
| Layer 5 fires faster than layer 2/3 | Partially reproduced |
| Layer 5 discriminates over more of the maze | Not reproduced |
| Paths diverge at 0.30, head direction at 0.24 | Partially reproduced |
| Side-arm selectivity 40% (layer 5) and 22% (layer 2/3) | Partially reproduced |
| Central-arm selectivity 16% and 18% | Partially reproduced (rests on the unit list) |
| 26% of neurons odor selective during nose poke | Not reproduced |
| Odor preference unrelated to maze selectivity | Not reproduced |
| Little retrospective coding | Reproduced |
| No positive rate-speed relation | Reproduced |
| Connection rates 0.79%, 0.55%, 0.24%, 0.17% | Not reproduced |
| Cell classes 32.5% and 12.5%, ratio 2.82 | Not reproduced |
| Pyramidal-pyramidal excitation 0.12% and 0.27% | Partially reproduced |
| Nearby pyramidal-interneuron probability 1 to 2% | Not reproduced |
| Figure 3b session counts 48 and 30 | Not reproduced |
| Hub of 39 of 117 cells | Not reproduced (the lab's own connection list gives 39) |
| Connection probability falls with distance | Partially reproduced |
| Trajectory-specific pyramidal cells and interneurons | Partially reproduced |
| No spatial clustering on the probe | Reproduced (layer 2/3 session only) |
| 67 of 343 connections position dependent | Partially reproduced (rests on an assumption) |
| 15 of 36 connections selective (Figure 5a) | Not reproduced (rests on an assumption) |
| Pair 156-136 | Not reproduced (rests on an assumption) |
| Pairs 197-201, 49-52, 186-201 | Not reproduced (rests on an assumption) |
| Dependence survives thinning | Reproduced (rests on an assumption) |
| Depression 12.7% and facilitation 10.7% | Not reproduced |
| Cells 197 and 186 onto 201 | Partially reproduced |
| Supralinear coincidence, 14 satellites | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/fujisawa-2008-03.yaml`](../../attempts/fujisawa-2008-03.yaml).

- `reproduce_fujisawa_2008.ipynb`: the analysis. It takes about 40 minutes, most of it the jitter tests and
  streaming the sensor channels.
- `fujisawa.py`: loading both datasets, the permutation test with global bands, the jitter tests for connections
  (both cells or one cell jittered) and for the position of excess coincidences, and the first and later spike test
  (with the shared jitter of both cells, or the presynaptic jitter). Other notebooks on these
  datasets can import it.
