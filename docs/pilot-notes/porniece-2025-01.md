# 001474, Porniece et al. 2025

Twenty-three claims reproduced (one on an assumption), seven partially (two on
an assumption), five not reproduced and two blocked, one as
`methods_underspecified` and one for missing data. All 37 claims are on the
dandiset. The first verification round gave outcomes for 36 of the 37 claims,
leaving out `fig2km-elevated-early-at-matched-licking`, and agreed with 35 of
them as they stood; the second agreed with all 37, and nothing was proposed
after the second, so there was no third round. It pins version 0.251031.1725,
the only published version; the paper cites none. The paper, Porniece, Baker,
Ausfahl, Zhang and Andermann, "Obesity dysregulates feeding-evoked response
dynamics in hypothalamic satiety neurons" in Scientific Reports, records
GCaMP6s fiber photometry from PVH MC4R neurons in head-fixed MC4R-Cre mice fed
normal chow (NCD) or a 60% fat diet (HFD) and then food restricted, in sessions
of tone-cued trials where a lick within 1 s of the tone delivers about 50 uL of
Ensure, and compares the early-meal and late-meal responses of the two diets in
a cohort of 60-trial sessions (Fig. 1), a new cohort of 90-trial sessions (Fig.
2) and a diet switch (Fig. 3). The claims were written from the version of
record served by Europe PMC (PMC12521569) with the legends of the supplementary
figures, without the figures as images; the code the Methods cite
(github.com/xzhang03/Photometry_analysis, commit b88d3943) is the lab's general
MATLAB photometry toolbox and holds none of the paper's Python analysis. The
claims file gives two Z readings computed from the raw 465 nm trace, Z1 and Z2,
and since the Methods' "a single Z-score per animal" does not say which
recordings are concatenated, each was run over all of a mouse's recordings and
over one diet phase (Z1p, Z2p); the depositors' Z-score (Z0) is shown as a
variant that decides nothing. Reproduced are the dF/F0, Ensure intake,
locomotion and meal-size claims of Figs. 1 and 2, the Fig. 2 lick-rate, weight
and meal-size correlations, `fig2d-delta-z-mice` (NCD 0.61 and HFD 0.20, under
Z2 with D15 only), the sex difference, the diet-switch claims `fig3i`, `fig3k`,
`fig3c`, `supp3c`, `supp3j` and `supp3l`, and, on the assumption that the 13
cohort-2 recordings with a modal trial offset are kept,
`fig2c-delta-z-recordings` (NCD 0.606 and HFD 0.197; without them HFD is 0.20 to
0.23 and the claim would be partial). Partial are `fig1k-early-late-recordings`
and `fig1l-early-late-mice`, whose directions hold while no combination puts all
four means within tolerance, `fig1c-hfd-heavier` (35.2% against 30 +- 3%),
`fig2e-lick-vigor` (decline onsets at trials 57 and 27 against 50 +- 5 and 20 +-
2), `fig3h-early-response-diet-switch` (Tukey p 0.11 to 0.99), and, on
assumptions, `supp3m-weight-gain-response` (recordings with at least 30
triggered trials) and `supp3q-hfd-ncd-weight-loss-meal-length` (the notes' `ad
lib bw` read as weight B of Supp. Fig. 3k). Not reproduced are `fig1k-lme`,
whose HFD coefficient has p 0.09 to 0.35 under every Z1 to Z2p reading while Z0
gives p 1.3e-06 to 4.7e-06, as the paper reports, `supp2h-delta-z-meal-size`,
`supp2lp-fasting-no-effect` (HFD sessions differ after fasting, t-test p 0.037
and LME p 0.005 for the lick rate), `fig3j-delta-z-diet-switch` and
`fig3-hfd-hfd-short-meals` (two of 30 HFD->HFD recordings exceed 60 triggered
trials, where the partial condition allows one). Blocked are
`supp1cd-licking-declines`, whose criterion's readings disagree (subtracting the
pre-tone lick rate gives a decline in both diets, dividing by it gives none),
and `supp2q-hfd-more-training`, as no training session is in the dataset. The
author's first run gave 24 reproduced, 6 partially, 5 not reproduced and 2
blocked, with `supp3q` reproduced on its assumption. The author asked no
questions of a reader, so the reader's run and the author-answers run changed
nothing. Round 1 disagreed with `supp3q`, putting it at partially reproduced
since Z1 finds the mid-meal correlation with meal size (p 0.039 and 0.043) that
the claim says is absent, and found that 58 recordings had their trials placed
by the modal offset with no check, that the fig1k-lme outcome turns on the Z
reading, and that several passes sit at a tolerance edge or rest on one reading;
in reply `supp3q` moved as the verifier gave it, a check of every recording
against the tone-evoked rise of the raw signal and a rerun of the raw-measure
analyses without the 58 were added (only `fig2c` would change), a Z0 against Z2
comparison was added (median per-recording r 0.935 in matched files), and the
MPK191 date was flagged. Round 2 agreed with all 37, asked that `fig2c` be
marked as assumed, which was done, and found sentences the outputs did not
support (the tone check said to place the trials of every modal-offset
recording, where it holds for the 58 as a group and proves nothing for 9 of
them, raw trace lengths of 67 to 106 min where 51.7 to 142.7 min is printed, and
Z0 called close to a per-mouse rescaling of dF/F0), all corrected. The author's
run took about 50 minutes (17:18 to about 18:07 UTC), of which a first metadata
survey with `remfile` took 10 minutes, and nothing failed in the final run; four
bugs found during development were fixed, among them Tukey p-values rounded to 0
with the sign of the differences reversed. The notebook ran in 103 s at first,
79 s of it reading the files, 109 s after the author-answers run, 69 s after
round 1 and 116 s at the end.

In 32 files the deposited Z-score does not match the raw 465 nm trace of the
same file at any offset (median correlation over trials below 0.5), while in the
other 285 it does (median 0.95), and the deposited Z-score is not a linear
transform of the raw trace; with no trial table and no tone time stamp, trial
onsets in the raw trace have to be inferred, so these 32 and 26 files without a
Z-score use the modal offset of the matched files, and 9 of these 58 show no
tone response at either end of the session. The 405 nm control trace, the
training sessions (Supp. Fig. 2q, r) and the home-cage food intake (Fig. 1d) are
not in the dataset. Cohort 2 holds 6 HFD mice (50 90-trial recordings, 47 with
at least 30 triggered trials) where the paper has 7 (54), the missing mouse
being a male by the Supp. Fig. 2k counts; cohort 1 has 38 and 32 qualifying
recordings against 39 and 33, cohort 2 NCD 57 against 59, and the diet-switch
first phase 46, 49 and 30 against 47, 52 and 35 for NCD->HFD6w, HFD->NCD and
HFD->HFD. Four files are byte-identical copies of other files of the same
subject, deposited under ses-None names (MPK118 2024-02-13, MPK133 2024-02-07,
MPK134 2024-02-12, MPK172 2024-07-25), and two other ses-None files (MPK122
2024-02-06, MPK143 2024-03-14) are unique sessions whose file names lack the
session date. In 27 files the Z-score (or another series) has more trial columns
than the Ensure, lick and running matrices (60 against 59, 90 against 89, and 90
against 60 and 46 in two files). The starting_time rate of the series is 1 Hz in
about half the files (188 of 349 for the Ensure matrix) and 50 Hz in the others,
while the data are at 50 Hz. The sex of MPK173 is M in its cohort files and F in
its diet-switch files, and that of MPK182 F and M, the cohort-file labels
reproducing the paper's female HFD count; the age is P12W/ in every file, for
recordings that span a year, and one diet-switch file of MPK191 is dated
2024-01-02, before the mouse's cohort recordings of October 2024. The notes give
ensure, bw, ad lib bw and before ad lib bw without units or definitions, the
running signal is signed (11.5% of cohort 1 samples are negative) with no
description of the sign, and the session descriptions name a norm_dff series
that no file holds. In two MPK120 recordings (2024-01-25, 2024-01-29) the raw
signal falls to near zero in 12 trials, which makes dF/F0 undefined there. The
Fig. 3 legend describes recordings with at least 30 of 90 triggered trials, but
the diet-switch recordings in the dataset include the 60-trial sessions of the
cohort-1 mice in both phases. Of the paper itself, for Supp. Fig. 2h the text
calls the NCD correlation positive and the HFD one negative and prints r = -0.34
and 0.26; the data give the signs of the words (NCD 0.13 to 0.22, HFD -0.003 to
-0.33), without significance in both. Questions are put to the paper's authors:
how the Z-score was computed (which recordings were concatenated per animal,
whether it was applied to F or to dF/F0, and whether each trial's pre-cue
baseline was subtracted), on which the fig1k-lme outcome depends; how the Supp.
Fig. 1d lick-rate AUC was normalized, over which window and with which test; and
which recordings enter Supp. Fig. 3l-q and what A and B of Supp. Fig. 3k are in
the files' notes.

The author's points on the protocol: archives.md says to stream with `remfile`,
which took about 30 s per file, so each file was read whole into memory with one
HTTPS GET; the protocol does not say whether a quantity the depositors computed,
here their Z-score, can count as a reading, and it was kept as a variant, which
changes how fig1k-lme reads; supp1cd's criterion says to block when its readings
disagree while step 1.6 would allow adopting the best-supported reading, and the
criterion was followed; the rule to record the first reading the criterion lists
does not cover the case where no reading matches, so the closest one was
recorded for fig1k and fig1l and the first-listed for most others; the rule for
absence claims does not cover a choice of recording set left open by the
criterion, so both sets were run and an assumption recorded where they disagree;
and device files created by the sandbox show as untracked in the repository
root and were left alone.
