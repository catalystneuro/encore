# 000945, Ramachandran et al. 2025

One claim reproduced, one partially, 11 not reproduced and nine blocked. The
first verification round agreed with 17 of the 22 outcomes and the second
with 20, and a third round, held on the two changes of outcome proposed after
the second, agreed with both. It pins version 0.250213.2212, the version the
paper cites; all five published versions hold the same 75 files. The paper,
Ramachandran, Gao, Yttri, Yu and He in the Journal of Neural Engineering,
records sorted units in S1 of awake, head-fixed rats with a chronic
32-channel array during transcranial focused ultrasound, sorts them into
regular spiking (RSU) and fast spiking (FSU) units by k-means on two waveform
durations, and compares time-locked and delayed responses across pulse
repetition frequency (PRF), duty cycle (DC) and isoflurane anesthesia, with a
sham aimed off target. The claims were written from the version of record in
Europe PMC (PMC11920894), without the supplementary materials, and the paper
links no code. 13 claims were tested on the dataset's own cell-type labels;
`fig3-cell-type-sorting`, `fig4-rsu-time-locked-both-states`,
`fig5e-rsu-delayed-prf-awake`, `fig6ad-time-adjacent-batch`,
`fig7a-rsu-time-locked-dc` and `fig7c-rsu-delayed-dc` are blocked as
`data_missing`, for want of waveforms, the sham, the second batch of rats or
the DC series' own 30% recordings, and `fig4h-awake-latency-wider`,
`fig6ef-rsu-ispta-rise-then-fall` and `sham-no-auditory-response` as
`methods_underspecified`, the first two because the claims file's readings
disagree. `delayed-anesthesia-factor` reproduces on an assumption of one
recording per rat and condition, the anesthetized mean being lower for RSU (p
= 4.2e-09 to 1.8e-08) and FSU (p = 0.0012 to 0.0015); with every recording
FSU gives p = 0.038 to 0.041 and the claim is partial at best.
`fig7d-fsu-delayed-dc` is partial, 60% being above 6% (corrected p = 0.015)
with both below baseline (99.6% and 98.2%) and the sham part untested. Among
the not reproduced, the highest time-locked RSU mean is at 3000 Hz (107.7 to
108.7%), not 1500 Hz (98.1 to 98.7%); anesthesia raises the time-locked RSU
response (102.6 to 102.9% against 100.1 to 100.4%), and with only BH498 and
BH512 the effect disappears (p = 0.425); FSU time-locked responses differ
across PRF (Kruskal-Wallis p = 1.8e-12 awake, 5.5e-04 anesthetized); no
reading gives awake FSU latencies later at p < 0.001 (p 0.018 to 0.92); and
at 6% DC the time-locked RSU mean (176.3 to 180.8%) is above that at 60%
(147.1 to 147.5%). The author's first run gave 2 reproduced, 2 partially, 15
not reproduced and 3 blocked. The author asked a reader no questions, so the
answer run and the following author run changed nothing. Round 1 disagreed
with fig3, which it gave as blocked since both outcomes of its criterion need
the waveform clusters, with fig4h and fig6ef, where the notebook had adopted
one reading against the claims file's rule for disagreeing readings, with
fig7c, decided by substitute 30% recordings, and with fig7d, reproduced with
an untested sham part; it also found that the recording dates of the repeat
recordings were never printed and that the anesthetized cell-type tests rest on two
rats. In reply the dates were printed, which showed three of the ten `_2`
recordings to start before their pair, a reading keeping the earliest of each
pair (Rep3) and one with no 30% group (C0) were added, and fig3 was given a
base rate. Round 2 disagreed with fig5e and fig7a, which could still be
partial if the untested sham or 30% parts held, and found sentences the
outputs did not support (twelve second copies where there are eleven, spike
counts said to match in every pair, and substitute dates true only of the
same rats' recordings), which were corrected; the author added the Rep1
result without the doubly filed recording (FSU p = 0.048 to 0.052) but kept
it as partial, as the RSU part holds alone. The author proposed blocked for
the two, and round 3 agreed. The author's run took about 23 minutes (21:25 to
21:48 UTC) and nothing failed; the helper was later fixed to decode start
times stored as arrays in the unlabelled anesthetized files. The notebook ran
in 60 s at first, 64 s after the answer, 92 s after round 1, about 90 s after
round 2 and 56 s in the last run.

The sham condition and the second batch of five rats are not in the
dandiset, and only part of the first batch is: the awake PRF series covers
seven rats, the anesthetized PRF series three (BH498 at five PRFs, BH512
without 30 Hz, BH521 at three PRFs, unlabelled) and the awake DC series three
rats at 6% and 60% only, where the paper describes ten rats for each series.
The DC series' own 30% recordings are missing; the only 1500 Hz, 200 us
recordings are the PRF series', those of the same rats made three to five
months earlier and those of the other rats from August 2023 to 6 March 2024.
The files hold no waveforms, voltage traces or electrode positions, so the
cell-type sorting cannot be repeated or checked; with the deposited labels
two of 59 recordings match the paper's counts, against 3.84 expected by
chance, and FSU have the higher median baseline rate in 46 of 59 labelled
recordings. The labelled anesthetized units come from two rats, so state and
PRF effects there are partly rat effects. Eleven files are second copies of
other recordings: the five anesthetized BH498 recordings are deposited under
BH498 without labels and under subject folder BH497 with labels, four
anesthetized BH512 recordings under BH512 without labels and under BH514
with labels, BH512_1500_200_anes2 is a third copy sorted differently and
dated two months later (spike counts 905,554 against 926,883), and
BH498_30_200 and BH508_30_200_2 share all 203 trial times and 18,860 spike
times, with session start times 6.5 hours apart, so which rat that recording
belongs to cannot be established. The description says the repeat
recordings were "taken a few months after the original ones", but three of
the ten `_2` recordings start before their unsuffixed pair. The labelled
copies of anesthetized recordings are described as "Awake S1 Stimulation by
tFUS", every file gives the age P24W where the paper gives 7, 9 and 10 months
and the description 8 to 10 and 12 months, and electrode columns carry
placeholders ("my description", "brain area"). PRF, tone-burst duration and
anesthesia state are coded only in the identifier, the trial table's
stop_time (always 2.2 s after start_time) is not described, and the files do
not say which 500 of the 505 trials delivered they hold. Fifteen anesthetized
files have no cell-type labels, among them all of BH521's and BH512's DC
recordings, and five recordings hold fewer than 500 trials (203, 238, 328 and
339). Only 10 of 64 recordings show a population rise in the 67 ms
time-locked window. Questions are put to the paper's authors: whether the
repeat recordings were part of the analysis, and if not which of each pair
was; whether a window off the 35.7 ms bin edges was measured from exact spike
times or from the overlapping bins; and whether the first latency bin allowed
after the 67 ms of ultrasound is the first starting at or after 67 ms or the
first ending after it.

The author's points on the protocol: fig3's criterion has no branch for
counts that match while the feature part cannot be tested, and blocking it
would block every claim that uses cell types by the dependency rule, so the
first run gave it as partial; the claims file's header covers a missing
anesthetized sham but not the awake one, and the same rule was applied as a
deviation; step 1.6 covers readings for gaps in the paper but not choices the
dataset forces, such as the repeats and the missing 30% recordings, and every
reading was run with one adopted as an assumption; fig4h's criterion asks for
every reading while step 1.6 says to adopt the best-supported one, and the
criterion was followed; and nothing covers recordings with fewer trials than
the paper describes, which were used as they are with a finding.
