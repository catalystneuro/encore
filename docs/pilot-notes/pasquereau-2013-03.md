# pasquereau-2013, Pasquereau et al. 2013, third attempt

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset; seventeen are blocked as `methods_underspecified`
and `monkey-l-perturbations` as `data_missing`. Round 1 agreed with 27 of 28
outcomes; it gave `kinematic-latency-unchanged` as blocked, since the
forwards-backwards filter moves movement onsets early (the post-MPTP flexion
mean, 3.05 ms, falls before the command leaves rest at 4 ms), and the author
kept not reproduced and added onset variants, of which only a causal 25 Hz
filter avoids the filter's spread and it also gives shorter latencies after
MPTP (F = 422.5). Round 2 agreed with all 28 and asked that the finding on
torque pulse sizes be raised to major. The author then compared the states at
the two pulse sizes both use and proposed four changes of outcome
(`kinematic-latency-unchanged` and `emg-onset-unchanged` to reproduced,
`emg-duration-longer` to not reproduced, `emg-m1-weak` to reproduced), so a
third round reviewed those four; it agreed with none, as the criteria compare
all sessions and the equal-pulse subsets are small (5 pre-MPTP channel-sessions
near 180 units, 14 post-MPTP near 90), and the outcomes stand with the
proposals on record. It pins version 0.261124.1906, the newest published. The
attempt was blind to `pasquereau-2013-02`, and the reconciliation found no
claim with a different outcome. The paper, Pasquereau and Turner, "Primary
motor cortex of the parkinsonian monkey: altered neuronal responses to muscle
stretch", reports how pyramidal tract and corticostriatal neurons (PTNs and
CSNs) in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP; only monkey V can be tested. The cell
counts (115 and 157 cells, 51 and 54 PTNs, 32 and 48 CSNs), the resting rates
and the faster firing of PTNs than CSNs reproduce; `antidromic-latency` is
partial, as the CSN p = 0.019 is above 0.05/3. The claims file's response
detection crosses its threshold after a pseudo onset in 0.230 of
cell-directions, where the paper implies 0.01, which blocks
`false-positive-rate` and the 15 claims that use the detected responses; the
other readings of the Methods' t-test give 0.465, 0.347 and 0.013, and the last
calls only 0.200 of real cell-directions responsive, so whether the claims file
misreads the t-test was put to a reader in `questions/pasquereau-2013.yaml`.
`trial-correlations` is blocked because the Methods define no single-trial
latency. After MPTP the evoked displacements are faster (+28.1%) and larger
(+14.8%), not slower and smaller, and the movement onset latency is shorter
(F = 709.5, p = 1.5e-102); `emg-m2-larger` reproduces, `emg-duration-longer` is
partial (22.2 and 51.5 ms against 57 and 79 ms), `emg-onset-unchanged` is not
reproduced (44.2 and 25.0 ms) and `emg-m1-weak` is partial (74.0% before MPTP
against the 75% asked). Nothing failed; the notebook ran in 344 s at first,
about 11 minutes after round 1, 838 s after round 2 and 570 s after round 3,
and 851 s in the reconcile run.

The dataset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
The monkey L (Leu) files mark no torque perturbation (major): all 5952 trials
have torque_perturbation_type not_available, the torque command is NaN in 114
files, and in the other 34, all after MPTP, it moves at task events, so the
paper's monkey L torque results (57 of 115 and 35 of 73 responsive cells)
cannot be tested; the dandiset description says so. The torque command's pulse
is larger after MPTP (major), mean 174.7 against 58.4 units and median 181.6
against 45.7, where the paper describes one 0.1 Nm pulse; the units have no
conversion to newton-metres, and the states share only pulses near 90 units
(483 pre-MPTP and 227 post-MPTP perturbations) and near 180 units (41 and
1540), so the kinematic and EMG comparisons over all perturbations cannot
separate the torque from the effect of MPTP. The evoked displacements differ
from the paper's (major): 2.4 to 3.8 degrees where the paper gives a mean of
10, peak velocities of 46 to 75 deg/s, with only 2 of 581 session-directions in
the 130 to 200 deg/s range of the paper's velocity-matched sessions, and
faster (+28%) and larger (+15%) after MPTP where the paper reports -16.2% and
-6.6%; the angle agrees with the 20 degree targets and with ElbowVelocity. In
the Venus files the torque onset follows the centre target by 1.695 to 1.698 s
in 88.4% of 5550 perturbations, where the paper gives 1 to 2 s at random
(minor). The Leu analog series are sampled at 100 Hz where the paper gives 200
Hz, and the Venus EMG is in arbitrary units, both stated in the description
(minor); three Venus sessions (v1401, v1402 and v1501) mark 51 perturbations
with no pulse in the command (minor). Checks that passed: no unit name or
recording repeats across files, is_post_mptp agrees with every file name, the
command leaves rest 4 ms after the marked onset, and twelve files join the
trials of two lab source files without repeating any. In the paper, the
pre-MPTP PTN and CSN resting rates are 16.3 and 3.6 spikes/s in the Results
and 18.3 and 3.2 in Table 1, and Table 1 marks a CSN change p < 0.01 where its
counts give p = 0.54. Two questions are put to the paper's authors: how the
detection t-test was computed, and how the single-trial response latency was
defined. The reconciliation found earlier findings 1 to 7 still present and
added three the attempt had not reported; the conversion code, in an open pull
request at `-02`, is now on main (https://github.com/catalystneuro/turner-lab-to-nwb/pull/33,
merged on 2026-11-24 before the version was published).

The author's points on the protocol: the rule that blocks claims when the
false-positive rate is far from the paper's does not say what happens to the
claim that is the false-positive rate, which was blocked as
`methods_underspecified` with its dependents blocked through `depends_on`; it
does not say whether claims blocked through a dependency show their numbers,
and all were shown as not deciding; breaking down by session when there is one
subject does not fit 291 sessions, so results were broken down by MPTP state;
and archives.md asks for pynwb, but 438 of the 439 files were read with h5py
because building the pynwb objects for every file is too slow.
