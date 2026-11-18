# jacobsen-2022, Jacobsen et al. 2022

Five claims reproduced, two partially, none not reproduced and 21 blocked,
all for missing data; four outcomes rest on an assumption. The first
verification round agreed with all 28 outcomes as they stood and the second
with all 28; nothing was proposed after the second, so there was no third
round. It pins version 0.220506.1516, the version the paper cites and the
latest published one. The paper, Jacobsen, Nair, Obenhaus, Donato, Slettmoen,
Moser and Moser, "All-viral tracing of monosynaptic inputs to single
birthdate-defined neurons in the intact brain" (Cell Reports Methods 2,
100221), targets single birthdate-defined hippocampal cells with in utero Cre,
a helper virus and rabies, counts their starter and input cells by histology,
and identifies the function of input cells in the medial entorhinal cortex
(MEC) by optogenetic tagging with RABV-ChR2-YFP and by two-photon imaging. The
claims were written from the version of record, with Figures S1 to S4 read
from the PDF; the paper reports no code of its own and its Methods cite
Rowland et al. (2018) for the analysis of the electrophysiology, whose
Methods and linked archdata code (for smoothing, the 5 cm/s speed cutoff and
tuning bins) are listed as inputs. The claims check made seven changes,
among them removing a responsiveness rule based on spikes before the pulse,
which the paper never uses, and adding `population-targeting-mec-labelling`,
for 28 claims. Only the optogenetic tagging claims could be tested. With the
pulse time taken as the TTL onset the paper's latencies and fidelities come
out to two decimals (T1 C89, the responsive grid cell, at 2.75 ms and
40.73%); with the offset T1 C89 is at 1.70 ms and not responsive. Reproduced
are `fig5c-functional-cell-types` (2 grid, 2 head direction and 1 border cell
under the standard shuffle, the border cell T4 C50 at 0.656 against 0.555,
falling short at 0.663 under the literal shuffle), `fig5c-responsive-grid-cell`,
`fig5c-example-cells` (all nine values, taking T1 C57 from the second laser
epoch of day 17 and T1 C52 from the first, which goes beyond the criterion),
`responsive-cells-at-19-days` and `mec-inputs-from-two-weeks` (day 14, a test
that cannot fail on the early side, as no earlier session is deposited).
Partial are `figs3-stable-input-cell` (17 of 18 values, the day 14 session 2
open-field rate 0.899 Hz against 1.06 ± 0.106; all 18 match over the first
1800 s, a reading not adopted because it was found from the expected values)
and `figs4-nonresponsive-cells` (the head direction score of 0.81 and the
peak rate of 9.02 Hz miss, at 0.912 and 10.62 Hz, and no tuning setting of 48
puts both within tolerance). The 19 histology claims of Figures 2 to 4, S1 and
S2 and the two imaging claims of Figures 6 and 7 are blocked. Round 1 found
that the notebook said earlier versions hold the same assets, that the shuffle
and the open-field span were unstated choices, that the per-epoch choice for
day 17 decides reproduced against partial, that tuning settings lowering the
peak rate had not been run and that the waveform does not identify the cell of
Figure S3; in reply the shuffle sentence was quoted and the shuffled
distributions shown, the first 1800 s were run for all 12 units, 48 tuning
settings were run and the measured head direction score became the tuning-map
mean vector length. Round 2 found sentences the outputs did not support (a
first TTL event of 0.6 to 1.9 s, now 45 ms to 1.9 s; LFP timestamps running
backwards 3 or 4 times, now 2 to 4), and that the first 275 pulses are not a
rule the paper applied to every session, all corrected. The author asked a
reader nothing, so the answer and author-answers runs changed nothing. The
author's run took about 21 minutes (03:04 to 03:25 UTC); its only failure,
repeated in the author-answers run, was `tools/entry.py lock` writing a
`python` field that the entry schema rejects, removed by hand. The notebook
ran in 81 s at first, 201 s after round 1 and 180 to 184 s at the end.

The dandiset holds only the optrode recordings of two mice (58313, 70375), and
of these only the 12 curated units shown in Figures 5C, S3 and S4; the
histology of the single-cell tracing and the two-photon imaging are not in it,
and the paper names no other deposit, so 21 of the paper's 28 claims cannot be
tested. For day 14 session 2 of mouse 70375 the file holds 2722 s of open
field and 413 pulses, and the paper's printed values (1.06 Hz, 2.95 ms, 48.00%)
are what the first 1800 s and the first 275 pulses give, where the whole file
gives 0.899 Hz, 3.05 ms and 46.49%; the paper does not say part of the session
was left out, and the first 275 pulses are not a rule it applied to every
session. The open field part of each session is not an epoch. The two laser
epochs of the day-17 session of mouse 58313 carry "N/A" for the power label,
where the other eight files carry "10Hz20mW", and nothing in the file tells
them apart. The first laser TTL event of every PhotoStim epoch starts at the
epoch start and lasts 45 ms to 1.9 s, where every other event lasts 1.0 to 1.1
ms. The TTL events show trains of 6 pulses at 10 Hz every 2.6 s, where the
STAR Methods describe pulses "at 10 Hz continuously". The LFP timestamps run
backwards 2 to 4 times within each file and end at 120 to 180 s, though each
series has 510,250 to 815,750 samples 4 ms apart. Units `waveform_mean` is
labelled volts but has a peak-to-trough of 31 to 41 for the 70375 unit and 34
to 243 for the units of 58313. No cluster label is shared across the six
sessions of 70375, and the unit's waveforms correlate with those of 58313 up to
0.965, so the cell of Figure S3 is identified only by each file holding one
curated unit. Version 0.220426.0814 holds 18 assets, the nine sessions twice
under real and hashed subject ids. The positions of the day-17 session span 76
x 75 cm, where the other eight span about 94 x 95 cm. Three questions are put
to the paper's authors: how the head direction score and the 9.02 Hz peak rate
are computed, which day-17 laser epoch Figure 5C uses, and whether the
shuffle of Rowland et al. (2018) shifts within 20 s or by at least 20 s.

The author's points on the protocol and tools: `tools/entry.py lock` writes a
`python` field the entry schema rejects; the protocol does not say how to
treat readings listed in the claims file's shared opening comment, and the
rule for criteria was applied with both readings reported; it has no rule for
an epoch choice made per unit, and every option was run with the outcome
marked assumed; its order of sources covers the paper's own code but not code
linked by a paper it cites, so the text came first and the code filled the
gaps; and the claims file's fidelity floor gives no chance level, so the
fidelity before each pulse and with shifted pulse times was shown instead.
