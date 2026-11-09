# 001605, Funamizu et al. 2016

Eleven claims reproduced, two partially, nine not reproduced and 18 blocked,
ten as methods underspecified, six for missing data and two as too large; no
outcome rests on an assumption. All 40 claims are on the dandiset. The first
verification round agreed with 25 of the 40 outcomes as they stood and the
second with 38, disagreeing on the too_large blocks of
`fig3b-distance-over-time` and `svm-correlations`, and nothing was proposed
after the second, so there was no third round. It pins version 0.251007.0553,
the published version. The paper, Funamizu, Kuhn and Doya, "Neural substrate of
dynamic Bayesian inference in the cerebral cortex" in Nature Neuroscience,
images layers 2, 3 and 5 of PPC and PM in eight mice with two-photon calcium
imaging during auditory virtual navigation to a goal whose sound is continuous
or intermittent, and reports the licking behaviour and the muscimol
inactivation of PPC (Fig. 1), the classes of task-relevant neurons (Fig. 2), the
goal-distance coding of single neurons (Fig. 3) and a Bayesian decoder of goal
distance with its error, MAP and uncertainty with and without sound (Figs. 4 and
5). The claims were written from the version of record and its supplement, with
the display equations of the Methods garbled in the text; the paper's Matlab
scripts are available only on request, so no code was read. Thirty-two claims
were run. Reproduced are `session-counts` and `neuron-counts` (94 sessions of 8
mice and 41,031 ROIs, every count exact), `fig1c-licking-without-sound`,
`fig2d-goal-distance-ppc-more`, the two Fig. 3c ramp claims,
`supp11-sound-reduces-error`, `fig5a-map-follows-continuous`, `fig5b`, `fig5cd`
and `fig5c`. Partial are `supp6-distance-not-sound` (23 of 24 comparisons) and
`fig4e-ppc-lower-uncertainty` (479 of 480 bins, 99.8%, in two of 16
configurations). Not reproduced are `behaviour-timing` (9.30 s to reward
against 7.4 +- 0.1 s), `lick-goal-correlation` (two sessions at r 0.218 and
0.227 below the bound of 0.232), `neuron-classes` (2 of 12 counts within 10%,
the others 12 to 41% above the paper's), `fig2d-task-relevant-proportions`,
`supp9-preserved-representation`, `fig5a-map-decreases-without-sound` (13 or 14
of the 16 tests needed), `fig5-layer3-steeper-than-layer2`, `supp13-map-speed`
and `lognormal-decoder-better`, where the Gaussian decoder has the lower RMSE in
15 to 18 of 18 settings. The two Fig. 5 failures turn on the MAP sitting at 0
cm, the lower end of the decoded range, in 51.6% of frames of the intermittent
1 zone at 8.4 to 0 cm; a decoder whose range extends past the goal was not
tried and is left for a new attempt. Ten claims are blocked as methods
underspecified because their readings disagree: the baseline of the
task-relevance t-test (O1) for `fig2d-after-vs-before`,
`fig2d-layer-distance-preference` and the three Supp. Fig. 8 claims, the
no-sound zone for `supp1-licking-speed`, the chance level for
`fig4-above-chance`, the bin width for `fig4c` and `fig4d`, and the coefficient
and frames for `tuning-similar-ppc-pm`, whose criterion itself directs a block.
`fig3b-distance-over-time` (about 29.7 h over the notebook's 4 workers) and
`svm-correlations` (about 173 min, and 43 min for one classification reading
with 37 min of the 60-minute limit left) are blocked as too large. The author's
first run adopted one reading where readings disagreed and gave 21 reproduced,
4 partially, 6 not reproduced and 9 blocked. The author asked a reader whether
the Supp. Fig. 9b difference is signed; the reader answered that it is and
amended the criterion, and the author-answers run moved
`supp9-preserved-representation` from reproduced on two assumptions to
partially reproduced. Round 1 disagreed with 15 outcomes, nine of them claims
settled by an adopted reading, which the claims file blocks, three partial
outcomes under criteria with no partial rule, `fig4e`, and the two too_large
blocks, which it would have called other as the data are present, and found
that the permuted-distance chance still decodes distance, that the widths were
quantized by a 25-point grid, that the speaker table and the frame sums were
asserted without output, that the zero MAP slopes were never checked and that
the lick onset was untested; in reply thirteen outcomes changed to the
verifier's, the assumptions were withdrawn, the speaker table, the stored 30.9
Hz rate, the form of the lick frequency, the MAP distribution, k-means per
session and a bounded optimizer for the widths were added, the timings were
moved into the notebook on real data, and two questions for a reader (the
supp1 zone and the chance level) were filed in `questions/001605.yaml`. Round 2
found that the quoted timings (0.66 s, 36.6 h, 146 h, 0.23 s, 1.2 h) were not
the printed ones (0.50 s, 27.6 h, 110.4 h, 0.24 s, 1.3 h), that the SVM
estimate ignored the 4 workers and had none for reading (b), that the
`speaker_on_matrix` sentence rested on no output, and that equal quarters fit
the Supp. Fig. 9a group sizes better (summed share difference 0.63 against
3.09); in reply the SVM was timed on the session of median neuron count, the
text was corrected, `speaker_on_matrix` was read in all 94 files and the supp9
point was filed as a further question, while "8 to 11" bins for `fig4d` was
kept as it matches that run's print. The notebook ran in 24.6 min at first,
2832 s after the author-answers run, 24 minutes after round 1, whose first full
run timed out at 60 minutes because linear-algebra threads competed for the
four cores, and 1,418 s at the end. An empty harness directory,
`entries/funamizu-2016/.claude/.cc-writes`, was left inside the entry
because its removal was denied.

The dandiset holds only the 94 imaging sessions, so the muscimol experiment
(three further mice, Fig. 1d to g and Supp. Fig. 2) and the sound-mapping trials
recorded before each imaging session (Supp. Fig. 4) are missing and six claims
cannot be tested; the paper's data page, checked outside the notebook, names no
other deposit. The description promises "sound on/off indicators" and describes
`sound_on_off` as "any speaker on", but in every file `sound_on_off` and
`speaker_on_matrix` are on only in the first frame of each trial (150 frames),
and every `speaker_presentations` row lasts one frame at a trial start (6 to 26
rows per trial start, one per speaker listed), so the task sound is not
recorded and sound and no-sound zones must be computed from the condition and
the distance. Licking is stored only as `lick_rate`, a held
1/inter-lick-interval value capped at 10 Hz, without lick times or a
description of how it was derived, so lick counts and first licks can only be
approximated. Each trial record runs from one start tone to the next, and the
goal time and the first reward edge are not stored per trial; derived from the
position and reward series, the mean time to reward is 9.30 s (s.e.m. 0.11 s
over sessions) against 7.4 +- 0.1 s in the Methods, and 0.48% of trials take
over 20 s against 2.71%. Against this, the files hold exactly the paper's
counts (94 sessions, 8 mice, sessions per area and layer, and 41,031 ROIs equal
to the active-neuron counts), `dF_over_F` equals (R - mean R)/mean R of
`RawFluorescence` to 3e-5, as the Methods define dR/R, and no recording is
deposited twice. With the decoder as described, a Gaussian likelihood beats the
log-normal one, contrary to the Methods, which may come from details the
Methods leave open (the positive shift, the decoded range). Of the paper
itself, the Results give the uncertainty decrease "between 25.8 and 0 cm" where
the figures use 25.1 cm, the Fig. 4c legend calls RMSE "the expected squared
deviation", and the Results and Supp. Fig. 8a give different P and z ranges for
the PM no-sound slopes. Questions are put to the paper's authors: the baseline
of the task-relevance t-test and whether k-means was run per session or pooled;
the chance level of Fig. 4b, the bin width of Fig. 4c to e and the borders of
the before-reaching groups of Supp. Fig. 9; and which coefficient of the
distance fit was compared between PPC and PM and over which frames the
regressions were fitted.

The author's points on the protocol: the claims file's header blocks a claim
whose readings disagree while step 1.6 allows adopting the best-supported
reading, and the first run adopted assumptions except where the criterion
itself says to block; for criteria without a partial clause, partially
reproduced was used where the effect held in part; a choice forced by how the
data are stored, such as licks as a capped frequency, is not a method reading
and was treated as a standard choice with a variant shown; a too_large block
needs a time estimate while numbers from outside the notebook may not enter the
record, so the first estimate was timed on synthetic data of the same size; the
claims file's permuted-distance chance does not measure chance, and the other
reading was adopted without asking a reader; the clock check used the
reward-to-goal lag and the decoder against the flat prior, not a decoder with
shifted labels; and the per-animal breakdown is given only for the behaviour and
neuron-class claims.
