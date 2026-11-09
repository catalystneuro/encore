# crcns-nac-1, Ray et al. 2022

Sixteen claims reproduced (12 on an assumption), seven partially (all seven on
an assumption), ten not reproduced (nine on an assumption) and one blocked, for
missing data. The first verification round agreed with 31 of the 34 outcomes
as they stood and the second with all 34; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0M906VB),
and the author pinned `data.zip` by its MD5. The paper, Ray, Moaddab and
McDannald, "Threat and Bidirectional Valence Signaling in the Nucleus Accumbens
Core" in the Journal of Neuroscience (42:817-833), records 368 nucleus
accumbens core (NAcc) units from 95 sessions of seven female Long-Evans rats
during fear discrimination, in which danger, uncertainty and safety cues
predict foot shock with probability 1.00, 0.25 and 0.00 while the rats nose
poke for food; it screens 193 cue-responsive units from 82 sessions, clusters
them by k-means into Threat Excited, Threat Inhibited, Danger Excited,
Bidirectional Valence and Non-Selective populations, and relates their firing
to threat, reward and nose poke cessation. The data set holds one MATLAB file
per unit, a precomputed cube and the authors' MATLAB scripts
(cubeScriptPR25.m and mainAnalysis.m), which the paper does not link; the
author's loader reproduces the cube exactly for all 368 units. The claims were
written from the PyMuPDF text of the version of record, without the Extended
Data and without rendering any figure; the paper's code page,
http://mcdannaldlab.org/resources, returned 404. The author used the scripts
as the paper's code, with the Methods first and the scripts as a reading or a
variant. Every claim could be tested except `fig1c-acquisition`, whose
pre-surgery sessions are not deposited. Most outcomes rest on two assumptions:
that the cue-responsive units are those of the scripts' screen on rates
floored to whole Hz, the only procedure that gives the paper's 193 units and
82 sessions, and that the populations are the partition among the claims
file's readings whose centroids best match the five patterns the Results
describe (N4 normalization, most frequent of 100 k-means++ starts), with 6, 28,
45, 89 and 25 units against the paper's 5, 26, 55, 91 and 16. Reproduced are,
among others, `cue-responsive-193` (211 units from 81 sessions under reading
(b)), `fig1g-discrimination` (F(2,12) 52.6 to 57.4, its uncertainty minus
safety CI excluding zero only with 0/0 suppression ratios read as 0, on the
median bounds over 50 seeds), `fig1h-discrimination-safety` (R = -0.978 to
-0.986 against the paper's -0.98), `fig6-thi-greatest-similarity` and
`fig8ab-thi-exaggerated-threat`. Partial are, among others,
`fig2-five-clusters` (the five patterns appear, no reading gives the five
counts within tolerance), `fig4ab-thi-threat-firing` and
`fig4cd-de-danger-firing` (the effects hold with means beyond tolerance) and
`fig9efg-reward-cue-correlations`. Not reproduced are, among others,
`units-recorded` (90 sessions against 95, with a tolerance of zero),
`populations-by-rat` (Threat Excited units from 3 rats),
`fig5ab-the-onset` (interaction p 0.08 to 0.11 on the assumed partition,
reproduced on the alternative N2 partition), `fig6e-de-similarity` (p = 0.023
and 0.011 against 0.0056) and `fig9hij-danger-safety-correlations`. The
author's first run had 17 reproduced, 8 partially, 8 not reproduced and 1
blocked, with units-recorded and fig9bcd partially reproduced and fig10bcd
reproduced. The author asked no questions of a reader, so the answer and
author-answers runs changed nothing. Round 1 disagreed on units-recorded (not
reproduced), fig9bcd (not reproduced) and fig10a (not reproduced), and found
that the reward and cessation baseline was the 2 to 1 s before the event where
the Methods say the 1 s before, that event windows ran past the recorded
segments and the last poke before a recording pause counted as a cessation,
that every judgement used the reflected bootstrap interval while the paper's
Figure 1G CIs match the non-reflected one, and that the partition was chosen by
a rule the claims file does not give, with N4 (0.79) and N2 (0.77) almost tied;
in reply units-recorded and fig9bcd were changed, the baseline and the events
were corrected, which moved fig10bcd to not reproduced and left fig10a
reproduced on the claims file's reading (interval p = 0.26 and 0.12,
interaction p < 1e-4), a section judging every CI-based claim under both
interval forms, two standard errors and five seeds was added, the alternative
partition was set beside the assumed one, and three questions went to a reader
in `questions/crcns-nac-1.yaml` (the 0/0 reading, the scripts' normalization
and the interval form), a file written after the answer run, so the questions
are unanswered. Round 2 agreed with all 34 outcomes, asked that fig1g be marked
assumed, as the authors' 0/0 handling leaves its uncertainty minus safety CI
containing zero in every seed with the standard interval, and found text the
outputs did not support, among them smallest cosines given as below 0.5 where
three partitions print 0.65 to 0.73 and a largest difference of 1.3e-15 where
the cell printed 9.09e-16; in reply fig1g was marked assumed, the text was
corrected, and a fourth question, on the overlapping conditions of the fig9efg
criterion, was added. The author's run went from 03:54 to about 04:26 UTC; the
notebook ran in 57 s at first, 103 s after the author-answers run and about 5
minutes after round 1, and nothing failed in the final run. The untracked
dotfiles that appeared in the repository root were left alone.

The paper's population labels are not deposited, and mainAnalysis.m computes
them with one MATLAB k-means start after rng(1), which cannot be repeated
outside MATLAB; the reproduced clustering is unstable (each normalized
partition found in 1 to 3 of 100 starts) and does not give the paper's counts,
so every population claim rests on a reproduced partition, and the near-tied
alternative changes the outcome of fig5ab and the Threat Inhibited extreme of
fig7. The authors' scripts differ from the Methods in ways that change
results: firing is normalized per trial against a floored 2-s pre-cue rate and
z-scored over all trials and bins, where the Methods average each trial type
and subtract its 10-s baseline; the screen and the normalization use rates
floored to whole Hz; 0/0 suppression ratios are set to 1; the reward and
cessation baseline is the 2 to 1 s before the event; and the waveform measure
is half the scale of Figure 3C. The scripts' normalization brings several
effect sizes close to the paper's (fig4cd 0.24, 0.25 and 0.16 against 0.22,
0.21 and 0.17), and setting 0/0 to 1 gives the paper's F(2,12) = 57.41
exactly. The 95% bootstrap CIs printed for Figure 1G match the bootstrap-t
quantiles added to the mean without reflection ([0.36, 1.03] against the
paper's [0.35, 1.03]; the studentized interval is [-0.09, 0.59]). The
recording is paused between trials, so the files hold spikes, pokes and
pellets only from 20 s before each cue onset to about 33.5 s after it, which
the data description does not say; the claims file's ITI reading (a) holds no
event, and under reading (b) 301 of 2159 rewards and 2737 of 15363 cessations
were dropped. The data set holds 90 sessions where the paper and the data
description say 95 (ac01 17, ac03 17, ac04 10, ac05 17, ac06 16, ac07 7 and
ac08 6), and counting distinct rows of suppression ratios, as mainAnalysis.m
does, gives 84; no unit is deposited twice. The eight pre-surgery sessions of
Figure 1C are not deposited; preRecordingBehavior.m reads them from a folder
(AC Group Data) that is not in the data set. The data description does not say
which EVT channel holds which event or that the cue channels change with the
behavior program; only cubeScriptPR25.m gives the map (EVT01 shock, EVT02
pellet, EVT13 poke). It says NAcccube.poke.base is the nose poke rate 2 s
before the cue, where cube.mat holds the rate over the 20 s before it.
Questions are put to the paper's authors: which normalization and which
k-means run produced the published populations, and whether their labels can
be deposited; how the inter-trial interval events for reward and nose poke
cessation were chosen, given the recording pauses; and how 0/0 suppression
ratios were handled.

The author's points on the protocol: scripts in the data set that the paper
does not link have no defined status, so they were treated as the paper's code
with the Methods first, run as a variant where they contradict the Methods and
as a reading where they settle a detail the Methods leave open; there is no
rule for choosing among reconstructed partitions that downstream claims depend
on, so the one best matching the five described patterns was used and each
claim reported under all 12; there is no rule for a bootstrap bound near zero
that flips with the seed at n = 7, so the median bounds over 50 seeds were
used; the protocol does not say whether running every reading combines with a
claims file's "reproduced under any reading" rule, so that rule was used for
the claims file's readings and claims of absence were judged on the paper's
procedure; a claims-file reading that the data cannot support (ITI reading
(a)) was run, shown and called unsupportable; and neither the CRCNS guidance
nor the protocol says how to pin an unversioned archive in the notebook, so
`unversioned` and the MD5 were recorded in the helper and the header.
