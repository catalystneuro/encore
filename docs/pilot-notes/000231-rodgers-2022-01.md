# 000231, Rodgers et al. 2022

Twenty-three claims reproduced, none partially, six not reproduced and ten
blocked, all on the dataset. It pins version 0.220904.1554, which the paper
cites and which is the only published version. The paper, Rodgers in
Scientific Data, is a data descriptor for 115 sessions of 15 head-fixed mice
doing whisker-based shape discrimination or detection, with whisker video, pose
tracking, contacts and, in 44 sessions, neural recordings from barrel cortex;
it reports no statistical tests. The claims were written from the version of
record as served by Europe PMC, without its figures, and from the paper's
UsageNotes.ipynb (cxrodgers/NwbDandiData2022 at commit 33d610b). The counts of
mice, sessions, frames and neural hours, the task rules, the trials table, the
video and neural timebases, the units and electrodes, the pose and contact
tables, the file layout and the subjects were tested. `response-window-timing`,
`neural-video-alignment`, `behavior-clock-drift` and the three tracking error
claims are blocked as `data_missing`, as the motor times, the sync pulse
channels, the Arduino logs and the curated training sets are not deposited;
`reward-and-timeout` and `session-min-trials` are blocked as
`methods_underspecified`, as the criterion's readings disagree (a timeout of
12.21 s or 8.34 s; a smallest session of 84 or 101 trials), and the two claims
restating findings of earlier papers are blocked by the claims file.
`dataset-size` is not reproduced, as the mice, sessions and 63,979,800 frames
match but the trials are 32,350 or 22,905 against 18,514;
`choice-time-first-lick` (77.6% of trials), `ignore-trial-definition` (160
spoiled trials not ignored), `trials-table-structure` (5 of 32,235 pairs),
`unit-quality-isi` (the firing-rate part fails under both bin readings) and
`session-labeling-quality` (up to 7.7% of a whisker's contacts with a missing
frame) are not reproduced too. The author asked a reader whether the tracking
claims and `behavior-clock-drift` should use the original Zenodo release (ref.
13, doi:10.5281/zenodo.4743837), whose README lists a trainset/ folder and
per-session behavioral log files; the reader answered that the paper never
says what that release holds, so the claims file and the outcomes were
unchanged and the release was not read. Round 1 agreed with all 39 outcomes,
though its totals line was miscounted (24, 7 and 8), which round 2 corrected
and which the author's first revision report had repeated. Its points led to
reading the Open Ephys record headers for neural-hours (33.770 h without seven
short segments, 33.782 h with them), a check that contact stops are inclusive,
contacts pooled over a session's whiskers (2.007% and 2.008%), a reading of the
task from the experiment description stated as such, amplitude drift from the
Kilosort files, the session KF134 2018-02-09 left out of the unit counts and
the Table 4 electrode columns checked. Round 2 agreed with all 39, so there was
no third round; it found statements the outputs did not support, among them
the short Open Ephys segments called the paper's test recordings, "on 22% of
other trials" for the share of mismatched trials, "begin at trial 61 or later"
for the first random trials, the README run time and the .log files left
unidentified, which were corrected. Two questions were put to a reader during
the revisions, after the answer step: whether "next trial" in
`trials-table-structure` means the next table row or the next trial run, under
which all 32,230 pairs with consecutive trial numbers agree and the outcome
would become reproduced, and whether the 2% bound of
`session-labeling-quality` is per whisker or pooled over a session, where the
pooled result rests on one contact (54 of 2,691 is 2.007%, 53 would be 1.97%).
The author's run finished by 04:33 UTC and took about 66 minutes; during
development a network reset and an S3 403 failed a pass, and retries and a fix
to how the S3 URL is resolved were added. The notebook ran in 4.7 minutes at
first and in 4.1 minutes in the last run.

The right reward series is identical to the right lick series in every file
(315,782 times against 12,447 correct right-rewarded trials), so right reward
times are not available. The analog inputs that carry the trial
synchronization pulse are listed in each session's .openephys index (100_ADC1
to 100_ADC8, 100_AUX1 to 100_AUX6) but not deposited, and all_channels.events
holds no events, so the neural to video alignment cannot be checked; the
behavioral (Arduino) timebase and the curated whisker training sets and
held-out predictions, which the abstract offers, are not in the dataset
either, and the paper does not say where they are. The paper's 18,514 trials
cannot be recovered from the files, which hold 32,350 trials, 22,905 with
ignore_trial False, and no other combination of the trial flags tried gives
it, while the video frame total and the 44 neural sessions match exactly. The
trials table departs from Table 6: choice_time is NaN on all 265 spoiled
trials, where Table 6 says it is 45 s after the window opens, and on the 22%
of other trials where it is not the first lick in the window (7,185 of
32,085) it falls 0 to 5 ms after the window opening on 7,183, with no lick
within 5 ms of it on 94% of them; 160 spoiled trials have ignore_trial False,
which in the files equals "non-random or optogenetic" on every trial; and
1,533 trials have stimulus "flatter convex" or "flatter concave", which Table 6
does not list. The dataset does not meet the paper's inclusion criteria as the
files allow them to be checked: in 27 sessions more than 2% of a whisker's
contacts hold an interpolated or absent frame (16 sessions for C1 to C3, up to
7.7%), C0 is labeled in fewer than 95% of frames in 3 to 7 sessions, and one
session (228CR, 2019-07-15) has 84 trials with ignore_trial False. The
keywords of all 30 detection sessions include "shape discrimination", contrary
to their experiment description. The Data Records sections name processing
groups behavioral_events, raw_whisker_position, processed_whisker_position and
identified_whisker_contacts, while the files, Table 1 and UsageNotes.ipynb use
one module behavior, so the access code printed in the Data Records fails on
these files. The neural recording has no timestamps array, which Table 2 and
the paper's access code describe, its times being stored as a starting time
and a rate, and 29 files hold three contacts tables, not four, without a note
on whether the whisker made no contact. Two questions are put to the paper's
authors: how the typical 9 s timeout is measured, as after an error stop_time
minus choice_time is a median 12.21 s and 8.34 s longer than after a correct
trial, and which trials count as "trials to analyze" in the rule that
excludes sessions with fewer than 90.

The author's points on the protocol: step 1.6 lets the author adopt a reading
when readings disagree while several criteria say to block, and the claims
file was followed; the reward part of `reward-and-timeout` fails on the right
side in a way the criterion's outcome rules do not cover; some criteria have
no partial outcome for near-total agreement, as in `trials-table-structure`;
it does not say whether an author may look at an outside archive only to
locate data for a reader question; video frame counts cannot be checked by
decoding 2 TB of video, so container headers were used; docs/archives.md does
not say that the version endpoint lacks `asset_count` or that a HEAD request
on DANDI's signed S3 URLs returns 403; and step 1.2 does not say what to
compare when checking for duplicate recordings.
