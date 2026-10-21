# Chen, Li, Daie & Svoboda (2017) from dandiset 000015

Tests the findings of [Chen et al. (2017)](https://doi.org/10.1016/j.neuron.2017.05.005) that can be
tested on [DANDI:000015](https://dandiarchive.org/dandiset/000015/0.220126.1914), which holds the
two-photon imaging of 105 image planes in left ALM and MM of six mice (each plane deposited twice),
with PT and IT labels in three mice. The plane depth, wide-field imaging, whisker tracking,
photoinhibition and silicon probe recordings are not in it.

| Claim | Outcome |
|---|---|
| Early-lick trials, 13.3% +- 10% | Reproduced |
| Imaging sample: mice, planes, trials and performance per plane | Partially reproduced (locations not identifiable) |
| Trials per type per plane | Reproduced |
| 15,431 neurons, 8,837 in ALM and 6,594 in MM | Reproduced |
| 31% of ALM and 23% of MM neurons selective | Not reproduced |
| Most selective neurons code one variable at a time | Reproduced |
| Lick-direction coding in different epochs | Reproduced |
| Object-location coding in sample and delay | Reproduced |
| Outcome selectivity begins after the answer lick | Not reproduced |
| Mixed selectivity mainly in the response epoch | Reproduced |
| Object location mainly in MM early in the trial | Reproduced |
| Lick-direction selectivity peaks after the go cue, minor in MM | Partially reproduced (depth part not testable) |
| Outcome neurons only after the go cue, uniform over ALM and MM | Not reproduced |
| Preparatory activity in ALM, object location in MM | Reproduced |
| Peak of activity shifts from MM to ALM | Not reproduced |
| 719 PT and 2,631 IT neurons, PT only deep | Partially reproduced (counts only) |
| ALM PT neurons prefer contralateral licking in the delay | Not reproduced |
| PT selectivity earlier than IT by 1.4 s | Not reproduced |
| MM neurons prefer the posterior pole | Not reproduced |
| Error-preferring neurons outnumber correct-preferring | Partially reproduced |
| Under 20% of ALM PT or IT cells lick-direction selective at a time | Reproduced |
| Tagged units of Li et al. (2015) on DANDI:000010 (link) | Reproduced |
| Four findings on depth | Blocked: metadata insufficient |
| Wide-field imaging (two), photoinhibition, whisking | Blocked: data missing |
| Silicon probe recordings (two) | Blocked: never made public |
| PT and IT onset in Li et al. (2015) units | Blocked: methods underspecified (question asked) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several of the outcomes not reproduced find the effect in the stated direction but below a bound the
claims file fixed (2 bootstrap SD), or turn on rules that count neurons selective in any single time
bin, which chance bins dominate. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000015-chen-2017-01.yaml`](../../attempts/000015-chen-2017-01.yaml).

- `reproduce_chen_2017.ipynb`: the analysis. It takes about twelve minutes, most of it streaming the
  210 files.
- `chen2017.py`: loading, deduplication of the doubled files, dF/F per trial, the 3-way ANOVA and
  coefficients of the paper's Methods, onsets and the hierarchical bootstrap. Other notebooks on
  this dandiset can import it.
