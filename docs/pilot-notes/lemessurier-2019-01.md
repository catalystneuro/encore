# crcns-ssc-10, LeMessurier et al. 2019

Fourteen claims reproduced, eleven partially, eight not reproduced and one
blocked, for missing data; no outcome rests on an assumption. The first
verification round agreed with 31 of the 34 outcomes as they stood and the
second with 32; the second proposed two changes, so a third round reviewed
those two and agreed with both. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0DB801M).
The paper, LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen and Feldman in eLife
(8:e46321), images GCaMP6s in L2/3 (Drd3-Cre) and L4 (Scnn1a-Cre) excitatory
cells of mouse S1 under anaesthesia while nine whiskers are deflected one at a
time, in mice raised from weaning either enriched (EN) or normally housed (NH),
and reports that enrichment strengthens the response to a column's own whisker
in L2/3 and suppresses it in neighbouring columns, makes more L2/3 cells tuned
to the column whisker, sharpens ranked receptive fields, sharpens the drop in
signal and noise correlation at column boundaries and improves the decoding of
whisker identity, while in L4 it weakens responses; the data set holds the
population imaging of all four groups as one 4.7 GB tar.gz, with raw and
neuropil traces, dF/F, stimuli, trial-aligned traces, stored responsiveness
p-values and ROI positions relative to each barrel. The claims were written
from the version of record (PMC6697414) as text flattened from the Europe PMC
XML, with the figure legends and figure supplements but without a PDF or any
figure, and from the paper's pipeline code at commit 5a21c9f, from which many
functions the figure scripts call are missing, among them the computation of
the equivalent best whiskers (eBWs); the claims check made eleven changes,
among them rewriting the criterion of `fig5eh-l23-correlation-gradient-at-edge`
and removing a rule that let some values fall outside tolerance in
`fig5a-l23-signal-correlation-boundary` and `fig6-l4-within-column-correlations`,
for 34 claims. All but `fig1f-gcamp-matches-spikes` could be tested, as the
cell-attached recordings with simultaneous imaging are not in the data set.
Reproduced are, among others, `table1-mice-and-fields` (the mouse and field
counts of Table 1, exact), `l23-cell-counts` (998 NH and 1147 EN ROIs against
the paper's 998 and 1257), `fig3c-l4-enrichment-more-cw-tuned` (EN 97.1%
against NH 75.0% at 0-75 um, p = 0.0003) and `fig4a-l23-ranked-rf-sharper`.
Several outcomes rest on one reading:
`fig2a-l23-point-representation-stronger`, `fig4b-l23-cw-and-best-sw-stronger`
and `fig4d-l23-cw-stronger` hold only with the stored responsiveness p-values,
`fig4c-spontaneous-activity` only under the claims file's variant without
baseline subtraction (under the main reading the L2/3 effect is reversed), and
`fig7c-population-decoder` only with ensembles pooled as units (per-field means
give p = 0.024 to 0.42), while the fig7d ANOVA treats overlapping ensembles as
independent. Partial are, among others, `fig2a-l23-flanks-suppressed` (three of
five bins significant), the correlation claims of Figures 5 and 6, where every
test holds and the values fall below the paper's (0.035 to 0.078 with the
Methods' test in fig5a), and `fig7b-single-roi-decoder` (NH 0.615, EN 0.634, p =
0.0009, outside the tolerances). Not reproduced are `l4-cell-counts` (NH 362
against 322), `fig2c-l4-point-representation-weaker` (NH 0.991 and EN 0.886 at
0-75 um, p = 0.39), `figs2-1-column-frame`, `figs3-1-l4-nh-tuning`,
`fig3a-l23-enrichment-more-cw-tuned` (EN lower than NH at 0-75 um, 82.7% of 133
against 91.7% of 48, with the NH values far above the paper's 67),
`figs4-1-absolute-dff` (the EN slope higher, not lower),
`fig4ae-l4-weaker-responses` (CW test p = 0.35) and
`figs5-2-neuropil-robustness`. The author's first run had 15 reproduced, 10
partially, 8 not reproduced and 1 blocked. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1 agreed
with every outcome but three and raised the eBW gap, the L4 neuropil rebuild,
the reading of Figure 4C, the outcomes resting on the stored p-values and the
untested comparison in fig5eh; in reply `figs3-1-l4-nh-tuning` and `figs5-1-row-and-arc-boundaries`
moved to partial and fig5eh from reproduced to partial, the L4 rebuild was
redone in the descriptor's order (within 0.012 of the stored dF/F), which
uncovered three L4 fields with shifted blank traces, a counting bug was fixed,
and an exploratory eBW reading was added. Round 2 retracted its own round-1
recommendation for `figs3-1-l4-nh-tuning`, as no reading meets the criterion's
partial clause, held that fig5eh now meets every condition of its criterion,
and found sentences the outputs did not support, among them the run time and
the fig5a gaps; the two changes went to a third round, which agreed with
both, noting that the noise half of fig5eh rests on differences of 0.0004 to
0.002 that cannot be told from zero and failed by 0.0002 in round 1. The fix of
the shifted blank traces changed the random stream, so every p-value of the
Methods' test moved slightly after round 1, and fig4b came to rest on the
stored p-values alone (CW p = 0.056). The author's run took about 2 h 20 min
(11:55 to about 14:15 UTC); the notebook ran in about 24 min at first, 9.7 of
them streaming, 831 s after the author-answers run, 23 min after round 1, and
about 19 min after round 3. During development the first full streams crashed
on inconsistent movie names and on the missing E-row whiskers in DNH13b, and
the reader was fixed to handle both.

The paper's test of equivalent best whiskers is in neither the Methods nor the
linked code, and every reading the claims file names puts 89.6-96.5% of NH L2/3
cells near a column centre among those tuned to the column whisker, against
the paper's 67%, while the NH L4 value matches (75.0%, paper 73%); this gap
bears on five claims, though an exploratory reading that also requires each
eBW to be a responsive whisker gives 72.9-75.0% and still no higher tuning in
EN L2/3 (77.4% against 75.0%, p = 0.84), so fig3a does not hinge on it. The stored
permTestResults come from a two-sided permutation test on medians, not the
Methods' one-sided test on means; the two give the same call for 86% of ROIs,
and the L2/3 point representation, the CW and surround responses and the CW
response of Figure 4D are significant only with the stored p-values. The
cell-attached recordings of Figure 1F (10 L2/3 cells in 5 C57BL/6 mice) are not
deposited. processed_data.mat holds more ROIs than reduced_data.mat in 21 of 36
fields (1044 against 998 NH L2/3, 1276 against 1147 EN L2/3, 464 against 362 NH
L4, 782 against 615 EN L4) with no list of the excluded ROIs or the reason, and
the paper's 1257, 322 and 586 match neither count. No barrel areas or radii are
stored, and ROI_pos_barrel_norm divides each position by a radius along the
ROI's direction that varies by a median 37% within a barrel, so the barrel-size
claim rests on a proxy. The stored dF/F is reproduced by a 5-frame moving
median and F0 at the 5th percentile, as the pipeline code does, not by the
Methods' 4 frames and 20th percentile, and the stored L4 dF/F only by filtering
before subtracting 0.3 of the neuropil, as the descriptor says and the Methods
do not. In three L4 fields (ScENR10c/20180104/f1, ScENR10c/20180110,
ScENR10b/20180105/f2) sponTrace holds 76-frame segments starting 0.5 s after
each blank onset, where every other field holds 106 frames starting 0.5 s
before, and sponTrace keeps fewer blank trials than Stimuli marks blank (51 of
61 in DNH15b/20170502/f1) with no stated rule. The code of Stimuli.Label is not
described (label k is whisk{k+1} for k = 0 to 8 and 9 a blank trial). Field
DNH13b/20161208/f2 has no trials for whiskers E1, E2 and E3 and lacks positions
for three barrels, which the descriptor does not mention. Movie names carry a
leading m in Stimuli and not in deltaF in some fields and the other way in
others, and three fields have one dF/F movie with no Stimuli entry. A clock
check with shifted onsets supports a shared clock in 30 of 36 fields and does
not establish it in the other six. Questions are put to the paper's authors: how
the equivalent best whiskers were tested, which responsiveness test gave the
cells analysed, and whether the spontaneous activity of Figure 4C is the
median dF/F on blank trials with or without the baseline subtracted; two
questions on the claims file, on the reading of Figure 4C and on the sign
comparison in fig5eh, are in `questions/crcns-ssc-10.yaml`.

The author's points on the protocol: `docs/archives.md` describes zip files
read by range requests, while this data set is one 4.7 GB tar.gz that every
run streams in full; a single tar.gz offers no cheap subset for development,
so reduced arrays were cached in `$TMPDIR`; the ten-minute target cannot be met
when streaming alone takes ten; the protocol does not say whether a variant
named in the claims file counts as a reading for "reproduced under any
reading", and the author counted it as one; it does not say what to do when a
criterion has no partial clause or the result misses its own partial clause;
it does not place the data set's own sample code in the order of sources; the
clock check by decoding shifted labels does not fit trial-aligned imaging, so a
whisker-minus-blank contrast with shifted onsets was used; it does not say what
to record as `measured` when no reading matches; and for unversioned data the
data set was pinned by its MD5.
