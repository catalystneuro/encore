# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/draft), which holds
single-unit recordings from M1 of two monkeys before and after MPTP. Only monkey V can be tested:
the monkey L files mark no torque perturbation.

This entry now uses the draft of the dandiset (last modified 2026-10-21 20:16:41 UTC), which was
asked for to test the fixes made after the first attempt. A draft can change. The first attempt
used the published version 0.260518.1819.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| Monkey V cell counts (112 and 159; PTNs 49 and 54; CSNs 31 and 48) | Reproduced |
| Lower resting rate after MPTP in PTNs, not CSNs | Reproduced |
| PTNs fire faster than CSNs at rest | Reproduced |
| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
| Long-latency (m2) triceps EMG larger after MPTP | Reproduced |
| EMG responses longer after MPTP | Partially reproduced |
| m1 EMG much smaller than m2 | Partially reproduced |
| Torque-induced movements slower and smaller after MPTP | Not reproduced |
| Movement latency unchanged | Not reproduced |
| EMG onset unchanged | Not reproduced |
| Monkey L torque responses | Blocked: data missing |
| The detection's false-positive rate, and the 15 claims that rest on the selection of torque responses (prevalence, latency, magnitude, FWHM, directionality, correlations) | Blocked: methods underspecified |
| Trial-by-trial correlations | Blocked: methods underspecified |

The detection of torque responses here has a false-positive rate of 0.23 over the 200 ms epoch,
where the paper's threshold implies 0.01, so the claims that use the selection are blocked; their
analyses still run, and the notebook reports them. The torque command is about four times larger
in most post-MPTP sessions than in most pre-MPTP ones, which bears on every pre against post
comparison of the movements and EMG.

In the draft, the analog streams share the clock of the trials, the angle's sign convention and
the monkey L series names are corrected, repeated files and unit copies are gone, and neurons
recorded across two source files are one unit with the trials of both. The cell counts move from
exactly the paper's (112 and 159) to 115 and 157, within tolerance; every outcome is the same as
in the first attempt.

The attempt records, with the reasons and the differences from the paper's method, are
[`attempts/001636-pasquereau-2013-02.yaml`](../../attempts/001636-pasquereau-2013-02.yaml) (this
version) and [`attempts/001636-pasquereau-2013-01.yaml`](../../attempts/001636-pasquereau-2013-01.yaml)
(version 0.260518.1819).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It took 1.8 min in the latest run (up to 4.5 min in others), most of it streaming the
  439 files of the draft and the units of the 447 files of the earlier version.
- `stretch.py`: loading the files (with the analog streams realigned to the trials where needed,
  and each unit's perturbations taken from its own trials), the spike density functions, response
  detection, directional selectivity, kinematics and EMG measures. Other notebooks on this
  dandiset can import it.
