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
| Theta-gamma comodulogram; hippocampal PAC lower in load 3, per channel and per patient; kappa; raw MI; nesting | Reproduced (6; three rest on an assumption) |
| Proportions of PAC channels | Partially reproduced (pre-SMA 17 channels against 5) |
| No load effect in other areas or for low gamma; only hippocampal high gamma in Table S1 | Not reproduced (pre-SMA channels differ) |
| Single-trial PAC predicts RT or category neuron firing; spectral slope does not differ; PAC controls of Extended Data Fig. 3 | Not reproduced (4; for the two single-trial claims a change is proposed, see below) |
| PAC neuron counts | Partially reproduced (8 and 5 against 79 and 163, above chance) |
| Spike-field coherence; claims on PAC neurons, noise correlations and decoding | Blocked (32) |

After the second verification, the single-trial GLMs were refitted with load 3 as the reference
level, as Supplementary Tables S2 and S3 code load. Coded so, the category neuron claim
(fig3h-pac-category-firing) meets its criterion under every reading, and the RT claim
(fig2f-rt-single-trial-pac) depends on the RT scale and the single-trial PAC measure, which the
paper does not give. The record keeps the verified outcomes and proposes the changes (reproduced,
and blocked as methods underspecified) for a third round of verification.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000673-daume-2024-01.yaml`](../../attempts/000673-daume-2024-01.yaml).

- `reproduce_daume_2024.ipynb`: behaviour, category neurons and their maintenance firing (4.3
  minutes in the last run).
- `reproduce_daume_2024_lfp.ipynb`: LFP phase-amplitude coupling, under two readings of the
  artefact rejection, and single-trial PAC against category neuron firing (20 minutes in the
  author run and 44 minutes in the last run, over the 30-minute limit, most of it filtering
  every channel and computing the surrogates; the run time depends on the machine).
- `reproduce_daume_2024_lfp_controls.ipynb`: the controls of Extended Data Fig. 3 on the
  hippocampal channels (power, bycycle waveform asymmetry, phase-phase coupling, preferred phase,
  PAC peak frequency; about 23 minutes).
- `reproduce_daume_2024_pac_neurons.ipynb`: the PAC neuron selection with its 200 trial shuffles,
  and the firing of PAC neurons (about 11 minutes).
- `sbcat.py`: loading, the category neuron selection of the paper's code, the PAC comodulogram with
  the paper's filters and surrogates, nesting, and the PAC neuron GLMs. Its docstring says where
  each parameter comes from.
