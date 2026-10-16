# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.260518.1819), which holds
single-unit recordings from M1 of two monkeys before and after MPTP. Only monkey V can be tested:
the monkey L files mark no torque perturbation.

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

The detection of torque responses here has a false-positive rate near 0.2 over the 200 ms epoch,
where the paper's threshold implies 0.01, so the claims that use the selection are blocked; their
analyses still run, and the notebook reports them. The analog streams are stored on a clock that
drifts behind the trials table and are realigned here. The torque command is about four times
larger in most post-MPTP sessions than in most pre-MPTP ones, which bears on every pre against
post comparison of the movements and EMG.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001636-pasquereau-2013-01.yaml`](../../attempts/001636-pasquereau-2013-01.yaml).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It took 2.4 min in the latest run, most of it streaming the
  447 files.
- `stretch.py`: loading the files (with the analog streams realigned to the trials), the spike
  density functions, response detection, directional selectivity, kinematics and EMG measures.
  Other notebooks on this dandiset can import it.
