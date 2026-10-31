# Daume et al. (2024) from dandiset 000673

Tests the findings of [Daume et al. (2024)](https://doi.org/10.1038/s41586-024-07309-z), "Control of
working memory by phase-amplitude coupling of human hippocampal neurons", on
[DANDI:000673](https://dandiarchive.org/dandiset/000673/0.240118.2135), version 0.240118.2135, the
version the paper cites. The dandiset holds 44 sessions of a Sternberg working memory task in 36
patients, with 1,454 single neurons and 1,922 microwire LFP channels: every count the paper reports.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claims | Outcome |
|---|---|
| Cohort counts, behaviour (RT, accuracy, false negatives) | Reproduced (4) |
| Category neuron counts; their persistent and selective maintenance activity, overall and by area | Partially reproduced (3) |
| Category neurons fire more in correct trials; no RT effect | Reproduced (2; one rests on rates as % of baseline) |
| Category neurons fire more in load 1 (preferred trials) | Not reproduced (rests on rates as % of baseline) |
| Theta-gamma comodulogram; hippocampal PAC lower in load 3, per channel and per patient; kappa; raw MI; nesting | Reproduced (6; four rest on an assumption) |
| Proportions of PAC channels | Partially reproduced (pre-SMA 17 channels against 5) |
| No load effect in other areas or for low gamma; only hippocampal high gamma in Table S1 | Not reproduced (pre-SMA channels differ) |
| Single-trial PAC predicts RT; spectral slope does not differ | Not reproduced |
| PAC neuron counts | Partially reproduced (8 and 5 against 79 and 163, above chance) |
| PAC controls (Extended Data Fig. 3); spike-field coherence; claims on PAC neurons, noise correlations and decoding | Blocked (34) |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000673-daume-2024-01.yaml`](../../attempts/000673-daume-2024-01.yaml).

- `reproduce_daume_2024.ipynb`: behaviour, category neurons and their maintenance firing (about 4
  minutes).
- `reproduce_daume_2024_lfp.ipynb`: LFP phase-amplitude coupling, under two readings of the
  artefact rejection (about 20 minutes, most of it streaming the LFP and filtering every channel).
- `reproduce_daume_2024_pac_neurons.ipynb`: the PAC neuron selection with its 200 trial shuffles,
  and the firing of PAC neurons (about 8 minutes).
- `sbcat.py`: loading, the category neuron selection of the paper's code, the PAC comodulogram with
  the paper's filters and surrogates, nesting, and the PAC neuron GLMs. Its docstring says where
  each parameter comes from.
