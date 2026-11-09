# 000044, Grosmark et al. 2016

Three claims reproduced, three partially, six not reproduced and eight
blocked, all on the dandiset. Round 1 disagreed on eight outcomes: it found
that `fig2d-shuffle-high-dpcc` ranks all place cells by dPCC and does not use
the strong-contributor selection, and the author changed it from blocked to
partially reproduced; for the six claims built on the rigid and plastic
classes the author kept the block under the rule for dependents of a blocked
claim, and round 2 accepted that and agreed with all 20 outcomes, so there
was no third round. The paper reports that diversity in the firing dynamics
of hippocampal cells supports both rigid and learned sequences, in rats
recorded in sleep before and after running on linear and circular tracks.
The sessions, place-cell count, PRE, MAZE and POST replay, coactivation by
firing rate, the rate split and the replay of low-rate and high-gain cells
were tested; the place-cell count is 417 at the 1 Hz threshold against 491,
and 480 at 0.5 Hz. `fig2b-strong-contributors` is blocked as
`methods_underspecified`, because the fixed test calls 56.1% of cells
significant with every rate map shifted, which shows it is not the paper's
procedure, and seven claims that depend on it are blocked with it. The
pooled replay test the criteria fix finds no replay before any manipulation
(p = 0.916), because the three circular-track sessions score lower in every
epoch and supply 11161 of 23801 POST events, so `fig1c-post-gt-pre`,
`fig4d-slow-sequences`, `fig4e-gain-sequences` and the informative half of
`fig2d-shuffle-high-dpcc` say little about the paper; POST exceeds PRE in 8
of 8 sessions and on each kind of track separately.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). It holds 8 sessions from 4 rats, with 562 pyramidal units and
128 interneurons, on one clock. The paper's derived data are not deposited:
there are no candidate or ripple events, no place-cell list, no sequence
scores and no PCC values or rigid and plastic labels, so every selection must
be rebuilt, and neither the paper nor the dandiset links analysis code, while
the supplementary Materials and Methods that define them are served only
behind a browser check. In versions 0.210812.1516 and 0.250624.0426 every
position series stores its sampling period (0.0256 s) as its rate, so the
positions span about 880 to 2360 hours; version 0.261005.2101 stores 39.06
Hz. Other findings: the description lists neck EMG and head-mounted
accelerometer signals, and the files hold neither, nor any wide-band data,
only the LFP at 1250 Hz; in Gatsby_08022013 the POST epoch ends at 30413.6 s
while the LFP, spikes and sleep states run to about 32000 s; every
electrode's location is "unknown", units carry only the hemisphere and
subject age is "/"; and on the circular track the animals ran toward
decreasing linearized position, which the metadata does not say.

The author's first draft assumed the circular track was run the other way;
the bug was fixed and the claims re-run, with the fix recorded in the
notebook. In round 2 the verifier's executed copy printed slightly different
values for the best-template variant (190 cells against 188) from the same
code and seeds; the cause was not found, and no conclusion rests on it. The
author's points on the protocol: the chance-level rule applies only when the
paper states a chance level, and "significant" was read as a 5%
false-positive rate; dependents of a blocked claim are blocked even when they
do not use the blocked result; no rule for a main text available without its
supplement; no guidance for a pre-registered test confounded by pooling
across sessions; no rule for code bugs found after claim analyses were run;
criteria that define no partial outcome; figures that could not be read, so
Figure 1D got no claim; and the rule to show how a result changes with a
threshold, which covers many choices here.
