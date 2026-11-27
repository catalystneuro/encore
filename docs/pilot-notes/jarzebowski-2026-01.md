# jarzebowski-2026, Jarzebowski et al. 2026

Ten claims on the dandiset reproduced, three partially and three not
reproduced, none blocked, all of them using the Allen CCFv3 annotation volume
as an outside input for each unit's layer; the 14 claims on the paper's model
(`data: elsewhere`, 11 reproduced, one partially, two not) and the link claim
`ccf-layer-link` (reproduced) are counted apart, for 22 reproduced, 4
partially and 5 not reproduced in all. The first verification round agreed
with 27 of the 31 outcomes as they stood and the second with all 31, and
nothing was proposed after the second, so there was no third round. It pins
version 0.240702.1725, which the Methods cite and which is the only published
version. The paper, Jarzebowski and Bendor, "Temporal Gating by Chandelier
Cells Encodes Signed Prediction Errors" (bioRxiv), simulates a two-compartment
model of one L2/3 neuron in which chandelier cell (ChC) inhibition of the axon
initial segment gates sensory (L4) input against predictive (L5 IT) input, and
tests its predictions on the Allen Institute's Visual Behavior Neuropixels
recordings of VISp, where the fraction of spikes in bursts (FSB) is highest on
the first repetition of an image, omission firing and bursting fall below
spontaneous, and running raises first-repetition bursting and rate. The claims
were written from the preprint's text without figures; its heading for
Supplemental Figures has nothing under it, so the legends of Figures S1 and
S2 could not be read, and the linked code repository was not public, so the
model was integrated in NumPy from the Methods' equations and parameters.
Not reproduced are `fig2a-weak-sensory-silenced` (0.90 to 0.975 spikes per
run, against 0.975 for the prediction alone), `fig3c-gain-keeps-release-delay`
(no release spike at Low gain in 800 runs, Mid and High 5.0 to 8.3 ms apart),
`figs1-novel-firing-rate-unchanged` (L5 index -0.043, p = 0.0095),
`figs2-l5-bursting-not-predicted-by-rate` (L5 rate predicts L5 FSB, t(6788) =
26.7) and `fig7d-running-lowers-omission-rate` (L5 -0.019, p = 0.29).
Partial are `model-positive-error-short-latency` (1 of 81 spikes after the
basket peak under the claim's seed), `fig6b-omission-firing-below-spontaneous`
and `fig6c-omission-bursting-below-spontaneous` (L5 outside tolerance, on an
assumption about the spontaneous period) and
`fig7b-running-raises-first-repetition-rate` (L5 0.186 against 0.05 to 0.16).
The author's first run gave 21 reproduced, 3 partially and 7 not reproduced.
The author asked a reader whether the analysis is limited to the sessions of
the optotagged mice; the answer added open detail O9 (all 153 sessions, or the
104 of the Sst-IRES-Cre;Ai32 and VIP-IRES-Cre;Ai32 mice), under whose second
reading `cell-counts` moved from not reproduced to reproduced (247 L2/3 cells
from 76 recordings, 997 L5 cells from 100). Round 1 disagreed on four claims:
on `fig2d-latency-grows-as-sensation-weakens`, kept as reproduced with a
resampled test of the largest step and the disagreement recorded; on
`fig3b-gain-lowers-burst-threshold`, moved to reproduced with 800 runs per
gain; and on fig6b and fig6c, moved from not reproduced to partially
reproduced by taking both spontaneous blocks in place of the 10 s block
alone. On its request every claim was also run on all 16 cell selections,
which moved `fig5c-fsb-highest-on-first-repetition` to reproduced, inside the
tolerance by 0.0002 to 0.0003 under O9 (b), and non-converged mixed models were
refitted with other optimizers. Round 2 agreed with all 31, found sentences the
outputs did not support, which were corrected, and found that both spontaneous
blocks are in effect block 3 and that the assumption is no better supported
than block 1 alone, against which neither fig6b nor fig6c reproduces. The
author's run took about 1 h 25 min (14:06 to 15:30 UTC), with the notebook at
740 s and peak memory 3.5 GB; nothing failed. Untracked dotfiles and a
`scripts` directory, which the author did not create, were left untouched.

The files give no layer for any unit, so layers come from the CCFv3 2017
annotation at 10 um, in which 7996 of the 7997 VISp units with coordinates fall
in a VISp layer; 351 VISp units in 7 sessions that pass the quality criteria
have coordinates x, y and z all 0, standing for missing values, and get no
layer. The spontaneous block right after the task is a 10 s grey screen
starting 18 to 29 s after it, and a 289 s block comes about 940 s after it; the
mice run in most windows of both, and in session 20211111T220915 the 10 s block
starts 3277 s after the last task presentation, with nothing in the files to
say why. The units and electrodes tables have no column descriptions. The
checks otherwise passed: 153 sessions from 81 mice, no two sharing a
spike-train signature, 4795 to 4811 active-task presentation rows per session,
and a clock check on which images and omissions separate 30 to 100 ms after
onset (median AUC 0.95); in 10 sessions the AUC is below 0.8 and 2 sessions
have no VISp unit passing the criteria, so a shared clock is not established
there, and leaving those 10 sessions out changes no outcome. Questions are put
to the paper's authors: which sessions enter the analysis, since only the 104
sessions of the optotagged mice give the paper's cell counts; which
spontaneous block and windows Figure 6 used; how FSB is formed for a cell; what
rule gave the 47 L2/3 and 658 L5 cells of Figures 7C and 7D; how running and
stationary presentations were defined for Figure 7, since 26 of the 104
sessions have no stationary Repetition 1 presentation; and the model's input
onsets, conductance ranges and burst threshold. The Figure 5C legend prints the
L5 slope as t(7523) = 8.1 with CI [-0.0011, -0.0007], a positive t with a
negative interval.

The author's points on the protocol: inputs must have a DOI or a repository at
a commit, and the CCF annotation has neither, so it was recorded by URL with a
SHA-256 the notebook checks; it does not say how to judge a claim of absence
whose cell selection is open between readings that give different outcomes,
and the criterion's counts picked the reading, marked as an assumption; the
model claims are `data: elsewhere` though their data is the paper's Methods,
listed as an input; a mixed model with one value per session cannot be fitted,
and the one-sample t test it reduces to was used; adding `depends_on:
ccf-layer-link` to `cell-counts` touches a claim, which the protocol requires
for link claims without saying the edit is allowed; and the clock check assumes
the response falls within the analysis window, so a 30 to 100 ms window was
added after a 250 ms count missed transient responses in about 25 sessions.
