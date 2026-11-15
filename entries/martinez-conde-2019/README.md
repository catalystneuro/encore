# Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019) from CRCNS pvc-12

Tests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)
on [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T), which holds per neuron and stimulus the spike
rate maps of V1 neurons of two monkeys viewing the Square and Edge, Star and Corners stimuli, and
the stimulus images. The spike times and eye positions behind the maps are not in it.

| Claim | Outcome |
|---|---|
| Neuron counts (58 neurons; 25, 30 and 28 per stimulus) | Not reproduced |
| Spikes per condition (mean 35,998) | Blocked: data missing |
| No difference in baseline across stimuli | Not reproduced |
| Midpoint responses above baseline, more so for sharper folds | Reproduced |
| Midpoint spike rate difference per fold (Table 1) | Partially reproduced |
| S40 > S90, S40 > P180, S52 > P180 | Reproduced |
| Average maps increase with sharper corners | Reproduced |
| Table 1, Edge, P180, S90, S52, S40 | Not, partially, not, partially, reproduced |
| Midpoint represents the whole fold | Reproduced |
| RMS contrast along the Edge and its exponential fit | Not reproduced |
| P180 like a 50% and S40 like a 90% contrast Edge | Not reproduced |
| P180 below the 94% Edge, S40 above the Edge below 68% | Reproduced |
| Non-linear relation of response to angle | Reproduced |
| Similar to the DOG model of reference [3] | Blocked: data missing |
| Responses peak near 60 ms latency | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds 53 cells and 77 maps, where the paper analysed 58 neurons and 83 maps, and only
60 of the maps carry the authors' registration to the stimulus; the Star results rest on 12 of the
paper's 30 neurons. The baseline comparison and the Table 1 Edge and S90 outcomes depend on where
the baseline squares are placed; the notebook shows both placements the Methods allow and the
files' own undocumented baseline. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/martinez-conde-2019-02.yaml`](../../attempts/martinez-conde-2019-02.yaml).

- `reproduce_martinez_conde_2019.ipynb`: the analysis. It takes about two minutes, most of it
  streaming the zip and matching each registered map to its gaze-frame map.
- `vasarely.py`: loading the zip in place, the fold geometry read from each file's own polygons,
  the midpoint, block, baseline and Edge measures. Other notebooks on this data set can import it.
