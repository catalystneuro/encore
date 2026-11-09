# crcns-ac-2, DeWeese et al. 2004

Fourteen claims reproduced (nine on an assumption), seven partially (five on
an assumption), two not reproduced and none blocked. The first verification
round agreed with 22 of the 23 outcomes as they stood and the second with all
23; nothing was proposed after the second, so there was no third round. CRCNS
does not version data sets, so the version is recorded as unversioned with the
data set's DOI, and the notebook checks the MD5 of the tar files against
`checksums.md5` as it streams them. The paper, DeWeese and Zador, "Shared and
Private Variability in the Auditory Cortex" in the Journal of Neurophysiology,
records tone-evoked PSPs by in vivo whole-cell current clamp in the auditory
cortex of anesthetized Sprague-Dawley rats, 33 neurons from 21 animals, 29 of
them with a simultaneous LFP, and divides the trial-to-trial variability of the
PSP height into a part shared with the LFP and a private part by culling and
regression on the LFP; the data set holds the 33 recordings, the six TTX
recordings behind the paper's mEPSPs and one awake recording of a later paper
that no claim uses. The claims were written from the extracted text of the
version of record, which printed =, <, >, the minus sign and plus/minus as a
replacement character, as the PDF could not be rendered; the paper has no
supplement and links no code. The check read these signs from the PDF's font
encodings, which corrected several guesses (among them the access resistance
groups, which had been reversed, and P = 0.5 for the LFP CV test), and left two
points open, that no figure was looked at as an image and that several criteria
put numbers on the paper's vague words. All 23 claims could be tested.
Reproduced are `fig3a-reliable-neuron` (022801md01b, 0.876 mV over 26 tones),
`fig3b-total-variability-distribution` (7 and 18 neurons, the first under the
criterion's second reading, q < 2 mV), `total-variability-population` (4.58 +-
0.47 mV), `lfp-culling-reduction` (4.80 to 3.19 mV, within by 0.01 mV),
`fig5b-residual-lfp-psp-correlation` (81% of 396 tones positive, 32% with p <
0.05), `fig7b-private-best-estimate` (1.48 +- 0.17 mV over 28 neurons),
`fig7d-large-responses` (an LFP-based bound of 1.62 mV, within by 0.02 mV,
from 14 neurons, not the paper's 16), `lfp-cv-not-different` (p = 0.674),
`anesthesia-comparison` (private 1.01, 1.37 and 1.93 mV, the first and last
within by 0.01 and 0.03 mV), `fig8-spontaneous-veto` (-0.155 and -0.193),
`overfitting-correction-example`, `quantal-comparison` (14 of 33),
`recording-properties` and `access-resistance-depth-no-effect`, though there
the higher access resistance group is the more variable, the reverse of the
paper. Partial are `fig2-stereotyped-shape` (19 of 33 neurons peak within the
claims file's 50 ms bound), `fig7a-lfp-culling-estimation` (largest reduction
80.0% against 71 +- 7.1), `psp-culling-reduction` (30 of 33 neurons at or
below 3.3 mV), `fig4c-psp-culling-can-increase` (16 of 33 against 18 +- 1.8),
`cv-large-responses` (private CV 0.383, 0.007 below its tolerance),
`private-shared-ranges` (20 of 28 private values, 71%, in 0.9 to 3.3 mV) and
`mepsp-size` (0.602 mV, outside 0.39 +- 0.08, with CV 0.354 within). Not
reproduced are `culling-controls`, where random culling matched to LFP-based
culling gives 3.82 mV and not 4.5 +- 0.1, and `large-responses-controls` (2.42
and 2.40 mV against 3.20 +- 0.05 and 3.2 +- 0.5). Most outcomes rest on
assumptions: spike trials found with each neuron's spikethresh from the data
set, where the claims file's rule (a fast rise to above -20 mV) gives 5.35 mV
total variability against 4.58; LFP-based culling run after PSP-based culling,
as the Figure 6 legend says; input resistance with the access resistance
subtracted; and an assumed mEPSP detector. The author's first run gave the
same outcomes except that `mepsp-size` was blocked as methods underspecified
and `anesthesia-comparison` was partially reproduced, with the two cullings
decided on the full ensemble and intersected. The author asked no questions of
a reader, so the answer and author-answers runs changed nothing. Round 1
disagreed on `mepsp-size`, which it found testable, and found that the spike
rule run as the claims file's dropped the fast rise and applied -20 mV to the
uncorrected trace, that the cullings were not run in sequence, that the mEPSP
noise SD had collapsed, that the per-tone overfitting correction equals the
per-neuron one by algebra, that the fig8 baseline lies inside the spontaneous
window, and that the LFP-matched random control may rest on a misreading of
the 10-trial rule; in reply the claims file's rule was run as written,
sequential culling became the main reading, which made
`anesthesia-comparison` reproduced, the mEPSP detector was rebuilt with a
clipped SD and a false-positive count on the inverted traces, which made
`mepsp-size` partially reproduced, the fig8 controls were added and the
10-trial question went to a reader in `questions/crcns-ac-2.yaml`. Round 2
found sentences the outputs did not support (2.99 and 1.36 mV called within
tolerance, a third group of spikes the claims file's rule misses, and the
ranges of the mEPSP finding), that heights were not re-measured after culling
as a reading, and that the figure panels had not been compared with the paper;
in reply the text was corrected, re-measured heights and two more spike rules
were added to every table, which marked `fig4c-psp-culling-can-increase`
assumed, and the panels were compared by eye and match, Figure 4 being
labelled 030301md03b, which the claims file reads as unnamed, so that went to
a reader as a second question. The author's run took about 1 h 30 min, an
hour of it lost when `entry.py check` hung and was killed at the 1-hour
timeout. The notebook ran in 67 s at first, 120 s after the author-answers
run, 82 s after round 1 and 126 s at the end. The untracked files in the
repository root were left alone.

Each anesthetized neuron's cell_specific_parameters.m gives first_cycle,
last_cycle, spikethresh and sweeps_to_include_in_bumps_anl, which the
documentation does not describe for these neurons; the cycles give the
paper's stable epochs (repetitions 10 to 63, mean 18.1) and spikethresh its
spike removal, so they carry the paper's trial selection. Anesthetized_cell_info.txt
gives a junction potential of about 10 mV and says the true potentials are
about 10 mV more depolarized than the recorded values, where the paper corrects
by 12 mV in the other direction, and only that gives the paper's rest
potentials (median -70.0 mV, -58.4 to -92.0); the documented direction gives
-33 to -66 mV. The documentation calls the prepulse height a voltage, while
the values (100 and 200) are currents in pA. It does not say which ep_<n>.ibw
file is trial k of a TTX recording, and its Matlab example's name order picks
different sweeps from the numeric one in four of the six recordings;
050401md02 has one stable sweep of 7.7 s. The TTX recording 030401md02h, after
the documented division by 4, sits near +2.6 mV, which is not a membrane
potential, so its offset or gain may be wrong. Sutter_diag_depth is missing
for 8 of the 33 anesthetized neurons, so the depth comparison can be checked
on 25. Questions are put to the paper's authors: whether spikes were removed
with spikethresh and whether the slow depolarizations it removes were counted
as spikes; whether input resistance had the access resistance subtracted;
which detector, threshold, filter, baseline and sweeps gave the mEPSP sizes;
and how the open details of the culling procedures were set, among them the
peak window, the span of the culling threshold, the negative scale factor rule
in PSP-based culling and whether the random controls apply the 10-trial
criterion again.

The author's points on the protocol: `archives.md` describes zips opened in
place, but ac-2 is a tar.gz that cannot be read by range, so it was streamed
once into memory; `entry.py check` hung for over an hour on its `LONG_LITERAL`
regex over a 32-number list of tone frequencies, worked around by reading the
list from the data set's docs; the suggested clock check cannot separate an
offset from a response when tones play in a fixed order, so post-onset tuning
against a permutation null and response latency were used; the claims file's
header wrongly says the spike rule can change only a few trials; several
criteria define only reproduced and partially reproduced, so narrow misses
with the effect holding were called partial and the two control claims not
reproduced; and the protocol does not say whether `assumed` applies when
another reading gives the same outcome.
