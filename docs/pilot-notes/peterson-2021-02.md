# peterson-2021, Peterson et al. 2021, second attempt

The second attempt on this paper, made blind to the first (peterson-2021-01),
under pilot-18. Seven claims reproduced (four on an assumption), four
partially, one not reproduced and none blocked on the dandiset; the claims that
also use the paper's projection matrices from electrodes to AAL regions on
Figshare (`with_inputs`) are counted apart, with six reproduced and four
partially, all on an assumption, and `fig3-lfb-more-widespread` blocked as
methods_underspecified; the two link claims, `subject-days` and
`roi-projection-link`, are left out, both reproduced. The first verification
round agreed with all 25 outcomes. In the first revision the author moved
`fig5-recording-day-effects` from partially to not reproduced by taking the
electrodes good in every file of a subject; the second round agreed with the
other 24 and left that one undecided, as the choice of electrodes decided it,
the author proposed partially reproduced on each file's own flags, whose 4.2 +-
2.1 removed surface electrodes per subject are closest to the paper's 4.9 +-
4.9, and a third round reviewed that one claim and agreed (20 of 24 pairs, the
criterion's threshold). The attempt pins version 0.261123.1703. The paper,
Peterson, Singh, Wang, Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021),
studies contralateral wrist movements detected from video pose in 12 subjects
with ECoG during clinical epilepsy monitoring over 3 to 5 days, describes ten
behavioural and environmental features of the movements, projects
movement-related spectral power onto eight AAL regions, and fits regression
models of single-event power on the features. The claims file, written under
pilot-10 from the version of record (PMC8225404) without the PDF, so the
Extended Data figures were read only from their legends, and with the paper's
code at commit 04c6faf, holds 25 claims. The cohort, the events and features
of Figure 2, the spectral changes of Figures 3 and 4, the band power of Figure
5 and Tables 1 and 2 and the regressions of Figure 6 could be tested; whether
low-frequency decreases are more spatially widespread could not be judged, as
the criterion's two readings disagree (8 against 8 regions, 36.0 against 22.2
significant bins per frequency bin) and the paper gives no measure. Reproduced
are, among others, the group decrease in low and increase in high frequency
power, largest in postcentral, precentral and inferior parietal regions, the
differences in band power across subjects, and the regressions, with a largest
withheld R2 of 0.177 and recording day and reach angle the most informative
features in both bands. Partial are `cohort` (seven subjects with depth
electrode groups against five), `fig2-reach-shape`, `extfig2-2-feature-correlations`
(magnitude and duration r = 0.232), `fig2-days-and-waking` (S04's busiest day
holds 0.400 of its events), `fig4-precentral-subject-variability` (two of four
parts), `table1-subject-band-power-ci` (18 of 24 inside), the recording-day
effects and `extfig6-2-angle-most-retained`. Not reproduced is
`fig2-event-counts` (fewest events 210 or 211, in S09, against 151 +- 15.1).
The reconciliation with peterson-2021-01 found that this attempt's helper
(`ajile.py`, `session_spectral`) reads every ECoG series from 0 s, while this
version sets the ECoG starting_time of sub-01 day 7, sub-04 day 3 and sub-06
day 3 to 29240.566 to 30682.414 s, so their events were read about 8 h late;
this gives the day effects of S01 LFB, S01 HFB and S06 HFB where the paper has
none, and read from the starting_time 23 of 24 pairs agree. It traces the
change of `fig4-precentral-subject-variability` from reproduced to the choice
of electrode flags, and notes that the same error touches the other ECoG claims
for those three files. The author asked a reader nothing at first; after round
1 three questions went to a reader in `questions/peterson-2021.yaml`, on the
row rule of `roi-projection-link`, the 15 degree window of `fig2-reach-shape`
and the 0.5 to 4 s filter of `fig2-event-counts`, and no claim was changed.
The author's run took about 2 h 33 min (05:06 to 07:39 UTC) and the notebook
36.6 min at first, with peak memory 1.8 GB per worker. In the second revision
a Figshare timeout stopped the first run, after which downloads were retried,
and the full run was marked failed for taking 63.5 minutes against the
60-minute limit, most of it in the 3904 regression models; the notebook ran in
1809 s after round 3.

The dataset was converted by CatalystNeuro (Benjamin Dichter and Micheal Scheid
of CatalystNeuro are listed as contributors). The files hold 8088 movement
events, 211 to 996 per subject (median 770.5), where the paper analysed 151 to
947 (median 640), and nothing marks the events the paper used or the false
positives it removed, so the paper's event set cannot be rebuilt. The record
says the ECoG of sub-01 day 7, sub-04 day 3 and sub-06 day 3 ends hours before
the day ends, leaving 237 events without neural data; the reconciliation shows
that the ECoG of these files starts late, at its starting_time, and runs to
86400 s. The good flags of the electrodes differ between a subject's files (bad
in at least one file 3 to 32 per subject, in every file 1 to 17), and nothing
says which applies; the surface electrodes this removes are 12.6 +- 8.4 per
subject for those bad in any file, 1.2 +- 0.4 for those bad in every file and
4.2 +- 2.1 for each file's own flags, against the paper's 4.9 +- 4.9. The ECoG
holds undescribed stretches of NaN samples in 125 events (47 in sub-10), and in
sub-09 and sub-10 every analysed event has runs of at least 50 ms of exact
zeros on 1 to 15 good electrodes. The bimanual overlap is described as a
fraction, but 1708 of 8088 values are above 1 (up to 3.83) and fit seconds; the
pose is labelled meters but holds pixels; the reach angle has no stated
convention and is in image coordinates, so upward reaches are negative; and
the low_freq_R2 and high_freq_R2 columns of the electrodes table are not
described. 24 electrodes have no position, the 16 depth electrodes of sub-03
and 8 of sub-12. One event of sub-08 day 4 is at 40.3 s in ReachEvents and at
86440.3 s in the reaches table. Electrode groups described as depth are in
seven subjects, where the paper reports five, and the group descriptions
disagree with the data descriptor's Table 2 for sub-11 (18 depth electrodes
against none) and sub-10 (78 and 48 against 86 and 40). The behavioural epochs
are empty at 4767 of the 8088 event times, and 17 events fall in epochs
labelled sleep or blocklist. The subjects and days are the paper's, the
paper's projection matrices match the electrodes of all 12 subjects, and band
power at onset differs from that 3 s earlier in 10 of 12 subjects for LFB and 8
of 12 for HFB, consistent with a shared clock; for sub-09 neither band differs
(p = 0.84 and 0.87), so its alignment could not be established. Of the 13
findings of peterson-2021-01, three are fixed in this version (the ECoG
starting_time, session_start_time at midnight UTC, and sex and age, now in
every file) and ten are still present. Questions are put to the paper's
authors: how segment power is pooled for the 0 dB and 3 SD rejection rules,
which measure makes low-frequency decreases more widespread, and whether bad
electrodes were removed per day or per subject.

The author's points on the protocol: the `roi-projection-link` criterion says
to drop all-zero rows where the code also drops the first non-zero row, and the
code's rule was used as a deviation; the notebook cannot run in about 10
minutes on about 150 GB of ECoG; running every random step under five seeds is
too costly for 3904 Huber models, so only the full-model R2 of the top models
was refit under the extra seeds at first; the clock check did not fit an event
table on continuous recordings, so power at onsets was contrasted with
pseudo-onsets 3 s earlier; the `cohort` claim has no partial rule; and it is
unclear when a small choice of event set makes an outcome rest on an
assumption, so every spectral and regression outcome was marked assumed.
