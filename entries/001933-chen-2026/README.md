# Chen, He et al. (2026) from dandiset 001933

Tests the findings of [Chen, He et al. (2026)](https://doi.org/10.1038/s41467-026-75194-3) that can be tested on
[DANDI:001933](https://dandiarchive.org/dandiset/001933/0.260825.1457), which holds the fiber photometry of Figure 6
and Supplementary Figures 7 and 8: GRAB-DA3m in the dorsal striatum during optogenetic stimulation of Anxa1+ (15 mice)
or Calb1+ (12 mice) SNc dopamine neurons, in LRRK2-WT and LRRK2-G2019S mice. The imaging, proteomics and western blots
of Figures 1 to 5 are not in it.

| Claim | Outcome |
|---|---|
| The paper's source data can be recomputed from the dandiset | Not reproduced (Anxa1 links; Calb1 does not) |
| Anxa1 evoked release lower in G2019S at 0.5 mW | Reproduced |
| 7 of 8 Anxa1 G2019S mice reduced, 3743 not | Reproduced |
| Anxa1 reduction at all four powers | Reproduced |
| Anxa1 spontaneous transients smaller in G2019S | Reproduced |
| 6 of 8 Anxa1 G2019S mice with smaller transients | Partially reproduced |
| Calb1 spontaneous transients not reduced | Reproduced (p = 0.051, at the threshold) |
| Calb1 evoked release reduced at four powers | Reproduced |
| Only 2 of 7 Calb1 G2019S mice reduced | Partially reproduced |
| Cohen's d larger for Anxa1 (2.05) than Calb1 (0.76) | Not reproduced |
| Figures 1 to 5 (eight claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences
from the paper's method.

The Anxa1 recordings are those behind the paper's figures: its published traces equal the dandiset's dF/F. The Calb1
dF/F in the dandiset is not the one behind Supplementary Figure 8, so the Calb1 results here are of the dandiset's
processing. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001933-chen-2026-01.yaml`](../../attempts/001933-chen-2026-01.yaml).

- `reproduce_chen_2026.ipynb`: the analysis. It takes about three minutes, most of it streaming the files.
- `lrrk2.py`: loading the files, the evoked and spontaneous measures of the paper's Methods and code, the dF/F
  recomputed from the raw signal, and the paper's source data. Other notebooks on this dandiset can import it.
