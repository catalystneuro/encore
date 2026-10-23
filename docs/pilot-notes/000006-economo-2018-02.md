# 000006, Economo et al. 2018, second attempt

Seven claims reproduced, five partially, three not reproduced and eight
blocked on the dandiset, with eight more on data in other archives, of which
five reproduced, one partially and two blocked. The claims file was written
again from the full text, as the earlier one, written from the abstract only,
is deprecated; it has 31 claims, and the dandiset is unchanged at version
0.220126.1855, its only published version. The author put 15 questions to a
reader. The answers made the code's per-unit rule the unit selection when
neither reading gives the paper's counts and each unit's own trial range the
trial range, so `pt-spike-rates-similar` moved from blocked to not reproduced
and `pt-variance-explained` and `pt-single-neuron-early-selectivity` from
blocked to reproduced; they moved the dependency of
`pt-lower-heterogeneous-rates` to `pt-tagged-units`, so it moved from blocked
to reproduced; they named three readings for the reconstruction counts, so
`pt-upper-thalamus-projection` and `pt-lower-medulla-projection` moved from
blocked to reproduced; and they made the test of `pt-types-shared-targets` on
the reconstructions a variant, so it moved from reproduced to blocked. The
commit with the answers had deleted four `- id:` lines from the claims file,
which then parsed to 27 claims, and the author put them back without changing
any statement, expected value or criterion. Round 1 agreed with 28 of 31
outcomes; for `pt-upper-persistent`, `pt-cohort-control` and
`pt-types-differ-in-timing` it gave the outcome of the claim's own test, where
the record blocks them because they depend on the blocked
`pt-upper-early-preparatory`. Round 2 accepted the dependency rule and agreed
with all 31, so there was no third round. The paper, "Distinct descending
motor cortex pathways and their roles in movement" in Nature, describes two
types of pyramidal tract (PT) neurons in mouse ALM, PTupper neurons projecting
to the thalamus and PTlower neurons projecting to the medulla, from
single-cell sequencing, axon reconstructions and units tagged by antidromic
photostimulation in a tactile delayed-response task, and reports that PTupper
populations carry early preparatory activity that persists until movement
while PTlower populations mainly carry late preparatory activity and movement
commands. The transcriptomic clusters, the reconstruction counts and the
fold-change correlation were tested on the paper's Figshare record, and the
unit counts, depths, spike rates, bursting, selectivity, variance explained,
coding directions, decoding and CDgo onsets on the dandiset. `pt-marker-genes`
is blocked as `data_missing` because the smFISH data are in no public file,
`reaction-time` as `data_missing` because no video is deposited, and
`pt-retrograde-sublaminae` and `pt-types-shared-targets` because the paper
gives no method for counting or analysing the anatomy images.
`pt-upper-early-preparatory` is blocked because its two rules for "larger"
give partially reproduced and not reproduced in all 8 combinations,
`pt-cd-change-at-go-cue` because levels 0.5 and 0.75 give reproduced and
partially reproduced, and `pt-lower-movement-termination` because its windows
and readings of a mouse give different outcomes. `pt-tagged-units` is not
reproduced with 44 PTupper and 56 PTlower units against 61 and 69,
`pt-selective-any-epoch` because 99 of the 100 included units the dandiset
holds cannot reach 122 +/- 12.2, and `pt-spike-rates-similar` because peak
rates differ (p = 0.030). Run on the paper's own 130 units from its processed
data, the same code gives the paper's numbers for unit counts, bursting,
late-delay counts, decoding, early selectivity and spike rates, and on the
processed data for the same 100 units it gives most of the dandiset's counts
and test results, so the count failures come from the missing sessions; the
CDgo onsets are out of tolerance even on the paper's units, the PTlower onset
falling in the 37.5 ms bin in the files, in the same units processed and in
all the paper's units, against 24 ms. Two questions added after round 1,
whether count criteria should be judged as fractions when units are missing
and whether the cohort control should count a difference in the opposite
direction as a failure, are unanswered.

The findings of `-01` are all still present, as the version has not changed.
Eleven sessions of the paper's processed data that hold tagged units are not
in the dandiset; they hold 17 of the 61 PTupper and 13 of the 69 PTlower units
the paper analysed, and the dandiset's description says some files were found
to be broken and left out without naming them. Every tagged unit the dandiset
holds is in the processed data with the same label, inclusion decision and
depth. New: the missing sessions also hold unidentified units, the dandiset
holding 232 in the PTupper cohort and 430 in the PTlower cohort against the
495 and 511 the paper analysed. Spike times are not sorted in 1120 of 1149
units, as they were written trial by trial and consecutive trials overlap on
the file's clock, so some spikes of one trial lie in the next trial's early
epochs (11.7% of the spikes counted in the baseline epoch are detectably out
of order); on the same 100 tagged units every unit's baseline rate is higher
in the files than in the processed data (median by 0.99 Hz for PTupper and
0.97 Hz for PTlower units). New: the lick times are stored the same way and
are out of order in 105 of 106 lick series (14,360 backward steps in 180,679
licks), and the files do not assign licks to trials; rebuilt from the stored
order, each trial's last lick matches the processed data's in 98.1% of correct
trials. The trial table's stop_time is NaN in every file, pole_in_time,
pole_out_time and cue_start_time are relative to the trial start without
saying so, and the go cue of a trial falls after the next trial's start_time
in 13,306 of 15,096 trials. The labels PTupper and PTlower are not described,
and their projection targets are stated only in the paper's code. Unit quality
mixes two vocabularies and has undescribed empty values, sex is U and genotype
empty for every mouse, the electrode positions are all zero, and every
electrode group gives layer 5 whatever the depth. The dandiset holds the
electrophysiology only, with the sequencing, axon reconstructions and anatomy
on the Figshare record and at GEO (GSE119182), and the smFISH data behind Fig.
3c in no public file; new, no file holds video or the session manipulator
depth. In the paper's processed data, and so in the files, the spike windows
of the first ten trials of every session start later relative to the pole
than those of the other trials (session medians 1.73 to 5.84 s after the pole
comes in, against -0.97 to -0.16 s), which the paper's code hides by leaving
those trials out.

The notebook ran in about 11 minutes in the first run, 628 s after the
answers, about 11 minutes twice after round 1, and 598 s and 611 s after round
2. `entry.py all` stopped at the check in every run on 22 errors in the
deprecated `-01` record, which lacks outcomes for the claims the rewritten
file added, so the author ran `entry.py run` directly; the `-02` record passes
the check. Round 1's points led to a rerun of the measures on the processed
data for the 100 units the dandiset holds, the CDgo 5th percentile from 0 to
0.1 s, the share of unit-trials whose last lick is more than 2.5 s after the go
cue (0.16% and 0.17%), the structures of AA0134's axon nodes, a
reconciliation of the processed data's 150 tagged units with the paper's 143
and the Anatomy.zip image counts; none changed an outcome. Round 2 found
statements the outputs did not support, among them unidentified pools called
about half the paper's where the PTlower cohort has 430 of 511, the processed
data for the same units said to give all of the dandiset's counts and test
results, and a baseline rise of about 1 Hz where it ranges from 0.14 to 6.47
Hz, and these were corrected. Untracked files in the repository root that the
author did not create were left alone. The author's points on the protocol:
`entry.py check` fails on the deprecated `-01` record, which cannot be fixed
without editing it, so `entry.py all` stops at the check; the dependency rule
over-blocks, as `pt-lower-heterogeneous-rates` used only the rates of
`pt-spike-rates-similar` yet was blocked with it; the rule for data elsewhere
forbids `data_missing` for data that are public nowhere; the section on repeat
attempts assumes the dandiset changed, where here the claims file changed and
the data did not; and no selection is designated when neither reading
matches, the gap behind most of the blocks before the answers.
