I wrote both files and changed nothing else. Nothing is committed. Two things to know:

- **No CatalystNeuro sentence:** `targets/dandisets.json` has no entry for 000021, so there is no `catalystneuro` field to go on. The notes don't say who converted the dataset.
- **Untracked files:** `git status` shows some untracked dotfiles and folders I didn't create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.

**`docs/pilot-notes/wei-2023-01.md`**

# wei-2023, Wei et al. 2023

Thirteen claims reproduced on the dandiset, six partially, thirteen not
reproduced and none blocked, with two more reproduced and two partially that
also use the model features of the paper's code (`with_inputs`); the link claim
`source-data-units-link`, partial because the dandiset holds 13 of the paper's
25 wild-type sessions, and the twelve claims on data held elsewhere (nine
reproduced, two partially, one blocked) are counted apart. The first
verification round agreed with 43 of the 49 outcomes as they stood and the
second with 46, disagreeing on `figs3b-fs-faster`, `figs5-depth-distribution`
and `fig7e-pvalb-sst-one-channel`, changes were proposed for the first two, and
a third round reviewed those two. It agreed that figs3b is not reproduced, since
its criterion has no partial clause and no reading puts both medians within
tolerance, and disagreed with partially reproduced for figs5, which it would
give as reproduced (p = 0.044 with the CSD depth and the attempt's own
clusters), so figs5 stays not reproduced with the proposal kept; fig7e stays not
reproduced with the round-2 disagreement recorded. The record pins version
0.251116.2246, the only published version; the paper cites none. The paper,
Wei, Nandi, Jia, Siegle, Denman, Lee, Buchin, Van Geit, Mosher, Olsen and
Anastassiou, "Associations between in vitro, in vivo and in silico cell classes
in mouse primary visual cortex" (Nature Communications 14, 2344), clusters the
extracellular action potential (EAP) waveforms of V1 units recorded in vivo,
first into fast-spiking (FS) and regular-spiking (RS) units on two
single-channel features (TPW and REP), then each into three sub-clusters on the
propagation velocity below and above the soma; it relates the clusters to
firing, visual responses and phase-locking to the LFP, maps them with
classifiers to 18 AP and 15 SP biophysical models and to in vitro features of
Allen Cell Types cells, and compares opto-tagged Pvalb and Sst units. The claims
were written from the version of record with its supplement and the Source Data
workbook, and from the code at commit 1e35126, which starts from prepared
waveform files and holds no code for Fig 3, Figs 5 to 7, the phase-locking or
the opto-tagging; the claims check corrected a misreading of the fig6d t-tests,
tightened several criteria and added `figs6c-granular-phase`, for 49 claims.
Reproduced on the dandiset are the FS/RS split (K = 2 by both methods), the FS
fraction (25.4%, on the attempt's own unit set), the greater asymmetry of RS
units, the RS1 and RS3 spatial claims and the lack of an FS spread difference,
the FS1 symmetry, the FS/RS classifier (99.34%), the lack of visual-response
differences among FS clusters, the RS theta preference, and three opto-tagging
claims (Pvalb units in FS, more symmetric and with a higher CV). Not
reproduced are the units per mouse (57.0 against 48 +- 4.8), the FS and RS
gray-screen rates, the three FS sub-clusters (FS gives K = 2), the depth
distribution, the RS2 and RS3 visual responses, six phase-locking claims, the
tagged unit counts and fig7e. Clustering the paper's own Source Data features
gives K = 3 for FS and RS with the paper's labels for all 1204 units, so the
fig2d failure comes from the features recomputed here; every FS1 to FS3 claim
rests on FS forced to K = 3. The model and in vitro claims ran on the code's
model features, the Source Data and the Allen Cell Types API, and
`figs8-rotation-symmetry` is blocked as `not_runnable`, as the models and their
simulations are not public. The author's first run gave 24 reproduced, 13
partially, 11 not reproduced and 1 blocked. Round 1 found that neither isolation
reading of the claims file gave the paper's unit set (reading (a) adds 248 units
that fire very little and loses 73), that the feature mismatch with the Source
Data was not diagnosed, that the CSD depth disagreed with the code's, that the
classifiers upsample before the split, and that spontaneous phase-locking was 4
to 16 times the paper's; in reply the claims after fig1d moved to a third unit
set, reading (c), reading (a) with at least 100 spikes in the first 5-min gray
screen, which keeps all 603 reading (a) units of the code's tables and adds 27,
the tagged units were put through the code's exclusions, permutation baselines
were added, the electrodes tables were checked, and a question on the isolation
readings went to a reader in `questions/wei-2023.yaml`. With about half the
paper's units, several weaker effects lost significance, and eleven outcomes
changed. Round 2 found that the code's layer 4 centre, which round 1's reply had
taken as the paper's CSD placement, is 2740 um on 8 of the 13 probes, that 9 of
the 10 tagged Pvalb units come from session 797828357, and sentences the outputs
did not support, among them that the 12 missing sessions belong to the
Functional Connectivity set and that the CCF coordinates are NaN on every
channel in 6 sessions; the CSD centre computed here then decided the depth
claims, and the sentences were corrected. The author's run went from 18:48 to
about 22:40 UTC, of which an hour was lost when `tools/entry.py check` hung on
a regular expression that backtracks on lists of 9-digit integers, fixed
by writing those lists as split strings; the notebook ran in 1433 s, twice with
identical outputs, at about 2 GB per worker, the random forests used 20
resamplings in place of 100, and the bifurcation distances were not recomputed.
The entry ran in 2571 s after round 1, 50 minutes after round 2 and 1754 s at
the end.

The dandiset holds 13 of the 25 wild-type sessions the paper analysed; the other
12 (766640955, 767871931, 768515987, 771160300, 771990200, 774875821, 778240327,
778998620, 779839471, 781842082, 793224716, 847657808), with 638 of the paper's
1204 units, are not among its 32 session files, and none of those 638 unit ids
is in any of them, though the paper's Data availability statement names only
this dandiset for the in vivo data. It also holds 5 of the 8 Pvalb and 6 of the
12 Sst opto-tagging mice. The electrodes tables' CCF coordinates hold NaN in 6
of the 24 sessions used (every value in 3, 1152 to 5760 of 6912 values in the
other 3), and in the other 18 y equals z on every channel, so no channel can be
placed in the CCF and the CCF layer of a unit cannot be read; the location
column gives VISp without the layer. The files do not say which units the paper
analysed or give its cluster labels, which come only from the Source Data under
the same unit ids. What is there agrees with the paper: every one of the 566
Source Data units of the held sessions is a VISp unit of quality good, with the
per-session counts of sheet Fig 1d, TPW and REP recomputed from the files' mean
waveforms equal the Source Data values for 85% of them, and the drifting-grating
metrics and the code's firing-rate columns are reproduced exactly. The units
table's waveform_mean is labelled volts but holds microvolts (amplitudes of
about 5 to 500). The paper does not state its isolation criteria: the code's
unit tables hold 618 units of the held sessions, 15 of which fail the AllenSDK
default filter, which passes 900, and every unit of the code's tables has at
least 100 spikes in the first 5-min gray screen while 270 of the 297
filter-passing units outside them have fewer. The code's 3 SD exclusion uses
np.mean and np.std, so one NaN turns it off for that feature, and run literally
it keeps a unit at 93.6 ms/mm that forms one of the three RS clusters on its
own. The code's classifiers upsample before the 75/25 split, so copies of a unit
fall in training and test; for the random forests of Fig 5c and 5d this inflates
the accuracy (61.7% on permuted RS1 to RS3 labels, where chance is about 33%;
splitting first gives 97.5% against 98.6% in vivo and 85.3% against 93.5% for
the SP models), while for the linear SVM the effect is small (53.2% on permuted
labels). The models' conductances are not public beyond a few Source Data
columns, and the model repository holds one example model; the in vitro
features of the Source Data equal those of the Allen Cell Types Database API.
The paper gives 24 wild-type mice in the Fig 1d legend and 25 in the text and
Source Data, 25 Pvalb units in the text and 24 in the Fig 7 legends and Source
Data, and p = 0.0067 for the fig6g maximum rate, where the rate gives 0.0011
and 0.0068 is the t-test p of the resting potential. Questions are put to the
paper's authors: how units were judged well isolated, how the layer 4 centre
was placed from the CSD, over which period the Fig 3a rate, CV and LV are
taken, which opto-tagging baseline window was used, and, for the phase-locking,
which LFP channel and which spikes under the 10,000 cap were used, what kappa
is, given that the Methods say it runs from 0 to 1, and which spikes and period
give 4.7% of RS units theta-locked in Fig S7, where 75% are here.

The author's points on the protocol: it does not say whether claims downstream
of a clustering that does not reproduce are tested or blocked, and they were
tested on FS forced to K = 3 with the paper's labels as a variant and marked
assumed; a claim on data elsewhere cannot be blocked as `data_missing` when
those data are public only in the Source Data, and such claims were tested on
the Source Data values; some criteria, those of fig5c and figs3b, have no
partial clause, and the protocol's general meaning was used; the ten-minute
target could not be met, as streaming and LFP filtering alone took about 11
minutes; and the check tool's regular expression hung for an hour and should be
fixed.

**`summaries/wei-2023-01.md`** (117 words)

The split of V1 units into fast-spiking (FS) and regular-spiking (RS) clusters on their waveforms held up in this data, and RS units formed the paper's sub-clusters, but FS units did not. Clustering the paper's own published features recovers its sub-clusters, so the gap lies in the features recomputed from the files, which hold only 13 of the paper's 25 sessions. Most sub-cluster differences in visual responses and LFP phase-locking did not reproduce, several weaker effects losing significance with fewer units. Opto-tagged Pvalb units fell in FS and were more symmetric than Sst units, though mainly from a single animal. The mapping onto biophysical models and in vitro cells largely held, tested on the paper's published values.
