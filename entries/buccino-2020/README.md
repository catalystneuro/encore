# Buccino et al. (2020) on dandiset 000034

Tests the findings of Buccino et al. (2020), "SpikeInterface, a unified framework for spike
sorting" (eLife 9:e61834), on [DANDI:000034](https://dandiarchive.org/dandiset/000034/0.211030.0713)
version 0.211030.0713.

The dandiset holds the four recordings the paper sorts and the two manual curations of its
Kilosort2 output. The notebook checks that the recordings are as the paper describes them, that
the curated and ground-truth spike times share the clocks of their recordings, and compares the
two curations with each other (226 shared units of 351, as in the paper; partially reproduced, as
the 174 Kilosort2 units both curators discarded need the Kilosort2 run). The findings about sorter
outputs are blocked: the dandiset holds no sorter output, and three of the six sorters need MATLAB
(one also a GPU), which this runner lacks.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_buccino_2020.ipynb`: the notebook.
- `si000034.py`: loading, the clock check and the curation comparison.
