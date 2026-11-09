# crcns-hc-7, Kohus et al. 2016

Ten claims reproduced (seven on an assumption), four partially (three on an
assumption), 12 not reproduced (six on an assumption) and 18 blocked, 16 for
missing data and two for insufficient metadata. The first verification round
agreed with 34 of the 44 outcomes as they stood and the second with all 44;
nothing was proposed after the second, so there was no third round. CRCNS does
not version data sets, so the version is recorded as unversioned with the data
set's DOI (10.6080/K0MK69T5), and the notebook header gives the MD5 sum of
`Data.zip`, the only copy in the bucket. The paper, Kohus, Kali,
Rovira-Esteban, Schlingloff, Papp, Freund, Hajos and Gulyas in the Journal of
Physiology, records pairs of CA3 interneurons and pyramidal cells (PC) in mouse
slices, with parvalbumin-expressing basket cells (PV+BC) and axo-axonic cells
(AAC) and cholecystokinin-expressing basket cells (CCK+BC) and dendritic-region
targeting cells (CCK+DTI) as the presynaptic cells, and compares the kinetics,
short-term plasticity and asynchronous release of their uIPSCs under 10-AP
trains, ripple-like bursts (RIP) and epileptiform bursts (EPI), fits models of
short-term plasticity, and relates PV+BC to PC recovery to the refractoriness of
sharp-wave ripples; the data set is one zip of raw paired sweeps and the
authors' per-sweep tables (`_EPA`) for 60 pairs in 8 connection types. The
claims were written from the version of record, whose text was extracted from
the PDF, without the figure images, as the PDF could not be rendered, and
without code, as the paper links none; the claims check corrected the Table 4
values and a tolerance, and added `sipsc-continuum`, for 44 claims. The uIPSC
properties of Figs. 4 and 8, the plasticity under RIP, trains and recovery
(Figs. 5, 6, 9 and 10), the asynchronous release and the models of Fig. 11
could be tested; the firing-pattern clusters of Fig. 2 and Tables 1 and 2, the
connection probabilities of Fig. 3, the CsCl comparisons of Fig. 7, the
spontaneous IPSCs of Fig. 12 and the field potential and optogenetic results of
Fig. 13 could not. Every outcome on interneuron to PC pairs except the CCK+DTI
ones rests on the assumption that all were recorded with high KCl. Reproduced
are, among others, `fig4b-in-pc-kruskal-wallis` (all five measures differ,
latency p 0.00842, though rise and latency no longer differ on the 6 CCK+BC
pairs at or below the median holding current, p 0.26 and 0.14),
`fig5c-pv-rip-depression`, `fig9-pvbc-pvbc-depression` (Spearman rho -0.737),
`fig10-cck-cck-frequency` (medians 1.559 at 10 Hz and 2.153 at 40 Hz),
`fig11-model-cck-facilitation`, on a BIC margin of 1.8 under one reading, and
`fig13-pvbc-pc-recovery-halftime` (median tau 525.8 ms), which only 3 of 8 fit
combinations meet. Partial are `decay-epi-vs-160`, `fig8-pvbc-pvbc-uipsc` (3 of
5 medians within 10%), `fig11-model-pv-udr` (SSE decreases of 22.9, 13.1 and
24.7% against 35, 22 and 34%) and `table4-model-parameters` (8 of 13 values).
Not reproduced are, among others, `fig4b-in-pc-posthoc` (4 of 8 comparisons),
`fig4c-cckdti-pc-silent-single-ap` (3 of 7 pairs silent; 7 of 7 counting only
the first sweep), `fig6-pv-trains-depression` (fails at 1 Hz),
`fig6-cckbc-pc-trains` (1 of 6 pairs facilitates at every frequency),
`fig9-pvbc-pvbc-transmission-probability`, `fig11c-parameter-differences` and
the four onset claims, `fig6-cckbc-async-onset` (CCK+BC EPI median onset 2.0
against 10 to 12), `cckdti-async-onset`, `fig10-cck-cck-heterogeneity` and
`fig10-cck-cck-async`, whose two onset rules from the claims file also mark
release in the PV+ pairs the paper calls synchronous. The author's first run
had 10 reproduced, 5 partially, 10 not reproduced and 19 blocked, with the four
onset claims and `fig10bd-be-async-charge` blocked as methods_underspecified.
The author asked no questions of a reader, so the answer and author-answers
runs changed nothing. Round 1 disagreed on ten claims: the onset claims should
be judged on the claims file's two rules, the three claims resting on a reading
the claims file does not list (`fig8-cck-pairs-uipsc`,
`fig8-cckbc-vs-cckdti-pairs`, `decay-pc-vs-interneuron`) should be blocked, and
`async-charge-epi-vs-160` and `decay-epi-vs-160` could not be judged, as the 160
Hz arm was measured after the isolated 11th AP and not the 10th, and
`fig10bd-be-async-charge` lacks only its 320 Hz data; it also asked that the
high KCl assumption be checked. In reply the code was fixed, the onset claims
became not reproduced, the three claims were blocked, fig10bd was blocked for
missing data with its other parts printed, `async-charge-epi-vs-160`
went from partially to not reproduced (p 0.0934), the 16 outcomes on
interneuron to PC pairs were marked as assumed with a per-pair check, and
questions on the fig4c and fig5c criteria and on the onset rules went to a
reader in `questions/crcns-hc-7.yaml`, written after the answer run, so they
are unanswered. Round 2 agreed with all 44, found that the fig11 text came from
a different run than the one saved (a tau_f p of 0.0339 where the output
printed 0.026, and a test error said to be finite that was infinite), noted
that onset rule (b) cannot tell asynchronous release from summation at 160 Hz,
and counted 21 assumed outcomes where the record marks 16; in reply the fig11
fits were repeated with three more seeds and the best of 16 starting points,
which kept every fig11 outcome, a sensitivity test of the high KCl assumption
was added and the text was corrected. The author's run took about 1.5 h; the
notebook ran in 342 s at first, 431 s after the author-answers run, 306 s after
round 1 and 1378 s after round 2, and nothing failed in the final runs. The
untracked entries in the repository root were left alone.

The current-step recordings of the 67 interneurons (Fig. 2, Tables 1 and 2),
the connectivity tests with unconnected pairs (Fig. 3), the spontaneous IPSCs
(Fig. 12) and the field potential and optogenetic recordings (Fig. 13A, C) are
not in the data set, which is described as holding the paired recordings only.
The data set holds 7 PV+BC, 8 AAC, 12 CCK+BC and 7 CCK+DTI to PC and 14 PV+BC
to PV+BC pairs, fewer than the paper's 8, 9, 14, 8 and 16, and the CCK+ to CCK+
pairs were recorded only with 10, 40 and 160 Hz trains, with no RIP recording,
1 Hz train or 320 Hz train, so their single-AP uIPSCs (Fig. 8) and 320 Hz
charges (Fig. 10B) cannot be measured. The pairs are not labelled by pipette
solution (high KCl, or low KCl with CsCl), which the comparisons of Fig. 7
need; the pair counts do not exceed the paper's high KCl counts, but in CCK+BC
to PC pairs latency rises with the holding current (rho 0.58, p 0.048), one
sign against the assumption. The stimulation timings differ from the data
descriptor and the paper: RIP bursts are at 222 Hz, not 160 Hz, the EPI burst
is at 147 and 303 Hz, not 160 and 320 Hz, and the single AP precedes the bursts
by 1.3 s, not 1 s. The `_EPA` tables use a code AR, not described in the
descriptor, that cuts off the mean row of every CCK+BC and CCK+DTI to PC EPI
table from some AP on; read as the onset of asynchronous release, it gives a
CCK+BC median of 12 against the paper's 11, but it was shown only. The block
the descriptor calls Relative ampl. holds amplitudes in pA, and the order of
the recovery intervals across sweeps is not documented.
`Experiments_description.txt` mislabels two recordings, names eight files that
are not in the zip, leaves 20 recordings unnamed, lists no PV+BC to AAC pairs
and numbers the interneuron to PC pairs differently from the folders. Three
recordings have a header but no sweeps, three have sweeps but no `_EPA` table,
two `_EPA` tables hold column labels in place of the mean values, several list
fewer sweeps than the raw data without a note, and a few mean rows differ from
the mean of their own per-sweep values by up to 38 pA. The files carry no
animal or slice identifiers. The Results say seven of eight CCK+DTI to PC pairs
did not transmit for a single AP or an AP after RIP, and also that four of
eight responded at 1 to 40 Hz or to RIP. Questions are put to the paper's
authors: how the onset of asynchronous release was determined and whether the
AR code marks it; which APs and windows gave the single-AP uIPSCs of the CCK+
interneuron pairs; and whether the recovery half-time of Fig. 13B was fitted
with the plateau fixed or free, and whether it is tau or tau ln 2.

The author's points on the protocol: it has no rule for when none of the claims
file's readings can be run on the data, so a reading from the paper's protocol
passage was added and marked assumed; the false-positive rule is written for a
chance level the paper states, and here was applied by analogy; there is no
slot for the authors' own scoring inside the data set, so the AR marks were
shown as a variant only; it does not say what `measured` holds when no reading
matches; some criteria are fixed counts of 8 where the data hold 7 pairs, and
each was judged as written; blocking every claim that depends on a blocked
claim takes out fig10 claims whose other parts could have been tested; results
cannot be broken down by animal without identifiers, so recording days were
reported; and CRCNS offers no published version to pin, so unversioned and the
MD5 sum were recorded.
