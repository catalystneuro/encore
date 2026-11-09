I wrote `docs/pilot-notes/000959-fan-2024-01.md` and changed no other file. The other untracked files at the repository root were there before this run. Nothing is committed. The `catalystneuro` field for this dataset is empty, so the second paragraph has no CatalystNeuro opening sentence. One mismatch in the record is noted in the text: the author's first report counts 33 claims, but the claims file holds 36.

# 000959, Fan et al. 2024

23 claims reproduced, five partially, two not reproduced and six blocked. The
first verification round agreed with 35 of the 36 outcomes and the second with
34, so there was no third round; in its two disagreements, on the saccade
claims, round 2 accepted the outcomes as computed and asked that they be marked
as resting on an assumption, which they now are. It pins version
0.261020.0242, the latest; the paper cites none, and the only other version,
0.260531.2104, has the same 1705 assets with the same ids and sizes. The paper,
Fan, Dal Monte, Nair, Fagan and Chang in Neuron, gives closed-loop
microstimulation (75 uA, 100 Hz, 200 ms) or a sham to the orbitofrontal cortex
(OFC), dmPFC or ACCg of two male rhesus macaques (monkeys L and T) when they
fixate the Eyes of a live partner, monkey E, on 27 days per area (15 from L and
12 from T) with Mouth stimulation on 5 days per area from T and non-social
control runs with a random dot motion (RDM) stimulus, and reports that OFC
stimulation brings gaze closer to the partner's eyes in the
contralateral hemifield, shortens the inter-looking interval and the
reciprocation latency, and leaves the partner, the pupil and saccades
unchanged. The claims were written from the accepted author manuscript in
PubMed Central (PMC11309918) with its one supplement, without the version of
record, and from the paper's code at commit cc0bf994. 30 claims were tested.
The six causal decomposition claims, `figs4a-causal-strength-no-stim-effect`,
`figs4b-causal-strength-no-epoch-effect`, `ofc-slope-unchanged-by-epoch`,
`fig4c-dmpfc-slope-late-greater`, `fig4d-dmpfc-slope-permutation` and
`dmpfc-slope-positive`, are blocked as `too_large`: one EEMD of one 150-bin
series with 1,000 ensembles took 15.9 s on one core (6.8 s on four processes;
13.1 and 5.5 s in the round-2 run), so the 19,474 social Eyes trials need about
1,380 CPU hours and the smallest subset, the 2,250 stimulation trials of the 25
OFC epoch days, about 159 CPU hours (68 hours of wall time on four processes),
against a notebook limit of one hour; the trials, distances and epochs are all
in the dataset, and `epoch-days-76-of-81` reproduces with the five days the
code names. The headline result reproduces: under the Methods reading the
median stimulation minus sham day difference in social gaze distance after OFC
stimulation is -17.9 pixels (-0.70 degrees), p = 0.00021 over 27 days (monkey L
p = 0.0067, T p = 0.016), with the contralateral effect p = 0.00048 and dmPFC
and ACCg unchanged. `figs1e-eyes-vs-rdm-comparable` is not reproduced under the
claims file's deciding reading (a), the day's total, Eyes fixations exceeding
RDM fixations for every area (corrected p 0.00036, 0.000025 and 0.00041), while
the code's mean per run gives 0.40, 0.40 and 0.52, as the paper reports.
`methods-eyes-vs-mouth-bootstrap` is not reproduced, contralateral p being
0.078 (a, one-sided) and 0.156 (b, two-sided) against the paper's 0.009, and
both hemifields 0.043 and 0.086 against 0.799; the code's M1-only fixations do
not give the paper's pattern either. `design-sessions-per-day` is partial,
monkey L's control mean being 6.02 against 5 plus or minus 0.5, and
`methods-ofc-longer-face-looking` partial, its tests holding but monkey T's
46.2 ms being outside 39.5 plus or minus 3.95. `partner-monkey-unchanged` is
partial, 1 of 18 tests giving p below 0.05 (dmPFC M2 reciprocation latency
from the start of the M1 look, p = 0.044), and
`fig5a-trigger-duration-unchanged` partial, the claim holding for OFC (p =
0.61) and not for dmPFC (median day difference 31 ms, p = 0.019; paper 0.269).
`fig3b-ofc-inter-looking-interval` reproduces at p = 0.044, which becomes 0.058
if the 91 whole Face events that start on the trial sample count as latency 0.
`methods-mouth-stimulation-no-effect` reproduces, though with 5 days per area
the smallest two-sided exact signed-rank p is 0.0625. The two saccade claims
rest on a Python port of the Otero-Millan et al. (2014) detector, run on M1's
unfiltered gaze as the paper's code passes it, marked as an assumption:
`fig5cd-saccade-counts-unchanged` is partial, OFC stimulation trials having
fewer macrosaccades (p = 0.044; paper 0.055), and
`fig5e-h-saccade-kinematics-unchanged` reproduces, 0 of 14 tests failing,
while the paper's code's labelling of microsaccades gives 0 of 4 and 3 of 14.
The author's first run gave fig5a as not reproduced and the two saccade claims
as blocked as `not_runnable`, the files holding no saccades and the paper's
detection being MATLAB code; its report counts 33 claims (19 reproduced, 4
partially, 5 not reproduced and 5 blocked), where the claims file holds 36. The
author asked a reader no questions, so the answer run and the following author
run changed nothing. Round 1 disagreed with fig5a, which it gave as partial,
and found that the claims file's reading (a) of the Eyes against RDM claim
compares day totals over 10 to 15 social runs with totals over about 5 control
runs, that the detector's software is public and the saccade claims were not
attempted, that the decomposition cost was estimated from one 100-ensemble run
multiplied by 10 and not for the subsets the claims need, that the bootstrap
was not run on the code's fixations, and that 29% of trials (5,695 of 19,474)
have no M1 Eyes event in progress at the trial time. In reply fig5a became
partial, the detector was ported and the saccade claims tested, the cost was
timed directly and per subset, the bootstrap was run on the code's fixations,
the trials without an Eyes event were shown to be spread evenly over areas and
trial types (27.3% to 30.1%), and a question was put to a reader on whether
reading (a) of the Eyes against RDM claim misreads the paper, which is still
pending. Round 2 asked that the saccade outcomes be marked `assumed`, as the
detector's output is not physiological and the port was never checked against
the MATLAB code, and found sentences the outputs did not support (decomposition
timings not updated after the re-run, dmPFC density sums of -2.46 and -0.0026
where -2.56 and -0.0027 were printed, 1 of 21 tests where there are 18, the
excluded epoch days said to be named by the paper where only the code names
them, and 6% of Eyes events outside the rectangle, true only of social runs),
which were corrected; a check of the port on synthetic gaze was added, since
MATLAB is not available. The author's run took about 67 minutes (23:22 to 00:29
UTC) and nothing failed. The notebook ran in 11.2 min at first, almost all of
it reading the data, 652 s after the answer, 14.4 min for the full entry run
after round 1 and 663 s after round 2.

The dataset holds every day the paper describes, 81 Eyes days and 15 Mouth
days, one file per run, with gaze, pupil, stimulation and sham times, ROIs and
fixation event tables, but no saccade events, so the saccade claims need an
outside detector; run on M1's gaze as the paper's code calls it, the detector
finds 386 saccades per social run with a median duration of 147 ms and a 95th
percentile of 1,062 ms, the gaze velocity inside fixations (median about 20
deg/s in one run) is above its 5 deg/s saccade limit for about 95% of samples,
so many detected saccades span several fixations, and in 202 of 1,179 social
runs the MATLAB code's merge of overlapping saccades would stop with an error.
The run counts differ from the paper's: monkey L has 6.0 control runs per day
on average (4 to 8; 14 of 45 days have 8) where the paper reports 5, and monkey
T 14 social runs on every Eyes day where the paper reports 15 on average (14 to
15); on the 14 days with 8 control runs the runs are numbered 1 to 8, each
295.8 to 296.9 s long with 9 to 32 kept trials, so nothing marks any as extra.
The Methods give the fixation counts of Figure S1E as the total per day and the
code takes the mean per session, and with about twice as many social runs as
control runs per day the Eyes against RDM comparison turns on that choice.
Neither the files nor the paper give the padding of the Eyes ROI, the number
missing from the Methods text, nor how fixation events were assigned to ROIs:
6% of the M1 Eyes events of social runs and 11% of those of Dot runs have a
mean gaze position outside the Eyes rectangle of their file, and 3% and 10% of
whole Face events outside the Face rectangle. The fixation tables are named
alike but cut the face differently, m1_neface (and m2_neface) being the face
outside the Eyes including the Mouth (all 23,641 m1_mouth events are in it) and
mutual_face the face outside both the Eyes and the Mouth, which the
descriptions do not say. The Dot runs do not hold `roi_m2_face`, the reference
of their hemifield split, nor say that their `roi_m1_eyes` is the RDM stimulus,
and the description of `laterality_label` names no reference, though it matches
the centre of `roi_m2_face` for 99.98% of M1 events. Trial times fall inside an
offline M1 event in the triggering ROI on 71% of social Eyes trials and 62% of
Dot Eyes trials, against 5 to 20% for times shifted by 0.5 to 2 s, consistent
with a shared clock, so about 30% of online triggers do not coincide with an
offline fixation in the ROI (65 of 954 social Eyes runs are below 50%).
Questions are put to the paper's authors: whether a whole Face event that
starts on the trial sample counts as the look back with latency 0, and whether
the inter-looking interval is taken over M1-only or M1-only and mutual events;
whether M2's reciprocation latency is measured from the start of M1's look or
from the trial time, and how the p-value of the Eyes against Mouth bootstrap is
computed; and whether M1's gaze was filtered before the saccade detector was
run and what durations and amplitudes the detected saccades had.

The author's points on the protocol: the DANDI section of `archives.md` says to
stream with remfile, which took about 14 s per file for metadata alone (12.5
min with 32 threads), and each file was read into memory over HTTP instead,
bringing the full load to about 10 min; a claim of absence is to be judged on
the paper's test alone, yet the claims file names several readings for some,
and the criterion requiring every reading to pass was followed; several
criteria have no rule for a partial result, and `partially_reproduced` was
given where most of the claim held; for the Eyes against RDM claim the
protocol's order (Methods first) gives a not reproduced that the code's reading
would reverse, and it was recorded as a `code_mismatch` finding without asking
a reader; the protocol does not say whether a cost estimate made inside the
notebook is enough to support `too_large`, and one decomposition was timed in
the notebook; and the harness created an empty `.claude/.cc-writes` in the
entry folder, which was removed, while unrelated untracked dotfiles at the
repository root were left untouched.
