# crcns-ssc-8, Goncalves et al. 2013

Five claims reproduced, three partially (all three on an assumption), three not
reproduced (one on an assumption) and 17 blocked, 16 for missing data and one
for insufficient metadata. The first verification round agreed with all 28
outcomes and the second with all 28; nothing was proposed after the second, so
there was no third round. CRCNS does not version data sets, so the version is
recorded as unversioned with the data set's DOI (10.6080/K0X63K3X). The paper,
Goncalves, Anstey, Golshani and Portera-Cailliau in Nature Neuroscience
(16:903-909), images layer 2/3 barrel cortex of unanesthetized wild-type (WT)
and Fmr1 -/- (KO) mice at P9-11, P14-16 and P30-40 with two-photon calcium
imaging at 3.9 Hz, and reports that pairwise correlation falls with age and
with distance, that it is higher in KO mice pooled over ages and most of all at
P14-16, that more KO neurons take part in peaks of synchrony, that firing rates
from the imaging do not differ, that in whole-cell recordings KO neurons fire
more in Up states, that firing rises with EEG low/high power in KO mice, and
that isoflurane raises correlation in WT but not KO mice; the data set holds
the raw TIFF movies of the unanesthetized mice, one per mouse, the estimated
firing rates of each neuron and the cell-to-cell distances. The claims were
written from the version of record (PMC3695061) as text flattened from the
Europe PMC XML, without figure legends, without the supplement (Supplementary
Figures 1 to 4) and without code, as the paper links none; the claims check made
seven corrections, among them making Spearman a variant that cannot decide a
claim and requiring a positive KO slope in the EEG claims, for 28 claims. Eleven
could be tested, all on the imaging. Reproduced are `fig1e-age-decrease` (p =
1.8e-07 for WT and 8.1e-08 for KO), `p30-40-no-difference` (p = 0.22),
`fig2b-peak-frequency` (0.060 and 0.054 peaks per s, no difference under any of
six readings, p = 0.13 to 0.96), `imaging-firing-rate-no-genotype-difference` and
`unanesthetized-p14-16-values` (0.304 and 0.304 Hz, WT correlation 0.169), which
rests on reading the rates as Hz, an argument the record calls partly circular.
Partial, all on the assumption that the deposited rates stand for the paper's
trace, are `fig1d-distance-dependent-decorrelation` (drops of 0.191, 0.105 and
0.025 against 0.223, 0.159 and 0.067, with the significance pattern holding),
`genotype-pooled-ages` (p = 0.0064 against the paper's 0.0057, with no reading
putting both means within the paper's s.e.m.) and `pearson-genotype` (p =
0.023 against 0.026). Not reproduced are `group-sizes`,
`fig1ef-p14-16-difference`, where the means are within the paper's s.e.m. (WT
0.169, KO 0.204) but Student's p = 0.057 and the difference is not largest at
P14-16, an outcome the record calls fragile, as leaving out one mouse in turn
gives p from 0.018 to 0.109, and `fig2c-participation` (KO 0.444 against WT
0.411, p = 0.25, and p = 0.052 to 0.76 over twelve readings). The whole-cell
claims of Figures 3 and 4, the EEG claims of Figure 5, the 15.6 Hz control and
the isoflurane claims of Figure 6 are blocked, as none of those data are
deposited, and `suppl4a-firing-vs-correlation` because the data set does not
mark which recordings were in the EEG subset. The author's first run had the
same counts, with `suppl4a-firing-vs-correlation` blocked for missing data. The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 agreed with every outcome and raised the "at least one
spike" reading never run with the rates per frame, the partly circular choice
of Hz, Student's against Welch's test at P14-16 (p = 0.057 against 0.049), the
four P14-16 mice with pairs over 200 um, the paper's pooled s.e.m. pointing to
the mean of the age means, the suppl4a variant and a summary left in the
notebook; in reply the missing reading was run without moving an outcome, a
unit check showed the values do not reveal the unit, the per-mouse P14-16
values, variance tests and leave-one-out p values were printed, and suppl4a
moved to insufficient metadata. Round 2 agreed with all 28, found sentences the
outputs did not support, among them a stale p range for fig2b and a finding
that said every reading gives proportions above the paper's, and asked whether
another shuffle seed would bring fig2c below 0.05, which would make it partial;
in reply the text was corrected and the reading was run over 20 more seeds per
shuffle (below 0.05 in none of 20 with one shuffle and 3 of 20 with the other)
and with 1000 shuffles (p = 0.056 and 0.051 to 0.054), and the author kept not
reproduced, as choosing the seeds that pass would select on the result. The
author's run took about 42 minutes (08:13 to 08:55 UTC); the notebook ran in 203
s at first, 239 s after the author-answers run, 307 s after round 1 and 795 s
after round 2. The first read of the TIFF archive failed with a 404 until `+`
in the file name was encoded as `%2B`, and an exploratory pass with `tifffile`
peaked at 7.3 GB of memory and was replaced by a small parser.

The data set holds 13, 8 and 7 WT mice and 9, 10 and 6 Fmr1 -/- mice at P9-11,
P14-16 and P30-40 (53), while the paper analysed 12, 9 and 8 and 9, 10 and 8
(56), and neither the descriptor nor the files say which mice differ or why; the
one WT P14-16 mouse fewer could alone move the P14-16 test across 0.05. No cell
contours or dF/F traces are deposited, so the paper's correlations cannot be
computed from the filtered dF/F if that is what the paper used; only the
estimated firing rates are given. The whole-cell recordings, the EEG, the
isoflurane imaging and the 15.6 Hz imaging are not deposited, and 17 of the
paper's 28 claims cannot be tested. The descriptor gives 40 to 149 neurons per
animal, where two WT P9-11 recordings have 164 and 198, and about 7 to 8 min per
recording, where at the stated 3.9 Hz the recordings last 3.8 to 15.4 min and
27 of 53 are 2160 frames (9.2 min). It gives no unit for the estimated firing
rates; their means fit Hz, and the values, which are continuous, do not show the
unit. It does not say that the k-th matrix of each group belongs to
Movie_k.tif, which the frame counts and the correlation of the population rate
with each movie's brightness show. The movie folders are named "4Hz" where the
paper and the descriptor give 3.9 Hz, most recordings are 2160 frames, three
3-min movies at 4 Hz, and frames are 128 x 256 pixels in 50 movies (and 357, 404
and 512 wide in one each), where the Methods give 512 x 128; the TIFFs carry no
time stamps, so the frame rate cannot be checked. The TIFF archive holds five
macOS resource-fork files beside the 53 movies, and no recording is deposited
twice. Questions are put to the paper's authors: which trace and which measure
give the pairwise correlation of Figure 1, with or without the mean subtracted
and at which lag; for peaks of synchrony, when a cell is active, how each trace
was shuffled and how the proportion of participating neurons is formed; and how
the pooled average correlation was formed and the unequal-variance 2 x 3 ANOVA
fitted, as the paper's s.e.m. fit an average of the three age means, not the
mean over mice.

The author's points on the protocol: the step-2 clock check assumes trial
tables or annotations, which this data set lacks, so the population rate was
compared with each movie's frame brightness, with the other movies and with
time-shifted rates; `docs/archives.md` does not say that `+` in a CRCNS file
name must be encoded as `%2B`; "run every reading" does not cover a reading
that cannot be run at all, so only T-a was run and the outcomes resting on it
were marked as assumed; a tar.gz cannot be opened in place like a zip, so it was
streamed once in order and each member hashed, as the archive's own MD5 needs
the whole stream; and the protocol does not say whether a variant for a blocked
claim may have its own tagged cell, so it was tagged `variant:` and stated to
decide nothing.
