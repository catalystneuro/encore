I wrote both files and committed nothing. The notes are in `docs/pilot-notes/patel-2026-01.md` (1,616 words, a little longer than the recent notes) and the summary is in `summaries/patel-2026-01.md` (116 words, five sentences). The dataset's `catalystneuro` field is empty, so the second paragraph does not open with the CatalystNeuro sentence. Untracked files such as `.bashrc`, `.idea` and `scripts` sit in the repository root. The author's reports say the sandbox created them, so I left them alone, but the workflow's commit should not pick them up.

# patel-2026, Patel et al. 2026

Eleven claims reproduced, one partially, 14 not reproduced and 35 blocked, 31
for missing data, three for too few bouts under the paper's own decoding rule
and one as not runnable; 14 outcomes rest on an assumption, among them
`fig2c-male-blampfc-excitability-up`, `fig3f-blampfc-distinct-clusters` and
`fig5b-isolation-increases-mpfc-alcohol`. The first verification round gave its
own outcome for each claim and agreed with 60 of the 61 as they then stood,
holding fig2c not reproduced where the record had it partial, and the second
agreed with all 61; nothing was proposed after the second, so there was no
third round. The dandiset is pinned at 0.260911.2319, its only published
version. The paper, Patel et al. in Nature Neuroscience, measures home-cage
two-bottle choice (2BC) drinking and social rank in group-housed and isolated
mice of both sexes, records basolateral amygdala neurons projecting to the
medial prefrontal cortex (BLA-mPFC) and nonspecific BLA neurons in current
clamp, images BLA and mPFC neurons through GRIN lenses during a cued 2BC, with
BLA-mPFC terminal stimulation during mPFC imaging, and manipulates the
projection optogenetically; it reports that isolation raises alcohol drinking
and BLA-mPFC excitability in males and lowers both in females, that BLA-mPFC
activity encodes and predicts alcohol drinking, that terminal stimulation
increases alcohol drinking, and that isolation increases mPFC responses to
alcohol and decreases them to sucrose, which stimulation mimics in group-housed
mice. The dandiset holds 205 current clamp files, 53 cued-2BC imaging files, 24
resident-intruder imaging files and videos. The claims were written from the
version of record (PMC13633117) as text with the legends, Methods and reporting
summary but without any figure, with the bioRxiv preprint cited once for the
3-s bout baseline; the paper links no code, and the values of Supplementary
Tables 1 and 2 are not in the text. The claims check made 17 corrections, among
them a new claim for Extended Data Fig. 8o,p, for 61 claims. Twenty-six could be
tested. Reproduced are, among others, `fig2e-female-higher-baseline-excitability`
(females fire more at 16 and 14 of 26 steps, Sidak significant at 80 to 200 and
80 to 180 pA), `ed2e-nonspecific-bla-excitability`, which rests on the spike
rule, `ed5ef-alcohol-water-nonoverlapping` (on excited sets of 2 to 6 ROIs),
`fig5c-isolation-no-water-change` and `fig6gj-stim-no-water-effect`. Partial is
`ed3c-male-rank-blampfc-excitability`, with rank 1 below rank 3 but below rank 2
at no step (smallest p 0.143 and 0.065). Not reproduced are, among others,
fig2c, where with the 2022 cohort as the group-housed group the interaction is
significant (F(25, 1200) = 4.70 and 4.83) but no step is Sidak significant
(smallest adjusted p 0.116) and the curves cross, while all 37 group-housed
neurons would meet the criterion; `supt1-male-input-resistance-up` (118.0
against 97.6 MOhm, p = 0.052; p = 0.0019 with all 37); fig3f (p = 0.88 and 0.26
with cohort 9 left out); `fig3k-blampfc-response-predicts-bouts` (r2 = 0.004
against the paper's 0.59 +- 0.059); fig5b (one-sided p = 0.49 with matched bouts
drawn at random, p = 0.024 with the first bouts); and the Figure 6 stimulation
claims on alcohol and sucrose responses, among them
`fig6f-stim-decreases-mpfc-alcohol-si` (stimulated 0.226 against 0.117, above
not below). Blocked for missing data are the twelve drinking and rank claims of
Figure 1 and Extended Data Fig. 1, the eight optogenetic behaviour claims, five
resident-intruder claims, the three that need isolated female neurons and three
others; the three decoding claims are blocked as only 1 of 10 nonspecific and 2
of 9 BLA-mPFC mice have five decoding bouts of each liquid, and
`ed9c-coregistered-fraction` as not runnable, as CellReg is MATLAB software. The
author's first run had 11 reproduced, 3 partially, 12 not reproduced and 35
blocked. The author asked no questions of a reader and no questions file
existed, so the answer and author-answers runs changed nothing. Round 1 found
that the 5 mV re-arm of the spike count undercounted at -20 mV, that the flat
female files were not shown to lack data, that a floor on the baseline s.d.
biased the z-scores of cohort 9, that ed3c ran only a per-step Tukey test and
that nonstimulated trials included forced ones; in reply spikes were counted with
a 1 mV re-arm and a 1 ms dead time, the flat files' series were listed and their
block became data_missing, cohort 9 was left out of the baseline z, a
pooled-error Tukey test was added, and fig2c moved to not reproduced, fig2e
from partial to reproduced and fig3f from reproduced to not reproduced. Round 2
asked that ed2e be marked as resting on the spike rule, that
`ed5d-cue-response-modest` name its reading of "falls back toward 0", and that
fig2e say why crossing curves do not count against it, and quoted six sentences
the outputs did not support, among them "7 mice" for 6; all were corrected. The
author's run took about 1 h 25 min; the patch-clamp notebook ran in about 6.6
min and the imaging notebook in about 2.8 min at first, and 7 and 4 min after
round 1. Nothing failed; two commands were denied, one to view a saved output,
which was read with the Read tool instead, and one to remove a `__pycache__`
directory and an empty `.claude/` directory, which were left.

The dandiset holds the current clamp recordings, the cued-2BC imaging sessions
and the resident-intruder imaging sessions only: the home-cage 2BC licks, the
tube-test ranks, the blood alcohol values, the unimplanted control mice, the
optogenetic behaviour sessions (ChR2, ChrimsonR, NpHR), the stability imaging of
Extended Data Fig. 7 and the pose tracking and interaction annotation of the
resident-intruder sessions are not in it, although the description lists pose
tracking, so 28 of the 61 claims cannot be tested for this reason. 13 of the 205
current clamp files hold no recording, only a flat voltage and stimulus series
of the amplifier's secondary channel (VmSec), their size of 31 or 62 MB coming
from histology images; they are 11 isolated female BLA-mPFC neurons and 2
group-housed ones, so only 3 isolated female neurons from one mouse remain
(paper 15 from 7), and one isolated male file holds only the -120 pA sweep. The
imaging files hold every CNMF-E ROI (1113 in the nonspecific BLA mice against
the paper's 540 neurons, 347 against 196 in the BLA-mPFC mice, 748 and 439
against 240 and 281 in the mPFC alcohol sessions), and the visual curation the
Methods describe is not recorded, so the paper's neurons cannot be selected. The
dandiset holds 37 group-housed male BLA-mPFC neurons from 12 mice where Figure
2c uses 21 from 7; the 2022 cohort holds exactly 21 from 7, but nothing marks
the neurons of Figure 2c or Supplementary Table 1. The BLA imaging files do not
say whether GCaMP was expressed in all BLA neurons or only in BLA-mPFC
projectors (the virus and experiment description fields are empty), so cohorts 9
and 10 (10 mice) and cohort 16 (11 mice) were told apart only by the paper's N.
Three pairs of cued-2BC files hold identical fluorescence traces with different
licks, the traces responding to the licks of the second file in each pair. All
53 cued-2BC files carry the same 30 cue timestamps and one of two trial-type
sequences, and in 24 sessions the licks show the forced types swapped against
the stored coding, with 3 cohort-16 sessions mixed; whether light was delivered
on type-4 trials cannot be checked. Cohort 9 traces are nonnegative (minimum
exactly 0, up to 7% of samples at 0) and smooth between transients, although the
Methods say CNMF-E ran without nonnegativity constraints, and on them the
Methods' z-score is undefined or unbounded for most bouts (62% of bout-neuron
pairs have a baseline s.d. under 5% of the session s.d.). Four mPFC sessions
hold 44791 to 65535 frames at 10 Hz for 1-h sessions, two of them exactly 65535,
the largest 16-bit count. The ranks of the imaged mice are not given, 29
nonspecific current clamp neurons carry no rank, and the subject name M3.1 is
used for two group-housed males of rank 1 and rank 3. Lick times are stored as
the data of TimeSeries that also declare a rate of 100 Hz, so a reader that
takes the series at face value gets lick indices. The alignment of fluorescence
and licks could be shown for 40 of 53 cued-2BC sessions. Neuron counts differ
from the paper's in places (56 isolated nonspecific neurons from 11 mice against
54 from 12), and the BLA imaging N includes two mice under the Methods' 50-lick
exclusion rule (44 and 49 alcohol licks). Questions are put to the paper's
authors: how the matched number of bouts was chosen, as Fig. 5b, Fig. 6l,m and
Extended Data Fig. 8n reach p < 0.05 here only with the first bouts; which
group-housed male neurons form Figure 2c and Supplementary Table 1; how five
decoding folds per animal were formed; which BLA imaging cohort is
projection-specific; whether the deposited cohort 9 traces are the ones analysed
and how flat baselines were treated; and how spikes were counted in Clampfit on
plateaus near the threshold.

The author's points on the protocol: it assumes one notebook, where this
attempt needed a patch-clamp and an imaging notebook; it says a seed cannot
change an outcome, but one random draw decided ed8n (p = 0.048), so that reading
was judged over 21 draws; it has no rule for a dataset that holds a superset of
the paper's units with the selection lost; the metadata_insufficient block did
not clearly apply when the imaging populations could be inferred from counts;
its alignment-check examples do not fit continuous imaging with licks; empty
files could be data_missing or data_unreadable, and the finding kinds have no
"unreadable"; and it does not say whether MATLAB-only software such as CellReg
should be reimplemented.

---

Few of the paper's main findings could be tested in this data, and most that could did not hold up. Isolation's opposite effects on male and female drinking, and the optogenetic effects on drinking, are untestable because those behaviour data are not deposited. The fall in female BLA-mPFC excitability is untestable, as most isolated female recordings are empty, and the male rise failed with the neurons taken to be Figure 2's but passes with all deposited ones. Isolation and stimulation effects on mPFC alcohol and sucrose responses, and BLA-mPFC responses predicting drinking, did not reproduce on all imaged ROIs, as the curated neurons are not marked. Higher excitability in group-housed females and most controls held up.
