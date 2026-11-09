# 001754 again, on the fixed draft (2026-10-15)

The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
The conversion was redone (`mcnaughton2000-to-nwb` at commit `7346882`) and
the draft re-uploaded on 2026-10-14, and the attempt pins `draft`. Three
claims reproduced, one not reproduced and three blocked, against two, two
and three before; both rounds agreed with every outcome and nothing was
proposed, so there was no third round.

The one change of outcome, `fd4-abnormal-selectivity` from not reproduced to
reproduced (one-sided p 0.024 against 0.055), comes from the data, not the
analysis: the draft drops every copy of each group of identical rate maps,
which removes three near-empty Rat2 maps the first attempt counted, and a
notebook cell runs the same test on the earlier maps to show it. Dropping
every copy instead of keeping one also removed six maps from the dandiset.
`flight-spatial-code` stays not reproduced (Rat1 10 of 25 significant on
flight day 9, Rat2 2 of 28); the rounds added tests of the shuffle null on
real spike trains cut off from position, which give fewer false positives
than the 0.05 the test assumes, and the record now calls a low fraction weak
evidence against a spatial code, since the test's power is unmeasured.

Of the eleven earlier findings, five are fixed (rate maps linked to units,
-999 and lost positions documented, duplicate maps gone, units' spike files
and windows listed, spike-time resolution documented), four partly fixed
(shared position trace, smoothing kernel, EEG, age and camera view) and two
still present (position only at spike times, and the description's flat
track). One is new: Rat2's preflight and flight units are on tetrodes with no
overlap, unlike the other two rats. The dandiset description was corrected
for the flat track and the EEG during the final revision, after round 2 had
read it, so the record still lists both; the next attempt will see the new
text.

The earlier attempt's transcripts are now in `transcripts/001754/attempt-01/`,
since the workflow writes every attempt's transcripts to the same paths. The
author's points on the protocol: the attempt schema has no field for an
earlier finding's status, so it marked each statement "Still present",
"Partly fixed" or "New" and listed the fixed ones in a comment; pinning
`draft` does not stop the attempt if the draft changes during it, which
happened here; and the protocol has no rule for an outcome that changes
because the data owner changed the data.
