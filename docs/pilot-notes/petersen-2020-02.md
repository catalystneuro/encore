# petersen-2020 again, Petersen et al. 2020

Seventeen claims reproduced, nineteen partially, eight not reproduced and two
blocked, all on the dandiset. The first verification round agreed with every
outcome it listed, but its table left out `suppl2d-interneuron-oscillation-slows`
(45 rows for 46 claims); the second round agreed with all 46, and nothing was
proposed after it, so there was no third round. This is the second attempt,
run blind to the first, on version 0.261115.0311, the latest published one (the
paper cites no version), and on a claims file rewritten on 2026-11-15 from the
paper's full text, which drops the session lists and thresholds the earlier
version took from the first author's unlinked code and adds eight claims. The
paper, Petersen and Buzsáki, "Cooling of Medial Septum Reveals Theta Phase Lag
Coordination of Hippocampal Cell Assemblies", reports that cooling the medial
septum (MS) of rats slows hippocampal theta and lowers its power, raises choice
errors, slows the oscillation of place cells (fp) with the LFP theta in their
fields (fLFP), and lengthens the theta time lags between place cell pairs while
their phase lags are kept. Every claim could be tested except two: the control
experiment's hippocampal temperature is not in the dandiset (`data_missing`),
and the distance-time compression of Figure 5C and G is blocked as
`methods_underspecified`, because the Methods' surface fit fails on the data,
also bounded and from several starts, and the paper does not say how the
density was prepared for it. Reproduced are, among others, theta frequency and
power lower during cooling than before and after, the recovery of errors, the
worst trials at 4 to 8, the decrease of fp and fLFP, the unchanged population
vector scale and the unchanged phase lags, the last only when a pair's lag is
read as the largest peak within pi of zero (the peak nearest zero gives P =
2.7e-8). Partial are, among others, the error increase (a ratio of about 2.0 to
2.25 against 3), the correlation of theta frequency with temperature (R = 0.978
on aligned trials, above 0.81 +- 0.081), the time lags (pre and post also
differ, P = 0.034) and the precession slope (flatter during cooling than before,
P = 0.016, only with a search range of 2 cycles per field and not without the
slopes at the bound). Not reproduced are errors independent of speed, the
preserved fp - fLFP difference, field size before and during cooling (R 0.41 to
0.49), the modelled field size, unchanged information (pre to post still falls
with equal trials, P = 0.016, and with equal spikes, P = 0.032, but not when
shuffle-corrected, P = 0.085), the fraction of cells active and the spikes per
theta cycle (by rank-sum over cycles; per session pre against cooling gives P =
1.0 and 0.80) and unchanged waveforms, measured on 4 sessions. Twenty outcomes
rest on an assumption, chiefly that place fields are found on the rate map over
all trials. Round 1 found that the precession slope search stopped at 1 cycle
per field, where 28 to 32% of the slopes sat, and that the surface fits mostly
failed; in reply the range became 2 cycles, `fig4d-precession-slope-decrease`
moved from not reproduced to partially reproduced and `fig5cg-compression` from
not reproduced to blocked. Round 2 agreed that fig5cg cannot be decided but not
with its reason, that the surface does not describe the density, which was
restated as a failed fit; it also asked for per-session tests of the pair and
cycle claims and for the dependence of fig4d on the bound to be stated, and it
led the author to withdraw a finding on the tracking rate, as each behaviour
description matches its timestamps. Against the first attempt (12, 15, 10 and
1), 14 outcomes changed, most through the rewritten claims file, a different
theta power measure, different field and size definitions, and the curated
units this version adds (23 sessions with place cell pairs against 15, 8506
pairs against 3136). The release notes of the pinned version say the
conversion fixes problems found by a reproduction attempt and list their
topics, which the author read before looking at the data; the blind audit
found one listing that showed the earlier summary's path, which no run opened.
The author asked a reader nothing, so the answer and author-answers runs
changed nothing. The author's session ran from 13:21 to 16:08 UTC; an early
pair cross-correlogram took 27 minutes and the first surface fit 20, the first
record failed the schema check, and one stale Result cell was corrected. The
notebook ran in about 16.4 min at first, with peak memory 4.7 GB, and in 27
minutes after round 1; the entry's run after round 2 took 1365 s, and the
notebook took 2782 s in the reconciliation run, against the 30 minutes
`entry.yaml` gives.

The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is a
contributor). Twenty sessions have no measured MS temperature, only the lab's
modelled curve (all MS10 sessions, 7 of 9 MS12 sessions, 2 of 5 MS13,
MS21-180627 and MS22-180628), so 31 of 51 sessions support temperature
analyses and MS10 none; the release notes name only MS10 and MS12-170715 as
modelled. The hippocampal temperature of the paper's control experiment
(Figure S1H to K), unit waveforms and the paper's place fields are not in the
dandiset, 23 of the 51 sessions hold no curated units and 5 hold units without
a cell type. The measured traces hold undescribed artefacts, with raw values up
to 1354 C (MS21-180625) and down to -1751 C (MS22-180712); 11 of the 31 hold
values outside 5 to 45 C, and three MS22 traces hold values near 5 and 10 C
outside the trials. The 2018-07-19 sessions of MS21 and MS22 are labelled as
cooled, but their measured temperature does not fall below 37.4 and 35.2 C, and
theta frequency falls during the labelled cooling in MS22-180719 (8.68 to 8.27
Hz) and rises in MS21-180719 (7.53 to 8.13 Hz); their cooling tables now say
the septum does not appear to have been cooled, but nothing says that they or
MS10-170307 are outside the paper's analysis. Five of the paper's 53 sessions
are not in the dandiset (MS12-170712, MS13-171204, MS13-171205, MS13-171206 and
MS21-180806), and the release notes do not mention the last; the paper's
subsets of 21, 19, 18 and 10 sessions and its 365 place fields are not named,
so they cannot be matched. Thirteen sessions have two cooling epochs, and in
MS12-170717 and MS12-170718 the second ends at 25683 s and 28409 s, long after
the last trial; four sessions have a no-cooling interval that ends before it
starts. In MS21-180621 and MS22-180621 the good units carry no more spatial
information than with their spikes shifted by 60 s (0.170 and 0.119 against
0.214 and 0.152 bits/spike), so the clock of spikes and position could not be
established there. The lab's theta channel of MS13-171130 (channel 82) is
marked bad, and 2 sessions name theta maze epochs Linear_Track_Peter. The
Methods give tracking at 120 Hz, while six MS10 sessions are tracked at 40 Hz,
one at 30 Hz and two at 119.8 Hz. Of the first attempt's 13 findings, 2 are
fixed (the undescribed 'Cooling off' state, and the trials of MS21-180627 and
MS21-180712), 6 partly fixed, 4 still present and 1 not checked; cell types and
electrode locations are now given, though 14 files of MS21 and MS22 still give
every electrode as unknown. In the paper, the Figure 5H legend gives P = 8.0e-5
by a sign rank test with N = 10 sessions, below the 0.00195 an exact test over
10 sessions can reach, and the Discussion's 12% decrease of theta frequency
does not match the Results' 8.4 and 7.7 Hz (8.3%). Questions are put to the
paper's authors: which correlogram peak is a pair's phase lag, on which rate map
the Figure 5 fields were found, within what range the precession slope was
searched, and the surface-fit procedure, whose equation has lost its fraction
bars in the available text; the hand-drawn fields of Figures 3 and 4 would let
the field claims be tested on the paper's fields.

The author's points on the protocol: running every reading of every claim
multiplies out, so the place field claims ran a subset; the rule that absence
is judged on the paper's test alone conflicts with readings of the measure
itself, as in fig5i; release notes in archive metadata can unblind a repeat
attempt; default tests over hundreds of fields or tens of thousands of cycles
detect very small effects in claims of absence; no block reason covers running
out of time; checks run outside the notebook cannot go in the record; and the
entry directory the prompt called empty did not exist.
