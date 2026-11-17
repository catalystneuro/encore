# starkweather-2018, Starkweather et al. 2018

Twenty claims reproduced and twelve blocked, all twelve for missing data; two
outcomes rest on an assumption, `fig5e-task1-significant-slopes-unchanged` and
`fig5f-task2-significant-slopes-shift`. The first verification round agreed with
all 32 outcomes, and so did the second; nothing was proposed after the second, so
there was no third round. CRCNS vta-1 is unversioned and is pinned by the MD5 of
data.zip. The paper, Starkweather, Gershman and Uchida in Neuron (98, 616-629),
records light-identified VTA dopamine neurons in mice trained on odor tasks in
which odor A is followed by reward after a delay of 1.2 to 2.8 s, rewarded in
100% of trials in task 1 and 90% in task 2, and inactivates the mPFC with KORD
and SalB. It reports that under saline post-reward responses decrease with the
delay in task 1 and increase in task 2, that SalB flattens the task 2 increase
and leaves task 1 unchanged, that omission responses survive SalB, and it
simulates a belief state TD model intact, with an impaired belief state and with
impaired timing. The claims were written from the version of record with its
STAR Methods and the supplement legends; the PDF could not be rendered, so
numbers printed only inside figures were read from the extracted text. The
paper's code (Starkweather2018 at commit d667730) holds only the model, in
MATLAB, and differs from the Methods in two settings, 10 simulations where the
legends say 50 and every simulation intact where the text says 60% impaired; the
Methods were followed. The reader wrote 31 claims and the claims check added
`figs6ce-kord-task1-animal`. Reproduced are every Figure 4 claim, among them
`fig4a-task1-saline-post-decrease` (F(8, 328) = 12.61, p = 8.4e-16, paper 12.6,
9.1e-16), `fig4b-task2-saline-post-increase` (F(8, 320) = 3.70, p = 0.00038, the
paper's values) and `fig4d-task2-salb-flat` (F(8, 368) = 0.70, p = 0.69), the
Figure 5 slope claims, among them `fig5f-task2-slope-signs` (29, 12 and 24, the
paper's counts exactly) and `fig4e-task2-slope-distribution-shift` (z = 2.15,
p = 0.032, paper 2.1, 0.038), the Figure 6 and Figure S5D omission claims, and
the three model claims, run as a line-by-line Python port of the paper's code, as
MATLAB could not be installed. fig5f-task2-significant-slopes-shift (Fisher
p = 0.0405, paper 0.041) holds only under trial-by-trial baseline subtraction and
gives p = 0.239 under the other readings. `fig7ijk-model-timing-impaired` passes
its criterion, but the omission dips are reduced, not removed (-0.073 and -0.032,
40% and 25% of the intact dips). Blocked are the claims on the mPFC units
(Figure 2, Figures S1E and S6C to S6E), on licking (Figure 3G, Figure S3), on the
unidentified VTA neurons (Figure S4), on the no-KORD controls (Figure S6), and
the four that need free water responses (Figures S5B and S5C and two ANOVAs).
The author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 held that the criterion for fig7ijk is weaker than the
paper's "abolished", that the notebook never printed the zip's member list, that
parts of the two blocked ANOVAs could be run as a deviation, that fig5f rests on
one baseline reading, and that the effect of the 21 untyped trials was not shown;
in reply the dip was tested against zero and the question went to
`questions/starkweather-2018.yaml`, the member list was printed, the partial
ANOVAs were run as deviations that decide no outcome, and the untyped trials were
added as a reading. Round 2 found loose wording on reading (b) of fig7ijk, on
the agreement of p values in the summary, on the Methods' support for the
trial-by-trial reading, and an unprinted runtime in the README, all corrected,
and that the port had not been checked line by line against blur_matrix,
blur_vector and the indexing in simulate; the author made that check and found
no difference, but no MATLAB or Octave run was available to compare traces. The
author's run took about 30 minutes; the notebook ran in 159 s at first, with peak
memory 0.33 GB, 272 s after round 1 and 267 s after round 2. Two errors in
development code were fixed before the final runs, and an empty harness directory
could not be removed for lack of permission.

The dataset holds only the 172 light-identified dopamine neurons of the four KORD
groups (42, 42, 41 and 47), each file with odor_onsets, reward_onsets,
spiketimes and trial_type; data.zip has 173 members, the 172 neuron files and
the directory entry data/. The mPFC recordings, the 761 unidentified VTA neurons,
the 26 neurons of the no-KORD SalB controls, the licks and the free water
deliveries are not in it, so 12 of the 32 claims cannot be tested. No file names
its mouse or recording session; sessions can be recovered as files with identical
odor onset arrays (77 sessions), but mice cannot, so the per-mouse inset of
Figure 5 cannot be repeated. Three pairs of task 1 SalB files share most of their
spikes within 0.5 ms (SalB_Task1_9 and SalB_Task1_10, 99.7%; SalB_Task1_17 and
SalB_Task1_18, 90%; SalB_Task1_36 and SalB_Task1_39, 81%), against at most 1.5%
at chance, so task 1 SalB very likely holds 39 distinct neurons, not 42; the
paper's statistics include all 42, and counting each once changes no outcome. 21
file trials (9 session trials in 8 sessions) are rewarded but have a missing
trial_type, at delays off the 0.2 s grid (1471 to 2421 ms), which the data
description does not mention; kept as odor A trials at the nearest grid ISI,
they change no result. The files give no recording onset or injection time, so
the paper's 40-minute window cannot be applied exactly; the trials of each
session span 23.8 to 38.3 min, consistent with files already cut to that window.
The Figure 4A legend gives a pre-reward window of 0 to 200 ms with F(8, 328) = 15
and p = 3.5e-11, while the Methods give 0 to 400 ms, and the data give F = 9.00,
p = 3.6e-11 with the 400 ms window, as the Results print. Figure 5F prints 9
significant negative task 2 SalB slopes with Fisher p = 0.041, while those counts
give p = 0.037; the data give 8 and p = 0.0405. The claims also record that
F(1, 163) = 2.2 cannot give p = 1.7e-5 for the effect of task on slopes, and that
several legends print F(1, 40) for 47 SalB neurons. A question is put to the
paper's authors: whether the baseline for the single-neuron slopes of Figure 5 is
subtracted trial by trial or as the neuron's mean, as the mean reading gives 3
significant negative task 2 saline slopes (paper 1) and a Fisher p of 0.24.

The author's points on the protocol: "count each recording once" conflicts with
claims whose expected counts include the duplicates; for paper code that cannot
be installed it offers only `not_runnable`, where a small port was possible; the
three model claims are marked `data: dataset` though they use no data; the rule
that a claim holds under any reading conflicts with author step 1.6 on adopting
the best-supported reading; and "pin the most recent published version" does not
fit CRCNS, which has no versions.
