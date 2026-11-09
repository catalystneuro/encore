# 001048, Semenov et al. 2025

No claim is counted on the dataset, as DANDI:001048 holds none of the paper's
data and all 20 claims are on data elsewhere; of these, three reproduced, six
partially, one not reproduced and ten blocked. The first verification round
was given another claims file and, its results mapped onto this file's claims,
agreed with 8 of the 16 it covered; the second agreed with 19 of the 20
outcomes, and a third round, held on the one change of outcome proposed after
the second, agreed with it. It pins version 0.250701.1624, the only published
version. The paper, Semenov, Kim, Silkuniene and Pakhomov, "Excitation and
polarization of isolated neurons by high-frequency sine waves for temporal
interference stimulation" in Cell Reports Physical Science, stimulates single
cultured rat hippocampal neurons with 250-ms unmodulated or 20-Hz modulated
sine waves at 2 and 20 kHz, records optical action potentials (APs) with
FluoVolt in NaCl or low-conductivity sodium gluconate solution, and images
membrane charging by 2-us pulses and polarization by modulated sine waves with
strobe imaging. The claims were written from the NIH author manuscript in
PubMed Central (PMC12320893) with its supplement; the paper reports no original
code. The claims were tested on the dandisets the paper lists, 001030, 001032,
001033, 001035 and 001271 to 001274, with 001034 used only to show it is a copy
and 001031 not used. Most time-lapse outcomes rest on an assumed soma ROI, the
16 x 16 pixel crop the depositors cut around the soma, where the claims file's
Otsu readings give other outcomes. `fig2d-5ap-above-1ap`,
`fig2c-pure-more-aps` (44 of 52 pairs against 2, p = 1.2e-08) and
`fig2-modulated-locks-to-beats` reproduce, the last resting on the O4 b level
by 0.14 % dF in one session, a choice made after the first run showed that
session. `ap-selection` is partial, the peak (10.53 % dF) holding and the
duration (3.70 ms) not; `fig1-pure-sine-excites-all` is partial, the latency
(59.8 to 88.4 ms against 90 to 220 ms) and rate ceiling (22.6 to 42.3 Hz)
failing under every reading; `fig2d-modulated-thresholds-higher` is partial,
the direction holding and one of three tests significant (p = 0.034);
`fig3c-sustained-firing-2s` is partial, no neuron showing the block;
`figs1-di8-same-as-fluovolt` is partial with 3 of the 8 neurons deposited; and
`figs2-ttx-blocks-depolarization` is partial, its depolarization half resting
on one neuron. `fig1-excitation-block` is not reproduced, none of the 12 to 14
neuron-frequencies tested above their best-rate voltage showing sustained
depolarization under the crop ROI. `fig1-20khz-needs-twice-the-field` and
`threshold-depolarization-estimate` are blocked as `metadata_insufficient` for
want of the voltage calibration, `fig3b-low-conductivity-halves-threshold` and
`fig3-extrapolated-threshold` as `other`, the low-conductivity 250-ms sessions
being in no dandiset, `fig3-not-heating` as `methods_underspecified` (3.89 or
1.95 C against 2.5 C), and the five strobe claims of Figures 4 to 6 as
`metadata_insufficient`, the files holding no ROIs and no cell identities. The
author's first run gave fig1-20khz and fig6-sine-less-than-pulse as partial and
fig4-pooled-time-constants and threshold-depolarization-estimate as not
reproduced. The author asked a reader no questions, so the answer run and the
following author run changed nothing. In round 1 `tools/entry.py handover`
copied the claims file of 001274, which has the same file name, over this one,
so the verifier judged 26 claims of another file; its problems with the code
still applied, among them an AP detector that counted oscillations on a plateau
as APs, the crop-ROI rule, uncorrected bleaching and early latencies, and in
reply the detector was changed, fig1-20khz, fig4-pooled and threshold were
blocked and outcomes resting on the crop ROI were marked assumed; the tool
could not be fixed, as the workflow collects changes only under attempts/,
claims/, entries/ and questions/. Round 2 disagreed with fig6, asked that
fig2d-modulated be marked assumed, questioned the crop-ROI rule, which the
author kept under protocol step 1.6, and the O4 b choice, and found sentences
the outputs did not support (four 100-Hz sessions at most where 2_20240522 has
five, carriers near antiphase in all cells where 7 of 9 are, the peak holding
in every crop reading where 12 of 16 do, a list of unused stimuli without 40
and 100 kHz, and a README saying all ten dandisets were used), which were
corrected; the change of fig6 to blocked was proposed and round 3 agreed, noting that the per-cycle reading
halves the peak-to-peak amplitude, which is now a deviation. The author's run
took about 2 h 20 min (03:35 to 05:57 UTC), a missing import, a misplaced
helper definition and a print-format bug being fixed during development. The
notebook ran in 28 min at first, 1549 s after the answer, 2,292 s after round
1, about 20 min after round 2 and about 24 min after round 3.

DANDI:001048 names the paper as related (IsPublishedIn) but holds TIRF
recordings of HEK cells under patch clamp from another study, with species
human; the paper's data are in 001030 to 001035 and 001271 to 001274, of which
only 001271 to 001274 name the paper. 001034 is a copy of 001032, all 178
recordings identical pixel for pixel under other subject names. The stimulus
voltages are generator settings; the files say the delivered amplitude is
"somewhat smaller", with frequency-dependent calibration factors "reported
separately", which are in none of the dandisets, and 001032 to 001035 label the
voltage peak to peak and give 36 V/cm per volt without saying of which, so
thresholds in V/cm and the 20-kHz to 2-kHz ratio cannot be computed as the
paper did. The low-conductivity 250-ms sessions of Figures 3A and 3B are in no
dandiset, and 001272 holds 3 of the 8 Di-8-ANEPPS neurons of Figure S1. 001030
gives its neurons as mouse and makes each session a separate subject, so its
four neurons appear as 17 subjects, and 001035 describes its neurons as
"C57BL/6 rat". 001271 does not mark when the vehicle was applied, and its 71
TTX session descriptions say TTX "caused sustained depolarization" where the
dandiset's description says it "completely prevented sustained
depolarization"; all 65 Di-8-ANEPPS session descriptions of 001272 say "without
tetrodotoxin (vehicle control)". The strobe dandisets hold no ROIs, no debris
ROI, no cell shape or orientation, no stimulus waveform and no mark of the 19
Figure 4 experiments or the cells C1 to C9 of Figure 6, the Figure 5 cell's 12
sine sessions match no cell, and 001273 notes that its 40, 80, 100 and 130 V
pulses measured 25, 62, 79 and 102 V, where the paper gives 140 V/cm for every
Figure 4 experiment. Frame 0 of every time-lapse file is a bright artefact (at
least 1.51 times frame 1, median 3.15), 59 sessions of 001032 end at 291 ms,
before the stimulus ends, and the stimulus onset is stored only in the
description text. The dandisets also hold stimuli the paper does not describe,
sine waves of 20 Hz to 10 kHz, 40 kHz and 100 kHz, 100-kHz bipolar pulses in
001031 and TTX strobe sessions in 001274. Questions are put to the paper's
authors: how the soma ROI was drawn, how APs were identified and their
duration measured (about 3.7 ms here against the paper's 8 ms), how the maximum
firing rate was measured where APs merge, and the calibration to V/cm; the size
of the strobe ROIs, which groups of 001273 are the 19 experiments and which
cells are elongated, which cells of 001274 are C1 to C9, the phase of the
modulated waves at the first frame and the field used for each cell; and which
field and heat capacity give the 2.5 C rise.

The author's points on the protocol: the data elsewhere are here other
dandisets in the same archive while the target holds nothing, and the target's
version was pinned with the ten dandisets under `inputs`; the checker rejects
`data_missing` for `elsewhere` claims even when the data are in no archive, so
`other` was used; the claims file's header blocks a claim whose readings
disagree while step 1.6 allows an assumption, and the protocol was followed;
the protocol does not say whether the author may add a reading, and the crop
ROI was added with every reading shown; the claims file's 5-SD AP reading
misses most APs on the noisy masks, and it was kept and shown; expected values
given for each frequency or type get one number under `measured`, and one was
recorded and named; there is no finding kind for duplicate deposits, and
`other` was used; no stimulus timing is stored, so the clock check used the AP
rate before, during and after the stimulus and sham sessions; the ten-minute
runtime aim cannot be met with 11 GB of strobe data; and derived traces were
kept in the scratch directory during development to avoid re-streaming.
