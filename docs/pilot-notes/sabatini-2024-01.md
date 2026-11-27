# sabatini-2024, Sabatini et al. 2024

Ten claims reproduced, 13 partially, 11 not reproduced and none blocked; 33
outcomes rest on an assumption, chiefly the trial selection. The first
verification round agreed with 29 of the 34 outcomes as they stood and the
second with all 34; after the second a change to
`fig6e-kinematics-predict-location` was proposed, and a third round reviewed
that one claim and agreed. The record pins version 0.260528.0919; the paper
cites none, and the two published versions list the same assets. The paper,
Sabatini and Kaufman, "Reach-dependent reorientation of rotational dynamics in
motor cortex" (Nature Communications 15:7007), reanalyses Utah array recordings
from M1 and PMd of two monkeys, J and N, making 72 straight and curved maze
reaches, and reports that each condition's activity is a low-dimensional linear
dynamical system (LDS), that its rotations share frequencies of about 0.5, 1.5,
2.5 and 4 Hz across conditions while their planes reorient with the reach, that
the state at movement onset predicts the planes, and that a model built on this
(LDR) encodes and decodes reaches better than standard models. The claims were
written from the version of record (PMC11325044) with its supplement and from
the paper's code, kaufmanlab/LDR-public at commit b65f28d, which loads
preprocessed files that are available only on request and so was not run; the
claims check corrected eight claims and left the reading of Supplementary
Figure 3, the p threshold of Supplementary Figure 8 and the test for Figure 6c
open. Reproduced are the data composition, the single-condition LDS fits
(dimensionality 5, 5, 7 and 5, explaining 85.3 to 94.6%), the variance explained
by the temporal basis factorization (94.1 to 96.9%), the plane alignment, the
segregation of frequencies, the prediction of rotations from rotations and from
the state space location, the location's distinctness from the rotations, LDR
encoding and its advantage over standard encoding models. Not reproduced are
the shared frequencies (median pair frequencies 0.56 to 0.86, 1.55 to 2.38 and,
in M1-N, 3.20 Hz), the near-identical eigenvalues (AUC 0.636 to 0.813 against
0.51 to 0.58), the single LDS over all conditions (78.1 to 82.9% against 46 to
66%), the duration warping, the eigenvalues from kinematics (0.285 against 0.1),
the model comparison of Supplementary Figure 3, which turns on its reading and
went to a reader, the dimensionality of rotation orientations and of the
location, the jPCA variance correlation, and the absence of a drop without the
output-potent dimensions (drops of 3.3 to 7.0 points, p < 1e-12). The other 13
hold in part, among them LDR decoding (two of four datasets in range) and the
decoder comparison, whose GPFA decoders were not run. The author's first run
gave 9 reproduced, 16 partially and 9 not reproduced, with every analysis on
trials with a delay above 400 ms. Round 1 found a kernel penalty that made the
standard kernel encoders predict only the mean, a mean-centring bug in the SNR
dimensionality, a chance level not measured like the data in Figures 3h and 4c,
a units check that checked nothing, and a trial reading chosen for a reason
that was false for monkey N; in reply the analyses moved to all successful
trials, with the other reading in a companion notebook giving the same
outcomes, `data-composition` and `fig5a-frequencies-segregated` moved to
reproduced and `fig3a-eigenvalue-clusters` and `fig3g-basis-frequencies` to not
reproduced, and `fig7c-standard-encoding-worse` stayed reproduced against the
verifier's partial once the penalty was removed. Round 2 asked that two
findings be rated critical and left the segment 3 anomaly open; the reply
traced it to one unit, added a second companion notebook without the three
unstable units, and proposed `fig6e-kinematics-predict-location` as partial,
since M1-N's kernel value rises to 90.9% there, above 89.1%. The round-2
revision left one wrong figure in the notebook summary (0.4% where 1,049 of
196,608 is 0.5%), as a full run would not have finished before the cutoff; the
attempt record gives the correct count. The author's run took about 3 h 15 min
of the 5 h, with three clean notebook runs of about 29 minutes each; the last
run of all three notebooks took 103 minutes.

The dataset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
The Nitschke file joins five recording segments whose clocks overlap, and no
metadata says so: trial start times, hand timestamps and every unit's spike
times jump backwards four times (hand timestamps span 5.4 to 6075.4 s, 6074.2
to 12075.9 s, 6070.6 to 12493.5 s, 6119.8 to 13515.2 s and 6073.5 to
6656.8 s), so a trial's spikes cannot be selected by time alone; splitting at
the jumps and assigning trials to segments in file order gives condition
decoding of 0.44 to 0.50 in segments 0 to 2. In the Jenkins file, unit 1's row
holds two spike trains one after the other, and the first, 196608 spikes from
4259.1 s, begins 55 ms after unit 0's train stops at 4259.0 s, so unit 1's row
appears to hold the rest of unit 0's train; only the unsorted order of the
spike times shows it. Both were rated critical. The units table holds 96 units
per array, exactly one on each of the 192 electrodes, with no column for single
or multi-unit, sorting quality or isolation, where the paper reports 79 to 118
single and stable multi-units per array; whether these are threshold crossings
or sorted units merged per electrode is not stated, and the record notes that
per-electrode units may give smoother, lower-dimensional activity, which would
raise every variance explained. In the Nitschke file unit 170 fires at a mean
of 175.2 spikes/s in segment 3, above 100 spikes/s on 229 of its 532 trials,
against 27.6 to 40.4 spikes/s elsewhere, with nothing marking it; it lowers
condition decoding within segment 3 to 0.179, and 0.425 without it. Hand,
cursor and eye positions are labelled meters with a NaN conversion but hold
millimetres, and the dataset holds no EMG, so Supplementary Figure 8 was run on
the kinematic dimensions only. Seven questions are put to the paper's authors:
which trials were analysed (all successful trials give 1595 and 2121, against
1469 and 2014), which units were used, the penalty for the OU kernel encoders,
how the noise excursion angles of Figure 4c were computed, whether the
Supplementary Figure 3 values were cross-validated, the span of the time
shuffle, and the scale of the kinematic basis functions and the units and
training size of the OU kernel decoders.

The author's points on the protocol: running every reading of a choice that
applies to every claim would double a 30-minute notebook; five seeds on every
random null multiply run time, so the eigenvalue nulls used 100 repeats instead
of 500; the clock check does not cover a file of segments with overlapping
clocks; any edit after the conclusions forces a full re-run of about 30
minutes, which the time guidance does not mention; some criteria have no
partial clause; the direction of a signed-rank result is undefined when median
and mean disagree; and the files were read with h5py, not pynwb as
archives.md says.
