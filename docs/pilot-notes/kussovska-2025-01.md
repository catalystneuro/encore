# kussovska-2025, Kussovska et al. 2025

Twenty-nine claims reproduced on the dandiset, eight partially, seven not
reproduced and none blocked; `supp4-rodent-validation`, tested on the feature
table shipped with the paper's code (`data: elsewhere`), reproduced and is
counted apart. Seventeen outcomes rest on an assumption, most of them on the
cell types of reading (a) of `acg-fit-yield` (every spike of the unit), among
them `fig4c-encoding-bursts-vs-poisson`, `fig4d-maintenance-bursts-vs-poisson`
and `fig6e-load-modulation-in`. The first verification round agreed with 41 of
the 45 outcomes and disagreed on the three dPCA claims, which the author had
blocked as too large and which it held testable, the block resting on run time
only, and on `fig6cd-celltype-epochs`, which it held not reproduced where the
record had it partial; the author took all four. The second round agreed with
all 45, calling fig4c and fig6e fragile, and the author proposed fig6e as
partially reproduced, so there was a third round, which reviewed that one claim
and agreed. The dandiset is pinned at 0.231213.2047, the version the paper
cites; all published versions hold the same 41 assets, while the code's README
downloads 0.240123.1806. The paper, Kussovska, Kim and Rungratsameetaweemana,
"Neural heterogeneity shapes the temporal structure of human working memory"
(bioRxiv, doi:10.1101/2025.10.31.684900), reanalyses the 902 units recorded in
21 epilepsy patients during a Sternberg task and reports that the persistence of
concept cells emerges only with population pooling and coarse temporal bins,
that encoding and maintenance occupy distinct dPCA subspaces, that population
bursting reorganizes between encoding and maintenance, and that autocorrelogram
(ACG) features split the neurons into putative pyramidal neurons (PY) and
interneurons (IN), whose concept cells differ in load and reaction time
modulation, spiking regularity and decoding during maintenance. The claims were
written from the bioRxiv full-text page, without a PDF and without the Extended
Data figures, on which 9 claims rest only through the main-text sentences that
cite them, and from the paper's code at commit 5144fe8, in which the matched
trial sets exist only as shipped tables and the ACG fit is MATLAB with an empty
spike input; the claims check made six corrections, for 45 claims, all of which
could be tested. Reproduced are the unit counts (AMY 259, dACC 171, HPC 190,
preSMA 250, vmPFC 32, exact), the behaviour claims (88.73%; load 1 against load
3, p = 0.0270 with the code's Bonferroni factor, the paper's P = 0.027),
`fig1e-load-modulated-neurons`, `concept-cells-count` (58 at seed 0, 57 to 60
over ten seeds), the persistence and cross-temporal claims of Fig. 2, the three
dPCA claims (`fig3d-encoding-vs-maintenance-separability`, H = 457.62, only with
the trials as the code selects them, and `fig3h-early-vs-late-maintenance` only
with protect [] for the early half), fig4c, fig4d over each trial's own
maintenance, `ext2-bursts-loads23`, acg-fit-yield (317 against 294),
`fig5c-cell-type-clusters` under reading (b) (100 PY, 198 IN),
`fig5gh-burst-index-cv2`, `fig5kl-concept-cell-types` (11 and 14),
`ext5bd-in-load-dependence`, `fig6kl-cross-temporal-by-type` and
`ext5ij-load2-decoding-by-type`. Partial are `ext1f-maintenance-decoding-load2`
(AMY 26.43%, above the tolerance of 21.2 to 25.9%), `fig2f-bin-width-decoding`,
`fig4-acg-group-differences`, `fig4f-all-cells-epochs` (no increase to the
probe, BH p 0.61 to 0.71), `fig4hj-group-epochs`,
`fig6ab-celltype-bursts-vs-null`, `fig6j-in-bin-width-decoding` and fig6e, where
IN concept cells come out at 3 of 16 = 18.75% (p = 0.042), just below the
tolerance of 19.28 to 23.56%, and meet it under two of four fits that differ at
rounding level. Not reproduced are `fig1f-rt-modulation-not-significant`, whose
values come out exactly only with the code's predictor, `fig2f-bin-width-pairwise`,
fig6cd (no IN probe difference, BH p 0.13 to 1.0), `fig6f-rt-modulation-in-concept`
(IN concept 12.50%, p 0.19 to 0.20), `fig6gh-in-concept-cv2` (p = 0.86 at load
1), `ext5gh-py-decay-preferred` and `fig6i-py-bin-width-decoding`. The author's
first run had 27 reproduced, 9 partially, 6 not reproduced and 3 blocked. The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing; a question on the per-trial thirds of maintenance of the Fig. 6c
legend went to `questions/kussovska-2025.yaml` after round 2. Round 1 held that
the dPCA block rested on run time only and the splits could run in parallel, that the downstream claims
used only the types of reading (a), whose PY count (102) is outside tolerance,
that the code's 2.8 s maintenance window lets the surrogates fill the silent tail
after the probe, that the scipy ACG fit is not stated as a limitation, and that
decoding p values are never compared with the paper's 20% chance; in reply the
estimate was found to come from fits competing for threads and the dPCA claims
ran in a second notebook on 4 processes, every cell-type claim also
ran with the types of reading (b), fig4d moved to each trial's own maintenance
after a burst-free Poisson control, and binomial tests against 20% were added.
Round 2 found that results changed between runs with fixed seeds (317 to 316
well-fit neurons, preSMA 51 to 50), stale numbers in the text, that fig4c rested
on the 1-bin variant, and that the tau decay groups were never compared with the
shipped `Decay` column; in reply the changes were traced to ties at the GLM
threshold and a fit sensitive at the level of rounding, and groups from the
shipped tau decay gave fig4-acg-group-differences its whole pattern, the outcome
kept as that table is an outside input. Round 3 found that the fig6e text and
that of most fit-dependent claims described another run, and they were
corrected. The author's run took about 2 h 55 min; the notebook ran in 19.6 min
at first, 2297 s after the author-answers run, 46 min (with 22 min for the dPCA
notebook) after round 1 and 52 and 23 min after round 2. The first full
development run was killed at 66 min with nothing saved, because of a slow
two-sided binomial test, and a fast SVM wrapper gave wrong predictions when
labels were not coded 0 to k-1, which was fixed before the final run.

The dandiset holds exactly the paper's 902 units with its region counts, and the
code's trial tables link to its trials exactly, but the matched trial sets of
the Methods (96 load-matched and 75 identity-matched trials per participant)
exist only as the code's data/new_trial_info.xlsx and data/new_trial_final.xlsx,
no script builds them and the paper does not say how they were chosen, so the
pseudo-population decoding depends on which trials enter (random draws of six
trials per image give 56.7 to 86.7% at 1000 ms against 76.67% with the code's
table). The paper's GLM code uses subject 1's reaction times as the predictor
for every neuron of every participant, and the Fig. 1f percentages (AMY 5.79%,
preSMA 8.00%, vmPFC 6.25%) come out exactly only with it; with each trial's own
reaction time preSMA, AMY and dACC have significant proportions after
correction. The code's maintenance burst test concatenates trials with a 2.8 s
stride while maintenance lasts 2.53 to 2.84 s, and homogeneous Poisson trains
confined to each trial's maintenance then exceed the null for all neurons in 17
to 20 of 20 participants (BH p 0.0005 to 0.0025), so the maintenance results of
Fig. 4d and Fig. 6a,b against the Poisson null can arise from the window alone.
08_dpca_matrices.py takes encoding trials by new_trial_id and maintenance trials
by trial_id, which in 4 of the 14 sessions with concept cells (subjects 7, 8, 9
and 16) are other trials, and the paper's Fig. 3d statistics are matched most
closely with the code as written; the code's protect setting for the early half
of maintenance reverses Fig. 3g,h in all 100 splits. The code assigns M1 to M3
by thirds of the concatenated train, that is of the trials, where the Methods
give three 1 s windows, and what it reports as CV2 for Fig. 5h is the plain
coefficient of variation (PY 1.673, IN 1.319 match it). The ACG features of the
shipped Cell_metrics.xlsx are recomputed from the spike times to within 1% for
99% of units, but the fitted R2 and time constants differ for part of the units
in a scipy port, which gives 317 well-fit units in place of 294, and changing
the fit's start point by 1 +/- 1e-9 or the ACG by 1 + 1e-12 gives 315 to 317;
in the GLM test 8 of the 902 neurons have |b1| equal to their null threshold, so
rounding moves preSMA between 47 and 51 significant neurons and vmPFC between 6
and 7. The paper states that sixteen participants completed 135 trials and five
108, while the dandiset has fifteen sessions of 135 and six of 108 (subjects 6,
7, 8, 9, 16 and 19). In sub-9's file one trial (row 29) has a maintenance of 0
s, against 2.53 to 2.84 s in every other trial. The first encoding image lasts
1.0, 1.2, 1.5 or 2.5 s depending on the session, which the paper does not state,
and fixation lasts about 0.91 to 1.2 s in most sessions, with single longer
fixations up to 14.07 s, where the paper gives 0.9 to 1.0 s. The clock could not
be checked by contrast in 7 sessions (subjects 1, 3, 6, 10, 17, 19, 20), which
have no image-selective neurons. Questions are put to the paper's authors: which
peak rule detects population bursts, with what surrogate threshold and minimum
spacing (140 ms in the Methods, 70 ms in the Results); what the label-shuffled
null of Fig. 6a,b is; which decay time constants Extended Data Fig. 5g,h
compares; how the temporal extent of a cross-temporal cluster is measured and
whether the binomial test is one- or two-sided; and over which window the
Poisson surrogates of the maintenance burst test are drawn.

The author's points on the protocol: it does not say how to judge a result that
holds in part when a criterion defines only "reproduced"; it does not say what
to record for `measured` when the first listed reading matches for only 2 of 10
seeds, as in concept-cells-count; it does not say whether downstream claims must
run every reading of an upstream claim, such as which spikes feed the ACG; it
has no category for outside inputs used only for comparison, such as the code's
concept-cell list and ACG table; its example entry uses bold labels that its
instructions forbid; and its advice to develop on a subset does not say to run
the full notebook cell by cell with saved progress, which cost a run.
