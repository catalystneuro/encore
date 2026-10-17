# The IBL brain-wide map (2025) from dandiset 000409

Tests the findings of [International Brain Laboratory et al. (2025)](https://doi.org/10.1038/s41586-025-09235-0)
on [DANDI:000409](https://dandiarchive.org/dandiset/000409/0.260309.1324), which holds 459 sessions of
Neuropixels recordings from 139 mice performing the IBL decision-making task.

| Claim | Outcome |
|---|---|
| Dataset composition: sessions, mice, labs, probes, units, well-isolated units, canonical regions, brain areas, sex, probe versions, trials per session (8 claims) | Reproduced |
| Age and weight of the mice | Partially reproduced (weight yes, age no) |
| Receptive-field mapping | Blocked: data missing |
| 81.4% correct; 22.8% of first movements under 80 ms | Reproduced |
| 58.7% correct at 0% contrast, t138 = 20.18 | Not reproduced (mean 0.44 points below the paper's) |
| Figure 1d to 1h: contrast, end of session, block switch, block bias | Reproduced |
| Stimulus decodable in fewer regions, VISp | Reproduced (10 regions) |
| Choice decodable in more regions than stimulus, GRN | Reproduced (10 regions) |
| Feedback decodable in nearly all regions | Partially reproduced (7 of 10) |
| Single-cell stimulus and choice selectivity | Blocked: methods underspecified (false-positive rate) |
| Visual latencies LGd < VISp = LP < VISpm < VISam | Not reproduced |
| Later latencies in IRN and GRN (100 to 120 ms) | Reproduced |
| About 10 Hz feedback oscillation tied to licking | Partially reproduced (7 Hz) |
| Stimulus trajectories significant in 104 regions | Not reproduced (46 of 201) |
| Whole-brain analyses: wheel speed, encoding, video, Granger (4 claims) | Blocked: not attempted |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The decoding, single-cell and latency claims are tested on a set of 14 regions fixed in advance,
each with all its sessions, with fewer cross-validation repeats and null sessions than the paper, to
fit the time limit. The stimulus trajectories are computed for all 201 canonical regions. In 64
sessions the block column (`probability_left`) alternates on every trial and does not describe the
blocks; analyses that need blocks leave these sessions out. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/000409-ibl-2025-01.yaml`](../../attempts/000409-ibl-2025-01.yaml).

- `reproduce_ibl_2025.ipynb`: the analysis. It took 25.0 minutes in the last run, and the time
  varies with streaming speed: 3.6 to scan the 459 processed files, 1.8 to stream the spikes of the
  14 regions in 168 sessions, 11.8 to stream every canonical unit of the 454 canonical sessions for
  the trajectories of all regions and the clock check, 4 to decode and 1.8 for the nested null of VISp.
- `bwm.py`: streaming, the paper's unit and trial inclusion, decoding with pseudo- and synthetic
  null sessions, the single-cell test and the population trajectories. Other notebooks on this
  dandiset can import it.
