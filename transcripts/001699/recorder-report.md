I added the 001699 row to README.md with `tools/readme_row.py`; it reads 14 reproduced, 7 partially, 5 not reproduced and 1 blocked. I also appended the subsection below to the end of docs/pilot-notes.md. Nothing is committed. The attempt, claims and entry are unchanged, and I left the untracked files in the repository root alone.

The `catalystneuro` field for this dandiset names a contributor (Paul Adkisson-Floro), not a repository. So I opened the second paragraph the way earlier subsections do for that case: "(… of CatalystNeuro is a contributor)".

### 001699, Moore et al. 2025

Fourteen claims reproduced, seven partially, five not reproduced and one
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 27; it would
call `fig1g-juvenile-halves-correlation`, `fig3g-adult-halves-correlation` and
`figs2j-adult-epochs-correlation` not reproduced, as neither of their two
values is within tolerance. The author applied that rule to all correlation
claims and changed fig3g and figs2j, but after fixes to spike counting and a
cut of every session to its first 20 min, the paper's session length, fig1g
gave a WT r of 0.815 against a bound of 0.81 and stayed partially reproduced.
In the same revision Isomap was fitted on every bin, as the criterion says, and
`fig2d-juvenile-isomap-wake-sharper` went from reproduced to not reproduced (p
= 0.056) and `fig2h-juvenile-isomap-rem-sharper` from not reproduced to
reproduced (p = 0.045). Round 2 agreed with all 27 but noted that the 20 min
cut departs from the claims file's session definition, which keeps blocks
whole and cuts only those over 30 min to 1300 s; under that definition fig1g
gives r = 0.761 and 0.839, neither within tolerance, the author proposed not
reproduced, and a third round reviewed only that proposal and agreed. The
paper, a bioRxiv preprint, records head-direction cells in the postsubiculum
(PoSub) of juvenile and adult Fmr1-/y and WT rats, and reports that juvenile
Fmr1-/y cells have higher HD information, also against the Isomap angle of
waking and REM sleep activity, and drift less relative to the room, while in
adults tuning does not differ and Fmr1-/y tuning curves drift more within and
between sessions. The unit counts, behaviour, cell metrics, HD tuning, its
stability between halves and between sessions, the drift of tuning curves and
of a Bayesian decoder, and the Isomap tuning in waking and REM sleep were
tested. `figs1d-probe-in-posub` is blocked as `other`: all 36 files hold
histology images, but none marks the probe tract or PoSub, and judging them
needs an anatomist. Besides fig1g, `fig3g-adult-halves-correlation` (r = 0.804
and 0.748 against 0.94) and `figs2j-adult-epochs-correlation` (0.787 and 0.562
against 0.90 and 0.76) are not reproduced, `fig1j-juvenile-less-drift` gives
the paper's direction at t(10) = -1.91, p = 0.085, and fig2d gives p = 0.056.
Some outcomes rest on weak ground: the main grouping counts H3026, labelled WT,
as a juvenile Fmr1-/y rat and H3029, whose date of birth makes it an adult, as
a juvenile WT rat, chosen because it matches the paper's unit counts, and with
H3026 left out the HD information of `fig1ef-juvenile-sharper-tuning`, fig1h
and fig2h give p = 0.072, 0.068 and 0.095; fig2h is at the threshold, with p
= 0.16 on the first day alone; `fig1h-juvenile-smaller-offset` gives p = 0.060
for cells with half-width below 120 degrees; cells re-recorded on later days
are counted on each day, as the files give no probe depth per day; and the
active speed of `figs1c-juvenile-behaviour-similar` differs on the first day
alone (p = 0.034). The author used the full text of version 1 of the preprint,
which the dandiset links, and version 2's Methods only where version 1 leaves
a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in round 2 and its revision, so the version-2 numbers in the notes
were not checked by a verifier.

The dandiset was converted by CatalystNeuro (Paul Adkisson-Floro of
CatalystNeuro is a contributor). The paper's unit counts (406 units in 7
juvenile WT rats, 372 in 5 juvenile Fmr1-/y rats, 543 in 6 adult WT rats) and
its range of 8 to 83 units per juvenile recording are matched exactly only if
H3026 and H3029 are regrouped as above; with the archive's labels the juvenile
groups have 5 WT and 4 Fmr1-/y rats, and the juvenile effects weaken (HD
information p = 0.23, offsets p = 0.17). The file of H4825 holds the recording
of H4824 (identical waveforms, unit and spike counts, and spike times up to
1248 s), with its spike and tracking times shifted piece by piece onto H4825's
epoch table and clipped at its end, where 131373 spikes share the last spike
time and 12970 tracking frames repeat a timestamp; H4825's own recording is not
in the dandiset, so the adult Fmr1-/y group has 5 rats and 440 units where the
paper has 6 and 507. The dates of birth of H3023 (2022-08-13) and H3026
(2022-09-13) are after their recordings in 2021, so the archive's asset
metadata give them negative ages (P-366D to P-344D), H3029 shares H4830's date
of birth, and no NWB file sets the subject's age. The units table holds only
spike times, mean waveforms, electrode group and sampling rate, with no cell
type, contamination or depth, so the paper's exclusion of cells recorded in
the part of PoSub already recorded on the previous day cannot be repeated. The
epochs and processing/tasks tables do not mark the exploration sessions
reliably: in H3001 200202 task epoch 1 is called wake but lasts 94 min without
tracking, in H3026 211003 epoch 1 spans 112 min of waking and sleep, in H3023
210813-1 epoch 2 runs from the end of the first session into the second, and
H4823 has a single epoch and no sleep task; every file's session description
mentions a cue rotation, and most files hold a third tracked session
(`wake_cue_rot`) that version 1 of the paper does not describe. Spikes and
tracking share a clock in 32 of 35 recordings, and in the other three the cells
are too weakly tuned to show it. Other findings: in H3015 210417 and H4823
221108 position is stated in centimetres but spans about 300 and 700 units, so
it is in pixels, and head direction runs from -pi to pi where the other files
use 0 to 2 pi; one unit of H3023 210812 has spike times out of order, and 22 of
the 24 juvenile files have one to three tracking frames whose timestamp does
not increase; the dandiset's `about` field lists "Fmr1 protein, rat" as an
anatomy term with the MeSH identifier of Fragile X Syndrome (D005600); the
paper's analysis code is not public, and the repository the dandiset links,
woodcode (commit 61ee178), is the lab's general library; and in the paper the
Methods exclude units with contamination scores "below 0.5", which would remove
1727 of 1761 units, the ranges of units per recording mix counts of all units
(8 to 83, maximum 114) with a count of putative excitatory units (minimum 30),
and version 2 gives the adult counts as 372 and 406 units in 6 rats each, the
juvenile numbers repeated.

The notebook ran in 154 to 162 s in the first clean run, 282 s after round 1,
about 13 minutes after round 2, which repeated every claim's main test under
both session definitions, and 789 s after round 3. The statsmodels mixed-model
fits failed to converge on several measures, one giving p = 1.0, and the author
replaced them with an exact profile-likelihood fit of the same model, which
matched statsmodels to 8 digits on a synthetic case. Round 1 also found that
frame counting on speed-filtered frames lost spikes (2.6% on synthetic data)
and that the decoder error was interpolated before unwrapping, and both were
fixed. Round 2 found statements the outputs did not support, among them
archive-label p values kept from round 1, a cause for the 279 decoded bins of
H3001 200201 that no output showed, and the 20 min cut presented as following
the paper, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: two preprint versions under one DOI; no rule for correlation values
outside tolerance; no rule for which grouping is the main one when the
archive's labels contradict the paper's own counts; counting each recording
once where a count claim matches only if the duplicate is counted; linked code
that is the lab's general library and not the paper's analysis; no rule for
claims of absence that rest on several tests; no blocking reason for images
that need expert judgement; and a contamination threshold in the Methods that
would remove almost every unit.
