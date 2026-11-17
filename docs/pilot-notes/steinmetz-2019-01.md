# steinmetz-2019, Steinmetz et al. 2019

Twenty-six claims reproduced, one partially, ten not reproduced and three
blocked, two as other and one for missing data. Three outcomes rest on an
assumption, `edtable1-region-counts`, `supptable2-sessions` and
`fig3d-vision-localized`. The first verification round agreed with 26 of the 40
outcomes and disagreed on `suppfig2-rate-amplitude`, `fig2fg-miss-restricted`
and `fig5b-miss-more-than-passive`, which it held not reproduced where the
record had them partial, as their criteria name no partial outcome, and on the
11 kernel regression claims, whose block as too large it questioned, the data
being in the files and the limit unsourced; the author took all three changes
and tested nine of the eleven. The second round agreed with all 40, and the
author proposed `ed5h-choice-shuffle-fpr` as reproduced on the mean of five
shuffles, so there was a third round, which reviewed that one claim and did not
agree, as the criterion is written for one shuffle and the averaging was chosen
after the first shuffle failed; the outcome stays not reproduced. The dandiset
is pinned at 0.240329.1926, its only published version; the paper cites no
version. The paper, Steinmetz, Zatka-Haas, Carandini and Harris, "Distributed
coding of choice, action and engagement across the mouse brain" (Nature 576,
266-273), records 29,134 neurons with Neuropixels probes in 39 sessions of 10
mice doing a visual task with left, right and NoGo responses, and reports that
visual coding is confined to visual areas, action coding is spread across the
brain, choice coding is rare and restricted to frontal cortex, basal ganglia and
midbrain, and engagement shows in pre-stimulus activity everywhere. The claims
were written from the author manuscript (PMC6913580) as Europe PMC text with
both supplement files, without a PDF, and from the paper's code at commit
9a0bea8; the claims check changed twelve claims and the opening comment and left
four points open, for 40 claims. Reproduced are the behaviour claims of Fig. 1
(easy trials 1.71% incorrect and 10.12% Misses on engaged trials),
`fig1d-reaction-time-difficulty` on the trials of definition T only,
`ed1q-wheel-choice-decoding` (48.9% and 94.8%), `recording-counts` (29,283
neurons, 9,538 engaged trials, the paper's count), edtable1 (38 of 42 regions,
exactly the threshold), supptable2, `task-modulated-fraction` (13,532 of 22,434,
60.32%), `fig2de-activity-order` under the half-maximum latency only, every
engagement claim of Fig. 5 and Extended Data Figs. 6, 7 and 9, among them
`fig5f-engagement-index` (7.85 a.u. against 8.42 ± 0.84, p = 1.2e-5) and
`fig5d-go-miss-matches-task-passive` (r = 0.641), `ed7b-detect-probability-widespread`,
`fig4d-jpecc-vis-leads`, whose VIS-Midbrain lead rests on one uncorrected time
point at 0.08 s, `fig3c-variance-explained` (median VE 0.12%), fig3d, which fails
with the Figs. 3 to 5 set as denominator, and `fig4f-contralateral-preference`
(100% and 38.5%, p = 9.6e-7). Partial is `fig3e-action-global`, as VISrl has no
Action neuron. Not reproduced are `passive-no-movement` (84.63% against 94.1 ±
0.6), suppfig2 (amplitude d' 0.201 against 0.10 ± 0.02), fig2fg, whose
condition (iii) fails (ipsilateral Miss 1.117% against half of 2.082%), fig5b,
on the 36 sessions kept against the criterion's 34,
`fig4d-jpecc-no-lag-frontal-midbrain` (one uncorrected point, none after
Bonferroni), `ed4f-focality` (0.092, 0.045 and 0.029 against 0.079, 0.069 and
0.040), ed5h (4 of 2,871 neurons, 0.14%, below 0.33 ± 0.17%),
`fig4b-choice-regions` (48 midbrain and 39 forebrain neurons against 54 and 48,
and 1 in VISp), `fig4fg-opposed-activity` (27.1% and 5.1% against 54% and 21%)
and `ed7c-choice-probability-restricted` (no frontal region marked, MOs share
6.7% against 20.8%). Blocked are `fig4c-choice-timing` and
`ed5g-ipsilateral-vision-rare`, as other, since the decoding from the kernel
model's residuals was not written although neither data nor time stopped it, and
`histology-alignment-error`, for missing data. The author's first run had 21
reproduced, 4 partially, 3 not reproduced and 12 blocked, the 11 kernel claims
as too large on a timed fit of one neuron. The answer run answered the author's
two questions, both as misreadings by the claims file: Extended Data Table 1
counts every neuron of the 42 regions, and the jPECC PCA is fitted across time
points and trials as the Methods say; in the author-answers run edtable1 and
fig4d-jpecc-vis-leads rose to reproduced. Round 1 found that fig2fg compared Miss
fractions on different session sets, that the kernel block rested on one neuron
of one session, that no list showed why 36 sessions are kept, that suppfig2
took `spike_amps` for the waveform amplitude, that fig5d and ed7f may need all
neurons, and that the clock of Tatum_2017-12-09 was not followed up; in reply a
coordinate-descent solver on the basis of the code's CanonCor2all.m fitted the
full model for 13,852 neurons in about 3 min, the matched comparison and the dropped
sessions were printed, the amplitude moved to `waveform_mean`, both
correlations held on all neurons, and the session's units showed detect
probability (16.9%, chance 5%). Round 2 found that the kernel model passes 2,886
neurons into the nested tests against about 4,240, that the fig3d method text
named the other denominator, and stale numbers in the README and record; in
reply four details of the code's fits were run as a variant, which passes 3,199
and changes no outcome, the solver was checked against scikit-learn (largest
difference 3e-6), and the text was corrected. The author's run took about 1 h 40
min; the notebook ran in 773 s at first, with peak memory 2.08 GB, 985 s after
the author-answers run, 17 min after round 1, 1,658 s after round 2 and 2,084 s
after round 3. `tools/entry.py lock` twice wrote a `python:` field the entry
schema rejects, deleted by hand, and the round 3 verifier gave the pooled
denominator as 14,317 where it is 14,267.

`units/peak_channel` is 1-based, which its description does not say: row
peak_channel - 1 of the electrodes table matches the unit's cluster depth
(median difference 8.0 um, against 13.4 um), and every unit's region depends on
it. Channel locations mix levels of the Allen hierarchy, 2,262 curated units
carrying finer labels (SCig, LSr, COA, TT, SCsg, ORBm, LSc, PIR, DP) and others
broad ones (TH, MB, CA), and the paper's counts per region come back only after
mapping the finer labels to their parents, which the dandiset does not
document; with labels as given edtable1 matches in 33 of 42 regions and
supptable2 in 25 of 39 sessions. The `rate` of the `starting_time` of
`wheel_position`, `lickPiezo` and `face_motion_energy` holds the sampling
interval in seconds (0.0004, 0.002 and 0.0253), not a rate in Hz.
`wheel_moves` is an IntervalSeries whose `data` has half the length of its
`timestamps`. `spike_amps` and `waveform_mean` give no unit, and the trial
table's `included` flag differs from the Methods' disengagement rule on 1.7% of
trials, although it gives the paper's 9,538 trials exactly. The Methods drop 5
of 39 sessions from the pupil analyses for unusable video, and the dandiset does
not say which; eye_area is in all 39 files, with missing values in two. There
is no histology (DiI spot coordinates, slice images) or electrophysiological
landmarks, so the probe localization cannot be checked; the figshare deposit the
paper names (doi:10.6084/m9.figshare.9598406) was not examined. Genotypes are
written differently from Supplementary Table 1, while sexes, ages and the 39
sessions match, and no recording is deposited twice. The kernel model of the
paper's code runs on the dandiset but passes 2,886 of 13,852 task-responsive
neurons into the nested tests, against about 4,240 in the paper; four details
of the code's fits raise this to 3,199, and the rest of the gap is unexplained.
The code's jPECC.m fits a PCA per time bin where the Methods fit one across time
points and trials, and kernelFitBasic.m keeps neurons whose test returns no
p-value, under a "BUG" comment. Questions are put to the paper's authors: how
neurons with no baseline spike, about 21% of them, whose z is infinite, were
treated; which count of "fewer than 10 such trials" leaves 34 sessions, where
36 have 10 per group and 38 over the three groups; which window and movements
the 94.1% of passive presentations without movement counts; and whether the
denominator of Fig. 3d,e is the neurons entering the nested tests or every
neuron of the region.

The author's points on the protocol: `tools/entry.py lock` writes a field the
entry schema rejects; for a claim of absence it says to judge on the paper's
test alone while the jPECC baseline window is still open; it does not say
whether an expected value outside tolerance overrides a criterion that does not
name it, as with 36 sessions against 34 in fig5f; several criteria have no
partial outcome; the rule that a claim depending on a blocked claim is blocked
forces out ed7c, whose choice probability part could run; a too_large block
needs a timing in the notebook, and the estimate also leaned on the claims
file's figure of about 4,240 neurons; the claims file follows the code where the
Methods differ, against the reader rule that the Methods come first; and the
claims file's wording of the asymmetry slice is ambiguous.
