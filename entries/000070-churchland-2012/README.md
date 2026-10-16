# Churchland, Cunningham, Kaufman, Foster, Nuyujukian, Ryu & Shenoy (2012) from dandiset 000070

Tests the findings of [Churchland et al. (2012)](https://doi.org/10.1038/nature11129) that can be
tested on [DANDI:000070](https://dandiarchive.org/dandiset/000070/0.260528.0919), which holds the
paper's two Utah array datasets (J-array, 2009-09-18, and N-array, 2010-09-23) and eight further
array sessions. The single-electrode datasets, the EMG, the leech and the walking-monkey data are
not in it, nor are the sorted isolations of the array datasets: its units are one per electrode.

| Claim | Outcome |
|---|---|
| The array datasets have 108 conditions and 146 and 218 isolations | Partially reproduced |
| The neural state rotates the same way for all conditions | Reproduced |
| Rotation direction does not depend on reach curvature | Partially reproduced |
| The preparatory state predicts the later state | Partially reproduced |
| The jPCA plane captures about 28% of the variance (typically 20 to 35%) | Reproduced |
| PC2 and PC3 capture 29%, about as much as the jPCA plane | Partially reproduced |
| Three jPCA planes in J-array capture 22, 19 and 12% | Not reproduced |
| Three planes capture 50 to 70% of the variance | Partially reproduced |
| The angle between state and derivative peaks near pi/2 | Reproduced |
| Rotational dynamics fit nearly as well as unconstrained dynamics | Reproduced |
| Rotations up to about 2.5 Hz | Partially reproduced |
| Shuffle controls remove the rotations | Not reproduced |
| PMd and M1 each show rotations (variance captured) | Partially reproduced |
| Rotations are faster in M1 than in PMd | Reproduced |
| A velocity-tuned model shows no rotations | Not reproduced |
| A complex kinematic model shows no rotations | Not reproduced |
| Leech, walking monkey, single-electrode datasets, EMG, generator model, speed task (six claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files have faults that the loader corrects: in nine of the ten files the first entry of
`spike_times_index` wrapped at 65536, and in five Nitschke files the clock restarts at recording
segments, so trials overlap in time and spikes are placed in trials by their storage order. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000070-churchland-2012-01.yaml`](../../attempts/000070-churchland-2012-01.yaml).

- `reproduce_churchland_2012.ipynb`: the analysis. It takes 10 to 15 minutes: streaming spike times
  and hand positions, the shuffle controls refitted per held-out condition, and the simulated
  populations.
- `reach.py`: loading the files with both corrections, condition-averaged rates, jPCA, the shuffle
  controls and the simulated kinematic populations. Other notebooks on this dandiset can import it.
