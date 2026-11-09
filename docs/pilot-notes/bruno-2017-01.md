# crcns-apl-1, Bruno et al. 2017

Twenty-two claims reproduced, four partially, three not reproduced and one
blocked, for insufficient metadata; three outcomes rest on an assumption,
`fig3h-perturbations-return`, `fig4c-orbital-period` and
`fig7gh-robust-to-participation`. The first verification round agreed with 24
of the 30 outcomes as they stood and disagreed on fig3h, fig4c,
`fig6d-decode-p10`, `fig6s2-dimensions-p10`, fig7gh and
`fig7s2-no-invariant-core`, the second agreed with 29 and held that fig6d was
not reproduced, and a third round, on that one claim, agreed with the change
proposed after the second. CRCNS does not version data sets, so the version is
recorded as unversioned with the data set's DOI (10.6080/K0SN074B) and the MD5
sums of the files read, which match the data set's own `checksums.md5`. The
paper, Bruno, Frost and Humphries in eLife (6:e27342), images the dorsal pedal
ganglion of isolated Aplysia preparations with a voltage-sensitive dye and a
464-element photodiode array while three bouts of fictive locomotion are
evoked in each of 10 preparations, and reports that the evoked population
activity forms a low-dimensional periodic orbit, that sequential bouts of a
preparation converge on the same manifold and return to it after
perturbation, that the local dynamics are a stable spiral attractor, that the
P10 nerve's motor output can be decoded from the orbit, that single neurons
vary widely in participation with no invariant core, and that strongly
participating neurons lie in the caudo-lateral quadrant of the ganglion; the
data set holds the spike times of the 30 recordings, the P10 channel for three
preparations and neuron location maps for eight. The claims were written from
the version of record (PMC5546814) as JATS XML flattened to text, with the
legends of all figures and of the twelve figure supplements but without a PDF,
and from the paper's MATLAB code at commit e5f28e98, for 30 claims. All but
`fig8-caudolateral` could be tested, as nothing says how the array is
oriented. Reproduced are, among others, `fig1d-slow-oscillation` (0.0486 Hz),
`fig2b-dimensions`, `fig2ef-periodic-recurrence` (26 of 30 periods in 9 to
16.5 s), `fig3c-same-manifold` and `fig3f-pairwise-similarity`, whose failing
pairs are the ones the paper names, fig4c (10.45 s, though the per-response
periods do not correlate with the recurrence periods, r = -0.063), fig6s2
under own/le80 only, and `fig7s2-no-invariant-core` (0 or 1 of 10
preparations with a core) on a Python port of the code's ensemble toolbox not
checked against MATLAB. Partial are `dataset-size` (10 preparations, 30
recordings and 1131 neurons, but only 12 of 30 recordings in 108 to 198
neurons), fig3h (15 of 16 kept periods returned, both counts just below their
tolerances, met only under own/le80), `fig4bc-stable-spiral` (the grand mean a
stable spiral, 8 of 10 preparations with two of three responses in the
region) and fig7gh, where one of the two absences holds and the other fails.
Not reproduced are `fig3a-coalescence` (within one period of onset in 12 of 30
responses against 27 required), `fig4s1a-contracting-dimensions` (11 of 30)
and fig6d, where response 1 of preparation 4, the one the paper describes as
apparently chaotic, fails under every reading of width and count, with
histories up to 100 ms and with the code's windowing, and the criterion
requires all nine. The author's first run had 20 reproduced, 5 partially, 3
not reproduced and 2 blocked, with fig7s2 blocked as not runnable in the time.
The author asked no questions of a reader, so the answer and author-answers
runs changed nothing. Round 1 held that the adopted reading (own/min80) fails
fig2b by one response and that no single reading makes the chain of claims
hold, that fig7gh and fig6d had been run under too few readings, that the
fig3h and fig3i passes are reading-shopped, that fig7s2 was testable and that
fig1d might measure the rate decay; in reply every reading was run through
fig6d and fig7gh, the weak-evidence wording added, fig7s2 tested with the
ported toolbox, a detrended spectrum added (an oscillation besides the decay),
windows counted at at least 90%, and fig6s2 moved to reproduced, fig7gh to
partial and fig7s2 to reproduced. The author's revision also found that the
committed notebook had none of its written text, as the author run had built
it without its text file, and recovered the text from the author transcript.
Round 2 found sentences the outputs did not support, among them the dimension
ranges, the "consistent with" sentence of fig4c and an unreported fact on
fig3h, where the code's removal rule keeps 19 periods of which 18 return, and
in reply the author found that the P10 decoding gives different numbers in
different executions, as forecasts diverge up to about 1e13 spikes/s in some
windows of the longer histories. Round 3 found that the fig6d prose came from
a different execution than the notebook it reviewed, and the re-run gave yet
another set of numbers; 8 of 9 responses pass under every reading in every
execution so far. The author's run took about 2 h (12:03 to 14:03 UTC); the
notebook ran in 1078 s at first, with peak memory about 1.3 GB, 931 s after
the author-answers run, 33.8 min after round 1 and 39.6 min after round 2. One
cell failed on the first development run, on a pandas column name, and was
fixed.

The Methods give the Gaussian width as the median ISI divided by 12 (possibly
its square root, lost in the extraction), but the code uses the median ISI
itself, as a running median over the recordings of the same bout number, and
the printed widths give 21 to 76 dimensions, not the paper's 4 to 8; the
Methods keep the dimensions for at least 80% of the variance, the recurrence
and participation code those at most 80% and the manifold code the smallest
number reaching 80%, and the outcomes of fig3h, fig4c and fig7gh change with
the choice. The orientation of the photodiode array is given nowhere:
Coordinates.mat gives each neuron's x and y on a 0 to 50 scale without a unit,
and neither the files, plot_maps.m nor the data description say which
direction is rostral, caudal, medial or lateral, so the caudo-lateral quadrant
of Figure 8 cannot be located. The paper gives 120 to 180 neurons per
recorded population and 1131 in all over 10 preparations, which cannot both
hold; the data set holds 75 to 160 per preparation, 1131 in all, as its
description says. Figure 6D's N = 173 forecast windows is close to the code's
windowing (174 per response), not the Methods' (40 per response). In
What_is_Participation.m two of the three pairs are mismatched between rate
and participation changes (mean R-squared 0.239 with matched pairs, 0.205 with
the code's), and LocalLinearDynamics.m can miss gaps in a point's
neighbourhood. The P10 spike times lie on a grid of 0.614 ms (1629.7 Hz), as
the description's 1630 Hz, where the paper says 1600 Hz, and the P10 files of
preparation 2 are named Jun0414da0Np10.mat while its spike and coordinate
files are Jun0414B. The clock check is consistent with a shared clock but does
not separate the data from shifted series in 2 of 9 recordings, and neuron
ids were taken to name the same neuron in all bouts, as the description says,
which per-neuron spike counts support (30 of 30 bout pairs above permuted
ids). Questions are put to the paper's authors: which kernel width was used
and whether the median ISI was per recording, which rule for the number of
dimensions produced Figures 2 to 5, whether the two-cycle rule for divergent
periods uses the mean or the median period and applies to all of them or only
to those that never return, and which permutation test gave Figure 5B.

The author's points on the protocol: it does not say how far readings of an
early detail such as the kernel width or the number of dimensions must be
carried into the claims that depend on it, so four were carried through every
claim; it does not say what `measured` should be for a claim stated as a
range, so the quartiles were recorded; the clock check is described for trial
tables, so cross-correlation against circular shifts was used, which is weak
for a 10 s rhythm; there is no rule for a criterion whose parts hold under
different readings, nor for choosing between partial and not reproduced when
one part fails; for claims of absence readings do not apply, while the inputs
to the test still have readings; and the 10-minute aim conflicts with running
every reading.
