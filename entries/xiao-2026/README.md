# xiao-2026

Reproduction of Xiao, Severson et al. (2026), "Peri-head distance coding in the mouse brainstem"
(Neuron, doi:10.1016/j.neuron.2026.05.027), on DANDI:001687 version 0.260821.2126.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_xiao_2026.ipynb`: the notebook, one section per tested claim.
- `prv.py`: streaming loader, per-pass rates, the paper's unit classification, the MCC, SVM and
  single-neuron decoders, mean waveforms from the raw voltage (unit depth, an approximate SNR and a
  waveform-stability proxy for the whisker-cutting sessions), the Methods' duplicate-unit rule, the
  whisker-cutting pass split, and a runner for the paper's circuit model at commit b1a9f3c.

The record of outcomes is `attempts/xiao-2026-01.yaml`.
