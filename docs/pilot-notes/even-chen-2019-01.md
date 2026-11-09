# 000121, Even-Chen et al. 2019

Six claims reproduced, seven partially, six not reproduced and one blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it
disagreed on `pca-variance`, where R's PC1 is 72.8% against a lower bound of
72.9%, and the author changed that claim from partially reproduced to not
reproduced, following the criterion's letter. The author also changed
`plane-timecourse` from reproduced to partially reproduced, because R's
divergence cannot be told from baseline noise; round 2 accepted this as a
judgment beyond the criterion and agreed with all 20 outcomes, and nothing
was proposed, so there was no third round. The paper reports the structure
and variability of delay activity in the dorsal premotor cortex (PMd) of two
monkeys, J and R, reaching to targets in four configurations: a plane in the
population activity that maps target position, its time course, how trial to
trial deviations along and off the plane relate to reach kinematics, and SVM
decoding of target direction and distance. The session configurations, trial
counts, delays and reaction times, the task-correlated channels, the PCA and
plane variance, the plane's time course, the on- and off-axis deviations, the
speed and distance axes, the ellipse orientation and the decoding errors were
tested on all 7 of R's sessions and 5 of J's 16; the claim that J's sessions
are complete is blocked as `data_missing`. Some outcomes rest on weak ground:
in `distance-error-and-plane-projection` R's full error is inside its bound by
0.001 cm, and projection brings the error to the level of the direction
errors for 1 of 6 rings, or 2 of 6 with the Figure 4d inset's restriction; in
`delays-and-times` R's mean reaction time matches only with the 5.9% of trials
whose onset precedes the go cue kept; the pooled counts of
`speed-axis-within-distance` rest on pooling sessions; and
`relative-deviation-decreases` comes mainly from dividing by distance, so the
test discriminates little.

The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
In every file the units' electrode_group labels are swapped: units 0 to 95 are
labelled PMd but point to electrode rows of the M1 group, and units 96 to 191
are labelled M1 but point to the PMd rows; the data agree with the electrodes
column, and in R the array labelled PMd has 29 silent channels and carries
almost no target information, as expected of the M1 array the paper calls
unusable, so units 96 to 191 were analysed as PMd. In every J file the
boundary between units 0 and 1 in units/spike_times_index is misplaced, so
unit 0 stops 1323 to 3120 s into sessions of 3083 to 8106 s and unit 1 holds
two to five times the median number of spikes, with spike times that restart
near 0. The dandiset holds 5 of the 16 sessions the paper uses for J, with all
four horizontal sessions missing, and the paper's own data link returns HTTP
403. Hand, cursor, eye and decoded positions are stated in meters with
conversion NaN but are in mm; task_id is 2 in every trial, so the target
configuration must be inferred from target_pos, which has no unit; electrode
positions are NaN and impedances -1. The files place R's horizontal targets on
2017-01-15 and 16 and vertical targets on 2017-01-17 and 18, the reverse of
the Methods, and R's trial counts match the Methods better when grouped by the
files' geometry. Other findings: the description of is_successful is wrong;
the dandiset description says sorted spikes, but the units are threshold
crossings, one per electrode; the archive's assetsSummary gives 15 files and
187.5 GB for a version of 12 files and 39.5 GB; R's horizontal targets lie at
5.2 + 10.4 k mm, and R's 2017-01-17 session holds 69 successful trials to ring
targets outside its layout; R's delays run to 1000 ms and R has 26 trials
without a delay, against 900 ms and 10% in the Methods; R's 3-rings session
holds 1340 successful delayed trials where the paper used 912, with no
selection stated; in R's 2017-01-19 the cursor differs from the hand by more
than 1 m in over 1% of samples; the paper prints R's distance errors in an
order that contradicts its text; and the paper names no analysis code and
reports neither its SVM hyperparameters nor the nulls of its p-values.

The author read the conversion code to interpret the files, as no analysis
code is published. Untracked files in the repository root that the author
did not create were left alone. The author's points on the protocol: a
criterion that names no outcome for a result it does not cover; a paper
uncertainty (SEM over cross-validation folds) that does not fit a repeat; no
guidance when the data contradict a label that every claim depends on; no
rule for one subject's data being partial; p-values with no stated null; no
finding kind for the Methods disagreeing with the data; a step that assumes
analysis code exists; a clock check that needed adapting to variable delays;
results per session that pooled analyses cannot give; and no mention of an
empty draft version.
