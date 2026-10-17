# Markowitz, Gillis, Jay et al. (2023) from dandiset 000559

Tests the findings of [Markowitz et al. (2023)](https://doi.org/10.1038/s41586-022-05611-2) that can
be tested on [DANDI:000559](https://dandiarchive.org/dandiset/000559/0.260528.0858), which holds the
dLight photometry, MoSeq syllables and closed-loop optogenetic sessions of the paper: 14 DLS and 8
DMS dLight mice, 20 Opto-DA mice and 12 no-opsin controls.

| Claim | Outcome |
|---|---|
| dLight is negatively correlated with velocity at short timescales and positively at long ones | Partially reproduced |
| Syllable-associated dLight differs across syllables (Kruskal-Wallis) | Partially reproduced |
| Syllable identity cannot be decoded from dLight | Reproduced |
| Syllables with more dLight are used more | Reproduced |
| Syllables with more dLight have less predictable outgoing transitions | Reproduced |
| dLight at a syllable instance predicts that syllable's use over the next minutes | Partially reproduced |
| DMS has fewer dopamine transients than DLS | Reproduced |
| DMS dopamine does not predict future syllable use | Not reproduced |
| Opto-DA increases target syllable use more than in controls (log2 fold change) | Reproduced |
| The same, for the change in counts | Reproduced |
| Nine Opto-DA mice are learners | Partially reproduced |
| In learners, change during stimulation predicts change after it | Reproduced |
| Brief Opto-DA does not change movement; 3-s stimulation increases velocity | Blocked: metadata insufficient |
| Spontaneous and food-reward transients are of similar size | Blocked: data missing |
| Figures 3i, 4f (need catch trials) | Blocked: metadata insufficient |
| Figure 1f, 2k, Extended Data 10d, Figures 4b, 4c, 4h and 5 | Blocked: not attempted |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not mark catch trials, the genotype or opsin of a mouse, or the session type, and
they hold fewer photometry sessions than the paper used. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/000559-markowitz-2023-01.yaml`](../../attempts/000559-markowitz-2023-01.yaml).

- `reproduce_markowitz_2023.ipynb`: the analysis. It takes about 13 minutes, half of it streaming
  1,723 files.
- `spontda.py`: streaming the files, the dLight processing and quality criteria of the paper,
  syllable instances, and the closed-loop counts. Other notebooks on this dandiset can import it.
