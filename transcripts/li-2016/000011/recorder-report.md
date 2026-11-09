I ran `tools/readme_row.py 000011 --write` and it left README.md unchanged. The 000011 row (6 | 5 | 9 | 18) was already there, committed by an earlier recorder run that stopped partway. The only file I changed is `docs/pilot-notes.md`, and nothing is committed. Here is the subsection I added at its end:

### 000011, Li et al. 2016

Six claims reproduced, five partially, nine not reproduced and eighteen
blocked, all on the dandiset. It pins version 0.220126.1907, the only
published version, as the paper cites none. The author put ten questions to a
reader, and nine of the answers were that the paper does not give the detail,
so each open detail became a set of readings under which the outcome must be
the same; the answers changed two outcomes. `cd-captures-selectivity` moved
from not reproduced to blocked as `methods_underspecified`, as the cd values
are within tolerance with all correct control trials (66.2% and 34.6%) and
outside with the training trials (73.7% to 88.0%), and `ed9f-reaction-time`
stayed blocked but moved from `methods_underspecified` to `data_missing`.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions and summary removed and agreed with 34 of 38. `selective-fraction`
and `ed2b-silencing-strength` moved from partially reproduced to not
reproduced, as with lick-early trials dropped only 1 of 4 counts holds in the
first and with them kept only 1 of 4 parts in the second, and
`cd-stable-over-epochs` moved from reproduced to blocked, since taking w from
all correct control trials (0.563 and 0.588) was the author's choice and the
training subset gives 0.534 to 0.554. The author kept
`ed7e-roc-larger-photoinhibition` and `ed8-roc-during-photoinhibition` as
partially reproduced, where round 1 gave not reproduced, under a rule written
after round 1 for criteria without a partial clause (partial when at least
half the parts hold under every reading that must agree); round 2 accepted it
for consistency and agreed with all 38, so there was no third round. The paper, "Robust neuronal
dynamics in premotor cortex during motor planning" in Nature, records units in
left ALM of mice in a delayed-response task while one or both hemispheres are
photoinhibited, and reports that preparatory activity and behaviour recover
after unilateral but not bilateral silencing, that the recovery needs the
other hemisphere, as shown by callosotomy, and that modular network models
recover where single-module models do not. The unit classes, selective counts,
recovery of rates and selectivity after silencing, the coding direction and
its modes, the session biases and the network models were tested. The
behavioural photoinhibition claims, the photoactivation claims and the spatial
extent of silencing are blocked as `data_missing`, the four callosotomy claims
on the recordings as `metadata_insufficient`, and `fig1g-selectivity-recovery`
and `ed7-larger-photoinhibition` as `methods_underspecified` because their
readings disagree (12, 9 and 3 of 24 combinations with three, two and no
times within tolerance for fig1g). `fig2e-selectivity-recovery-times` is not
reproduced because ipsilateral selectivity does not reach 80% of control
before the go cue under any of the 24 combinations, against the paper's 538
ms, and `fig3d-persistent-mode` and `fig3e-ramping-mode` because both modes
predict the lick on control trials above chance (59% to 62% and 55% to 58%).
Some outcomes rest on weak ground: `fig1f-spike-rate-recovery` holds only on
the reading without exclusion, which tests 248 neurons per condition against
the paper's 168 to 175, while the reading close to the paper's counts fails;
and the partial outcomes of `unit-classification`, `fig2-recordings-recovery`,
ed7e, ed8 and `fig6-modular-models-recover` rest on the author's rule, which
the claims file does not contain and under which, read strictly, they would be
not reproduced. A question asks a reader whether the claims file adopts it.

The dandiset holds only the recording sessions: the behavioural
photoinhibition sessions (Figs 1d, 2b, 5b and Extended Data Fig. 3), the
photoactivation mice (Extended Data Fig. 5), the untrained mice used to map
photoinhibition (Extended Data Fig. 2d) and any session before callosotomy are
not in it, so nine of the paper's findings cannot be tested, and its
genotypes are VGAT-ChR2-EYFP and PV-ires-Cre x ReaChR only. 33 sessions of 7
mice, the callosotomy group by genotype and delay, and 3 experiment-1 sessions
of mouse 255200 have no photostimulus record, though most of them contain
trials whose activity is silenced in the light window of the other sessions,
so their photoinhibition and control trials cannot be told apart; no file
says which mice were callosotomised, on which side or when. The trial table
has no photostimulus column, so the site, number of laser spots and timing of
a trial can be recovered only from the per-site laser power traces and the
photostim_start_time events, and the number of spots is stated nowhere. In
lick-early trials the photostimulus events are logged at the restarted delay,
after the light seen in the laser trace; over all labelled sessions 339
lick-early photostimulus trials have the event more than 0.1 s after the
light, with the light up to 10 s before the logged go cue, so with lick-early
trials kept these trials enter the photoinhibition averages without light (3%
to 16% of each condition's trials in experiment 1, 6.5% to 7.5% in experiment
2). No file holds lick times, only the analogue lick_trace, which in the 24
experiment-2 sessions used for the activity space holds no licks, so reaction
times cannot be computed there. The control mice hold 979 units against the
paper's 1012, with 15 of intermediate spike width against 50, so about 33
intermediate units were not deposited (widths from upsampled waveforms give
11), and the units' cell_type labels intermediate-width units as FS, where the
Methods exclude them (45 units in all). The paper's neuron and session counts
for its selectivity and population analyses (55, 143 and 40 selective
neurons; 16 sessions with 6 to 20 neurons) cannot be reached with the
criteria the paper states, the dataset giving 138 to 173, 221 to 293, 58 to 62
and 24 sessions with 6 to 37 neurons, and experiment 1 holds 4 mice where the
paper reports 6. Other findings: session 258250_20141202 holds two
interleaved sequences of trial ids (1 to 24 and 105 to 160) whose times
overlap (98 overlapping pairs), in 28 units of 3 sessions the spike times are
not in time order and two sessions have trials out of time order; and the
asset sub-255200_ses-20140910_behavior.nwb holds only metadata.

The notebook ran in about 11.5 minutes in the first run, 1042 s after the
answers, 791 s after round 1 and about 19 minutes after round 2, and
`entry.py all` passed with no errors. One run failed after a regex that
stripped bold markup also removed `**` operators from the code; they were
restored and the outputs matched the earlier run. Round 1's points led to
spike widths from waveforms interpolated to ten times the stored rate, the
size of the lick-early artefact, per-neuron trial counts and epoch
selectivity of the included populations (no simple further selection gives
the paper's counts), per-session ROCs of the modes, raw lick-trace levels
above the experiment-2 baseline with the ed9f test run on the 6 experiment-3
sessions as a variant (it holds under 18 of 26 combinations), reference
numbers on the recording sessions for the blocked behaviour and callosotomy
claims, and three more questions to a reader, which are unanswered. Round 2
found statements the outputs did not support, among them a time of 750 ms
called outside a tolerance of 210 to 770 ms in ed7, the event said to be
logged up to about 2 s after the light where the maximum printed is 1587 ms,
and differences within 2 s.e.m. under every reading in fig3e where that holds
for T1 only, and these were corrected; a typo fix in a markdown cell came
after the last run and was applied to the executed copy by hand. Untracked
files in the repository root that the author did not create were left alone.
The author's points on the protocol: it does not say how the claims file's
rule that any reading may reproduce combines with readings of details the
author finds open; it gives no guidance on reporting up to 256 combinations
per claim; the claims file's "trials per condition" could not be left open;
there is no `data` kind for simulations that use no data; unlabelled
photoinhibition trials fit both `data_missing` and `metadata_insufficient`;
there is no channel to pass back a point the data settle in the claims file;
its rule for selections covers only chance levels; it does not say whether a
measured recovery time is the point estimate or the bootstrap mean; the
header table allows only "tested" or "blocked" for claims that ran but are
blocked; and question files name a single claim where questions apply to
many.
