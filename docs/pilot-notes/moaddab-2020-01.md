# crcns-pag-2, Moaddab et al. 2020

Thirteen claims reproduced (one on an assumption), four partially, one not
reproduced and two blocked, both for missing data. The first verification round
agreed with 19 of the 20 outcomes as they stood and the second with all 20;
nothing was proposed after the second, so there was no third round. CRCNS does
not version data sets, so the version is recorded as unversioned with the data
set's DOI (10.6080/K0833Q7F), and the zip's ETag matches `checksums.md5`. The
paper, Moaddab, Wright and McDannald in Scientific Reports (10, 18035), compares
12 female Long Evans rats given early adolescent adversity (EAA) with 8 Controls
in fear discrimination, where danger, uncertainty and safety cues predict foot
shock with probability 1.00, 0.375 and 0.00 while the rats nose poke for food,
and records 151 Control and 203 EAA single units in vlPAG/DR; the data set is
one `data.zip` holding the 354 unit files, the authors' cube built from them,
their script `vlpagAnalysis.m` and three cue sounds. The claims were written
from the flattened JATS text of the version of record, without the supplement,
and without code, as the lab page the paper names returned 404. The behaviour,
cue-responsive selection, population firing, regression and correlation claims
could be tested; the body weights of Fig. 1B, C and the pre-surgery
discrimination of Fig. 1E, F could not, nor the bregma part of the Fig. 4
ANOVAs. Reproduced are, among others, `fig2d-cue-responsive-counts` (32, 49, 48
and 84, the paper's counts exactly, from the cube's stored rates),
`fig2d-higher-proportion-responsive` (133/203 against 80/151, chi-square = 5.68,
p = 0.017), `fig4c-excited-inflated-onset`, `fig5efg-inhibited-fear-output`
(F(9,1170) = 2.15, p = 0.023) and, on the assumption that the regressions use
the cube's trial-wise Z score regressed on `cer.cue` (0/0 trials stored as 1) as
the script does, `fig5d-threat-tuning-curve` (group F(1,79) = 4.15, p = 0.045; p
= 0.07 to 0.24 under the claims file's readings). Partial are
`fig4ab-excited-temporal-pattern` and `fig4de-inhibited-temporal-pattern` (the
interaction holds, the bregma part cannot be tested),
`fig5abc-excited-reduced-threat-probability` (the threat beta is higher in
Control, p = 0.037, but the group by regressor interaction has p = 0.055) and
`fig6-excited-firing-threat-decoupled` (the danger part holds and the
uncertainty part fails under all twelve readings with the Methods'
normalization; with the script's, every part holds under nine). Not reproduced
is `fig7-inhibited-firing-fear-output`: Control uncertainty firing over the last
5 s of the cue correlates with the fear output beta under every reading (r =
0.35 to 0.73, p <= 0.015), where the paper gives R2 = 0.04, p = 0.16. The
author's first run had the same outcomes, and the author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1 disagreed
on fig6 (reproduced under the script's normalization), and asked that this
normalization be run as a full reading, that one rule choose among the twelve
regression readings, that the script be searched for bregma levels and that the
paper's smaller degrees of freedom be looked into; in reply the normalization
was run under all twelve readings, the script's combination was adopted for
every regression claim with a table showing it closest to the paper's statistics
(mean relative deviation 0.076, next 0.167), the script was found to have no
occurrence of bregma, fig6 was kept partial as the Methods decide, and first-5 s
firing was found to give the paper's Fig. 7 statistics. Round 2 agreed with all
20 outcomes, withdrawing its fig6 view, asked that the assumption flags of
fig5abc and figs4 be dropped as the claims file's readings give the same
outcomes, raised one cue-inhibited design not of full rank, and found text the
outputs did not support, among them an EAA safety p range of 0.03 to 0.04 where
the cell printed 0.0084 to 0.040; in reply the two flags were removed, the
script's regression lines were printed, a Matlab-style fit was added that
changes no outcome, and the text was corrected. The author's run went from 19:53
to 20:24 UTC; the notebook ran in about 60 s at first, 59 s after the
author-answers run, 42 s after round 1 and 68 s after round 2, and nothing
failed, though two clean-up commands were denied by permissions, leaving an
empty harness folder in the entry. The untracked dotfiles in the repository root
were left alone.

The Methods describe the normalized firing as the trial-averaged differential
firing Z scored over all bins and trial types of a neuron, while the authors'
script averages the cube's trial-wise Z scores (each trial's own 2 s baseline
subtracted, Z scored over all trials and bins); only the script's version gives
the statistics of Figs. 4C, 4F and 6 to the second digit (group F(1,79) = 4.96
and F(1,130) = 10.81 against 4.96 and 10.82), and with the Methods' version the
uncertainty part of Fig. 6 fails. The legend of Fig. 7 and the Results take
cue-inhibited firing over the last 5 s of the cue, but the script computes it
only over the first 5 s and the whole cue (vlpagAnalysis.m lines 2796 to 2817),
and the paper's Fig. 7 statistics follow from the first 5 s (Control uncertainty
R2 = 0.042, p = 0.16 against 0.04, 0.16; safety Z = 0.60 against 0.60), where
last-5 s firing gives R2 = 0.49 (p = 2.8e-8). The group of each rat is given
only by lists in the script (lines 99 to 122), and the event codes EVT01 to
EVT14 are not described: EVT09, EVT11 and EVT12 are the cue onsets, which cue
each marks depending on the behaviour program in the file name (epr38a, b, c),
EVT08 holds the shocks, EVT13 the nose pokes, EVT14 a marker about 31.5 s after
each onset, and EVT02 could not be identified. The cube stores raw firing rates
as unsigned integers truncated towards zero (775 trials with spikes have a
stored 10 s baseline of 0), and the paper's counts of cue-excited and
cue-inhibited neurons follow exactly from these truncated rates; with exact
rates from the spike times the Control cue-inhibited count is 54, not 48. The
cube stores a suppression ratio of 1 for the 255 unit-trials (143
session-trials) with no nose poke in the baseline or the cue, and the paper does
not say how such trials are treated. The units come from 182 recording sessions
(74 Control, 108 EAA) where the paper and the data description state 72 and 107;
the unit and rat counts match, and the extra sessions are not duplicates. The
data description calls poke.base the nose poke rate 2 s before the cue where it
is the rate in the 20 s before cue onset (99.8% of trials), in pokes per minute,
and gives the uncertainty shock rows a shock probability of 0.25 where the paper
and the description's own summary give 0.375. It gives no bregma level per rat,
only how many rats were at each of four levels, and does not say that spikes and
nose pokes are stored only from about 20 s before to about 33.5 s after each cue
onset. The body weights and the eight pre-surgery discrimination sessions are
not in the data set. Questions are put to the paper's authors: which trial-wise
normalized firing and which treatment of trials with no nose poke entered the
regressions of Figs. 5 to 7; which neurons were left out of tests whose error
degrees of freedom are smaller than the selected neurons give (Fig. 5A to C
t(66) and F(1,65) for 81 cue-excited neurons, Fig. 4A, B F(110,8360), Fig. 2E, F
F(2,346) for 354 neurons), and why; and whether the firing in Fig. 7 was taken
over the first 5 s of the cue and not the last 5 s the legend gives.

The author's points on the protocol: the protocol names only code the paper
links, while this zip holds the authors' own script, which was used to settle
details the paper leaves open, with line numbers cited; no outcome fits a
criterion with one part untestable, so the bregma ANOVAs were recorded as
partially reproduced with the reason in the notes; the protocol gives no route
when the claims file follows the Methods but the data show the paper's numbers
came from the script, so the claims file's method was kept with a
`code_mismatch` finding; with twelve reading combinations, accepting a claim
under any one invites fishing, so the script's combination was adopted for every
regression claim; the clock check's shift into the inter-trial interval is
impossible when the streams are stored only around trials, so onsets were
shifted 10 s earlier for the spikes (221 responsive units drop to 15) and the
cue labels permuted for the pokes; truncated cube rates against exact spike
rates is a data variant the readings concept does not cover, so the script was
followed and both shown; and developing on a subset did not apply, as the whole
data set loads in 35 s.
