# 000138, Churchland et al. 2010

Nine claims reproduced, one partially, two not reproduced and two blocked on
the dataset; `fig8-oscillator-model`, a simulation with no recorded data that
the claims file marks `with_inputs`, is counted apart and reproduced. It pins
version 0.220113.0407, its only published version, as the paper cites none;
the draft holds the same two blobs. The paper, Churchland, Cunningham,
Kaufman, Ryu and Shenoy in Neuron, records three rhesus monkeys making delayed
reaches and reports that preparatory and peri-movement tuning are only weakly
correlated (mean r 0.13 for the J-array dataset), that a preferred direction
(PD) captures preparatory tuning best when expressed in a space built from
peri-movement activity, and that a simulated linear oscillator shows the same
pattern. The claims were written from the NIH author manuscript in PubMed
Central (PMC2991102) with its one supplement; the main-text PDF was not
available, so Figure 6A-D and the per-dataset values of Figures 6 and 7 could
not be read, and the paper links no code. The J-array claims were tested on
the dandiset's one session: the tuning correlations of Figure 4D and 4E, the
anterior and posterior comparison, the dimensionality of preparatory
activity, the PD performance of Figure 6, the controls of Figure 7 and the
Figure 8 simulation. The single-electrode claims of Figure 4A-C and the
summary of Figure 6E, which needs monkeys A and B, the single-electrode monkey
J dataset and EMG, are blocked as `data_missing`.
`fig4e-correlation-time-course` is not reproduced, as the mean correlation at
movement onset is 0.218 and 0.129 to 0.218 over all eight readings, against a
bound of 0.1, and `fig7c-anterior-posterior` is not reproduced, with the
anterior array at 0.963 and the posterior array at 0.615 of the random halves.
`fig4d-tuning-correlation-j-array` is partially reproduced (mean r 0.195,
mean Spearman r 0.212, p = 0.023). The author asked a reader no questions, so
the answer run and the following author run changed nothing. Round 1 agreed
with all 15 outcomes; its points led to the refit curves for Figure 6,
per-condition trial counts under every reading, 20 draws in every variant of
fig7a and fig7c, the spread of the random halves and the overlap of the fig7d
draws. On its reading of the Supplemental Procedures the author first changed
the fig7c upper-limit space to leave out the unit being fit; round 2 agreed
with all 15 but judged that keeping the unit in is at least as well
supported, as the paper builds that space "from the preparatory activity of
all neurons" and states an exclusion only for the peri-movement space, and the
author changed it back, with anterior again better than posterior, as the
paper reports. Round 2 also found statements the outputs did not support,
among them a Spearman range of 0.147 where the output prints 0.146, a README
run time of about ten minutes, a test-file sentence resting on 20 of 122
units, the word "collapses" for an unprinted curve and an unmeasured effect of
overlapping draws on fig7d, which were corrected; nothing was proposed, so
there was no third round. In round 1 the first cell still held the author's
outcome table, which the verifier did not use. Some outcomes rest on weak
ground: `fig4d-tuning-correlation-j-array` rests on 20 units and is above zero
at p < 0.05 in 2 of 8 readings (onset from a speed threshold, a median 14 ms
later, gives p = 0.166, and a ratio of 1.25 gives p = 0.069);
`supp-preparatory-dimensionality` gives 11 components, at the upper end of
6.3 to 11, with 12 under the per-axis trial selection and 14 and 13 on each
half of the trials; `fig6-dimensionality-trend` holds in 91% of combinations
with the space computed once and 6% with it refit; `fig7a-shuffled-space-poor`
holds with the space refit by 0.001, within the noise of the draws (standard
error 0.009), and fails under the per-axis selection; and
`results-ap-location-no-effect` is a claim of absence tested on 20 units. The
author's run went from 19:45 to 20:27 UTC and nothing failed; the notebook
took 5.5 to 5.7 minutes at first and 7.6 minutes in the last run.

The dandiset holds one session of monkey J's array recordings on the maze
task (2009-10-06), cut to 500 trials over 27 conditions for the Neural Latents
Benchmark, where the paper's J-array dataset had 108 conditions and a mean
2166 trials per neuron; the single-electrode datasets of monkeys A, B and J
and all EMG recordings are not in it, so two of the paper's main findings
cannot be tested and the rest only on J-array. Nothing in the dandiset or the
paper says whether this session is the one behind the paper's J-array
dataset; the file has 162 units where the paper reports 146 isolations. Every
unit's electrode reference points into the PMd group of the electrodes table,
although the unit ids encode a prefix (1 for 83 units, 2 for 79) and a
channel, and the referenced electrode is the channel minus one for both
prefixes, so the 79 units of one array reference electrodes of the other.
Which prefix is the PMd array is not stated and all electrode coordinates are
NaN, so the anterior and posterior analyses rest on taking prefix 1 as PMd,
supported only by its stronger preparatory tuning. Hand, cursor and eye
position are at 1 kHz and only within trials, where the paper tracked the hand
at 60 Hz and the eye at 240 Hz, and the resampling is not described. Eight
trials have a delay of 0 ms or less (down to -2 ms). The paper gives 2166 mean
trials per neuron for the J-array dataset in the Results and 2155 in the
Methods. Four questions are put to the paper's authors: whether the PCA space
is computed once from all conditions or recomputed without the left-out
condition; how the maze proto-trial was defined, over which window, and
whether the horizontal and vertical profiles each had to pass r > 0.9; what
"spikes/s of preparatory tuning" measures and how movement onset was detected, as with the range 92 of
162 units pass the 5 spikes/s criterion and with the SD 6; and whether the
Figure 7C upper-limit space included the neuron being fit, and at which
dimensionality.

The author's points on the protocol: it does not say whether to run the full
product of readings or one at a time, so the full grid was run for Figure 6
and 7B and one at a time elsewhere; it does not say what outcome a claim
spanning four datasets gets when only one is in the dandiset, so the testable
part was judged and the missing datasets listed as deviations; `measured`
asks for one value per expected value, which fig7b's second value cannot
give; it is unclear whether a reading the author adds counts under the
criterion's any-reading rule or under step 1.6, which was followed; fig8 is
marked `with_inputs` but uses no outside input, a case the protocol does not
cover; and the repository root has untracked files from the sandbox.
