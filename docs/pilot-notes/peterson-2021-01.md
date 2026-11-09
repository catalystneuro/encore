# 000055, Peterson et al. 2021

Seven claims reproduced (four on an assumption), four partially, one not
reproduced and none blocked; the claims that also use the paper's projection
matrices from electrodes to AAL regions on Figshare (`with_inputs`) are counted
apart, with eight reproduced (six on an assumption), two partially (one on an
assumption) and `fig3-lfb-more-widespread` blocked as methods_underspecified,
and the two link claims, `subject-days` and `roi-projection-link`, are left out,
both reproduced. The first verification round agreed with 19 of the 25 outcomes
as they stood and the second with all 25; nothing was proposed after the
second, so there was no third round. The version is 0.220127.0436, the only
published one, which the paper does not cite. The paper, Peterson, Singh, Wang,
Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021), studies contralateral
wrist movements detected from video pose in 12 epilepsy patients with ECoG over
several days of clinical monitoring, describes ten behavioural and
environmental features of these movements, projects movement-related spectral
power onto eight AAL regions, and fits regression models of single-event power
on the features; the dandiset (AJILE12) holds 55 NWB files, one per
subject-day, 845.87 GB in all. The claims were written from the version of
record (PMC8225404) without the PDF, so the Extended Data figures were read
only from their legends, and with the paper's code at commit 04c6faf, which the
author read but did not run; the claims check added
`extfig2-1c-contralateral-larger`, for 25 claims. The cohort, event counts and
features of Figure 2, the group and per-subject spectral changes of Figures 3
and 4, the band power of Figure 5 and Table 1 and the regressions of Figure 6
could be tested; sex and age could not, and whether low-frequency decreases are
"more spatially widespread" could not be judged, as the criterion's two
readings disagree (7 against 7 regions, but 35.2 against 25.9 significant bins
per frequency) and the paper gives no measure. Reproduced are, among others,
`fig3-group-lfb-decrease-hfb-increase` and `fig3-sensorimotor-largest`
(postcentral, precentral and inferior parietal at 0.523, 0.512 and 0.336 dB),
`fig5-recording-day-effects` (all 24 subject and band pairs agree with the
paper), `fig6-r2-at-most-025` (largest withheld R2 0.189),
`fig6c-angle-and-day-most-informative` and
`fig6d-upward-reaches-enhance-pattern` (median angle coefficient -1.027 in LFB
and 0.535 in HFB); `fig4-precentral-subject-variability` is reproduced on a
tie-break by interpolated width that the paper does not give, and would be
partial under the strict bin count. Partial are `cohort` (seven subjects with
depth electrode groups against five), `fig2-reach-shape` (angle density peaks
at -71.5 and 75.0 degrees, not near +-90, though the criterion's KDE without
boundary correction puts the peaks of synthetic angles peaking at +-90 near
+-72 as well), `extfig2-2-feature-correlations` (magnitude and duration r =
0.233 against 0.26 +- 0.026), `fig2-days-and-waking` (S04's busiest day holds
0.379 of its events), `table1-subject-band-power-ci` (23 of 24 inside, S06 HFB
1.782 dB against 2.02 to 2.37) and `extfig6-2-angle-most-retained` (angle is
retained most, the order of the next four does not hold). Not reproduced is
`fig2-event-counts` (211 to 996 events per subject, median 770.5, against 151
to 947 and 640). The regression claims rest on a small set of electrodes above
R2 0.05 (22 in LFB from 4 subjects, 14 in HFB from 6), whose R2 correlates with
the R2 stored in the files at a Spearman of 0.718 and 0.643; selected by the
stored R2 instead, as a sensitivity output, the Figure 6 results still hold.
The author's first run had 12 reproduced, 5 partially, 1 not reproduced and 7
blocked, the six regression claims as too large, as one model was timed at 8.0
s for an estimate of 4.9 h on one core; the author-answers run timed 5.2 s per
model and 3.2 h, and kept the claims blocked. The author asked no questions of
a reader, so the answer and author-answers runs changed no claim. Round 1
disagreed on the six regression claims, finding them blocked without good
reason, and raised the unmarked false positives, the KDE boundary bias, a
single bootstrap seed, the fig4 tie-break, the depth classification, the bad
electrodes and the bad-segment rule; in reply a batched Newton solver for
sklearn's Huber objective (within 4.4e-05 of sklearn in withheld R2) ran all
regressions and variants in about 2 minutes, five became reproduced and one
partial, ten other seeds gave the same tie, and a question on the angle
criterion went to a reader in `questions/000055.yaml`, written after the answer
run, so it is unanswered. Round 2 asked for the overlap with the stored R2
sets, a statement of how the day coefficient SD is taken and a deviation for
the false positives under every ECoG claim, and these were added. The author's
run took about 1 h 30 min, the notebook ran in 1723 s at first and about 41 min
after round 2, of which reading the ECoG segments took 34.6 and 35.4 min, and
nothing failed; an empty `.claude/` folder the harness created in the entry
could not be removed, as the request was denied automatically.

The dataset was converted by CatalystNeuro (Benjamin Dichter and Micheal Scheid
of CatalystNeuro are listed as contributors). The files hold 8088 wrist
movement events (211 to 996 per subject), where the data descriptor states 6931
verified events and the paper reports 151 to 947 per subject (median 640), and
no event is marked as a false positive or as removed, so the events the paper
analysed cannot be selected and every ECoG outcome includes events the paper
removed (17.8% of events, as false positives or occlusions). In three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the
ECoG holds 15.5 to 15.9 h with a starting_time of 0, while the reaches table and
pose run on a clock from midnight; the ECoG starts 29241 to 30682 s after
midnight, and the movement response appears only with this shift (S06 day 3,
precentral HFB +1.98 dB with it, -0.07 dB without). Reach_angle_degrees is
described only as "Reach angle in degrees" and holds the angle in image
coordinates, so upward reaches are negative, where the paper's feature is the
negated angle folded to -90 to 90. Pose positions are labelled meters but hold
pixels; Bimanual_overlap is described as a fraction of the contralateral
movement duration, but 1708 of 8088 values exceed 1 (up to 3.83);
session_start_time is 19:00 at UTC-5 for files that start at local midnight;
and 124 event segments contain missing ECoG samples on every electrode, in 30 of
55 files. The electrode good flags differ between a subject's files, and the
paper's code takes the list of each subject's first file. Seven subjects have
electrode groups described as depth, where the paper says five, and the group
descriptions disagree with the data descriptor's Table 2 for S10 (78 and 48
against 86 and 40) and S11 (18 depth electrodes against none). Sex and age are
not in the files or the archive's metadata. Questions are put to the paper's
authors: how a segment's power was summarised, in which unit and over which
segments, for the 0 dB and 3 SD rules for bad segments, whose preprocessing
code is not published; and whether "more spatially widespread" was judged by
the number of regions with significant changes or by the extent of significant
bins.

The author's points on the protocol: step 4 does not say whether a link claim
may be written after looking at the data, as `roi-projection-link` was after
the electrode and row counts were listed; the rule to break ties in a
criterion's ranking "as the paper implies" gives nothing when the paper implies
nothing; `measured` cannot hold null when some expected values cannot be
measured, so it was left out for `cohort`; and the protocol does not say how to
correct a conclusion's numbers after the run, which the author did by editing
the markdown cell in both the committed and executed notebooks.
