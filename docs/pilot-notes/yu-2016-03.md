# crcns-ssc-7, Yu et al. 2016

Twenty-four claims reproduced (one on an assumption), 13 partially (three on an
assumption), six not reproduced (two on an assumption) and five blocked, all
five for missing data. The first verification round agreed with 47 of the 48
outcomes as they stood and the second with all 48; nothing was proposed after
the second, so there was no third round. CRCNS does not version data sets, so
the version is recorded as unversioned with the data set's DOI
(10.6080/K0T43R01), and the notebook header gives the MD5 of `data.tar.gz`. The
paper, Yu, Gutnisky, Hires and Svoboda, "Layer 4 fast-spiking interneurons
filter thalamocortical signals during active somatosensation" in Nature
Neuroscience (19:1647-1657), records 29 VPM single units with silicon probes and
layer 4 excitatory (L4 E) and fast-spiking (FS) neurons, whole-cell and
cell-attached, in head-fixed mice performing a lick/no-lick pole localization
task with whisker video, and adds thalamic photoinhibition, infraorbital nerve
(ION) transection, eNpHR suppression of PV cells and rabies tracing; the data
set is one 6.2 GB `data.tar.gz` of 148 NWB 1.0 files in 7 folders, whose counts
match Supplementary Table 2. The claims were written from the extracted text of
the version of record and the legends of its supplement, without rendering the
PDF, and without the paper's code, which is the data set's own
`example_analysis_code` folder; the claims check corrected 11 claims and two
shared method notes and added `fs-hf-fluctuations`, for 48. The claims on VPM,
L4 E and FS activity during touch and whisking, thalamic photoinhibition of
cortical neurons, the ION cut and eNpHR could be tested; the two claims on the
depolarized recordings of Fig. 3, the thalamic multiunits under TRN
photostimulation, the rabies tracing and the L5 FS neurons after ION cut could
not. Reproduced are, among others, `vpm-whisking-rate` (4.34 and 11.92
spikes/s, p = 5.2e-8), `vpm-phase-modulation` (27 of 29 units),
`fs-whisking-rate` (21.7 against 9.43 spikes/s, p = 2.3e-5), `ion-cut-behavior`
(0.492 correct over 1,335 trials), `enphr-kruskal-wallis` (H = 18.0, p =
0.00044, n = 43) and `l4e-reversal-potential`, whose median whisking reversal
lies 4.9 mV above rest, inside the 5 mV margin; `fs-touch-vm` is reproduced on
taking the first tracked whisker series as the principal whisker. Partial are,
among others, `vpm-baseline-rate` (median 1.99 spikes/s, outside 3.3 +- 0.33),
`thalamus-inhibition-fs` (all tests hold, rates at 12%, 27% and 47% of control),
`ion-cut-l4e-whisking` (a control mean of 1.337 mV, 0.003 below its bound) and
`thalamus-inhibition-l4e-vm`, on the assumption of 1 ms smoothing and a 1 ms
hold for the light-onset latency (4.8 and 2.6 ms), since the rule as written
crosses at the onset sample. Not reproduced are `l4e-spikes-touch-selective`
(whisking changes the rate, p = 0.020 to 0.027), `ion-cut-l4e-touch` (0.321 mV
against zero, p = 0.0078, though random times give 0.208 mV and touch does not
differ from them, p = 0.148), `enphr-spikes-per-touch`, `enphr-auc-groups`,
`enphr-auc` (rho = -0.23, p = 0.16 and rho = -0.28, p = 0.09 with the first
touch of trials tagged passive left out; kept, p = 0.038 under reading (b)) and
`enphr-behavior` (4 of 9 mice decrease against 6 of 8, assuming the recording
sessions are those of Supplementary Fig. 14). The author's first run had 24
reproduced, 14 partially, 5 not reproduced and 5 blocked. The author asked no
questions of a reader, so the answer and author-answers runs changed nothing.
Round 1 disagreed on `l4e-example-e24-e32` (reproduced under the 100 ms rise),
and raised an extrapolated threshold line in the distance to threshold, the
untested principal whisker choice, an incomplete check of the Fig. 3 recordings,
criteria for `ion-cut-l4e-touch`, `enphr-auc` and `thalamus-inhibition-dose`
that cannot tell the effect from its null, the sessions of `enphr-behavior`,
and passive first touches and later touches left in the windows; in reply
`l4e-example-e24-e32` became reproduced, setting Vm after a later touch to NaN
moved `l4e-reversal-potential` to reproduced and `ion-cut-l4e-whisking` to
partial, leaving out passive first touches moved `enphr-auc` to not reproduced
on an assumption, 13 drifting trials of JY1139 were left out of the Vm measures,
variants were added, and three questions on those criteria went to a reader in
`questions/crcns-ssc-7.yaml`, a file written after the answer run, so they are
unanswered. Round 2 agreed with all 48 outcomes, corrected its own round-1 count
line, asked that `fs-touch-vm` and `enphr-behavior` be marked assumed (the
latter arguably blocked), and found text the outputs did not support, among
them seven VPM sessions where there are 7 units in 6 sessions and 8 or 9 direct
cortical activation neurons where 8 were printed; in reply both were marked
assumed, `enphr-behavior` was kept tested, the forward-difference threshold
search was run and the text was corrected. The notebook streams the archive
once per run and ran in 583 s at first, 806 s after the author-answers run,
1048 s after round 1 and about 22 minutes after round 2; during development a
cache placement bug made the light traces look stored for one trial per file
until the first full streamed run exposed it, and those claims were redone. The
untracked dotfiles and `scripts/` directory in the repository root were left
alone.

Four experiments the paper reports are not in the data set: the 17 thalamic
multiunit recordings during TRN-axon photostimulation, the rabies tracing, the
L5 FS neurons after ION cut and the whole-cell recordings with depolarizing
current injection of Fig. 3 (n = 6), where no whole-cell L4 E trial has a median
Vm above -42.8 mV, so five claims cannot be tested. Seventy cortical files hold
two tracked whisker series and nothing says which whisker each is; mapping them
in the order of general/whisker_configuration gives FS neurons almost no touch
response (0.45 against 1.78 spikes per touch with series 1), while for several
L4 E neurons it picks the series with the larger response (JY1345 0.857 against
0.235), and the example code takes the first whisker as the main one. In the
cortical files the whisker timestamps, labelled seconds, are the trial start in
milliseconds plus the time within the trial in seconds. JY1139, in the
whole-cell FS folder, is described as "Excitatory" in its file, and its first 18
trials have median Vm between -2.3 and -26.8 mV while it fires 8 to 85 spikes per
trial with no injected current above 0.1 nA, with nothing marking those trials.
Eight whole-cell L4 E files flag 132 stimulus trials but hold no photostimulus
series, and Exp_2015-09-24_004 and JY1633 have 23 flagged trials without light.
The data hold 43 eNpHR L4 E neurons against the paper's 40, 13 under thalamic
photoinhibition against 12, 8 under direct cortical activation against 7 and 9
mice with eNpHR light against 8; the cell list does not name JY1268, which has
eNpHR light trials, and lists JY0781 among the PV-IRES-Cre neurons though its
file holds no photostimulus series. The paper itself gives 26 and 25 L4 FS
neurons and 8, 9 or 10 ION-cut L4 E neurons in different passages. Questions
are put to the paper's authors: how the Vm latency after light onset of
Supplementary Fig. 9c,f was defined, how the light artifact was handled and
whether dVm/dt was smoothed; which tracked series is the principal whisker and
whether the touch-speed cutoff of compute_touchNWB.m was applied; and whether
the first touch of a trial tagged passive was used in the ROC analysis of Fig.
8f,g.

The author's points on the protocol: the CRCNS section of `docs/archives.md`
assumes zips that can be opened in place, while this data set is a single gzip
tar that can only be read in order, so it was streamed once per run; developing
on a subset is costly when every read streams from the start, so a reduced cache
was kept in `$TMPDIR`; many criteria have no rule for a partial result, so
partially reproduced was used when some parts held and the effect was present;
the absence rule forces not reproduced on `ion-cut-l4e-touch` although its
measure is positive by construction, so a comparison with random times was
shown as a variant; the protocol gives no guidance when a fixed latency rule
fails on the data, so a stated variant was adopted for the Vm latency and the
PSTH latencies were reported as not found; and runs are asked to take under ten
minutes, where streaming alone takes about 8.
