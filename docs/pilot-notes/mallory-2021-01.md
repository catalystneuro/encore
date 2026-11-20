# mallory-2021, Mallory et al. 2021

Nine claims reproduced on the dandiset, seven partially, four not reproduced
and four blocked, two for missing data, one as `metadata_insufficient` and
`supp3-eye-low-false-positives` as too large to run; five of the outcomes rest
on an assumption, four of them on how cross-validation folds are built. The link claim
`headfixed-session-link`, which identifies the paper's 11 head-fixed recordings
among the dandiset's files, reproduced, and the 22 claims on the freely moving
data, moved to the paper's figshare deposits (`data: elsewhere`), are counted
apart: 7 reproduced, 1 partially, 3 not reproduced and 11 blocked as too large.
The first verification round agreed with 21 of the 47 outcomes as they stood,
holding that the freely moving claims, supp3-eye, supp9-eye and supp12 were
blocked for run time only and that the blocks of fig8c and fig8e were not
shown; the second agreed with 46 of 47, the exception being supp12, which the
author had run and proposed as reproduced, and a third round reviewed that one
claim and agreed. The attempt pins version 0.210819.0345, the published
version. The paper, Mallory, Hardcastle, Campbell, Attinger, Low, Raymond and
Giocomo in Nature Communications (12, 671), records medial entorhinal cortex
(MEC) cells with tetrodes in freely moving mice, one cohort with an inertial
sensor for head pitch and roll, and with Neuropixels in head-fixed mice on a
virtual linear track with eye tracking, and reports from a spline
linear-nonlinear (LN) Poisson model that MEC cells encode head pitch, roll and
azimuthal head velocity and eye position and velocity, mostly conjunctively,
with diverse tuning shapes that do not cluster into classes. The claims were
written from the version of record (PMC7844029) with the supplementary legends,
and from the spline LN code at commit 34b470f, which holds none of the pitch,
roll or eye analyses; the claims check made ten corrections, and the answer to
the author's question moved the freely moving claims to figshare and split
supp3, supp4, supp5 and supp9 into a head part and an eye part. Reproduced on
the dandiset are the eye movement ranges, the count of eye-encoding cells (718
of 2861, paper 711, with sections assigned to folds in turn; at random 614),
eye conjunctive coding, the absence of an up or down preference in vertical eye
position cells, the stability of linear horizontal eye position tuning, the
order of contributions (on one held-out section, which fails with random
folds), the model fit (median 0.0513 in the units of compute_llh.m, 0.107 in
bits per spike, a reading put to a reader), the model and raw tuning agreement,
and the simulated control of Supplementary Fig. 12 (eye variables found in 0,
2, 2 and 0 simulated cells). Not reproduced are the temporal preference of
nonlinear eye velocity cells, the eye velocity stability (Ev dot 0.823 above
body speed 0.772, where the paper has it less stable), the absence of
clustering (3 of 30 combinations reach P < 0.005) and the shuffle comparison
for the eye variables (within-cell shuffling finds 0.718 and 0.609 of the Eh
and Ev LN cells). The Figure 8 claims are blocked because the no-landmark
sessions cannot be identified, and the hemisphere comparison because hemisphere
is not recorded. On figshare, head posture distributions and 58 of 179 head
direction cells reproduced, while 37 pitch and 43 roll cells (paper 46 and 53)
and the pitch and roll tuning shapes did not; these Cohort 1 outcomes rest on
one of four readings, an inconclusive clock check and dropping 31% of the bins,
and the Cohort 2 claims would need about 3 h per reading. The author's first
run tested only the head-fixed claims and blocked the 19 freely moving claims
for missing data. The author's run lost a third notebook, for the clipping
reading, to the 2-hour limit on one command, and the author-answers run lost
the Cohort 1 LN model to the 60-minute notebook limit; the model ran in 31.4
min in round 1, with the freely moving notebook's peak memory at 12.06 GB. From
then on each run was split into parts with `entry.yaml` cut down and
`result.json` joined by hand. The clipping reading was never run, nor random
folds on Cohort 1. In round 3 the machine was under outside load, three
notebooks took 72.1, 78.9 and 70.7 min, over the 60-minute limit, the freely
moving notebook was not re-run, and no clean-run stamp was written.

The dataset was converted by CatalystNeuro (Luiz Tauffer of CatalystNeuro is a
contributor). The open field files hold no head pitch, roll or their
velocities, on which the paper's freely moving findings rest; the paper
deposited them on figshare. The dandiset holds 20 head-fixed ecephys files from
9 mice (5120 units) and does not say which are the paper's 11 recordings (2861
units, 8 mice), which can be found only by matching subject, unit and frame
counts to the figshare deposit; the trial tables have no field for the track or
its landmarks, so the no-landmark blocks of Figure 8 (1621 cells in 6 sessions)
cannot be identified, though six of the other nine files, from six mice, sum to
1621 units. In two files the first entry of units/spike_times_index has wrapped
at 2**16, so unit 0 lacks its later spikes and unit 1 begins with them. Eye
position is labelled metres and eye velocity 'unknown', where the values are in
% of the eye width. Hemisphere is not recorded (every electrode location is
'unknown'), no subject has sex or age, and the open field cohorts are not
identified. Ten behaviour-only files repeat the behaviour of ten ecephys files,
and two probe insertions are each converted twice. Two head-fixed sessions have
gaps in the behaviour timestamps of up to 82 s and of 217 and 308 s, and one is
missing 66% of its eye samples. The open field files hold 1200 units from 25
subjects, against 26 mice in the paper, and include arenas of 75 and 91.4 cm
that the Methods do not list. In figshare Dataset 1, head direction is in
radians though the description gives degrees, and two sessions of different
mice have identical body position, speed and head direction over 400,050
samples. Six questions are put to the paper's authors: how sections were
assigned to folds, how contributions were normalised, what rule separates
symmetric from asymmetric velocity cells, which side a cell prefers, which
cells were simulated for Supplementary Fig. 12, and whether out-of-range bins
were dropped or clipped.

The author's points on the protocol: data public elsewhere but not marked
`elsewhere` in the claims file have no fitting blocked reason, so
`data_missing` was used and a reader asked; the rule that a claim depending on
a blocked claim is blocked also blocked the Cohort 2 head velocity count, which
could have been tested; there is no place for deciding which files are the
paper's sessions, so a link claim and `depends_on` entries were added; several
criteria name no partial outcome; conclusions must be written after a costly
run that cannot be repeated in time, so the result cells were added after
execution; and it does not say how to do a run longer than the 2-hour command
limit.
