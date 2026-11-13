# laboy-juarez-2019, Laboy-Juarez et al. 2019

Twenty-nine claims reproduced, 13 partially, seven not reproduced and one
blocked. The first verification round agreed with 45 of the 50 outcomes; on
its reasons `fig7a-dt-half-width` moved from reproduced to partially
reproduced and `fig8c-awake-cw-stronger` from partially reproduced to not
reproduced (p = 0.0021, where the criterion needs p < 0.001), while the
author kept partially reproduced for `exp1-cw-sw-comparable-firing`,
`supp4-selectivity-at-high-rates` and `fig4c-sw-tuned-decoding` and recorded
the disagreement. Round 2 agreed with all 50 and nothing was proposed, so
there was no third round. The paper, Laboy-Juarez, Langberg, Ahn and Feldman
in Nature Neuroscience, records units in mouse barrel cortex while whiskers
of a 3 x 3 grid are deflected singly and in two-whisker sequences at
different intervals (dt), under urethane in experiments 1 and 2 and in awake
mice doing a visual lick task in experiment 3, and reports that units prefer
sequences that include the columnar whisker (CW), that combination tuning is
sharper than the linear sum of single-whisker responses predicts, and that
selective units prefer inbound order. The claims were written from the
version of record, and the paper's code is available only on request, so no
code was read. The unit counts, the sequence and CW claims, the sharper than
linear tuning, the global scaling and most awake claims reproduce. Not
reproduced are `methods-dt-modulation` (no curve best fit unsmoothed, against
23%), `exp2-combination-selective-prevalence` (318 of 463 response sets
selective, against 187 of 451), `fig3e-identity-decoder` (0.145 against 0.42),
`fig6b-enhancement-not-different` (p = 0.0096), `fig7g-inbound-decoding`,
`supp8-order-decoding` (0.584 against a bound of 0.585, a fragile miss) and
fig8c; `fig8b-awake-behavior` is blocked as `data_missing`. Every claim on
selective sets uses the 318, and is also run on the 187 sets with the
smallest p and, after round 2, on the 162 sets that FDR selects from p-values
calibrated on a real-data null; five outcomes (supp4, fig7a, fig3g, supp8,
fig6b-enhancement-not-different) and then supralinear depend on the group and
are marked as assumed. The answer and author-answers runs found no questions
and changed nothing; the question whether the paper's maximal evoked firing
is in Hz was filed in the first revision, after them. The notebook ran in
about 13 minutes at first, 46 minutes after round 1 and 2024 s at the end;
during development peak memory reached 9.8 GB (3.7 GB in the final run) and
Python's randomized `hash()` gave recording IDs that changed between runs,
replaced with MD5.

The experiment 1 files hold each single whisker deflected in both directions
(18 single-whisker stimuli), where the paper describes 9, and which direction
the paper used is not stated; the caudal deflections reproduce the paper's
unit counts. In both 20170510 recordings about half the trials of each pair
that involves whisker 3 or 8 have that whisker deflected rostrally and the
other caudally (about 5,300 trials per recording), and the pair 3-8 has only
such trials, which neither the paper nor the descriptor mentions. The
experiment 3 files hold no lick times, trial boundaries or Go and No-go
labels, so Figure 8b cannot be tested and the Methods' exclusion of epochs
within 200 ms of a lick cannot be applied; they also hold no deflection times
and no per-unit depth, and the descriptor does not say how DeltaT is signed or
where epoch time 0 lies, which the CW response latencies settle (30 ms when
the CW leads, 70 ms when the SW leads by 40 ms). About a third of the
experiment 3 spike times (26 to 35% per file) lie after the roughly 300 ms
epoch, up to 425 s after its start, in 5.6% of unit-epochs. Nine of the 16
experiment 2 recordings hold 16,000 to 24,000 three-whisker trials that
neither the paper nor the descriptor mentions. Two experiment 2 units in
20160909 have identical spike trains, and in 20160803 and 20160909 some units
carry the recName of another recording. Two experiment 2 recordings (20160225
and 20160316, 10 units) have no sham trials, and CW-SW dt takes 101 values
where the paper gives 100. Questions are put to the paper's authors: how the
dt smoothing handled held-out dt values without training trials, zero rates
and the edges; which best dt was used for units whose curve is set constant
across dt; which deflection direction experiment 1 used; and how the shuffle
test treated constant curves and inverted the Mahalanobis covariance, as the
test as described gives p < 0.05 for 25% of sets on a real-data null.

The author's points on the protocol: open readings that multiply across
claims, of which only the main combination was carried downstream; expected
values left out of a criterion's "reproduced when" clause; partial rules
that miss the case found; dependent claims whose parent ran but selected a
different set of units; which outcomes to mark as assumed when one assumption
touches every claim of an experiment; and a clock check that does not fit
epochs that start at the stimulus, replaced by the CW latency shift.
