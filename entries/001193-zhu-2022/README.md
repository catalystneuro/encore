# Zhu, Xu, Lu, Hu et al. (2022) from dandiset 001193

Tests the findings of [Zhu et al. (2022)](https://doi.org/10.1038/s41562-022-01334-6) that can be
tested on [DANDI:001193](https://dandiarchive.org/dandiset/001193/0.240921.1006), which holds the
high-gamma ECoG of ten participants, four blocks each, from two 128-electrode grids.

| Claim | Outcome |
|---|---|
| Ten participants (4 male, 6 female), 256 electrodes each, five with COM and five with NL | Partially reproduced |
| The other 23 findings on the recordings (task timing, responses, electrode selection, violation responses, latencies, spatial layout, frequency bands) | Blocked: data missing |
| Keyword frequencies matched between conditions (stimuli and an outside corpus only) | Reproduced, on an assumed reading of the corpus |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold one z-scored high-gamma matrix per block and an electrode table. They hold no trial
or event times, condition labels, responses or electrode locations, which every analysis of the
paper needs. The stated rate (400 Hz) and unit (volts) do not fit the data, which are consistent
with z scores at the paper's 100 Hz. The attempt record, with the reasons and the findings about
the dataset, is [`attempts/001193-zhu-2022-01.yaml`](../../attempts/001193-zhu-2022-01.yaml).

The keyword frequencies use no data of the dataset: the notebook reads the sentence lists from the
paper's supplement and the bigram counts of the corpus the paper names (Jun Da, Chinese text
computing), pooled over its news and fiction sub-corpora. That site is not versioned.

- `reproduce_zhu_2022.ipynb`: the data check, the participant counts and the keyword frequencies.
  It takes about a minute, most of it streaming the 40 files.
- `ifg_hga.py`: loading and per-file summaries (scale, duplicates, block lengths). Other notebooks
  on this dandiset can import it.
- `keyword_frequency.py`: the stimulus lists of the supplement and the keyword counts of the
  corpus.
