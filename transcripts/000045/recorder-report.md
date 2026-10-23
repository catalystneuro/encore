I've written `docs/pilot-notes/000045-ibl-2021-01.md` and changed no other file. Nothing is committed. `git status` also lists dotfiles and a `scripts` entry at the repository root as untracked. I didn't create them, and the author's reports say the same of theirs, so I left them alone.

For the heading I used "International Brain Laboratory et al. 2021". The paper's first author is the consortium, as the claims file names it. `tools/readme_row.py` prints the shorter "Ibl et al. 2021", so change the heading if you'd rather match that. The counts below don't include the `lab-link` claim, because `readme_row.py` doesn't count it.

# 000045, International Brain Laboratory et al. 2021

Nineteen claims reproduced, thirteen partially, five not reproduced and one
blocked, all on the dandiset, with the link claim `lab-link`, which the
author added, also reproduced. It pins version 0.211209.1413; the paper cites
no version, and the two published versions, made a minute apart, hold the
same files. The paper, "Standardized and reproducible measurement of
decision-making in mice" in eLife, trains mice in seven laboratories on a
basic and a full visual decision task and reports that learning rates differ
across laboratories but that performance, psychometric parameters and the use
of block priors at proficiency do not, so that a classifier cannot tell the
laboratories apart. The cohort counts, days and trials to proficiency, the
Figure 2 psychometric ranges, the lab tests and classifiers of Figures 3 and
4, the GLM weights and accuracy of Figure 5, win-stay/lose-switch, updating
by contrast and the session end criteria were tested. Only
`early-sessions-predict-slow-learners` is blocked, as
`methods_underspecified`: the paper gives no code or method for its Random
Forest, and the criterion's readings disagree, 3 of 20 accuracy values within
0.53 +- 0.053 and the others from 0.143 to 0.667. The author put seven
questions to a reader; the answers, mostly from the paper's code and the
IBL-pipeline code it imports, changed how basic proficiency (P1) is computed
(each session and the two before it, all trials counted, 1a or 1b at any
date) and let the classifiers run with 5 mice per lab, the lowest lab count,
against the code's 8, which moved `fig2h-proportion-learned-40-days`,
`fig3cde-no-lab-difference-medians`, `fig3f-classifier-chance-basic`,
`fig3f-positive-control` and `fig4j-classifier-chance-full` from blocked to
reproduced and `fig3c-easy-errors-basic` from reproduced to partially
reproduced. Round 1 gave its own outcome for each claim without the
conclusions and summary and agreed with 33 of 39; the author took its
outcomes for `fig2g-days-differ-across-labs`, `fig3s2a-trial-duration` and
`fig3s4-looser-criterion` (from not reproduced to partially reproduced) and
for `fig5s2-glm-accuracy` (from blocked to reproduced, dropping the
notebook's own rule that readings of an open detail must agree), moved
`fig3s3-other-classifiers` from blocked as `not_runnable` to reproduced, where
round 1 gave partially reproduced, by running the Random Forest in 4
processes on the first 50 of the criterion's 2000 subsamples (2.5th
percentile 0.035, bootstrap 95% interval 0.029 to 0.057, against a shuffled
mean of 0.100), and kept `fig5dg-history-weights-higher-full` as reproduced
where round 1 gave partially reproduced. Round 2 agreed with all 39, so there
was no third round; it found statements the outputs did not support, among
them a run of 100 Random Forest subsamples that no output printed, wheel
timestamps called not monotonic and a loading time of about six minutes
against 3.4 printed, and these were corrected. Some outcomes rest on weak
ground: `fig3s2a-trial-duration` has a median of 420.45 ms, just outside 468
+- 46.8; `fig4i-bias-shifts-with-block` is partial because the paper's p <
1e-16 cannot be reached by a Wilcoxon test with 60 mice (smallest p
1.6e-11); and `fig5dg-history-weights-higher-full` holds on the code's
sessions while its unrewarded difference is not significant on the sessions
of reading (b) (p = 0.10 to 0.39). Streaming the 6,615 files with h5py in
threads took 108 minutes, and processes brought it to about 5 minutes; the
entry ran in 18.3 minutes at first and 1607 s in the last run, beyond the
protocol's aim of ten.

The dandiset holds only part of the paper's data: 178 mice and 6,615
sessions from 2019-06-11 to 2020-03-23, while the paper's mice began training
in January 2019 (206 mice, 10,903 sessions), so 41 mice of the project begin
mid-training in the dandiset, only 136 have their whole training in it, and
83 reach basic and 60 full task proficiency against 140 and 98. The training
status of each session, on which every analysis of the paper selects
sessions, is not in the files and had to be recomputed from the trials, which
leaves open details of the criteria, and the metadata do not say which of the
178 mice are the paper's; one mouse (SWC_029) belongs to another project by
its subject record. probabilityLeft is described as the probability of a left
stimulus for the current block, but in every basic-task session it varies
from trial to trial between 0 and 1 (24% of basic-task trials are not 0.5),
with the stimulus side following it. session_start_time is stated in UTC
(+00:00) but holds local clock times, as all seven labs, from London to
Berkeley, have median start hours between 11.0 and 14.4 h, so the start times
cannot confirm the time zones `fig3f-positive-control` takes from the code.
Other findings: in 807 files the wheel position data and its timestamps
differ in length (for example 181,623 samples against 340,799 timestamps), 16
files have no wheel series, and in one session checked (ibl_witten_07) the
wheel moves the opposite way to the choice on every trial; 257,021 trials
(6%) have no stimulus onset time, 185 sessions have none, and 1,541 trials in
220 sessions have a response time before the stimulus onset (down to -5,638
s), though no proficiency window fails for the missing onsets alone; one
recording is deposited twice, under two mice (CSHL_013 and CSHL_015,
2019-07-15); one session (ZM_1367, 2019-06-11) uses contrasts of 4% and 8%,
which the paper does not describe; and the Methods give the 1a/1b
performance criterion on easy trials and the lapse criterion as a maximum of
0.2 for the sum of the lapses, while Appendix 1, table 1d gives performance on
100% contrast and a bound on each lapse rate, which with performance on 100%
contrast only gives 84 mice at P1 against 83.

The author's points on the protocol: it does not say what to do when the
claims file's own readings disagree on a claim of absence; it has no rule for
partial outcomes when only some expected values match; `other` was used for
too few units under the claim's own rule; the clock check had no streams to
check, as the claims use only the trial table, so the wheel was checked
against it; a criterion that cannot be met, p < 1e-16 with 60 mice, was
applied as written; the schema forbids `inferred` on a link claim, so the
note went into its criterion; and the aim of under ten minutes was not met.
