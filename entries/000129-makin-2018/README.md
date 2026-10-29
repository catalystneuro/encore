# Makin, O'Doherty, Cardoso & Sabes (2018) from dandiset 000129

Tests the findings of [Makin et al. (2018)](https://doi.org/10.1088/1741-2552/aa9e95) that can be
tested on [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444), which holds one
session of monkey I (M1 array, 649 s of sorted-unit spikes with kinematics) from the Neural Latents
Benchmark. The paper compared eight decoders over 49 sessions from three monkeys; the session in
the dandiset is dated 2017-02-02, which is not in the paper's session list. All eight decoders are
re-implemented here from the paper's Methods and code (`makin.py`).

| Claim | Outcome |
|---|---|
| Units per monkey I session after the 0.5 Hz cut, 171 to 413 | Not reproduced (111; no hash units in the file) |
| rEFH (+KF) velocity gain over linear regression, more than twice KFobs's and nearly twice the UKF's | Not reproduced (rests on the Methods kinematics) |
| The dynamic map changes KFlatent little | Reproduced |
| The static rEFH decodes velocity and acceleration best among the other decoders | Reproduced |
| The dynamic map adds about 3 dB to the rEFH's position SNR | Not reproduced (4.45 dB) |
| y is decoded better than x for every decoder and variable | Partially reproduced (23 of 24) |
| Linear regression is the worst decoder | Reproduced |
| Negative R2 only for the UKF and KFlatent (+KF) | Reproduced (no negative R2 at 64 ms) |
| rEFH (+KF) beats KFobs and the UKF for velocity and acceleration in every session | Reproduced for this session |
| Velocity is the rEFH's best-decoded variable | Not reproduced (position is) |
| KFlatent only modestly better than KFobs, the UKF more | Reproduced |
| Velocity losses of the rEFH variants, 0.7 and 0.4 dB | Not reproduced |
| The standard-normal rEFH still beats the UKF | Reproduced (rests on standardized counts) |
| The rEFH's advantage grows with bin width | Reproduced |
| Quality falls and the advantage grows with derivative order | Partially reproduced (3 of 4 widths) |
| The advantage grows with derivative order for each amount of training data | Reproduced |
| Static decoders' position SNR is affine in the fraction of neurons, KFlatent the most curved | Not reproduced |
| Decoders with a kinematic model rise faster, then saturate | Reproduced, only because KFlatent (+KF) diverges with 13 units |
| Tests across the paper's 49 sessions (12 claims) | Blocked: the dandiset holds one session (single-session values are printed for ten of them) |
| Monkey C against monkey I | Blocked: monkey C's data have no archive identifier |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most of the paper's findings are averages or bootstrap tests over its 49 sessions. Here they are
tested on the one session the dandiset holds, and those that need the bootstrap are blocked. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000129-makin-2018-01.yaml`](../../attempts/000129-makin-2018-01.yaml).
