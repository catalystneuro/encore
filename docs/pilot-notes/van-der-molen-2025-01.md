# van-der-molen-2025, van der Molen et al. 2025

Twenty-nine claims reproduced, eleven partially, seven not reproduced and two
blocked, both as `methods_underspecified`; `supp5-murine-organoid-forebrain-identity`,
on single-cell data in GEO (GSE290330, `data: elsewhere`), is blocked too and
counted apart. Three outcomes rest on an assumption (supp8-backbone-stable-4h,
fig7d-murine-organoids-slices-same-lag and supp27-d2-near-critical). The first
verification round agreed with 44 of the 50 outcomes as they stood, the second
with 48 and the third, which reviewed only the two changes proposed after the
second, with both. It pins version 0.260923.0623, the only published version;
the paper cites none. The paper, van der Molen, Spaeth, Chini et al.,
"Preconfigured neuronal firing sequences in human brain organoids" (Nature
Neuroscience), records spontaneous activity of sorted units on high-density
microelectrode arrays in human brain organoids (HO1 to HO8), murine organoids
(MO1 to MO14), acute mouse cortical slices (MS) and primary cortical cultures
(Pr1 to Pr8), and reports that bursts are organised around backbone units that
fire in every burst, with higher burst-to-burst and pairwise correlations than
non-rigid units, that hidden Markov models (HMMs) find structure in them, and
compares these features across the four models. The claims were written from
the NIH author manuscript (PMC12912721.1) with the Supplementary Information,
without the version of record, and from the paper's code (Protosequences at
e9a79c4), which lacks the R models of Figs. 2, 3, 6 and 7; the claims check
added `fig4c-similarity-variance` and `supp24d-backbone-non-poisson`, for 50
claims. Reproduced are, among others, the burst counts (mean 34.8 over the 31
recordings; HO1 has the 46 bursts of Fig. 1C), the backbone fraction, the
burst-to-burst and pairwise correlations of backbone units in organoids and
slices, the gabazine and NBQX with R-CPP effects on bursting, burst similarity,
the HMM likelihood against shuffled data and the HMM dimensionality across
models. Not reproduced are `fig5c-states-converge-at-peak`,
`fig5f-svm-states-beat-rate` (states beat rate in neither test, and rate alone
reaches 89% to 95% in HO2, HO3 and HO4), `fig7b-normalized-b2b`,
`fig7c-backbone-pairs-above-random`, `fig7d-murine-organoids-slices-same-lag`
and `fig7e-pca-backbone-variance`, each failing in murine organoids, and
`ed2d-alam-el-din-rates` (p 0.0019 where the paper has 0.40). Blocked are
`ed4d-gabazine-rank-order` and `supp10b-rank-order-by-model`, whose two
normalisations give opposite results. The author's first run gave 29
reproduced, 11 partially, 5 not reproduced and 5 blocked, with supp27 not run
for lack of time. The author asked a reader nothing, so the answer and
author-answers runs changed nothing. Round 1 found that the burst detector
emitted duplicate bursts where a long burst holds two peaks, that the HMM
surrogate was scored differently from the real data, that the mixed models used
Wald z where the paper uses lmerTest, and that supp8 and the d2 test of supp27
were testable after all; in reply overlapping bursts were merged (35 bursts in
13 recordings), the models moved to Satterthwaite t, the second reading of the
recording length was run, units were linked across 0 h and 4 h by their ordered
positions and the d2 code of Sooter et al. was ported, which made the record
31 reproduced, 11 partially, 7 not reproduced and 1 blocked, with ed4d and
supp10b reproduced on the assumed z-score. Round 2 held that the claims file
reads the paper correctly on the rank-order normalisation, so both should be
blocked, asked for one rule for partial outcomes, and found sentences with no
output behind them (HO7 has 21 bursts, not 24; a comparison of HO1 to HO4 with
the paper's processed tables that was never run), which were corrected; a refit
without MO3 was added, and round 3 agreed to block ed4d and supp10b. The
author's run took about 3 h 35 min (12:17 to 15:52 UTC); its last
`entry.py all` was killed after 10 minutes because editing the README changed
the entry hash and restarted every notebook, and the author-answers run made
the full clean run instead. SSM would not install in a locked environment, so
the HMMs were fitted with the entry's own EM at K = 10, 12, ..., 30, 41 of 341
models stopping at 300 iterations, and 10 shuffles per recording (3 for some
measures) were run in place of 100. The notebooks ran in 23 and 21 min at
first, 1354 and 1266 s after the author-answers run, 29 and 18 min after round
1 and 1658 and 1318 s at the end.

The burst detection parameters for the murine organoids are not given, and with
the stated detection (4 x RMS of the 20 ms and 100 ms smoothed population rate)
MO2, MO4, MO5 and MO6 have no burst and MO3 has four, as their highest peaks
reach only 3.0 to 3.7 times the RMS, while the paper's code lists backbone
units for all nine; the murine results of Fig. 7 rest on five of nine
recordings, MO3's four bursts make 160 of its 234 units backbone units, and
without MO3 the murine contrast of Fig. 7B holds and the murine organoid
against slice lag contrast of Fig. 7D is not significant. The rank-order
normalisation is z-scored in the Extended Data Fig. 4D legend and (A - B)/(A +
B) in the Supplementary Methods; on shuffled Spearman correlations centred near
0 the ratio runs from -86,000 to 3,200, and the two give opposite conclusions.
The baseline sorted recording of MO12 and every longitudinal murine organoid
recording are missing (every MO file has age P45D), so the murine halves of
Supplementary Fig. 2 cannot be tested. Units carry positions but no identifier
across recordings of one organoid; the ordered positions are identical for HO2
at 0 h and 4 h (90 units), for HO3 once the 4 h file's unit 24 is left out
(116 units) and for MO10, MO11 and MO14 between baseline and gabazine, but not
for MO13 nor for any NBQX with R-CPP recording, and positions alone are not
unique (61 distinct positions for 90 HO2 units). The HO2 and HO3 recordings at
6, 7, 8 months and 8 months plus 4 h are each deposited twice under different
session names, and the 7-month ones a third time, with identical spike
matrices. The dandiset description says only spike-sorted data are included
for the sourced human organoids, but sixteen raw ecephys files are present for
HO1 to HO4, and the slice files say "Sorting/curation not specified". The n
reported with several tests counts all sorted units or pairs (507 units and
34,056 pairs in HO1 to HO4, 959 units and 125,607 pairs in the slices), while
the stated rules restrict the tests, and the Fig. 7A legend's counts (1048,
1179, 786, 1048) match neither all units (930, 1273, 959, 2001) nor units with
at least 30 spikes. Pr1 to Pr4 are rat cultures, as the Methods and files say,
where the paper calls all primary cultures murine. The AR fit check of the d2
analysis is not described, and two readings keep 0, 5, 0 and 1 or 7, 9, 3 and 8
recordings of HO, MO, MS and PR against the paper's 3, 7, 4 and 7. Three
questions are put to the paper's authors: the murine organoid burst parameters,
the rank-order normalisation and the level it was applied at, and the d2 fit
check.

The author's points on the protocol: `entry.py lock` writes a `python:` field
that the entry schema rejects; editing the entry's README changes its hash and
reruns every notebook; step 1.6 adopts the best-supported reading where the
claims file makes disagreeing readings `methods_underspecified`, and the claims
file was followed; 100 shuffles per recording do not fit the 60-minute
notebook limit and the protocol says nothing about running fewer; expected n
values count all sorted units while the criteria restrict the units tested, so
the count of all units was recorded as `measured`; the time rule has no
category for a claim never started, and `other` was used for supp27; and the
rule that every stream shares the trial clock does not apply without trial
tables.
