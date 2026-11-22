# Hiraoka and Jo (2025) on DANDI:000044

Tests the findings of T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in
event sequences" (doi:10.1063/5.0296506), on dandiset 000044 version 0.210812.1516, the version the
paper cites: the hippocampal recordings of Grosmark and Buzsaki (2016). The claims are in
`claims/hiraoka-2025.yaml` and the record in `attempts/hiraoka-2025-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_hiraoka_2025.ipynb`: the data check, the paper's representative unit (row 9 of
  session Achilles-10252013), and its bursty trains, merging numbers and power-law fits (Figure 2).
- `other_neurons.ipynb`: the same pattern in every unit of the eight sessions, pyramidal and
  inhibitory (about 45 minutes on 4 processes).
- `other_neurons_cap3.ipynb`: the same test with the power-law exponent capped at 3, the default
  of the locked powerlaw 2.0.0, as a variant (about 11 minutes on 4 processes).
- `model.ipynb`: the paper's two generative algorithms (Section IV, Figure 4), simulated here.
- `bursttree.py`: loading, bursts, merging numbers, fits and the algorithms, with the source of
  each parameter.

The Wikipedia and earthquake sequences of the paper are not tested.

Run with `python tools/entry.py all entries/hiraoka-2025`.
