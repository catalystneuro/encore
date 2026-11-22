I added the two new files and changed nothing else. The summary is 116 words, nothing was committed, and no em dash or "rather" appears in either file. The `catalystneuro` field for 000009 is empty, so the second paragraph does not open with the CatalystNeuro sentence. The README row puts the link claim and the 24 simulation claims outside its counts, so the notes say so.

`docs/pilot-notes/lakshminarasimhan-2024-01.md`:

# lakshminarasimhan-2024, Lakshminarasimhan et al. 2024

No claim reproduced on the dandiset, one partially, four not reproduced and six
blocked, all six for missing data; the link claim `wm-sessions-link`, partially
reproduced, and the 24 claims on the paper's model simulations (`data:
elsewhere`), 23 blocked as `too_large` and `figs5cd-thalamic-recurrence` as
`methods_underspecified`, are counted apart. No outcome rests on an assumption.
The first verification round agreed with 34 of the 36 outcomes as they stood
and the second with all 36; nothing was proposed after the second, so there was
no third round. The dandiset is pinned at 0.220126.1903, the only published
version; the paper cites none. The paper, Lakshminarasimhan, Xie, Cohen,
Sauerbrei, Hantman, Litwin-Kumar and Escola, "Specific connectivity optimizes
learning in thalamocortical loops" (Cell Reports 43, 114059), models a cortical
network that learns through plastic thalamocortical synapses and reports that
corticothalamic weights aligned with the cortical readout help in motor control
and weights aligned with the leading cortical PCs help in working memory; it
checks the prediction on the reach-to-grasp recordings of Sauerbrei et al.
(2020) and on the ALM and thalamic recordings of Guo et al. (2017) in a delayed
response task, which are DANDI:000009. The claims were written from the NIH
author manuscript (PMC11104520) with the supplement legends, without rendered
figures, and from the paper's code at commit 2aa94dd, which holds the motor and
reaching simulations only, with no working memory task, no meta-learning and no
analysis of the neural data; the claims check corrected ten things and added
four claims, for 36. The link is partial: mouse anm00264943 holds the paper's
151 ALM and 72 thalamic units exactly, but in eleven sessions, five ALM and six
thalamic, where the paper says five. Not reproduced are the choice readout from
ALM (test-set R2 -1.705 on the first reading and at most -0.247 against 0.97),
the thalamic variance explained by ALM (-2.068 against 0.70), the fraction
captured by the top 5 PCs (0.040 against 0.63, and no reading within 0.59 to
0.67) and the Figure S6F alignment test, whose difference the paper calls not
significant and which here gives p = 8.3e-06. The leading-PC claim of Figure 6C
is partial: both readings hold for the pooled readout, only one for the
per-session readout, by a margin of 0.0003, and the leading PCs carry less of
the readout than a random direction would. The six motor task claims are
blocked because the Sauerbrei et al. (2020) data are not deposited; the
simulation claims were timed with the paper's motor control model, and one set
of 40 runs at M = 1 takes 0.98 h on one core in the final run, so none fits in
the notebook's hour. The author's first run had the link and the Figure 6C
claim reproduced. Round 1 found that the session count was never checked and
the "sessions holding both: 0" line was hard-coded, that the leading PCs fall
below chance, that the Figure S6F test compares alignments with different
chance levels, and that the simulation timings were inflated by the first call;
in reply both claims moved to partial, and noise ceilings, larger test sets and
chance levels were added as diagnostics. Round 2 found the simulation timings
stale again, since they vary between runs (5.3 ms per trial at M = 1 in the run
it read, 8.8 ms in the final run), called fig3ab's `too_large` thin at four
cores, and found summary sentences the outputs did not support, all corrected.
The author's run took about 45 minutes (15:26 to about 16:10 UTC); a signed S3
URL refused a HEAD request and an alignment profile broke for sessions with
fewer than 16 units, both fixed before the final run. The notebook ran in 8
minutes at first, with peak memory 0.95 GB, 13 minutes after round 1 and 14.0
minutes at the end.

The units tables give no interval over which each unit was recorded, though
many units fire in only part of their session: in the paper's mouse only 61%
of the pairs of a unit and a correct trial without photostimulation fall
between the unit's first and last spike, and in one thalamic session the
median unit spans 56% of the trial period, so trial averages over all trials
include trials in which a unit may not have been recorded; the analysis was
run both ways, with the same outcomes. No session holds both ALM and thalamic
units, so how the paper paired the thalamic units with ALM activity for its
training and test sets is not stated, and the Methods' "5 behavioral sessions"
match the five ALM sessions. The electrode group location gives the ALM
coordinates (AP 2.50, ML -1.50, DV 0.00 from bregma) in all 137 extracellular
files, including the 72 thalamic and 18 SNr recordings; the thalamic files name
no nucleus (VM and VAL in the paper); the trial columns type, response,
photo_stim_type and photo_stim_period have no description, and photo_stim_type
is "stimulation" on every trial; and eighteen files from three mice are
labelled SNr, which the dandiset description does not mention. No spike train
or trial table among the 1,936 units and 137 files is deposited twice, and
choice decoding rises in the delay and after the go cue in all eleven sessions
of the mouse, consistent with spikes and trials sharing a clock. With OLS on
trial averages as the Methods describe, the test-set R2 values are negative
while the training-set values are close to the paper's (choice 0.95 to 1.00,
thalamic 0.74, top-5 fraction 0.68), and with 10% test sets the thalamic
test-set averages are mostly noise (reliability at most 0.28). Questions are
put to the paper's authors: whether the working memory R2 values are in-sample,
how the thalamic units were paired with ALM activity, which trials each unit
was averaged over, what smoothing grid was searched, which of the three Figure
6D normalizations was used, and what recurrent thalamic weights Figure S5C and
S5D used.

The author's points on the protocol: `data: elsewhere` is written for data in
another archive, and the claims on undeposited model output were treated as
claims to run, timed with the paper's model and blocked as `too_large`; it
does not say how to judge a link that holds for the unit counts but not the
session count; for a claim of absence it does not say which of the criterion's
readings decides, and the main reading was chosen from the cited passages; it
has no place for a diagnostic that is not a reading of the claim, such as the
training-set R2, shown as a labelled variant; five seeds over every combination
of readings multiply the runtime, and only the main combinations were run under
the other four seeds; timings change from run to run while the record may only
use printed numbers; and the example record predates the `severity` field,
which was taken from the schema.

`summaries/lakshminarasimhan-2024-01.md`:

None of the paper's working memory findings held up in this data: ALM activity did not predict the mouse's choice on held-out trials (test R2 at most -0.247 against 0.97) or explain thalamic activity, and the top five cortical PCs did not capture most of the thalamic variance. The same fits come close to the paper's values on the training trials, so the paper's numbers may be in-sample, a question put to its authors. The leading cortical PCs drove the choice readout under only one of two readouts. The motor control findings could not be tested, as those recordings are not deposited. The model simulations of Figures 1 to 5 were too large to run here.
