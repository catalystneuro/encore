# ghaderi-2026, Ghaderi et al. 2026

Thirteen claims reproduced, nine partially, three not reproduced and two
blocked, one for methods underspecified and one as not runnable; the two claims
that also need the paper's cluster labels from Zenodo (`with_inputs`) are
counted apart, with `fig5c-cluster-removal` not reproduced and
`fig4b-named-clusters` blocked for methods underspecified, and the link claim
`cluster-label-link`, which the author added and which reproduced, is not
counted. Two outcomes rest on an assumption, `fig3d-wm2-infragranular-delay`
and `fig4-29-clusters`. The first verification round agreed with 27 of the 30
outcomes and disagreed on `fig5d-null-space-decoding`,
`fig8b-lick-coding-direction` and `figs18-later-lick-coding`, all blocked in
the notebook, which it held testable; the second agreed with 28, held fig5c not
reproduced where the record had it blocked and fig5d still testable, and agreed
with figs18 and `fig2-other-trial-types` under the claims file only; a third
round, on fig5c alone, agreed with the change to not reproduced. The
disagreement on fig5d stands. The version is 0.260605.0601, the only published
one. The paper, Ghaderi, Crochet and Petersen in Nature Communications (17,
5982), trains mice in a context-dependent whisker detection task, in which an
auditory cue (Go-tone, Nogo-tone or none) is followed after a 1 s delay by a
whisker deflection that is to be licked for only after the Go-tone, inactivates
six areas optogenetically in three windows of the trial and records 10,294
units in A1, wS1, wS2, wM2 and ALM with Neuropixels in 35 sessions of 14 mice;
it reports that wM2 and ALM inactivation in the delay reduces licking, that
wM2 and ALM carry the context during the delay in single neurons, decoders,
population states and a context coding direction, that removing clusters 11
and 25 lowers that decoding, and that after the whisker stimulus the context is
decoded from 20 ms in wM2 and lick trials separate from no-lick trials in wM2;
the dandiset holds 196 NWB assets (2595.45 GB), with the 35 recording sessions
and the optogenetic sessions. The claims were written from the version of
record as served by Europe PMC (PMC13346651), main text, legends and Methods,
without a PDF or the Supplementary Information, and from the paper's code on
Zenodo (doi:10.5281/zenodo.17973874), also on GitHub at commit 20cf10c7, for 29
claims and the link claim. Reproduced are, among others, `units-recorded`
(10,294 units, exact, but only with the area list from Zenodo),
`fig1c-lick-probabilities` (78.18% on Go-tone Whisker trials), the three
inactivation windows of Figure 2 (Delay window wM2 44.5, ALM 32.1 and wS1 16.0
points), `fig2-wm2-vs-alm-auditory` (33.0 against 7.8),
`fig5b-decoding-time-course`, `fig6b-context-coding-direction`,
`fig6c-temporal-correlation`, `fig7b-early-whisker-response`,
`fig7c-no-whisker-cd-change` and fig8b, tested with the lick times of
Lick_times.mat from Zenodo. Partial are `fig1f-movement-latencies` (tongue
192.4 ms against 231 under reading (a)), `quiet-trials-half` (55.06% of
completed trials not quiet, just outside 45 to 55%),
`fig3b-delay-and-response-psth` (wS2 Hit against No-tone Whisker CR, p 0.11),
`fig3c-delay-modulation-wm2-alm`, fig3d (wM2 infragranular 0.955 Hz, below 1.1
to 1.3), `fig5a-single-neuron-context` and `fig6a-pca-delay-states`, where
values fall below the paper's under the Methods' quiet rule and match it under
the code's, `fig5b-context-decoding-delay` (wM2 62.0 and ALM 58.9% with the
code's decoder, above A1, wS1 and wS2 under both readings) and
`fig8a-wm2-lick-divergence`, where wM2 separates lick from no-lick trials in
the Go-tone context (p 0.0041) but not in the Nogo-tone context (p 0.28). Not
reproduced are fig2-other-trial-types (18 of 72 changes significant, where the
claims file's threshold allows 7, a threshold the paper does not give),
fig4-29-clusters (BIC minimum at k = 40 for the best of 20 initialisations, in
place of the code's 1,000, against 29), fig5c (cluster 25 not significant
under the Methods' grid search, FDR p 0.085, and the code's decoder failing in
4 of 5 runs) and figs18, where wM2 and not ALM has the largest effect by both
of the claims file's effect sizes while the plain difference of the means,
which the Supplementary Fig. 18 legend appears to describe, gives the paper's
order. Blocked are fig4b, as cluster 1 is 30.5% A1, the largest share but not
more than half, `fig7d-context-decoding-after-whisker`, where the code's
decoder puts wM2 at 1.020 s before ALM at 1.025 s and the Methods' grid search,
on a reduced run, puts wM2 after ALM, and fig5d, which needs the MATLAB
toolboxes subspaceID and manopt. The author's first run had 13 reproduced
(with the link claim), 9 partially, 2 not reproduced and 6 blocked, with fig8b
and figs18 blocked as `other`, not tested in the run's time, and fig5c blocked
as its two readings differed. The author asked one question of a reader, on
fig1f, whose criterion took the maximum over 1.0 to 1.2 s, under which no
latency can reach 231 ms; the reader moved the window to 1.0 to 2.0 s, the
Methods' response window, and the author-answers run kept the outcome partial
with whisker and jaw latencies now within tolerance under reading (a). Round 1
held that fig8b and figs18 could be tested with Lick_times.mat, that fig5d
could be tested by reimplementing the subspace optimisation, that the trials
without video were counted as not quiet without a check, that the clustering
was not checked against the code and that the decoders ran too few repetitions;
in reply fig8b moved to reproduced and figs18 to not reproduced, the code lines
of the quiet rule were printed, the clustering followed the code's reg_covar 0,
and more seed sets and the code's quiet rule were run for fig5b and fig5c.
Round 2 found that only seed set 0 of fig5c gave partial, asked for fig3d and
fig4 to be marked assumed, quoted the legends of Supplementary Figs. 3, 17 and
18 and found sentences the outputs did not support, among them the run times;
in reply the change of fig5c was proposed, the two outcomes marked, three
questions put in `questions/ghaderi-2026.yaml` and the sentences corrected.
Round 3 also judged that fig5c's dependency on the blocked fig4b does not touch
the cluster labels it uses, adding that a mechanical reading of the rule would
keep it blocked. A full run of the Methods' grid search for fig7d, with all 10
baseline bins, had not finished after 53 min when the runner's two-hour limit
on one command stopped the entry's run, so it was dropped; an earlier full run
started in the background was killed by the sandbox, at a cost of about 25
minutes, and the first full run failed in the two decoding notebooks on a
session with no analysed units, which was fixed. The author's run took about 2
h 35 min (23:44 to about 02:19 UTC); the three notebooks ran in 5.5, 14.5 and
21.5 min at first, 334, 880 and 1309 s after the author-answers run, 15, 30 and
43 min after round 1, 8, 28 and 41 min after round 2 and 8, 15 and 24 min after
round 3.

The Methods define quiet trials with the median absolute deviation, while the
code calls MATLAB mad() with its default, the mean absolute deviation, which
keeps more trials (60% against 45% of completed trials); with the code's rule
the fractions of Fig. 3c and 5a, the layer values of Fig. 3d and the explained
variances of Fig. 6a come out at the paper's values, so the paper's numbers
appear to come from the code's rule. The dandiset gives each unit a probe
location and an Allen CCF label but not which labels make up the five areas,
and the unit counts match the paper (10,294) only with data_helpers/Area_list.mat
from the Zenodo record; without it 12,066 units sit on the five areas' probes.
The detected lick times and lick mask of Fig. 8b and Supplementary Fig. 18 are
only in Lick_times.mat on Zenodo, as the dandiset's BehavioralEvents hold only
Valve_OpeningTime in all 35 sessions, and the paper's cluster labels are only
in Data_Clustering.mat there. In 12 optogenetic sessions (11 of mouse PG061 and
one of PG021) the genotype is C57BL/6JRj, which carries no ChR2, though light
reduces licking as in the VGAT-ChR2 mice and the other sessions of PG021 give
VGAT_ChR2-eYFP. The units' spike_width is described as "Trough to peak in ms"
but holds seconds (0.0001 to 0.0012), and several trial-table descriptions do
not fit their columns, among them opto_area ("laser light duration", holds an
area name) and context ("Boolean for sound", holds go_tone, nogo_tone or
no_tone). Eleven trials of sub-PG028_ses-20210318T163504 have trial_type 0,
sub-PG076_ses-20220502T140636 has no No-tone trials, 343 trials have no video
frames in their -1 to 2 s window, at least one in every session and most in
sub-PG061_ses-20220212T233813 (243) and sub-PG038_ses-20210316T152753 (29), and
sub-PG038_ses-20210317T180556 has no unit that passes the CCF filter. The Fig. 2
legend gives mean +/- SD and 1,000 bootstrap iterations, while the spreads
match the SEM over sessions (A1 Auditory 4.1 against SD 16.9) and the p-values
need the code's 10,000 iterations; the Methods give 34 recording sessions where
the Results and the dandiset have 35, and 8 mice for ALM inactivation where the
dandiset has 7. Questions are put to the paper's authors: whether "mostly" for
cluster 1 means more than half or the largest share, whether the decoders used
a grid search of SVM parameters, and over which grid, or the code's nu-SVC with
no search, and how "time to 20% max" of Fig. 1f is computed and over which
window, as none of the code computes it.

The author's points on the protocol: the Methods-first rule makes claims
partial even where the code's rule gives the paper's numbers, with no way for
the author to adopt it; the fig3d criterion's partial case does not fit the
result; claims files that block when readings differ conflict with step 1.6,
which allows adopting the best-supported reading; there is no rule for running
fewer repetitions than the paper when the full runs would take about 37 min
and about 30 h; there is no block reason for a claim left untested because the
run's time ran out; the protocol does not say whether the author may add a link
claim to `depends_on`; a label mapping used by every unit claim, such as
Area_list.mat, cannot be marked in claims that are `data: dataset`; and
`docs/archives.md` could note that a HEAD request on DANDI's download redirect
returns 403, so the asset metadata's `contentUrl` was used.
