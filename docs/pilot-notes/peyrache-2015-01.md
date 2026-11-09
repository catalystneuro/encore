# 000056, Peyrache et al. 2015

Six claims reproduced, two partially and thirteen blocked, all on the
dandiset. Round 1 gave its own outcome for each claim without seeing the
record and agreed with all 21; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports that
head-direction cells in the antero-dorsal thalamic nucleus (ADn) and the
post-subiculum (PoS) of mice keep their coordination in sleep, with the
represented direction moving about ten times faster in slow-wave sleep. The
HD cell count, the preservation of rates and pair correlations across
waking, REM and SWS, the 60 degree packet, the angular velocity in each
state, the noise correlations and decoding were tested on the HD cells of
each session pooled over regions; the 13 claims that separate the ADn from
the PoS are blocked as `metadata_insufficient`. Some outcomes rest on weak
ground: the count of 378 HD cells passes only with Mouse12-120808 as
deposited, and with that session realigned it is 391 (390 with one
constant shift), above the upper bound of 388.3; the estimator of angular
velocity returns 4.99 for a trajectory played ten times faster, and scaled
by that the data's 8.33 becomes 16.69, so the fold is not determined; and
the waking crossing of `fig3a-packet-60-degrees` is 0.2 degrees inside the
tolerance, with reading (b) at 54.1 degrees just outside it. The
supplementary files could not be downloaded, as PubMed Central served a
browser check in their place.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The units tables hold only spike times, with no electrode,
shank, brain region, waveform or quality measure, and every electrode's
location is "unknown", which blocks 13 of the paper's 21 claims; the
electrode groups and ripple annotations are consistent with Mouse24,
Mouse25 and Mouse28 being the three dual-site mice, but the files do not
say so. The files hold 1959 unit rows (103 with no spikes) in 40 sessions,
against the paper's 1077 recorded cells in 42 sessions; Mouse12-120809
alone has 292 units, 167 of them firing below 0.5 Hz, unit ids run from 0
to N-1 with no shank or cluster number, 1526 rows fire at 0.5 Hz or more,
and nothing marks which units or sessions the paper analysed. In 36 of 40
files one unit's spike times are two sorted runs, the first ending at an
index of the form k x 65536 - 1, and in 10 of them 821 to 22281 times of
the second run also appear in the first, which suggests an error in the
conversion. In Mouse12-120808 the position and the spikes do not share a
clock (the best shift is -1.5 s at the start of the exploration and -3.4 s
at its end, against -0.2 to 0 s in all other sessions), and no unit passes
the HD criteria as deposited. Other findings: the open-field exploration,
the paper's waking epoch, is not marked, and the "Awake" state also covers
waking in the home cage; the raw LED positions are stated in meters with a
conversion of NaN but hold camera pixels; Mouse32-140820 has no sleep-state
table and no processed position, Mouse17-130201 has no processed position,
and in three Mouse20 sessions the position series ends 11 to 109 minutes
before the recording; the annotation series `dow`, `hdD` and `rip` have no
description; the related resource for the paper gives its name as
"nternally organized mechanisms of the head direction sense" and the title
in place of a DOI; and neither the paper nor the dandiset links analysis
code.

The first criterion of `fig4b-noise-correlations` used a Pearson scaling
that contradicts the Methods' formula; after the first run it was changed to
that formula before the outcome was recorded, with the first version kept as
a variant. The author's points on the protocol: step 5 assumes there is code
to read; no rule for a criterion found wrong after a run; a clock check that
does not fit continuous sessions of spikes, position and sleep states; no
rule for a condition the paper uses that the data do not mark; whether a
region assignment inferred indirectly may decide an outcome; one expected
value across several conditions; reported counts that do not decide a
claim; the default 10% tolerance, which gives 9 to 11 for "approximately
tenfold"; open-access supplements that cannot be downloaded; where
descriptive statements go; and the rule on seeds when no step uses random
numbers.
