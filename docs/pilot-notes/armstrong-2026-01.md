# 001341, Armstrong et al. 2026

No claim reproduced, one partially, five not reproduced and 27 blocked, 15 as
`metadata_insufficient` and 12 for missing data. The first verification round
agreed with all 33 outcomes as they stood and the second with all 33, and
nothing was proposed after the second, so there was no third round. It pins
version 0.260414.1316, which the paper cites and which is the only published
version. The paper, Armstrong and Vlasov, "Neural correlates of perceptual
decision-making in the primary somatosensory cortex" in PNAS, records units in
the barrel cortex of mice running on an air-suspended sphere in a tactile
virtual reality, where closed-loop straight runs alternate with open-loop turns
in which one wall approaches the snout, and relates staged spiking, a ramp of
the population rate and a drift diffusion model (DDM) of the reaction times to
the decision to turn; the dataset holds two of the paper's 19 animals (489 and
503), with units, trials and ball tracking. The claims were written from the
accepted author manuscript (PMC13142948) with its SI Appendix, whose Tables S2
and S3 are images that could not be read, and the paper links no analysis code
of its own. Not reproduced are `table-s1-recordings` (61 and 43 units against
65 and 48), `fig1n-epoch-rates` (an epoch 1 rate of 6.65 to 7.80 Hz at every
lag against 2.0 ± 0.1 Hz), `figs1-running-speed` (5.93 cm/s against 21 ± 4),
`fig2a-success-rate` (0.609 to 0.694 against 0.95) and `fig2b-lateral-spread`
(an SD of 0.84 cm at t = 0 against 0.55 ± 0.055). `fig4-ddm-fit` is partial on
an assumption about early reaction times, with low confidence: the GDDM has a
lower BIC than the DDM, but no reading gives a nondecision time within 0.108 to
0.132 s, and under the mixture handling of early reaction times the GDDM
condition fails too. The 15 claims blocked as `metadata_insufficient` need
spikes aligned to the turn onset, and the 12 blocked for missing data need
whisker, touch, wall or gait data or animals not in the dataset. The author's
first run gave none reproduced, one partially, four not reproduced and 28
blocked. The author asked a reader nothing, so the answer and author-answers
runs changed nothing. Round 1 agreed with every outcome and found that the
nondecision time was probably set by a few very early reaction times, that no
clock-drift model had been fitted from the running-speed correlation, that the
lateral traces hid missing values, that the decoder z-scored before the
cross-validation split and that taking the first 1000 rows of 489 as Table S1's
trials was an assumption; in reply every DDM reading was fitted three ways
(all reaction times kept, a uniform mixture, reaction times below 0.1 s
dropped), a speed clock for 503 and a null for the lag search were added, a bug
that left only 212 of 513 (503) and 91 of 249 (489) trials with a value at
t = 2 s was fixed, and on the verifier's suggestion `fig1n-epoch-rates` moved
from blocked to not reproduced. The record's round-1 entry said the claims-file
header had been changed to note the SI's TTL synchronisation, which was wrong.
Round 2 agreed with all 33, found that error and sentences the outputs did not
support (a stored-onset range of 7.27 to 7.48 Hz where the outputs give 7.15 to
7.48 Hz, swapped 95th percentiles, the mixture weight called at its limit in
every fit, 0.12 s called not excluded by the likelihood profile, and "no
alignment can be found" for 489, whose best lags rise from 4.36 to 12.23 s),
and asked for a caveat that the 503 speed clock may reflect running, all
corrected. The author's run took about 1 h 35 min (02:11 to about 03:46 UTC);
an early notebook run took 35 minutes and wrote 334 MB of PyDDM warnings, fixed
by silencing warnings in the workers and fitting the GDDM on fewer readings, and
the notebook ran in 152 s at first, 96 s after the author-answers run, 356 s
after round 1 and 335 s at the end. Untracked placeholder files in the
repository root, which the author did not create, and an edit to
`tools/build_site.py` were left untouched.

The spike times are not on the clock of the trials table and the behaviour, and
the files hold no synchronisation signal or offset (processing, analysis and
stimulus are empty), though the SI says LabVIEW TTL signals were used to
synchronise the recordings with the behaviour. At the stored turn onsets
neither session shows a trial-locked population response, and turn type cannot
be decoded from the units' spike counts, while the animal's lateral position
decodes it at 0.92 to 0.95. In 503 the lag of the best correlation between
spike rate and running speed grows smoothly from 12.9 to 19.75 s over the first
5200 s, and a line through it (11.86 s plus 1.37 ms per s, residual SD 0.56 s)
recovers trial-locked, turn-specific responses, which may in part reflect
running, since 503 runs in 1.7% of OL_L and 31.8% of OL_R rows; in 489 the
onset-triggered best lags rise from 4.36 to 12.23 s over the first seven
windows, but no window's lag is separated from chance and the speed
correlations are weak, so no clock can be fitted. None of the paper's findings
on spike timing can be tested. The dataset holds 2 of the paper's 19 animals;
the other 11 ephys sessions, the 6 behaviour-only sessions, and the wall
positions, whisker tracking, touch times and gait of any session are not in it,
though the SI says the spikes of all filtered units are packaged with the
behavioural data in one NWB file per animal. In session 489 the trials table
rows 1000 to 1610 (611 rows) all have start 3681.414 s, stop 3683.414 s and
label OL_L_1.dat, while the `trial` sample series gives them their own times
(3683 to 6218 s), and 256 of their 305 turns go to the right. In both sessions
a run of OL rows (62 in 489, 63 in 503) has a stop time earlier than its start
time, and their sample timestamps go back in time (891 times in 489, 557 in
503). The units tables hold 61 units for 489 and 43 for 503, where Table S1
gives 65 and 48; for 489 Fig. 5B gives 10 L2/3 and 13 L6 units, 43 FS and 22
RS, where the file has 7, 12, 30 and 31, and 503 has three units in a layer
labelled WM, which the paper does not use. Unit 101 of 489, which the paper
calls 489101 and describes as RS, is labelled Inhibitory in layer 5A with a 0.2
ms waveform, FS by the paper's 0.4 ms rule. The population rate of 489 is 6.65
to 7.80 Hz in the second before the turn at any alignment from -20 to 60 s, and
7.09 Hz over the whole recording, where Fig. 1N gives 2 ± 0.1 Hz. The paper's
trial selections cannot be identified in the files: 489 has 249 and 251
labelled OL_L and OL_R trials where Fig. 1J-K uses 266 and 265, and 503 has 230
and 283 where Fig. S4A uses 305 and 304; in 503 only 27.7% of trials are run
above 10 cm/s (Table S1 52.8%), and all 513 OL trials give a success rate of
0.68 while the 94 run above 10 cm/s give 0.98 to 1.00, so the paper's figures
may rest on a selection of running trials, or the deposited session of 503 may
differ from the one analysed. The file of 489 gives the age as P63D, but its
date of birth and session date are 68 days apart, the P68 of Table S1.
`distance_lat` and `distance_for` restart at 0 at each trial, the sign of
lateral distance is not stated, `trial` and `ts_local` are not described, the
trial types are stimulus file names, and `unit_type` is the waveform-duration
classification, not a cell-type identification. No question is put to the
paper's authors.

The author's points on the protocol: it does not cover streams whose alignment
could only be fitted from the response under test, and those claims were
blocked as `metadata_insufficient` with the evidence shown; criteria such as
"17 of 19" cannot be met when most animals are absent, and `table-s1-recordings`
was judged not reproduced because the counts present already fail while the
cross-animal neural claims were blocked; "blocked for the same reason" does not
say which reason to give when a claim lacks two things or its dependencies are
blocked for different reasons, and one was given under `blocked_by` and the
other in the notes; the rule for `measured` covers only several matching
readings, and when none matched a reading was picked and named; readings too
slow to run are not covered, and the GDDM was fitted on 4 of 16 readings as a
deviation; corrupted table rows are not covered, and they were excluded with a
`format_error` finding; and reaction times at the window edge, which made PyDDM
fail, were dropped as a standard choice (2 to 5 of 249 trials).
