# Moaddab & McDannald (2021) from CRCNS rrf-1

Tests the findings of [Moaddab and McDannald (2021)](https://doi.org/10.1016/j.cub.2021.02.055) on
the CRCNS data set [rrf-1](https://doi.org/10.6080/K04B2ZJ5): 743 single units recorded in the
retrorubral field of 11 rats over 228 fear discrimination sessions, the authors' derived data file
(`cube.mat`) and the paper's MATLAB code. The files are streamed from the public S3 bucket
`crcnsarchive`; CRCNS data sets are not versioned, and the notebook checks the MD5 of `data.zip`.

| Claims | Outcome |
|---|---|
| Counts of units, sessions and rats; the cue-responsive screen; behavior | Reproduced (3) |
| K-means clusters and their characteristics; cue firing (Table 1, Table S1, Figure S4); correlations of Figure 4; threat probability tuning and regressions (Figure 5) | Reproduced (17), resting on the code's normalization |
| Figure 4A to 4C threat bias; Table S3 | Partially reproduced (2) |
| Outcome firing (Table 1, Figure 6) | Reproduced (4), partially reproduced (3), not reproduced (1: k1) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds the paper's code, and the analysis follows it where the claims file left a
method open. The code's k-means run is repeated outside MATLAB and gives the paper's eight clusters
exactly, and most of the paper's counts, F values and correlations are recovered to the printed
digits. The Methods describe a different normalization from the code's; outcomes that use
normalized firing rest on the code's. For k1, k3, k5 and k6 the Table S4 values fit a window of 0
to 4 s after shock offset, not the 0 to 8 s of the Figure 6 gray boxes the claims file uses, which
is why k1 is not reproduced. Bootstrap CIs are judged by the sign they give in most of 20
random draws, since several end within 0.01 of zero. The attempt record, with the reasons and the differences from the
paper's method, is
[`attempts/crcns-rrf-1-moaddab-2021-01.yaml`](../../attempts/crcns-rrf-1-moaddab-2021-01.yaml).

- `reproduce_moaddab_2021.ipynb`: the analysis. It takes about five minutes, most of it redrawing
  the bootstrap CIs.
- `rrf.py`: loading the cube and the unit files, the code's normalization and the Methods'
  variants, MATLAB's k-means with its default generator, the pattern tests for the clusters, the
  bootstrap, the ANOVAs and Meng's Z. Other notebooks on this data set can import it.
