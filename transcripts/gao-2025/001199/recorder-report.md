I wrote the notes in `docs/pilot-notes/001199-gao-2025-01.md` and changed no other file. Nothing is committed. The working tree already had untracked files at the repository root (`scripts`, `.idea`, shell profiles and others) before I started; they aren't mine, and I left them alone.

# 001199, Gao et al. 2025

No claim reproduced, none partially, three not reproduced (one on an
assumption) and 32 blocked, all 32 for missing data. The first verification
round agreed with 32 of the 35 outcomes as they stood and the second with 34,
and the second revision proposed one change, so a third round reviewed it and
agreed. It pins version 0.250829.1250; all four published versions and the
draft hold the same 229 files and differ only in contributor order. The paper,
Gao, Ramachandran, Yu and He, "Transcranial Focused Ultrasound Modulates
Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively
Activating Excitatory Neurons" in the Journal of Neuroscience, steers 1.5 MHz
ultrasound to S1 in anesthetized rats while recording S1 and POm, and S1 and
auditory cortex (AC) in a second group, with two 32-channel probes, and sorts
units into RSUs and FSUs from their waveforms across series of PRF and duty
cycle; the dataset holds sorted spike times and trial tables from 13 rats. The
claims were written from the version of record as served by PubMed Central,
which has no supplement; the paper links no code, and its Methods name
dandiset 000946 as the repository of all its data. `subjects` is not
reproduced: 6 rats have simultaneous S1 and POm recordings (paper 16) and 6
have S1 and AC (paper 12), under every reading, and the rats cannot be a subset
of the paper's, every S1 file listing a 64-channel A1x64-Edge probe (or H9),
two rats (BH648, BH658) being in both groups and none of the ten being in
000946. `fig4-unit-counts` is not reproduced on upper bounds from untyped
units: in the claims file's sessions at most 4 of the 8 counts can be within
10%, where a partial result needs 6. `fig11b-ac-responses` is not reproduced
on the assumptions that the 2025 sessions were at 5 V and that their trial
starts are the sonication onsets: 194 AC units in 7 rats (paper 453), no
Kruskal-Wallis test significant at 0.01 (p 0.013 to 0.74), only 1,500 Hz during
sonication significant and only under R1 and T2, and no PRF above baseline
after sonication. The other 32 claims are blocked as `data_missing`: 17 on RSUs
and FSUs for want of waveforms or type labels, the duty-cycle series of
Figures 7 to 9 and 10D to 10F, the raw voltage of Figure 2, and
`fig5-unit-counts` and `fig5b-cg1-control-no-response` for want of a CG1
control at 3,000 Hz. The author's first run gave `subjects` as partially
reproduced, `fig11b-ac-responses` as not reproduced and 33 blocked. The author
asked a reader nothing, so the answer and author-answers runs changed nothing.
Round 1 disagreed with `subjects`, `fig4-unit-counts` and `fig5-unit-counts`,
which moved to not reproduced, gave `metadata_insufficient` for 17 blocked
claims, and asked whether the 2025 trial starts are onsets; in reply the main
counts were restricted to the 5 V files plus every 2025 file, the "none extra"
evidence was printed, and a lagged correlogram and an untyped S1 positive
control were added. Round 2 withdrew `metadata_insufficient`, disagreed with
`fig5-unit-counts`, since CG1 sessions at 300 and 4,500 Hz cannot bound control
sessions at 3,000 Hz that were not deposited, asked that `fig11b-ac-responses`
be marked assumed and that the T2 rise of 2025 S1 units be reported, and found
sentences the outputs did not support (the 4,224% rate, the places out of order
per unit, the files with 400 and 149 trials, a delayed rise from about 125 ms,
the BH594 counts at 10 and 15 V, the R2 means without BH654), all corrected or
printed. The second revision proposed `blocked` for `fig5-unit-counts`, and
round 3 agreed, noting that `fig5b-cg1-control-no-response` is the direct
parallel and `fig7-9-unit-counts` not quite one. The author's run took about
50 minutes (08:59 to 09:48 UTC) with nothing failing, an early bug on unsorted
spike times having been fixed; the notebook ran in 205 s at first, 94 s after
the author-answers run, 133 s after round 1, 116 s after round 2 and 147 s at
the end. `tools/build_site.py` and `tools/site_assets/progress.js` were found
modified and left untouched.

The dandiset names the paper as the description of its data, but its 13 rats
were recorded from August 2024 to July 2025, after the paper's preprint of June
2024, and of them only BH594 has a file in dandiset 000946, which lists 20 rats
recorded from August 2023 to April 2024; it also holds conditions the paper does
not describe (10 and 15 V, stimulation at POm, 64-channel probes with and
without z-coating, 2 mm offsets). The files hold spike times only, with no
spike waveforms and no RSU or FSU labels, so the paper's typing of units cannot
be repeated, and of the 20 claims on RSUs and FSUs 18 cannot be tested. The
units column celltype_label is described as "label 1 = RSU, label 2 = FSU", but
no file holds a 1 or a 2 (1,272 units labelled 0, 414 POm and 773 S1): it holds
0 in the 49 files of BH590 and BH594 and the area of the unit in the 47 files of
BH596 and BH615, and the 133 files of the 2025 cohort have no such column. Every
stimulated file has a pulse duration of 200 us, so the duty-cycle series are
absent, as are the target-determination trials and raw voltage of Figure 2 and
a CG1 control at 3,000 Hz (CG1 sessions are at 300 and 4,500 Hz). In the 2025
cohort, which holds every AC recording, the spikes lock to the trial starts no
more than to starts shifted by 1.25 s (true above shifted in 7 of 108
stimulated files), and the population correlogram peaks within 0 to 400 ms of
the trial start in 4 of 108 stimulated files, against 39 of 92 in the 2024
cohort, with no other lag within 60 s at which the files lock; untyped S1 units
of the 2025 cohort show a weak rise at 30 and 1,500 Hz (means 107 to 109%), so
some sessions lock, and for the others the files cannot tell missing responses
from trial times that are not onsets. The data_collection field gives
"PRESSURE:67V" in most 2024 files whatever voltage the identifier gives (the 67
is the ultrasound duration), and the 2025 files state no pressure or voltage
anywhere. The stimulation targets "S1-6", "NEW", "y-1" and "SEP" and the
identifier tags of the 2024 files are explained nowhere, and electrode
locations are "unknown" in every file. In the 2025 cohort session_start_time
does not date the session, two probe files of one session having start times
minutes apart and the BH608 sham pair five months apart (2025-02-06 and
2025-07-11), and one file is named ses-None; in the BH608 30 Hz session the S1
file gives stimulation at S1 and the POm file, sharing its trial table, at
"SEP". In 64 units of 16 files of the 2025 cohort the spike times are not in
increasing order (one to seven places per unit), and they are sorted on
reading. The files sub-BH646_ses-None and sub-BH646_ses-20250308T003900 hold
the same recording (AC at 30 Hz). The S1 files list 64-channel A1x64-Edge
probes where the paper used two 32-channel A1x32-Poly3 probes, four BH590 files
name a device "H9", and the description gives 500 trials per recording where
most files hold 499 and some 113 to 480. No question is put to the paper's
authors, every reading giving the same outcome; the data owners could state the
voltage and the trial timing of the 2025 sessions.

The author's points on the protocol: it has no rule for a dataset that may not
hold the paper's data when the paper names another dandiset, and 001199 was
tested as the claims file says with the mismatch recorded as a finding; step
1.4 does not say whether another dandiset's file list may be read just to
identify rats, and 000946's asset paths were listed under `inputs`; with
waveforms absent and the label column mislabelled the claims could be
`data_missing` or `metadata_insufficient`, and `data_missing` was chosen; it
does not say how a failed clock check bears on a claim whose result is an
absence of response; "none extra" in the subjects criterion cannot be checked
without the paper's list of rats; the claims file's Bonferroni factor B1 is
ambiguous, and factors of 5, 10 and 15 were run; and it records format errors
without saying whether to repair them, and the spike times were sorted.
