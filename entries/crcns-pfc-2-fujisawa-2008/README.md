# Fujisawa, Amarasingham, Harrison & Buzsaki (2008) from CRCNS pfc-2

Tests the findings of [Fujisawa et al. (2008)](https://doi.org/10.1038/nn.2134) on
[CRCNS pfc-2](https://doi.org/10.6080/K01V5BWK), which holds the prefrontal spikes, correct trials
and positions of 13 working memory sessions of three of the paper's four rats (EE, FF and GG; rat
H is not in it), and, in each session's archive, the raw sensor channels of the nose-poke. The layer 5 session of the paper's Figure 2a and Supplementary Figure 11 is not in
the data set; the layer 2/3 session of Figures 2a, 3 to 6 (EE.188) is, with the authors' own list
of its connections.

| Claim | Outcome |
|---|---|
| 633 units recorded | Partially reproduced |
| Mean performance 91.9% | Partially reproduced (one session, from the nose-poke sensors) |
| 10% (layer 2/3) and 20% (layer 5) of cells active per 100 ms | Partially reproduced |
| The population fires uniformly over the maze | Not reproduced |
| Firing width 0.27 +- 0.17 of the maze | Reproduced |
| Paths diverge at 0.30, head directions at 0.24 | Partially reproduced |
| Side-arm selectivity, 40% (layer 5) and 22% (layer 2/3) | Not reproduced |
| Central-arm selectivity, 16% and 18% | Not reproduced |
| 26% of cells odor selective | Not reproduced |
| Odor preference unrelated to arm selectivity | Not reproduced, resting on an assumption |
| Few cells code the previous trial | Reproduced |
| Connection counts (0.79%, 0.55%, 0.24%, 0.17%) | Not reproduced |
| Cell type fractions and ratio | Not reproduced |
| Pyramidal to pyramidal connections | Not reproduced |
| Connections of the Figure 3b session | Not reproduced |
| Hub of 39 of 117 cells | Not reproduced |
| Connection probability falls with distance | Partially reproduced |
| 1 to 2% nearby pyramidal-interneuron connections | Not reproduced |
| Most connected cells are trajectory specific | Partially reproduced |
| Left and right cells are not clustered | Reproduced |
| 67 of 343 connections are position dependent | Not reproduced |
| 15 of 36 connections selective in the Figure 5a session | Not reproduced |
| Pair 156-136 transmits between 0.4 and 0.6 | Partially reproduced |
| Example pairs of Figure 5b | Not reproduced |
| Position dependence survives thinning | Not reproduced |
| Depressing (12.7%) and facilitating (10.7%) pairs | Not reproduced |
| Cells 197 and 186 depress and facilitate onto 201 | Partially reproduced |
| Supralinear effect of coincident inputs | Not reproduced |
| No positive rate-speed relation | Reproduced |
| Population vector width 0.18 and 0.27 | Reproduced, resting on an assumption |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-pfc-2-fujisawa-2008-01.yaml`](../../attempts/crcns-pfc-2-fujisawa-2008-01.yaml).

- `reproduce_fujisawa_2008.ipynb`: the analysis. It takes about 22 minutes: under 3 minutes to
  stream the files (the whole 2.4 GB EE.188 archive is read as a stream, for the example file and
  the nose-poke sensor channels), 5 minutes for the jitter cross-correlograms of 40,240 cell pairs,
  and the rest for the coincidence and spike-order tests.
- `pfc2.py`: loading the sessions from the bucket, the position PSTHs, the permutation test with
  global bands, the jitter test for connections, and the coincidence, thinning and spike-order
  measures of the Methods. Other notebooks on this data set can import it.
