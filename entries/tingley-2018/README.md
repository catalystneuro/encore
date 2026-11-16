# Tingley and Buzsaki (2018) on DANDI:000213

Tests the claims of Tingley and Buzsaki (2018), "Transformation of a Spatial Map across the
Hippocampal-Lateral Septal Circuit" (Neuron 98, 1229-1242), on dandiset 000213 at version
0.261109.2219, streamed from the archive.

- `reproduce_tingley_2018.ipynb`: one notebook for all claims. It loads every session, reduces it to
  the spikes within trials with their linearized position, CA1 theta phase, instantaneous rate and
  running speed, then tests each claim. It runs in about 55 minutes on 4 CPUs.
- `tingley.py`: loading and the reusable measures (maps, the single-cell decoder, place fields,
  Olypher information, circular statistics, LFP coherence and coupling, ensemble decoding, peer
  prediction). Its docstring says where each parameter comes from.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The outcomes and their reasons are in `attempts/tingley-2018-02.yaml`.
