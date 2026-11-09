# 001131, Mountoufaris et al. 2024

Three claims reproduced (all three on an assumption), one partially (on an
assumption), ten not reproduced and 21 blocked, 20 for missing data and one as
`metadata_insufficient`. With outside data, counted apart: one partially
reproduced, on an assumption. The first verification round agreed with 33 of
the 36 outcomes as they stood and the second with all 36, and the second
revision proposed one change, so a third round reviewed it and agreed. It pins
version 0.260601.1203; the paper cites no version, and this one contains the
earlier 0.240826.1647, whose two files are the same recordings as mice 510 and
500 under other subject ids. The paper, Mountoufaris, Nair, Yang, Kim,
Vinograd, Kim, Linderman and Anderson, "A line attractor encoding a persistent
internal state requires neuropeptide signaling" in Cell, edits the oxytocin and
vasopressin receptor genes Oxtr and Avpr1a with gRNAs in Esr1+ VMHvl neurons of
male mice and images these neurons with a miniscope ("CRISPRoscopy") while the
mice meet male and female intruders, relating the edit to aggression, unit
activity, a line attractor in a recurrent switching linear dynamical system
(rSLDS) and the autocorrelation half-width (ACHW), with behaviour cohorts, fiber
photometry, slice imaging and an outside single-cell RNA-seq atlas besides; the
dataset holds z-scored miniscope traces and male-intruder behaviour annotations
of 10 mice. The claims were written from the accepted author manuscript
(PMC11490375) with the supplement's figure images, and from the paper's linked
code (DJALab/VMHvl_MPOA_dynamics at commit ed83c41), which holds no code for the
paper's data and points to the rSLDS notebook of ssm (commit eb6c8aa), whose
settings the claims file adopts; ssm and the Kim et al. 2019 atlas are listed
under `inputs`. `figs4a-unilateral-no-behavior-deficit` reproduces on the
attack-triggered reading of attack probability (smallest p 0.114),
`fig4ef-male-activity-slightly-lower` on the pooled reading of "nested" (0.53
against 0.95 sigma, Mann-Whitney p = 0.002) and `figs4e-active-units-unchanged`
on a baseline of all frames before the first annotated behaviour. Partial are
`fig5bd-behavior-selective-units-reduced`, every direction holding and 3 of 7
values inside tolerance, and, with the atlas, `fig1e-oxtr-avpr1a-coexpression`,
Oxtr at 73.9% inside 78 +/- 7.8% and Avpr1a among those cells at 49.4% below 61
+/- 6.1%, on all 850 cells of the eight Esr1 clusters at any expression above 0
counts per million (CPM). Not reproduced are `methods-unit-counts` (587 units in
4 control mice and 554 in 6 experimental, against 585 in 5 and 546 in 7),
`figs5c-peth-activity`, `figs5e-behavior-decoding-intact` (control decoding
better, p = 0.036), `fig7c-achw-all-units` (a reduction of 15 to 31% under
every estimator against 50.9 +/- 5.1%) and the six rSLDS claims, whose fits
explain 59.4% of the variance against 85 +/- 8.5% and give control time
constants tau1 of 409 to 964 s against 90 to 132 s. Blocked are the 20 claims
on female intruders, the behaviour cohorts, photometry and slices, for missing
data, and `fig6e-integration-dimension-persistence`, since the intruder's
removal is not marked. The author's first run gave 3 reproduced, 1 partially,
9 not reproduced and 23 blocked, with fig1e blocked as other, not attempted for
lack of time and a GEO search having found no accession for the atlas. The
author asked a reader nothing at first, so the answer and author-answers runs
changed nothing. Round 1 disagreed with three outcomes, putting figs4a and
figs4e at partially reproduced and figs5c, blocked by the author, at not
reproduced, and found that the ACHW estimator is biased over 1 to 2 min, that
the frame-wise decoder folds put frames of one bout in training and test, that
the rSLDS fit used ssm's default alpha = 0.5 where the cited notebook uses 0.0,
that a complex eigenvalue pair gave dimensions 1 and 2 the same weights, that
flow fields were drawn for 2 mice only and that fig1e was untested; in reply
figs5c moved to not reproduced, figs4a was kept with four declared readings of
attack probability (a bout rate differing at p = 0.036, experimental mice
attacking more), figs4e was kept on a changed assumption (the baseline in place
of a reading of "nested"), two more ACHW estimators with a synthetic check,
decoders on 31 units per mouse with shuffles, a refit with alpha = 0.0, flow
fields of all ten mice, a seed-0 notebook with sigma-normalized fits and a
one-fold held-out score, and the male parts of `fig4g-male-selective-reduced`
and `fig5e-cp-tuning-shift` were added, and a reader was asked whether the
paper's "~85% of variance" is the emissions R2. Round 2 agreed with all 36,
found sentences the outputs did not support (|Spearman r| "at most 0.47" for
any dimension where any reaches 0.70, "3 to 5 mice per group", a fig4g range
stated too broadly, "more than nearly twice", and the README's reason for
fig1e), all corrected, and raised two star marks in Figure S4A; the second
revision rendered the figure, found them on % time attacking and the interval
between attacks, both with experimental mice more aggressive, and asked a
reader, ran the check without mice 497, 510 and 500 for figs4e, fig5bd, figs5e
and fig7c (figs4e then finds control higher pooled at 1 min, p = 0.012), and
found the atlas on Mendeley Data (doi:10.17632/ypx3sw2f7c.1) through the Kim et
al. 2019 article's data links in Europe PMC, proposing partially reproduced for
fig1e. Round 3 agreed, noting that at 5 CPM or more both values fall outside
and that at CPM above 0 all eight clusters hold co-expressing cells where the
paper gives 5 of 8, and the third revision asked a reader about the claim's
calling the atlas one of VMHvl, where it covers the whole VMH. The four rSLDS
seeds took over the 60-minute notebook limit and were split over two notebooks,
and ssm cannot be built from the lock file, so it is installed at the pinned
commit without build isolation. The author's clean run took 52 min, the main
notebook 228 s and the two rSLDS notebooks about 24 min each, after a first
draft of the clock check failed and was replaced; the notebooks ran in 230,
1508 and 1442 s after the author-answers run, and the whole entry in 77 min
after round 1, 72 min after round 2 and 58 min at the end. After the second
revision's run the fig1e conclusion was edited to correct a misstated range. A
change to `tools/build_site.py` and untracked dotfiles in the repository root,
already there, were left untouched.

The dandiset holds the miniscope data of 4 control and 6 experimental mice,
where the paper reports 5 and 7, and the female-intruder part of every imaging
session, the behaviour cohorts of Figures 2 and 3, the fiber photometry and the
slice imaging are absent, although the paper's data statement says the source
data will be deposited at DANDI; 20 of the 36 claims cannot be tested for these
reasons. The files mark neither the 5-min pre-intruder baseline nor the
intruder's entry and removal, though the paper's activity measures are in sigma
relative to that baseline, so the baseline was assumed from the first annotated
behaviour and the post-intruder claim could not be tested; only z-scored traces
are given, not dF/F. Clock alignment could not be established for mice 497, 510
and 500, and leaving them out makes the pooled figs4e test find control higher
at 1 min (p = 0.012) and lowers the fig7c reduction to 5 to 18%. The unit
counts differ from the STAR Methods in the other direction from the mouse
counts: 587 control units in 4 mice and 554 experimental units in 6, against
585 in 5 and 546 in 7. The files of mice 510 and 500 describe their trace as
"DF/F" with "GCaMP6m", while the values are z-scores (every unit of mouse 510
has mean 0 and SD 1) and the paper used GCaMP8s; these two files hold only
sniffing annotations, with no attack or mounting, and mouse 510's sniffing
bouts all fall between 179 and 279 s of a 1200-s recording. The trace of mouse
500 is not z-scored over its file (unit SDs 0.65 to 1.05, means up to 0.23 away
from 0), unlike the other nine, so it was z-scored over a longer recording and
then cut. The group of each mouse is given only by the prefix of its subject id
(ctrl, mut) and, in eight files, a keyword, with no genotype or description of
the gRNA, and nine sessions carry the same start date (2023-02-01), apparently
a placeholder. The rSLDS weights deposited for mice 510 and 500 ("latent factor
1") are not recovered by fits with the claims file's settings, with |Spearman
r| at most 0.47 for the first fitted dimension and 0.70 for any. The Results
give n=4 control mice for Figure 4E-F, while the Figure 4 and S4 legends and
the STAR Methods give 5. Neither the paper nor the claims file names the
atlas's archive. Questions are put to the paper's authors: where the baseline
lies in each file and when each intruder entered and left, what the "nested"
Mann-Whitney and KS tests are, which frames, seeds, restarts, folds, horizon and
dynamics matrix the rSLDS analyses used and how complex eigenvalue pairs enter
the line attractor score, how ACHW is computed, how the attack probability of
Figure S4A(vii) is computed and summarized per mouse, whether mouse 511's
sniffing annotation of two bouts of 22 and 40 s is complete, and which atlas
cells and expression threshold Figure 1E used.

The author's points on the protocol: the claims file asks for four rSLDS seeds,
which take over the 60-minute notebook limit, so they were split over two
notebooks; the pinned ssm cannot be installed from the lock file, and it was
installed without build isolation and recorded as a deviation; the protocol
does not say whether conclusions may be written after the clean run, and only
the markdown was copied into the executed copies, with the code cells checked
identical; `measured` takes only numbers, so for fig7b, whose first reading
cannot be computed, the first fully defined combination was recorded; no
`blocked_by` reason fits public outside data not attempted for lack of time,
and `other` was used; for an absence claim the paper's test alone decides, but
here the test ("nested") is ambiguous, and one reading was adopted as an
assumption; and under the claims file's "reproduced under any reading" rule
fig4ef passes on the pooled reading only.
