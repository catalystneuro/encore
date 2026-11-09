# 001065, Dembrow et al. 2024

Nineteen claims reproduced on the dataset (one on an assumption), six
partially (four on an assumption), six not reproduced (one on an assumption)
and none blocked; all but the two cohort counts rest on the per-cell labels of
the paper's code. Of the 10 claims on data elsewhere, two reproduced, one
partially reproduced on an assumption and seven blocked, and the link claim
`link-cells` reproduced. The first verification round agreed with 41 of the 42
outcomes as they stood and the second with all 42, and nothing was proposed
after the second, so there was no third round. It pins version 0.241028.1559,
the only published version; the paper cites none. The paper, Dembrow, Sawchuk
et al., "Areal specializations in the morpho-electric and transcriptomic
properties of primate layer 5 extratelencephalic projection neurons" in Cell
Reports, compares L5 ET neurons of macaque motor (MCx) and temporal cortex
(TCx) by snRNA-seq, Patch-seq, dendritic reconstructions and whole-cell current
clamp in acute and cultured slices, and the dataset holds the current clamp
recordings, 294 NWB files, one per cell, from 57 subjects. The claims were
written from the author manuscript (PMC11488157) with its supplement, without
Tables S1 to S5; the paper's code (Zenodo 13749343) lacks the feature
extraction, the classifier helpers and the R code of Figure 7, so every feature
was computed from the traces, agreeing with the code's table at a median
Spearman of 0.957 over 39 features. The six Patch-seq and snRNA-seq claims are
blocked as other, their data being in SRA PRJNA1088539 and NeMO and not
processed within the run's five hours, and `fig5b-dendrite-depth` as other, the
deposited RawFeatureWide.csv holding no per-layer length; the other morphology
claims were run on that table of 19 reconstructions. Among the physiology
claims, L5 ET neurons have a higher resonant frequency, lower input resistance
and faster spikes than other cells (BH p = 7.6e-33, 4.7e-25 and 3e-30 for min
dV/dt), and `species-no-effect` and `tcx-et-types-no-difference` reproduce.
`fig3a-cs-with-l5et` is not reproduced (42 of 52 CS neurons with an L5 ET
nearest neighbour, 35 to 45 over ten seeds, never 52), nor are
`fig4a-top-subthreshold`, `fig4-interaction-small` and
`figs6b-mcx-higher-rheobase` (BH p 0.16 against 0.0496), all three failing on
the code's table values for the same cells as well, nor `fig6j-spike-width-ratio`
(TCx 1.55 where the paper needs above 2) and `fig7k-oscillation-power-vm` (MCx r
= -0.002). `fig3e-classifier-accuracy` and `fig5e-morph-classifier` are partial,
the 50% score below its bound (78.3 and 80.3%), the three partial oscillation
claims rest on a pipeline rebuilt from the Methods, the spline maximum lying at
the 3 Hz band edge in 52% of sweeps, `figs7-cv-isi-higher-mcx` rests on an
assumed area by bin interaction (additive model p = 0.18 with bins of 25), and
`figs7g-modal-rates-long-isis` rests on the 200-spike limit and 1 Hz bins. The author's first run gave 21 reproduced, 7
partially, 7 not reproduced and 7 blocked. The author asked a reader nothing,
so the answer and author-answers runs changed nothing. Round 1 disagreed only
with `fig5c-basal-apical-features`, whose criterion rule is the four corrected
tests, and found that the four-way species ANOVA was rank deficient, that
features held outliers (MaxRn up to 2575 MOhm, SSRn as low as -460.7 MOhm),
that the oscillation claims skipped the smoothing spline and that fig6j used one
width definition; in reply a sweep check and a chirp check were added, type II
tests were computed from nested least-squares fits, the spline was fitted and
variants on the code's table values and with two other widths were run, so
`species-no-effect` moved from not reproduced to reproduced, fig5c from partial
to reproduced and fig3e from reproduced to partial. Round 2 asked that
`figs7-cv-isi-higher-mcx` be marked assumed, done, and found sentences the
outputs did not support (the fig3a count of 38 where 42 was printed, the
statsmodels feature counts, the median Spearman of 0.952 in every deviation, the
rheobase wording, an unexplained "wash" hit and the summary's oscillation
bullet) and two claims missing from the README, all corrected. The author's run
took about 1 h 50 min (04:29 to 06:17 UTC), the first metadata survey alone 25
min, with nothing failing; the notebook ran in 8.1 min at first, 668 s after
the author-answers run, 872 s after round 1 and 498 s at the end. Untracked
dotfiles appeared in the working tree during the author's run, and
`tools/build_site.py` was found modified and left untouched.

The files carry no cortical area, brain region, slice preparation,
transcriptomic or predicted subclass, retrograde label or drug condition, and
session_description is a placeholder, so these come only from the per-cell
tables of the paper's code, matched by the electrode cell_id; of the 51 L5 ET
cells the table lists with synaptic blockers, only QN23.26.013.4A.05.01 records
when they were applied ("started washon of synaptic block" at sweep 91). 47 of
the 341 cells of the code's L5 physiology table (35 of them recorded by one
user) are not in the dandiset, where the paper reports 333 cells, 33 of them
from earlier studies. Files hold several runs of each protocol (repeats, series
stopped early, a 50 pA and a 200 pA series, runs before and after drug
application) and nothing marks which sweeps the paper used; for 61 of the 68
cells of the 4 nA analysis the steps differ from those of the code's pickles.
In 10 files the first run of 1 s hyperpolarizing steps holds 13 unmarked sweeps
that do not hyperpolarize the cell, start above -40 mV or reach -20 mV, which
gave negative steady-state input resistances for 3 cells. File sub-Q19-26-009
names subject Q19.26.009 where the table gives donor Q19.26.012, the two files
of subject Q19.01.001 give Macaca mulatta where the table gives M. nemestrina
(the M. mulatta count falls from 9 to 8, outside tolerance, by the table), one
subject has sex U and Q19.01.001 has age P1Y/, and the files hold 57 subjects,
22 male and 34 female, against the paper's 58, 23 and 35. Five files hold 1 s
steps above 4 nA (up to 16 nA), beyond the headstage limit STAR Methods give.
The code's table holds SFA as the inverse of the Methods' ratio, the Figure 6D
and 6E legend gives the opposite direction for the fAHP and spike symmetry from
the Results and the code's means, and RawFeatureWide.csv covers 10 MCx and 9 TCx
reconstructions where the paper reports 12 and 11. Questions are put to the
paper's authors: whether the classifier's training splits were stratified and
how regularized (78.3 or 77.5% at 50% held out, against 87.9%); how the
oscillations of Figures 7 and S7 were computed; and which sweeps fed the
features and how the half-width of late spikes in the 4 nA trains was measured
(TCx ratio 1.55 by the Methods, 2.84 by IPFX's width, 2.27 in the pickle).

The author's points on the protocol: no blocked reason fits data elsewhere that
were not attempted for lack of time, and `other` was used; it does not say
whether the paper's own derived tables may stand in for raw data held
elsewhere, and the morphology table was used as a deviation; step 1.4 asks for
`depends_on` entries on the reader's claims, which the author otherwise may not
edit; it is unclear whether partially reproduced is allowed when a criterion
has no partial rule; it does not say when the link claim's criterion is
written, and it was written after a first comparison with the table; and the
suggested clock checks do not fit intracellular sweeps, so spikes were checked
to fall inside the current step (11,925 inside, 11 outside).
