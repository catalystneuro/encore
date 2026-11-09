# 000128, Churchland et al. 2010

Eleven claims reproduced, one partially, three not reproduced and seven
blocked, all on the dandiset. It pins version 0.220113.0400, the only
published version, whose draft holds the same two files with identical
contents. The claims were written from the PubMed Central author manuscript
and its supplement, without a PDF of the main text, so the main figures were
read from their legends; the claims check added
`fig4-no-separate-populations`, so the file has 22 claims. The author put three
questions to a reader, and the answers set aside the proto-trial reading T1
(which kept 73.8% of trials with delay over 400 ms and left two conditions
empty) and the tuning measure S2 (which selected no neuron for the correlation
claims), and named two readings of the normalising maximum in
`suppfig1-population-averages`, both already run. The counts moved from 7, 1, 2
and 12 to 11, 1, 3 and 7: `fig3-maze-most-not-maintained`,
`fig6-peri-movement-space-best`, `fig6-each-dimensionality` and
`fig7a-shuffled-space-poor` moved from blocked as `methods_underspecified` to
reproduced, and `fig6-performance-vs-dimensionality` to not reproduced. Round 1
gave its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with all 22, and round 2 agreed with all 22, so
there was no third round. The paper, "Cortical preparatory activity:
representation of movement or first cog in a dynamical machine?" in Neuron,
records units in PMd and M1 of three monkeys making delayed reaches in a speed
task and a maze task, with single electrodes and, for monkey J, two
96-electrode arrays, and reports that preparatory and peri-movement tuning are
only weakly correlated and that preparatory tuning is best captured by a
preferred direction in the space of the population's peri-movement response.
Only the J-array maze session could be tested: its counts, the tuning
correlations and their time course, the population averages, the PD spaces,
the controls and the two model simulations. The speed task, single-electrode
and EMG claims are blocked as `data_missing`, and the two anterior-posterior
claims as `metadata_insufficient`. `fig4d-mean-correlation-jarray` is not
reproduced because the mean r is 0.051 and the mean Spearman r 0.072 against
0.13 and 0.11, with no test below p = 0.05 (P1 0.47, P2 0.42, P3 0.61),
`fig6-performance-vs-dimensionality` because performance rises to its best at
k = 14 (0.518) and does not decline, and `prep-dimensionality` because 90% of
the variance needs 15 components (N1) or 18 (N2) against 7 to 11; the main
text says "at least 7-10 dimensions", which 15 and 18 would meet, and whether
the claim is a range or a lower bound is asked in a question. Some outcomes
rest on weak ground: the correlation claims use only 17 neurons that pass the
selection, so their tests have little power; fig3 rests on one neuron, unit
1581 (r 0.765), with the next largest r 0.457; the best k in the PD analyses
is the upper end of the tested range, an edge value and not a peak; the
preparatory separation in suppfig1 is positive by construction; and
`fig8-model-weak-correlation` has a criterion that almost any small value
would pass.

The dandiset holds only the J-array session of monkey Jenkins (2009-09-25),
with no speed task, no single-electrode recordings and no EMG, and the paper
names no other archive for them. Every unit's electrode reference points into
the first 96 rows of the electrodes table, labelled PMd, so by the file all
182 units are in PMd although the electrode groups describe one array in M1
and one in PMd; the reference equals the unit id's channel digits minus one,
which suggests the array offset was dropped in conversion. The electrodes have
no coordinates (x, y and z are NaN), and the leading digit of the unit ids (1
for 92 units, 2 for 90), which may be the array, is not documented, so no unit
can be placed on the anterior-posterior axis or on an array; regressing tuning
correlation on that digit, a variant that decides nothing, gives r of
magnitude 0.432 (p 0.084). The dataset holds 182 units where the paper reports
146 and does not record which units or trials the paper used, or that this
session is the paper's. 574 of the session's successful trials are in the test
file as 0.7 s segments around movement onset, without condition labels or
behaviour and with only the 137 held-in units, so they cannot enter a
condition-mean analysis; the test file has a clock of its own and no delay or
success column, and the train file's trial ids are contiguous, so the files do
not record which session trials the packaging dropped. Reading (a) of
`recordings-jarray` gives 2869 trials with the test file and 2295 without it,
and the 182 units fail under every reading. Other findings: 14 trials have a
negative delay (as low as -3 ms), where the go cue precedes the recorded
target onset.

The notebook ran in 152 s in the first run, 81 s after the answers and 121 s
after round 1, and `entry.py all` passed with 0 errors after round 2. A bug
found during development averaged an empty condition as zero rates and had
made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.
Round 1's points led to a table labelled by reading for `recordings-jarray`, a
per-neuron table for fig4d, the lost fig6-each-dimensionality comparison (the
2-D initial-velocity space, 0.238 against 0.223) printed, and checks of the
test file's clock and the electrode group descriptions. Round 2 withdrew its
round-1 point that the supplement's T-matrix might be a conditions by
(neurons by times) matrix, as the supplement defines it as c by n, so those
variants were removed; it also found statements the outputs did not support,
among them both fig4d means called below half the paper's where the Spearman
mean is 65% of it, the fig8 interval given as its outer envelope, an ambiguous
"91% of trials kept" for T2, and notes quoting T1 and S2 values the notebook
no longer prints, and these were corrected. Untracked dotfiles in the
repository root that the author did not create were left alone. The author's
points on the protocol: it does not cover a reading that selects no units; it
does not say what to do when a trial reading leaves a condition with no
trials; it has no rule for an undocumented substitute such as the unit-id
digit when the claims file's fallback, the array, is wrong in the data; its
check for a selection is written only for chance levels and false-positive
rates, though the paper's "~90% kept" works like one; the `recordings-jarray`
criterion says only when the claim is reproduced, not when it is partial; and
some details the criteria leave open below their stated readings were run both
ways and recorded as deviations.
