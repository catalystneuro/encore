# 000620-watters-2026

Reproduction of Watters, Gabel, Tenenbaum and Jazayeri (2026), "Working Memory of Multi-Object Scenes
in Primate Frontal Cortex" (doi:10.64898/2026.01.27.702062), on DANDI 000620 version 0.261019.2000.

- `reproduce_watters_2026.ipynb`: data check, behaviour, unit counts, selectivity, signal and noise
  correlations, and the timing of the encoding-model fits.
- `decoding_watters_2026.ipynb`: the decoders of Extended Data Fig. 3.
- `decoding_variants_watters_2026.ipynb`: variants of those decoders that are not the code's
  (z-scored inputs; Ring decoders without the output sigmoid), which decide no outcome.
- `wm.py`: loading (streamed from DANDI) and measures, with the source of each parameter.

The outcomes are in `attempts/000620-watters-2026-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
