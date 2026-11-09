# 000139, Churchland et al. 2010

Fourteen claims reproduced, two partially, two not reproduced and five
blocked, all on the dataset. It pins version 0.220113.0408, its only published
version, as the paper cites none. The paper, Churchland, Cunningham, Kaufman,
Ryu and Shenoy in Neuron, records three rhesus monkeys making delayed reaches
and reports that preparatory and peri-movement tuning in PMd and M1 are only
weakly correlated (mean r = 0.13 for the J-array dataset), that a preferred
direction (PD) captures preparatory tuning best when expressed in a space
built from peri-movement activity, better than kinematic, task and EMG
spaces, and that a simulated linear dynamical system shows the same pattern.
The claims were written from the NIH author manuscript in PubMed Central
(PMC2991102) with its one supplement, not the version of record; the paper
links no code. The J-array claims were tested: the recordings, the tuning
correlations of Figure 4D and 4E and Supplemental Figure 1, the PD performance
of Figure 6D, the controls of Figure 7, the anterior and posterior
comparisons, and the Figure 8 simulation. The claims on the speed-task
datasets of monkeys A and B, the single-electrode monkey J dataset and EMG
(Figures 4A to 4C, 6A to 6C and 6E, and the AP regression for those datasets)
are blocked as `data_missing`, and `prep-activity-more-anterior` as
`metadata_insufficient`, as nothing in the files says which unit id prefix is
the PMd array. `fig6-preparatory-dimensionality` is not reproduced (12 PCs
for 90% of the variance against 6.3 to 11; 17 with condition labels shuffled,
and 7 by cross-validated PCA), and `fig7c-anterior-posterior-performance` is
not reproduced, as neither array is within 10% of the random halves (6-D, S
fixed, 0.761 and -0.402 against 0.455). The author's first run gave 13
reproduced, 2 partially, 3 not reproduced and 5 blocked. The author asked a
reader no questions, so the answer run and the following author run changed
nothing; two questions were put to a reader during the revisions, after the
answer step, on whether the partial clause of `j-array-recordings` fits a
27-condition session and on the width of the fig7c band (+/- 0.046 against
an SD of 0.153 for the random halves). Round 1 agreed with 20 of 23 outcomes;
the author took its outcomes for `fig6-maze-task-spaces` (from blocked as
`methods_underspecified` to reproduced, as the claims file names both segment
divisions) and `prep-activity-more-anterior` (from not reproduced to blocked),
and kept `fig6-dimensionality-peak` reproduced, resting on S fixed across
folds, where the verifier gave partially reproduced. Its points led to a
label-shuffled reference for the 5 spikes/s threshold, a per-unit permutation
test, chance levels for the spaces, Figure 7C run with the paper's upper limit
including the fitted neuron, a cross-validated ranking for Supplemental Figure
1, cross-validated PCA and a printout of the session description and the
electrode metadata. Round 2 agreed with all 23, the verifier changing its
round-1 position on the dimensionality peak after the chance curves (a fall
of 2.292 from k = 6 to 14 with S fixed and 0.094 with S recomputed), so there
was no third round; it found statements the outputs did not support, among
them "Only 59" units passing on shuffled labels, chance stated for every space,
upper limits all at or below zero where 2 of 8 are, 350 trials for units the
test file does not hold and a sentence on dandiset 000128 that nothing
printed, which were corrected, and `j-array-recordings` was marked as assumed.
Some outcomes rest on weak ground: `fig4e-correlation-time-course` passes in
the main selection only with the trace spliced at the median RT, which sets
the decline (-263 ms) at the end of the preparatory window, and without the
splice holds in 6 of 8 selection readings with all preparatory neurons and 3
of 8 with the neurons of Figure 4D; `suppfig1-population-psth-weak-movement-tuning`
does not survive cross-validated ranking for the claim's 17 neurons (ratio
1.115); `fig4d-mean-correlation-j-array` passes p < 0.05 by the t-test only
(p = 0.042, Wilcoxon p = 0.071) and in 5 of 8 selection readings;
`fig6-maze-task-spaces` has segment directions above zero in 2 of 8 selection
readings and rests on segments equal in time; and the check of
`fig8-linear-dynamics-simulation` is weak and rests on the full-cycle gray
interval. The author's run went from 19:44 to about 20:23 UTC and nothing
failed; the notebook ran in 362 s at first and in 620 s in the last run.

The dandiset holds one maze-task array session of monkey J (2009-09-29) cut
for the Neural Latents Benchmark, with 152 units, 27 conditions (9 mazes in
three versions) and 250 labelled trials, where the paper's J-array dataset had
108 conditions and about 2166 trials per neuron; the speed-task datasets of
monkeys A and B, the single-electrode monkey J dataset and all EMG are not
deposited, so 4 of the paper's main findings cannot be tested and the others
rest on 6 to 10 trials per condition. With so few trials a median of 59 of 152
units pass the 5 spikes/s threshold on shuffled labels against 75 observed,
only 43 of the 76 PD neurons have tuning distinguishable from noise, and the
split-half reliability of preparatory tuning is a median r of 0.374. Nothing
in the files or the dandiset metadata says whether this session is the
paper's J-array recording or how its 27 conditions relate to the paper's 108;
the trial timeline is rebuilt, so the files cannot show whether the session
held other mazes. Every unit's electrode reference points at a row of the PMd
electrode group, although the unit ids put 77 of the 152 units on a second
array, whose references (rows 14 to 94) match their channel numbers without
the offset of 96 that would place them on the M1 rows. The electrode table's
x, y, z and impedance columns are empty, and nothing says whether id prefix 1
or 2 is the PMd array. The 100 test trials are 700 ms segments without
condition labels, go cue or behaviour, for the 114 held-in units only, and how
the trials and the 9 mazes were chosen from the session is not described.
Five questions are put to the paper's authors: what the proto-trial of the
trial selection is and whether the horizontal and vertical velocity profiles
are compared separately or together; whether tuning strength is the range or
the standard deviation of condition means; whether the PCA-based space S is
recomputed without the left-out condition; whether the reach is divided into
segments of equal time or equal path length; and how movement onset was
detected, where the Figure 4E trace is spliced and what the gray interval of
Figure 8 is.

The author's points on the protocol: it does not say whether a reading adopted
for one claim carries to the claims that depend on it, so one main reading was
adopted for all and the dependent outcomes marked assumed; it is unclear
whether `assumed` covers data identity, such as whether the 27 mazes are among
the paper's 108; it gives no rule for a criterion whose reference value comes
out degenerate, as the Figure 7C normalization did; the criterion's rule that
any reading suffices and step 1.6's rule that all open-detail readings must
agree can conflict, as in suppfig1; and the repository root has untracked
files from the sandbox.
