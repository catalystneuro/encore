# 001516, Semenov et al. 2026

No claim reproduced or partially reproduced, one not reproduced and 23 blocked,
all for missing data; the eight claims that also use an input from outside the
dataset are counted apart and are all blocked for missing data.
All 32 claims are on the dandiset. The first verification round agreed with all
32 outcomes as they stood and the second with all 32, and nothing was proposed
after the second, so there was no third round. It pins version 0.261006.1833,
the only published version; the paper cites none. The paper, Semenov,
Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov and Pakhomov,
"Sub-microsecond optical measurements of cell membrane charging and lesioning by
pulsed electric fields" in Bioelectrochemistry, images CHO cells stained with
the potentiometric dyes Di-8-ANEPPS and FluoVolt during 1-us and 0.3-us pulses,
measures the charging at the anodic and cathodic poles as the field is raised
(Figs. 1 to 4), its change with Gd3+ and a conductivity calibration by Eq. (2)
(Fig. 5), Fluo-4 calcium responses (Fig. 6) and membrane recovery by a two-pulse
protocol at a 5-us interval (Fig. 7). The claims were written from the version
of record, from a PDF supplied by a person, without opening the figures; the
paper has no supplement and links no code, and the claims file follows the
checked file for the same paper on dandiset 001517, with one claim added for
the Fig. 7A profiles. The only claim that could be tested is
`fig5b-conductivity-calibration`, which uses no recordings: Eq. (2) with the
constants of Methods 2.3 gives a 1.33% IMP reduction for a 10-fold rise in
conductivity (1.20% relative to the intact membrane), outside 2 +- 0.2%, while
the 100-fold value of 11.87% is within 12 +- 1.2%. The other 31 claims are
blocked because the dandiset holds none of the paper's experiments; the
notebook measures the dataset's own sets with the paper's pole method as
variants that decide nothing, and on them the criterion of
`fig2a-fluovolt-stable` would give not reproduced. The author's first run gave
the same outcomes. The author asked no questions of a reader, so the reader's
run and the author-answers run changed nothing. Round 1 agreed with every
outcome and found that the claims file's header assumes from the dandiset's
title that the data are the Fig. 7 experiment, that the notebook header misdescribed Fig. 3,
that fig2a-fluovolt-stable could be run as a variant, that F0 included the
dimmed frame 0, that the field direction was taken from the response it then
measures, that the amplitude-to-field mapping cannot be checked, and that no
overlay of the traces on the images was shown; in reply the header premise was
sent as a question to a reader in `questions/001516.yaml` without changing the
claims, the variant was added, frame 0 was left out of the baseline, the
direction was taken from the other pulse sets of each field of view (it moves
by -0.4 to 0.7 degrees), and the overlay was added, which showed that touching
pairs of cells in c2, c3 and c10 and a stacked pair and a cluster of dim cells
in c11 had each been measured as one cell, so touching cells were split and
objects that are not round left out, giving 29 cells in place of 30. The author
also looked at Fig. 5B by eye in that revision and wrote in the record that the
curve passes close to the printed points. Round 2 agreed with all 32 and found
sentences the outputs did not support (the first frame of every set said to be
dimmer where only the median was printed, now 65 of 72 files with a range of
0.52 to 1.11, the 12-point and 16-point falls given as first against last 10
frames, the touching cells listed differently in two cells, the by-eye reading
of Fig. 5B, and round-1 cell numbers that had moved), all corrected, the by-eye
sentence being removed. The author's run took about 30 minutes (20:14 to 20:43
UTC) and nothing failed; the notebook ran in 78 s at first, 73 s after the
author-answers run and 75 s after round 1.

The dandiset holds none of the recordings behind the paper's figures. Its 72
files are one FluoVolt experiment of 2023-06-22 in 12 fields of view, single
1-us pulses (2 fields) and pulse pairs at intervals of 1, 5, 25, 125 and 250 us
(2 fields each), at 150 to 1570 V/cm; the paper's Di-8-ANEPPS escalations, its
FluoVolt escalation, the Gd3+ experiments, the Fluo-4 calcium imaging and the
Di-8-ANEPPS two-pulse recordings at a 5-us interval are absent. Dandisets 001517
and 001518, titled as Di-8-ANEPPS and dye-comparison experiments of the same
lab, are separate targets and were not used. The dandiset's metadata names the
paper as the publication of its data, but the paper reports no FluoVolt
two-pulse experiment and no interval other than 5 us, and its Discussion names
varying the interval as future work; the files also give 1.00-mm electrode
spacing against the paper's 1.6 mm, and 20 sham and 40 pulse frames per set
against 40 and 60. The general description in every file lists the intervals
as 1, 5, 25 and 125 us, but fields of view c5 and c12 hold pairs at 250 us. The
ImageSeries starting_time holds the Unix time of each set's acquisition
(1687481119 to 1687486631 s), the same instant as session_start_time, so every
recording starts about 53 years after its session. The pulse protocol of each
set is only in the free text of session_description, with no stimulus or trial
table and no frame labelled as sham or pulse (the data confirm 20 sham frames,
then 40), and the field direction, the pixel size and the imaging delay per set
are not recorded, so no radius in um can be had. The amplitudes are given in
volts (50 to 250 V) and the field strengths 0.15, 0.52, 0.9, 1.27 and 1.57 kV/cm
are listed without a mapping; read in order they are not proportional to
voltage (5 times the voltage for 10.5 times the field), while the paper states
that the current scaled linearly with voltage. The 12 subjects are fields of
view holding several cells, some touching (29 whole, round cells, 2 or 3 per
field of view, are measured), and the files do not say which was the
experiment's cell, where the paper reports one cell per experiment. Subject
metadata describe a cell line as an organism, with age P1D and sex U, and the
archive's summary gives the species as "Cricetulus griseus - Cricetulus
aureus" for NCBITaxon_10029. On the cells, the 40 frames after the sham frames
are 13.3 to 16.2% dimmer than sham frames 1 to 19 in the sham sets with no
pulse, the per-frame pole dF falls within the sham sets (by 12.1 and 12.2
points between pulse frames 20-29 and 50-59, and by 15.9 and 16.3 points
between baseline frames 1-9 and 10-19), and in 65 of the 72 files the first
frame is more than 10% dimmer than frames 1 to 19 (median 0.64); this uniform
offset enters the paper's collapsed dF measure at both poles. Of the paper
itself, Results 3.5 states that a 10-fold rise in effective membrane
conductivity yields a ~2% IMP reduction by Eq. (2), but Eq. (2) with the
constants of Methods 2.3 gives 1.33%, and a 2% reduction needs a 15- to 16-fold
rise.

The author's points on the protocol: it has no case for a dataset that holds a
different, unreported experiment, so every recording-based claim was blocked as
`data_missing` and the dataset's own sets shown as variants; it does not say
how a claim that needs no data counts toward the dataset, and fig5b was tested
with a note that it is independent of the data; step 2 asks to align data with
trial tables where there are none, and the contrast between sham and pulse sets
at frame 20 was used instead; there is no prescribed place for analyses of data
that are not the paper's, and they were put in an untagged section after the
claim sections; it is unclear whether `elsewhere` covers sibling dandisets on
the same archive, and `data_missing` was kept with 001517 and 001518 named in
the notes; and docs/archives.md says to read files with `pynwb`, where `h5py`
was used for the one ImageSeries.
