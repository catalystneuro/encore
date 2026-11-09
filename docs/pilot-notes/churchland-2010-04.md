# 000140, Churchland et al. 2010

Five claims reproduced, one partially, eight not reproduced and six blocked,
all on the dataset. It pins version 0.220113.0408, the only published version,
as the paper cites none; the draft holds the same two assets. The paper,
Churchland, Cunningham, Kaufman, Ryu and Shenoy in Neuron, records three rhesus
monkeys making delayed reaches and reports that preparatory and peri-movement
tuning are only weakly correlated (mean r 0.13 for the J-array dataset), that
a preferred direction (PD) captures preparatory tuning best when expressed in
a space built from peri-movement activity, and that a simulated linear
dynamical system shows the same pattern. The claims were written from the NIH
author manuscript in PubMed Central (PMC2991102) with its one supplement, not
the version of record; the paper links no code. The J-array claims were tested
on the dandiset's one session: the tuning correlations of Figure 4D and 4E and
Supplemental Figure 1, the PD performance of Figure 6, the dimensionality of
preparatory activity, the controls of Figure 7, the anterior and posterior
comparisons and the Figure 8 simulation. The claims on monkeys A and B, the
single-electrode monkey J dataset and EMG (Figures 4A to 4C, 6A to 6C and 6E,
and the AP regression for those datasets) are blocked as `data_missing`,
`fig7c-anterior-posterior-performance` as `other`, as the upper limit used to
normalise performance is at or below zero, and `prep-activity-more-anterior`
as `metadata_insufficient`, as nothing says which unit id prefix is the PMd
array. `fig4d-mean-correlation-j-array` is not reproduced (mean r -0.079,
Spearman -0.020, no reading within 0.13 +/- 0.013 or positive at p < 0.05),
`prep-dimensionality-7-to-10` gives 16 components where shuffled labels give
16 to 17, and `fig6-perimovement-best-each-dimensionality` wins 7% to 36% of
comparisons against the 80% required. The author's first run gave 6
reproduced, 1 partially, 9 not reproduced and 4 blocked. The author asked a
reader no questions, so the answer run and the following author run changed
nothing. Round 1 agreed with 16 of 20 outcomes, and the author took all four
of its outcomes: `fig4-broad-near-zero` (from partially reproduced to not
reproduced, as the criterion has no partial rule), `fig6d-perimovement-best-j-array`
(from reproduced to partially reproduced, as 32 of 96 readings are partial),
`fig7c-anterior-posterior-performance` (from not reproduced to blocked) and
`prep-activity-more-anterior` (from not reproduced to blocked). Its points led
to a condition-shuffled null and a disjoint-trial reference, SEs and paired
tests for fig6d and the endpoint-speed space, a peri-movement space built from
the included units only, the anterior and posterior results under both array
mappings, and fig7a, fig7b and fig7d run on all six onset and proto-trial
settings, fig7d also under both readings of tuning. Round 2 agreed with all
20, so there was no third round; it found statements the outputs did not
support, among them 10 of 12 partial readings for fig4e where 11 are, a
Summary saying the peri-movement space performs best on the SD units where it
has the highest mean in 5 of 6 settings and no difference is significant,
"clearer tuning" that no output showed, 23 of 24 for the fig7d axes where 11
of 12 pairs agree, and the suppfig1 noise explanation stated as shown, which
were corrected, and `fig7b-window-start-slide` was marked as assumed. Some
outcomes rest on weak ground: `fig4e-correlation-time-course` and
`suppfig1-population-averages-lose-tuning` are met by trial noise too (in 18
of 20 and 11 of 20 shuffles), so their passes carry little evidence;
`fig7a-shuffled-space-poor` holds trivially under the range reading, where
the intact space is below zero, and its evidence is the 7 or 8 units of the SD
reading; `fig7b-window-start-slide` rests on the SD reading alone, as the
ratio is undefined under the range reading; `ap-location-no-effect-j-array`
is a claim of absence tested on 19 units; and `fig4-broad-near-zero`,
`fig6-maze-endpoint-speed-space-poor` and `fig6-dimensionality-trend` change
outcome between the range and SD readings of tuning. The author's run went
from 00:05 to 00:32 UTC and nothing failed; the notebook ran in 110 s at
first, 232 s after round 1 and 131 s in the last run.

The dandiset holds 100 trials of 27 of the 108 maze conditions from the
arrays of monkey J (1 to 4 trials per condition after the paper's delay rule)
and 142 units, where the paper's J-array dataset has about 2166 trials per
neuron; the single-electrode datasets of monkeys A, B and J and all EMG are
not in it, so four claims cannot be tested, and the claims that were tested
rest on condition means whose split-half reliability has a median of 0.20.
With condition labels shuffled across trials, 82 to 96 of the 142 units pass
the paper's > 5 spikes/s inclusion rule read as the range, against 93 with the
true labels, and the paper justified that threshold by its high trial count.
The dandiset says the data are "limited to 100 train trials and 100 test
trials" but not how the 27 conditions and 100 trials were chosen, whether the
session is the paper's J-array dataset, or whether the trials were filtered by
the paper's velocity-profile rule; 22 of the 100 train trials have delays of
400 ms or less, which the paper excludes. Every unit's electrode entry points
to an electrode of the PMd group (indices 0 to 94), though the unit ids carry
two array prefixes (72 units with 1, 70 with 2), and the electrode index
equals the channel number minus one for both prefixes, so the units of one
array point to the wrong group and which prefix is PMd is not stated. The
electrodes table has no positions or impedances (x, y, z and imp are NaN for
all 192 electrodes), so no unit has an anterior-posterior location. The test
file's 100 segments (0.7 s, movement onset at 0.25 s) have no condition, go
cue, target or behaviour and hold only the 107 held-in units; none duplicates
a train trial. Three questions are put to the paper's authors: whether the
inclusion rule's "spikes/s of preparatory tuning" is the range, the SD or
another measure, and whether the same measure was used for the 1.5 times
peri-movement rule; how the maze proto-trial was chosen, over what window
velocity profiles were correlated and how movement onset was detected; and,
for the task spaces, how the end of the reach was set, whether segments were
of equal length or duration, whether peak velocity was signed, whether axes
were scaled for Figure 7D, whether the upper-limit space included the fitted
neuron and whether the peri-movement space used all recorded neurons or only
the included ones.

The author's points on the protocol: it has no rule for a criterion that
stops making sense, as when the fig7c upper limit is at or below zero or the
fig7b ratio divides negative performances; it does not say what to record
when a criterion defines no partial outcome but most of its conditions hold,
as in fig4-broad; it does not say whether an adopted reading must be the same
across claims when open details give up to 96 readings, so one was kept for
all; it has no notion of statistical power, so a claim can be not reproduced
only because the subset is tiny; it does not say what `measured` holds when
one expected value cannot be computed, as for fig7b's monkeys A and B value;
step 1.6 covers method details but not metadata questions such as the array
mapping, which was treated the same way; and the repository root has
untracked dotfiles from the sandbox.
