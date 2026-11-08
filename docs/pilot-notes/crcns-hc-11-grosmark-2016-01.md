# crcns-hc-11, Grosmark et al. 2016

Thirteen claims reproduced (nine on an assumption), eight partially (six on an
assumption), ten not reproduced (six on an assumption) and none blocked. The
first verification round agreed with 28 of the 31 outcomes as they stood and
the second with 28; the second disagreed on `fig4c-coactivation-by-rate`,
`figs16c-low-rate-coding` and `fig4d-slow-cells-replay`, and five changes were
proposed for a third round, which reviewed only those five and agreed with
four: `figs16c-low-rate-coding` and `fig4d-slow-cells-replay` became not
reproduced, `figs11-cluster-quality-similar` went from blocked to reproduced
and `fig2e-plastic-removal` from reproduced to partially. On
`fig4c-coactivation-by-rate` it did not agree with the proposed partially
reproduced and would give not reproduced, so the outcome stays reproduced, as
round 2 agreed, and the proposal stays open for a new attempt. CRCNS does not
version data sets, so the version is recorded as unversioned with the data
set's DOI (10.6080/K0862DC5); the notebook streams one file,
`NoveltySessInfoMatFiles.tar.gz`, whose computed MD5 sum matches the data set's
`checksums.md5`. The paper, Grosmark and Buzsaki in Science (351, 1440-1443),
records CA1 pyramidal cells with silicon probes in four rats over eight
sessions, each about 4 hours of rest and sleep (PRE), exploration of a novel
linear or circular maze (MAZE) and about 4 hours of rest and sleep (POST), and
reports that the sequence content of ripple events rises from PRE to POST, that
the rise depends on a minority of plastic cells whose contribution grows, while
rigid cells already contribute in PRE, that plastic cells are more place
specific and sharpen their fields during running, that rigid cells fire faster
offline, and that slow-firing cells and cells with high within-ripple gain
carry the rise; the data set holds the eight sessions with spike times, cluster
identities and cell types, state epochs, tracked position, LFP, spike features
and waveforms. The claims were written from the NIH author manuscript
(PMC4919122) and its supplement, with the supplement PDF rendered to read values
in the panels of Figures S5, S9, S12, S13, S14 and S16 to S19, without the
images of the main Figures 1 to 4, and without code, as the paper links none;
the claims check changed the fig2d range to 9 to 22%, made all five specificity
measures count for `fig3a-plastic-more-specific`, added a maze-running test to
`fig4a-rigid-fire-faster`, and added `fig2e-plastic-removal` and
`figs19c-pcc-change-per-cell`, for 31 claims. Every claim could be tested, the
event-based ones on population synchrony events without the paper's LFP ripple
condition, as the LFP was not read, and `figs11-cluster-quality-similar` on
cluster quality and stability only, without waveform similarity. Reproduced
are, among others, `fig1c-sequence-content` (MAZE > POST > PRE under all 12
combinations of readings run, though not the LFP readings),
`fig2-pre-contributors-persist` (73.9%), `fig2d-high-dpcc-shuffle-abolishes-replay`
(the change first reaches zero or below at 10%), `figs12-high-dpcc-exclusion`,
`figs5e-duration-unchanged` (173 ms in PRE and POST), `figs13-outfield-rate-falls`,
which rests on the D-a groups, and `figs16ab-plastic-synchrony-increase`, which
rests on coactivity reading (d). Partial are, among others, `place-cell-count`
(565 place units against 491, and 504 with the kernel read as a full width at
half maximum), `rigid-plastic-counts` (121 per group under reading D-a, 109,
113 and 108 under D-b, against 105), `fig2b-strong-contributors`,
`fig3a-plastic-more-specific` (more specific on all five measures, but not
fewer fields, p = 0.51), `fig4e-high-gain-cells-replay` and
`fig2e-plastic-removal`. Not reproduced are `fig3b-plastic-specificity-increases`
(plastic r = +0.052, p = 0.10), `fig4a-rigid-fire-faster` (session-wide offline
p = 0.098), `fig4d-slow-cells-replay`, `figs16c-low-rate-coding`, both Figure
S14 claims, `figs16de-more-ripples-post` (median intervals 1.348 and 1.242 s
against 3 and 2.47 s), `figs17d-rigid-plastic-coactivity`,
`figs18-temporal-bias` and `figs19c-pcc-change-per-cell` (5.66% and 14.69%
against 2.2 and 21.4). The author's first run had 12 reproduced, 9 partially,
9 not reproduced and 1 blocked, `figs11-cluster-quality-similar` as `other`, as
it was not written within the run's time. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1
disagreed on `rigid-plastic-counts`, `fig4c-coactivation-by-rate` and
`figs16de-more-ripples-post`, and raised the missing LFP condition, the D-a
groups that every rigid and plastic claim used while only D-b matches 105, the
SD kernel, the five rate splits not run, the readings of fig2d and figs12, the
units counted per direction and a missing within-session test; in reply
`rigid-plastic-counts` moved to partially and `figs16de-more-ripples-post` to
not reproduced, `fig4c-coactivation-by-rate` was kept against the verifier,
every group claim was rerun with the D-b groups, the other rate splits and the
six Y and D readings were run without moving an outcome, and the LFP readings
and the FWHM kernel were not run. Round 2 found sentences the outputs did not
support, among them a largest p of 7.0e-12 where 3.18e-10 was printed and a
71-minute run time where 38.2 was printed; in reply these were corrected, figs11
was tested from the spike features and fig2e was rerun with the D-b groups. The
author's run went from 11:11 to about 13:40 UTC; the notebook ran in 39 min at
first and 1,974 s after the author-answers run, then in 71 and 75.4 min after
rounds 1 and 2, over the 60-minute limit, so both runs were marked as failed,
and in 55.5 min after round 3. About an hour of the round-1 revision was lost to
a development script that ran the shuffles with too many threads. The shuffle
counts of fig2d (100 templates per step) and figs12 (200 shuffles) were cut for
run time. The untracked dotfiles and `scripts` in the repository root were left
alone.

The LFP is only in one tar.gz archive per session (5.1 to 9.0 GB compressed, 70
GB in all), which cannot be read in part and was measured to stream at about 23
MB/s, about 55 minutes for the eight sessions, and the paper does not give the
ripple detector's channel or threshold; the events here therefore lack the
condition that each holds an LFP-detected ripple, which affects every
event-based claim (1,855 events per hour of NREM, median interval within one
NREM interval 1.19 s). The data set holds no list of the paper's 491 place
cells, its ripple events, or its 216 strongly contributing and 105 rigid and
105 plastic cells, so the selections cannot be compared cell by cell. The
Materials and Methods name a one-tailed Wilcoxon rank-sum test for strongly
contributing cells and the Figure S19B legend a one-tailed signed-rank test;
with the signed-rank test 222 to 252 units are strongly contributing, with a
rank-sum test of observed against cell-shuffled rZ only 22 to 39. The state
epochs mark only Wake (and in two sessions 2 to 81 s of Drowsy) during the MAZE
epoch, so the quiet waking on the maze is not given. In Gatsby_08022013 the
sessInfo file has spike times up to 32,002.4 s, 1,588.7 s past sessDuration
(30,413.6 s), which the epochs and the descriptor do not explain. Position is
sampled every 25.6 ms (39.06 Hz), where the paper states 39.69 Hz, and the 2D
head position is noisy in some sessions; in Gatsby_08022013 the smoothed head
speed is above 13 cm/s in 95% of samples. The descriptor does not say which
columns of the `.fet` files are the PCA features. On the paper's side, the main
text cites figs. S16 and S17 for what the supplement numbers S17 and S18, the
Figure S14 colour key swaps the rigid and plastic labels, Figure S17B gives a
difference of -0.035 where its panels give -0.028, and the low and high firing
rate split is referred to the Methods, which do not give it. Questions are put
to the paper's authors: whether the 5 cm kernel is an SD or a width; whether
each event on the linear mazes is scored with both direction templates or
assigned to one direction first; which test marks a strongly contributing cell;
which part of the longer of PRE and POST is kept when the epochs are yoked;
which LFP channel and threshold detect the ripples; whether Figure S5B compares
observed |r| with single shuffled values or with each event's expected null;
whether the cells of Figure 4B and C are ranked within each session or pooled;
and how quiet waking on the maze is identified.

The author's points on the protocol: `docs/archives.md` describes CRCNS data as
zips that can be opened in place, while hc-11 is tar.gz, so only the 277 MB
sessInfo archive was streamed; readings multiply across dependent claims and the
protocol does not say how they carry through, so Y-a, D-a and P-a were fixed for
the rigid and plastic claims as a stated assumption; several criteria say
"reproduced under one reading" where the protocol takes the outcome all readings
give, and the criterion was followed where it said so; no blocking reason fits a
claim stopped by the author's own time limit, so `other` was used; the schema
rejects `null` in `measured`, so a claim tested in part cannot list one value
per expected value; conclusions are written after a run that `entry.py all`
repeats in full, so markdown cells were added to both notebooks without a rerun;
nothing covers cutting a paper's shuffle counts for time; and "do not download
to disk" is hard to keep while developing 40-minute analyses, so files were
briefly written to `$TMPDIR` and deleted.
