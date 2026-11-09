# 001678, Bell Vila et al. 2026

One claim reproduced (on an assumption), none partially, none not reproduced
and 41 blocked, 29 for missing data and 12 as too large; the three claims that
also use an input from outside the dataset, the finite element model, are
counted apart and are all blocked for missing data. All 45 claims are on the
dandiset. The first verification round agreed with all 45 outcomes, though it
would have blocked the three finite element claims as other and called the
too_large block of the 20-minute neurons weak, and the second agreed with all
45, and nothing was proposed after the second, so there was no third round. It
pins version 0.260227.1824, the only published version; the paper cites none,
and the draft holds the same files. The paper, Bell Vila, Koletar, Dorr,
Trevisiol, Goubran, Sled, Bazzigaluppi and Stefanovic, "Parametrizing
alternating current stimulation for neuromodulation" in Imaging Neuroscience,
records from a 4 x 4 multielectrode array in layer 3 of the sensorimotor cortex
of 22 rats under propofol during sinusoidal alternating current stimulation
(sACS) from subcutaneous pads, in a 1-minute paradigm of 9 rats over 16
combinations of frequency and amplitude and a 20-minute paradigm of 13 rats at
40 Hz and 100 uA, with one sham rat, and reports the electric field from the
stimulation artifact, a finite element model of it, firing rate and entrainment
(sqrt|PPC|) of sorted neurons, and LFP power and phase-amplitude coupling. The
claims were written from the version of record in Europe PMC (PMC12779756) with
the supplementary material, and from the paper's code
(m-bellvila/Parametrizing-alternating-current-stimulation-for-neuromodulation
at commit 3b89bf2); the check made eight corrections and left three points
open. Only `efield-20min-median` was tested. Its median over rats of each
rat's mean field is 1.834 mV/mm and the median of all 117 estimates 1.525, both
within 1.65 +/- 0.21, on the assumption that channels aw_1 to aw_16 sit row by
row in the grid; the files give no electrode positions and the maker's map is
not published, at most 1.35% of 2000 random layouts are as smooth in any rat,
and a serpentine order gives the same outcome, while over all 2000 random
layouts reading (a) is within tolerance in 18% and (b) in 43%. Reading (ii),
the largest pair per axis, gives 3.698, outside, and the criterion takes one
matching reading although the claims file's opening comment blocks a claim
whose readings disagree. The 1-minute claims, the electric fields of the
1-minute trials and both sham claims are blocked because the data are not in
the dandiset, the finite element claims because the Sim4Life software and the
ViZOO rat model are not public, and the 20-minute spike claims, with the eight
power and coupling claims whose channels are chosen by those neurons, as too
large: loading and sorting the 13 rats takes about 85 minutes at the speed
measured on one full rat, over the 60-minute limit. The author asked no
questions of a reader, so the answer and author-answers runs changed nothing.
Round 1 found that the timing estimate of 52 minutes contradicted the block,
that the layout matters and the maker's map was not sought, that the
per-electrode variant used only 9 electrodes, that some channels' artifact was
not stable over the 20 minutes, and that `fem-depth-falloff`, a ratio, does not
depend on the 1-minute fields; in reply the extrapolation was replaced by a
timed sort of one rat (sub-2023-04-28) over its whole 49.3-minute window, the
map was searched for, and the random layouts, bootstrap intervals (1.310 to
1.777 for (b)), an all-16-electrode variant (1.748 and 1.650) and the field
without the 14 unstable channels of 208 (1.834 and 1.695) were added, and the
conflict between the claims file's header and the criterion was filed as a
question in `questions/001678.yaml`, after the reader's run. Round 2 found that
the prose gave 98 minutes, 9.2 s per minute and 26 units where the notebook
printed 68 minutes, 6.4 s and 27, asked that the reason say the block is narrow
and depends on the machine, and found the statement that the stream is not
notch-filtered at 60 Hz unsupported for sub-2023-05-04 and sub-2023-05-05; all
were corrected, and the record now says the block holds
by 8 to 25 minutes for the sorting alone. SpyKING CIRCUS 1, which the paper
used, needs an MPI library that is not available, so SpyKING CIRCUS 2 was used
for the timing. One early bug in the onset detection, which shortened two
rats' stimulation periods, was fixed before the final runs, and nothing else
failed; the notebook took 8 to 9 minutes at first, 502 s after the
author-answers run, 731 s after round 1 and about 12 minutes at the end.
Untracked items at the repository root (`.bashrc`, `.gitconfig`, `scripts`,
`.idea` and others), which the author did not create, were left alone.

The 9 files of the 1-minute paradigm hold only the stimulation command channel
('S1r 1', the TDT stream uS1r), one series per trial, so the multi-unit
recordings, the LFP and the stimulation monitor that the paper analysed are
not in them and none of the paper's 1-minute findings (the parameter
exploration, Tables 1 to 3, Figures 3 to 10) can be tested. No file holds
sorted units, although the paper's results rest on SpyKING CIRCUS output; the
20-minute recordings could be sorted again, but the published spike times would
make the 20-minute findings testable. The sham recording (one F344 nTg female
rat, 80 minutes under propofol) is not in the dandiset, and Science Data Bank
(doi 10.57760/sciencedb.32375), which the paper names for its data, answers
PERMISSION NO ACCESS without a login. Every series is labelled in volts with a
conversion of 1e-6, while the 1-minute values are the stimulation current in uA
(peaks of 49.98 to 399.87 for 50 to 400 uA) and the 20-minute values are
already in volts, so the conversion would make them a million times too small.
The 20-minute stream (channels 'aw_ 1' to 'aw_ 16', 12207 Hz) matches neither
stream of Methods 2.3: it has the LFP's rate but is not low-passed at 300 Hz
and carries spikes, and in 8 of 13 rats the 60 Hz line stands 10 to 1099 times
above its neighbours, so these are not notch-filtered, while in the other five
the ratio is 1.0 to 9.6 and a notch cannot be ruled out; the files and the
description do not say which TDT stream it is, and the description gives 24
kHz for all data. The electrodes table has no positions (location 'unknown'),
so the 4 x 4 layout the field estimate needs is not documented, the 20-minute
files have no epochs or stimulation times, so the stimulation is found only
from its artifact, and session descriptions are empty. The paper gives 20
trials per 1-minute rat where the files hold 15 to 23 (185 in all), with
repeats of some combinations, three rats missing some of the 16 analysed
combinations (one lacks all four at 400 uA) and one trial at 100 Hz and 20 uA
outside the paper's design, and which trials the paper analysed is not
documented. The 20-minute subjects are 6 male and 7 female in the files where
Methods 2.1 say 7 male and 6 female; the 1-minute subjects (4 male, 5 female)
agree with the paper. Questions are put to the paper's authors on the electric
field estimate of Methods 2.8: the 4 x 4 layout of channels 1 to 16, how the
differences along the two axes are paired for the vector addition, over which
set Grubbs' test is applied, and whether the reported median of 1.65 +/- 0.21
mV/mm is taken over rats or over all channel-pair estimates, and what the +/-
is.

The author's points on the protocol: the claims file's opening comment blocks a
claim whose readings give different outcomes while the field criterion says one
matching reading reproduces it, and the criterion was followed; a too_large
block needs a timing while numbers in the record must come from the notebook,
so the timing run was put in the notebook; the protocol does not say whether a
sorter may write working files, and the sorter wrote only its own output to a
temporary directory; results cannot pass between notebooks, so the sorting
could not be split to fit the 60-minute limit; it does not cover a claim with a
1-minute and a 20-minute part, so baseline-fr and baseline-ppc were given
data_missing with too_large in the notes; and the newest example record follows
an older protocol version (pilot-5), so pilot-13's text was followed.
