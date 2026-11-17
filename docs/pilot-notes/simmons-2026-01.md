# simmons-2026, Simmons et al. 2026

Thirteen claims reproduced, two partially, four not reproduced and 18 blocked, 16
for missing data and two for insufficient metadata;
`fig6d-gat1-enriched-aldh1a1` and `figs5-gat-expression-in-snc`, on data outside
the dandiset (`data: elsewhere`), are counted apart and blocked as other, as
Dopabase has no pinned version and neither source was attempted in the time. Two
outcomes rest on an assumption, `fig3b-gabazine-increases-rate` and
`fig7d-astrocyte-gi-increases-rate`. The first verification round agreed with 37
of the 39 outcomes and disagreed on `fig5d-shrna-higher-rate`, which it held
blocked for insufficient metadata where the record had it reproduced on stand-in
controls, and on `fig6c-snc-gi-dreadd-no-snr-change`, which it held testable on
its own 8 SNr cells; the author took the first, moved
`fig5f-aldh-inhibitors-higher-rate` from not reproduced to blocked for the same
reason, against the verifier's outcome for that claim, and kept fig6c blocked
through its dependency on the missing SNc recordings, with the disagreement
recorded and its test run (P = 0.81). The second round agreed with all 39, and
nothing was proposed after it, so there was no third round. The dandiset is
pinned at 0.260521.2201, its published version. The paper, Simmons et al.,
"Astrocytes mediate the dopaminergic modulation of tonic GABAergic signaling in
substantia nigra" (Science Advances 12, eadq8840), records SNr neurons in mouse
slices, in cell-attached mode for spike rate before and after a drug and in
whole-cell voltage clamp for evoked GPe IPSCs, and reports that the D2R agonist
quinpirole lowers the GPe IPSC and raises SNr firing, that gabazine raises SNr
firing through a tonic GABAA inhibition, that this effect is lost after ALDH1A1
knockdown, ALDH inhibitors, the MAO-B inhibitor rasagiline or the GAT-1
antagonist NNC-711, and that Gi-DREADD activation in SNr astrocytes raises the
rate while the GAT-3 antagonist SNAP-5114 lowers it and occludes quinpirole. The
claims were written from the version of record with its supplement, opening PDF
pages to read panels, and from the paper's code deposit, one Mathematica notebook
in which every window, bin and dropped episode is a placeholder; spikes were
detected in Clampfit with settings given nowhere, so the attempt uses a threshold
of 8 robust noise units and shows every rate result at 6 and 12. The reader wrote
38 claims and the claims check added `fig1b-gabazine-blocks-gpe-ipsc`, for 39.
Reproduced are `fig1c-quinpirole-reduces-gpe-ipsc` (-30.1%, P = 0.0087, n = 5),
`fig1e-ppr-rises` (up in 5 of 5 cells), `fig2b-inhibition-wanes` (4.26 against
11.85 Hz, 8 of 8 cells), `fig7h-nnc711-increases-rate` (+36.0%, P = 0.0041),
fig7d (+30.2%, P = 0.029, only under reading b of M1 at thresholds 8 and 12) and
the claims of no effect, `fig4b-gpe-gi-dreadd-no-rate-change`,
`fig5e-shrna-gabazine-no-change`, `fig5g-disulfiram-blocks-gabazine`,
`fig5h-deab-blocks-gabazine`, `fig6a-rasagiline-blocks-gabazine`,
`fig6e-nnc711-blocks-gabazine`, `fig7e-gabazine-occludes-astrocyte-gi` and
`fig7f-snap5114-occludes-quinpirole`; fig5g rests on 3 cells against the paper's
5, with which a paired t test finds an effect of the paper's gabazine size with
probability 0.25. Partial are fig3b, 21.4 to 23.2 Hz over 49 cells, +9.5% against
25 +/- 2.5%, significant with all cells only under reading b at thresholds 6 and
8 (P = 0.047 at 8), and `fig7f-snap5114-decreases-rate` (-11.7%, P = 0.0050,
about half of 23 +/- 2.3%). Not reproduced are
`fig2c-quinpirole-attenuates-gpe-inhibition` (inhibition 56.8 against 42.3,
Wilcoxon P = 0.11), `fig3a-quinpirole-increases-rate`, where the 7 cells without
an opsin go from 24.8 to 21.0 Hz (P = 0.30) and the 8 Chronos cells before the
train rise by 31.8% (P = 0.24), `figs1-gabazine-effect-vs-base-rate` (R2 = 0.004
against 0.11) and `fig4a-gpe-gi-dreadd-reduces-ipsc`, where the clean-sweep mean
falls in 4 of 4 cells by 48.7% with P = 0.11, 16 points or more from fig1c. The
author's first run had 14 reproduced, 2 partially, 5 not reproduced and 16
blocked, with fig5d reproduced and fig5f not reproduced against gabazine-alone
cells as stand-in controls, and four outcomes marked assumed. The answer and author-answers runs found no questions file and changed nothing.
Round 1 held that collapsing cells had never been inspected, that reading b of M1
was not applied to fig2c, that the fig4a mean was contaminated by spontaneous
action currents, that the stand-in controls of fig5d and fig5f are not a reading
the criterion allows, that fig5g's power was not discussed and that file 0023 of
subject 9019 was never checked; in reply every cell's rate was printed at the
three thresholds, seven failed recordings were found and each affected claim
rerun without them, with no outcome changing, fig2c gave P = 0.078 to 0.11 under
reading b, fig4a was measured on clean sweeps, the power was computed and file
0023 proved to hold a 225 pA evoked current, not a recording in gabazine. Round 2
asked that the assumptions of fig3b and fig4b be named, after which fig4b lost
its flag, as the absence holds at every threshold under reading a, found eight
places where the text did not match the outputs, all corrected, and left two
round-1 points open, now closed: 8979-2025-05-27-164 was shown to be a failed
recording, with both fig7f claims run without it, and the drug timing of
8945-2025-04-16-144 was shown not to affect fig3b. The author's run took about
1 h 30 min; the notebook ran in about 10 minutes at first, 592 s after the
author-answers run, 14.1 min after round 1 and 11 min after round 2. A first
metadata survey of the 412 files hung for 30 minutes when run with threads and
took 80 s with processes and timeouts, an early dead time of 2 ms counted each
spike twice and was set to 4 ms, and `tools/entry.py lock` wrote a `python:`
field the schema rejects, from an uncommitted change to the tool, which the
author and author-answers runs removed by hand.

Each recording's condition (virus, drugs, which file is control and which drug,
when the drug was applied, measurement windows) is given only in free-text NWB
notes, in many spellings, with no icephys tables, intervals or structured labels,
and the light and electrical stimuli are not stored (the stimulus series hold
only a -10 mV test pulse), so stimulus times were read from the responses. The
dataset holds no SNc recordings, no recordings with SCH39166, NPPB or Gq-DREADD,
gabazine then quinpirole, low glucose or room temperature, no evoked IPSCs in
gabazine, and none of the imaging, RNAscope, PercevalHR or voltammetry data;
sixteen claims are blocked for missing data, one of them, fig6c, only through its
dependency, as its own SNr recordings are present. No cell is labelled as a
control of the shRNA or inhibitor experiments, and counts differ from the
paper's: 49 gabazine-alone cells against 45 (Fig. 3B legend), 10 (Results) and
39 (Fig. S1), 3 disulfiram-then-gabazine cells against 5 and 7 quinpirole cells
without an opsin against 8. Seven cell-attached recordings lose their action
currents during the experiment, the spike amplitude shrinking to the noise and
the rate falling to under a quarter of the condition before (cells of subjects
5110, 6808, 6812, 7084, 7310, 7324 and 8797), and an eighth, 8979-2025-05-27-164,
shrinks to the noise in the same way while its rate falls only to 26%; nothing
in the files marks them. The nine files 0015 to 0023 of subject 9019, an
optogenetic IPSC cell, carry the notes of files 0003 to 0010 of the same day, so
which were recorded in quinpirole is not stated, and file 0007 of subject 8952
and file 0000 of subject 6813 are not named in their own notes. Sixteen files are
deposited twice, each pair with the same session id, different `obj-` suffixes
and the same first sweep (subjects 4981, 4982, 4983, 4984, 5011, 5012 and 9045).
Subject ids 6806, 6813 and 7321 have recordings on dates 4, 32 and 7 days apart,
with ages that advance with the date, so either the ids were reused or the dates
are wrong. The notes give 30 C for all 412 files, where the Methods give 32 to
33 C (the Fig. S4E legend also says 30 C), and holding potentials of -50, -55
and -70 mV for the optogenetic IPSC cells, where the paper gives -60 mV. The
dandiset's related resource is the bioRxiv preprint, and the published paper is
not linked. Questions are put to the paper's authors: the spike detection
settings in Clampfit and how the stable window of each condition was chosen, as
the significance of three outcomes changes with the threshold; which 18 control
cells form Fig. 5D and 5F; and which 8 cells form Fig. 3A.

The author's points on the protocol: the dependency rule blocks fig6c although
its own 8 SNr cells are in the dataset; an `elsewhere` claim whose source cannot
be pinned, such as Dopabase, has no blocked_by reason, nor does outside data not
tried for lack of time, so `other` was used; `tools/entry.py lock` writes a
`python:` field the schema rejects; it is unclear whether a method choice the
claims file leaves to the author, such as the spike threshold, counts as an
assumption; it does not say whether a significant result outside the size
tolerance, or a result in the right direction but not significant, is partial or
not reproduced; reading b of M1 defines no window for the control condition; and
with no trial tables or stored stimuli, the clock check had to be made from the
responses.
