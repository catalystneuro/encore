# 001272, Semenov et al. 2025

Two claims reproduced on the dataset, three not reproduced and none blocked,
and of the two claims that also need the FluoVolt dandisets, one partially
reproduced and one not reproduced. Of the 12 claims on data elsewhere, other
dandisets of the same paper, two reproduced (one on an assumption), two
partially reproduced, four not reproduced and four blocked. The first
verification round agreed with 12 of the 19 outcomes as they stood and the
second with 18, and a third round, held on the one change of outcome proposed
after the second, agreed with it. It pins version 0.250805.1358, the latest
published version; the paper cites none, and 0.250701.1622 has the same blobs.
The paper, Semenov, Kim, Silkuniene and Pakhomov, "Excitation and polarization
of isolated neurons by high-frequency sine waves for temporal interference
stimulation" in Cell Reports Physical Science, records optical APs by fast
imaging in cultured rat hippocampal neurons stimulated with sine waves, and
001272 holds the control experiment of Figure S1, neurons stained with
Di-8-ANEPPS in place of FluoVolt and stimulated with 250-ms unmodulated 2-kHz
sine waves. The claims were written from the NIH author manuscript
(PMC12320893) with its supplement, Figure S1 read from its legend only; the
paper reports no original code. On the dataset,
`figs1-aps-as-emission-decrease` reproduces under all 12 readings, the inverted
trace giving more APs than the trace as recorded in every neuron, and
`figs1-stronger-field-shorter-delay-sustained-firing` reproduces on reading
the AP height as prominence and as 5 SD of the trace before onset (latency
correlating negatively with field in all 3 neurons, rho -0.63, -0.03 and
-0.50, and sustained firing in all 3). `figs1-eight-neurons` is not reproduced
(3 neurons). `figs1-near-threshold-delayed-aps` is not reproduced on reading
"delayed" as at least 100 ms after onset: every neuron fires a median of 1 AP
at threshold, but only subject 4 at 100 ms or later (137 ms), and under the
other reading, later than at the neuron's higher fields, every neuron passes,
so the outcome rests on the reading. `figs1-culminates-in-sustained-depolarization`
is not reproduced (at most 1 of 3 neurons under any of 24 combinations, and
none after a bleaching correction); subjects 2 and 4 were stimulated up to 234
V/cm only. `figs1-noisier-than-fluovolt` is not reproduced, the Di-8-ANEPPS
traces being less noisy by the SD before onset (whole frame 0.55 against
0.88%), and `figs1-effects-same-as-fluovolt` is partially reproduced on an
assumed amplitude scale, the response pattern holding only in part and the
t test finding no threshold difference with n = 2 or 3 and 95% intervals as
wide as -156 to 124 V/cm. Elsewhere, `fig2c-pure-more-aps` reproduces under all
12 readings, and `figs2-ttx-blocks-depolarization` on the whole frame, with its
sustained-depolarization part tested in 1 of 6 TTX neurons.
`fig2-modulated-locks-to-beats` is partially reproduced (89 to 91% of APs
within 12.5 to 37.5 ms of a beat under the whole frame, but one modulated
session with 13 APs), and `fig3c-sustained-firing-2s` on the height read as
prominence, with neuron c7 alone showing the pattern and no null test to
confirm the reading. `fig1-pure-sine-excites-all`,
`fig1-20khz-needs-twice-the-field` (ratios 1.71 to 2.98),
`fig2d-modulated-thresholds-higher` (the 2-kHz 5-AP test at p = 0.0500 under
two whole-frame readings) and `fig4-pooled-time-constants` (0 of 8 readings,
on DANDI:001273) are not reproduced. `fig3b-low-conductivity-halves-threshold`
is blocked as other, since the checker does not allow `data_missing` on a
claim marked elsewhere, `fig4-orientation-and-poles` as `metadata_insufficient`,
`fig6-sine-less-than-pulse` as other, not attempted though the data are in
DANDI:001274, and `threshold-depolarization-estimate` as depending on it, its
FluoVolt threshold measured at 140 to 178 V/cm against 57.7 +/- 3.6. The
author's first run gave 4 reproduced, 5 partially, 5 not reproduced and 5
blocked. The round-1 verifier was handed the claims file of DANDI:001273 in
place of this one, since `tools/entry.py handover` copies every claims file of
the paper under the same file name, and it judged several claims against the
001273 criteria; each response says where the two files differ. Round 1 also
found that a height read as the dF value counts noise on a raised baseline as
APs, that the detector had no null test, that the eroded Otsu ROI is empty in
all 65 files and that the strobe fits reported values stuck at a bound; in
reply a null test was added, prominence was adopted for Di-8-ANEPPS,
`figs1-noisier-than-fluovolt` moved from partially to not reproduced and
`fig4-pooled-time-constants` from blocked to not reproduced, all 22 strobe
experiments now fitted. A reader question on the AP width at half height was
answered by widening it from 2 to 20 ms to 1 to 20 ms, and no outcome changed.
Round 2 disagreed only with `figs1-near-threshold-delayed-aps`, whose
criterion is one test per neuron, found sentences the outputs did not support
(the median AP height, the O5 (b) counts, an unprinted session, the gluconate
count, the 001034 file count and the description texts), which were corrected,
and raised three gaps in the claims file, which were put to a reader. Round 3
agreed with the change to not reproduced. The author's run took about 1 h 20
min (14:18 to 15:39 UTC); the first notebook build failed because nbconvert
was missing from the scratch environment. The notebooks ran in 201 s, 245 s
and 95 s at first and in 421 s, 301 s and 549 s at the end.

The dataset holds 3 neurons recorded with Di-8-ANEPPS (subjects 2, 3 and 4 of
2024-08-06) where the paper reports 8. Every one of its 65 files describes the
session as "without tetrodotoxin (vehicle control)", wording taken from the
tetrodotoxin experiment of DANDI:001271, though the Di-8-ANEPPS experiment had
no tetrodotoxin arm, and the 71 tetrodotoxin sessions of 001271 say it "caused
sustained depolarization", where the paper says it blocked it and the late dF
after tetrodotoxin is -0.38 to -0.70% in all 6 neurons. Amplitudes are given
in volts with inconsistent meaning: 001032 to 001035 call them peak-to-peak,
001030 and 001031 one polarity, and 001272 and 001271 neither, yet all apply
36 V/cm per volt, and the frequency-dependent calibration to the delivered
amplitude is "to be reported separately" and not deposited; with the stated
conversion the mean 2-kHz FluoVolt threshold is about 150 V/cm, against the
paper's 57.7 V/cm. The frames are 16 x 16 pixels where the Methods give 64 x 64
after binning, with no soma ROI, so the paper's ROI cannot be reproduced; the
stimulus onset, waveform and field are not stored other than as text. Frame 0
of every 001272 file is 1.7 to 15.7 times brighter than the median frame, and
33 of 62 intervals between consecutive sessions are under the 20 s the Methods
give (range 4 to 168 s). Across the paper's deposits, all 80 2-kHz unmodulated
files of DANDI:001034 have frame stacks identical to those of 001032 under
other subject names, none of the ten deposits holds the 250-ms sessions in
sodium gluconate behind Figure 3B, and DANDI:001273 lacks the debris ROI, the
pole ROIs and the cell-shape groups of Figure 4, its files forming 22
experiments where the paper reports 19, with dark frames in 164 of 175
replicates. The paper does not say which figure each of its ten dandisets
holds. Questions are put to the paper's authors: whether the soma emission was
taken over the whole 16 x 16 frame, what AP height, baseline and delay count as
an AP and as "delayed" for Di-8-ANEPPS, whether the 001272 amplitudes are
peak-to-peak and what amplitudes were delivered, which trace without APs was
subtracted in Figure 3C, and when the vehicle was added in 001271.

The author's points on the protocol: a claim marked elsewhere whose data are in
no archive cannot be `data_missing`, as the checker rejects it, and `other` was
used; the protocol does not say how far to go on elsewhere claims that are full
targets of their own, such as 001273 and 001274; it does not say whether to add
a reading or ask a reader when a claims file's standard choice proves
unworkable on the data; some criteria do not say whether a pattern is judged
per neuron or in the representative neuron; it does not say whether one
adopted reading must hold across claims; and the format of the questions file
is not specified.
