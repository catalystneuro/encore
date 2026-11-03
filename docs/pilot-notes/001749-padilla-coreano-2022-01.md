# 001749, Padilla-Coreano et al. 2022

Six claims reproduced (two on an assumption), one partially, two not
reproduced (one on an assumption) and 37 blocked, 23 as metadata insufficient
and 14 for missing data. All 46 claims are on the dandiset. The first
verification round agreed with 42 of the 46 outcomes as they stood and the
second with all 46; one change of outcome was proposed after the second, and a
third round agreed with it. It pins version 0.260311.1727, the published
version. The paper, Padilla-Coreano, Batra, Patarino et al., "Cortical
ensembles orchestrate social competition through hypothalamic outputs" in
Nature, records mPFC neurons with a wireless logger while two cagemates of
known tube-test rank compete for a reward; the dandiset holds 53 NWB files of
implanted mice in three cohorts, mPFC ("ephys"), mPFC-BLA and mPFC-LH
("chrimson"), with ranks, tones, port entries, AlphaTracker poses and nine
hand-scored behaviour labels, and 52 videos. The claims were written from the
PMC author manuscript (PMC9576144) and the Nature supplementary information,
which holds Methods sections 1 to 17, without a main-text PDF, and from the
paper's HMM-GLM code (Tyelab/HMMGLM at commit 3fc3567), after an earlier claims
run had stopped because the Methods were missing; the check changed eight
claims, removing a test and a threshold the paper does not give, and left four
points open. The behavioural claims of Extended Data Fig. 5 were tested on the
hand-scored labels: `ed5b-rank1-wins-most` (rank 1 won 10 of 11, 90.9%, with
12, 11, 15 and 15 competitions per rank against 12, 12, 15 and 14),
`ed5e-port-occupancy-not-different` (p = 0.284 over 20 sessions),
`ed5f-dominants-displace-more` (91.7% against 60.2% of pushes, p = 0.0051, over
13 sessions) and `ed5g-time-displaced-not-different` (p = 0.359) are
reproduced, and `ed5c-rewards-not-different` is partial, as rewards did not
differ (p = 0.498) but no file holds a body weight. `ed5d-subordinates-slower-latency`
is not reproduced, on an assumption: subordinates are slower in every reading,
and the rank-sum p is 0.0196 when label trial j is set against tone j, but with
each file's best tone shift and without the files whose labels and port entries
agree at r below 0.3 it is 0.375, and the label latencies give 0.206. The three
HMM-GLM claims rest on the paper's MATLAB code ported line by line to Python and
on multi-unit counts computed from the raw recordings of the 17 labelled files
whose clock offset can be placed (512 of 965 trials, 10 of 14 mice).
`fig1i-hmmglm-decodes-behaviour` is reproduced on the assumption of counts and
contiguous folds (AUCs 0.60 to 0.83, median 0.774, sign test p = 0.0039), and
`ed5k-hmmglm-generalizes-across-rank` on the assumption of threshold crossings
in either direction, where every combination gives 9 of 9 AUCs above 0.5 and
negative crossings give 7 of 9 (p = 0.18) from subordinates to dominants.
`ed5j-six-states` is not reproduced: held-out likelihood selects 2 states on the
dandiset's input (3 with crossings in either direction) and 6 on the paper's own
processed input, so the difference comes from the input. The 22 single-unit
claims are blocked because no cluster carries a curation label, and
`ed7b-distance-by-trial-type-not-rank` because no file holds the port location;
the unimplanted cohort, the AlphaTracker evaluation frames, the alone sessions,
the ex vivo recordings, the phototagging pulses and the optogenetic experiments
are not deposited. The author's first run tested six claims, all reproduced,
and blocked the other 40, the HMM-GLM claims as metadata insufficient without
porting the model, with no outcome on an assumption. The author asked no
questions of a reader, so the answer and author-answers runs changed nothing.
Round 1 disagreed on `ed5c-rewards-not-different`, which it gave partially
reproduced, and on the three HMM-GLM claims, which it found testable in part
from the raw signal, called `ed5d-subordinates-slower-latency` fragile, and
found that the weights, the file contents and the alone sessions were asserted
without output, that one reading double-counted sessions and that two variants
tested nothing new; in reply ed5c became partial, ed5d not reproduced on an
assumption after the robustness checks it asked for, the HMM-GLM was ported and
run, sessions became the main reading and cells printing every file's groups
and subject fields were added. Round 2 agreed with all 46, asked that ed5k be
marked assumed or run under the other readings, asked for the paper's input at
1 to 10 states, z-scored runs at another learning rate, a run without
20191029-chrimson2-2-2v3 and a second cut-off for ed5d, and found five sentences
the outputs did not support; in reply these were run and corrected, and the
change of ed5k to reproduced was proposed, which round 3 accepted provided it
stays marked as an assumption. The -498.757 that round 2 read for one state on
the paper's input could not be reproduced, as both later runs print -529.600
with the same seed. The author's run took 12:00 to 13:52 UTC, with a
column-name clash and a misreading of the tone schedule and delivery times in
the data check fixed before the final run; the notebook ran in 550 s at first
and 527 s after the author-answers run, and with the HMM-GLM in about 50
minutes at the end. The changes in `tools/build_site.py` and
`tools/site_assets/app.css` and the untracked files in the repository root were
left alone.

Every one of the 5,879 Klusta clusters is labelled unsorted, where the paper
analyses 998 manually curated cells, and no rule on firing rate comes near 998
(5,232 clusters at or above 0.05 Hz, 2,075 above 1 Hz), so none of the
single-unit findings can be tested. The spike_times of every units table are
two thirds of the time of the same spikes in the ElectricalSeries, as if divided
by 30 kHz where the logger samples at 20 kHz; multiplied by 1.5 they line up
with threshold crossings in 50 of 53 files. In 18 of the 21 mPFC-LH files and
one ephys file the rescaled spikes match the recording only after an offset of 5
to 28 s, and in 3 mPFC-LH files at no offset within 60 s. The offset between the
neural recording and the behaviour clock is in no file, though the dandiset
description says a video_gap variable holds it; estimated from the units'
responses to port entries it is 4 to 45 s, differing by session (294 s in one
file), and it cannot be estimated for the 10 ephys files or for 12 of the 38
files with port entries. The paper's processed HMM-GLM input matches the
labelled trials and gives one offset per file, which agrees within 1 s with the
port-entry offset in 20 of the 23 files where both are clear. The
ElectricalSeries of sub-20191025-chrimson2-3-1v3 is the same signal as that of
sub-20191029-chrimson2-3-1v3, while their units differ. The 10 ephys files hold
no port entries, labels or poses, every pose value is missing in all 22
mPFC-BLA files, 17 of the 53 competitions have no labels of either mouse, and
the poses are given for Mouse1 and Mouse2 with nothing saying which is the
subject and without the nose the Methods say was tracked. Reward deliveries are
0.49 s after tone onset in every file, where the Methods give 2 s; the tone
times are the program's schedule, the same in all files of a cohort, and in 7 of
the 10 ephys files the last tones fall after the end of the recording.
pair_in_dataset is 'not included' in all 53 files, though for 20 sessions the
competitor's file is in the dandiset; sub-20200121-BLA2-1-1v2 has a session
start of 2020-01-22 13:30 while its labels mirror those of the 2020-01-21 13:15
session, and the subject description of sub-20200123-BLA1-3-2v3 swaps the
mouse numbers of its file name. Where both mice of a session are labelled, one
file's labels mirror the other's, in every bin for most sessions but in only 76%
and 68% of position bins in 20200121-BLA2-3v4 and 20200122-BLA1-3v4. In 18 of
the 34 labelled files the labels hold fewer trials than tones and nothing says
which tones were scored. The 34 labelled files hold 965 trials from 14 mice, the
size of the paper's HMM-GLM dataset (965 trials, 32 sessions, 13 mice), and the
paper's processed input holds 14 animals too, where Methods 17 says 13 mice,
with 487 dominant trials where the Extended Data Fig. 5k legend gives 482.
Questions are put to the paper's authors: in which direction the 4 SD
multi-unit threshold was applied and whether the HMM-GLM input is counts or
normalised rates, and how the reward latencies of Extended Data Fig. 5d were
matched to trials and which tones the hand-scored labels cover.

The author's points on the protocol: it does not say what counts as a session,
and the paper's counts fit one file per mouse better than unique competitions,
so both readings were run where the measure allows; it has no rule for a claim
that is half untestable, such as Extended Data Fig. 5c with its weight part;
it gives no way to choose the main block reason when two apply, as for the
HMM-GLM claims, where the missing clock offset was chosen over the MATLAB-only
code; and it does not say whether a clock offset estimated from neural
responses may be used, so it was used at first only to show that the offset
exists.
