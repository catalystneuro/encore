# 000673, Daume et al. 2024

Thirteen claims reproduced (five on an assumption), five partially, six not
reproduced (three on an assumption) and 33 blocked, one as
`methods_underspecified` and 32 as other. The first verification round agreed
with 41 of the 57 outcomes as they stood and the second with 49, and the second
revision proposed two changes, so a third round reviewed those two and agreed
with both. It pins version 0.240118.2135, which the paper's reference 59 cites;
in the latest version, 0.250122.0110, each of the 44 files has a new asset a few
hundred kilobytes smaller, and the contents were not compared. The paper,
Daume, Kaminski, Schjetnan, Salimpour, Khan, Kyzar, Reed, Anderson, Valiante,
Mamelak and Rutishauser, "Control of working memory by phase-amplitude coupling
of human hippocampal neurons" in Nature, records single neurons and microwire
LFPs in the hippocampus, amygdala, pre-SMA, dACC and vmPFC of 36 patients
during a Sternberg task of 70 load 1 and 70 load 3 trials, and relates
theta-gamma phase-amplitude coupling (PAC) in the hippocampus to category
neurons, PAC neurons, spike-field coherence (SFC) and memory load; the dataset
holds the 44 sessions as NWB files with spikes, LFP and trials tables. The
claims were written from the version of record (PMC11078732) with its
Supplementary Information, and from the paper's linked code
(SBCAT-release-NWB at commit a25e8cc3), which holds sample code only; the
attempt read that code for method details, listed under `inputs`. The cohort
counts (44 sessions, 1,454 units, 1,922 LFP channels), the three behaviour
claims, `category-no-rt-effect`, `fig2a-theta-gamma-pac`,
`fig2c-hippocampus-load` and `edf3a-kappa-load` reproduce, as do
`edf2b-hippocampus-load-patients` and `edf3f-raw-mi-load` on artefact reading
(a), `fig3d-category-correct-incorrect` on rates as % of baseline,
`edf3e-nesting` on windows aligned on gamma peaks (105 of 144 channels nested,
against 9 of 144 aligned on amplitude maxima) and
`fig3h-pac-category-firing` on artefact reading (a). Partial are
`category-cell-counts`, the pre-SMA's 18 neurons also exceeding chance (p =
0.010); `fig3b-persistent-activity` and `edf4b-persistent-activity-by-area`,
preferred against non-preferred holding in % of baseline and not in Hz;
`fig2b-pac-channel-proportions`, the pre-SMA having 17 significant channels
against the paper's 5; and `pac-neuron-counts`, 8 of 269 hippocampal and 5 of
422 amygdala neurons qualifying against 79 of 212 and 163 of 358, though above
the shuffles (p = 0.005). Not reproduced are the three claims of no load
effect outside the hippocampus (`fig2c-no-load-effect-other-areas`,
`edf2c-low-gamma-no-load-effect`, `tables1-slow-fast-theta`), the pre-SMA and
in some readings the amygdala or dACC differing between loads, and on
assumptions `fig3c-category-load` (% of baseline, p = 0.77; in Hz the claim
holds), `edf3-hippocampus-pac-controls` (high-gamma power and gamma peak
frequency higher in load 3) and `methods-spectral-slope` (2 to 150 Hz, a
difference of 0.004 with p = 0.0073). `fig2f-rt-single-trial-pac` is blocked
as `methods_underspecified`, the two readings of single-trial PAC disagreeing on
the RT scales that fit Table S2. Of the 32 blocked as other, six need SFC,
which was not run (`fig3f-gamma-sfc-preferred`, `fig3g-gamma-sfc-anova`,
`edf5c-theta-sfc-null`, `edf5d-sfc-high-gamma-power`,
`edf5fg-gamma-sfc-all-channels-patients` and panels f and g of
`edf8fgh-frontal-controls`), and the other 26 rest on the PAC neuron
selection, on SFC or on the decoding, which was not run. The author's first
run gave 12 reproduced, five partially, six not reproduced and 34 blocked, with
edf3, edf8fgh, the five SFC claims and fig3h blocked as `too_large`. The author
asked a reader nothing, so the answer and author-answers runs changed nothing.
Round 1 disagreed with 16 outcomes, fig3c and 15 blocked claims, 6 of which it
judged from results printed in the notebooks and 9 it found testable from the
archive; in reply the missing edf3 controls were run in a new notebook and
fig3h was tested (both then not reproduced), the reading (b) comodulogram was
added so that fig2a no longer rests on an assumption, the paper's
`artif_trials.mat` was found to support artefact reading (a), the pre-SMA
channels, the nesting windows and the units-table columns were printed, and a
reader question on the edf3 V test was filed; the disagreements on fig3c and
on five PAC neuron claims, which the record keeps blocked on 8 and 5 neurons,
are recorded. Round 2 disagreed with fig2f and fig3h, whose GLMs coded load 1
as the reference where Tables S2 and S3 code load 3, and with the six SFC
claims, which it would block as not run and not as too large, and found
sentences the outputs did not support (the "opposite sign" of the fig3h term,
Table S2 giving RT in ms, the SFC timings, an RT maximum of 16.8 s taken from
the wrong data frame, file indices given as session numbers, "but one" in the
PAC neuron counts, -3.26 for -3.27 and the README's run times), all corrected.
The second revision moved the SFC claims to other, refitted with load 3 as the
reference and proposed reproduced for fig3h and `methods_underspecified` for
fig2f; round 3 agreed with both, asking that fig2f be marked assumed, which
the schema does not allow on a blocked outcome, so a deviation says it rests on
artefact reading (a), and a reader question asks whether Table S2's PAC
estimate (-49.07) fixes the reading under which fig2f would be not reproduced.
The author's run went from 08:09 to about 10:35 UTC with nothing failing in
the final run, the notebooks taking 3.3, 20 and 8.2 min. In the author-answers
run the LFP notebook took 35 min, over the 30-minute limit, which the report
puts down to a slower machine, and after round 1 it took 42 min and failed the
limit again; after round 2 the four notebooks took 4.3, 44, 23 and 11.4 min
and at the end 3.1, 42, 21 and 9 min, passing because `tools/entry.py` in the
working tree already had the limit raised to 60 minutes, a change left
untouched with the other `tools/` edits.

The files do not mark the LFP trials, channels or regions that the paper's
artefact rejection removed, most of it by visual inspection (20.4 +/- 13.9
trials per wire, and whole wires or regions), and the remaining channels change
several results: the automated rules of the Methods remove 11.4% (on the
epochs) or 25.9% (on whole trials) of trials, the pre-SMA has 17 channels with
significant theta-high-gamma PAC where the paper has 5, and they decide three
claims of absence. 269 hippocampal and 422 amygdala neurons have LFP in their
bundle, where the paper analysed 212 and 358. The paper's code ships the
rejected trials of one example channel (artif_trials.mat, sub-26 session 1,
channel 33, 17 trials); reading (a) removes 4 there, all among them, and
reading (b) removes 9, 5 of which the paper kept. The files do not identify the
microwire bundles that the analyses pair neurons and LFPs within: every wire is
its own ElectrodeGroup, the location names only area and hemisphere, some
locations of a session hold up to 15 wires and 26 of 285 location groups have
more than one set of coordinates, so bundles were inferred from location and
coordinates. Spike times are not sorted in four units of two files: in sub-13
ses-1 units 6, 14 and 15 jump back by up to 1,319 to 1,339 s (units 6 and 15
once, unit 14 three times), as if two spike trains had been concatenated, and
in sub-22 ses-2 unit 10 steps back 24 times by up to 3.3 ms; the analysis sorts
them. The maintenance period lasts 2.53 to 3.20 s in the trials table against
2.55 to 2.85 s in the Methods, the blank between pictures in load 3 lasts 0.011
to 0.341 s against 17 to 200 ms, and RTs reach 74.2 s (69 trials above 10 s).
sub-20 has no LFP. Questions are put to the paper's authors: whether the
firing-rate tests of Fig. 3b-d and Fig. 4 use rates in Hz or the percentage
change from baseline, over what span the automated artefact rejection works,
whether the nesting windows are centred on gamma amplitude maxima or gamma
peaks, over what range and with what spectral estimate the spectral slope was
compared, how single-trial PAC is computed and whether RT is transformed in
Table S2, and which family the FDR correction of the PAC neuron selection
covers, run as in plot_PAC_neuron.m giving 8 and 5 neurons against 79 and 163.

The author's points on the protocol: with 57 claims the five-hour limit forces
choices the protocol does not rank, and what needs no SFC or decoding was
tested first; the protocol asks for every reading while a notebook must stay
under 30 minutes, and the fig2a comodulogram was first run under artefact
reading (a) only; `blocked_by` has no category for a claim not started for
lack of run time or a selection that gives too few units, and `too_large` and
`other` were used; it does not say whether a claim of absence with parts run
and parts not run is blocked or graded from the parts run, and edf3 and
edf8fgh were blocked with the partial results in the notes; one reading in the
claims file is logically inverted, a significant V test for edf3 meaning no
shift; and `entry.py` has no single-notebook option, so notebook 1 was
re-executed alone with the same environment and nbconvert command.
