# Scala, Kobak et al. (2021) from dandiset 000035

Tests the findings of [Scala, Kobak et al. (2021)](https://doi.org/10.1038/s41586-020-2907-3)
that can be tested on [DANDI:000035](https://dandiarchive.org/dandiset/000035/0.211014.0808),
which holds the paper's follow-up Patch-seq recordings at physiological temperature: 185 neurons
of mouse motor cortex, mostly layer 5 Sst and excitatory cells. The paper's main data set,
recorded at room temperature, is in dandiset 000008 and is not tested here.

| Claim | Outcome |
|---|---|
| Figures 1 to 5 and Extended Data Fig. 5: the main data set (nine claims) | Blocked: data missing |
| Cohort at 34 degrees: cells, mice, t-types, layers | Reproduced |
| Stimulus: 600 ms steps from -200 pA in 20 pA increments up to 1,380 pA | Partially reproduced |
| IT and ET neurons overlap electrophysiologically at 34 degrees | Reproduced |
| AP threshold differs between layer 5 IT and ET at 34 degrees | Reproduced |
| The files are the cells of the paper's published table (with the paper's table) | Partially reproduced |
| Features from the traces agree with the published ones (with the paper's table) | Reproduced |
| Sst t-types keep their relative differences between 25 and 34 degrees (with the paper's room-temperature features) | Reproduced |
| Transcriptomic and electrophysiological distances of Sst t-types correlate at 34 degrees | Blocked: not tested (the reference expression data are public, but fetching them takes about 10 to 55 minutes depending on Zenodo's rate) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The features are computed by a re-implementation of the paper's extraction, which gives the
published values for most cells. The attempt record, with the reasons and the differences from
the paper's method, is
[`attempts/000035-scala-2021-01.yaml`](../../attempts/000035-scala-2021-01.yaml).

- `reproduce_scala_2021.ipynb`: the analysis. It takes about three minutes, including a timed request to Zenodo.
- `scala34.py`: streaming the files, the 17 electrophysiological features, the paper's
  representation and its nearest-neighbour family classifier. Other notebooks on this dandiset
  can import it.
