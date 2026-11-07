# crcns-pfc-6, Peyrache et al. 2009

Four claims reproduced, six partially (two on an assumption), five not
reproduced and fourteen blocked, all fourteen for missing data. The first
verification round agreed with 26 of the 29 outcomes as they stood and the
second with all 29; nothing was proposed after the second, so there was no
third round. CRCNS does not version data sets, so the version is recorded as
unversioned with the data set's DOI (10.6080/K0KH0KH5), and the archive is
pinned by its MD5, which matches the bucket's ETag; it is a single tar.gz,
streamed in memory once per run. The paper, Peyrache, Khamassi, Benchenane,
Wiener and Battaglia in Nature Neuroscience, records mPFC cells with tetrodes
in the right prelimbic cortex of four rats over 63 sessions, each a rest epoch,
a Y-maze rule-shift task and a second rest epoch, takes signal components of
the awake cell correlation matrix as templates and finds them reactivated in
the slow-wave sleep (SWS) after the task, and relates the replay to
hippocampal sharp wave/ripple complexes (SPWRs), cortical delta waves,
spindles and rule learning; the data set holds 86 sessions with spike times, a
putative cell type per cell, the trials, the awake and SWS intervals and the
position. The claims
were written from the PyMuPDF text of the version of record and its
supplement, without rendering any figure; the paper links no code. The check
changed eight claims, among them the non-SWS test of `supp5-sws-only` and the
tolerance of `fig2f-tail-contribution`, and left open the order of the three r
values in Figure 6d and the bins, lag ranges and DOWN-state thresholds of three
criteria. The session, rule, signal component, reactivation, skewness, shuffle,
DOWN to UP and behaviour claims could be tested; the SPWR, delta-wave, spindle,
same-tetrode and learning-template claims of Figures 5 to 7 could not.
Reproduced are `fig2b-post-greater-than-pre` (paired t p = 0.0015, 0.00014 and
0.00023), `supp6-pre-post-sws-alike` (its SWS duration and firing-rate parts
only), `supp10-no-coactivation` and `supp12-behavior-unchanged` (paired t p =
0.16, n = 10). Partial are `fig1b-signal-components` (285 signal and 730
nonsignal components against 291 to 355 and 730 to 892),
`supp5-sws-only` (state p = 0.0019 and epoch p = 4.9e-08, but post exceeds pre
outside SWS, p = 0.042), `fig2b-pre-weaker` (the slope difference at p of
2.4e-08 to 3.3e-13, not below 1e-20), `fig2f-tail-contribution` (52.2% for Phi
above 1.8, one and two of three groups in 36 to 55%), `supp11-shuffle-control`
(post higher for Phi above 1.8, paired t p = 0.031) and `fig6b-down-up` (pre
lower in the window, 0.063 against 0.107, higher at its largest value, 0.145
against 0.132, per-component p = 0.15). Not reproduced are
`sessions-and-cells` (56 sessions and 1499 cells against 63 and 1692),
`rules-learned` (right arm 3 rats, lit 4, left 3 and dark 1, against 4, 4, 2
and 1), `learning-sessions` (no reading gives 9 to 11 sessions),
`fig2b-encoding-correlation` (r squared 0.384 against 0.549 to 0.671) and
`fig2e-skewness`. `supp5-sws-only` rests on rest-epoch bounds taken from the
data set's epoch times, and `fig6b-down-up` on the rule that pre is lower only
if both comparisons agree or the per-component difference is significant; the
window comparison alone would make it reproduced. The author's first run had 5
reproduced, 5 partially, 5 not reproduced and 14 blocked, with
`fig6b-down-up` reproduced. The author asked no questions of a reader, so the
answer and author-answers runs changed nothing. Round 1 disagreed on
`supp5-sws-only` (not reproduced, its state effect at p = 0.0138), on
`supp6-pre-post-sws-alike` (partially reproduced, the LFP measures blocked)
and on `fig6b-down-up`, and found that reading (b) of `learning-sessions`
returned nothing when the block of correct trials ran to the end of a session;
in reply the bug was fixed with a test (22 and 14 sessions), the ANOVA became a
repeated-measures one, `fig6b-down-up` became partially reproduced, the other
two outcomes stayed with the disagreements recorded, and a 3.5 min SWS variant
of `fig1b-signal-components` was added (315 and 820, group sizes 11, 39 and
265, all within tolerance). Round 2 withdrew both disagreements and found
that the stated assumption of `fig6b-down-up` would give reproduced, a summary
range of 16 to 34 sessions where the outputs give 14 to 34, and an unmentioned
fourth significant bin; in reply the text was corrected and the fourth bin
printed, a dip at 0 s (-0.059). The author's run took about 30 minutes (02:52
to 03:21 UTC) and nothing failed. The notebook ran in 96 to 102 s at first,
110 s after the author-answers run, 92 s after round 1 and about 2 minutes at
the end. Deleting an empty `.claude` folder in the entry was refused for lack
of approval, and the untracked files in the repository root were left alone.

The data set holds no LFP, no SPWR, delta-wave or spindle times and no tetrode
of each cell, so the paper's analyses of Figures 5 to 7 and its same-tetrode
control cannot be repeated, 14 of 29 claims. It holds 14 sessions of rat 15,
where the paper reports 16 analysed; with the paper's inclusion rule (at least
ten cells and 4 min of SWS in each rest epoch) 56 sessions and 1499 cells
remain, against 63 and 1,692, and rats 18 and 20 match the paper's counts, rat
19 has one fewer and rat 15 six fewer. With a 3.5 min SWS threshold the totals
match (63 sessions, 1682 cells) but the per-rat counts do not (11, 12, 11, 29).
The data set holds 86 sessions, including 23 of rat 20 that fail the 4 min SWS
rule, and does not say which sessions the paper analysed. Two of the ten
learning sessions the description lists (201227 and 201229) have less than 4
min of SWS in one rest epoch by the data set's SWS intervals (2.2 min pre, and
3.3 min post), though the paper's Figure 7 uses ten learning sessions, and the
paper's learning definition does not recover the listed trial in 181020,
201222 or 201227. The bounds of the pre and post rest epochs are not given, nor
the position units and the maze's coordinates. In the recorded trials rat 18
never reaches the rule-change criterion on the right-arm rule (22 trials, a
longest correct run of 9), yet its rule was changed, and three rats, not two,
reach criterion on the left-arm rule. Sessions without SWS in a rest epoch
store a single [0, 0] interval (four sessions) or an empty file (150704
SwsPRE). Cell types are all 0 (unknown) in 200107 and all 1 (interneuron) in
200209, and mostly unknown in 200131, 200224 and 200301. In five sessions
spikes continue 12 to 176 min after the position record ends, and in 200213 the
position record ends before the awake interval does. The spike clock check
does not establish the clock in 18 sessions. Questions are put to the paper's
authors: whether the match epoch is z-transformed over the whole rest epoch or
its SWS bins; how the rest epochs were bounded and DOWN states detected for
Figure 6b; and which tests lie behind Figure 2b, Figure 2e and Supplementary
Figure 11D, and whether the 0.61 of Figure 2b is an r or an r squared.

The author's points on the protocol: `archives.md` describes opening a zip in
place, while this data set is a tar.gz that cannot be read by range, so it was
streamed once per run; expected values that are only sample sizes, such as the
fig2b group counts, conflict with a criterion that defines reproduced without
them, so the criterion was followed and the mismatch recorded as a deviation;
there is no rule for a claim of which only some parts can be tested, so the
outcome rests on the testable part; `measured` is defined only for when
readings match, so when none did the paper-supported or first-listed reading
was recorded; `depends_on` covers only blocked dependencies, so fig1b and
supp12 used the paper's stated rule and the description's learning list; and
the exact mean over all permutations replaced 1000 shuffles per bin in supp11,
recorded as a deviation.
