I wrote `docs/pilot-notes/000689-li-2022-01.md` and changed no other file. The untracked dotfiles and the `scripts` folder in the checkout were there before this run, and I left them alone. Nothing is committed.

# 000689, Li et al. 2022

No claims reproduced, two partially, three not reproduced and 34 blocked.
The first verification round agreed with 38 of the 39 outcomes and the second
with 37, and a third round, held on the two changes of outcome proposed after
the second, agreed with both. It pins version 0.240530.1923, the latest; the
paper cites none, and the other published version lists the same 85 assets
with the same IDs. The paper, Li, Namburi, Olson et al. in Nature, deletes the
neurotensin gene (Nt) in PVT neurons projecting to the basolateral amygdala
(BLA) by CRISPR, records BLA units with phototagging of BLA-NAc and BLA-CeA
projectors in a task with sucrose, neutral and shock cues, clusters the units
and the trial-by-trial behaviour from DeepLabCut pose, and measures
neurotensin in the BLA with the GRAB-NTS1.0 sensor during tone-sucrose and
tone-airpuff learning, alongside anatomy, slice physiology and behaviour
cohorts. The claims were written from the accepted author manuscript in
PubMed Central (PMC9583860), without its source data files or a PDF, and the
paper links no code. Five claims were tested; 19 are blocked as
`data_missing`, 14 as `metadata_insufficient` (13 for want of group and
projection labels, and `fig4c-photoidentification`) and
`fig4d-seven-clusters` as `methods_underspecified`, seven clusters coming only
under one reading with an 820 ms smoothing window and 6 to 12 over windows of
20 ms to 2 s. `fig3k-nt-sensor-sucrose-increase` is not reproduced on an
assumption: under the per-trial z-score the late response is higher in all
four readings, and with all trials AUC +3.53, t(4) = 5.74, p = 0.0046, but
with the first 16 trials p = 0.093, and the criterion asks for p < 0.05 under
every reading; with the regression fitted on the pooled baseline bins p >=
0.44, and under the session-pooled z-score p >= 0.16.
`fig3l-nt-sensor-airpuff-decrease` is not reproduced, the direction matching
(AUC -5.47 with the first 16 trials, against the paper's -3.657) but no
reading reaching p < 0.05 (smallest p = 0.074), and `fig3-nt-sensor-early-dip`
is not reproduced, the early sucrose mean being -0.62 and the airpuff mean
+0.11 (first 16 trials, per-trial z-score) and no reading of 8 having both
below zero. `fig4-recording-count` is partial, 31 mice being within tolerance of 30
and 1902 units (1739 at a baseline rate of at least 0.3 Hz) far from 685.
`fig5dh-behavior-clusters` is partial on an assumption, the pose being put on
the trial clock by a linear map fitted to the port entries, which holds in 21
of 29 sessions: z-scored features give 7 sucrose and 3 shock clusters and raw
features 6 and 5, so each reading meets one count and not the other, and the
"passive and active strategies" are not tested. The author's first run gave
`fig4-recording-count` as not reproduced and `fig4c-photoidentification` and
`fig5dh-behavior-clusters` as blocked. The author asked a reader no questions,
so the answer run and the following author run changed nothing. Round 1
disagreed with `fig4-recording-count`, giving it as partial, and found that
the fake-session test of the phototagging was never applied, that only fixed
pose lags were scanned where a fitted clock might remove the drift, that the
photometry regression coefficients were never printed, that the notebook listed
fig2c under the wrong block reason, and text errors. In reply printing the
coefficients exposed a slope of -0.02 in Mouse6's late sucrose session, whose
LED labels move by one frame partway through, so channels were taken from the
frame order and fig3k became partial; the fake-session test gave 91 to 256
tagged units under every reading and fig4c became not reproduced; the fitted
clock made fig5dh partial; and a question was put to a reader on whether a mean
over 2 to 7 s can test a "transient" dip. Round 2 disagreed with fig3k, as only
2 of 4 readings pass, and with fig4c, as the block taken as fake evokes a
short-latency response in 1353 of 1902 units, so the count does not test the
claim; it agreed with fig5dh's outcome but not its reason, and found sentences
the outputs did not support (a remaining clock lag of 1 to 15 s where H11's is
19.2 s, a pose clock off by "tens of seconds" where it reaches 192 s, and
confocal images in 29 files where 27 hold them), which were corrected.
Re-running the same code then changed the raw-feature counts from 7 and 5 to 6
and 5, and z-scored features were adopted, as an exact PCA or changes of 1e-9
in the features move the raw counts. The author proposed not reproduced for
fig3k and blocked for fig4c, and round 3 agreed. The author's run took about
1 h 40 min (12:52 to 14:32 UTC); photometry channels were first assigned by
frame order, then by the LED labels when one session shifted phase, and a
behaviour analysis with tsfresh was dropped once the pose turned out not to
align, until round 1. The notebook ran in 9.5 min at first, 526 s after the
answer, 19 min after round 1, 28 min after round 2, close to the 30-minute
limit with about 16 min of tsfresh, and 1586 s in the last run.

No file says which recorded mouse is in the CRISPR or the control group, or
whether its Cav2-Cre went to the NAc or the CeA; every genotype reads "Wild
type", and no text field, units or electrodes column or archive subject field
holds such a label, so 13 of the paper's claims cannot be tested. The units are
not sorted single units: 21 of 31 sessions hold exactly 64 units on 32
channels, 1902 units in all against the paper's 685, in 1061 units more than 5%
of inter-spike intervals are below 1 ms, and in each session 6 to 65% of spike
samples recur in another unit. Each session holds two blocks of about 427 light
events, fitting the paper's fake and real phototagging sessions, but nothing
says which is which, in H31 to H42 one block comes before the task, and the two
evoke much the same responses (1353 and 1243 of 1902 units, with 88% of the
units responsive to the second also responsive to the first); there is no 1 s
light. Only the in vivo recordings of Figures 4 and 5 and the NT sensor
photometry of Figure 3j-l are deposited, so 19 of the 39 claims cannot be
tested. In H17 the spike times of all 64 units fall within the first 249 s of a
12118 s recording. The DeepLabCut pose has no timestamps, only a start time of
0 s and a nominal 15 frames per second; port entries match the head's approach
to the port at lags a median of 80 s and up to 192 s from zero that drift
within 28 of 29 sessions, a fitted linear map holds in 21 sessions with a rate
factor of about 0.988 in 20 of them, and in 8 no such map holds; the videos of
H07, H09 and H10 run 818 to 1528 s longer than their pose and that of H11 426 s
longer. 27 of the 31 ecephys files hold stacks of 8 to 42 confocal images of
the PVT named only by depth, with no channel, probe, stain or group label. H09
to H14 hold 75 sucrose and 45 shock CSs and no neutral CS, while their session
description says 2 to 1 to 1. The dandiset has 31 mice where the paper reports
30, and for H28 and H32 the recorded session is earlier than another
discrimination day for which only pose is deposited, while the paper analyses
only the last day. The photometry files store one 60 Hz series interleaving
the 415 nm frames, the 470 nm frames and a third, undescribed frame type, told
apart only by the LED event labels, which shift by one frame in Mouse6's late
sucrose session; the cue events last 2 s where the Methods give a 4 s CS, no
event marks the US or whether a cue was paired, and in two airpuff sessions the
lick label is on for most of the session. Questions are put to the paper's
authors: what window MATLAB's smoothing factor of 0.85 produced and whether it
was applied to each CS trace or to the concatenated trace; whether the NT
sensor residuals were z-scored against each trial's baseline or the session's
pooled baseline; and whether the tsfresh features were scaled before PCA, and
which scikit-learn release and t-SNE settings were used.

The author's points on the protocol: it does not say how to classify a claim
blocked by a timing defect of the files themselves, such as pose without
timestamps, and `metadata_insufficient` was used; a method choice that is not
one of the criterion's readings, such as the smoothing window, sits between
step 1.6 and the criterion's "reproduced when one reading gives seven", and
fig4d was blocked as `methods_underspecified` since the 7 comes from one window;
a claim with two missing pieces, such as fig2c with missing data and missing
labels, needs a choice of `blocked_by`, and the reason that blocks every
reading was picked; and no check covers a paper-specific light artefact or
fake session, so the first run reported the rule's outcome without the
fake-session test.
