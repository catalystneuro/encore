# 000233, Tingley et al. 2021

Seven claims reproduced, three partially, four not reproduced and 20 blocked
on the dataset; `edfig10-expression-correlates-effect`, which also needs the
histology scores printed only in Extended Data Fig. 10e, is counted apart and
blocked as `metadata_insufficient`. It pins version 0.250624.0414, the latest
published version, as the paper cites none; the earlier version 0.230223.0815
has the same 345 files with the same sizes. The paper, Tingley, McClain, Kaya,
Carpenter and Buzsaki in Nature, reports that the rate of hippocampal sharp
wave-ripples (SPW-Rs) in rats is negatively correlated with future changes in
interstitial glucose (R = -0.21 at a lag of 10.7 min over 30 rats), that
optogenetically induced ripples are followed by a fall in glucose, and that
inhibiting the lateral septum with hM4Di and CNO decreases the SPW-R
correlation with glucose. The claims were written from the accepted author
manuscript in PubMed Central (PMC9214835) with its Supplementary Information
but without the figures, and from the lab's buzcode toolbox at commit
e615663b, which holds the ripple detector but no code for the glucose
analyses. The SPW-R and glucose correlations of Figure 2, the shuffle and
clustering tests, ripple features, cross-frequency coupling, the glucose
rhythm and sensor decay, ripple rate, stability and rhythms, the refractory
period, and the NREM, wake and hour-of-day comparisons were tested. The
optogenetic claims of Figure 3 and Extended Data Fig. 7, the units of Extended
Data Figs 3e and 8, the fasting experiment and the dorsal and ventral
comparison are blocked as `data_missing`, the DREADD claims of Figure 4 as
`metadata_insufficient`, and the three predictor models of Extended Data Fig.
6 as `too_large`, as reading the LFP and accelerometer for the 3 rats whose
brain state is stored takes 41 min in 4 processes and 28 min in 16 before any
model is fitted, against the 30-minute notebook limit. `fig2h-phase-reset`
(rho -0.24, p = 0.51, or 0.55, p = 0.098), `edfig1-glucose-rhythm` (residual
peak at 51.4 min against 60 +- 6 min), `edfig2-refractory-period` (shortest
interval 28.8 to 39.2 ms, median 34.4 ms) and `edfig4-no-hour-differs` (10 of
276 pairs of hours at p < 0.05, smallest p = 0.010, against a smallest P of
0.53) are not reproduced. The author's first run gave 7 reproduced, 4
partially, 3 not reproduced and 21 blocked. The author asked a reader no
questions, so the answer run and the following author run changed nothing.
Round 1 agreed with 33 of 35 outcomes; the author took its outcome for
`edfig1-glucose-rhythm` (from partially reproduced to not reproduced) and its
`data_missing` reason for `edfig9-dorsal-ventral`, and kept
`edfig1-glucose-circadian-meals` blocked where the verifier gave not
reproduced. Its points led to 12 fit variants for the glucose rhythm, start,
stop and stop-to-next-start intervals for the refractory period, coupling
filtered only where both signals are recorded with 100 shuffles per rat, a
within-subject circadian test, a bootstrap over rats, and a full listing of
the groups and channels of all 345 files. A question was then put to a reader
on which time point and which intervals the refractory period should use; it
is unanswered, as it was added after the answer step. Round 2 agreed with all
35, so there was no third round; it found statements the outputs did not
support, among them edfig6 timings quoted from another run, "an oscillation of
about 50 min", a sentence that a Spearman test over 3 to 5 days rarely reaches
p < 0.05, the glucose hours of CGM48 and the README run time, which were
corrected. Its points also led to both alignments one reading apart for five
more claims, after which `fig2g-clustered-ripples`, `edfig4-ripple-features`
and `edfig4-nrem-wake` were marked as assumed. Some outcomes rest on weak
ground: `fig2-ripple-rate-predicts-glucose` matches under 3 of the 16
combinations of readings (R -0.176 at 14.2 min) on 18 rats, 1 of 16 once rats
with less than 6 h of data are left out, and none with the SPW-R count over
the 5 min after each reading, and its mean lag falls in tolerance as peaks at
-100 to -20 min offset peaks at +55 to +80 min; `fig2g-clustered-ripples`,
`edfig4-ripple-features` and `edfig4-nrem-wake` change outcome under one of
the two other alignments, and `edfig4-nrem-wake` rests on 3 rats where the
paper has 8; and `supp-ripple-rate` holds with the Methods' 5 s.d. threshold
(10.19 per minute) and not with all stored events (11.07). The author's run
went from 17:40 to 19:04 UTC and nothing failed in the end; one file per rat
in CGM1 to CGM3 was found during the clean run to hold its glucose on another
clock, and the fix moved the main claim's lags. In the revisions a first
survey command hung and cost an hour, and one run hit a temporary 503 from the
DANDI API and passed on retry. The notebook ran in 3.1 minutes at first and in
6.5 minutes in the last run.

The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is a
contributor). It holds no spike units, no optogenetic stimulation times, no
CNO or vehicle labels or injection times and no meal times, so sixteen of the
paper's findings (Figures 3 and 4, Extended Data Figs 3e, 4d-f, 7, 8 and 10)
and the meal part of Extended Data Fig. 1f cannot be tested; a listing of all
345 files found no stimulation or TTL channel. Nothing links the 25 subjects
(CGM1 to CGM60, bruce, dt15, flex1, ros, Vanessa) to the rats 1 to 45 of
Supplementary Table 1 or to the paper's cohorts, and only the files of CGM1
state an experiment. In twelve subjects the GlucoseLevel timestamps carry
dates with day and month swapped whenever the day is 12 or less, so a reading
of 4 March 2021 is stored as 3 April 2021; swapping back raises the hours of
glucose overlapping the electrophysiology from 1139 to 1717, and in CGM32 86
readings dated up to 2021-12-02 look like the same swap and were left as
stored. Session start times hold local wall-clock time labelled UTC, files of
one subject in CGM2 and CGM3 carry two different reference times, and in CGM1,
CGM2 and CGM3 one file stores the glucose series in a different order or
relative to its own reference. 27 recordings of CGM1, CGM3, CGM30, CGM31 and
CGM32 are deposited twice, under file names with dashes and with underscores.
In the SPW-R tables `start_time` and `stop_time` are on the session clock but
`peak` is seconds from the start of the file, which the column descriptions do
not say, and seven table names are not described. The stored SPW-R tables of
nine subjects hold events down to 4 s.d. (7 to 29% of their events), and
CGM30's down to 0.23, where the Methods give a 5 s.d. threshold; applying it
changes the mean SPW-R rate from 11.07 to 10.19 per minute. The Methods say
the detection parameters are stored with each session's ripple events, but
the NWB tables carry only column names and a description. No interval between
stored SPW-R peaks is shorter than 28.8 ms, and the gap from one event's stop
to the next one's start has its minimum at exactly 20.0 ms in 19 of 22 rats,
which matches a rule that merges events closer than 20 ms, so the 20-ms
refractory period of Extended Data Fig. 2a may be this rule. In CGM37, CGM60,
dt15 and flex1 the glucose readings and the electrophysiology cover different
days, and CGM36, bruce and ros have no SPW-R table, so 7 of 25 subjects cannot
contribute to the SPW-R and glucose analyses; Vanessa's glucose current has a
median of 0.25 nA, against about 30 nA in the other subjects. One question is
put to the paper's authors: how the 5-min SPW-R counts were aligned with the
glucose readings for the cross-correlograms, which correlation was used, and
over which offsets the peak lag was searched, as with 18 rats the mean lag of
10.7 min is matched only under some combinations and moving the alignment by
one reading moves the mean lag by 5 min.

The author's points on the protocol: it does not say what to do when the
data's own processing contradicts the Methods while the claims file says to
use the stored events, so the Methods' 5 s.d. threshold was applied and the
stored events shown as a variant; repairing data such as the swapped dates is
not covered, so the repair was recorded as a finding and a deviation; it does
not say how to record a claim of which only part can be tested, so the
circadian and meal claim was blocked as `data_missing` with the circadian
result in the notes; neither it nor the claims files say whether a partial
outcome is allowed when a criterion has no partial case; and the check that
the glucose and electrophysiology clocks agree has no contrast independent of
the claims, which the notebook states.
