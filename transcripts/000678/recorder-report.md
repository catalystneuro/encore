I wrote `docs/pilot-notes/000678-hulsey-2024-01.md` and changed no other file. Some untracked files I did not create also show up in `git status` (`.bashrc`, `.profile`, `.idea`, `scripts` and others), and I left them alone. The verifier's round 2 report gives the counts as 19 reproduced and 8 partial, but the record and `readme_row.py` both give 21 and 6. The note uses the record's counts.

# 000678, Hulsey et al. 2024

Twenty-one claims reproduced, six partially, one not reproduced and one
blocked. The first verification round agreed with all 29 outcomes and the
second with all 29, so there was no third round. It pins version
0.231004.2146, the version the paper cites; the later 0.261020.0029 has the
same assets and differs only in archive metadata. The paper, Hulsey, Zumwalt,
Mazzucato, McCormick and Jaramillo in Cell Reports, fits a GLM-HMM to the
choices of each of 13 head-fixed mice on an auditory (8) or visual (5)
discrimination task, types the states as optimal, disengaged and sub-optimal,
relates them to pupil diameter, face motion energy and locomotion speed, and
classifies the states from these measures with decoders. The claims were
written from the accepted author manuscript in PubMed Central (PMC11016285)
and its supplement, without the main-text PDF, and from the paper's code on
Zenodo (doi:10.5281/zenodo.10306018) and in uobrainflex at commit ef48985.
The model of the paper's ssm fork was reimplemented with the same priors, EM
updates and stopping rule. 28 claims were tested; `training-duration` is
blocked as `data_missing`, as every session is stage 5 or 6. `cohort-inclusion`
is partial, the 13 mice matching but 376 sessions passing the criteria against
the paper's 381, and every later analysis uses those 376.
`fig5c-movement-index-best` is not reproduced: the movement index decodes the
states at 68.6% against 71.5% for pupil (p = 0.086), and the code's conditions
that favour it keep pupil information, so they do not test the claim.
`fig2a-state-types` reproduces on an assumption, one state of BW059 with no
trial of posterior 0.8 or more in the sessions with the optimal state being
typed on all sessions, where Figure2.py's nansum would score it 0 against
every template and mislabel the optimal state. `fig2c-dwell-times`,
`figs4-r2-individual-movement`, `fig3-distance-from-optimal-pupil`,
`fig4a-lower-variability` and `fig4b-variability-at-transitions` are partial,
their tests holding but some values outside tolerance or some tests failing
(the optimal dwell is 43.8 trials against 37, and the distances from the
optimal pupil are 8.8, 16.0 and 11.8% against 7, 12.6 and 9). The author's
first run used 3 cross-validation initialisations in place of 10, to fit the
30-minute limit, and visual stimulus values of 1, 0.8 and 0.6 for every
session, and gave `fig2b-optimal-occupancy` and `fig3f-movement-index-inverted-u` as partial.
The author asked a reader no questions, so the answer run and the following
author run changed nothing. Round 1 agreed with all outcomes but found that 2
of 3 random starts of the EM ended in a worse local optimum on synthetic data,
that the movement-index variants keep pupil information, that the stationary
rule counted backward running, that the template matching of other states
cannot fail, that the dwell code adds zero-length epochs, that pupil r2 rests
on one split with an outlier (BW051), and that the visual stimulus values
could come from the `visual_gabor_angle` column. In reply every state model
was re-fit with 10 initialisations and the stimulus values of
`get_stim_vals`, which moved fig2b (indeterminate share 13.1% +/- 1.6%) and
fig3f (r2 0.574 against the 0.57 bound) to reproduced, and variants were added
for the other points; the notebook then took 1550 s, close to the limit. Round
2 agreed with all 29, calling fig3f marginal, and found sentences the outputs
did not support, which were corrected; three of its mismatches (1,879 against
1,821 stationary trials, locomotion r2 0.570 against 0.567, p = 0.051 against
0.053) did not appear in the author's runs, and the author ascribes them,
without confirming it, to a run on another machine and speeds rounding to zero
in the smoothing filter (9,869 trials are below 1e-9 m/s but not exactly 0);
both values are now given. The author's run took about 100 minutes (09:19 to
11:00 UTC); a first version of the model fitting diverged and was fixed with
damped Newton steps before any reported fit. The notebook ran in 13 to 14
minutes at first, 581 s after the answer, 1550 s after round 1 and 15.7
minutes in the last run.

The dandiset holds 391 stage 5 and 6 sessions of the 13 included mice, where
the paper analysed 381; the paper's inclusion criteria select 376 of them
counted from the reward series and 375 counted from the hits (14 fail both,
13 with fewer than 100 rewards and 1 with less than 20% at one port, and 3
fail one count only), and nothing in the dandiset marks which sessions the
paper used. The training sessions before stage 5, the other stage 5 and 6
sessions of the 500 the paper names, and the 18 mice that did not meet the
inclusion criteria are not in the dandiset, so the training duration (21 +/- 8
sessions) cannot be tested. The running_speed series of every file is
labelled cm/s, but its values (session medians around 0.07, 99th percentiles
up to 0.67) are in m/s, the unit of the paper and of its code. In 38 of the 391
sessions the post hoc pupil diameter series is present but entirely missing
values (14 of BW046's 34 sessions). The rig names in the session metadata are
spelled several ways for what appear to be the same rigs (Box 1, Box1,
Boox1). No recording is deposited twice, and a response against no-response
contrast is consistent with the measures sharing the trial clock. A question
is put to the paper's authors: how Figure2.py handled a state with no trial of
posterior 0.8 or more in the sessions where the optimal state occurs, and
which 381 sessions were analysed.

The author's points on the protocol: the paper's method does not fit the
30-minute notebook limit in full (10 initialisations per fold and 1000 shuffle
runs for the decoders), and the reductions to 3 initialisations and to 3 runs
per shuffled condition with 20 null runs were recorded as deviations, not as
`too_large`, as blocking would have blocked almost every claim resting on the
state fits; the paper's ssm fork is not a locked dependency, and the protocol
says nothing about reimplementing a method against installing the original,
so the reimplementation was recorded as a deviation; the protocol does not say
what to do when the data trigger a latent bug in the paper's code, and the fix
was treated as an assumption with a question to the authors; and there is no
rule for a session set the dataset cannot reconstruct, so the paper's criteria
were used with a `selection_undocumented` finding.
