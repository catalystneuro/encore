# Laquitaine et al. (2024) from dandiset 001250

Tests the findings of [Laquitaine, Imbeni, Tharayil, Isbister and Reimann (2024)](https://doi.org/10.1101/2024.12.04.626805),
"Spike sorting biases and information loss in a detailed cortical model", on
[DANDI:001250](https://dandiarchive.org/dandiset/001250/0.251012.1648). The dandiset holds the fitted
simulated Neuropixels and dense probe recordings, their ground truth spike times, the in vivo
recordings of Marques-Smith and Horvath, and the paper's sortings of the first 10 minutes.

Of 39 claims, 24 are tested: 7 reproduced, 6 partially reproduced and 11 not reproduced; 15 are
blocked. Blocked are the claims on Buccino's synthetic recording, NS-2X and the 10-minute evoked
recording, whose sortings are not deposited; the curation and feature models, whose quality metrics
need waveforms over the full traces; and the Figure 7 manifold analyses, as the dandiset holds no
stimulus table.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The trace statistics rest on six 10 s blocks of the first 10 minutes of each recording, not on the
whole 10 minutes, except the maxima and amplitude-to-noise extremes, which are streamed over the whole
first 10 minutes. The dense probe depth 1 folder holds a copy of the depth 2 sortings. After the first
verification round three outcomes changed from partially reproduced to not reproduced
(ground-truth-neuron-counts, fig4a-yield-deep-layers, fig5a-evoked-more-units), as their criteria
name no partial outcome.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001250-laquitaine-2024-01.yaml`](../../attempts/001250-laquitaine-2024-01.yaml).

- `reproduce_laquitaine_2024.ipynb`: the analysis, about 45 minutes, most of it streaming traces.
- `spikebias_check.py`: loading, agreement and chance scores, unit quality tags and trace
  statistics, with where each parameter comes from.
