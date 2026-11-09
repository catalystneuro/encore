# 000404, Athalye et al. 2023

20 claims reproduced, six partially, one not reproduced and two blocked. It
pins version 0.230605.2024, which the paper cites; it is the only published
version and the draft holds the same files. The paper, Athalye, Khanna, Gowda,
Orsborn, Costa and Carmena in Current Biology, records two rhesus macaques,
Monkey G (9 sessions, velocity Kalman filter) and Monkey J (4 sessions,
velocity point process filter), moving a cursor through a brain-machine
interface in a center-out and an obstacle-avoidance task with the same
fixed decoder in each session, and shows that the same command is issued by different population
activity in different conditions, that one linear dynamics model fitted on all
conditions predicts that activity and the next command better than shuffle
dynamics, and, in simulations built from the fitted dynamics and the decoders,
that such dynamics reduce the input needed. The claims were written from the
accepted author manuscript in PubMed Central (PMC10527529) with its supplement
and from the paper's code (pkhanna104/bmi_dynamics_code at commit 4161873); the
dandiset names the bioRxiv preprint (10.1101/2021.08.27.457931). 27 of the 29
claims were tested, most of them on a decoder gain recovered from the files, and
Monkey J's obstacle trial types were recovered with a target list from the
paper's code, recorded as an outside input. `figs3-low-dimensional-decaying-dynamics`
is not reproduced: Monkey G session 4 has 5 long-timescale eigenvalues for the
full model, outside 2 to 4, Monkey J session 3 has 1 for decoder-null dynamics,
outside 2 to 5, and Monkey G's mean frequencies (0.083 and 0.068 Hz) are
outside 0.09 to 0.11 and 0.054 to 0.066. The partial outcomes are
`figs1e-next-commands-differ` (Monkey G 1.873, above 1.844),
`fig3e-fractions-significant` (three or four of six fractions within tolerance
under every combination of readings), `fig4f-condition-specific-component` and
`fig5h-turn-predicted`, where the means hold but some sessions do not and the
partial verdict is a judgment the criteria do not provide for,
`fig5e-next-command` (Monkey J's condition left-out model pooled p = 0.003,
where the paper gives p < 0.001) and `fig6g-ofc-uses-distinct-patterns`
(Monkey J's decoder-null LME finds a difference, p = 0.020 to 0.021). The three
simulation claims rest on an assumption, Monkey J's 100 ms decoder fitted by
least squares to the decoder state, and `fig6d-decoder-null-dynamics-no-saving`
depends on it, as with the summed 5 ms gain Monkey J session 1's Wilcoxon test
gives p = 0.0016 and the criterion would give not reproduced.
`monkey-j-linear-command` is blocked as `data_missing`, as its criterion
directs when the files hold neither the point process filter's update nor its
parameters, and `figs5f-nonlinear-no-better` as `not_runnable`, as the rsLDS
package ssm cannot be installed in the entry's locked environment (its setup.py
imports numpy and Cython but declares no build dependencies); a timing run
outside the entry gave about 3 h of single-core compute for Monkey J and about
35 h for Monkey G. The author's first run gave 17 reproduced, nine partially,
two not reproduced and one blocked. One question was put to a reader, the units
of the Table S1 next-command errors; the answer, ten times the command's own
units as the code that prints the table applies the decoder to activity in Hz,
amended the criterion, and the following author run moved
`fig5f-condition-specific-next-command` from partially reproduced to reproduced
(3.973 and 7.052 against 3.956 and 7.324). Round 1 agreed with 28 of 29
outcomes, disputing only the block of figs5f, then `too_large`, as it was not
attempted even on the 4 Monkey J sessions. Its points led the author to the
pairs the paper's code scores (generalization_plots.check_ix_lo and
plot_loo_r2_overall), with every model compared with the shuffle on its own
pairs, which moved `fig5c-next-activity` and
`figs4g-generalize-condition-classes` from partially reproduced to reproduced
and freed fig4c, figs4b and fig5e from their assumption; it also moved
monkey-j-linear-command from not reproduced to blocked and figs5f from
`too_large` to `not_runnable`, and added the code's pairwise command matching
for figs6cd, the pooled reading of fig3e, a fit on rates in Hz for figs3 and
the run of the simulations with Monkey J's summed 5 ms gain. Round 2 agreed with
28 of 29 and with the block of figs5f only conditionally, so there was no third
round; it found five sentences the outputs did not support, among them fig3e's
"four of the six" in every combination and an Hz variant said to leave every
count unchanged when it refits only the full model, which were corrected. It
noted that fig5c rests on the code's scored pairs (7 of 9 Monkey G sessions for
decoder-null dynamics under the other readings) and that Monkey J's condition
classes and outside target list could not be checked. The author's run took
about 2 h 25 min (01:59 to 04:25 UTC) and nothing failed in the final runs; the
rsLDS timing test was killed at its 10-minute timeout. The two notebooks ran in
about 14 and 7 minutes at first and in 928 s and 498 s in the last run.

The files hold no decoder matrices (Kalman gain, steady-state cursor dynamics,
the point process filter's parameters), although the paper's Data availability
lists decoder parameters among the deposited data, and the code that wrote the
files has these lines commented out (online_analysis/nwb_utils.py). Monkey G's
steady-state gain and cursor update can be recovered exactly from the decoder
state and spike counts (variance accounted for above 0.99999 on 99% of
updates), but Monkey J's filter cannot, and its linear approximation must be
refitted. Monkey G's decoder state does not follow the steady-state filter on
0.03 to 0.95% of updates per session, among them the first updates of each
task entry, so the gain must be fitted on the updates the filter explains; the
gain so recovered accounts for 0.928 to 1 of the variance of the velocity
update over all updates. Monkey J's target_state and obs_details series carry
one target and obstacle for every trial of a session, as the writer indexes
frames with the position of each go event in the event list, so the last
trial's values fill the file; in Monkey G's sessions 0 and 1, checked,
target_state at reward is one value for all trials. Targets have to be read
from the cursor position at reward. The trials table has only start and stop
times, with no task, target, direction around the obstacle or Monkey J
obstacle trial type, and those trial types can be recovered only by matching
start and end positions to a target list in the paper's code. Units differ
within Monkey J's files: the cursor and decoder state are in m and m/s, while
target_state, obstacle_position and obs_details are stated in cm, and
target_state holds center-out targets in m (0.1027, 0.1384) and obstacle-task
targets in cm (-3.25, 8.13) under that one unit; Monkey G's files are in cm
throughout. Two questions are put to the paper's authors: how Monkey J's 100 ms
decoder for the simulations was built, as the expression for F in the Methods'
"BMI cursor dynamics" does not survive in the text, and in what units the
next-command errors of Table S1 are given, as they match the paper's only when
multiplied by 10.

The author's points on the protocol: it says to block `too_large` from a timed
subset but also that analyses run outside the notebook may never supply a
number in the record, and the rsLDS timing was run outside the notebook and
stated so in the notes; several criteria define partially reproduced only as
tests holding with values outside tolerance, not values within tolerance with
one session test failing or per-session ranges failing, and
`partially_reproduced` was used for an effect that holds only in part;
`measured` has no rule when no reading matches, and the first reading the
criterion lists was recorded; a detail no criterion named, which bins are
scored, changed outcomes and was handled under step 1.6 as an assumption with
both readings shown, which the protocol supports but does not anticipate for a
detail spanning many claims; and the prompt forbids bold apart from the Result
openers while the example entry uses bold labels, and the prompt was followed.
