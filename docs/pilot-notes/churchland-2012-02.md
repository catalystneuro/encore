# churchland-2012, Churchland et al. 2012, second attempt

Five claims reproduced, six partially, five not reproduced and six blocked,
all six for missing data; seven outcomes rest on an assumption, five of them
on which movement-onset column the paper aligned on. The first verification
round agreed with 21 of the 22 outcomes and the second with all 22; nothing
was proposed after the second, so there was no third round. The attempt pins
version 0.261122.2046. The paper, Churchland, Cunningham, Kaufman, Foster,
Nuyujukian, Ryu and Shenoy in Nature, reports that the population activity of
premotor (PMd) and motor (M1) cortex in monkeys reaching in a maze task
rotates in the plane found by jPCA, in the same direction for all conditions
and with a phase that follows from the preparatory state, that a rotational
dynamics matrix (M_skew) fits it nearly as well as an unconstrained one, and
that simulated kinematic populations and muscle activity show no consistent
rotations. The claims file is the one churchland-2012-01's author wrote under
pilot-7, from the NIH author manuscript (PMC3393826) and the Supplementary
Information, with the choices the Methods leave open taken from a Python port
of the jPCA codepack (bantin/jPCA at commit 3f8be9f). On the J-array and
N-array datasets, with the 192 unsorted threshold crossings each file holds in
place of the paper's sorted isolations, the direction of rotation (95.4% and
99.1% of conditions counter-clockwise), the angle between the state and its
derivative, the fit of M_skew, the rotation frequency and the faster M1
rotations reproduce; the variance captured by the first jPCA plane (14.9% and
22.9% against 28%), by PC2 and PC3, by the J-array planes and by each array
alone does not, nor does the complex kinematic model, whose angle distribution
does not peak near zero; and the curvature, phase, shuffle, three-plane and
velocity-model claims are partial. The six claims on the leech and
walking-monkey data, the single-electrode datasets, the EMG, the generator
model and the speed task are blocked. The author's first run gave the same
counts with the two model claims the other way round. Round 1 found that the
angle-peak test let any negative peak pass, which made the complex model not
reproduced, and that the simulated switch from preparatory to movement tuning
fell inside the analysed window; the author moved it before the window, chose
this before running it, and the velocity model became partial, with the
earlier timing kept as a reading that gives not reproduced. Round 1 also asked
for the onset columns' descriptions, two variants of the phase test and a
check of the lag between the arrays, all added, and its points that the
shuffle-3 reference cannot test the phase claim, that R2(M_skew) measures
what the supplement does not expect shuffles 2 and 3 to remove, and that "typically 20-35%"
comes from the per-area legend went to a reader in
`questions/churchland-2012.yaml`. Round 2 found five sentences the outputs did
not support, which were corrected, and rated the onset-column finding major,
as it now is. The attempt is recorded as not blind, narrowly: the author saw
nothing of churchland-2012-01 but the claims file's header, which names two
faults that attempt found and says sub-Nitschke ses-20090910 is consistent
with the N-9-10-2010 dataset. The reconciliation traces four of the six
outcomes that differ from churchland-2012-01 (`var-captured-jpc-plane`,
`pc23-variance`, `rotation-frequency` and `suppfig3-shuffle-controls`) to the
`offline_move_onset_time` column the new version adds, `suppfig5-areas-variance`
to an error in the earlier attempt, whose normalisation range took in the
smoothed edge bins of its window, and `fig6-velocity-model` to when the
simulated preparatory term ends. The author's run took about 1 h (23:12 to
00:12 UTC) and nothing failed, though a script that stripped bold from the
markdown damaged one code line, which a diff caught before the final run; the
notebook ran in 9.7 min at first, with peak memory 3.5 GB, 16 min after round
1, 19.5 min after round 2 and 1222 s in the reconciliation.

The dataset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
The Units tables of all ten files hold unsorted threshold crossings, one unit
per electrode (192 per session), as their description says, where the paper
analysed 146 (J-array) and 218 (N-array) sorted single and multi-unit
isolations, which are not in the dandiset; on these units the first jPCA
plane captures 14.9% and 22.9% of the variance, against the paper's average
of 28%. The trial table has two movement-onset columns, `move_begins_time`,
described only as "movement onset time", and `offline_move_onset_time`,
"calculated offline using a robust algorithm", a median of 25 ms (J-array)
and 52 ms (N-array) apart, and nothing says which one the paper aligned on;
the hand speed starts to rise at the offline onset (median 43 and 15 mm/s)
and is already 137 and 160 mm/s at `move_begins_time`, and the choice changes
the outcomes of five claims (in J-array the plane captures 14.9 against
18.7% and rotates at 1.344 against 1.098 Hz). The dandiset holds the paper's
two array datasets (sub-Jenkins ses-20090918 and sub-Nitschke ses-20100923)
and eight further array sessions, one of which, sub-Nitschke ses-20100910,
matches the N-9-10-2010 session of Supplementary Figure 5; the seven
single-electrode datasets, the EMG, the leech and walking-monkey recordings
and the J-11-06-2009 session are not in it, so six of the 22 claims cannot be
tested. Two sessions, sub-Nitschke ses-20100920 and ses-20100922, have no
`maze_condition`, `correct_reach`, `trial_version`, `active_target`,
`proto_trial`, `novel_maze` or `unhittable` columns, so their trials cannot be
grouped by condition; round 2 would rate this minor, as the paper does not use
them, and the author kept it major. Nothing in the metadata or the files says
which sessions are the paper's datasets: every session_description is empty,
the two can be found only by their dates, and the eight others are not
described. The clock checks passed: reach direction decodes at chance from
each array before target onset (0.12 to 0.17 against 0.14 to 0.17 with
shuffled labels) and above it after (0.37 to 0.70), the lag between the
arrays is constant over six blocks of each session, and after target onset
they respond nearly together (M1 lag -4 ms in J-array and 9 ms in N-array),
so the later M1 change around movement in N-array is consistent with a later
M1 response, not a clock offset. No recording is deposited twice, and the
hand, in mm with a conversion to metres, ends a median 9.1 mm (J-array) and
11.4 mm (N-array) from the hit target minus the cursor offset. Of the eight
findings of churchland-2012-01, six are fixed (the wrapped first entry of
`spike_times_index`, the clock restarts and overlapping trials, the hand
position stated in metres but stored in mm, the undescribed cursor offset,
now a `cursor_offset` column, the default Units description and the 2009
session dates of the Nitschke files) and two are still present (the missing
sorted isolations and other datasets, and nothing saying which sessions are
the paper's). Two questions are put to the paper's authors: which movement
onset the array datasets were aligned on and over which times each neuron's
range was taken for the soft normalisation, and, for the kinematic models,
how far the simulated rates led the hand, how the preparatory term evolved
and how the factors were weighted.

The author's points on the protocol: it has no rule for a criterion whose
literal reading passes a case it was not meant for, such as the complex
model's angle peak of -0.97 pi counting as below pi/4, which was applied as
written in the first run; the claims file names `simulate_population`, a
helper from the earlier attempt that the blind checkout lacks, so a model was
written from the Methods under that name; the claims file's header refers to
"the notebook" and the clock resets of the 2010 file from the earlier
attempt, which could not be checked, so the clock was tested anew; it does
not say whether a claim that depends on another's shuffle runs should reuse
them, and the phase claim got its own; and it says "the directory is empty"
where `entries/churchland-2012` did not exist, so it was created.
