I wrote the notes to `docs/pilot-notes/xia-2021-01.md` and the summary to `summaries/xia-2021-01.md`; nothing else was changed or committed. `targets/dandisets.json` lists only DANDI dandisets and has no entry for SPARC:75 or SPARC:108. With no `catalystneuro` field to read, the second paragraph does not open with the CatalystNeuro sentence.

# xia-2021, Xia et al. 2021

Four claims reproduced, four partially, three not reproduced and 18
blocked, 16 for missing data, one as `metadata_insufficient` and one as
`not_runnable`; nine outcomes rest on an assumption. The first
verification round agreed with 26 of the 29 outcomes as they stood and the
second with 27; it disagreed on `fig7-peak-timing` and
`figs12-3v-propagation`, a change of the latter to blocked was proposed,
and a third round reviewed that one claim and agreed. Both datasets have
only version 1, which the record pins. The paper, Xia, Yang, Mu, Micovic,
Poskanzer, Monaghan and Clark in PNAS (118:e2023807118), builds a DNA
nanosensor for acetylcholine (ACh) carrying AChE, pHAb and BTX-AF647,
characterises it by HPLC, PAGE and staining, calibrates it ex vivo in the
mouse submandibular ganglion (SMG) and images ACh release in vivo under
lingual nerve stimulation, with vesamicol, and its spread across the
ganglion by AQuA. The claims were written from the version of record and
its SI Appendix, without Movies S1 to S4; the paper links no code and
names AQuA without a version, and the claims check corrected 14 things in
13 claims. Reproduced are the PAGE bands, the BTX staining (by eye), the
peak timing of Figure 7 and the flat AF647 channel. Partial are the HPLC
yield (79.1% under reading (b) only; every usual split of the overlapping
peaks gives 65.8 to 69.1%, and the volumes cannot be tested without a flow
rate), the sensor on the soma (puncta coincide beyond chance but not on
the somata), vesamicol (one experiment of four, reduction 77.8%) and the
rostral to caudal order of Figure 7, which holds in all 18 variants while
none of the six times is within tolerance and the direction rests on the
frame's orientation. Not reproduced are the Michaelis-Menten calibration
(Km 0.031 to 0.73 uM over 80 readings against 49.24 uM), the lower limit
of detection and the in vivo response (dF/F 17.1 to 40.1% against 3.7%).
The control nanosensor, pH, voltage, pulse, repeat, AFM, stability,
two-photon and conjugation claims are blocked for missing data, the
response time for lack of an addition time, and the AQuA comparison
because AQuA is MATLAB with no parameters given. In place of AQuA, Figure 7
was tested with the onsets of pixel blocks. The author's first run gave 3
reproduced, 2 partially, 4 not reproduced and 20 blocked. Round 1 found
the HPLC flow rate picked to put the peaks at the paper's volumes, a
puncta threshold that marked 32 to 48% of the field, rate windows starting
before the responses and the Figure 7 claims testable without AQuA; in
reply the volumes were dropped, three ends of the second peak run, the
threshold replaced, the rates started at each trace's rise, and
fig7-rostral-caudal, fig7-peak-timing and figs12 tested. Round 2 would
have given fig7-peak-timing partial at most, as reading (ii) gives 8.80 s
for the rostral region on the paper's own times; the author kept reproduced, which
the criterion as written allows, and put the reading to a reader in
`questions/xia-2021.yaml`. Round 2 also found sentences the outputs did
not support, on the HPLC tail, the puncta densities and the AF647 trace,
which were corrected. In round 3 the schema did not allow `assumed` on a
blocked outcome, so it was removed from figs12. The author's run took
about 45 minutes (06:49 to 07:34 UTC); two runs of `entry.py` failed for
lack of pyyaml in the author's scratch environment and were rerun with the
system Python, and the notebook ran in 67 to 74 s at first, at about 1.4
GB, and in 122 s at the end.

SPARC:108 holds only part of the paper's data: one of three ex vivo
calibration mice (8 concentrations, none above 714 uM), one of four
vesamicol experiments, the 3 V and 8 V recordings of the AQuA mouse, one
10 V recording, the nanosensor HPLC, UV-Vis and gel files and one confocal
stack. Every control nanosensor recording, the pH calibrations, the 5 V,
pulse-number and repeated stimulations, the AF647 concentration
calibration, the AFM images, the spectra of pure AChE and BTX, the
retention, stability, fiber and two-photon images and two of the three
3 V AQuA mice are not deposited. The imaging recordings do not say which
half of the W-VIEW GEMINI frame is pHAb and which AF647, give no spatial
scale, and record neither the stimulation onset nor the time of ACh
addition, and the files resaved in ImageJ (sub-1, sub-4, sub-6) keep only
the first frame's timestamp; the paper gives the onset only as 10.45 s in
two figures, and sub-4 does not follow it. The timestamps that remain
(sub-2, sub-3) give 0.50 s per frame where the paper states 0.55 s, so
rates differ by 10% between the two. Many pixels saturate at 65535 in the
vesamicol recordings (19.6% of tissue pixels at some frame with the drug,
69.0% after washout) and in the pHAb half of sub-2 and sub-3 (11.5% and
16.4%). subjects.xlsx lists sub-2 and sub-3 as two mice, but they were
recorded 14 minutes apart on one day and show the same field (mean images
r = 0.93). The primary manifest.xlsx describes 40 of its 50 files under
names not in the dataset, seven of the eight calibration files lack the
.tif extension, and the sheet calls the calibration recordings "ACh
release by electrical stimulation". In SPARC:75 50 of the 62 planes of the
high-magnification BTX stack are all zero. Neither dataset names the PNAS
paper: SPARC:108 gives the bioRxiv preprint and SPARC:75 none. In the
paper, Figure S2C labels gel lane 1 as unpurified nanosensor where Figure
2E has the DNA scaffold, and the deposited gel fits Figure 2E. Seven
questions are put to the paper's authors: the frames, onset and baseline
of the initial rate and the times of ACh addition and stimulation; the
ROIs of Figures 5B and 6B and which recordings are the three mice of
Figure 5B; the frame interval; the HPLC flow rate and peak integration;
the frames of the photobleaching fit; the AQuA version, parameters and
areas, and whether rostral is at the top of the frames; and the background
of the puncta threshold.

The author's points on the protocol: it does not say what to record under
`measured` when no reading matches, and the first reading was recorded;
claims judged by eye sit awkwardly with the rule that every result
sentence rests on a printed number, and counts were printed with chance
references; the clock check assumes event times that are not recorded
here, and responses were checked to start after the paper's onset; it
does not say whether a claim with only part of its data deposited should
be tested or blocked, and these were tested with the shortfall as a
deviation; when software cannot run and its parameters are unstated both
`not_runnable` and `methods_underspecified` apply, and `not_runnable` was
used; and the rule to print each file's SHA-256 is in docs/archives.md,
not in the protocol's list of notebook parts.

---

Of the paper's main in vivo findings, the vesamicol block of the nanosensor signal and its rostral to caudal spread across the ganglion held up in part, each in the one experiment or mouse deposited; the spread's timings did not match. The ex vivo Michaelis-Menten calibration and the size of the evoked response did not reproduce: the deposited recordings rise by 17.1 to 40.1% where the paper reports 3.7%, and no file records when stimulation began or ACh was added. The control nanosensor tests ruling out pH effects, and the voltage and pulse dose responses, are untestable, as those recordings are not deposited. The sensor's gel bands and receptor staining reproduced, and its placement on somata in part.
