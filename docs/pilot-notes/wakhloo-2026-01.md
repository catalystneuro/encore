# wakhloo-2026, Wakhloo et al. 2026

Twelve claims reproduced, three partially, none not reproduced and seven
blocked, with five more blocked claims on data in other archives left out of
the count; no outcome rests on an assumption. Both verification rounds agreed
with all 27 outcomes; in round 1 the verifier gave `data_missing` for the two
pose-network and three macaque claims, kept as `not_runnable` and `other`
because the claims file marks their data as elsewhere, and in round 2 it
accepted that. The paper, Wakhloo, Slatton and Chung in Nature Neuroscience
("Neural population geometry and optimal coding of tasks with shared latent
structure"), derives the error of a Hebbian linear readout over many tasks from
four geometric terms of population activity (neural-latent correlation,
signal-signal factorization, signal-noise factorization and dimension), tests
the theory in multilayer perceptrons, a DeepLabCut pose network and macaque V4
and IT, derives optimal codes, and applies the measures to PFC and CA1 of rats
learning a continuous alternation task over eight sessions. The claims were
written from the version of record as publisher HTML, without the
Supplementary Information and without figures, with the open method details
taken from the paper's code at commit 9674a6c; the claims check made two small
fixes, for 27 claims. Reproduced are the Fig. 7 learning results:
`fig7d-behavioral-error-learning` (error 0.668 at session 1, 0.157 at session 4
and 0.180 at session 8), `fig7e-readout-error-learning`,
`figs12c-behavior-readout-r2` (R2 0.493 in CA1, 0.508 in PFC),
`fig7f-theory-vs-empirical` (r = 0.983 in PFC and 0.948 in CA1),
`fig7g-total-dimension-drops-early`, `fig7h-task-dimension-increases` under
reading (a), `fig7hk-measures-increase-early` (PFC 4 of 4 measures, CA1 3 of
4), `fig7-late-reversal`, the three quadratic mixed-model claims and the PFC
and CA1 part of `svc-hebbian-correlation` (r2 0.926 and 0.832), with the SVC
run on 4 of the 500 subsets per session as a recorded deviation. Partial are
`mixed-linear-ssf-task-dim` (CA1 SSF P = 0.00106 raw against the 1e-3 bound,
0.00065 with the code's 19 CA1 units), `late-trends-match-optimal` (PFC only;
the CA1 task-relevant dimension falls after session 4, -0.126) and
`glm-cross-validated-d2` (3 of 4 values match; the PFC spread across rats is
0.0599 or 0.0640 against 0.022). Blocked are the five theory and two MLP
claims, which no recorded data test, the two pose-network claims, which need a
DeepLabCut network trained in a separate Python 3.8 environment, and the three
macaque claims, whose Brain-Score data are public but were not attempted in the
run's time. The first run gave `fig7f-theory-vs-empirical` as not reproduced,
as the mean absolute difference was 11.6% and 10.7% of the mean empirical error
against a 10% bound; the author asked whether that bound misreads the legend's
"small bias for low error values", the paper's own results file failing it too
(11.55% in PFC), and the answer run dropped the bound and asked for r of at
least 0.9, so the author-answers run made the claim reproduced. Round 1 marked
this as a criterion changed after outcomes were visible, defensible but for
the next round to know; it also held that the PFC D2 spread was not
diagnosed, that the best-score selection differed from the code's for nan
scores, that the CA1 24-unit row took the task dimension on 19-unit subsets and
that the paper's `rat_stats.csv` was never shown; in reply the paper's own GLM
fits were read and matched to this attempt's (session D2 differing by less than 3e-09),
`np.argmax` replaced the nan-safe selection, 24-unit task dimensions and the
paper's mixed-model table were printed. Round 2 found a CA1 percentage compared
with the paper's at a different unit count, an unsupported README run time and
a D2 difference not printed anywhere, and noted that the point on time-correlated
train and test bins, which make the empirical errors optimistic as in the
paper's method, was missing from the record; all were corrected. It also held
that the claims file may misread the Methods in taking the CA1 task-relevant
dimension on 19 units, and with 24-unit sets `late-trends-match-optimal` would
pass the sign test (slope +0.0130, P = 0.86); this went to
`questions/wakhloo-2026.yaml` for a reader and the outcome was kept. The
notebook ran in 1958 s from a clean environment, with peak memory 0.59 GB,
1404 s after the answer, 32 min after round 1 (0.84 GB) and 32.4 min after
round 2, where the verifier's run printed 17.0 min. About an hour was lost when
a grep over the paper's one-line text hung until it timed out at 60 min, and on
the first full run the clock-check cell failed on a string bug, fixed before the
clean run.

The attempt pins version 0.240511.0307, the version the paper cites and the
latest; all three published versions have the same 9 assets, NWB files for 8
rats of about 323 GB with spikes, LFP, position and trials, and all 8 rats have
their 8 sessions. The per-session measures agree with the paper's own results
files to a median of 0.1% to 0.7%, the behavioural errors are identical, and
position decoded from CA1 spikes beats the 10 s and 60 s shifts in 64 of 64
sessions. The Methods use 19 PFC and 24 CA1 units per subset, while the paper's
code and its results files use 19 in both areas, with the 24 commented out; the
fewest units kept in a session are 19 (PFC) and 24 (CA1), so either is
possible, and the choice moves the CA1 SSF slope across the 1e-3 bound (P =
0.00106 with 24, 0.00065 with 19). The Methods give a standard deviation across
rats of the session-averaged population D2 of 0.022 in PFC, which the paper's
code does not compute; the paper's own GLM fits give 0.0599 (ddof 0) or 0.0640
(ddof 1), with per-rat PFC means from 0.161 to 0.336, and this attempt's fits
give the same, while the s.e.m. over rats is 0.0226 in PFC but 0.0380 in CA1,
so the question of how the 0.022 was computed goes to the authors. Rat ZT2 is
split over two files that both carry session_id "01" and the same subject, with
different units (233 and 240), and nothing in the files or the dandiset says
that they are two parts of one day or their order; the paper's code supplies
it, and their time ranges (206 to 14664 s and 14760 to 30586 s) are consistent
with that order. Position is sampled at 27.0 frames per second (ER1) and 32.3 to
33.1 in the other files, where the paper states 30 fps; sessions last 13.0 to
20.0 minutes (median 15.85; 36 of the 64 between 15.0 and 16.0), where the
paper states about 20, and JS15's timestamps run from 3605 to 90718 s, about 24
hours, in a dataset described as one day. No spike train or position trace is
repeated across files. The Results give R2 = 0.48 for CA1 behaviour against
readout error and the Fig. 7 legend 0.49, where the code prints 0.477, and the
SVC comparison notebook loads an older results file that is not in the
repository, so the Supplementary Fig. 3 rat panels cannot be traced to the
published results files.

The author's points on the protocol: blocked theory and simulation claims fit no
`blocked_by` value, so `other` was used; nothing says which reason to give for
claims on data elsewhere left untested by choice with time left, as the macaque
claims were, so `other` was used and not `too_large`; the paper's results files
used as a comparison and not as a link claim were listed under `inputs` as
comparison only; conclusion markdown filled in after the clean run was copied
into the executed copy, with the code cells identical; and a costly method was
cut short, the SVC run on 4 subsets per session as a deviation and the GLM basis
grid search not repeated, the basis the code chose being used as the claims file
does.
