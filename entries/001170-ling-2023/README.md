# Ling, Moss, Smith, Deng, Kroeger, Reimer, Raman & Arenkiel (2023) from dandiset 001170

Tests the findings of [Ling et al. (bioRxiv 2023, v2 2024)](https://doi.org/10.1101/2023.04.24.538157)
that can be tested on [DANDI:001170](https://dandiarchive.org/dandiset/001170/0.260528.1016), which
holds two-photon imaging of olfactory bulb glomeruli in awake mice: seven sessions from four mice
under the paper's block protocol, and five random-order sessions, four of them from other mice. The locust
findings are tested on the recordings the paper deposited on
[Figshare](https://doi.org/10.6084/m9.figshare.31435543.v2).

| Claim | Outcome |
|---|---|
| Seven block sessions in four mice, median 215 glomeruli | Reproduced |
| The dandiset's traces are the paper's deposited traces (198-glomerulus session) | Reproduced |
| Mouse ON-OFF angle above 90 degrees, mean 121.8 | Partially reproduced |
| Mouse ON and OFF responses anticorrelated | Not reproduced |
| A reference odor's ON response is closer to other ON responses than to OFF responses | Partially reproduced |
| Clustering separates ON from OFF responses | Not reproduced |
| Contrast enhancement for methyl salicylate after another odor | Not reproduced |
| Contrast enhancement for acetophenone after another odor | Blocked: data missing |
| Activity after offset stays anticorrelated with the ON response | Not reproduced |
| ITI averages classify the preceding odor | Partially reproduced |
| Time-bin classifier names the odor throughout the ITI | Reproduced |
| Inter-block intervals classified near chance (34.8%) | Blocked: methods underspecified |
| Random-order odors: information declines to chance after offset | Partially reproduced |
| PID kinetics of odor delivery | Blocked: data missing |
| Locust (Figshare): ON-OFF angle above 90 degrees, mean 106.7 | Partially reproduced |
| Locust (Figshare): reference odor ON closer to ON, 5 of 11 significant | Reproduced |
| Locust (Figshare): contrast enhancement for geraniol | Reproduced |
| Locust (Figshare): ITI averages classify the odor | Reproduced |
| Locust (Figshare): time-bin accuracy decays to about 40% | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds raw fluorescence. With dF/F relative to the 2 s before each odor, or F z-scored
on those 2 s, ON and OFF responses are positively correlated and the contrast enhancement is absent.
With traces z-scored within each trial window, close to the arrays the paper deposited, they appear
as the paper reports, but on synthetic data that normalisation produces such anticorrelations by
itself. The ON-OFF angles exceed 90 degrees only because of the centring the paper's code applies,
and the classifiers of the block sessions cannot separate the odor from slow differences between
blocks.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001170-ling-2023-01.yaml`](../../attempts/001170-ling-2023-01.yaml).

- `reproduce_ling_2023.ipynb`: the analysis. It takes about three minutes, most of it streaming the
  fluorescence traces.
- `olfdyn.py`: loading the sessions, rebuilding odor presentations from the 1-s trials rows, dF/F,
  population angles and the k-nearest-neighbour classifiers, and reading the Figshare files. Other
  notebooks on this dandiset can import it.
