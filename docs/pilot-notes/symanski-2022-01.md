# 001539, Symanski et al. 2022

Seventeen claims reproduced (15 on an assumption), six partially (all on an
assumption), twelve not reproduced (ten on an assumption) and twelve blocked,
six for missing data and six as methods underspecified. All 47 claims are on
the dandiset. The first verification round agreed with 40 of the 47 outcomes as
they stood and the second, by the record, with 44, disagreeing on
`fig5gh-phase-preference`, `fig5-rr-more-than-beta` and `fig4d-ccg-lags`; the
author proposed those three changes, and a third round, which reviewed only
them, agreed with all three. It pins version 0.250815.1203; the paper cites no
version, and the two published versions hold identical assets, differing only
in metadata. The paper, Symanski, Bladon, Kullberg, Miller and Jadhav,
"Rhythmic coordination and ensemble dynamics in the hippocampal-prefrontal
network during odor-place associative memory and decision making" in eLife,
records tetrodes in dorsal CA1 and PFC (spikes and LFP) and the olfactory bulb
(LFP only) of eight rats in an odor-place T-maze task, and reports beta (20 to
30 Hz) and respiratory rhythm (RR, 7 to 8 Hz) power, coherence and phase
locking during odor sampling, the choice selectivity of single cells, ensemble
discrimination and GLM choice prediction (Fig. 6) and spatial fields on the
outbound route (Fig. 7). The claims were written from the version of record
(PMC9799972.1, as served by Europe PMC) without a PDF, so the figures were not
seen, and from the paper's code (JadhavLab/Jadhav-Lab-Codes-JHB at commit
88d5f8d, BetaOdorProject), whose two pipelines (Path A and Path B) often
disagree and are named as readings where they do. Thirty-five claims were
tested. Reproduced are the behaviour of `fig1b-performance` (75.74% against
77.0 +/- 1.3, inside by 0.04 points) and `fig1c-sampling-duration`, the beta
power and coherence increases during odor sampling, the higher beta coherence
at the odor port than at the reward well, fewer ripples at the odor port (38 of
38 sessions under reading (a)), RR-beta coupling, `fig3s1c`, `fig5s1de`,
`fig5s1fh`, `fig5f-rr-mvl-no-difference` (PFC pyramidal p = 0.0502, under 0.05
in 4 of 10 other bootstrap seeds), the four spatial claims `fig7-spatial-field-counts`,
`fig7s1b`, `fig7f` and `fig7s1f`, and `fig5e-beta-mvl-correct-incorrect` and
`fig5s2-ca1-int-pfc-beta-accuracy`, which hold by the criterion's method but
not under a split-half control (locking decided on half of the correct trials),
as selecting and measuring on the same spikes can alone make the incorrect MVL
lower. Partial are `fig2e-rr-coherence-increase` (CA1-PFC p = 0.11 and 0.10),
`fig2d-power-odor-vs-reward`, `unit-counts`, `fig3ij-si-anticorrelated`,
`fig5c-local-locking` and `fig5d-cross-region-beta`, whose significance rule
holds while its counts are outside tolerance (12 against 9, 3 against 11 and
10, 6 against 10). Not reproduced are `fig1d-turn-direction` (opposite turns 47
and 30 against 32 +/- 3 and 21 +/- 2), `fig2d-rr-power-no-increase`,
`fig2s2d-phase-offsets` (a CA1-OB beta offset, p = 0.011 and 0.012, where the
paper finds none), `fig3-choice-selective-fraction` (PFC 35.9% to 41.1%
against 31 +/- 3.1%), `fig4c-interneuron-si`, `fig6d-discrimination-time`,
`fig6c-even-odd-control`, `fig7b-odor-active-more-fields`,
`fig7c-field-properties-no-difference`, `fig7s1e`, `fig7d` (PFC p = 0.010 and
0.0061) and `fig7e-odor-decoder-first-quintile`. Six claims are blocked as
methods underspecified because their readings give different outcomes
(`fig2e-rr-coherence-odor-vs-reward`, `fig2de`, `fig2s1e`, `fig3s1e`,
`fig6e-glm-choice-prediction`) or depend on such a claim
(`fig6e-glm-with-interneurons`); three for missing data because the
thermocouple and the air-only sessions are not deposited; and the three claims
round 2 disputed, also for missing data, because the two rate-only interneuron rules give different
outcomes and the Methods' rule needs spike widths, which the files lack. The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 disagreed with seven outcomes, those of fig1d,
fig2s2d, fig3-choice-selective-fraction and fig7b (partial, where the
criterion names no partial band), fig5d (reproduced, where its counts are
compared), fig5-rr-more-than-beta and fig6e-glm-with-interneurons, and found
that the main interneuron rule, rate over 7 Hz without a width, was neither the
Methods' rule nor the code's, that the cross-correlogram threshold was applied
pointwise to the largest z of 80 bins, that cells for fig5e and fig5s2 were
selected on the spikes they were then measured on, and that the electrode-group
reading of the unit regions was never tested. In reply the first five outcomes
were changed, the main rule became the code's rate-only 9.5 Hz
(F7/ParsePyrIN.m) as an assumption with 7 Hz beside it, which made fig5gh and
fig5-rr reproduced on an assumption and fig4d blocked as methods
underspecified, fig6e-glm-with-interneurons was kept blocked with the
disagreement recorded, as the protocol blocks a claim that depends on a blocked
claim, and the three electrode readings, an inventory of every object in all 38
files, per-epoch performance (minimum 57.9%), a global jitter band (5 to 32
pairs per type kept, no type skewed) and the split-half control were added,
giving 19, 6, 12 and 10. Round 2 said fig5gh and fig5-rr should be blocked and
fig4d blocked for missing data, as the claims file names 9.5 Hz as a variant,
and found sentences the outputs did not support (the fig2de smallest rank-sum p
of 0.249 given as 0.65, that the dandiset holds the active units only, GLM
times moving by one window where they move by two, and others), all corrected.
The author's run took about 2 h 25 min (01:10 to 03:35 UTC) and nothing failed
in the final run; the notebook ran in 30 minutes at first, 1,119 s after the
author-answers run and 27 minutes after round 1, and after round 2 its first
re-run took 65 minutes, over the 60-minute limit, so the independent GLM runs
were made to run 4 at a time, with the same printed numbers, in 41 minutes; it
ran in 1595 s at the end. The GLM's resampled control uses 10 resamples instead
of 100 and was not re-run under the 7 Hz rule.

The units table's electrodes column, a reference to rows of the electrode
table, holds tetrode numbers in all 38 files: read as rows, as NWB tools do, it
places 131 units on OB tetrodes, which carried no units, and gives 540 CA1 and
752 PFC units, while read as tetrode numbers it gives 915 CA1, 508 PFC and no
OB units; electrode group names and labels also disagree in every file (group
Tetrode5 is labelled tetrode6), and read as group numbers the values put 24
units on OB tetrodes and match no group for 333. The files hold no spike
waveforms or widths, no nasal thermocouple signal, no air-only sessions and no
sleep epochs, so three claims cannot be tested, every claim that separates
pyramidal cells from interneurons rests on a rate-only rule, and the two
rate-only rules give different outcomes for three claims. The 915 CA1 and 508
PFC units are close to the paper's active units (934 and 508), not the 1,309
and 717 recorded, the selection is not described, and 53 units have fewer than
100 spikes within the task epochs. The trial table has no odor identity and no
chosen well, and unrewarded trials have no reward times, so odor and choice
were reconstructed from the position (the side agrees with the rewarded well
on 99.85% of rewarded trials) and which side is odor 1 (heptanol) cannot be
known; the files hold no DIO events, so the code's well-exit times cannot be
built. The electrode table's referenced column, which separates the
ground-referenced from the locally referenced channels, has the placeholder
description 'my description' in all 38 files. The acquisition ElectricalSeries
is a copy of the processed LFP in every file, which doubles the dandiset to 95
GB, stored as uncompressed, unchunked float64. Position in CS39 session 02
spans 59 by 25 units against about 105 by 45 cm on the other CS39 days, so its
unit of centimeters does not hold; four CS42 trials (sessions 02, 04, 05) end
after the last LFP sample, and the odor port position moves between epochs in
CS31 session 02 and CS34 session 02. Against this, every epoch is typed
odorplace, the 38 files are the paper's 38 odor-cued sessions, and the files
hold 3,174 rewarded trials, the paper's count of odor-cued correct trials. Of
the paper itself, the Results say the correct-incorrect SI correlation of
non-selective cells is not significant, while the legend of Figure 3-figure
supplement 1e reports r = -0.34 with p = 0.001 and 3.0e-4. Questions are put to
the paper's authors: which pipeline and test produced each Figure 2 panel and
how many correct-trial subsamples were used; the windows and frequency range of
the theta peak search; which SI produced Figure 3i-j; whether the GLM windows
were aligned to odor onset or port exit and whether sessions needed a minimum
of cells; the cross-correlogram window and band; and the z-scoring period, the
filter order, the epochs of the interneuron rate and whether the 9.5 Hz rule
was used for any panel, and the tapers of cs_PSD.m.

The author's points on the protocol: it is unclear whether readings giving
partial and not reproduced "differ", so a difference in degree was treated as
one and the claim blocked; several criteria give no rule for a partial result;
for fig2de the paper names two tests where the protocol says to judge on "the
paper's test", so the claim was blocked when they disagreed; a claim that
depends on a blocked claim is blocked although its analysis ran, so its numbers
were given in the notes; the unit-counts note that totals compare what was
deposited is ambiguous; the clock check's label shifting would mean re-reading
the LFP, so a spike-time shift control (436 against 133 responsive units) was
used and the LFP reported as consistent with a shared clock, not shown; Monte
Carlo noise can move results across p = 0.05 while the protocol only says to
fix seeds, so the spread over other seeds was printed; expected values the
criterion does not judge were recorded as measured and flagged; it does not say
whether approximating whole-file processing to fit the time limit is a method
choice, so it was recorded as an assumption; and, contrary to its rule against
saving data to disk, streamed LFP windows (6.8 GB) and parsed sessions were
cached during development, while the notebook itself streams everything.
