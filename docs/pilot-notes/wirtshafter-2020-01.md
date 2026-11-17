# wirtshafter-2020, Wirtshafter et al. 2020

No claim reproduced, one partially, none not reproduced and 30 blocked, all
as `data_missing`. The first verification round disagreed with one outcome,
giving `units-recorded` as partially reproduced where the author had blocked
it, and the author changed it; the second round agreed with all 31, and
nothing was proposed after it, so there was no third round. CRCNS does not
version data sets, so the record gives it as `unversioned`; the MD5 sums of
all three files match the data set's `checksums.md5`. The paper, Wirtshafter
and Wilson, "Differences in reward biased spatial representations in the
lateral septum and hippocampus" in eLife, records units in dorsal CA1 and
caudodorsal lateral septum (LS) of six rats at once on a double-sided T maze
with a forced and a free choice phase, and compares spatial information,
place fields, their skew by direction of travel, their locations relative to
reward and the cross-correlations of CA1 and LS place cell pairs. The claims
were written from the version of record (PMC7274787) and from the paper's
code (elifesciences-publications/data_analysis at commit 5c6320a9).
`units-recorded` is partial: the data set holds 452 LS and 178 CA1 clusters,
exactly the paper's counts of units recorded, but the 165 CA1 and 378 LS
cells meeting the rate and track coverage criteria need the animal's position
and speed. The other 30 claims, from spatial information and place fields to
skew, field locations and the CA1-LS cross-correlations, need position too.
No reader was asked anything, so the answer and author-answers runs changed
nothing. Round 1 also asked for the code repository's file list, every sample
interval of Times.mat and the spike-free stretches of each recording, which
were added; round 2 found sentences the outputs did not support, among them
that no recording has a minute without a spike when only the span between
first and last spike was checked, and that 410 distinct LS trains keep the
count within tolerance when dropping the clusters that hold others' spikes
and MUA9 leaves 395, outside it, and these were corrected. The author's
session used about 35 minutes; the notebook ran in 117 s at first and in
243 s at the end, and nothing failed in the final runs. Untracked dotfiles
and a `scripts` folder that the author did not create were left alone.

The data set holds no position, speed or direction data, and no trial, lap
or epoch markers, though the Methods describe position tracked at about
30 Hz by overhead cameras, so none of the paper's findings beyond the counts
of units recorded can be tested; the data description names only spikes and
time files, the paper's Data availability names only this data set, and the
paper's code repository holds no tracking data (only three of its 177 files
that could hold data reach the 432,000 bytes of one session's tracking, and
they are chronux's spike sorting samples). In rat 7, two spike trains, of
1033 and 1441 spikes, are deposited byte for byte under 18 and 25 cluster
names, across 16 of the 19 rat 7 recordings with clusters and three tetrodes
(18, 27 and 32); 27 of the copies hold spikes after the end of their
recording's timestamps (5403 spikes in all, none before the start), the only
spikes in the data set outside their recording, and the paper's 452 LS
clusters include these 41 copies. Several clusters hold the spikes of others:
on rat 6's tetrode 26, in each of the 14 recordings with clusters there, the
largest cluster holds at least 99.6% of the spikes of each other cluster on
the tetrode (47 of 47), and two of these clusters (2017-05-01, cl_7 and cl_9)
are identical; 89 pairs of clusters on one recording share at least 99% of
the smaller train's spikes within 0.5 ms, and 24 pairs on neighbouring
tetrodes share 71.5 to 98.5% of their spikes, against a median of 0.5% (at
most 1.3%) with one train shifted by 1 s. The data set does not say which
clusters are single units, and of its 630 clusters 588 are distinct trains.
Times.mat is described only as "time files for all sessions"; it holds 57
time bases of the six rats, most at 0.512 ms intervals, six of rat 6 at
3.2 ms and one of rat 7 at 0.0512 ms, lasting from 2.5 min to 31 h, while the
paper analyses one 30 min maze session a day, and nothing marks which part
of a recording is the session: no recording changes its sampling interval or
has a gap of 0.1 s, and none has a stretch of 60 s without a spike between
its first and last spike. In rats 7, 8 and 9 the spikes span 0.5 to 0.9 h,
which may be the session, while in rat 6 they span up to 4.9 h and in rats
10 and 12 the whole 3.8 to 6.4 h recording; eleven recordings have no
cluster. The sampling intervals are not stated, and the six rat 6 recordings
at 3.2 ms have 25 brief gaps of 4.9 to 93 ms, two of them with repeated
timestamps (1121 in 3 s of 2017-04-21, 3280 at the end of 2017-04-26). Ten
cluster names of rat 7 write cl1 for cl_1, one LS cluster of rat 9 is
labelled MUA9 with no description, the CA1 clusters come from two of the six
rats (10 and 12), which neither the description nor the paper states, and
tetrodes 1 to 16 are CA1 and 17 to 32 LS, which the files show but the
description does not say. No question is put to the paper's authors.

The author's points on the protocol: a claim whose criterion needs four
counts, of which only two can be computed, fits no outcome cleanly, as
partially reproduced means an effect that holds in part, not one tested in
part; the clock check assumes trial tables or annotations to align spikes
with, and here it could only show that spikes fall within each recording's
time range; the duplicate check says to report each pair, and the 117
heavily overlapping pairs and the copies were reported grouped; and "one
section per tested claim" leaves open how to show a blocked claim with
partial numbers.
