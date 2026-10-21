# Nagelhus, Andersson, Gonzalo Cogno, Moser & Moser (2023) from EBRAINS 10.25493/Q0FG-1X8

Tests the findings of [Nagelhus et al. (2023)](https://doi.org/10.1016/j.neuron.2023.04.008) on
[EBRAINS:Q0FG-1X8](https://doi.org/10.25493/Q0FG-1X8), version v1. The dataset holds spike times and
tracking of CA1 and CA3 cells in rats foraging in an open field with and without an object, from
tetrodes and Neuropixels probes. Its single-cell files give each cell once. Its population files give
the No Object and Object trials of the 16 decoding sessions.

The outcomes, with the reasons and the differences from the paper's method, are in the attempt record
[`attempts/ebrains-q0fg-1x8-nagelhus-2023-01.yaml`](../../attempts/ebrains-q0fg-1x8-nagelhus-2023-01.yaml).
Many claims are blocked because the readings of a method detail that the claims file does not fix
give different outcomes; the questions are in
[`questions/ebrains-q0fg-1x8.yaml`](../../questions/ebrains-q0fg-1x8.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

What the attempt found about the dataset: in the two Neuropixels population files the y coordinate
of the tracking is a copy of x. The CA1 single-cell file holds the correct tracking of the same
recordings, and the decoding notebooks use it. The CA3 file holds 341 cells, against the paper's 313.
There are no cell identities across days, no implant sites and no head direction.

- `01_single_cells.ipynb`: the data check of every file; object tuning, firing fields, whole-trial changes.
- `02_single_cell_changes.ipynb`: the within/between-trial classification and object traces.
- `03_population_decoding.ipynb`: the Bayesian decoder and its controls.
- `04_distance_tuning.ipynb`: single-cell distance tuning and the cell properties that predict it.
- `05_subsets.ipynb`: decoding with random subsets of cells.
- `06_words.ipynb`: words and counts.
- `objcode.py`: loading (streamed from the EBRAINS data proxy), rate maps, fields, template
  matching, the decoders and the information measures. Other notebooks on this dataset can import it.
