I wrote `docs/pilot-notes/001968-nakagawa-2026-01.md` and changed no other file. It runs to 1601 words, within the range of the five most recent notes. The dataset's `catalystneuro` field is empty, so the second paragraph has no conversion sentence. Nothing is committed. The untracked dotfiles in the repository root were already there, and I left them alone.

# 001968, Nakagawa et al. 2026

Two claims reproduced (one on an assumption), four partially (three on an
assumption), four not reproduced (all four on an assumption) and 33 blocked, 32
for missing data and one as methods underspecified; the two link claims the
author added, both partially reproduced, are counted apart. The first
verification round agreed with 42 of the 45 outcomes as they stood and the
second with all 45; nothing was proposed after the second, so there was no
third round. It pins version 0.260914.1316. The paper, Nakagawa et al., "Early
dopamine disruption in the entorhinal cortex of a knock-in model of Alzheimer's
disease" in Nature Neuroscience, records layer 2/3 units of the lateral
entorhinal cortex (LEC) with tetrodes in APP NL-G-F knock-in (APP-KI) and WT
mice during a head-fixed olfactory go/no-go task in which a novel rewarded
Odor-1 and a novel punished Odor-2 are learned beside the prelearned Odor-A and
Odor-B, records dopamine signals in LEC by photometry of GCaMP6m in VTA/SNc
dopamine neurons, and tests the behaviour of old mice, optogenetic stimulation
of dopamine fibres, L-DOPA and histology; the dandiset holds 3855 assets (1.63
GB) from 37 subjects, 3813 unit files from 27 tetrode mice and 41 photometry
sessions from 10 mice. The claims were written from the version of record as
served by Europe PMC (PMC13246448) and the supplement PDF extracted to text,
without seeing the figures; the paper's code page (igarashilab.org/resource)
holds only MATLAB scripts of a 2021 place cell protocol, so no method detail is
settled by code. The unit counts, firing rates, the photometry claims of Fig. 4
and Supplementary Fig. 7 and the young mice's behaviour of Fig. 1d and 1e (on
10 of the paper's 27 mice) could be tested; the cue response, population
trajectory, similarity and decoding claims, the spike width classes, the
histology, the behaviour of old, prelearning, optogenetic and L-DOPA mice and
the dopamine-behaviour correlation of Supplementary Fig. 6d could not. Most
photometry and behaviour outcomes rest on assumptions: that the traces are
sampled at 1 kHz with the cue at sample 1000, that codes 1 to 4 are Odor-A,
Odor-B, Odor-1 and Odor-2, and that the mean over a mouse's sessions stands in
for the paper's hemispheres, with sessions as a variant. Reproduced are
`ed4c-higher-firing-rates` (principal cells Z = -7.18, p = 6.8e-13,
interneurons Z = -2.21, p = 0.027, higher in APP-KI) and
`fig4f-error-sessions-no-difference` (interaction p = 0.22 to 0.998, though
there are 1 or 2 WT error sessions, so the absence carries little weight).
Partial are `units-recorded` (young APP-KI 891 units, within 846 +- 85; young
WT 635 against 479 +- 48), `fig1e-young-correct-sessions` (under B1 both means
within tolerance with p = 0.067, under B2 p = 0.046 with WT at 90.0%),
`fig4b-wt-dopamine-t1` (T1 means 1.17, 1.66 and 0.55, all within tolerance,
the significance part not testable with 5 mice, whose smallest possible
signed-rank p is 0.0625) and `figs7-odor1-specific-decrease` (Odor-1 against
Odor-B p = 0.055 with mice as units, reproduced with sessions). Not reproduced
are `fig1d-young-new-association-impaired` (WT 87.3 and 88.8 against 90.6 +-
0.9, interaction p = 0.26 and 0.13, with a power of 0.69 on 5 against 5 mice),
`fig4c-app-dopamine-delayed`, `fig4d-app-odor1-dopamine-decreased`
(interaction p = 0.16 and T1 Tukey p = 0.059 in the 1 to 4 s window the
criterion fixes; the 2 to 4 s variant gives T1 Tukey p = 0.0032) and
`fig4e-correct-sessions-odor1-decreased` (interaction p = 0.08 to 0.33). The
author's first run had the same outcomes except that figs7 was reproduced, on
sessions as units. The author asked no questions of a reader, so the answer
and author-answers runs changed nothing. Round 1 disagreed on units-recorded
and fig1e (not reproduced, as their criteria say only when the claim is
reproduced) and figs7 (partially reproduced), and found that sessions count
each hemisphere more than once (30 APP-KI sessions from 8 hemispheres), that
the rank-sum and signed-rank tests disagree for fig4b, that fig1d and fig1e
rest on 10 of 27 mice, that the RS/FS labels allow a two-class test of ed4a and
that the type II ANOVA differs from MATLAB's default; in reply the mouse mean
was adopted as the unit, which moved figs7 to partially reproduced, the
signed-rank test was adopted, power estimates, a two-class variant (chi2 =
39.0, p = 4.1e-10), a cue check from the step at samples 1001 to 1002, type III
sums of squares and a table of principal cells per mouse and session were
added, and units-recorded and fig1e were kept as partial. That revision did not
write round 1 into the record. Round 2 agreed with all 45 outcomes, found no
number the outputs contradict, asked that the record say why units-recorded and
fig1e are partial and that fig4b and fig4c say their significance parts are
settled by the 5-mouse unit, and noted duplicated passages in the record; in
reply the text was corrected and both rounds were written into the record,
round 1 rebuilt from its report. The author's run went from 06:30 to 07:16
UTC; the first notebook run failed on a pandas `.any(1)` call, which was fixed,
and the notebook ran in 165 s at first, 174 s after the author-answers run and
about 2 and 3 minutes after the two revisions. Small files were fetched whole
into memory, as remfile was about 20 times slower. The untracked dotfiles in the
repository root were left alone.

The unit files hold spike times only, with no odor onset, trial type, lick or
trial table in any file, so no unit can be aligned to the task and the 13
claims on cue responses, population trajectories, similarity and decoding
cannot be tested; they hold no waveforms or spike widths either, only an RS or
FS label in each source file name, so the paper's three spiking classes cannot
be formed. The histology, the optogenetic and L-DOPA behaviour, the
behaviour-only mice, the prelearning sessions and the behaviour of the tetrode
mice are not in the dandiset, and photometry mouse 00163 of Supplementary Table
2 is missing. No file states genotype, age group or treatment: strain appears
only in the unit source file names (WT, AD, NLGF), the photometry files carry
none, and the L-DOPA and saline mice are both labelled NLGF, so the groups come
from Supplementary Table 2 and Supplementary Fig. 2a. The photometry files
state no sampling rate, cue time, brain region, hemisphere or odor and action
names, and call the trial columns dF/F while they are z-scored to their first
1000 samples; each holds one trace per session, while Supplementary Table 2
lists bilateral recordings in 7 of the 11 mice. The source file names label
mice 01398 and 01431 as AD, where the paper lists both as young WT. Mouse
00375's units are deposited twice, in 100 files named LEC_Sim1_..._Sum.mat with
genotype 'Sim1' and age P205D that repeat the spike trains of its 99 regular
files, one of them twice; the earlier published version 0.260913.1518 holds one
of these copies only. One file,
sub-mouse02491/sub-mouse02491_ses-mouse02491-20250408_obj-8lnxe6.nwb, holds no
units table. Sex in the files differs from Supplementary Table 2 for 00265,
00703 and 00789, and 00789's date of birth makes it 1.3 to 1.6 months old at
recording, below the paper's young range of 3 to 6 months. The dandiset holds
more units than the paper reports (635 against 479 for young WT, 860 and 778
against 671 and 618 for old mice, 263 and 286 against 144 and 132 for the
L-DOPA cohorts), nothing marks which units the paper analysed, an odor-set
field that doubles the novel letters (ABCCDD against ABCD) is not explained,
and no rule over sessions or odor sets gives the per mouse cell counts of
Supplementary Fig. 2a (for 01398 its first four sessions give exactly the
paper's 112, of 203). Photometry sessions hold 99 to 269 trials with novel
odors from the first trials, where the paper describes about 20 A/B-only trials
followed by 160 AB12 trials. The paper contradicts itself: Supplementary Table
2 lists mice 247, 690, 703, 925 and 941 as young APP-KI and 789, 1199, 1253,
1254 and 1517 as old, while Supplementary Fig. 2a lists the second five as
young, and the files' birth dates agree with Supplementary Fig. 2a. A question
is put to the paper's authors: whether the 3 SD threshold of Supplementary Fig.
6d is the SD of the precue baseline or of the session's signal, over which
window, and whether the window mean or any sample must exceed it, since with
the precue SD r ranges from 0.30 to 0.73 across these choices.

The author's points on the protocol: link claims need a criterion written
before analysis while their need appears only after the metadata survey, so
they were written after the survey and before any measures and recorded as a
deviation; nothing covers a dataset that lacks the paper's unit of analysis
(hemispheres), so both sessions and mice were run; when the paper names a test
two ways (rank sum in the text, signed-rank in Supplementary Table 1) the
protocol does not say whether these are alternatives or method readings; it is
unclear whether testing a claim on a subset of animals (10 of 27 mice for fig1d
and fig1e) should be an outcome or a block, so it was tested with the subset
recorded as a deviation; claims with no partial rule where only part holds were
marked partially reproduced; and the rule that the paper is not an outside
input does not cover group labels taken from its supplement, so Supplementary
Table 2 and Supplementary Fig. 2a were listed under `inputs` and those claims
marked `with_labels`.
