# crcns-alm-1, Li et al. 2015

Twelve claims reproduced (one on an assumption), four partially (one on an
assumption), one not reproduced and 12 blocked, 11 for missing data and one as
methods_underspecified. The first verification round agreed with 26 of the 29
outcomes as they stood and the second with all 29, withdrawing its round-1 not
reproduced for `ed1-fast-spiking-properties` and
`contra-ipsi-selectivity-forms`; nothing was proposed after the second, so there
was no third round. CRCNS does not version data sets, so the version is recorded
as unversioned with the data set's DOI (10.6080/K0RF5RZT), and the notebook
header gives the MD5 sums of the files read. The paper, Li, Chen, Guo, Gerfen
and Svoboda in Nature (519, 51-56), records left ALM in mice performing a
delayed whisker-based object location discrimination task with directional
licking, and reports that unilateral photoinhibition of ALM biases licking to
the inhibited side, that ALM neurons carry preparatory and peri-movement
selectivity with contra- and ipsi-preferring neurons in equal proportions, that
pyramidal tract (PT) neurons identified by antidromic tagging prefer
contralateral licking and develop contralateral selectivity late in the delay
where intratelencephalic (IT) neurons do not, with calcium imaging of
retrogradely labelled PT and IT neurons, and that subthreshold photostimulation
of PT neurons biases licking contralaterally; the data set holds the
electrophysiology, 1,408 units from 99 sessions in 19 mice, with cell type
labels, trial types, epoch times, photostimulation type per trial, lick traces,
raw voltage traces and the authors' MATLAB scripts, in one tar.gz per animal.
The claims were written from the version of record as text extracted from the
PDF, with PDF pages 2, 3 and 5 opened to read Figs 1d, 2c, 2d, 3e, 3f, 3i and
5b, and without code, as the paper links none and the data set's scripts were
not read; the claims check made ten corrections, among them the IT fractions of
Fig. 3i (about 0.22, 0.56 and 0.22) and jitter tolerances of 0.05 ms, for 29
claims. The author followed the deposited scripts where the paper is silent. The
selectivity counts and time course of Fig. 2, the error trials, the contra and
ipsi balance, the fast-spiking neurons, the tagging and the PT and IT
selectivity of Fig. 3 could be tested, task performance only on the 19
electrophysiology mice of the paper's 42; the photoinhibition behaviour of Fig.
1, the imaging of Fig. 4, the photoactivation behaviour of Fig. 5 and ED Figs 3
and 6, the anatomy and the recordings of ED Fig. 7 could not, and the reaction
time could not be judged, as it falls inside or outside tolerance with a
detection rule the paper does not give (65.0 ms at 3 times the noise with a 2 mV
floor, within 61.1 +/- 10.5, and 71.7 to 103.7 ms under the other noise rules on
correct trials). Reproduced are, among others, `fig2-selective-fraction` (912 of
1,245 pyramidal neurons, exactly), `fig2d-response-categories` (219 preparatory
only, 389 with both and 304 peri-movement only, the figure's reading),
`fig2e-equal-contra-ipsi` (427 and 485), `ed2-error-trials-predict-choice`,
though weak in the sample epoch (r -0.085 to -0.123),
`fig2c-dynamic-single-neurons`, on the claims file's assumed 0.5 bound,
`tagging-counts` (45 PT and 27 IT, counts of the deposited labels) and
`fig3fj-contra-preferring-pt-not-it` (PT 24 of 38, P = 0.033, IT P = 0.74),
which holds with selective neurons and not with all tagged neurons (P = 0.089)
or with the more than 15 correct trials of each type that a line of the data
set's script requires (P = 0.11). Partial are `unit-counts` (the stated widths
give 1,245, 158 and 5 units, the labels 1,245, 124 and 39),
`ed1-fast-spiking-properties` (higher baseline rates, but FS neurons are more
selective, 79.8% against 73.3%), `antidromic-latency-jitter`, which rests on a
+/-1 ms window (PT 2.672 ms and 0.126 ms; IT jitter 0.310 ms, within tolerance
only with a +/-0.5 ms window), and `contra-ipsi-selectivity-forms`. Not
reproduced is `fig3f-late-contra-selectivity-pt`: PT modulation is 34.4%, the
paper's value, but all task-selective neurons give 9.2% with P = 0.024 where the
paper has P = 0.13, the onset is 310 ms against 570, and none of 32 combinations
of readings gives the paper's pattern. The author's first run had 13 reproduced,
3 partially, 2 not reproduced and 11 blocked. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1 disagreed
on three claims, giving not reproduced for `ed1-fast-spiking-properties` and
`contra-ipsi-selectivity-forms` and partially for `antidromic-latency-jitter`,
and raised the +/-0.5 ms window, the reaction-time detector, the widths of the
unlabelled units, readings of the shared methods that were not run, the t-test
on rates and the NaN-type light trials; in reply `antidromic-latency-jitter`
moved to partially on a +/-1 ms window, `reaction-time` went from not reproduced
to blocked after a second detector was added, the two other disagreements were
kept and recorded, the four readings of the shared methods were run without
moving any outcome, and the cited MATLAB lines were printed. Round 2 agreed with
all 29, asked for the IT jitter measured without the window and for the fig3fj P
value under the script's trial filter, and found sentences the outputs did not
support, among them type-0 light trials said to start from 3.2 s and
sample-epoch light trials said to be always at about 23 mW; in reply the outputs
were added and the text corrected, and no outcome changed. The author's run went
from 21:14 to about 22:02 UTC; the notebook ran in 239 to 251 s at first, 400 s
after the author-answers run and 324 s after round 1, and nothing failed. The
raw voltage traces (about 800 GB) were not read, and the untracked dotfiles and
`scripts` folder in the repository root were left alone.

The data set holds only the electrophysiology of Figures 2 and 3 and Extended
Data Figures 1, 2 and 5; the photoinhibition and photoactivation behaviour (Fig.
1, Fig. 5, ED Figs 3 and 6), the calcium imaging (Fig. 4), the anatomy (ED Fig.
3) and the recordings with somatic PT photoactivation (ED Fig. 7) are not in it,
and the paper names no other deposit, so eleven of the paper's findings cannot
be tested. The trough-to-peak widths of the deposited mean waveforms put 34 of
the 39 unlabelled units below 0.35 ms (158 in all), where the paper and the data
description call all 39 intermediate (0.35 to 0.45 ms); the labels split the
widths cleanly (FS 0.154 to 0.256 ms, unlabelled 0.307 or 0.410 ms, pyramidal
0.461 to 0.666 ms), so the cellType labels match the paper's counts but the
stated thresholds do not give them. Only neurons that passed the collision test
are labelled (45 PT, 27 IT), so the 22 and 106 activated neurons and the 7
untestable ones cannot be checked. PhotostimulationType takes the values 3, 4
and 5 in 495 trials, all in the two Tlx_PL56-Cre x Ai32 mice, though the data
description lists only 0, 1, 2 and NaN, and the NaN-type test trials carry light
in 3,756 trials of all 19 mice in configurations the description does not give,
so which of them, if any, are the ED Fig. 7 PT photostimulation sessions cannot
be told; the one Sim1 x Ai32 mouse (ANM218693, 3 sessions) has 520 light trials,
all NaN-type, as eight 1 ms pulses, not the 20 Hz trains of 2 ms pulses of Fig.
5. In session ANM210862_20130627, 43 trials of type 0 ("non-stimulation trials")
carry 8 to 22 light pulses of 50 ms at 47.1 mW. The lick trace is described only
as "licking movement from photodiode", and its baseline (0.07 to 4.83 V per
session), scale and sign differ between sessions, with no detection rule or
calibration. In 3,707 of 28,465 performing trials the sample or delay epoch
differs from 1.3 s by more than 50 ms (up to 14 s), which the description does
not mention, and 10 units have spike times out of order. The NWB copies of the
sessions omit the photostimulation type, the AOM and laser power traces and
GoodTrials, so only the MATLAB files support the analysis. The Results give 389
neurons with peri-movement selectivity only and 304 with both, where Fig. 2d and
the data have the reverse. Questions are put to the paper's authors: how the
reaction time of 61.1 +/- 10.5 ms was found from the photodiode trace, with what
threshold, trials and mice; how antidromic spikes were told from spontaneous
ones, and whether spikes locked to the pulse over several milliseconds were
counted; and whether the PT and IT bootstraps of Fig. 3f, j use all tagged
neurons or only the selective ones, and which neurons and window give the P =
0.13 for all task-selective neurons.

The author's points on the protocol: `docs/archives.md` describes CRCNS data as
zip files, while this data set has one tar.gz per animal, which was streamed in
sequence (about 14 GB); CRCNS has no pinned version, and the bucket's
`version_1/` and `version_2/` folders hold only documentation, so `live` was
used and recorded as unversioned, with the MD5 sums in the notebook header; the
authors' scripts ship in the data set but the paper does not link them, so their
rank among the method sources is unclear, and they were used as the basis for
assumptions and cited; the authors' precomputed results
(`ALM_compiled_all_data.mat`) were not read, to keep every number computed from
the data; `measured` needs one number per expected value, so it was left out for
`tagging-counts` and `antidromic-latency-jitter`, whose activated-neuron values
cannot be measured; criteria without a partial outcome were judged by the
protocol's general meaning of partially reproduced; for `unit-counts` the
criterion's width measure was followed where it and the labels disagree; and for
`fig3fj-contra-preferring-pt-not-it` the criterion's "under one reading" was
followed over step 1.6, without marking the outcome as resting on an assumption.
