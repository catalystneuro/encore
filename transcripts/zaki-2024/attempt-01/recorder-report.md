I ran `tools/readme_row.py 000718 --write`, which added the row `2 (+1) | 0 | 2 | 21` to README.md, and appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

### 000718, Zaki et al. 2024

Two claims reproduced, two not reproduced and twenty-one blocked on the
dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
own outcome for each claim from the notebook with its conclusions removed and
agreed with 25 of the 26; it gave not reproduced for
`offline-bursts-above-shuffle`, as the criterion is written, and suggested
blocking it as `methods_underspecified`, which the record already did, as
round 1 had not seen the record. Round 1 agreed that
`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
the criterion, but argued that the Methods' scoring has no quiet-wake class;
applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
bursts in wake, and under that reading the overlap ensemble co-bursts less
with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
p = 0.13), so the author changed the claim to not reproduced and recorded the
departure from the criterion as a deviation. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper reports that a
strong aversive experience links fear to a neutral context experienced two
days before, that neutral and aversive ensembles in CA1 co-reactivate in
offline population bursts, mostly during wake, and that this co-bursting of
the overlap ensemble with the neutral ensemble goes with the linking. The link
to the paper's per-mouse source data, aversive freezing of the high- against
the low-shock mouse, bursts and skew against shuffled data, the pause in
movement before bursts and wake co-bursting were tested, the last four on the
EEG/EMG cohort where the paper shows three of them in another cohort. The
bursts claim is blocked as `methods_underspecified`, since surrogate over true
burst rate is 1.26 to 1.60 against the paper's 0.72 to 0.96, and a synthetic
control shows the criterion's test cannot detect coordination (5.6 true
against 34.98 surrogate bursts per min); the other 20 blocked claims are
`data_missing`. Some outcomes rest on weak ground:
`ed9b-aversive-freezing-high-vs-low` compares one mouse per group over 30 s
bins that are not independent; in `offline-skew-above-shuffle` both arms are
below the paper's Extended Data Figure 3o values, so the chance level is not
shown to match the paper's; `burst-locomotion-pause` uses the telemetry
activity signal as a proxy for the paper's webcam tracking, and the test gives
p = 0.016 at 300 random times in Ca_EEG2-1; and
`fig5c-wake-overlap-neutral-coburst` rests on one 10 min recording of one
mouse, z-scored within it, and on a log EMG RMS measure chosen after the data
were seen. The author used the open access full text (PMC11666460).

The dandiset was converted by CatalystNeuro (catalystneuro/cai-lab-to-nwb). It
holds two of the nine mice of the calcium imaging and EEG/EMG experiment
(Ca_EEG2-1, high shock; Ca_EEG3-4, low shock) and, of each offline period,
only the first 10 min recording of the 24 the Methods describe; Ca_EEG2-1 has
no offline-day-1 recording and no neutral or novel recall session, and the
mice of the one-hour imaging and offline experiments, the behaviour-only
experiments and the inhibitory tagging and no-shock experiments are not
deposited, so twenty of the 26 claims cannot be tested. Ca_EEG3-4 has no cell
registration, so its ensembles cannot be formed, and the Week file of
Ca_EEG2-1 holds 19 registration tables for offline-day-2 recordings, of which
only the first recording is deposited, and none for offline day 1. The
dandiset does not say why these two mice and only the first offline recording
of each period were deposited, nor that the paper analysed more. The session
start times of the Ca_EEG2-1 behaviour sessions, and the Week epochs built
from them, are about 1 h later than the telemetry and Miniscope clock, so that
OfflineDay2Session1 starts 47 min before the FC session it follows; the
telemetry is absent in windows that contain each of these epochs moved 1 h
earlier. Other findings: the OnePhotonSeries timestamps of three files run at
16.7 ms and end at half the recording's length, while their frame counts fit
30 Hz over the full length; the sleep states include `quiet wake`, which the
paper neither uses nor maps to its states, and the three offline recordings
hold no NREM or REM epochs; the telemetry is sampled at 500 Hz where the
Methods say 100 Hz; the offline session description speaks of an hour of
recording with a webcam, where the deposited recordings last 10 min and hold
telemetry and no video; the fluorescence series carry placeholder
descriptions and unit "n.a.", the FC session descriptions give the shock
amplitude without a unit, and the Week file has an empty session
description; and the analysis code repository the paper names returns 404.
The registration tables agree with the ROI centroids, no recording is
deposited twice, and calcium, behaviour and telemetry are consistent with a
shared clock except in Ca_EEG3-4 offline day 1, where it could not be
established.

The notebook ran in 81 s in the first clean run, and `tools/entry.py all`
took about 2 minutes after round 1. `git clone` from GitHub asked for
credentials, so the source-data and conversion repositories were fetched as
tarballs at pinned commits; removing `__pycache__` and an empty `.claude/`
directory in the entry was denied, and untracked files in the repository root
that the author did not create were left alone. Round 2 found sentences the
outputs did not support, among them that the skew values lie in the range of
the paper's, and a wrong grouping of `fig1ef` and `fig1g`, and these were
corrected. The author's points on the protocol: general claims shown only in a
cohort that is not deposited; a chance level the paper states only in its
source data, for another cohort at another frame rate; whether the lab's
repository of per-mouse figure values counts as data deposited elsewhere; a
link claim on which no claim depends; across-mouse claims with one mouse per
group; a clock check that covers streams within a session but not start times
across sessions; a value seen in the data check before the criteria were
written; and which year to use in the entry name for a paper online in 2024
and in an issue of 2025.
