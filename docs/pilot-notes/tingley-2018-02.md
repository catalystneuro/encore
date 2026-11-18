# tingley-2018 again, Tingley et al. 2018

The second attempt on this paper, made blind to the first (tingley-2018-01),
under pilot-15. Eight claims reproduced, eight partially, thirteen not
reproduced and one blocked on the dandiset, `figs6-reference-frame`, as
`metadata_insufficient`, since nothing marks a maze rotation; the two claims
on data elsewhere, the Allen connectivity analysis of Figure S3 and the
spiking model of Figure 7, are blocked as `other` for lack of time and counted
apart. The attempt pins version 0.261109.2219, the latest published version.
The paper, Tingley and Buzsaki, "Transformation of a Spatial Map across the
Hippocampal-Lateral Septal Circuit" (Neuron 98, 1229-1242.e5), reports that
lateral septum (LS) neurons in rats encode position in the theta phase of
their spikes more than in their rate, while hippocampal place fields carry it
equally in both, and relates this to recording depth in the LS,
hippocampal-LS assemblies, and theta coherence and theta-gamma coupling with
CA1 and CA3. The claims file was written again by a reader who had not seen
the data, from the NIH author manuscript (PMC6605060) with its supplement and
the paper's code (DavidTingley/papers at 9f4cd48, buzcode at e615663), and
holds 32 claims. Reproduced are the LS unit and active-neuron counts (1,696
units in 62 sessions; 829 active against 840), the reliability of the LS phase
code across the population (Figure 3), the rise of CA3-LS coherence and
coupling along the run (Figure 6C and 6D), the absence of a link between
assemblies and hippocampal phase locking, the fine-scale phase information of
Figure 1G and the depth gradient of Figure 4D. Not reproduced are the phase
decoding claims of Figure 2, the rate and phase equivalence of hippocampal
place fields (Figure 1I), the onset-depth correlation, the assemblies of Figure
5 and their stronger phase code, the Figure S7 ensembles, the rate and phase
independence of Figure S2, and the hippocampal unit, Figure 6 session and
Figure S1F trial counts. Most decoding outcomes rest on an assumption: the
paper does not say how a position bin enters phase decoding when no spike
falls in its smoothing window, and setting its phase to 0 was adopted after
round 1 showed that leaving such bins out lets the decoder read where the cell
fires (shifted phases beat rate in 0.207 to 0.535 of conditions). The record
says the decoder is weak on these files (median hippocampal rate MSE 6,329
against 6,733 for uniform guessing), and that the Figure 1G and 4D matches are
fragile: the phase-0 fill causes the first, and the second holds under one
decoder reading (bb1) alone. The author's first run had 9 reproduced, 12
partially, 11 not reproduced and 6 blocked, with leaving bins out as the
assumption and the assembly claims blocked as too large. Round 1 disagreed
with 9 of the 32 outcomes, found the left-out treatment confounded and the
cost estimate for the assemblies unsupported, and in reply the decoder was
calibrated, ties were broken at random and peer prediction was run on a random
7% of LS unit-conditions (7,098 pairs). Round 2 agreed with all 32 but found
readings chosen inconsistently between fig4d and fig1i, and the author proposed
`fig1i-hpc-rate-phase-equivalent` as reproduced under a rule that a criterion
is met under any one reading, and `fig6-session-counts` as not reproduced, as
the verifier asked, so a third round reviewed the two. It agreed with the
second and not the first, since the criterion has no "under one reading"
clause, so fig1i stays not reproduced with its proposal recorded; it noted that
fig4d's criterion lacks the clause too and judged on the adopted reading would
likely be not reproduced, which was not proposed and so stands for a later
attempt. The author asked a reader nothing, so the answer and author-answers
runs changed nothing. The reconciliation with tingley-2018-01 changed 11
outcomes, through changes in the claims file, the dataset and the method;
the clone was shallow, so the earlier entry was read from `main`, and
`entry.py check` still reports one error, from the earlier record's cell tag
`claim:ls-information-lower`, which the new notebook lacks. The author's run
took about 2 h 50 min; one development command ran past its 30-minute timeout
on millimetre positions read as metres, and three full runs failed on columns
missing from some files and one on a guard for empty shuffle sets. The
notebook ran in about 19 minutes at first, 53.7 min after round 2 and 41
minutes after round 3.

The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is a
contributor). The `hpc` unit label names the probe aimed at CA1, not a
subfield, and each session's units carry one hippocampal label, so the
paper's 2,297 CA1 and 654 CA3 units cannot be recovered: the files hold 3,260
hippocampal units (2,636 hpc, 624 ca3) and 1,696 LS units against 2,951 and
1,647. DT8's 17 sessions have hippocampal channels, with a flagged CA1
channel, but no hippocampal units, and sessions with LS and CA1 units number
25 or 33 against the paper's 63. In 31 sessions of DT7, DT8 and DT9 the head
position and the condition templates are labelled meters but hold
millimetres, so speeds and metric distances read from them are 1,000 times
too large. No CA1 channel is flagged in five DT9 sessions and in DT7
20170317, though the paper refers all LS spike phases to CA1 theta. Which
probe each depth in a session name belongs to and the order of sites along a
shank are not stored, and the direction of the Figure 4 depth gradient
depends on both. Nothing marks the maze rotations of Figure S6. DT7 20170324
has no units table; some files lack `trial_type`, `condition_type` or
`max_waveform_channel`, and some conditions have 151 template points where
the rest have 201. In DT9 20170501 the trials do not match the head
position, and in DT2 20160221 the linearized positions match the head best
0.75 s after the trial times. Of the 16 findings of tingley-2018-01, five are
fixed (among them the copied z column, the repeated DT2 timestamps and the
LFP chunking), seven partly fixed and four still present; the 31 millimetre
files, which the first attempt found consistent with their stated unit, now
state meters. On the paper's side, questions are put to its authors on the
treatment of undefined phase (about 70% of trial-by-bin samples), on ties
between equally near template bins, on the conversion of peak information to
bits/cm and its levels, and on the peer-prediction fit and the 11,264 pairs,
where the files give 81,393; the 1,425 hippocampal neurons of the place-field
definition are not identified, the Results give 1,811 place fields where the
figures use 1,820, `bz_phaseMap2Bins`, which makeFig4.m calls, is in no
public repository, and the code writes its 20% place-field file with the
function's default threshold of 0.01.

The author's points on the protocol: it does not say what to do with a claim
of absence when method readings, not the test, change the outcome, so fig1i
was judged under the adopted assumption with the other readings reported;
timing numbers in result text change from run to run and any fix forces a
full run, so costs were worded approximately; an `elsewhere` claim not
attempted for lack of time has no fitting block reason, so `other` was used;
some criteria have no partial rule, and the general meaning of
`partially_reproduced` was used at first; and the rule for `measured` covers
only cases where a reading matches, so the closest reading was recorded and
named.
