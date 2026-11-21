# Souza et al. (2026) from dandiset 000713

Tests the findings of [Souza et al. (2026)](https://doi.org/10.3389/fnbeh.2026.1944695), "Reward
coding across mouse visual cortical areas", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Visual Behavior
Neuropixels dataset, which the paper reuses. The notebook rebuilds the paper's reward-modulated
cohort of visual-cortex units and tests its composition by area, waveform class and layer, the
reward modulation index, the cohort's population variability, the archetype decomposition of its
peri-reward profiles, and the behavioural numbers.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Of 38 claims, 17 are reproduced, 15 partially reproduced and 6 not reproduced; the attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/souza-2026-01.yaml`](../../attempts/souza-2026-01.yaml).

- The paper's 103 sessions and 54,039 units fit the 104 sessions of the dandiset's Sst-Cre and Vip-Cre
  mice with units of quality "good" and presence ratio >= 0.95 (54,045 units); this selection is an
  assumption.
- The split-half null uses 100 permutations per unit in place of the paper's 1,000, to fit the run
  time.
- The layer claims use BrainGlobe's packaging of the Allen CCFv3 25 um annotation volume (GIN
  brainglobe/atlases at commit 78272d68), an outside input.

Files:

- `reproduce_souza_2026.ipynb`: the analysis. It takes about 40 minutes, most of it streaming the
  spike times of 104 sessions in six processes.
- `vbn.py`: loading the session files, the per-session reduction (peri-reward histograms, the
  split-half test and its null, the cross-condition tests, population counts, waveform measures),
  and the layer lookup. Other notebooks on this dandiset can import it.
