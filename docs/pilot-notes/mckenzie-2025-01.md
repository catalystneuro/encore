# mckenzie-2025, McKenzie et al. 2025

Six claims reproduced, three partially, five not reproduced and fourteen
blocked, all fourteen for missing data. Nine outcomes rest on an assumption.
The first verification round agreed with 27 of the 28 outcomes and gave
`figs7cd-movement-not-time-locked` as partially reproduced where the record had
not reproduced; the author took it. The second round agreed with all 28 and with
the critical finding, and nothing was proposed after it, so there was no third
round. It pins version 0.230630.2304, the version the paper cites, and takes the
CellExplorer cell types, the epoch names and the LFP of one session
(e13-26m1-211119) from version 0.261113.1035, whose spike times are identical.
The paper, McKenzie, Sommer, Donaldson et al., "Event boundaries drive
norepinephrine release and distinctive neural representations of space in the
rodent hippocampus" (eLife 14:RP105183), records norepinephrine (NE) in dorsal
CA1 with GRAB-NE fiber photometry and reports that it rises on each context
transition and decays over minutes, faster with experience, and reanalyses the
CA1 recordings of Huszar et al. (2022), deposited here, to report that the
spatial code settles over minutes after transfer, that moments 10 to 11 minutes
after a novel transition are more reactivated in post-experience ripples than
moments in the first minute, and that track patterns are absent from ripples
before the experience. The claims were written from Reviewed Preprint version 1;
the paper links no code and has no data availability statement. The 13
photometry claims and the NE half of `ne-and-settling-time-course` are blocked,
as the photometry is deposited nowhere. The ensemble size reproduces on all
units, not on pyramidal cells; the settling claims of Figure 7E to 7G and the
unconditioned similarity of Figure S7G and S7H reproduce, Figure 7G more weakly
than the paper's t(7) = 7.58. The UMAP embedding maps position but early moments
are not at its periphery, and out-of-field firing falls and movement is unrelated
to time only in the familiar run. The novel-run decorrelation of Figure S6B, the
time-only model of Figure S7E and S7F, where dropping |dvel|NN also worsens the
fit in both runs, and the three reactivation claims are not reproduced: late
moments are not more reactivated (-0.0214 percentage points, p = 0.253), the
familiar run shows early above late (p = 0.0134), and pre ripples reactivate
0.1373% and 0.1491% of moments, above the 0.1% false positive rate. With time 0
at the first tracked frame, a variant not judged, Figure 8B and 8D would be
reproduced; the claims file reads transfer as the epoch start, and the question
went to a reader in `questions/mckenzie-2025.yaml`. Round 1 found that time 0
did not fit the data, that E1 reading (b) for e16-3m2-211211 was possible but
not run, that the reactivation readings were not fully crossed, that the
time-only model's sign constraints could not follow a rise, and that the ripples
were the deposited ones, not detected from the LFP; in reply the variant was run,
the linear-track epoch of e16-3m2-211211 was run throughout, the readings were
crossed in two notebooks, every beta was bounded at +-10 as the photometry
Methods say, and ripples were detected from the LFP streamed one channel at a
time, with the deposited ones as a variant. Round 2 found sentences the outputs
did not support, on the UMAP ranges, the reactivation rates and the README, which
were corrected, and asked that the pre-ripple rate be split by minute; in the
novel run the excess comes from minute 1, and the outcome holds under every
variant. The untracked second environment of e15-13f1-220118, e15-13f1-220119
and e16-3m2-211212 was not run for decorrelation or reactivation, for lack of
time. In the author's first run the notebooks took 11 and 35 minutes, with peak
memory 4.1 GB; at the end they took about 23, 57 and 34 minutes, the novel
reactivation notebook close to the 60-minute limit.

The dataset was converted by CatalystNeuro (contributors Garrett Flynn and Cody
Baker). In session e16-3m2-211211 the tracking and the 45 trials of the novel
linear track are filed from 9575 to 11203 s, inside the open-field epoch, where
spikes carry no spatial information about the position at any shift (0.246 bits
per spike at zero shift); moved by 5564.5 s onto the linear-track epoch, the same
tracking gives 0.656 bits per spike at zero shift, and version 0.261113.1035
files it at the same wrong times (critical). The pinned version has no cell types
and no epoch names, and e13-26m1-211116 has no epochs table, so pyramidal cells
and the home cage, familiar and novel periods cannot be told apart (major); it
has no open-field tracking, so three sessions have one tracked run and four with
two novel environments have only one tracked (major); and it has no raw file, so
no LFP, for e13-26m1-211119 (minor). All of these are fixed in 0.261113.1035,
which gives the open-field tracking in the lab's units without a scale. The x, y
position of five novel runs spans 0 to 1 while the series states cm, so location
was binned on the linearized position; tracking starts 14.6 to 63.3 s after the
maze epochs begin and the files do not say when the mouse was placed in the
maze, which decides Figure 8B; and in three files the behavior module's
description spells its recordings as single letters. In the paper, the ensemble
size (mean 253.8, 191 to 363) is the count of all units in the nine sessions with
a tracked novel run, where the Methods analyze only pyramidal cells (mean 211.0)
and every test has 8 sessions, and the Methods list 7 environments for 8
sessions. Seven questions are put to the paper's authors, on the location used,
the sessions and runs, a speed filter, the 100-s moving average, the pre ripples,
z-scoring and shuffle pool, the model of Figure S7E and S7F, and the pyramidal
cell thresholds.

The author's points on the protocol: it does not say what to do when the cited
version lacks labels a later version adds, and `entry.yaml` can name only one
version per dataset; it does not say how to handle a recording known to be
misfiled; crossing every reactivation reading would push a notebook past the
time limit; and "absence is judged on the paper's test alone" does not fit when
the criterion leaves a reading open, where the first-listed reading was used and
the outcome marked assumed.
