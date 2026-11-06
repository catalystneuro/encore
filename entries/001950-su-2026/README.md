# Su et al. (2026) from dandiset 001950

Tests the findings of [Su et al. (2026)](https://doi.org/10.1038/s41586-026-11026-0) that can be
tested on [DANDI:001950](https://dandiarchive.org/dandiset/001950/0.260928.2230), which holds the
dynamic foraging behavior, tetrode and Neuropixels recordings of opto-tagged locus coeruleus
neurons, pupil diameter, and fiber photometry of LC-NE axons. The anatomy, transcriptomics and
slice findings (Figures 1 to 3) are not in it.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claims | Outcome |
|---|---|
| Choice, engagement and switch regressions; go-cue excitation; tonic-phasic anticorrelation; baseline before ignored cues; outcome-responsive fraction; RPE and no-reward populations; choice change against RPE; axonal RPE coding; no correlation of outcome coding with anatomical axes; axonal outcome coding more positive than neurons (12) | Reproduced |
| Inter-trial interval; switch coding along anatomical axes; axons against neurons for switch and engagement; outcome coding in space and coefficient angles; waveform space; licks; cross-correlograms; pupil (10) | Partially reproduced |
| Trials per session; tonic modulation against engagement; engagement and switch coding in space; opposing behavior of the two outcome populations (6) | Not reproduced |
| Anatomy, transcriptomics and slice data (10); cortex-projecting neurons (1) | Blocked |

The published version does not mark the paper's LC-NE units or its cortex-projecting units; the
units are selected here with the criteria files of the paper's code (252 units from 21 mice,
against 241 from 19). The draft adds both labels. The Q-learning variables, which the dandiset does
not hold, come from refitting the paper's model per session by maximum likelihood. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/001950-su-2026-01.yaml`](../../attempts/001950-su-2026-01.yaml).

- `reproduce_su_2026.ipynb`: the analysis. It takes about 18 minutes, most of it streaming the files.
- `lcne.py`: loading the files, the unit selection, the trial measures, the spatial tests, the
  Q-learning model and circular statistics. Other notebooks on this dandiset can import it.
